from django.contrib import admin
from .models.Shtab import *
from .models.Ispolnitel import *
from .models.Poruchenie import *
from .models.Object import *

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter


# Register your models here.

admin.site.register(Sortforpo)
admin.site.register(Predsedatel)

@admin.register(Statysisp)
class ObjectForpo(admin.ModelAdmin):
    list_display = ['pk','stat']

@admin.register(Forpo)
class ObjectForpo(admin.ModelAdmin):
    list_display = ['pk','statforpo']


@admin.register(Shtab)
class ObjectShtab(admin.ModelAdmin):
    list_display = ['pk','dateshtabe','predsedatel']
    search_fields = ['dateshtabe']

#_____________________  ПОРУЧЕНИЯ ______________________________________

class PoruchenieResource(resources.ModelResource):
    class Meta:
        model = Poruchenie

# class Filter(admin.ModelAdmin):
#     list_display = ['object', 'otv', 'por']
#     list_filter = ['redzone',]

@admin.register(Poruchenie)
class PoruchenieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PoruchenieResource
    list_display = ['shtab','object','otv', 'por']
    # list_editable = ['redzone']
    search_fields = ['otv__surname','soisp__surname']
    list_filter = [('shtab', RelatedDropdownFilter),'obiaz','redzone','kritvopr','porneizprot','factsrivsroka','gpr','otvotpo']
    raw_id_fields = ['otv', ]

    fieldsets = (
        ('Информация по поручению', {
            'fields': ('shtab', 'numberpor',
                       ('otv', 'soisp'),'srokisp',
                       ('por','obiaz','gpr','factsrivsroka','porneizprot','kritvopr','redzone','forpo'))
        }),
        ('Работа с поручением', {
            # 'classes': ('extrapretty',),
            'fields': (('itogi', 'dateisp'), ('otprzapr','polzapr','kratkopisisppor'),
                       'anal','otvotpo')
        }),
    )
    # Не используемые поля statysisp,forpo
    filter_horizontal = ('soisp',)

    # autocomplete_fields = ['otvotpo']

    # def get_form(self, request, obj=None, change=False, **kwargs):
    #     form = super().get_form(self,request,obj,**kwargs)
    #     form.base_fields['otvotpo'].initial = request.user
    #     return form

#_____________________  ОБЪЕКТЫ ______________________________________

class ObjectResource(resources.ModelResource):
    kratknaim = fields.Field(column_name='Краткое наименование', attribute='kratknaim')
    sortforpo = fields.Field(column_name='Сортировка для ПО', attribute='sortforpo', widget=ForeignKeyWidget(Sortforpo,'category'))

    class Meta:
        model = Object
        # exclude = ['id']

@admin.register(Object)
class ObjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ObjectResource
    list_display = ['kratknaim','numberobjectaip','objectaip']
    search_fields = ['kratknaim']
# admin.site.register(Object, ObjectAdmin)


#_____________________ОРГАНИЗАЦИИ______________________________________

class OrganizationResource(resources.ModelResource):
    kratknaim = fields.Field(column_name='Краткое наименование', attribute='kratknaim')
    polnnaim = fields.Field(column_name='Полное наименование', attribute='polnnaim')
    mail1 = fields.Field(column_name='Общая электронная почта', attribute='mail1')

    class Meta:
        model = Organization
        exclude = ['id']
#
@admin.register(Organization)
class OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = OrganizationResource
    # list_display = ['surname','name','patronymic','dolzhnost,','org','mail1']
    list_display = ['kratknaim', 'polnnaim', 'mail1']
    list_display_links = ['kratknaim',]
    # list_display = ['dolzhnost']
    # list_editable = ['dolzhnost',]
    search_fields = ['kratknaim',]
# admin.site.register(Object, ObjectAdmin)


#______________ОТВЕТСТВЕННЫЕ______________________________________

class IspolnitelResource(resources.ModelResource):
    surname = fields.Field(column_name='Фамилия', attribute='surname')
    name = fields.Field(column_name='Имя', attribute='name')
    patronymic = fields.Field(column_name='Отчетсво', attribute='patronymic')
    dolzhnost = fields.Field(column_name='Должность', attribute='dolzhnost')
    org = fields.Field(column_name='Организация', attribute='org', widget=ForeignKeyWidget(Organization,'kratknaim'))
    mail1 = fields.Field(column_name='Электронная почта', attribute='mail1')
    # redzone = fields.Field(column_name='В красной зоне', attribute='redzone')
    #

    class Meta:
        model = Ispolnitel
        exclude = ['id']
#
@admin.register(Ispolnitel)
class IspolnitelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IspolnitelResource
    # list_display = ['surname','name','patronymic','dolzhnost,','org','mail1']
    list_display = ['pk','surname', 'name', 'patronymic','dolzhnost', 'org', 'mail1']
    list_display_links = ['surname',]
    # list_display = ['dolzhnost']
    # list_editable = ['dolzhnost',]
    search_fields = ['surname',]
# admin.site.register(Object, ObjectAdmin)