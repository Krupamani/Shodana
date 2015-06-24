from django.contrib import admin
from labourwages.models import *

# Register your models here.
class AgoperationAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Agoperation,AgoperationAdmin)

class WagetypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Wagetype,WagetypeAdmin)

class WorkprogrammeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Workprogramme,WorkprogrammeAdmin)

class ObligationtypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Obligationtype,ObligationtypeAdmin)

class TaskdescriptionAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Taskdescription,TaskdescriptionAdmin)

class CollecteditemsAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Collecteditems,CollecteditemsAdmin)

class MagencyAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Magency,MagencyAdmin)

class CheatingfacedAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Cheatingfaced,CheatingfacedAdmin)

class WorkdescriptionAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Workdescription,WorkdescriptionAdmin)

class AnimaltypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Animaltype,AnimaltypeAdmin)

class AnimalproductionAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Animalproduction,AnimalproductionAdmin)

class LabourdaysAdmin(admin.ModelAdmin):
	fields=('household','household_number','labour_deployed','s_no','crop','extent','agricultural_operation','family_labour_days_m','family_labour_days_w','family_labour_days_c','family_labour_hours_m','family_labour_hours_w','family_labour_hours_c','daily_labour_days_m','daily_labour_days_w','daily_labour_days_c','daily_labour_hours_m','daily_labour_hours_w','daily_labour_hours_c','daily_labour_wages_m','daily_labour_wages_w','daily_labour_wages_c','exchange_labour_days_m','exchange_labour_days_w','exchange_labour_days_c','exchange_labour_hours_m','exchange_labour_hours_w','exchange_labour_hours_c','piece_rated_cash','piece_rated_kind','machine_labour_workhours','machine_labourpayment','comments',)
admin.site.register(Labourdays,LabourdaysAdmin)

class WagesAdmin(admin.ModelAdmin):
	fields=('household','household_number','is_agricultural_labour','worker_name','crop','operation','type_wage','place_work','labour_days','work_hours','earnings_cash','income','piece_rate_kind','contract_number_acres','contract_remuniration','contract_howmany_workers','contract_total_wage','wagerates_increased','migrations_declined','isthere_change_peasants','has_baragaining_power_increased','comments',)
admin.site.register(Wages,WagesAdmin)

class NonaglabourAdmin(admin.ModelAdmin):
	fields=('household','household_number','workedin_nonag_operation','worker_name','description_specify_programme', 'type_wage_contract','place_work','number_days','work_hours','wage_rate' ,'totalearnings_cash','comments')
admin.site.register(Nonaglabour,NonaglabourAdmin)

class EmpfreedomAdmin(admin.ModelAdmin):
	fields=('household' , 'household_number', 'comments',)
admin.site.register(Empfreedom,EmpfreedomAdmin)

class IncomeotherAdmin(admin.ModelAdmin):
	fields=('household','household_number','worker_name','work_description','work_place','totalnet_earnings','earlier_income_kind','comments',)
admin.site.register(Incomeother,IncomeotherAdmin)

class AnimalsourceAdmin(admin.ModelAdmin):
	fields=('household','household_number','animal_owned','type','s_no','nu','age','feed_home_grown','feed_purchased','total_present_value','veternary_charges','maintanence_buildings','insurance','interest_loans_livestock','labour_charges','others','income_production_one','production_work_qty_one','production_work_price_one','income_production_two','production_work_qty_two','production_work_price_two','comments')
admin.site.register(Animalsource,AnimalsourceAdmin)

