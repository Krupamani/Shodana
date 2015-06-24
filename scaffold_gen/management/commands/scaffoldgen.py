from django.core.management.base import BaseCommand, CommandError
from django.db import models
import os,inspect
from optparse import make_option

class Color(object):
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BOLD = '\033[1m'

    @staticmethod
    def pad(string, bold = False):
        if bold:
            return Color.UNDERLINE + Color.BOLD + string + Color.END

        return Color.UNDERLINE + string + Color.END



class Command(BaseCommand):
    args = "<model_full_qualified_name>"
    help = "Generates ROR style scaffolds"
    option_list = BaseCommand.option_list + (
        make_option('--admin',
            action='store_true',
            dest='admin',
            default=False,
            help='Generate admin.py'),
        make_option('--aadmin',
            action='store_true',
            dest='aadmin',
            default=False,
            help='Generate admin.py'),
        make_option('--view',
            action='store_true',
            dest='view',
            default=False,
            help='Generate views.py'),
        )


    def gen_view(self, model_name, model_p):
#        print model_name, model_p
        app_name = model_p[0]
        model_name = model_p[-1]
        views_path = app_name + "/views.py" 
        urls_path = app_name + "/urls.py"
#        print views_path, urls_path
        views_file = None
        views_mode = ""
        urls_file = None
        urls_mode = ""
        vprepend = ""
        uprepend = "" 
        new_content = ""
        
        if (not os.path.exists(urls_path)):
            self.stdout.write(Color.pad("{urls_path} not found, I am creating it".format(**locals()),True))
            uprepend = "from django.conf.urls import patterns, url\nfrom {package} import views".format(package = app_name)
#            print prepend
            urls_mode = "new"
        else:
            self.stdout.write(Color.pad("{urls_path} found, Generating new urls".format(**locals()),True))
            urls_mode = "old"
            urls_content = open(urls_path).read()
#            print urls_content
            new_content = ""
            for ind in range(1,len(urls_content)+1):
                if urls_content[-ind] == ')': 
                    new_content = urls_content[:-ind]
                    break 
        
        index_url = "url(r'^{model}s/$',views.{model}_index,name='{model}_index')".format(model = model_name.lower())
        create_url = "url(r'^{model}s/create/$',views.{model}_create,name='{model}_create')".format(model = model_name.lower())
        detail_url = "url(r'^{model}s/(?P<id>\d+)/$',views.{model}_detail,name='{model}_detail')".format(model = model_name.lower())
        update_url = "url(r'^{model}s/(?P<id>\d+)/update/$',views.{model}_update,name='{model}_update')".format(model = model_name.lower())
        delete_url = "url(r'^{model}s/(?P<id>\d+)/delete/$',views.{model}_delete,name='{model}_delete')".format(model = model_name.lower())

        uwrite = new_content  + "\n\n"
        if urls_mode == "new":
            uwrite = uprepend + "\n" + "urlpatterns = patterns('',\n"

        self.stdout.write(Color.pad("Generating {model}/ url".format(model = model_name.lower()),True))
        uwrite += "\t #/{app_name}s/{model}s/\n".format(app_name = app_name,model = model_name.lower())
        uwrite += "\t" + index_url + ",\n"

        self.stdout.write(Color.pad("Generating {model}/detail url".format(model = model_name.lower()),True))
        uwrite += "\t #/{app_name}s/{model}s/5\n".format(app_name = app_name,model = model_name.lower())
        uwrite += "\t" + detail_url + ",\n"

        self.stdout.write(Color.pad("Generating {model}/update url".format(model = model_name.lower()),True))
        uwrite += "\t #/{app_name}s/{model}s/5/update\n".format(app_name = app_name,model = model_name.lower())
        uwrite += "\t" + update_url + ",\n"

        self.stdout.write(Color.pad("Generating {model}/delete url".format(model = model_name.lower()),True))
        uwrite += "\t #/{app_name}s/{model}s/5/delete\n".format(app_name = app_name,model = model_name.lower())
        uwrite += "\t" + delete_url + ",\n"

        self.stdout.write(Color.pad("Generating {model}/create url".format(model = model_name.lower()),True))
        uwrite += "\t #/{app_name}s/{model}s/create/\n".format(app_name = app_name,model = model_name.lower())
        uwrite += "\t" + create_url + ",\n"
        uwrite += ")"
        
    
        
        with open(urls_path,"w") as u:
            u.write(uwrite)
        self.stdout.write(Color.pad("Generated URLS",True))

