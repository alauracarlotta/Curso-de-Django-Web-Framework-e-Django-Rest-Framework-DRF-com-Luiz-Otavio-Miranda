from django.test import TestCase
from django.urls import resolve, reverse

from apps.recipes import views
# from apps.recipes.models import Recipe, Category, auth_models
from apps.recipes.models import Recipe, Category, User


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

    def test_home_template_loads_recipes(self):
        # category = Category(name='Fast Food')
        # category.save()
        # category.full_clean()
        category = Category.objects.create(name='Datas Especiais')
        author = User.objects.create_user(
            first_name='Maria',
            last_name='Antônia',
            username='mariaantonia',
            password='Varekai**963,',
            email='maria@antonia.com',
        )
        recipe = Recipe.objects.create(
            title='Receita de Sorvete',
            description='Receita muito boa, caseira, barata e que rende horrores', # noqa
            slug='receita-de-sorvete',
            preparation_time=60,
            preparation_time_unit='minutos',
            servings=20,
            servings_unit='pessoas',
            preparation_step='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio illum voluptate neque , voluptas maxime sit itaque, corrupti debitis saepe repellat rerum, eveniet beatae odio at dolorem fugiat quam non vero!', # noqa
            preparation_step_is_html=False,
            is_published=True,
            category=category,
            author=author,
        )
        assert 1 == 1

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
