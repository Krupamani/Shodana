from django.contrib import admin
from cropping.models import *

# Register your models here.
class CropAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Crop,CropAdmin)

class OtheractivitiesAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Otheractivities,OtheractivitiesAdmin)

class TenurialstatusAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Tenurialstatus,TenurialstatusAdmin)

class MarketingplaceAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Marketingplace,MarketingplaceAdmin)

class FertilisertypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Fertilisertype,FertilisertypeAdmin)

class ManuretypeAdmin(admin.ModelAdmin):
        fields=('name',)
admin.site.register(Manuretype,ManuretypeAdmin)


class TransportmodeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Transportmode,TransportmodeAdmin)

class ItemcodeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Itemcode,ItemcodeAdmin)

class TubewelltypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Tubewelltype,TubewelltypeAdmin)

class BusinessactivitiesAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Businessactivities,BusinessactivitiesAdmin)

class TasksperformedAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Tasksperformed,TasksperformedAdmin)

class TimeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Time,TimeAdmin)

class ProductionsalesAdmin(admin.ModelAdmin):
	fields=('household','household_number', 'produced','s_no','crop','tenurial_status','extent','month_sowing','month_harvesting','source_irrigation','production_grain','production_straw','household_consumpion_grain','household_consumption_straw','sale_month_disposal','sale_quantity','sale_price','sale_where_marketed','sale_marketing_agency','sale_transport_mode','sale_transport_cost','sale_other_marketing_costs','sale_wasthe_price_fixedbefore','sale_by_products_amt','sale_by_products_price','comments')
admin.site.register(Productionsales,ProductionsalesAdmin)

class InputsAdmin(admin.ModelAdmin):
	fields=('household','household_number','inputs_used','s_no','crop','manure_type_one', 'manure_home_qty_one', 'manure_type_two', 'manure_home_qty_two',  'manure_type_three', 'manure_home_qty_three',  'manure_type_four', 'manure_home_qty_four', 'manure_purchased_type_one', 'manure_purchased_qty_one', 'manure_purchased_price_one',  'manure_purchased_type_two', 'manure_purchased_qty_two', 'manure_purchased_price_two','manure_purchased_type_three', 'manure_purchased_qty_three', 'manure_purchased_price_three', 'manure_purchased_type_four', 'manure_purchased_qty_four', 'manure_purchased_price_four','manure_transport_mode','manure_transport_costincurred','fertiliser_type_one', 'fertiliser_qty_one','fertiliser_price_one', 'fertiliser_type_two', 'fertiliser_qty_two','fertiliser_price_two', 'fertiliser_type_three', 'fertiliser_qty_three','fertiliser_price_three', 'fertiliser_type_four', 'fertiliser_qty_four','fertiliser_price_four',  'fertiliser_type_five', 'fertiliser_qty_five','fertiliser_price_five', 'fertiliser_type_six', 'fertiliser_qty_six','fertiliser_price_six', 'fertiliser_type_seven', 'fertiliser_qty_seven', 'fertiliser_price_seven', 'fertiliser_type_eight', 'fertiliser_qty_eight','fertiliser_price_eight', 'fertiliser_transport_mode','fertiliser_transport_costincurred','seeds_home_qty','seeds_purchased_qty','seeds_purchased_price','plant_protection_value','irrigation_charges_source','irrigation_charges_price','advice_regarding_cultivation','comments')
admin.site.register(Inputs,InputsAdmin)

class SpecifiedproductionAdmin(admin.ModelAdmin):
	fields=('household','household_number','implements_owned','itemcode','ownership_number','ownership_yearpurchase','ownership_pricepaid_perunit','ownership_subsidy_received','ownership_presentvalue','maintenance_charges_lastyear','rental_earnings_units','rental_earnings','comments',)
admin.site.register(Specifiedproduction,SpecifiedproductionAdmin)

class TubewellsAdmin(admin.ModelAdmin):
	fields=('household','household_number','tubewell_owned','s_no','year_installed','depth_installed','depth_present','type','cost_installation','maintanence_last_year','operated_other_crop','operated_other_sale_area','operated_other_sale_totalrevenue','total_earnings','comments',)
admin.site.register(Tubewells,TubewellsAdmin)

class OthercostsAdmin(admin.ModelAdmin):
	fields=('household','household_number','item_code','amount_spent','comments',)
admin.site.register(Othercosts,OthercostsAdmin)

class ManagerpaymentsAdmin(admin.ModelAdmin):
	fields=('household','household_number','employ_manager_lastyear','employ_longterm_lastyear','name_worker','caste','since_when','number_months','payments_incash','payments_inkind','payments_total','comments',)
admin.site.register(Managerpayments,ManagerpaymentsAdmin)

class LongtermworkerAdmin(admin.ModelAdmin):
	fields=('household','household_number','workedas_longtermworker','name_worker','name_manager','caste_manager','occupation_manager','land_owned','land_leasedin_mortin','land_leasedout_mortout','other_business_activities','tasks_performed_one','tasks_performed_two','tasks_performed_three','number_months','earning_cash','earning_kind','total','get_number_days_off','working_from','working_to','illness_get_help','illness_get_help_text','subjected_harassments','subjectd_harassments_describe','comments')
admin.site.register(Longtermworker,LongtermworkerAdmin)

