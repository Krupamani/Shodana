# -*- coding: utf-8 -*-
from django.db import models
from household.models import *
from land.models import *
from landlease.models import *
from cropping.models import *
from labourwages.models import *
# Create your models here.
class Ownedorrented(models.Model):
	name = models.CharField(max_length=255, verbose_name= 'స్వంతమా? అద్దె  ఇల్లా ')
	def __str__(self):
                return self.name

class Cardcolor(models.Model):
	name = models.CharField(max_length=255, verbose_name='కార్డు రంగు' )
	def __str__(self):
                return self.name

class Cardtype(models.Model):
        name = models.CharField(max_length=255, verbose_name= 'కార్డు రకము ')
	def __str__(self):
                return self.name

class Rooftype(models.Model):
	name = models.CharField(max_length=255, verbose_name='పై కప్పు రకం ')
	def __str__(self):
                return self.name

class Walltype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Floortype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Latrinetype(models.Model):
	name = models.CharField(max_length=255, verbose_name='లెట్రిన్ ')
	def __str__(self):
                return self.name

class Electricitytype(models.Model):
	name = models.CharField(max_length=255, verbose_name='ఎలక్ట్రిసిటీ ')
	def __str__(self):
                return self.name

class Sourcecooking_one(models.Model):
	name = models.CharField(max_length=255, verbose_name='వంట చేయుటకు ఏమి వాడుతున్నారు 1')
	def __str__(self):
                return self.name

class Sourcecooking_two(models.Model):
        name = models.CharField(max_length=255, verbose_name='వంట చేయుటకు ఏమి వాడుతున్నారు 2')
        def __str__(self):
                return self.name


