from django.test import TestCase
from django.urls import resolve, reverse

from apps.recipes import views


class RecipeViewsTest(TestCase):

    # ----------------------------------
    #               HOME
    # ----------------------------------
    # view function is correct
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    # view status code == 200
    def test_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # error msg template == 404
    def test_home_template_shows_no_recipes_found_if_no_recipes_404(self):
        response = self.client.get(reverse('home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    # correct template returns
    def test_home_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

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
