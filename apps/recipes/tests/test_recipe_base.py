from django.test import TestCase
from apps.recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Categoria'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='Nome',
        last_name='Sobrenome',
        username='username',
        password='Varekai**963,',
        email='email@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        title='Título da Receita',
        description='Descrição da Receita',
        slug='receita-slug',
        preparation_time=60,
        preparation_time_unit='Minutos',
        servings=4,
        servings_unit='Porções',
        preparation_step='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio illum voluptate neque , voluptas maxime sit itaque, corrupti debitis saepe repellat rerum, eveniet beatae odio at dolorem fugiat quam non vero!', # noqa
        preparation_step_is_html=False,
        is_published=True,
        category_data=None,
        author_data=None,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create( # noqa
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_step=preparation_step,
            preparation_step_is_html=preparation_step_is_html,
            is_published=is_published,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )
