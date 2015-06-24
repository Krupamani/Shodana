# -*- coding: utf-8 -*-
from django.db import models
from household.models import * 
from land.models import * 

# Create your models here.
class Registration(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Contracttype(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Kind(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Period(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Percent(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
                return self.name

class Landtanent(models.Model):
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	total = models.FloatField(verbose_name='మొత్తం (య॥ )')
	sharedrent = models.FloatField(verbose_name='పాలుకు ఎంత (య॥ )')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	fixedrent = models.FloatField(verbose_name='కౌలుకు ఎంత (య॥ )')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Landleasedin(models.Model):
	tenant_or_not = models.ForeignKey(Yesorno, related_name ="tenant_or_not")
	input_owner_machinary = models.FloatField(null=True, blank=True, verbose_name='ఇతర యంత్రాలు')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	input_owner_pumpset = models.FloatField(null=True, blank=True, verbose_name='పంపు సెట్టు')
	input_owner_seed = models.FloatField(null=True, blank=True, verbose_name='విత్తనాలు')
	annual_fixedrent_cash = models.FloatField(null=True, blank=True, verbose_name='కౌలు - నగదు రూపం')
	landowner_name = models.CharField(max_length=255,null=True, blank=True, verbose_name='భూయజమాని పేరు')
	loan_fromowner_interestfree = models.FloatField(null=True, blank=True, verbose_name='భూయజమాని ఇచ్చిన ఋణం (వడ్డీ లేకుండా)')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	landowner_caste = models.ForeignKey(Caste,null=True, blank=True, verbose_name='భూయజమాని కులం')
	input_owner_pesticide = models.FloatField(null=True, blank=True, verbose_name='పురుగు మందులు')
	loan_fromowner_withinterest = models.FloatField(null=True, blank=True, verbose_name='భూయజమాని ఇచ్చిన ఋణం (వడ్డీ తో)')
	tenurial_registration = models.ForeignKey(Registration,null=True, blank=True, verbose_name='కౌలు - రిజిస్టర్ అయ్యిందా? లేదా?')
	input_owner_fertiliser = models.FloatField(null=True, blank=True, verbose_name='రసాయన ఎరువులు')
	tenurial_contracttype = models.ForeignKey(Contracttype,null=True, blank=True, verbose_name='కౌలు - ఒప్పందం కాల పరిమితి')
	extent = models.FloatField(null=True, blank=True, verbose_name='భూమి - ఎంత')
	qty_hay_byowner = models.FloatField(null=True, blank=True, verbose_name='కౌలు - వస్తు రూపం (గడ్డి)')
	input_owner_electricity = models.FloatField(null=True, blank=True, verbose_name='కరెంటు')
	annual_fixedrent_kind = models.ForeignKey(Kind,null=True, blank=True, verbose_name='కౌలు - వస్తు రూపం (ముఖ్య ఉత్పత్తి)')
	input_owner_manure = models.FloatField(null=True, blank=True, verbose_name='సేంద్రియ ఎరువులు')
	landowner_extent_landholding = models.FloatField(null=True, blank=True, verbose_name='భూయజమానికున్న మొత్తం భూమి',)
	landtype = models.ForeignKey(Landtype,null=True, blank=True, verbose_name='భూమి - రకం',)
	tenurial_sincewhen = models.CharField(max_length=255,null=True, blank=True, verbose_name='కౌలు - ఎప్పడి నుంచి')
	landowner_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name='భూయజమాని వృత్తి')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Landleaser(models.Model):
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	total = models.FloatField(verbose_name='మొత్తం (య॥ )')
	sharedrent = models.FloatField(verbose_name='పాలుకు ఎంత (య॥ )')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	fixedrent = models.FloatField(verbose_name='కౌలుకు ఎంత (య॥ )')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Landleasedout(models.Model):
	leaseout_or_not = models.ForeignKey(Yesorno, related_name ="leaseout_or_not")
	household = models.ForeignKey(Base, verbose_name = 'కుటుంబ యజమాని పేరు')
	input_you_pesticide = models.FloatField(null=True, blank=True, verbose_name = 'పురుగు మందులు')
	input_you_pumpset = models.FloatField(null=True, blank=True, verbose_name = 'పంపు సెట్టు')
	annual_fixedrent_cash = models.FloatField(null=True, blank=True, verbose_name = 'కౌలు - నగదు రూపం')
	landtype = models.ForeignKey(Landtype,null=True, blank=True,  verbose_name = 'భూమి - రకం')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	landtenant_name = models.CharField(max_length=255,null=True, blank=True, verbose_name = 'కౌలురైతు పేరు')
	input_you_seed = models.FloatField(null=True, blank=True, verbose_name = 'విత్తనాలు')
	input_you_machinary = models.FloatField(null=True, blank=True, verbose_name = 'ఇతర యంత్రాలు')
	input_you_fertiliser = models.FloatField(null=True, blank=True, verbose_name = 'రసాయన ఎరువులు')
	input_you_manure = models.FloatField(null=True, blank=True, verbose_name = 'సేంద్రియ ఎరువులు')
	tenurial_registration = models.ForeignKey(Registration,null=True, blank=True, verbose_name = 'కౌలు - రిజిస్టర్ అయ్యిందా? లేదా?')
	tenurial_contracttype = models.ForeignKey(Contracttype,null=True, blank=True, verbose_name = 'కౌలు - ఒప్పందం కాల పరిమితి')
	extent = models.FloatField(null=True, blank=True, verbose_name = 'భూమి - ఎంత')
	landtenant_extent_landholding = models.FloatField(null=True, blank=True, verbose_name = 'భూయజమానికున్న మొత్తం భూమి')
	annual_fixedrent_kind = models.ForeignKey(Kind,null=True, blank=True, verbose_name = 'కౌలు - వస్తు రూపం (ముఖ్య ఉత్పత్తి)')
	landtenant_caste = models.ForeignKey(Caste,null=True, blank=True, verbose_name = 'కౌలురైతు కులం')
	loan_fromyou_withinterest = models.FloatField(null=True, blank=True, verbose_name = 'భూయజమాని ఇచ్చిన ఋణం (వడ్డీ తో)')
	loan_fromyou_interestfree = models.FloatField(null=True, blank=True, verbose_name = 'భూయజమాని ఇచ్చిన ఋణం (వడ్డీ లేకుండా)')
	qty_hay_bytenant = models.FloatField(null=True, blank=True, verbose_name = 'కౌలు - వస్తు రూపం (గడ్డి)')
	landtenant_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name = 'కౌలురైతు వృత్తి')
	input_you_electricity = models.FloatField(null=True, blank=True, verbose_name = 'కరెంటు')
	tenurial_sincewhen = models.CharField(max_length=255,null=True, blank=True, verbose_name = 'కౌలు - ఎప్పడి నుంచి')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Mortgagedin(models.Model):
	mortgagedin_or_not = models.ForeignKey(Yesorno, related_name ="mortgagedin_or_not")
	businessman_caste = models.ForeignKey(Caste,null=True, blank=True, verbose_name='కుదువ పెట్టించుకున్న వారి కులం')
	interest = models.FloatField(null=True, blank=True, verbose_name='వడ్డీ రేటు')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	year_mortgage = models.CharField(max_length=255,null=True, blank=True, verbose_name='కుదువపెట్టిన సంవత్సరం')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	businessman_name = models.CharField(max_length=255,null=True, blank=True, verbose_name='కుదువ పెట్టించుకున్న వారి పేరు')
	businessman_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name='కుదువ పెట్టించుకున్న వారి వృత్తి')
	mortgage_period = models.ForeignKey(Period,null=True, blank=True, verbose_name='కుదువ కాలం')
	extent = models.FloatField(null=True, blank=True, verbose_name='భూమి - ఎంత')
	landtype = models.ForeignKey(Landtype,null=True, blank=True, verbose_name='భూమి - రకం')
	mortgage_amount = models.FloatField(null=True, blank=True, verbose_name='కుదువ డబ్బు')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Mortgagedout(models.Model):
	mortgagedout_or_not = models.ForeignKey(Yesorno, related_name ="mortgagedout_or_not")
	year_mortgage = models.CharField(max_length=255,null=True, blank=True, verbose_name='కుదువపెట్టిన సంవత్సరం')
	interest = models.FloatField(null=True, blank=True,)
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	mortgagee_caste = models.ForeignKey(Caste,null=True, blank=True, verbose_name='కుదువ  పెట్టినవారి కులం')
	mortgagee_name = models.CharField(max_length=255,null=True, blank=True, verbose_name='కుదువ పెట్టినవారి  పేరు')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	mortgage_period = models.ForeignKey(Period,null=True, blank=True, verbose_name='కుదువ కాలం')
	extent = models.FloatField(null=True, blank=True, verbose_name='భూమి - ఎంత')
	landtype = models.ForeignKey(Landtype,null=True, blank=True, verbose_name='భూమి - రకం')
	mortgagee_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name='కుదువపెట్టినవారి వృత్తి')
	mortgage_amount = models.FloatField(null=True, blank=True, verbose_name='కుదువ డబ్బు')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Sharerentin(models.Model):
	sharedin_or_not = models.ForeignKey(Yesorno, related_name ="sharedin_or_not")
	input_owner_machinary_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_machinary_percent', verbose_name='ఇతర యంత్రాలు (%)')
	input_owner_machinary_rs = models.FloatField(null=True, blank=True, verbose_name='ఇతర యంత్రాలు (నగదు)')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	period = models.ForeignKey(Period,null=True, blank=True, verbose_name='పాలు - ఒప్పందం కాల పరిమితి')
	since_when_leased = models.CharField(max_length=255,null=True, blank=True, verbose_name='పాలు - ఎప్పడి నుంచి')
	landowner_name = models.CharField(max_length=255,null=True, blank=True, verbose_name='భూయజమాని పేరు')
	input_owner_manure_rs = models.FloatField(null=True, blank=True, verbose_name='సేంద్రియ ఎరువులు (నగదు)')
	household_number = models.FloatField( verbose_name='కుటుంబ సంఖ్య')
	input_owner_labor_rs = models.FloatField(null=True, blank=True, verbose_name='శ్రమ (నగదు)')
	landowner_caste = models.ForeignKey(Caste,null=True, blank=True, verbose_name='భూయజమాని కులం')
	input_owner_elec_rs = models.FloatField(null=True, blank=True, verbose_name='కరెంటు (నగదు)')
	input_owner_pump_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_pump_percent', verbose_name='పంపు సెట్టు (%)')
	input_owner_pest_rs = models.FloatField(null=True, blank=True, verbose_name='పురుగు మందులు (నగదు)')
	input_owner_seed_rs = models.FloatField(null=True, blank=True, verbose_name='విత్తనాలు (నగదు)')
	owner_share_hay_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'owner_share_percent', verbose_name='గడ్డిలో యజమాని భాగం (%)')
	input_owner_fert_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_fert_percent', verbose_name='రసాయన ఎరువులు (%)')
	input_owner_elec_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_elec_percent', verbose_name='కరెంటు (%)')
	loan_by_owner_amt = models.FloatField(null=True, blank=True,)
	owner_share_crop_qty = models.FloatField(null=True, blank=True, verbose_name='పంటలో యజమాని భాగం (పరిమాణం)')
	input_owner_labor_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_labor_percent', verbose_name='శ్రమ (%)')
	input_owner_seed_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_seed_percent', verbose_name='విత్తనాలు (%)')
	input_owner_fert_rs = models.FloatField(null=True, blank=True, verbose_name='రసాయన ఎరువులు (నగదు)')
	owner_share_crop_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'owner_share_crop_percent', verbose_name='పంటలో యజమాని భాగం  (%)')
	extent = models.FloatField(null=True, blank=True, verbose_name='భూమి - ఎంత')
	input_owner_pest_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_pest_percent', verbose_name='పురుగు మందులు (%)')
	loan_by_owner_interestfree = models.FloatField(null=True, blank=True, verbose_name='అప్పు- వడ్డీ లేకుండా')
	loan_by_owner_interest = models.FloatField(null=True, blank=True, verbose_name='వడ్డీతో అప్పు')
	loan_by_owner_rateofinterest = models.FloatField(null=True, blank=True, verbose_name='వడ్డీ రేటు')
	input_owner_manure_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = 'input_owner_manure_percent', verbose_name='సేంద్రియ ఎరువులు (%)')
	landowner_extent_hold = models.FloatField(null=True, blank=True, verbose_name='భూయజమానికున్న మొత్తం భూమి')
	landtype = models.ForeignKey(Landtype,null=True, blank=True, verbose_name='భూమి - రకం')
	owner_share_hay_qty = models.FloatField(null=True, blank=True, verbose_name='గడ్డిలో యజమాని భాగం (పరిమాణం)')
	input_owner_pump_rs = models.FloatField(null=True, blank=True, verbose_name='పంపు సెట్టు (నగదు)')
	registered_or_not = models.ForeignKey(Registration,null=True, blank=True, verbose_name='పాలు - రిజిస్టర్ అయ్యిందా? లేదా?')
	landowner_occupation = models.ForeignKey(Occupation,null=True, blank=True, verbose_name='భూయజమాని వృత్తి')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Sharerentout(models.Model):
	sharedrent_or_not = models.ForeignKey(Yesorno, related_name ="sharedrent_or_not")
	input_you_elec_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_elec_percent", verbose_name='కరెంటు (%)')
	cropper_occupation = models.ForeignKey(Occupation,null=True, blank=True, related_name = "cropper_occupation", verbose_name='పాలురైతు వృత్తి')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	input_you_seed_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_seed_percent", verbose_name='విత్తనాలు (%)')
	period = models.ForeignKey(Period,null=True, blank=True, related_name = "period", verbose_name='పాలు - ఒప్పందం కాల పరిమితి')
	loan_by_you_interestfree = models.FloatField(null=True, blank=True, verbose_name='అప్పు- వడ్డీ లేకుండా')
	loan_by_you_interest = models.FloatField(null=True, blank=True, verbose_name='వడ్డీతో అప్పు')
	loan_by_owner_rateofinterest = models.FloatField(null=True, blank=True, verbose_name='వడ్డీ రేటు')
	since_when_leased = models.CharField(max_length=255,null=True, blank=True, verbose_name='పాలు - ఎప్పడి నుంచి')
	input_you_pest_rs = models.FloatField(null=True, blank=True, verbose_name='పురుగు మందులు (నగదు)')
	input_you_pump_rs = models.FloatField(null=True, blank=True, verbose_name='పంపు సెట్టు (నగదు)')
	tenant_share_hay_qty = models.FloatField(null=True, blank=True, verbose_name='గడ్డిలో పాలురైతు భాగం (పరిమాణం)')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	input_you_elec_rs = models.FloatField(null=True, blank=True, verbose_name='కరెంటు (నగదు)')
	input_you_fert_rs = models.FloatField(null=True, blank=True, verbose_name='రసాయన ఎరువులు (నగదు)')
	input_you_labor_rs = models.FloatField(null=True, blank=True, verbose_name='శ్రమ (నగదు)')
	input_you_fert_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_fert_percent",  verbose_name='రసాయన ఎరువులు (%)')
	cropper_name = models.CharField(max_length=255,null=True, blank=True, verbose_name='పాలురైతు పేరు')
	input_you_machinary_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_machinary_percent",  verbose_name='ఇతర యంత్రాలు (%)')
	input_you_manure_rs = models.FloatField(null=True, blank=True, verbose_name='సేంద్రియ ఎరువులు (నగదు)')
	cropper_caste = models.ForeignKey(Caste,null=True, blank=True, related_name = "cropper_caste", verbose_name='పాలురైతు కులం')
	cropper_extent_hold = models.FloatField(null=True, blank=True, verbose_name='పాలురైతుకున్న మొత్తం భూమి')
	loan_by_you_amt = models.FloatField(null=True, blank=True, verbose_name='')
	input_you_machinary_rs = models.FloatField(null=True, blank=True, verbose_name='ఇతర యంత్రాలు (నగదు)')
	extent = models.FloatField(null=True, blank=True, verbose_name='భూమి - ఎంత')
	tenant_share_crop_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "tenant_share_crop_percent", verbose_name='పంటలో పాలురైతు భాగం  (%)')
	input_you_labor_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_labor_percent", verbose_name='శ్రమ (%)')
	tenant_share_hay_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "tenant_share_hay_percent", verbose_name='గడ్డిలో పాలురైతు భాగం (%)')
	input_you_seed_rs = models.FloatField(null=True, blank=True, verbose_name='విత్తనాలు (నగదు)')
	input_you_manure_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_manure_percent", verbose_name=' సేంద్రియ ఎరువులు (%)')
	tenant_share_crop_qty = models.FloatField(null=True, blank=True, verbose_name='పంటలో పాలురైతు భాగం (పరిమాణం)')
	landtype = models.ForeignKey(Landtype,null=True, blank=True, related_name = "landtype", verbose_name='భూమి - రకం')
	input_you_pump_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_pump_percent", verbose_name='పంపు సెట్టు (%)')
	registered_or_not = models.ForeignKey(Registration,null=True, blank=True, related_name = "registered_or_not", verbose_name='పాలు - రిజిస్టర్ అయ్యిందా? లేదా?')
	input_you_pest_percent = models.ForeignKey(Percent,null=True, blank=True, related_name = "input_you_pest_percent", verbose_name='పురుగు మందులు (%)')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)

