# Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda

Curso de Django Web Framework e Django Rest Framework (DRF) com Luiz Otavio Miranda pela plataforma Udemy

➜ python manage.py shell
Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from apps.recipes.models import Recipe, Category
>>> rec = Recipe.objects.all()
>>> cat = Category.objects.all()
>>> rec
<QuerySet [<Recipe: Bolo de Cenoura by admin>, <Recipe: Bolo de Banana by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta de Limão by admin>, <Recipe: Torta Holandesa by admin>]>
>>> cat
<QuerySet [<Category: Tortas>, <Category: Doces>, <Category: Carnes>, <Category: Aves>, <Category: Bolos>]>
>>> rec.__dir__
<built-in method __dir__ of QuerySet object at 0x7c241442ef00>
>>> print(rec.__dir__)
<built-in method __dir__ of QuerySet object at 0x7c241442ef00>
>>> print(list(rec.__dir__))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not iterable
>>> dir(rec)
['__aiter__', '__and__', '__bool__', '__class__', '__class_getitem__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '__xor__', '_add_hints', '_annotate', '_batched_insert', '_chain', '_check_bulk_create_options', '_check_operator_queryset', '_check_ordering_first_last_queryset_aggregation', '_clone', '_combinator_query', '_db', '_defer_next_filter', '_deferred_filter', '_earliest', '_extract_model_params', '_fetch_all', '_fields', '_filter_or_exclude', '_filter_or_exclude_inplace', '_for_write', '_has_filters', '_hints', '_insert', '_iterable_class', '_iterator', '_known_related_objects', '_merge_known_related_objects', '_merge_sanity_check', '_next_is_sticky', '_not_support_combined_queries', '_prefetch_done', '_prefetch_related_lookups', '_prefetch_related_objects', '_prepare_for_bulk_create', '_query', '_raw_delete', '_result_cache', '_sticky_filter', '_update', '_validate_values_are_expressions', '_values', 'aaggregate', 'abulk_create', 'abulk_update', 'acontains', 'acount', 'acreate', 'adelete', 'aearliest', 'aexists', 'aexplain', 'afirst', 'aget', 'aget_or_create', 'aggregate', 'ain_bulk', 'aiterator', 'alast', 'alatest', 'alias', 'all', 'annotate', 'as_manager', 'aupdate', 'aupdate_or_create', 'bulk_create', 'bulk_update', 'complex_filter', 'contains', 'count', 'create', 'dates', 'datetimes', 'db', 'defer', 'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'none', 'only', 'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list']
>>> from pprint import pprint
>>> pprint(dir(rec))
['__aiter__',
 '__and__',
 '__bool__',
 '__class__',
 '__class_getitem__',
 '__deepcopy__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__or__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '__xor__',
 '_add_hints',
 '_annotate',
 '_batched_insert',
 '_chain',
 '_check_bulk_create_options',
 '_check_operator_queryset',
 '_check_ordering_first_last_queryset_aggregation',
 '_clone',
 '_combinator_query',
 '_db',
 '_defer_next_filter',
 '_deferred_filter',
 '_earliest',
 '_extract_model_params',
 '_fetch_all',
 '_fields',
 '_filter_or_exclude',
 '_filter_or_exclude_inplace',
 '_for_write',
 '_has_filters',
 '_hints',
 '_insert',
 '_iterable_class',
 '_iterator',
 '_known_related_objects',
 '_merge_known_related_objects',
 '_merge_sanity_check',
 '_next_is_sticky',
 '_not_support_combined_queries',
 '_prefetch_done',
 '_prefetch_related_lookups',
 '_prefetch_related_objects',
 '_prepare_for_bulk_create',
 '_query',
 '_raw_delete',
 '_result_cache',
 '_sticky_filter',
 '_update',
 '_validate_values_are_expressions',
 '_values',
 'aaggregate',
 'abulk_create',
 'abulk_update',
 'acontains',
 'acount',
 'acreate',
 'adelete',
 'aearliest',
 'aexists',
 'aexplain',
 'afirst',
 'aget',
 'aget_or_create',
 'aggregate',
 'ain_bulk',
 'aiterator',
 'alast',
 'alatest',
 'alias',
 'all',
 'annotate',
 'as_manager',
 'aupdate',
 'aupdate_or_create',
 'bulk_create',
 'bulk_update',
 'complex_filter',
 'contains',
 'count',
 'create',
 'dates',
 'datetimes',
 'db',
 'defer',
 'delete',
 'difference',
 'distinct',
 'earliest',
 'exclude',
 'exists',
 'explain',
 'extra',
 'filter',
 'first',
 'get',
 'get_or_create',
 'in_bulk',
 'intersection',
 'iterator',
 'last',
 'latest',
 'model',
 'none',
 'only',
 'order_by',
 'ordered',
 'prefetch_related',
 'query',
 'raw',
 'resolve_expression',
 'reverse',
 'select_for_update',
 'select_related',
 'union',
 'update',
 'update_or_create',
 'using',
 'values',
 'values_list']
>>> rec.id
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'id'
>>> pprint(dir(rec.all))
['__call__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__func__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__self__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']
>>> pprint(dir(rec))
['__aiter__',
 '__and__',
 '__bool__',
 '__class__',
 '__class_getitem__',
 '__deepcopy__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__or__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '__xor__',
 '_add_hints',
 '_annotate',
 '_batched_insert',
 '_chain',
 '_check_bulk_create_options',
 '_check_operator_queryset',
 '_check_ordering_first_last_queryset_aggregation',
 '_clone',
 '_combinator_query',
 '_db',
 '_defer_next_filter',
 '_deferred_filter',
 '_earliest',
 '_extract_model_params',
 '_fetch_all',
 '_fields',
 '_filter_or_exclude',
 '_filter_or_exclude_inplace',
 '_for_write',
 '_has_filters',
 '_hints',
 '_insert',
 '_iterable_class',
 '_iterator',
 '_known_related_objects',
 '_merge_known_related_objects',
 '_merge_sanity_check',
 '_next_is_sticky',
 '_not_support_combined_queries',
 '_prefetch_done',
 '_prefetch_related_lookups',
 '_prefetch_related_objects',
 '_prepare_for_bulk_create',
 '_query',
 '_raw_delete',
 '_result_cache',
 '_sticky_filter',
 '_update',
 '_validate_values_are_expressions',
 '_values',
 'aaggregate',
 'abulk_create',
 'abulk_update',
 'acontains',
 'acount',
 'acreate',
 'adelete',
 'aearliest',
 'aexists',
 'aexplain',
 'afirst',
 'aget',
 'aget_or_create',
 'aggregate',
 'ain_bulk',
 'aiterator',
 'alast',
 'alatest',
 'alias',
 'all',
 'annotate',
 'as_manager',
 'aupdate',
 'aupdate_or_create',
 'bulk_create',
 'bulk_update',
 'complex_filter',
 'contains',
 'count',
 'create',
 'dates',
 'datetimes',
 'db',
 'defer',
 'delete',
 'difference',
 'distinct',
 'earliest',
 'exclude',
 'exists',
 'explain',
 'extra',
 'filter',
 'first',
 'get',
 'get_or_create',
 'in_bulk',
 'intersection',
 'iterator',
 'last',
 'latest',
 'model',
 'none',
 'only',
 'order_by',
 'ordered',
 'prefetch_related',
 'query',
 'raw',
 'resolve_expression',
 'reverse',
 'select_for_update',
 'select_related',
 'union',
 'update',
 'update_or_create',
 'using',
 'values',
 'values_list']
>>> rec
<QuerySet [<Recipe: Bolo de Cenoura by admin>, <Recipe: Bolo de Banana by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta de Limão by admin>, <Recipe: Torta Holandesa by admin>]>
>>> rec.objects
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'objects'
>>> rec.order_by('id')
<QuerySet [<Recipe: Bolo de Cenoura by admin>, <Recipe: Bolo de Banana by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta de Limão by admin>, <Recipe: Torta Holandesa by admin>]>
>>> rec.order_by('-id')
<QuerySet [<Recipe: Torta Holandesa by admin>, <Recipe: Torta de Limão by admin>, <Recipe: Panquecas by laura>, <Recipe: Frango Assado by admin>, <Recipe: Bolo de Banana by admin>, <Recipe: Bolo de Cenoura by admin>]>
>>> rec.order_by('name')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/query.py", line 1701, in order_by
    obj.query.add_ordering(*field_names)
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 2249, in add_ordering
    self.names_to_path(item.split(LOOKUP_SEP), self.model._meta)
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 1768, in names_to_path
    raise FieldError(
django.core.exceptions.FieldError: Cannot resolve keyword 'name' into field. Choices are: author, author_id, category, category_id, cover, created_at, description, id, is_published, preparation_step, preparation_step_is_html, preparation_time, preparation_time_unit, servings, servings_unit, slug, title, updated_at
>>> rec.order_by('title')
<QuerySet [<Recipe: Bolo de Banana by admin>, <Recipe: Bolo de Cenoura by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta Holandesa by admin>, <Recipe: Torta de Limão by admin>]>
>>> rec.order_by('title', '-id')
<QuerySet [<Recipe: Bolo de Banana by admin>, <Recipe: Bolo de Cenoura by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta Holandesa by admin>, <Recipe: Torta de Limão by admin>]>
>>> rec.order_by('title', 'id')
<QuerySet [<Recipe: Bolo de Banana by admin>, <Recipe: Bolo de Cenoura by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta Holandesa by admin>, <Recipe: Torta de Limão by admin>]>
>>> rec.order_by('id', 'title')
<QuerySet [<Recipe: Bolo de Cenoura by admin>, <Recipe: Bolo de Banana by admin>, <Recipe: Frango Assado by admin>, <Recipe: Panquecas by laura>, <Recipe: Torta de Limão by admin>, <Recipe: Torta Holandesa by admin>]>
>>> rec.order_by('-id', 'title')
<QuerySet [<Recipe: Torta Holandesa by admin>, <Recipe: Torta de Limão by admin>, <Recipe: Panquecas by laura>, <Recipe: Frango Assado by admin>, <Recipe: Bolo de Banana by admin>, <Recipe: Bolo de Cenoura by admin>]>
>>> for recipe in rec: print(recipe.id, recipe.title)
... 
1 Bolo de Cenoura
2 Bolo de Banana
3 Frango Assado
4 Panquecas
5 Torta de Limão
6 Torta Holandesa
>>> len(rec)
6
>>> for recipe in rec.order_by('-id'): print(recipe.id, recipe.title)
... 
6 Torta Holandesa
5 Torta de Limão
4 Panquecas
3 Frango Assado
2 Bolo de Banana
1 Bolo de Cenoura
>>> for recipe in rec.order_by('-id').first(): print(recipe.title)
... 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'Recipe' object is not iterable
>>> rec.order_by('-id').first()
<Recipe: Torta Holandesa by admin>
>>> recipe = rec.order_by('-id').first()
>>> dir(recipe)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_db_table_comment', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_field_expression_map', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_parse_params', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', '_validate_force_insert', 'adelete', 'arefresh_from_db', 'asave', 'author', 'author_id', 'category', 'category_id', 'check', 'clean', 'clean_fields', 'cover', 'created_at', 'date_error_message', 'delete', 'description', 'from_db', 'full_clean', 'get_constraints', 'get_deferred_fields', 'get_next_by_created_at', 'get_next_by_updated_at', 'get_previous_by_created_at', 'get_previous_by_updated_at', 'id', 'is_published', 'objects', 'pk', 'preparation_step', 'preparation_step_is_html', 'preparation_time', 'preparation_time_unit', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'servings', 'servings_unit', 'slug', 'title', 'unique_error_message', 'updated_at', 'validate_constraints', 'validate_unique']
>>> pprint(dir(recipe))
['DoesNotExist',
 'MultipleObjectsReturned',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_check_column_name_clashes',
 '_check_constraints',
 '_check_db_table_comment',
 '_check_default_pk',
 '_check_field_name_clashes',
 '_check_fields',
 '_check_id_field',
 '_check_indexes',
 '_check_local_fields',
 '_check_long_column_names',
 '_check_m2m_through_same_relationship',
 '_check_managers',
 '_check_model',
 '_check_model_name_db_lookup_clashes',
 '_check_ordering',
 '_check_property_name_related_field_accessor_clashes',
 '_check_single_primary_key',
 '_check_swappable',
 '_check_unique_together',
 '_do_insert',
 '_do_update',
 '_get_FIELD_display',
 '_get_expr_references',
 '_get_field_expression_map',
 '_get_next_or_previous_by_FIELD',
 '_get_next_or_previous_in_order',
 '_get_pk_val',
 '_get_unique_checks',
 '_meta',
 '_parse_params',
 '_perform_date_checks',
 '_perform_unique_checks',
 '_prepare_related_fields_for_save',
 '_save_parents',
 '_save_table',
 '_set_pk_val',
 '_state',
 '_validate_force_insert',
 'adelete',
 'arefresh_from_db',
 'asave',
 'author',
 'author_id',
 'category',
 'category_id',
 'check',
 'clean',
 'clean_fields',
 'cover',
 'created_at',
 'date_error_message',
 'delete',
 'description',
 'from_db',
 'full_clean',
 'get_constraints',
 'get_deferred_fields',
 'get_next_by_created_at',
 'get_next_by_updated_at',
 'get_previous_by_created_at',
 'get_previous_by_updated_at',
 'id',
 'is_published',
 'objects',
 'pk',
 'preparation_step',
 'preparation_step_is_html',
 'preparation_time',
 'preparation_time_unit',
 'prepare_database_save',
 'refresh_from_db',
 'save',
 'save_base',
 'serializable_value',
 'servings',
 'servings_unit',
 'slug',
 'title',
 'unique_error_message',
 'updated_at',
 'validate_constraints',
 'validate_unique']
