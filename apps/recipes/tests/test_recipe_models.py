from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelsTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_default(self):
        recipe = Recipe(
            title='Título da Receita',
            description='Descrição da Receita',
            slug='receita-slug',
            preparation_time=60,
            preparation_time_unit='Minutos',
            servings=4,
            servings_unit='Porções',
            preparation_step='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio illum voluptate neque , voluptas maxime sit itaque, corrupti debitis saepe repellat rerum, eveniet beatae odio at dolorem fugiat quam non vero!', # noqa
            category=self.make_category(name='Categoria teste default'),
            author=self.make_author(username='judite'),
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    """
    def test_from_test(self):
        recipe = self.recipe
        response = self.client.get(
            reverse('home')
        )
        ...
    """

    def test_recipe_title_raises_error_if_title_has_more_65_chars(self):
        # context manager do próprio unittest
        self.recipe.title = 'a' * 81

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
        """ self.recipe.save()
        self.fail(self.recipe.title) """

    @parameterized.expand([
        ('title', 80),
        ('description', 1000),
        ('preparation_time_unit', 80),
        ('servings_unit', 80),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        # fields = [
        #     ('title', 80),
        #     ('description', 1000),
        #     ('preparation_time_unit', 80),
        #     ('servings_unit', 80),
        # ]

        # for field, max_length in fields:
        #     with self.subTest(field=field, max_length=max_length):
        #         setattr(self.recipe, field, 'a' * (max_length + 0))
        #         with self.assertRaises(ValidationError):
        #             self.recipe.full_clean()
        setattr(self.recipe, field, 'a' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand([
        ('preparation_step_is_html', False),
        ('is_published', False),
    ])
    def test_recipe_fields_default(self, field, *args):
        setattr(self.recipe, field, '')
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_step_is_html_is_false(self):
        # não podemos usar a mesma do setup, isso porque como deixamos os
        # valores defaults, estariamos testando o motor do django e não a
        # funcionalidade em si.
        recipe = self.make_recipe_no_default()
        self.assertFalse(
            recipe.preparation_step_is_html,
            msg='Recipe preparation_step_is_html is not False'
        )

    def test_recipe_is_published_is_false(self):
        # não podemos usar a mesma do setup, isso porque como deixamos os
        # valores defaults, estariamos testando o motor do django e não a
        # funcionalidade em si.
        recipe = self.make_recipe_no_default()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False'
        )