#        print uwrite
        

        # print index_url
        # print detail_url 
        # print create_url
        # print update_url
        # print delete_url

        if (not os.path.exists(views_path)):
            self.stdout.write("{views_path} not found, I am creating it".format(**locals()))
            views_mode = "w"
            vprepend = "from django.shortcuts import render\nfrom django.http import HttpResponse\nfrom {package} import *\n".format(package = app_name+".models")
 
        else: 
            views_mode = "a" 
            vprepend = "\n"
        
        # Generating the index
        self.stdout.write(Color.pad("Generating {model}_index view".format(model = model_name.lower())))
        index_code = "def {model}_index(request):\n\treturn HttpResponse('You are @ {model}/index')\n".format(model = model_name.lower())
        self.stdout.write(Color.pad("Generating {model}_detail view".format(model = model_name.lower())))
        detail_code = "def {model}_detail(request,id):\n\treturn HttpResponse('You are @ {model}/detail')\n".format(model = model_name.lower())
        self.stdout.write(Color.pad("Generating {model}_create view".format(model = model_name.lower()),True))
        create_code = "def {model}_create(request):\n\treturn HttpResponse('You are @ {model}/create')\n".format(model = model_name.lower())
        self.stdout.write(Color.pad("Generating {model}_update view".format(model = model_name.lower()),True))
        update_code = "def {model}_update(request, id):\n\treturn HttpResponse('You are @ {model}/update')\n".format(model = model_name.lower())
        self.stdout.write(Color.pad("Generating {model}_delete view".format(model = model_name.lower()),True))
        delete_code = "def {model}_delete(request, id):\n\treturn HttpResponse('You are @ {model}/delete')\n".format(model = model_name.lower())

        # print vprepend
        # print index_code
        # print detail_code
        # print create_code
        # print update_code
        # print delete_code
        
        views_code = vprepend + index_code + detail_code + update_code + create_code + delete_code
        with open(views_path, views_mode) as v:
            v.write(views_code)
            
        self.stdout.write(Color.pad("Generated Views",True))
        
            
        
    def handle(self, *args, **options):
        if len(args) < 1:
            self.stdout.write("Usage, <model_full_qualified_name>")
            return None
        model_name = args[0]
        model_p = args[0].split(".")
        app_name = model_p[0]
        app_o = models.get_app(app_name)
#        print models.get_models(app_o)
        model_list = [model.__module__ + "." + model.__name__ for model in models.get_models(app_o)]

        if options["admin"] or options['aadmin']:
            self.stdout.write("Note :: You must have the line \"{line}\" at the top of {filename}. \nThis program will not add it".format(line = "from "+ model_p[0] +".models import *", filename=model_p[0] + "/admin.py" ))
            self.stdout.write("Note :: This program will not check for duplicate registration")
            if (not os.path.exists(app_name + "/admin.py")):
                self.stdout.write("{app_name}/admin.py not found, I am creating it.".format(**locals()))
                a_file = open(app_name + "/admin.py","w") 
                prepend =  "from django.contrib import admin"
                prepend += "from {mname} import *".format(mname = ".".join(model_p[1:]))
                a_file.write(prepend)
                
            else: 

                if options['admin']:
                    if model_name not in model_list:
                        self.stderr.write("No such model : {model_name} found. Have you registered your app in settings.py ?".format(**locals()))
                        return None

                    with open(app_name + "/admin.py","a") as f: 
                        prefix = ".".join(model_p[:-1])
                        f.write("\nadmin.site.register({mname})".format(mname = model_p[-1]))
                        self.stdout.write("Done !!")
                else:
                    with open(app_name + "/admin.py","a") as f:
 #                       from django.db.models import get_app, get_models
#                        app = models.get_app(app_name)
 #                       modellist = models.get_models(app)
                        field_file = open(args[1])
                        fields = {}
                        for line in field_file.readlines():
                            line = line.strip("\n\t ")
                            if line not in [""]:
                                line = line.split(" ")
                                fielddata = []
                                for field in line[2:]:
                                    fielddata.append(field.strip(" ").split(":")[0])
                                
                                fields[line[0].strip(" ")+".models."+line[1].strip(" ")]=fielddata
                                
                        for model in model_list:
                            self.stdout.write("Generating "+model)
                            admin_class_name = model.split('.')[-1]+"Admin"
                            admin_class_content = "class "+admin_class_name+"(admin.ModelAdmin):"
                                                        
                            field_list = "("
                            for field in fields[model]:
                                field_list += "'"+field+"',"
#                            field_list = field_list[:-1]
                            field_list += ")"
                            admin_class_content += "\n\tfields="+field_list
                            f.write(admin_class_content)
         #                   self.stdout.write(admin_class_content)

                            f.write("\nadmin.site.register({mname},{mclass})\n\n".format(mname = model.split('.')[-1], mclass=admin_class_name))
          #                  self.stdout.write("\nadmin.site.register({mname},{mclass})".format(mname = model.split('.')[-1], mclass=admin_class_name))

        elif options["view"]:
#            pass
            self.gen_view(model_name,model_p)
