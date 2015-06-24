# -*- coding: utf-8 -*-
from django.db import models
from household.models import *
from land.models import *
from landlease.models import *
from cropping.models import *
from labourwages.models import *
from housing.models import *
# Create your models here.
class Class(models.Model):
	name = models.CharField(max_length=255, verbose_name= 'పేరు')
	def __str__(self):
                return self.name

class Mergeoption(models.Model):
	name = models.CharField( max_length=255)
	def __str__(self):
                return self.name


class Expmonthly(models.Model):
	electronics_cable_value = models.FloatField(verbose_name= u'కేబుల్ కనెక్షన్ విలువ')
	food_rice_outside = models.FloatField(verbose_name= u'బియ్యం  బయటకొన్నవి ')
	soaps_paste_peryear = models.FloatField(verbose_name= u'సబ్బులు,షాంపులు,టూత్పేస్ట్లు-')
	roti_noofdays = models.FloatField(verbose_name= u'రొట్టెలు')
	food_pulse_price = models.FloatField(verbose_name= u'పప్పులు బయటకొన్నవి రేటు ')
	household = models.ForeignKey(Base)
	eggs_noofdays = models.FloatField(verbose_name= u'గుడ్లు')
	milk_noofdays = models.FloatField(verbose_name= u'పాలు')
	entertainment_movies = models.FloatField(verbose_name= u'సినిమాలు-')
	entertainment_tours = models.FloatField(verbose_name= u'యాత్రలు')
	socialcustoms_festivals = models.FloatField(verbose_name= u'పండగలు')
	food_milk_outside = models.FloatField(verbose_name= u'పాలు  బయటకొన్నవి ')
	socialcustoms_funerals = models.FloatField(verbose_name= u'కర్మకాండ')
	socialcustoms_childnaming = models.FloatField(verbose_name= u'బారసాల')
	nookalasankati_noofdays = models.FloatField(verbose_name= u'నూకల సంకటి')
	pindivantalu_noofdays = models.FloatField(verbose_name='పిండి వంటలు ')
	ragimudda_noofdays = models.FloatField(verbose_name='రాగి ముద్ద ')
	household_number = models.FloatField(verbose_name= u'ఇంటి కోడ్')
	socialcustoms_onifunctions = models.FloatField(verbose_name= u'ఓని ఫంక్షన్')
	food_vegtbles_price = models.FloatField(verbose_name= u'కూరగాయలు బయటకొన్నవి రేటు')
	food_sugar_ration = models.FloatField(verbose_name= u'చక్కెర రేషన్షాపు నుండి కి.గ్రా  ')
	entertainment_liquor = models.FloatField(verbose_name= u'మద్యం, సారా-')
	food_kerosene_outside = models.FloatField(verbose_name= u'కిరోసిన్  బయటకొన్నవి ')
	food_spices_price = models.FloatField(verbose_name= u'తాలింపు దినుసులు రేటు ')
	food_kerosene_price = models.FloatField(verbose_name= u'కిరోసిన్ బయటకొన్నవి రేటు ')
	food_eggs_price = models.FloatField(verbose_name= u'గుడ్లు  బయటకొన్నవి రేటు ')
	buttermilk_noofdays = models.FloatField(verbose_name= u'మజ్జిగ')
	meat_noofdays = models.FloatField()
	karam_noofdays = models.FloatField(verbose_name= u'కారం')
	cloths_per_year = models.FloatField(verbose_name= u'బట్టలు-సంవత్సరానికి, ఎలక్త్రానిక్స్ గూడ్స్- సంవత్సరానికి  ')
	food_wheat_ration = models.FloatField(verbose_name= u'గోధుమలు  రేషన్షాపు నుండి కి.గ్రా ')
	food_eggs_outside = models.FloatField(verbose_name= u'గుడ్లు  బయటకొన్నవి ')
	food_oil_ration = models.FloatField(verbose_name= u'నూనె రేషన్షాపు నుండి ')	
	food_oil_price = models.FloatField(verbose_name= u'నూనె బయటకొన్నవి రేటు ')
	food_meat_price = models.FloatField(verbose_name= u'మాంసము బయటకొన్నవి రేటు')
	food_pulse_ration = models.FloatField(verbose_name= u'పప్పులు రేషన్షాపు నుండి కి.గ్రా ')
	food_rice_ration = models.FloatField(verbose_name= u'బియ్యం రేషన్షాపు నుండి కి.గ్రా ')
	curds_noofdays = models.FloatField(verbose_name= u'పెరుగు')
	food_vegtbles_outside = models.FloatField(verbose_name= u'కూరగాయలు  బయటకొన్నవి ')
	food_milk_price = models.FloatField(verbose_name= u'పాలు బయటకొన్నవి రేటు ')
	food_pulse_outside = models.FloatField(verbose_name= u'పప్పులు  బయటకొన్నవి ')
	pappu_noofdays = models.FloatField(verbose_name= u'పప్పు')
	food_sugar_price = models.FloatField(verbose_name= u'చక్కెర బయటకొన్నవి రేటు ')
	food_meat_outside = models.FloatField(verbose_name= u'మాంసము  బయటకొన్నవి ')
	food_kerosene_ration = models.FloatField(verbose_name= u'కిరోసిన్ రేషన్షాపు నుండి కి.గ్రా ')
	entertainment_smoking = models.FloatField(verbose_name= u'సిగరెట్లు')
	rice_noofdays = models.FloatField(verbose_name= u'అన్నం')
	food_wheat_price = models.FloatField(verbose_name= u'గోధుమలు బయటకొన్నవి రేటు ')
	food_oil_outside = models.FloatField(verbose_name= u'నూనె  బయటకొన్నవి ')
	socialcustoms_templefairs = models.FloatField(verbose_name= u'జాతరలు ')
	food_sugar_outside = models.FloatField(verbose_name= u'చక్కెర  బయటకొన్నవి ')
	family_withoutfood_noofdays = models.FloatField(verbose_name= u'మీరు సంవత్సరంలో ఎప్పుడైనా పస్తులున్నారా? ఉంటే సంవత్సరంలో ఎన్నిరోజులు?')
	food_rice_price = models.FloatField(verbose_name= u'బియ్యం బయటకొన్నవి రేటు ')
	pachhadi_noofdays = models.FloatField(verbose_name= u'పచ్చడి')
	current_bill = models.FloatField()
	socialcustoms_marriages = models.FloatField(verbose_name= u'పెళ్ళిళ్ళు')
	kuralu_noofdays = models.FloatField(verbose_name= u'కూరలు')
	entertainment_cockfights = models.FloatField(verbose_name= u'కోళ్ళపందాలు')
	food_spices_outside = models.FloatField(verbose_name= u'తాలింపు దినుసులు  బయటకొన్నవి')
	food_wheat_outside = models.FloatField(verbose_name= u'గోధుమలు  బయటకొన్నవి')
	entertainment_playcards = models.FloatField(verbose_name= u'పేకాట')
	socialcustoms_birthday = models.FloatField(verbose_name= u'జన్మదినాలు')
	cylinder = models.FloatField(verbose_name= u'సిలిండర్ ')
	phone = models.FloatField(verbose_name= u'ఫోన్')
	shaving_cutting = models.FloatField(verbose_name= u'షేవింగ్ / కటింగ్')	
	house_rent = models.FloatField()
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)


