from django.contrib import admin
from land.models import * 

# Register your models here.

class LandtypeAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Landtype,LandtypeAdmin)

class IrrigationsourceAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Irrigationsource,IrrigationsourceAdmin)

class IrrigationflowAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Irrigationflow,IrrigationflowAdmin)

class IrrigationownshipAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Irrigationownship,IrrigationownshipAdmin)

class AquirelandAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Aquireland,AquirelandAdmin)

class ReasonforsaleAdmin(admin.ModelAdmin):
	fields=('name',)
admin.site.register(Reasonforsale,ReasonforsaleAdmin)

class CurrentownershipAdmin(admin.ModelAdmin):
	fields=('household','household_number','landowned_or_not','landtype','extent_of_owned','irrigationsource_one','irrigationflow_one','irrigationownship_one','irrigationsource_two','irrigationflow_two','irrigationownship_two','irrigationsource_three','irrigationflow_three','irrigationownship_three','value','patta_for_land','how_aquireland','comments',)
admin.site.register(Currentownership,CurrentownershipAdmin)

class LandsoldAdmin(admin.ModelAdmin):
	fields=('household','household_number','land_sold_or_not','year_of_sale','extent','type_of_land','buyer_name','buyer_catse','buyer_occupation','buyer_place_residence','price_land','reason_for_sale','comments',)
admin.site.register(Landsold,LandsoldAdmin)

class LandboughtAdmin(admin.ModelAdmin):
	fields=('household','household_number','land_bought_or_not','year_of_purchase','extent','type_of_land','seller_name','seller_catse','seller_occupation','seller_place_residence','price_land','income_source','comments',)
admin.site.register(Landbought,LandboughtAdmin)

