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
    args = "--file file_name <appname modelname fieldname:fieldtype:fieldargs ..>"
    help = "Generates ROR style scaffolds"
    f_map = {
           "text" : "models.CharField",
           "int" : "models.IntegerField",
           "date" : "models.DateTimeField",
           "f" : "models.ForeignKey"
        }
    option_list = BaseCommand.option_list + (
    make_option('--file',
            action='store_true',
            dest='file',
            default=False,
            help='Read models From File'),)


    def handle(self, *args, **options):
        if len(args) < 2:
            self.stderr.write(Color.UNDERLINE + "Usage, <appname modelname fieldname:fieldtype:fieldargs ..>" + Color.END)
            return None

        app_name = args[0] 
        if (not os.path.exists(app_name)) or (not os.path.isdir(app_name)):
            self.stderr.write(Color.pad("No such app, {app_name} found".format(**locals())))
            return None
        if (not os.path.exists(app_name+"/models.py")):
             self.stderr.write(Color.pad("Models.py not found at {app_name}/".format(**locals())))
             return None
        if options["file"]:
            file_name = args[1]
            if (not os.path.exists(file_name)):
                self.stderr.write(Color.pad("No such file {file_name} found".format(**locals())))
                return None
            else:
                with open(file_name) as model_file:
                    self.stdout.write(Color.pad("Reading file : {file_name}".format(**locals()),True))
                    for line in model_file:
                        line = line.strip("\n")
#                        self.stdout.write(Color.pad(line,True))
                        line = line.split(" ")
                        self.create_model(app_name, line, options)
        else:
            self.create_model(app_name,args[1:],options)

    def create_model(self, app_name,args, options):
        class_name = args[0]
        if ':' in class_name:
            self.stderr.write(Color.pad("Invalid Class name, {class_name}".format(**locals())))
            return None

        class_rep = app_name + ".models." + class_name
#        print models.get_models()
        if class_rep in [model.__module__ + "." + model.__name__ for model in models.get_models()]:
            self.stderr.write(Color.pad("Class : {class_name} already exists".format(**locals())))
            return None

        fields = {}
        for arg in args[1:]:
            if ':' not in arg:
                self.stderr.write(Color.pad("Invalid field format, {arg}".format(**locals())))
                return None
            arg = arg.split(":")
            if arg[1] not in self.f_map.keys():
                self.stderr.write("Invalid field type, {type}".format(type=arg[1]))
                return None
            if arg[1] == "text":              
                fields[arg[0]] = self.f_map[arg[1]]+"(max_length=255)"
            elif arg[1] != "f":
                fields[arg[0]] = self.f_map[arg[1]]+"()"
            else: 
                if len(arg) < 3:
                    self.stderr.write(Color.pad("ForeignKey requires modelname, Wrong format: {format}".format(format=":".join(arg))))
                    return None
                fields[arg[0]] = self.f_map[arg[1]]+"("+arg[2]+")"
                
        #import pprint 
        #pprint.pprint(fields)
        
        with open(app_name+"/models.py","a") as f:
           to_write = "class {class_name}(models.Model):\n".format(**locals())
           self.stdout.write(Color.pad("Generating class {class_name}".format(**locals()),True))
           if len(fields) < 1: 
               to_write += "\tpass"
           for field in fields:
               self.stdout.write(Color.pad("Generating field {fname} as {ftype}".format(fname=field,ftype=fields[field])))
               to_write += "\t{fname} = {ftype}\n".format(fname=field,ftype=fields[field])
          
           f.write(to_write)
           self.stdout.write(Color.pad("Done !",True))
           

            
