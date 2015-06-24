from django.contrib import admin
from housing.models import *

# Register your models here.

class OwnedorrentedAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Ownedorrented,OwnedorrentedAdmin)

class CardcolorAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Cardcolor,CardcolorAdmin)

class CardtypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Cardtype,CardtypeAdmin)

class RooftypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Rooftype,RooftypeAdmin)

class WalltypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Walltype,WalltypeAdmin)

class FloortypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Floortype,FloortypeAdmin)

class LatrinetypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Latrinetype,LatrinetypeAdmin)

class ElectricitytypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Electricitytype,ElectricitytypeAdmin)

class Sourcecooking_oneAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Sourcecooking_one,Sourcecooking_oneAdmin)

class Sourcecooking_twoAdmin(admin.ModelAdmin):
        fields=('name',)
admin.site.register(Sourcecooking_two,Sourcecooking_twoAdmin)

class NaturereimbusmentAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Naturereimbusment,NaturereimbusmentAdmin)

class InteresttypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Interesttype,InteresttypeAdmin)

class BorrowingsourceAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Borrowingsource,BorrowingsourceAdmin)

class HoubaseAdmin(admin.ModelAdmin):
	fields=('household', 'household_number', 's_no', 'owned_or_rented', 'year_construction', 'isthere_kitchen', 'noof_additional_rooms', 'type_roof','type_of_floor','type_wall','isthere_veranda', 'latrine', 'electricity', 'source_energy_cooking_one','source_energy_cooking_two', 'govtscheme_yes_or_no', 'year_recent_repair','govtscheme_year', 'govtscheme_nature_reimbusment', 'govtscheme_cash', 'value_of_house', 'availbility_safe_drinking_text','does_village_have_safe_waterfacility', 'does_house_have_watertap','distance_travelled_water', 'amount_spending_water', 'comments',)
admin.site.register(Houbase,HoubaseAdmin)

class IndebtednessAdmin(admin.ModelAdmin):
	fields=('household','household_number','month_year','principal','collateral','thing_indebtedness','type_interest','rate_interest','amount_outstanding_principal','amount_outstanding_interest','amount_outstanding_total','amont_repaid','source_borrowing','purpose_borrowing','comments')
admin.site.register(Indebtedness,IndebtednessAdmin)

class SelfhelpgroupsAdmin(admin.ModelAdmin):
	fields=('household','household_number','name_member','name_group','name_group_leader','bank_group_linked','period_member','number_members_group','savings_perweek','savings_permonth','comments')
admin.site.register(Selfhelpgroups,SelfhelpgroupsAdmin)

class AssetsAdmin(admin.ModelAdmin):
	fields=('household', 'household_number', 'agricultural_land_area', 'agricultural_land_value', 'homestead_land_area', 'homestead_land_value', 'anyother_land_area', 'anyother_land_value', 'ponds_tanks_area', 'ponds_tanks_value', 'buildings_house_no', 'buildings_house_value', 'buildings_cattleshed_no', 'buildings_cattleshed_value', 'buildings_shop_no', 'buildings_shop_value', 'buildings_anyother_no', 'buildings_anyother_value', 'transport_bicycle_no', 'transport_bicycle_value', 'transport_moped_no','transport_moped_value','transport_scooter_no','transport_scooter_value', 'transport_car_no', 'transport_car_value',  'transport_lorry_no', 'transport_lorry_value', 'transport_bus_no', 'transport_bus_value','transport_bullockcart_no', 'transport_bullockcart_value', 'transport_tractor_no', 'transport_tractor_value', 'transport_auto_no', 'transport_auto_value' , 'transport_other_no', 'transport_other_value','investments_bonds_no', 'investments_bonds_value','investments_chitfunds_no', 'investments_chitfunds_value', 'investments_gold_no', 'investments_gold_value', 'investments_silver_no', 'investments_silver_value' ,'electronics_refrigerator_no', 'electronics_refrigerator_value', 'electronics_ac_no', 'electronics_ac_value', 'electronics_colortv_no', 'electronics_colortv_value', 'electronics_mobile_no','electronics_mobile_value','electronics_telephone_no','electronics_telephone_value','electronics_fan_no','electronics_fan_value','electronics_dish_no','electronics_washingmachine_no','electronics_washingmachine_value','electronics_grinder_no','electronics_grinder_value','electronics_mixy_no','electronics_mixy_value','durables_tailoringmachine_no' ,'durables_tailoringmachine_value' ,'durables_wwatch_no','durables_wwatch_value', 'durables_gasstove_no','durables_gasstove_value','durables_biogas_no','durables_biogas_value','durables_handpump_no','durables_handpump_value','durables_kitchenset_no','durables_kitchenset_value', 'woman_land_patta', 'woman_land_patta_text','comments')
admin.site.register(Assets,AssetsAdmin)

class GovtdistribAdmin(admin.ModelAdmin):
	fields=('household','household_number','rationcard_exist','card_type','card_color','number_registered','number_registered_adults','number_registered_kids','reasons_for_nocard','comments','ration_available_intime','ration_available_sufficient','ration_reasonable_price','ration_weights_perfect','ration_buy_onetime','ration_buy_multipletimes_accept',)
admin.site.register(Govtdistrib,GovtdistribAdmin)

