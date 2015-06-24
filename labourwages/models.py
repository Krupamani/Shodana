# -*- coding: utf-8 -*-
from django.db import models
from household.models import *
from land.models import *
from landlease.models import *
from cropping.models import *

# Create your models here.
class Agoperation(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Wagetype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Workprogramme(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Obligationtype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Taskdescription(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Collecteditems(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Magency(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Cheatingfaced(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Workdescription(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Animaltype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Animalproduction(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Labourdays(models.Model):
	labour_deployed = models.ForeignKey(Yesorno, related_name ="labour_deployed")
	daily_labour_days_m = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు పని దినాలు పురుషులు')
	s_no = models.ForeignKey(Numbers,null=True, blank=True,)	
	exchange_labour_hours_m = models.FloatField(null=True, blank=True,verbose_name='బదుళ్లు  పని గంటలు పురుషులు ')
	daily_labour_wages_c = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు కూలిరేట్లు  పిల్లలు')
	family_labour_days_m = models.FloatField(null=True, blank=True,verbose_name='కుటుంబశ్రమ పని దినాలు పురుషులు ')
	exchange_labour_hours_c = models.FloatField(null=True, blank=True,verbose_name='బదుళ్లు  పని గంటలు  పిల్లలు ')
	family_labour_hours_w = models.FloatField(null=True, blank=True,verbose_name='కుటుంబశ్రమ పని గంటలు స్త్రీ లు ')
	household = models.ForeignKey(Base)
	daily_labour_hours_m = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు పని గంటలు పురుషులు')
	daily_labour_wages_m = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు కూలిరేట్లు  పురుషులు')
	crop = models.ForeignKey(Crop,null=True, blank=True, verbose_name='పంట ')
	family_labour_hours_m = models.FloatField(null=True, blank=True,verbose_name='కుటుంబశ్రమ పని గంటలు పురుషులు')
	daily_labour_wages_w = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు కూలిరేట్లు  స్త్రీ లు ')
	daily_labour_hours_c = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు పని గంటలు పిల్లలు ')
	daily_labour_days_w = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు పని దినాలు స్త్రీలు ')
	family_labour_hours_c = models.FloatField(null=True, blank=True,verbose_name='కుటుంబశ్రమ పని గంటలు పిల్లలు')
	family_labour_days_w = models.FloatField(null=True, blank=True,verbose_name='కుటుంబశ్రమ పని దినాలు స్త్రీ లు ')
	longterm_labour_hours_c = models.FloatField(null=True, blank=True,)
	household_number = models.FloatField()
	longterm_labour_days_w = models.FloatField(null=True, blank=True,)
	longterm_labour_hours_m = models.FloatField(null=True, blank=True,)
	comments = models.CharField(max_length=255,null=True, blank=True, verbose_name='కామెంట్స్  ')
	longterm_labour_days_m = models.FloatField(null=True, blank=True,)
	longterm_labour_hours_w = models.FloatField(null=True, blank=True,)
	longterm_labour_days_c = models.FloatField(null=True, blank=True,)
	family_labour_days_c = models.FloatField(null=True, blank=True,verbose_name='కుటుంబశ్రమ పని దినాలు పిల్లలు ')
	exchange_labour_days_m = models.FloatField(null=True, blank=True,verbose_name='బదుళ్లు  పని దినాలు  పురుషులు ')
	machine_labourpayment = models.FloatField(null=True, blank=True,verbose_name='యంత్రాలతో పని అయిన ఖర్చు ')
	daily_labour_hours_w = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు పని గంటలు స్త్రీ లు')
	daily_labour_days_c = models.FloatField(null=True, blank=True,verbose_name='దినకూలిలు పని దినాలు  పిల్లలు')
	extent = models.FloatField(null=True, blank=True,verbose_name='విస్తీర్ణ ')
	machine_labour_workhours = models.FloatField(null=True, blank=True,verbose_name='యంత్రాలతో పని గంటలు ')
	exchange_labour_days_w = models.FloatField(null=True, blank=True,verbose_name='బదుళ్లు  పని దినాలు స్త్రీ లు ')
	agricultural_operation = models.ForeignKey(Agoperation,null=True, blank=True, related_name = "agricultural_operation",verbose_name='పని వివరము ')
	exchange_labour_hours_w = models.FloatField(null=True, blank=True,verbose_name='బదుళ్లు  పని గంటలు స్త్రీ లు')
	piece_rated_kind = models.FloatField(null=True, blank=True,)
	exchange_labour_days_c = models.FloatField(null=True, blank=True,verbose_name='బదుళ్లు  పని దినాలు  పిల్లలు')
	piece_rated_cash = models.FloatField(null=True, blank=True,)
	def __str__(self):
                return str(self.household)

class Wages(models.Model):
	is_agricultural_labour = models.ForeignKey(Yesorno, related_name ="is_agricultural_labour")
	labour_days = models.FloatField(null=True, blank=True,verbose_name=u'పని దినాలు ')
	contract_howmany_workers = models.FloatField(null=True, blank=True,verbose_name=u'కాంట్రాక్టు పని అయితే ఎంత మందికి ఇచ్చారు')
	contract_remuniration = models.FloatField(null=True, blank=True,verbose_name='పని పూర్తి చేయడానికి ఇచ్చిన డబ్బు ')
	household_number = models.FloatField()
	contract_total_wage = models.FloatField(null=True, blank=True,verbose_name='మొత్తం కూలి')
	contract_number_acres = models.FloatField(null=True, blank=True,verbose_name=u'కాంట్రాక్టు పని అయితే ఎన్ని ఎకరాలు ')
	type_wage = models.ForeignKey(Wagetype,null=True, blank=True, related_name = "type_wage",verbose_name=u'దిన కూలి /పిన్ రేట్ ')
	wagerates_increased = models.ForeignKey(Yesorno,null=True, blank=True, related_name = "wagerates_increased",verbose_name=u'కూలి రేట్లు పెరిగాయ ?')
	earnings_cash = models.FloatField(null=True, blank=True,)
	crop = models.ForeignKey(Crop,null=True, blank=True,verbose_name=u'పంట ')
	work_hours = models.FloatField(null=True, blank=True,verbose_name=u'పని గంటలు ')
	place_work = models.CharField(max_length=255,null=True, blank=True,verbose_name=u'పని స్థలం ')
	migrations_declined = models.ForeignKey(Yesorno,null=True, blank=True, related_name = "migrations_declined",verbose_name=u'వలసలు తగ్గాయా ?')
	worker_name = models.CharField(max_length=255,null=True, blank=True,verbose_name=u'వ్యవసాయ కూలి పేరు ')
	isthere_change_peasants = models.ForeignKey(Yesorno,null=True, blank=True, related_name = "isthere_change_peasants",verbose_name='మీ యెడల భూమి గల రైతు వైఖరి లో ఏమైన మార్పు కనిపించిందా ?')
	income = models.FloatField(null=True, blank=True,verbose_name=u'పీన్  రేటు /కాంట్రాక్టు అయితే మొత్తం సంపాదన') 
	has_baragaining_power_increased = models.ForeignKey(Yesorno,null=True, blank=True, related_name = "has_baragaining_power_increased",verbose_name=u'రైతులతో వ్యవహరించటం లో మీకు వెసులబతు పెరిగిందా ?')
	operation = models.ForeignKey(Agoperation,null=True, blank=True, related_name = "operation", verbose_name='పని వివరము ')
	household = models.ForeignKey(Base)
	comments= models.CharField(max_length=1255, null= True, blank=True)
	piece_rate_kind = models.ForeignKey(Kind,null=True, blank=True, related_name = "piece_rate_kind")
	def __str__(self):
                return str(self.household)

class Nonaglabour(models.Model):
	wage_rate = models.FloatField(null=True, blank=True,verbose_name=u'కూలి రేటు')
 	workedin_nonag_operation = models.ForeignKey(Yesorno, related_name ="workedin_nonag_operation")
	number_days = models.FloatField(null=True, blank=True,verbose_name=u'పనిదినాలు ')
	type_wage_contract = models.ForeignKey(Wagetype,null=True, blank=True, related_name = "type_wage_contract", verbose_name= u'దినకూలి ')
	description_specify_programme = models.ForeignKey(Workprogramme,null=True, blank=True, related_name = "description_specify_programme",verbose_name=u'పని వివరము ')
	household_number = models.FloatField()
	household = models.ForeignKey(Base)
	place_work = models.CharField(max_length=255,null=True, blank=True,verbose_name=u'పని స్థలము')
	worker_name = models.CharField(max_length=255,null=True, blank=True,verbose_name=u'వ్యవసాయేతర కార్మికుడి పేరు ')
	totalearnings_cash = models.FloatField(null=True, blank=True,)
	work_hours = models.FloatField(null=True, blank=True,verbose_name=u'పని గంటలు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Empfreedom(models.Model):
	household_number = models.FloatField()
	household = models.ForeignKey(Base)
	comments =  models.CharField(max_length=1255, verbose_name= u'కామెంట్స్ ') 
	def __str__(self):
                return str(self.household)

class Incomeother(models.Model):
	household_number = models.FloatField()
	work_description = models.ForeignKey(Workdescription, related_name = "work_description",verbose_name=u'పని వివరము')
	household = models.ForeignKey(Base)
	comments = models.CharField(max_length=255,verbose_name=u'కామెంట్స్ ')
	worker_name = models.CharField(max_length=255,verbose_name=u'పని చేసేవారి పేరు ')
	work_place = models.CharField(max_length=255,verbose_name=u'పని స్థలము ')
	totalnet_earnings = models.FloatField(verbose_name=u'గత సంవత్సరం సంపాదన ')
	earlier_income_kind = models.ForeignKey(Kind,null=True, blank=True, related_name = "earlier_income_kind")	
	def __str__(self):
                return str(self.household)

class Animalsource(models.Model):
	animal_owned = models.ForeignKey(Yesorno, related_name ="animal_owned")
	insurance = models.FloatField(null=True, blank=True,verbose_name=u' ఇన్సురన్సు ')
	labour_charges = models.FloatField(null=True, blank=True,verbose_name=u'కూల్లి ఖర్చు ')
	household_number = models.FloatField()
	s_no = models.ForeignKey(Numbers,null=True, blank=True,)
	feed_purchased = models.FloatField(null=True, blank=True,verbose_name=u'మేత ఖర్చులు కొన్నది ')
	age = models.ForeignKey(Numbers,null=True, blank=True, related_name = "age",verbose_name=u'వయసు ')
	veternary_charges = models.FloatField(null=True, blank=True,verbose_name=u'పశు వైద్య ఖర్చులు ')
	
	rent_for_land = models.FloatField(null=True, blank=True,)
	nu = models.ForeignKey(Numbers,null=True, blank=True, related_name = "nu", verbose_name= u'ఒక దాని విలువ ')
	income_production = models.ForeignKey(Animalproduction,null=True, blank=True, related_name = "income_production", verbose_name= u'ఉత్పత్తి / పని రూ  ॥')
	income_production_one = models.ForeignKey(Animalproduction,null=True, blank=True, related_name = "income_production_one", verbose_name= u'ఉత్పత్తి / పని 1 రూ  ॥')
	income_production_two = models.ForeignKey(Animalproduction,null=True, blank=True, related_name = "income_production_two", verbose_name= u'ఉత్పత్తి / పని 2 రూ  ॥')
	production_work_qty_one = models.FloatField(null=True, blank=True,)
	production_work_qty_two = models.FloatField(null=True, blank=True,)
	production_work_price_one = models.FloatField(null=True, blank=True)
	production_work_price_two = models.FloatField(null=True, blank=True)
	maintanence_buildings = models.FloatField(null=True, blank=True,verbose_name=u'నిర్వహణ ఖర్చులు రూ ')
	others = models.FloatField(null=True, blank=True,verbose_name=u'ఇతరములు ')
	interest_loans_livestock = models.FloatField(null=True, blank=True,verbose_name=u'అప్పుల మీద వడ్డీ ')
	feed_home_grown = models.FloatField(null=True, blank=True,verbose_name=u'మేత ఖర్చులు ఇంటి తయారి ')
	total_present_value = models.FloatField(null=True, blank=True,verbose_name= u'మేత ఖర్చులు మొత్తం విలువ రూ ')
	type = models.ForeignKey(Animaltype,null=True, blank=True, related_name = "type",verbose_name=u' రకము ')
	household = models.ForeignKey(Base)
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

