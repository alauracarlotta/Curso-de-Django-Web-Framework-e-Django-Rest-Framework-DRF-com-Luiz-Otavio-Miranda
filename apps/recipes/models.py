# from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=80)
    """ CAKES = 'BOLOS', 'BOLOS'
    PIES = 'TORTAS', 'TORTAS'
    DESSERT = 'SOBREMESA', 'SOBREMESA'
    FAST = 'RÁPIDAS', 'RÁPIDAS'
    SPECIAL_DATES = 'DATAS_ESPECIAIS', 'DATAS_ESPECIAIS'
    MEATS = 'CARNES', 'CARNES'
    CHICKEN = 'AVES', 'AVES'
    FISH_AND_SEAFOOD = 'PEIXES_E_FRUTOS_DO_MAR', 'PEIXES_E_FRUTOS_DO_MAR'
    SALADS_E_SAUCES = 'SALADAS_E_MOLHOS', 'SALADAS_E_MOLHOS'
    SOUPS = 'SOPAS', 'SOPAS'
    PASTA = 'MASSAS', 'MASSAS'
    DRINKS = 'BEBIDAS', 'BEBIDAS'
    HEALTHY_EATING = 'COMIDA_SAUDÁVEL', 'COMIDA_SAUDÁVEL'
    SINGLE_DISH = 'PRATO_ÚNICO', 'PRATO_ÚNICO'
    OTHERS = 'OUTROS', 'OUTROS' """

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Caterory'
        verbose_name_plural = 'Categories'
        ordering = ['-id']


class Recipe(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=80)  # futuro select
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=80)  # futuro select
    # ingredients = models.IntegerField()
    # ingredients_unit = models.CharField(max_length = 80) # futuro select
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default=''
    )
    # category = models.CharField(max_length = 100, choices = Category.choices)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    author = models.ForeignKey(
        # auth_models.User, on_delete=models.SET_NULL, null=True, blank=True,
        User, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )

    def __str__(self):
        return f'{self.title} by {self.author}'
