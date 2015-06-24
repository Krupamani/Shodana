from django.contrib import admin
from landlease.models import *

# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Registration,RegistrationAdmin)

class ContracttypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Contracttype,ContracttypeAdmin)

class KindAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Kind,KindAdmin)

class PeriodAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Period,PeriodAdmin)

class PercentAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Percent,PercentAdmin)

class LandtanentAdmin(admin.ModelAdmin):
	fields=('household','household_number','fixedrent','sharedrent','total','comments')
admin.site.register(Landtanent,LandtanentAdmin)

class LandleasedinAdmin(admin.ModelAdmin):
	fields=('household','household_number','tenant_or_not','landtype','extent','landowner_name','landowner_caste','landowner_occupation','landowner_extent_landholding','tenurial_registration','tenurial_contracttype','tenurial_sincewhen','annual_fixedrent_cash','annual_fixedrent_kind','qty_hay_byowner', 'loan_fromowner_withinterest' , 'loan_fromowner_interestfree','input_owner_manure','input_owner_fertiliser','input_owner_seed','input_owner_pesticide','input_owner_electricity','input_owner_pumpset','input_owner_machinary','comments')
admin.site.register(Landleasedin,LandleasedinAdmin)

class LandleaserAdmin(admin.ModelAdmin):
	fields=('household','household_number','fixedrent','sharedrent','total','comments')
admin.site.register(Landleaser,LandleaserAdmin)

class LandleasedoutAdmin(admin.ModelAdmin):
	fields=('household','household_number','leaseout_or_not','landtype','extent','landtenant_name','landtenant_caste','landtenant_occupation','landtenant_extent_landholding','tenurial_registration','tenurial_contracttype','tenurial_sincewhen','annual_fixedrent_cash','annual_fixedrent_kind','qty_hay_bytenant','loan_fromyou_withinterest','loan_fromyou_interestfree','input_you_manure','input_you_fertiliser','input_you_seed','input_you_pesticide','input_you_electricity','input_you_pumpset','input_you_machinary','comments')
admin.site.register(Landleasedout,LandleasedoutAdmin)

class MortgagedinAdmin(admin.ModelAdmin):
	fields=('household','household_number','mortgagedin_or_not','landtype','extent','businessman_name','businessman_caste','businessman_occupation','year_mortgage','mortgage_period','mortgage_amount','interest','comments')
admin.site.register(Mortgagedin,MortgagedinAdmin)

class MortgagedoutAdmin(admin.ModelAdmin):
	fields=('household','household_number','mortgagedout_or_not','landtype','extent','mortgagee_name','mortgagee_caste','mortgagee_occupation','year_mortgage','mortgage_period','mortgage_amount','interest','comments')
admin.site.register(Mortgagedout,MortgagedoutAdmin)

class SharerentinAdmin(admin.ModelAdmin):
	fields=('household','household_number','sharedin_or_not','landtype','extent','landowner_name','landowner_caste','landowner_occupation','landowner_extent_hold','registered_or_not','period','since_when_leased','owner_share_crop_percent','owner_share_crop_qty','owner_share_hay_percent','owner_share_hay_qty','input_owner_manure_percent','input_owner_manure_rs','input_owner_fert_percent','input_owner_fert_rs','input_owner_seed_percent','input_owner_seed_rs','input_owner_pest_percent','input_owner_pest_rs','input_owner_elec_percent','input_owner_elec_rs','input_owner_pump_percent','input_owner_pump_rs','input_owner_machinary_percent','input_owner_machinary_rs','input_owner_labor_percent','input_owner_labor_rs','loan_by_owner_interestfree','loan_by_owner_interest','loan_by_owner_rateofinterest','comments')
admin.site.register(Sharerentin,SharerentinAdmin)

class SharerentoutAdmin(admin.ModelAdmin):
	fields=('household','household_number','sharedrent_or_not','landtype','extent','cropper_name','cropper_caste','cropper_occupation','cropper_extent_hold','registered_or_not','period','since_when_leased','tenant_share_crop_percent','tenant_share_crop_qty','tenant_share_hay_percent','tenant_share_hay_qty','input_you_manure_percent','input_you_manure_rs','input_you_fert_percent','input_you_fert_rs','input_you_seed_percent','input_you_seed_rs','input_you_pest_percent','input_you_pest_rs','input_you_elec_percent','input_you_elec_rs','input_you_pump_percent','input_you_pump_rs','input_you_machinary_percent','input_you_machinary_rs','input_you_labor_percent','input_you_labor_rs','loan_by_you_interestfree','loan_by_you_interest','loan_by_owner_rateofinterest','comments')
admin.site.register(Sharerentout,SharerentoutAdmin)

class TenantproblemsAdmin(admin.ModelAdmin):
	fields=('household','household_number','loan_landowner_prior_tenancy','debt_inherited','why_ownland_notsufficient','why_opportunity_cattle','why_for_foodgrains','why_lowrent_profitable','why_wageslow_manage','why_tenancy_respectable','why_inability_wagework','why_noskill_urban','dueto_lack_opportunites','other_reasons','because_debt_to_leaser','because_debt_to_leaser_amt','reason_compelled','reason_compelled_one','reason_compelled_two','reason_compelled_three','nature_contract_written','nature_contract_verbal','nonereason_tenant','inherited_problems','lack_anyother_option','provide_freeservice_owner','nota_comeout_otherreasons','comments',)
admin.site.register(Tenantproblems,TenantproblemsAdmin)

class InterlinksAdmin(admin.ModelAdmin):
	fields=('household','household_number','inputs_labour','inputs_commodity','inputs_land','inputs_loans','loans_labour','loans_commodity','loans_land','land_labour','land_commodity','comodity_labour','comments')
admin.site.register(Interlinks,InterlinksAdmin)

