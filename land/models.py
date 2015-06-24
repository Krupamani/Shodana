# -*- coding: utf-8 -*-
from django.db import models
from household.models import * 
 
# Create your models here.
class Landtype(models.Model):
	name = models.CharField( null=True, blank=True,verbose_name= 'భూమి రకము', max_length=255)
	def __str__(self):
                return self.name

class Irrigationsource(models.Model):
	name = models.CharField( null=True, blank=True,verbose_name= 'సాగు నీటి వసతి_నీటి వనరు', max_length=255)
	def __str__(self):
                return self.name

class Irrigationflow(models.Model):
	name = models.CharField( null=True, blank=True,verbose_name='సాగు నీటి వసతి_పారుదల', max_length=255)
	def __str__(self):
                return self.name

class Irrigationownship(models.Model):
	name = models.CharField( null=True, blank=True,verbose_name='సాగు నీటి వసతి_యజమాన్యం', max_length=255)
	def __str__(self):
                return self.name

class Aquireland(models.Model):
	name = models.CharField( null=True, blank=True,verbose_name='భూమి విలువ', max_length=255)
	def __str__(self):
                return self.name

class Reasonforsale(models.Model):
	name = models.CharField (null=True, blank=True,verbose_name='అమ్మకానికి కారణం', max_length=255)
	def __str__(self):
                return self.name

class Currentownership(models.Model):
	landowned_or_not = models.ForeignKey(Yesorno, related_name = 'landowned_or_not')
	household_number = models.FloatField(verbose_name= u'కుటుం బ సం ఖ్య ')
	irrigationownship = models.ForeignKey(Irrigationownship, null=True, blank=True,related_name='irrigationownship', verbose_name= u'సాగు నీటి వసతి_యజమాన్యం ')
	irrigationownship_one = models.ForeignKey(Irrigationownship, null=True, blank=True,related_name='irrigationownship_one', verbose_name= u'సాగు నీటి వసతి_యజమాన్యం 1')
	irrigationownship_two = models.ForeignKey(Irrigationownship, null=True, blank=True,related_name='irrigationownship_two', verbose_name= u'సాగు నీటి వసతి_యజమాన్యం 2')
	irrigationownship_three = models.ForeignKey(Irrigationownship, null=True, blank=True,related_name='irrigationownship_three', verbose_name= u'సాగు నీటి వసతి_యజమాన్యం 3')
	household = models.ForeignKey(Base, verbose_name = u'కుటుంబ యజామాని పేరు ')
	how_aquireland = models.ForeignKey(Aquireland ,null=True, blank=True,  verbose_name= u'భూమి ఎలా వచ్హింది')
	extent_of_owned = models.FloatField( null=True, blank=True,  verbose_name= u'స్వంత భుమి(ఎకరాలు)')
	value = models.FloatField( null=True, blank=True,   verbose_name= u'భూమి విలువ')
	patta_for_land = models.ForeignKey(Yesorno, null=True, blank=True,  related_name = 'patta_for_land', verbose_name= u'పట్టా ఉందా లేదా?')
	landtype = models.ForeignKey(Landtype, null=True, blank=True, verbose_name= u'భూమి రకము')
	irrigationflow = models.ForeignKey(Irrigationflow, null=True, blank=True,related_name='irrigationflow', verbose_name= u'సాగు నీటి వసతి_పారుదల')
	irrigationsource = models.ForeignKey(Irrigationsource, null=True, blank=True,related_name='irrigationsource', verbose_name= u'సాగు నీటి వసతి_నీటి వనరు')
	irrigationflow_one = models.ForeignKey(Irrigationflow, null=True, blank=True,related_name='irrigationflow_one', verbose_name= u'సాగు నీటి వసతి_పారుదల1')
        irrigationsource_one = models.ForeignKey(Irrigationsource, null=True, blank=True,related_name='irrigationsource_one', verbose_name= u'సాగు నీటి వసతి_నీటి వనరు1')
	irrigationflow_two = models.ForeignKey(Irrigationflow, null=True, blank=True,related_name='irrigationflow_two', verbose_name= u'సాగు నీటి వసతి_పారుదల2')
        irrigationsource_two = models.ForeignKey(Irrigationsource, null=True, blank=True,related_name='irrigationsource_two', verbose_name= u'సాగు నీటి వసతి_నీటి వనరు2')
	irrigationflow_three = models.ForeignKey(Irrigationflow, null=True, blank=True,related_name='irrigationflow_three', verbose_name= u'సాగు నీటి వసతి_పారుదల3')
        irrigationsource_three = models.ForeignKey(Irrigationsource, null=True, blank=True, related_name='irrigationsource_three', verbose_name= u'సాగు నీటి వసతి_నీటి వనరు3')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Landsold(models.Model):
 	land_sold_or_not = models.ForeignKey(Yesorno, related_name = 'land_sold_or_not')
	buyer_name = models.CharField(null=True, blank=True,max_length=255, verbose_name= u'కొన్నవారు పేరు')
	household_number = models.FloatField(verbose_name= u'కుటుంబ సంఖ్య')
	price_land = models.FloatField(null=True, blank=True,verbose_name= u'యాకరం ధర')
	type_of_land = models.ForeignKey(Landtype,null=True, blank=True, verbose_name= u'భూమి రకము')
	year_of_sale = models.ForeignKey(Year,null=True, blank=True, verbose_name= u'అమ్మిన సంవత్సరం ')
	household = models.ForeignKey(Base, verbose_name = u'కుటుంబ యజామాని పేరు ')
	buyer_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name= u'కొన్నవారు_వౄతి')
	buyer_place_residence = models.CharField(null=True, blank=True,max_length=255, verbose_name= u'కొన్నవారు_ఊరు')
	buyer_catse = models.ForeignKey(Caste,null=True, blank=True, verbose_name= u'కొన్నవారు_కులం ')
	extent = models.FloatField(null=True, blank=True,verbose_name= u'విస్తీర్ణము')
	reason_for_sale = models.ForeignKey(Reasonforsale,null=True, blank=True, verbose_name= u'అమ్మాటానికి కారణాలు')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Landbought(models.Model):
	land_bought_or_not = models.ForeignKey(Yesorno, related_name = 'land_bought_or_not')
	seller_catse = models.ForeignKey(Caste,null=True, blank=True, verbose_name= u'అమ్మిననారు_కులం ')
	seller_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name= u'అమ్మిననారు_వౄతి')
	household_number = models.FloatField(verbose_name= u'కుటుంబ సంఖ్య')
	seller_name = models.CharField(max_length=255,null=True, blank=True, verbose_name= u'అమ్మిననారు_పేరు')
	price_land = models.FloatField(null=True, blank=True,verbose_name= u'యాకరం ధర')
	type_of_land = models.ForeignKey(Landtype,null=True, blank=True, verbose_name= u'భూమి రకం ')
	household = models.ForeignKey(Base, verbose_name = u'కుటుంబ యజామాని పేరు ')
	comments = models.CharField(max_length=255,null=True, blank=True, verbose_name= u'కామెంట్స్')
	extent = models.FloatField(null=True, blank=True,verbose_name= u'విస్తీర్ణము ')
	seller_place_residence = models.CharField(max_length=255,null=True, blank=True, verbose_name= u'అమ్మినవారు_ఊరు')
	year_of_purchase = models.ForeignKey(Year,null=True, blank=True, verbose_name= u'కొన్న  సంవత్సరం')
	income_source = models.CharField(max_length=255,null=True, blank=True, verbose_name = u'ఆదాయ వనరు ')
	def __str__(self):
                return str(self.household)