class Tenantproblems(models.Model):
	reason_compelled_one = models.CharField(max_length=255, verbose_name='అతనివద్దనే కౌలు ఎందుకుతీసుకొనవలసివచ్చింది 1?')
	inherited_problems = models.ForeignKey(Yesorno, related_name = "inherited_problems", verbose_name='పూర్వికులనుండి వచ్చిన సమస్య?')
	reason_compelled = models.ForeignKey(Yesorno, related_name = "reason_compelled", verbose_name='అతనివద్దనే కౌలు ఎందుకుతీసుకొనవలసివచ్చింది 1?')
	household = models.ForeignKey(Base, verbose_name='కుటుంబ యజమాని పేరు')
	why_wageslow_manage = models.ForeignKey(Yesorno, related_name = "why_wageslow_manage", verbose_name='కూలిద్వారా ఇల్లుగడవలేదా?')
	why_lowrent_profitable = models.ForeignKey(Yesorno, related_name = "why_lowrent_profitable", verbose_name='కౌలు తక్కువ కాబట్టి గిట్టుబాటు అవుతుందా?')
	nonereason_tenant = models.ForeignKey(Yesorno, related_name = "nonereason_tenant")
	why_noskill_urban = models.ForeignKey(Yesorno, related_name = "why_noskill_urban", verbose_name='పట్టణపనులు చేయలేకా?')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	why_tenancy_respectable = models.ForeignKey(Yesorno, related_name = "why_tenancy_respectable", verbose_name=' కౌలు గౌరవప్రదమనా?')
	comments = models.CharField(max_length=255)
	because_debt_to_leaser = models.ForeignKey(Yesorno, related_name = "because_debt_to_leaser", verbose_name='భూయజమానికి బాకీఉన్నారా?')
	loan_landowner_prior_tenancy = models.ForeignKey(Yesorno, related_name = "loan_landowner_prior_tenancy", verbose_name='మీ భూయజమాని వద్ద అప్పుచేశారా?')
	reason_compelled_three = models.CharField(max_length=255, verbose_name='అతనివద్దనే కౌలు ఎందుకుతీసుకొనవలసివచ్చింది ?')
	lack_anyother_option = models.ForeignKey(Yesorno, related_name = "lack_anyother_option", verbose_name='గత్యంతరం లేక?')
	provide_freeservice_owner = models.ForeignKey(Yesorno, related_name = "provide_freeservice_owner", verbose_name='భూయజమానికి ఉచితపనులుచేస్తారా?')
	other_reasons = models.CharField(max_length=255, verbose_name='ఇతర కారణాలు?')
	why_for_foodgrains = models.ForeignKey(Yesorno, related_name = "why_for_foodgrains", verbose_name='ఇంట్లో తిండి గింజల కోసమా?')
	nature_contract_written = models.ForeignKey(Yesorno, related_name = "nature_contract_written", verbose_name='వ్రాతపూర్వకమైన కౌలా?')
	dueto_lack_opportunites = models.ForeignKey(Yesorno, related_name = "dueto_lack_opportunites", verbose_name='వీరే అవకాశాలు దొరకకా?')
	nota_comeout_otherreasons = models.ForeignKey(Yesorno, related_name = "nota_comeout_otherreasons", verbose_name='అప్పువలన బయటికిరాలేకుండా ఉన్నారా?')
	why_inability_wagework = models.ForeignKey(Yesorno, related_name = "why_inability_wagework", verbose_name='కూలికి వలసపోలేకా?')
	reason_compelled_two = models.CharField(max_length=255, verbose_name='అతనివద్దనే కౌలు ఎందుకుతీసుకొనవలసివచ్చింది ?')
	why_ownland_notsufficient = models.ForeignKey(Yesorno, related_name = "why_ownland_notsufficient", verbose_name='స్వంత భూమి చాలకనా?')
	why_opportunity_cattle = models.ForeignKey(Yesorno, related_name = "why_opportunity_cattle", verbose_name='పాడి చేసుకునేందుకా?')
	debt_inherited = models.ForeignKey(Yesorno, related_name = "debt_inherited", verbose_name='అప్పు వంశపారంపర్యమా?')
	nature_contract_verbal = models.ForeignKey(Yesorno, related_name = "nature_contract_verbal", verbose_name='నోటిమాట కౌలా?')
	because_debt_to_leaser_amt = models.FloatField(verbose_name='బాకీ ఎంత?')
	def __str__(self):
                return str(self.household)

