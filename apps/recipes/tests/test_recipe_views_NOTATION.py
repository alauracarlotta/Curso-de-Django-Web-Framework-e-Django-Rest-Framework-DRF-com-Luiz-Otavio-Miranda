from unittest import skip
from django.shortcuts import render
from django.test import TestCase
from django.urls import path, reverse, resolve

from apps.recipes import views
from apps.recipes.models import Recipe

"""
O QUE É TESTADO NO DJANGO?
    => _T_U_D_O_!!
        * URLs  --|
        * VIEWs --| (inside-out)
        * TEMPLATES (teste funcional, usar selenium => outside-in)
"""

# =============================================================================

"""
PARTE IMPORTANTE:
A CADA EXECUÇÃO DE TESTE, O PYTEST CRIA E DESTROI UM BANCO DE DADOS.
VEREMOS QUE, PARA ALGUNS TESTES SERÁ NECESSÁRIO A CRIAÇÃO DE UM ITEM. NOTE*3
"""

# =============================================================================

""" NOTE*4: Lembrar sempre do namespacing!!! """
""" recipe_home """

# =============================================================================

""" O PRIMEIRO TESTE SEMPRE DEVE FALHAR """

# =============================================================================

"""
NOTE*5
resolve() =>
    pode ser usada para resolver caminhos de URL para as funções de
    visualização correspondentes.

reverse() =>
    É semelhante à urltag template que é usada para converter URL com namespace
    em padrão de URL real.
"""
# reverse => concatena e monta o path
# resolve => Qual função está sendo usada por uma URL + path

# <<< Por exemplo >>>


@skip('Exemplo de reverse') # noqa
def test_list_reverse():
    # cheeses:list should reverse to /cheeses/.
    assert reverse('cheeses:list') == '/cheeses/'  # noqa


@skip('Exemplo de resolve') # noqa
def test_list_resolve():
    # /cheeses/ should resolve to cheeses:list.
    assert resolve('/cheeses/').view_name == 'cheeses:list'  # noqa

# =============================================================================

# imports na linha 1

# =============================================================================
# =============================================================================
    # test_recipe_urls
# =============================================================================
# =============================================================================


class RecipeUrlsNOTATIONTest(TestCase):
    # TESTE 1:
    # Instalamos o pytest. Eles está funcionando?
    def test_pytest_esta_ok(self):
        # NOTE*2:
        # Já o print mostra no terminal tanto em caso de sucesso quanto em caso
        # de falha (isso, porque nosso arquivo pytest.ini tem o -rP em addopts
        print('Olá mundo de teste no terminal.')
        assert 1 == 1, '1 é igual a 1'  # (=> AssertionError)

        # NOTE*1:
        # pós vírgula, a msg no terminal aparecerá somente se o teste der erro
        # caso contrário, a msg não aparece.

    # TESTE 2:
    # O retorno da url está sendo o esperado? (*HOME*)
    def test_url_da_home_da_receita_esta_correta(self):  # NOTE*4
        url_home = reverse('home')  # NOTE*5
        self.assertEqual(url_home, '/')
        # url_home é igual a '/'?

    # TESTE 3:
    # O retorno da url está sendo o esperado? (*CATEGORY*)
    def test_url_da_categoria_da_receita_esta_correta(self):
        # url_categoria = reverse('category', args=(1,))
        url_categoria = reverse('category', kwargs={'category_id': 1})  # =>
        # category_id => Como o parâmetro passado em urls.py
        self.assertEqual(url_categoria, '/category/1/')
        # url_categoria é igual a '/category/1/'?

    # TESTE 4:
    # O retorno da url está sendo o esperado? (*DETAILS*)
    def test_url_do_detalhe_da_receita_esta_correta(self):
        url_detalhe = reverse('recipe', kwargs={'id': 1})  # =>
        # id => Como o parâmetro passado em urls.py
        self.assertEqual(url_detalhe, '/recipe/1/')
        # url_detalhe é igual a '/recipe/1/'?

# =============================================================================
# =============================================================================
    # test_recipe_views
# =============================================================================
# =============================================================================


"""
    Atualmente, as nossas views estão sendo escritas no formato
    FUNCTION BASED VIEWS. (classic based views)
"""


