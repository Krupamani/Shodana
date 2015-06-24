from django.db import models
#-*- coding: utf-8 -*- 
# Create your models here.
class Village(models.Model):
	name = models.CharField(verbose_name='గ్రామము', max_length=255)
	def __str__(self):
		return self.name 
class Mandal(models.Model):
	name = models.CharField(verbose_name='మండలం', max_length=255)
	def __str__(self):
                return self.name

class District(models.Model):
	name = models.CharField(verbose_name='జిల్లా', max_length=255)
	def __str__(self):
                return self.name

class Sex(models.Model):
	name = models.CharField(verbose_name='లింగము ', max_length=255)
	def __str__(self):
                return self.name

class Caste(models.Model):
	name = models.CharField(verbose_name='కులం' , max_length=255)
	def __str__(self):
                return self.name

class Year(models.Model):
	name = models.CharField(verbose_name='సంవత్సరము' , max_length=255)
	def __str__(self):
                return self.name

class Religion(models.Model):
	name = models.CharField(verbose_name='మతం' , max_length=255)
	def __str__(self):
                return self.name

class Yesorno(models.Model):
	name = models.CharField(verbose_name='అవును లేదా కాదు' , max_length=255)
	def __str__(self):
                return self.name

class Numbers(models.Model):
	name = models.IntegerField(verbose_name='సంఖ్యలు' , max_length=255)
	def __str__(self):
                return str(self.name)
        
class Relationship(models.Model):
	name = models.CharField(verbose_name='సంబంధాలు' , max_length=255)
	def __str__(self):
                return self.name

class Maritalstatus(models.Model):
	name = models.CharField(verbose_name='వైవాహిక స్థితి' , max_length=255)
	def __str__(self):
                return self.name

class Literarystatus(models.Model):
	name = models.CharField(verbose_name='సాహిత్య స్థాయిి' , max_length=255)
	def __str__(self):
                return self.name

class Educationlevel(models.Model):
	name = models.CharField(verbose_name='విద్య స్థాయి' , max_length=255)
	def __str__(self):
                return self.name

class Occupation(models.Model):
        name = models.CharField(verbose_name='ఉపాది' , max_length=255)
        def __str__(self):
                return self.name

class Base(models.Model):
	name_of_household = models.CharField(max_length=255, verbose_name = u'కుటుంబ యజామాని పేరు ' )
	household_number = models.IntegerField(verbose_name= u'కుటుం బ సం ఖ్య ' )
	phone = models.CharField(max_length=255, verbose_name= u'టెలిఫొన్ నంబరు')
	age = models.ForeignKey(Numbers, verbose_name= u'వయస్సు ')
	address = models.CharField(max_length=255, verbose_name= u'చిరునామా ')
	father_occupation = models.ForeignKey(Occupation,   verbose_name= u' తం డ్రి వృత్తి')
	tehisil_of_birth = models.CharField(max_length=255, verbose_name= u'పుట్టిన గ్రామం ')
	sex = models.ForeignKey(Sex,  verbose_name= u'లింగము')
	religion = models.ForeignKey(Religion,  verbose_name= u'మతము')
	scorst = models.ForeignKey(Yesorno,  verbose_name=  u'యస్.సి లేదా యస్.టి లేదా బి.సి')
	father_name = models.CharField(max_length=255, verbose_name= u'తం డ్రి పేరు ')
	village = models.ForeignKey(Village, verbose_name = u'గ్రామం ')
	year_migration = models.ForeignKey(Year, verbose_name= u'వలస వచ్చిన సంవత్సరం ')
	mandal = models.ForeignKey(Mandal, verbose_name= u'మండలం ')
	caste = models.ForeignKey(Caste, verbose_name= u'కులం')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return self.name_of_household

class Hhmembers(models.Model):
	name_location_institute = models.CharField(max_length=255, verbose_name= u'పిల్లలు చదువుతున్న సంస్థ పేరు ')
	household_number = models.FloatField(verbose_name= u'కుటుంబ సం ఖ్య ')
	occupations_one = models.ForeignKey(Occupation,related_name =' occupations_one', verbose_name= u'ఊపాది1')
	occupations_two = models.ForeignKey(Occupation,related_name =' occupations_two', verbose_name= u'ఊపాది2')
	occupations_three = models.ForeignKey(Occupation,related_name =' occupations_three', verbose_name= u'ఊపాది3')
	age = models.ForeignKey(Numbers, verbose_name= u'వయస్సు ')
	place_of_work_one = models.CharField(max_length=255, verbose_name= u'పని చేసే స్థలం  1')
	place_of_work_two = models.CharField(max_length=255, verbose_name= u'పని చేసే స్థలం  2')
	place_of_work_three = models.CharField(max_length=255, verbose_name= u'పని చేసే స్థలం 3')
	sex = models.ForeignKey(Sex, verbose_name= u'లింగము ')
	marital_status = models.ForeignKey(Maritalstatus,  verbose_name= u'వివహ స్థితి')
	education_level = models.ForeignKey(Educationlevel, verbose_name= u'ఎంత్ వరకు చదువుకున్నరు ')
	relationship_to_head = models.ForeignKey(Relationship, verbose_name= u'కుటుంబ యజమనితో  సంబందం ')
	literary_status = models.ForeignKey(Literarystatus, verbose_name= u'అక్షరాస్యత స్థితి')
	household = models.ForeignKey(Base, verbose_name = u'కుటుంబ యజామాని పేరు ')
	name = models.CharField(max_length=255, verbose_name= u'పేరు ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)
