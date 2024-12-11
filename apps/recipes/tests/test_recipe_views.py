from django.urls import resolve, reverse
from apps.recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip
# from apps.recipes.models import Recipe, Category, auth_models


class RecipeViewsTest(RecipeTestBase):
    # HOME
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    def test_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    @skip('WIP')
    def test_home_template_shows_no_recipes_found_if_no_recipes_404(self):
        response = self.client.get(reverse('home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )
        # TODO: Escrever mais coisas no test
        self.fail('...Para que eu termine de digitá-lo.')

    def test_home_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_template_loads_recipes(self):
        """ NEED A RECIPE FOR THIS TEST - create the recipe """
        """ ...PRECISA DE UMA RECEITA PARA ESSE TESTE - cria a receita """
        self.make_recipe(
            title='Receita de Sorvete',
            category_data={
                'name': 'Fast Food'
                }
        )
        response = self.client.get(reverse('home'))
        response_recipes = response.context['recipes']
        response_context = response.content.decode('utf-8')

        """ verify if recipe was created """
        """ ... verifica se uma receita foi criada """
        self.assertEqual(len(response.context['recipes']), 1)

        """ verify recipe title was created as register title """
        """ ...verifica se a receita criada foi com o título regsitrado """
        self.assertEqual(response_recipes.first().title, 'Receita de Sorvete')

        """ Check if one recipe exists """
        """ ... Checa se 1 receita é encontrada no códogp do template """
        self.assertIn('Receita de Sorvete', response_context)

    # CATEGORY
    def test_category_view_function_is_correct(self):
        view = resolve(
            reverse('category', kwargs={
                'category_id': 1
            })
        )
        self.assertIs(view.func, views.category)

    def test_category_view_returns_404_if_no_category_found(self):
        response = self.client.get(reverse('category', kwargs={
                'category_id': 9999
            }))
        self.assertEqual(response.status_code, 404)

    # DETAILS
    def test_details_view_function_is_correct(self):
        view = resolve(
            reverse('recipe', kwargs={
                'id': 1
            })
        )
        self.assertIs(view.func, views.recipes)

    def test_detail_view_returns_404_if_no_detail_found(self):
        response = self.client.get(reverse('recipe', kwargs={
                'id': 9999
            }))
        self.assertEqual(response.status_code, 404)
