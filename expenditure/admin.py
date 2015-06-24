from django.contrib import admin
from expenditure.models import *
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Class,ClassAdmin)

class MergeoptionAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Mergeoption,MergeoptionAdmin)

class ExpmonthlyAdmin(admin.ModelAdmin):
	fields=('household','household_number','food_rice_ration','food_rice_outside','food_rice_price','food_wheat_ration','food_wheat_outside','food_wheat_price','food_sugar_ration','food_sugar_outside','food_sugar_price','food_kerosene_ration','food_kerosene_outside','food_kerosene_price','food_pulse_ration','food_pulse_outside','food_pulse_price','food_oil_ration','food_oil_outside','food_oil_price','food_spices_outside','food_spices_price','food_milk_outside','food_milk_price','food_vegtbles_outside','food_vegtbles_price','food_meat_outside','food_meat_price','food_eggs_outside','food_eggs_price','soaps_paste_peryear','cloths_per_year','current_bill','phone','shaving_cutting','house_rent','cylinder','socialcustoms_festivals','socialcustoms_marriages','socialcustoms_funerals','socialcustoms_templefairs','socialcustoms_onifunctions','socialcustoms_childnaming','socialcustoms_birthday','entertainment_movies','entertainment_tours','entertainment_liquor','entertainment_smoking','entertainment_playcards','entertainment_cockfights','electronics_cable_value','meat_noofdays','eggs_noofdays','pappu_noofdays','kuralu_noofdays','pachhadi_noofdays','karam_noofdays','milk_noofdays','curds_noofdays','buttermilk_noofdays','rice_noofdays','nookalasankati_noofdays','roti_noofdays','pindivantalu_noofdays','ragimudda_noofdays','family_withoutfood_noofdays','comments')
admin.site.register(Expmonthly,ExpmonthlyAdmin)

class ExpeducationAdmin(admin.ModelAdmin):
	fields=('household','household_number','child_name','age','studentclass','govt_or_private','school_fee','tuition_fee','books_fee','travel_expenses','total_expenses','comments')
admin.site.register(Expeducation,ExpeducationAdmin)

class ExphealthAdmin(admin.ModelAdmin):
	fields=('household','household_number','name_familymember','illness','govt_or_private','cost_of_treatment','expendutre_morgaging_selling_land_gold_loan','others','comments')
admin.site.register(Exphealth,ExphealthAdmin)

class MigrationAdmin(admin.ModelAdmin):
	fields=('household','household_number','s_no','name_migrant','in_migration','out_migration','shortterm_from','shortterm_to','longterm_from','longterm_to','destination_village','destination_town','destination_country','reason_migration','annual_inflow','sufficient_meet_needs','using_this_amount','haveyou_bought_assets','comments')
admin.site.register(Migration,MigrationAdmin)

class InvistigatorsAdmin(admin.ModelAdmin):
	fields=('household','household_number','comments_observations','name_of_invistigator','date_of_interview','time_taken_for_interview','data_entry_by','date_data_entry','is_furtherinv_needed','comments')
admin.site.register(Invistigators,InvistigatorsAdmin)