>>> recipe._meta.get_fields()
(<django.db.models.fields.BigAutoField: id>, <django.db.models.fields.CharField: title>, <django.db.models.fields.CharField: description>, <django.db.models.fields.SlugField: slug>, <django.db.models.fields.IntegerField: preparation_time>, <django.db.models.fields.CharField: preparation_time_unit>, <django.db.models.fields.IntegerField: servings>, <django.db.models.fields.CharField: servings_unit>, <django.db.models.fields.TextField: preparation_step>, <django.db.models.fields.BooleanField: preparation_step_is_html>, <django.db.models.fields.DateTimeField: created_at>, <django.db.models.fields.DateTimeField: updated_at>, <django.db.models.fields.BooleanField: is_published>, <django.db.models.fields.files.ImageField: cover>, <django.db.models.fields.related.ForeignKey: category>, <django.db.models.fields.related.ForeignKey: author>)
>>> pprint(recipe._meta.get_fields())
(<django.db.models.fields.BigAutoField: id>,
 <django.db.models.fields.CharField: title>,
 <django.db.models.fields.CharField: description>,
 <django.db.models.fields.SlugField: slug>,
 <django.db.models.fields.IntegerField: preparation_time>,
 <django.db.models.fields.CharField: preparation_time_unit>,
 <django.db.models.fields.IntegerField: servings>,
 <django.db.models.fields.CharField: servings_unit>,
 <django.db.models.fields.TextField: preparation_step>,
 <django.db.models.fields.BooleanField: preparation_step_is_html>,
 <django.db.models.fields.DateTimeField: created_at>,
 <django.db.models.fields.DateTimeField: updated_at>,
 <django.db.models.fields.BooleanField: is_published>,
 <django.db.models.fields.files.ImageField: cover>,
 <django.db.models.fields.related.ForeignKey: category>,
 <django.db.models.fields.related.ForeignKey: author>)
