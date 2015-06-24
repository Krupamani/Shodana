# -*- coding: utf-8 -*-
from django.db import models
from household.models import *
from land.models import *
from landlease.models import *
from adminsortable.models import Sortable



# Create your models here.
class Crop(models.Model):
	name = models.CharField(max_length=255)
        class Meta:
                verbose_name_plural = "1.Crops"  


	def __str__(self):
                return self.name

class Otheractivities(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Tenurialstatus(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Marketingplace(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Fertilisertype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Transportmode(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Manuretype(models.Model):
        name = models.CharField(max_length=255)
        def __str__(self):
                return self.name

class Itemcode(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Tubewelltype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Businessactivities(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Tasksperformed(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Time(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Productionsales(models.Model):
	produced=models.ForeignKey(Yesorno, related_name = "produced")
	sale_wasthe_price_fixedbefore = models.ForeignKey(Yesorno,null=True,blank=True,related_name = "sale_wasthe_price_fixedbefore", verbose_name='ధర ముందే నిర్నయమయ్యిందా?')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	crop = models.ForeignKey(Crop,null=True, blank=True, verbose_name='పంట')
	source_irrigation = models.ForeignKey(Irrigationsource,null=True, blank=True, related_name = "source_irrigation", verbose_name='సాగునీటి వనరు')
	production_straw = models.FloatField(null=True, blank=True, verbose_name='గడ్డి ఉత్పత్తి')
	sale_by_products_price = models.FloatField(null=True, blank=True, verbose_name='గడ్డి అమ్మిన ధర')
	tenurial_status = models.ForeignKey(Tenurialstatus,null=True, blank=True, related_name = "tenurial_status", verbose_name='కౌలు/సొంత/తాకట్టు')
	sale_marketing_agency = models.ForeignKey(Marketingplace,null=True, blank=True, related_name = "sale_marketing_agency", verbose_name='ఎవరికీ అమ్మారు')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	sale_quantity = models.FloatField(null=True, blank=True, verbose_name='అమ్మిన పరిమాణం')
	month_harvesting = models.CharField(max_length=255,null=True, blank=True, verbose_name='కోసిన నెల')	
	sale_transport_cost = models.FloatField(null=True, blank=True, verbose_name='రవాణా ఖర్చు')
	household_consumption_straw = models.FloatField(null=True, blank=True, verbose_name='ఇంటి వాడకం - గడ్డి')
	sale_price = models.FloatField(null=True, blank=True, verbose_name='అమ్మిన ధర')
	sale_transport_mode = models.ForeignKey(Transportmode,null=True, blank=True, related_name = "sale_transport_mode", verbose_name='రవాణా పధ్ధతి')
	sale_where_marketed = models.CharField(max_length=255,null=True, blank=True, verbose_name='అమ్మిన స్థలం')
	month_sowing = models.CharField(max_length=255,null=True, blank=True, verbose_name='విత్తిన నెల')
	production_grain = models.FloatField(null=True, blank=True, verbose_name='ధాన్యం ఉత్పత్తి')
	household_consumpion_grain = models.FloatField(null=True, blank=True, verbose_name='ఇంటి వాడకం - ధాన్యం')
	extent = models.FloatField(null=True, blank=True, verbose_name='భూమి ఎంత?')
	s_no = models.ForeignKey(Numbers,null=True, blank=True, verbose_name='వ.సం')
	sale_other_marketing_costs = models.FloatField(null=True, blank=True, verbose_name='మార్కెట్ ఖర్చులు')
	sale_month_disposal = models.CharField(max_length=255,null=True, blank=True, verbose_name='అమ్మిన నెల')
	sale_by_products_amt = models.FloatField(null=True, blank=True, verbose_name='అమ్మిన గడ్డి పరిమాణం')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Inputs(models.Model):
	inputs_used= models.ForeignKey(Yesorno, related_name ="inputs_used")
	irrigation_charges_source = models.ForeignKey(Irrigationsource,null=True, blank=True, related_name = "irrigation_charges_source")
	fertiliser_transport_mode = models.ForeignKey(Transportmode,null=True, blank=True, related_name = "fertiliser_transport_mode")
	household = models.ForeignKey(Base)
	crop = models.ForeignKey(Crop,null=True, blank=True, related_name = "crop")
	manure_purchased_qty = models.FloatField(null=True, blank=True,)
	fertiliser_transport_costincurred = models.FloatField(null=True, blank=True,)
	seeds_purchased_price = models.FloatField(null=True, blank=True,)
	irrigation_charges_price = models.FloatField(null=True, blank=True,)
	manure_home_value = models.FloatField(null=True, blank=True,)
	household_number = models.FloatField()
	manure_purchased_cost = models.FloatField(null=True, blank=True,)
	fertiliser_type = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type")
	manure_purchased_price = models.FloatField(null=True, blank=True,)
	fertiliser_qty = models.FloatField(null=True, blank=True,)
	advice_regarding_cultivation = models.CharField(max_length=1255,null=True, blank=True,)
	manure_transport_mode = models.ForeignKey(Transportmode,null=True, blank=True, related_name = "manure_transport_mode")
	seeds_home_qty = models.FloatField(null=True, blank=True,)
	manure_transport_costincurred = models.FloatField(null=True, blank=True,)
	fertiliser_cost = models.FloatField(null=True, blank=True,)
	s_no = models.ForeignKey(Numbers,null=True, blank=True,)
	manure_home_qty = models.FloatField(null=True, blank=True,)
	manure_home_cost = models.FloatField(null=True, blank=True,)
	plant_protection_value = models.FloatField(null=True, blank=True, verbose_name=u'కలుపు / పురుగు మందుల ఖర్చు రూ ॥')
	seeds_purchased_qty = models.FloatField(null=True, blank=True,)
	
	fertiliser_type_one = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_one")
	fertiliser_price_one = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_one = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_two = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_two")
	fertiliser_price_two = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_two = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_three = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_three")
	fertiliser_price_three = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_three = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_four = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_four")
	fertiliser_price_four = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_four = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_five = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_five")
	fertiliser_price_five = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_five = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_six = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_six")
	fertiliser_price_six = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_six = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_seven = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_seven")
	fertiliser_price_seven = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_seven = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_type_eight = models.ForeignKey(Fertilisertype,null=True, blank=True, related_name = "fertiliser_type_eight")
	fertiliser_price_eight = models.CharField(max_length=255,null=True, blank=True,)
	fertiliser_qty_eight = models.CharField(max_length=255,null=True, blank=True,)
	manure_type_one = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_type_one")
	manure_home_qty_one = models.CharField(max_length=255,null=True, blank=True,)
	manure_type_two = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_type_two")
	manure_home_qty_two = models.CharField(max_length=255,null=True, blank=True,)
	manure_type_three = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_type_three")
	manure_home_qty_three = models.CharField(max_length=255,null=True, blank=True,)
	manure_type_four = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_type_four")
	manure_home_qty_four = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_type_one = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_purchased_type_one")
	manure_purchased_price_one = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_qty_one = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_type_two = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_purchased_type_two")
	manure_purchased_price_two = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_qty_two = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_type_three = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_purchased_type_three")
	manure_purchased_price_three = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_qty_three = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_type_four = models.ForeignKey(Manuretype,null=True, blank=True, related_name = "manure_purchased_type_four")
	manure_purchased_price_four = models.CharField(max_length=255,null=True, blank=True,)
	manure_purchased_qty_four = models.CharField(max_length=255,null=True, blank=True,)
	comments= models.CharField(max_length=1255, null= True, blank=True)

	
	def __str__(self):
                return str(self.household)

class Specifiedproduction(models.Model):
	implements_owned = models.ForeignKey(Yesorno, related_name = "implements_owned")
	ownership_yearpurchase = models.ForeignKey(Year,null=True, blank=True, related_name = "ownership_yearpurchase", verbose_name=u'యాజమాన్యం కొన్న సంవత్సరం ')
	household_number = models.FloatField()
	maintenance_charges_lastyear = models.FloatField(null=True, blank=True,verbose_name=u'గత సంవత్సరం నిర్వహణ ఖర్చులు ')
	household = models.ForeignKey(Base)
	comments = models.CharField(max_length=255,null=True, blank=True, verbose_name=u'కామెంట్స్ ')
	ownership_subsidy_received = models.FloatField(null=True, blank=True,verbose_name=u'యాజమాన్యం ప్రభుత్వ సబ్సిడీ ')
	ownership_number = models.ForeignKey(Numbers,null=True, blank=True, related_name = "ownership_number", verbose_name= u'యాజమాన్యం సంఖ్య ')
	itemcode = models.ForeignKey(Itemcode,null=True, blank=True, related_name = "itemcode")
	ownership_presentvalue = models.FloatField(null=True, blank=True,verbose_name=u'యాజమాన్యం ప్రస్తుత విలువ ')
	rental_earnings_units = models.FloatField(null=True, blank=True,verbose_name=u'అద్దె ద్వారా ఆదాయం ఎ పనిముట్టు ఎన్ని రోజులు? ')
	rental_earnings = models.FloatField(null=True, blank=True,verbose_name=u'అద్దె ద్వారా ఆదాయం సంపాదన ')
	ownership_pricepaid_perunit = models.FloatField(null=True, blank=True,verbose_name=u'యాజమాన్యం ఒకోక్కదని ఖరీదు')
	def __str__(self):
                return str(self.household)

class Tubewells(models.Model):
	tubewell_owned = models.ForeignKey(Yesorno, related_name ="tubewell_owned")
	operated_other_sale_totalrevenue = models.FloatField(null=True, blank=True,verbose_name= u'ఇతర రైతులకిచ్చిన సాగు నీరు నీటి అమ్మకం రాబడి')
	operated_other_crop = models.ForeignKey(Crop,null=True, blank=True, related_name = "operated_other_crop", verbose_name= u'ఇతర రైతులకిచ్చిన సాగు నీరు పంట ')
	household_number = models.FloatField()
	depth_present = models.FloatField(null=True, blank=True,verbose_name= u'ఇప్పుడున్న లోతు ')
	household = models.ForeignKey(Base)
	depth_installed = models.FloatField(null=True, blank=True,)
	comments = models.CharField(max_length=255,null=True, blank=True, verbose_name= u'కామెంట్స్ ')
	operated_other_sale_area = models.FloatField(null=True, blank=True,verbose_name= u'ఇతర రైతులకిచ్చిన సాగు నీరు భూమి విస్తీర్ణం ')
	year_installed = models.ForeignKey(Year,null=True, blank=True, related_name = "year_installed", verbose_name= u'ఏ సంవత్సరం బిగించారు ')
	maintanence_last_year = models.FloatField(null=True, blank=True,verbose_name= u'గత సంవత్సరం నిర్వహణా ఖర్చులు ')
	total_earnings = models.FloatField(null=True, blank=True,verbose_name= u'నికారదాయం ')
	cost_installation = models.FloatField(null=True, blank=True,verbose_name= u'బిగించడానికి అయిన ఖర్చు ')
	type = models.ForeignKey(Tubewelltype,null=True, blank=True, related_name = "type", verbose_name= u'కరెంటు / డిజిఎల్ ')
	s_no = models.ForeignKey(Numbers,null=True, blank=True, related_name = "s_no", verbose_name= u'వ. నెం ')
	def __str__(self):
                return str(self.household)

class Othercosts(models.Model):
	amount_spent = models.FloatField(verbose_name=u'ఖర్చు')
	household = models.ForeignKey(Base)
	household_number = models.FloatField()
	item_code = models.ForeignKey(Itemcode, related_name = "item_code", verbose_name=u'పేరు ')
	comments = models.CharField(max_length=255, verbose_name=u'కామెంట్స్ /నోట్స్ ')
	def __str__(self):
                return str(self.household)

class Managerpayments(models.Model):
	payments_inkind = models.CharField(max_length=255, verbose_name= u'చేలింపులు వస్తు రూపంలో విలువ')
	household_number = models.FloatField()
	employ_longterm_lastyear = models.ForeignKey(Yesorno, related_name = "employ_longterm_lastyear", verbose_name= u'గత సంవత్సరం పాలేరు / జీతగాడు / గాసగడుని నియమించారా ?')
	household = models.ForeignKey(Base)
	payments_incash = models.FloatField(verbose_name= u'చెలింపులు నగదు ')
	comments = models.CharField(max_length=255, verbose_name= u'కామెంట్స్ ')
	number_months = models.FloatField(verbose_name= u'గత సంవత్సరం అన్ని నెలలు పెట్టుకున్నారు')
	name_worker = models.CharField(max_length=255, verbose_name= u'కార్మికుని పేరు ')
	payments_total = models.FloatField(verbose_name= u'మొత్తం ')
	since_when = models.CharField(max_length=255,verbose_name= u' ఎప్పటి నుంచి నియమించారు ')
	employ_manager_lastyear = models.ForeignKey(Yesorno, related_name = "employ_manager_lastyear",verbose_name= u'గత సంవత్సరం మేనేజర్ ను నియమించారా ?')
	caste = models.ForeignKey(Caste, related_name = "caste", verbose_name= u'కార్మికుని కులం ')
	def __str__(self):
                return str(self.household)

class Longtermworker(models.Model):
	workedas_longtermworker = models.ForeignKey(Yesorno, related_name = "workedas_longtermworker") 
	illness_get_help = models.ForeignKey(Yesorno,null=True, blank=True, related_name = "illness_get_help", verbose_name=u'జబ్బు చేసిన ,ప్రమాదం జరిగిన మీ యజమాని సహాయం చేస్తాడా ?')
	household = models.ForeignKey(Base)
	tasks_performed_two = models.ForeignKey(Tasksperformed,null=True, blank=True, related_name = "tasks_performed_two")
	number_months = models.FloatField(null=True, blank=True,verbose_name=u'గత సంవత్సరం ఎన్ని నెలలు పాలేరుగా ఉన్నాడు ')
	name_worker = models.CharField(max_length=255,null=True, blank=True, verbose_name=u'పాలేరు పేరు  ')
	total = models.FloatField(null=True, blank=True,verbose_name=u'సంపాదన మొత్తం విలువ ')
	earning_cash = models.FloatField(null=True, blank=True,verbose_name=u'సంపాదన నగదు రూపం లో ')
	household_number = models.FloatField()
	occupation_manager = models.ForeignKey(Occupation,null=True, blank=True, related_name = "occupation_manager", verbose_name=u'యజమాని వృత్తి ')
	subjectd_harassments_describe = models.CharField(max_length=255,null=True, blank=True, verbose_name=u'వేధింపులకు గురయ్యారా? వివరించండి ')
	land_leasedin_mortin = models.FloatField(null=True, blank=True,verbose_name=u'భూమి కౌలుకు తీసుకునది ')
	illness_get_help_text = models.CharField(max_length=255,null=True, blank=True, verbose_name=u' జబ్బు చేసిన ,ప్రమాదం జరిగిన మీ యజమాని సహాయం చేస్తాడా ? వివరించండి ')
	tasks_performed_three = models.ForeignKey(Tasksperformed,null=True, blank=True,)
	working_from = models.ForeignKey(Time,null=True, blank=True, related_name = "working_from")
	caste_manager = models.ForeignKey(Caste,null=True, blank=True, related_name = "caste_manager", verbose_name=u'యజమాని కులం ')
	earning_kind = models.FloatField(null=True, blank=True,verbose_name=u'సంపాదన వస్తు రూపం లో ')
	get_number_days_off = models.ForeignKey(Numbers,null=True, blank=True, related_name = "get_number_days_off", verbose_name=u'సెలవులు ఉన్నాయ ? సెలవులు ఉంటే నెలకు ఎన్ని?')
	subjected_harassments = models.ForeignKey(Yesorno,null=True, blank=True, related_name = "subjected_harassments", verbose_name=u'వేధింపులకు గురయ్యారా?')
	other_business_activities = models.ForeignKey(Otheractivities,null=True, blank=True, related_name = "other_business_activities", verbose_name=u'ఇతర వ్యాపారాలు ')
	land_leasedout_mortout = models.FloatField(null=True, blank=True,verbose_name=u'భూమి కౌలుకు ఇచ్చినది ')
	working_to = models.ForeignKey(Time,null=True, blank=True, related_name = "working_to")
	tasks_performed_one = models.ForeignKey(Tasksperformed,null=True, blank=True, related_name = "tasks_performed_one")
	land_owned = models.FloatField(null=True, blank=True,verbose_name=u'భూమి స్వంతం')
	name_manager = models.CharField(max_length=255,null=True, blank=True, verbose_name=u'యజమాని పేరు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