class Naturereimbusment(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Interesttype(models.Model):
	name = models.CharField(max_length=255, verbose_name='సాధారణ వడ్డీ /చక్ర వడ్డీ')
	def __str__(self):
                return self.name

class Borrowingsource(models.Model):
	name = models.CharField(max_length=255, verbose_name='రునదాతలు / సంస్థలు ')
	def __str__(self):
                return self.name

class Houbase(models.Model):
	household = models.ForeignKey(Base)
	govtscheme_nature_reimbusment = models.ForeignKey(Naturereimbusment, related_name = "govtscheme_nature_reimbusment", verbose_name= u'ఇంటి స్థలం, ఇల్లు కట్టుకోవటానికి, రిపేరు కు, ప్రభుత్వ సహాయం అందిందా ? దేనికి ఇచ్చరు ')
	value_of_house = models.FloatField(verbose_name= u'ఇంటి విలువ ')
	year_recent_repair = models.ForeignKey(Year, related_name = "year_recent_repair")
	type_roof = models.ForeignKey(Rooftype, related_name = "type_roof", verbose_name=u'పై కప్పు రకం')
	type_wall = models.ForeignKey(Walltype, related_name = "type_wall")
	household_number = models.FloatField()
	source_energy_cooking_one = models.ForeignKey(Sourcecooking_one, related_name = "source_energy_cooking_one", verbose_name=u'వంట చేయుటకు ఏమి వాడుతున్నారు 1')
	source_energy_cooking_two = models.ForeignKey(Sourcecooking_two, related_name = "source_energy_cooking_two", verbose_name=u'వంట చేయుటకు ఏమి వాడుతున్నారు 2')
	electricity = models.ForeignKey(Electricitytype, related_name = "electricity", verbose_name=u'ఎలక్ట్రిసిటీ')
	comments = models.CharField(max_length=255, verbose_name=u'కామెంట్స్ ')
	isthere_kitchen = models.ForeignKey(Yesorno, related_name = "isthere_kitchen", verbose_name= u'వంట గది ప్రత్యేకంగా ఉందా ?')
	availbility_safe_drinking_text = models.CharField(max_length=255, verbose_name=u'మీ  ఇంట్లో  తాగడానికి నీళ్ళు ఏల వస్థాయి ?')
	noof_additional_rooms = models.ForeignKey(Numbers, related_name = "noof_additional_rooms", verbose_name='అదనపు ఉన్న గదుల సంఖ్య')
	owned_or_rented = models.ForeignKey(Ownedorrented, related_name = "owned_or_rented", verbose_name=u'స్వంతమా? అద్దె ఇల్లా' )
	govtscheme_cash = models.FloatField(verbose_name= u'ఇంటి స్థలం, ఇల్లు కట్టుకోవటానికి, రిపేరు కు, ప్రభుత్వ సహాయం అందిందా ? నగదా ఏంత మొత్తం ')
	amount_spending_water = models.FloatField(verbose_name=u'మీ ఇంటి నీటి అవసరాలకు సంవత్సరానికి ఏంత ఖర్ఛు పెడుతున్నారు ?')
	enough_water_text = models.CharField(max_length=255)
	s_no = models.ForeignKey(Numbers,verbose_name=u'వ నం ')
	year_construction = models.ForeignKey(Year, related_name = "year_construction", verbose_name=u'కట్టిన సంవత్సరం ')
	latrine = models.ForeignKey(Latrinetype, related_name = "latrine",verbose_name=u'లెట్రిన్' )
	does_house_have_watertap = models.ForeignKey(Yesorno, related_name = "does_house_have_watertap", verbose_name='మీ ఇంటికి టాప్ ఉన్నదా ?')
	does_village_have_safe_waterfacility = models.ForeignKey(Yesorno, related_name = "does_village_have_safe_waterfacility", verbose_name='గ్రామం లో రక్షిత మంచి నిటి సరఫర  ఏర్పాటు ఉన్నా దా ?')
	type_of_floor = models.ForeignKey(Floortype, related_name = "type_of_floor")
	govtscheme_yes_or_no = models.ForeignKey(Yesorno, related_name = "govtscheme_yes_or_no",verbose_name=u'ఇంటి స్థలం, ఇల్లు కట్టుకోవటానికి, రిపేరు కు, ప్రభుత్వ సహాయం అందిందా ?' )
	isthere_veranda = models.ForeignKey(Yesorno, related_name = "isthere-veranda")
	govtscheme_year = models.ForeignKey(Year, related_name = "govtscheme_year",verbose_name=u'ఇల్లు కట్టుకోవటానికి, రిపేరు కు, ప్రభుత్వ సహాయం అందిందా ? సంవత్సరం ')
	distance_travelled_water = models.FloatField(verbose_name='లేకుంటే ఏంత దూరం నుండి తేస్తారు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Indebtedness(models.Model):
	collateral = models.FloatField(verbose_name = u'సబ్సిడీ ')
	amont_repaid = models.FloatField(verbose_name = u' చెల్లించినది ')
	household_number = models.FloatField()
	amount_outstanding_principal = models.FloatField(verbose_name = u'తిర్చవలసిన మొత్తం  అసలు ')
	amount_outstanding_interest = models.FloatField(verbose_name = u'తిర్చవలసిన మొత్తం వడ్డీ ')
	household = models.ForeignKey(Base)
	source_borrowing = models.ForeignKey(Borrowingsource, related_name = "source_borrowing", verbose_name = u'రునదాతలు / సంస్థలు ')
	purpose_borrowing = models.CharField(max_length=255, verbose_name = u'ఏందుకు రుణం తీసుకున్నారు ')
	month_year = models.CharField(max_length=255,verbose_name = u'సంవత్సరం')
	thing_indebtedness = models.CharField(max_length=255, verbose_name = u'హామీ ')
	amount_outstanding_total = models.FloatField(verbose_name = u'తిర్చవలసిన మొత్తం మొత్తం ')
	type_interest = models.ForeignKey(Interesttype, related_name = "type_interest", verbose_name = u'సాధారణ వడ్డీ /చక్ర వడ్డీ ')
	rate_interest = models.FloatField(verbose_name = u'వడ్డీ రేటు  సం ॥ నికి  ')
	principal = models.FloatField(verbose_name = u'అసలు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Selfhelpgroups(models.Model):
	period_member = models.ForeignKey(Period, related_name = "period_member", verbose_name=u'సభ్యత్వకల వ్యవది /సభ్యత్వం ఏప్పటి నుండి ?')
	household_number = models.FloatField()
	bank_group_linked = models.CharField(max_length=255, verbose_name=u'బ్యాంకు/ స్వచ్చంద సేవ సంస్థ తో అనుబంధం ')
	household = models.ForeignKey(Base)
	name_group = models.CharField(max_length=255, verbose_name=u'గ్రూప్ పేరు')
	savings_permonth = models.FloatField(verbose_name=u'పొదుపు నెలకి కట్టే డబ్బు ')
	name_group_leader = models.CharField(max_length=255, verbose_name=u' దాని నాయకురాలు ')
	name_member = models.CharField(max_length=255, verbose_name=u'సభ్యుని పేరు ')
	savings_perweek = models.FloatField(verbose_name=u'పొదుపు వారానికి కట్టే డబ్బు ')
	number_members_group = models.ForeignKey(Numbers, related_name = "number_members_group", verbose_name=u'సభ్యుల సం ఖ్య ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Assets(models.Model):
	anyother_land_value = models.FloatField(verbose_name= u'ఇతర భూములు భూమి విలువ')
	transport_car_value = models.FloatField(verbose_name= u'కారు/జీప్ విలువ')
	ponds_tanks_area = models.FloatField(verbose_name= u'కుంట/చెరువు విస్తీర్ణము')
	transport_lorry_no = models.ForeignKey(Numbers, related_name = "transport_lorry_no",verbose_name= u'లారీ సంఖ్య')
	household = models.ForeignKey(Base,)
	electronics_mobile_no = models.ForeignKey(Numbers, related_name = "electronics_mobile_no",verbose_name= u'మొబైల్ ఫోన్ సంఖ్య')
	transport_bullockcart_no = models.ForeignKey(Numbers, related_name = "transport_bullockcart_no")
	transport_lorry_value = models.FloatField(verbose_name= u'లారీ విలువ')
	electronics_mixy_no = models.ForeignKey(Numbers, related_name = "electronics_mixy_no",verbose_name= u'మిక్సీ సంఖ్య')
	electronics_refrigerator_value = models.FloatField(verbose_name= u'రిఫ్రిజరేటర్ విలువ')
	buildings_cattleshed_value = models.FloatField(verbose_name= u'పశువుల కొట్టెం విలువ ')
	electronics_refrigerator_no = models.ForeignKey(Numbers, related_name = "electronics_refrigerator_no",verbose_name= u'రిఫ్రిజరేటర్ సంఖ్య')
	woman_land_patta = models.ForeignKey(Yesorno, related_name = "woman_land_patta")
	durables_tailoringmachine_value = models.FloatField(verbose_name= u'కుట్టు మెషిన్ ')
	durables_kitchenset_no = models.ForeignKey(Numbers, related_name = "durables_kitchenset_no",verbose_name= u'వంటసామానులు సంఖ్య')
	anyother_land_area = models.FloatField(verbose_name= u'ఇతర భూములు విస్తీర్ణము')
	investments_gold_value = models.FloatField(verbose_name= u'గోల్డ్ విలువ')
	investments_silver_value = models.FloatField(verbose_name= u'వెండి విలువ ')
	investments_silver_no =  models.FloatField(verbose_name= u'వెండి సంఖ్య ')
	household_number = models.FloatField()
	durables_wwatch_no = models.ForeignKey(Numbers, related_name = "durables_wwatch_no", verbose_name='గడియారాలు సంఖ్య')
	electronics_mobile_value = models.FloatField(verbose_name= u'మొబైల్ ఫోన్ విలువ')
	electronics_grinder_no = models.ForeignKey(Numbers, related_name = "electronics_grinder_no",verbose_name= u'గ్రైండర్ సంఖ్య')
	investments_chitfunds_value = models.FloatField(verbose_name= u'చిట్-ఫండ్స్ విలువ')
	transport_bullockcart_value = models.FloatField()
	agricultural_land_area = models.FloatField(verbose_name= u'వ్యవసాయ భూమి విస్తీర్ణము')
	electronics_fan_no = models.ForeignKey(Numbers, related_name = "electronics_fan_no", verbose_name= u'సీలింగ్ ఫ్యాన్ సంఖ్య')
	agricultural_land_value = models.FloatField(verbose_name= u'వ్యవసాయ భూమి విలువ ')
	electronics_fan_value = models.FloatField(verbose_name= u'సీలింగ్ ఫ్యాన్ విలువ')
	homestead_land_area = models.FloatField(verbose_name= u'ఇంటిస్థలము విస్తీర్ణము')
	transport_moped_value = models.FloatField(verbose_name= u'మోపెడ్ విలువ')
	durables_kitchenset_value = models.FloatField(verbose_name= u'వంటసామానులు విలువ ')
	durables_wwatch_value = models.FloatField(verbose_name= u'గడియారాలు విలువ')
	durables_tailoringmachine_no = models.ForeignKey(Numbers, related_name = "durables_tailoringmachine_no", verbose_name= u' కుట్టు మెషిన్ సంఖ్య')
	investments_gold_no = models.ForeignKey(Numbers, related_name = "investments_gold_no", verbose_name= u'గోల్డ్ సంఖ్య')
	transport_tractor_value = models.FloatField()
	electronics_ac_value = models.FloatField(verbose_name= u'ఏసి విలువ')
	electronics_dish_no = models.ForeignKey(Numbers, related_name = "electronics_dish_no", verbose_name= u'డిష్ ఆంటెన్నా సంఖ్య')
	woman_land_patta_text = models.CharField(max_length=255)
	buildings_shop_no = models.ForeignKey(Numbers, related_name = "buildings_shop_no", verbose_name= u'షాపులు/వాణిజ్య నిర్మాణాలు సంఖ్య ' )
	electronics_ac_no = models.ForeignKey(Numbers, related_name = "electronics_ac_no", verbose_name= u'ఏసి సంఖ్య')
	durables_handpump_no = models.ForeignKey(Numbers, related_name = "durables_handpump_no", verbose_name= u'హ్యాండుపంపు సంఖ్య')
	durables_biogas_no = models.ForeignKey(Numbers, related_name = "durables_biogas_no", verbose_name= u'బయోగ్యాస్ సంఖ్య')
	transport_other_value = models.FloatField(verbose_name= u'ఇతరములు విలువ')
	buildings_anyother_value = models.FloatField(verbose_name= u'ఇతరత్రా భవనాలు విలువ')
	transport_scooter_no = models.ForeignKey(Numbers, related_name = "transport_scooter_no", verbose_name= u'స్కూటర్/మోటర్సైకిల్ సంఖ్య')
	ponds_tanks_value = models.FloatField(verbose_name= u'కుంట/చెరువు భూమి విలువ ')
	electronics_mixy_value = models.FloatField(verbose_name= u'మిక్సీ విలువ')
	buildings_anyother_no = models.ForeignKey(Numbers, related_name = "buildings_anyother_no",verbose_name= u'ఇతరత్రా భవనాలు సంఖ్య')
	investments_bonds_value = models.FloatField(verbose_name= u'బాండ్లు విలువ')
	electronics_washingmachine_value = models.FloatField(verbose_name= u'వాషింగ్ మెషీన్ విలువ')
	transport_scooter_value = models.FloatField( verbose_name= u'స్కూటర్/మోటర్సైకిల్ విలువ')
	electronics_grinder_value = models.FloatField( verbose_name= u'గ్రైండర్ విలువ')
	transport_bicycle_value = models.FloatField( verbose_name= u'బైసికిల్ విలువ ')
	electronics_colortv_no = models.ForeignKey(Numbers, related_name = "electronics_colortv_no", verbose_name= u'కలర్_టివి సంఖ్య')
	investments_chitfunds_no = models.ForeignKey(Numbers, related_name = "investments_chitfunds_no", verbose_name= u'చిట్-ఫండ్స్ సంఖ్య')
	electronics_colortv_value = models.FloatField( verbose_name= u'కలర్_టివి విలువ ')
	transport_moped_no = models.ForeignKey(Numbers, related_name = "transport_moped_no", verbose_name= u'మోపెడ్ సంఖ్య ')
	buildings_shop_value = models.FloatField( verbose_name= u'షాపులు/వాణిజ్య నిర్మాణాలు  విలువ')
	investments_bonds_no = models.CharField(max_length=255, verbose_name= u'బాండ్లు ')
	transport_bus_value = models.FloatField( verbose_name= u'బస్సు విలువ')
	transport_auto_value = models.FloatField(verbose_name= u'ఆటో విలువ' )	
	transport_auto_no = models.FloatField(verbose_name= u'ఆటో సంఖ్య ' )
	durables_biogas_value = models.FloatField( verbose_name= u'బయోగ్యాస్ విలువ')
	electronics_washingmachine_no = models.ForeignKey(Numbers, related_name = "electronics_washingmachine_no", verbose_name= u'వాషింగ్ మెషీన్ సంఖ్య')
	transport_tractor_no = models.ForeignKey(Numbers, related_name = "transport_tractor_no")
	transport_car_no = models.ForeignKey(Numbers, related_name = "transport_car_no", verbose_name= u'కారు/జీప్ సంఖ్య')
	buildings_cattleshed_no = models.ForeignKey(Numbers, related_name = "buildings_cattleshed_no",verbose_name = u'పశువుల కొట్టెం సంఖ్య ')
	transport_other_no = models.ForeignKey(Numbers, related_name = "transport_other_no", verbose_name= u'ఇతరములు సంఖ్యo')
	transport_bicycle_no = models.ForeignKey(Numbers, related_name = "transport_bicycle_no", verbose_name= u'బైసికిల్ సంఖ్య')
	transport_bus_no = models.ForeignKey(Numbers, related_name = "transport_bus_no", verbose_name= u'బస్సు సంఖ్య')
	electronics_telephone_value = models.FloatField(verbose_name= u'టెలి ఫోన్ విలువ')
	durables_gasstove_value = models.FloatField(verbose_name= u'గాస్-స్టౌవ్ విలువ')
	electronics_telephone_no = models.ForeignKey(Numbers, related_name = "electronics_telephone_no",verbose_name= u'టెలి ఫోన్ సంఖ్య')
	homestead_land_value = models.FloatField(verbose_name= u'ఇంటిస్థలము భూమి విలువ')
	buildings_house_value = models.FloatField(verbose_name= u'ఇళ్ళు విలువ ')
	durables_handpump_value = models.FloatField(verbose_name= u'హ్యాండుపంపు విలువ')
	buildings_house_no = models.ForeignKey(Numbers, related_name = "buildings_house_no", verbose_name= u'ఇళ్ళు సంఖ్య')
	durables_gasstove_no = models.ForeignKey(Numbers, related_name = "durables_gasstove_no", verbose_name= u'గాస్-స్టౌవ్ సంఖ్య')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Govtdistrib(models.Model):
	ration_available_intime = models.ForeignKey(Yesorno, related_name = "ration_available_intime",verbose_name=u'రేషన్ సరుకులు సకాలంలో ఆందుతున్నాయా?')
	ration_weights_perfect = models.ForeignKey(Yesorno, related_name = "ration_weights_perfect",verbose_name=u'రేషన్ తుకాలు, కొలతలుసక్రమంగా వుంటున్నాయా?')
	household_number = models.FloatField()
	number_registered = models.ForeignKey(Numbers, related_name = "number_registered",verbose_name=u'రిజిష్టరు అయిన సభ్యుల సంఖ్య ')
	ration_buy_onetime = models.ForeignKey(Yesorno, related_name = "ration_buy_onetime",verbose_name=u'రేషన్ సరకులన్నీ  ఒకేసారి కొనగలుగుతున్నారా?')
	household = models.ForeignKey(Base)
	reasons_for_nocard = models.CharField(max_length=255,verbose_name=u'కార్డు లెకపోడానికి కారణాలు')
	card_color = models.ForeignKey(Cardcolor, related_name = "card_color",verbose_name=u'కార్డు రంగు')
	ration_reasonable_price = models.ForeignKey(Yesorno, related_name = "ration_reasonable_price",verbose_name=u'రేషన్ సక్రమమైన ధరకు ఇస్తూన్నారా?')
	comments = models.CharField(max_length=255,verbose_name=u'కామెంట్స్')
	card_type = models.ForeignKey(Cardtype, related_name = "card_type",verbose_name=u'కార్డు రకము')
	ration_buy_multipletimes_accept = models.ForeignKey(Yesorno, related_name = "ration_buy_multipletimes_accept",verbose_name=u'రేషన్ కొనలేక పోతే రెండు, మూడు దఫాలుగా తీసుకోడానికి చౌక దుకాణం యజమాని అంగీజరిస్తారా?')
	number_registered_adults = models.ForeignKey(Numbers, related_name = "number_registered_adults",verbose_name=u'రిజిష్టరు అయిన సభ్యుల సంఖ్య పెద్దవాళ్ళు')
	rationcard_exist = models.ForeignKey(Yesorno, related_name = "rationcard_exist",verbose_name=u'మీ కుటుంబానికి రేషన్ కార్డు వుందా?')
	number_registered_kids = models.ForeignKey(Numbers, related_name = "number_registered_kids",verbose_name=u'రిజిష్టరు అయిన సభ్యుల సంఖ్య పిల్లలు')
	ration_available_sufficient = models.ForeignKey(Yesorno, related_name = "ration_available_sufficient",verbose_name=u'రేషన్ ఆందవలసిన మోతాదులో అందుతున్నాయా?')
	def __str__(self):
                return str(self.household)