>>> pprint(recipe._meta.get_fields()[0])
<django.db.models.fields.BigAutoField: id>
>>> pprint(recipe._meta.get_fields()[0].value)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'BigAutoField' object has no attribute 'value'
>>> pprint(recipe._meta.get_fields()[0].value())
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'BigAutoField' object has no attribute 'value'
>>> pprint(recipe._meta.get_fields()[0])
<django.db.models.fields.BigAutoField: id>
>>> pprint(recipe._meta.get_fields()[0].name)
'id'
>>> getattr(recipe, recipe._meta.get_fields()[0].name)
6
>>> getattr(recipe, id)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: attribute name must be string, not 'builtin_function_or_method'
>>> getattr(recipe, 'id')
6
>>> recipe['id']
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'Recipe' object is not subscriptable
>>> recipe.id
6
>>> new_c = Category()
>>> new_c
<Category: >
>>> new_c.name = 'drinks'
>>> new_c
<Category: drinks>
>>> new_c.name = 'Drinks'
>>> new_c
<Category: Drinks>
>>> new_c.save()
>>> new_c.id
7
>>> new_c = Category()
>>> new_c.id
>>> new_c.save()
>>> new_c.id
8
>>> new_c.name
''
>>> new_c = Category.objects.create()
>>> new_c = Category.objects.create(name='Pasta')
>>> new_c
<Category: Pasta>
>>> new_c.name = 'Massas'
>>> new_c.save()
>>> other = Category.objects.get(id=10)
>>> other
<Category: Massas>
>>> other = Category.objects.get(id=9)
>>> other
<Category: >
>>> other.delete()
(1, {'recipes.Category': 1})
>>> other = Category.objects.get(id=8)
>>> other
<Category: >
>>> other.delete()
(1, {'recipes.Category': 1})
>>> other
<Category: >
>>> other = Category.objects.get(id=6)
>>> other
<Category: Tortas>
>>> other = Category.objects.get(id=7)
>>> other
<Category: Drinks>
>>> other = Category.objects.get(id=8)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/query.py", line 649, in get
    raise self.model.DoesNotExist(
apps.recipes.models.Category.DoesNotExist: Category matching query does not exist.
>>> cat = Category.objects.a
Category.objects.aaggregate(         Category.objects.aggregate(
Category.objects.abulk_create(       Category.objects.ain_bulk(
Category.objects.abulk_update(       Category.objects.aiterator(
Category.objects.acontains(          Category.objects.alast()
Category.objects.acount()            Category.objects.alatest(
Category.objects.acreate(            Category.objects.alias(
Category.objects.aearliest(          Category.objects.all()
Category.objects.aexists()           Category.objects.annotate(
Category.objects.aexplain(           Category.objects.aupdate(
Category.objects.afirst()            Category.objects.aupdate_or_create(
Category.objects.aget(               Category.objects.auto_created
Category.objects.aget_or_create(     
>>> cat = Category.objects.filter(id=8)
>>> cat
<QuerySet []>
>>> cat = Category.objects.filter(id=7)
>>> cat
<QuerySet [<Category: Drinks>]>
>>> cat.first()
<Category: Drinks>
>>> cat = Category.objects.filter(id=7).first()
>>> cat
<Category: Drinks>
>>> cat = Category.objects.get(id=5)
>>> cat
<Category: Doces>
>>> cat = Category.objects.get(id=8)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/laura-carlotta/dev-projects/python-study/django_projects/Curso-de-Django-Web-Framework-e-Django-Rest-Framework-DRF-com-Luiz-Otavio-Miranda/.venv/lib/python3.12/site-packages/django/db/models/query.py", line 649, in get
    raise self.model.DoesNotExist(
apps.recipes.models.Category.DoesNotExist: Category matching query does not exist.
>>> cat = Category.objects.filter(id=8)
>>> cat
<QuerySet []>
>>> cat = Category.objects.filter(id=8).first()
>>> cat
>>> 




➜ python manage.py shell    
Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.
User.DoesNotExist(                    User.get_username(
User.EMAIL_FIELD                      User.groups
User.Meta()                           User.has_module_perms(
User.MultipleObjectsReturned(         User.has_perm(
User.REQUIRED_FIELDS                  User.has_perms(
User.USERNAME_FIELD                   User.has_usable_password(
User.acheck_password(                 User.id
User.add_to_class(                    User.is_active
User.adelete(                         User.is_anonymous
User.arefresh_from_db(                User.is_authenticated
User.asave(                           User.is_staff
User.check(                           User.is_superuser
User.check_password(                  User.last_login
User.clean(                           User.last_name
User.clean_fields(                    User.logentry_set
User.date_error_message(              User.mro()
User.date_joined                      User.natural_key(
User.delete(                          User.normalize_username(
User.email                            User.objects
User.email_user(                      User.password
User.first_name                       User.pk
User.from_db(                         User.prepare_database_save(
User.full_clean(                      User.recipe_set
User.get_all_permissions(             User.refresh_from_db(
User.get_constraints(                 User.save(
User.get_deferred_fields(             User.save_base(
User.get_email_field_name()           User.serializable_value(
User.get_full_name(                   User.set_password(
User.get_group_permissions(           User.set_unusable_password(
User.get_next_by_date_joined(         User.unique_error_message(
User.get_previous_by_date_joined(     User.user_permissions
User.get_session_auth_fallback_hash(  User.username
User.get_session_auth_hash(           User.username_validator(
User.get_short_name(                  User.validate_constraints(
User.get_user_permissions(            User.validate_unique(
>>> User.objects.
User.objects.aaggregate(           User.objects.defer(
User.objects.abulk_create(         User.objects.difference(
User.objects.abulk_update(         User.objects.distinct(
User.objects.acontains(            User.objects.earliest(
User.objects.acount()              User.objects.exclude(
User.objects.acreate(              User.objects.exists()
User.objects.aearliest(            User.objects.explain(
User.objects.aexists()             User.objects.extra(
User.objects.aexplain(             User.objects.filter(
User.objects.afirst()              User.objects.first()
User.objects.aget(                 User.objects.from_queryset(
User.objects.aget_or_create(       User.objects.get(
User.objects.aggregate(            User.objects.get_by_natural_key(
User.objects.ain_bulk(             User.objects.get_or_create(
User.objects.aiterator(            User.objects.get_queryset()
User.objects.alast()               User.objects.in_bulk(
User.objects.alatest(              User.objects.intersection(
User.objects.alias(                User.objects.iterator(
User.objects.all()                 User.objects.last()
User.objects.annotate(             User.objects.latest(
User.objects.aupdate(              User.objects.model(
User.objects.aupdate_or_create(    User.objects.name
User.objects.auto_created          User.objects.none()
User.objects.bulk_create(          User.objects.normalize_email(
User.objects.bulk_update(          User.objects.only(
User.objects.check(                User.objects.order_by(
User.objects.complex_filter(       User.objects.prefetch_related(
User.objects.contains(             User.objects.raw(
User.objects.contribute_to_class(  User.objects.reverse()
User.objects.count()               User.objects.select_for_update(
User.objects.create(               User.objects.select_related(
User.objects.create_superuser(     User.objects.union(
User.objects.create_user(          User.objects.update(
User.objects.creation_counter      User.objects.update_or_create(
User.objects.dates(                User.objects.use_in_migrations
User.objects.datetimes(            User.objects.using(
User.objects.db                    User.objects.values(
User.objects.db_manager(           User.objects.values_list(
User.objects.deconstruct()         User.objects.with_perm(
>>> User.objects.create_
User.objects.create_superuser(  User.objects.create_user(       
>>> User.objects.create_user(first_name='Maria', last_name='do Bairro', username='mariadobairro', email='mariadobairro@gmail.com, password='123456')
  File "<console>", line 1
    User.objects.create_user(first_name='Maria', last_name='do Bairro', username='mariadobairro', email='mariadobairro@gmail.com, password='123456')
                                                                                                                                                  ^
SyntaxError: unterminated string literal (detected at line 1)
>>> User.objects.create_user(first_name='Maria', last_name='do Bairro', username='mariadobairro', email='mariadobairro@gmail.com', password='123456')
<User: mariadobairro>
>>> from apps.recipes.models import Recipe
>>> recipes = Recipe.objects.filter(
...         category__id = category_id,
...         is_published = True
... 
... 
... 
... 
... 
... 
... 
... 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> recipes = Recipe.objects.filter(
...         category__id = category_id,
...         is_published = True
...     ).order_by('-id')
Traceback (most recent call last):
  File "<console>", line 2, in <module>
NameError: name 'category_id' is not defined
>>> recipes = Recipe.objects.filter(
...         category__id = 2,
...         is_published = True
...     ).order_by('-id')
>>> recipes
<QuerySet [<Recipe: Bolo de Fubá by admin>, <Recipe: Bolo de Prestigio by laura>, <Recipe: Bolo de Banana by admin>, <Recipe: Bolo de Cenoura by admin>]>
>>> recipes.first()
<Recipe: Bolo de Fubá by admin>
>>> recipes.first().category
<Category: Bolos>
>>> recipes.first().category.name
'Bolos'
>>> exit()