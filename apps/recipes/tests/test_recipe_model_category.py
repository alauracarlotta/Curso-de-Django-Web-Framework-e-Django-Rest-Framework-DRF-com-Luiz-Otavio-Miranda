from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeCategoryModelsTest(RecipeTestBase):
    def setUp(self):
        # self.category = self.make_category()
        self.category = self.make_category(
            name='Category Test'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_mopdel_name_max_length_is_65_chars(self):
        self.category.name = 'a' * 81
        with self.assertRaises(ValidationError):
            self.category.full_clean()