class Expeducation(models.Model):
	household_number = models.FloatField(verbose_name= u'ఇంటి కోడ్')
	school_fee = models.FloatField(verbose_name= u'సంవత్సరానికి_స్కూలు/కాలేజి/యూనివర్సిటీ ఫీజు')
	age = models.ForeignKey(Numbers, verbose_name= u'చదివే పిల్లలు_వయస్సు')
	govt_or_private = models.CharField(max_length=255, verbose_name= u'చదివే పిల్లలు_ప్రభుత్వ/ప్రైవేటు')
	books_fee = models.FloatField(verbose_name= u'సంవత్సరానికి_పుస్తకాలు/స్టేషనరీ  ')
	studentclass = models.ForeignKey(Class, related_name = "studentclass", verbose_name= u'చదివే పిల్లలు_తరగతి')
	travel_expenses = models.FloatField(verbose_name= u'సంవత్సరానికి_ప్రయాణఖర్చులు')
	child_name = models.CharField(max_length=255, verbose_name= u'విద్యార్ధి పేరు ')
	total_expenses = models.FloatField(verbose_name= u'మొత్తం ఖర్చు ')
	tuition_fee = models.FloatField(verbose_name= u'ట్యూషన్ ఫీజు ')
	household = models.ForeignKey(Base)
	student_name = models.CharField(max_length=255, verbose_name= u'విద్యార్ధి పేరు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Exphealth(models.Model):
	name_familymember = models.CharField(max_length=255, verbose_name= u'కుటుంబ సభ్యులు ')
	household_number = models.FloatField(verbose_name= u'ఇంటి కోడ్')
	household = models.ForeignKey(Base)
	govt_or_private = models.CharField(max_length=255,verbose_name= u'ప్రభుత్వ/ప్రయివేటు అస్పత్రి/ ఆర్_ఎం_పి' )
	illness = models.CharField(max_length=255, verbose_name= u'జబ్బు /ప్రమాదం ')
	expendutre_morgaging_selling_land_gold_loan = models.ForeignKey(Mergeoption, verbose_name= u'వైద్యం ఖర్చులకోసం ఏమి చేసారు?')
	others = models.CharField(max_length=255)
	cost_of_treatment = models.FloatField(verbose_name= u'అయిన ఖర్చు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Migration(models.Model):
	out_migration = models.CharField(max_length=255,verbose_name= u'గ్రామం నుండి బయటకు')
	in_migration = models.CharField(max_length=255,verbose_name= u'గ్రామం లోనికి')
	shortterm_to = models.CharField(max_length=255,verbose_name= u'స్వల్పకాలిక వలసలు నెలలు_వరకు ')
	household_number = models.FloatField(verbose_name= u'ఇంటి కోడ్')
	longterm_from = models.CharField(max_length=255,verbose_name= u'దీర్ఘకాలిక వలసలు సంవత్సరాలలో_నుండి')
	shortterm_from = models.CharField(max_length=255,verbose_name= u'స్వల్పకాలిక వలసలు నెలలు_నుండి')
	household = models.ForeignKey(Base,)
	destination_country = models.CharField(max_length=255, verbose_name= u'వలసపోయిన ప్రాంతం _దేశము')
	name_migrant = models.CharField(max_length=255, verbose_name= u'వలసదారుని పేరు')
	longterm_to = models.CharField(max_length=255,verbose_name= u'దీర్ఘకాలిక వలసలు సంవత్సరాలలో_వరకు')
	reason_migration = models.CharField(max_length=255, verbose_name= u'వలసకు కారణాలు ')
	destination_town = models.CharField(max_length=255, verbose_name= u'వలసపోయిన ప్రాంతం _పట్టణం ')
	destination_village = models.CharField(max_length=255, verbose_name= u'వలసపోయిన ప్రాంతం _గ్రామం')
	s_no = models.ForeignKey(Numbers,)
	comments= models.CharField(max_length=1255, null= True, blank=True)
	sufficient_meet_needs = models.ForeignKey(Yesorno, related_name = "sufficient_meet_needs",  verbose_name= u'దీనితో మీ అవసరాలు తీర్చుకోగల్గుతున్నారా?')
	using_this_amount = models.CharField(max_length=255,  verbose_name= u'ఈ డబ్బును దేనికి వాడుతున్నారు')
	annual_inflow = models.FloatField( verbose_name= u'సంవత్సరానికి అందుతున్న డబ్బు')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	haveyou_bought_assets = models.CharField(max_length=255,  verbose_name= u'ఈ డబ్బు తో ఆస్తులు ఏమన్నా కొన్నారా?')
	def __str__(self):
                return str(self.household)

class Invistigators(models.Model):
	is_furtherinv_needed = models.ForeignKey(Yesorno, related_name = "is_furtherinv_needed",  verbose_name= u'పరిశీలన అవసరమా?')
	household_number = models.FloatField( verbose_name= u'ఇంటి కోడ్ ')
	time_taken_for_interview = models.FloatField( verbose_name= u'ఎంతకాలం పట్టింది')
	household = models.ForeignKey(Base, related_name = "household",)
	name_of_invistigator = models.CharField(max_length=255, verbose_name= u'ఎన్యూమరేటరు పేరు’')
	data_entry_by = models.CharField(max_length=255,  verbose_name= u'డేటా ఎంట్రీ బై')
	comments_observations = models.CharField(max_length=2550000, )
	date_of_interview = models.CharField(max_length=255, verbose_name= u'ఇంటర్వ్యూతేది')
	date_data_entry = models.CharField(max_length=255, verbose_name= u'ఎంట్రీ తేది ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)
