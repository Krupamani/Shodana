from django.contrib import admin
from household.models import * 
# Register your models here.

class VillageAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Village,VillageAdmin)

class MandalAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Mandal,MandalAdmin)

class DistrictAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(District,DistrictAdmin)

class SexAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Sex,SexAdmin)

class CasteAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Caste,CasteAdmin)

class YearAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Year,YearAdmin)

class ReligionAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Religion,ReligionAdmin)

class YesornoAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Yesorno,YesornoAdmin)

class NumbersAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Numbers,NumbersAdmin)

class RelationshipAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Relationship,RelationshipAdmin)

class MaritalstatusAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Maritalstatus,MaritalstatusAdmin)

class LiterarystatusAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Literarystatus,LiterarystatusAdmin)

class EducationlevelAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Educationlevel,EducationlevelAdmin)


class OccupationAdmin(admin.ModelAdmin):
        fields=('name',)
admin.site.register(Occupation,OccupationAdmin)

class BaseAdmin(admin.ModelAdmin):
	fields=('village','household_number','name_of_household','sex','age','caste','scorst','tehisil_of_birth','mandal','year_migration','father_name','father_occupation','religion','address','phone','comments')
admin.site.register(Base,BaseAdmin)

class HhmembersAdmin(admin.ModelAdmin):
	fields=('household', 'household_number', 'name', 'sex', 'age', 'relationship_to_head', 'marital_status', 'occupations_one', 'place_of_work_one', 'occupations_two', 'place_of_work_two', 'occupations_three', 'place_of_work_three' , 'literary_status', 'education_level', 'name_location_institute','comments')
admin.site.register(Hhmembers,HhmembersAdmin)