class Interlinks(models.Model):
	comodity_labour = models.ForeignKey(Yesorno, related_name = "comodity_labour", verbose_name='సరుకు-శ్రమ')
	household_number = models.FloatField(verbose_name='కుటుంబ సంఖ్య')
	land_labour = models.ForeignKey(Yesorno, related_name = "land_labour", verbose_name='భూమి-శ్రమ')
	household = models.ForeignKey(Base, related_name = "f_household", verbose_name='కుటుంబ యజమాని పేరు')
	inputs_land = models.ForeignKey(Yesorno, related_name = "inputs_land", verbose_name='ఉత్పాదకాలు-భూమి')
	inputs_loans = models.ForeignKey(Yesorno, related_name = "inputs_loans", verbose_name='ఉత్పాదకాలు-ఋణం')
	inputs_commodity = models.ForeignKey(Yesorno, related_name = "inputs_commodity", verbose_name='ఉత్పాదకాలు-సరుకు')
	loans_commodity = models.ForeignKey(Yesorno, related_name = "loans_commodity", verbose_name='ఋణం-సరుకు')
	inputs_labour = models.ForeignKey(Yesorno, related_name = "inputs_labour", verbose_name='ఉత్పాదకాలు - శ్రమ')
	loans_land = models.ForeignKey(Yesorno, related_name = "loans_land", verbose_name='ఋణం-భూమి')
	land_commodity = models.ForeignKey(Yesorno, related_name = "land_commodity", verbose_name='ఋణం-సరుకు')
	loans_labour = models.ForeignKey(Yesorno, related_name = "loans_labour", verbose_name='ఋణం-శ్రమ')
	comments= models.CharField(max_length=1255, null= True, blank=True)
	def __str__(self):
                return str(self.household)