# EX: (VIEWS)
def home(request):  # NOTE*7...
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('title')

    return render(
        request,
        'recipes/pages/home.html',  # ... NOTE*7
        context={
            'recipes': recipes
        }
    )

# EX: (URLS)
urlpatterns = [  # noqa
    path(
        '',  # NOTE*6 ...
        views.home,  # ...NOTE*6
        name='home'
    ),
    path(
        'category/<int:category_id>/',
        views.category,
        name='category'
    ),
    path(
        'recipe/<int:id>/',
        views.recipes,
        name='recipe'
    ),
]

# NOTE*6 => Essa url está renderizando essa view?
# NOTE*7 => Essa função está renderizando esse template?

# =============================================================================


class RecipesViewsTest(TestCase):
    # TESTE 5:
    # teste de detalhe de código de implemtação. Suponhamos que:
    #       haja uma outra função na views e ela é chamada no urls como 'home2'
    #       quando testarmos, veremos que a função que está sendo chamada é uma
    #       função incorreta.
    # A função da view que eu pedi é a que está sendo renderizada?
    def test_funcao_da_view_home_esta_correta(self):
        view_home = resolve(reverse('home'))
        # Em view_home.(function_variables).func retorna qual função view está
        # sendo chamada. Utilizamos o assertIs para verificar se é o mesmo
        # local de memória. (is != == (is verifica local em memória) e
        # (== verifica iguadade de valor))
        self.assertIs(view_home.func, views.home)

# =============================================================================

    """
        NOTE*8 => Um teste verifica apenas uma coisa, ele poderá ter mais de
        uma asserção, porém somente se for pra testar aquela coisa.
    """

# =============================================================================

    # TESTE 8:
    # STATUS_CODE: Para conseguirmos testar o status_code do retorno da view,
    # teriamos que fazer uma request para poder obter uma response. utilizando
    # as ferramentas do django, podemos pegar o self.client.__algumacoisa__
    # para fazer um.get, .post e afins.
    def test_status_code_da_view_home_retorna_200_OK(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # TESTE 9:
    # TEMPLATE USED: Para verificarmos se o template renderizado, foi o
    # solicitado.
    def test_view_home_carrega_o_template_correto(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

# =============================================================================
    # @fixture => criar dados para os testes
# =============================================================================

    # TESTE 10:
    # Mesmo tendo receitas, o teste é concluído pois o terminal cria uma base
    # de dados local para cada teste e emseguida deleta o mesmo. Para termos um
    # teste eficiente, precisaremos criar uma receita dentro da função teste.
    def test_mostra_mensagem_de_erro_no_template_da_home_se_nao_encontrar_nenhuma_receita(self):  # noqa
        response = self.client.get(reverse('home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    # TESTE 6:
    # A função da view que eu pedi p/ categoria é a que está sendo renderizada?
    def test_funcao_da_view_das_categorias_esta_correta(self):
        view_categoria = resolve(reverse('category', kwargs={
            'category_id': 1
        }))
        self.assertIs(view_categoria.func, views.category)

    # TESTE 11:
    # Sem receitas criadas dentro do contento do teste, o status retornará
    # sempre 404 pois o terminal utiliza uma base de dados local ao invés do
    # 'admin'.
    def test_funcao_da_view_das_categorias_retorna_404_se_nao_encontrar_receitas(self):  # noqa
        response = self.client.get(reverse('category', kwargs={
            'category_id': 99999
        }))
        self.assertEqual(response.status_code, 404)

    # TESTE 7:
    # A função da view que eu pedi p/ categoria é a que está sendo renderizada?
    def test_funcao_da_view_de_detalhes_da_receita_esta_correta(self):
        view_detalhe = resolve(reverse('recipe', kwargs={'id': 1}))
        self.assertIs(view_detalhe.func, views.recipes)

    # TESTE 12:
    # NOTE mesmo caso TESTE 11
    def test_funcao_da_view_de_detalhes_retorna_404_se_nao_encontrar_receitas(self):  # noqa
        response = self.client.get(reverse('recipe', kwargs={
            'id': 9999
        }))
        self.assertEqual(response.status_code, 404)
