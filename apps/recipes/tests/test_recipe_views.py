from django.urls import resolve, reverse
from apps.recipes import views
from .test_recipe_base import RecipeTestBase
from unittest import skip
# from apps.recipes.models import Recipe, Category, auth_models


class RecipeViewsTest(RecipeTestBase):
    # ----------------------------------
    #               HOME
    # ----------------------------------
    # view function is correct
    # ...função da view está correta
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    # view status code == 200
    # ... status code da view é 200
    def test_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # error msg template == 404
    # ... mensagem de erro no template é 404 - 'No recipes found here'
    @skip('WIP')
    def test_home_template_shows_no_recipes_found_if_no_recipes_404(self):
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )
        # TODO: Escrever mais coisas no test
        self.fail('...Para que eu termine de digitá-lo.')

    # correct template returns
    # ... retorna o template correto
    def test_home_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # home loads recipes
    # ... home carrega receita no template
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

    # ----------------------------------
    #               CATEGORY
    # ----------------------------------
    # view function is correct
    def test_category_view_function_is_correct(self):
        view = resolve(
            reverse('category', kwargs={
                'category_id': 1
            })
        )
        self.assertIs(view.func, views.category)

    # view status code == 404
    def test_category_view_returns_404_if_no_category_found(self):
        response = self.client.get(reverse('category', kwargs={
                'category_id': 9999
            }))
        self.assertEqual(response.status_code, 404)

    # ----------------------------------
    #               DETAILS
    # ----------------------------------
    # view function is correct
    def test_details_view_function_is_correct(self):
        view = resolve(
            reverse('recipe', kwargs={
                'id': 1
            })
        )
        self.assertIs(view.func, views.recipes)

    # view status code == 404
    def test_detail_view_returns_404_if_no_detail_found(self):
        response = self.client.get(reverse('recipe', kwargs={
                'id': 9999
            }))
        self.assertEqual(response.status_code, 404)
