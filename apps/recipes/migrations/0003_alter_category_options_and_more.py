# Generated by Django 5.1.3 on 2024-12-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_category_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Caterory', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='severings',
            new_name='servings',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='severings_unit',
            new_name='servings_unit',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/'),
        ),
    ]
