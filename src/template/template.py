import json
import os
import re

import jinja2

from consolecolors.fg import Fg
from consolecolors.print_color import PrintColor
from consolecolors.style import Style
from template.arguments import Arguments
from template.post_build_task import PostBuildTask

TAG_PATTERN = "([A-Za-z0-9]+)"
FOR_PATTERN = "FOR " + TAG_PATTERN + " in " + TAG_PATTERN + ":(.*)"


class Template:
    def __init__(self, templates_repository):
        self.TEMPLATES_REPOSITORY = templates_repository
        self.template = None
        self.arguments = None

    def process(self, output):
        self.generate(output)
        post_build_task = PostBuildTask()
        post_build_task.process(self, output)
        PrintColor.log(Style.BOLD.value + Fg.SUCCESS.value + "SUCCESS")

    def choose(self):
        template_dirs = os.listdir(self.TEMPLATES_REPOSITORY)
        index = 1
        for template_dir in template_dirs:
            print(index, ":", template_dir)
            index += 1

        self.template = self.get_input_template(template_dirs)

        print()
        PrintColor.log(Style.BOLD.value + Fg.FOCUS.value + '[' + self.template + ']')

    def configure(self):
        self.arguments = Arguments()
        self.arguments.choose(self)

    def confirm(self):
        print()
        PrintColor.log(Style.BOLD.value + Fg.FOCUS.value + '[' + self.template + ']')
        self.arguments.print_colored()
        confirm_input = input("confirm [y/n] ? ")
        if confirm_input == "y" or confirm_input == "Y" or confirm_input == "":
            return True
        return False

    def generate(self, output):
        if not os.path.exists(output):
            os.makedirs(output)
        template_path = self.template_path()
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        template_env = jinja2.Environment(loader=template_loader)

        PrintColor.log(Fg.FOCUS.value + "STARTED TEMPLATE GENERATION")
        for (dir, sub_dirs, files) in os.walk(template_path):
            current_template_directory = dir.replace(template_path, "")
            if len(current_template_directory) == 0:
                continue
            self.create_dir_from_template(output + current_template_directory, output)

            for (template_file) in files:
                template_file_path = dir + "/" + template_file
                template_file_path = template_file_path.replace(template_path + "/", "")
                template_current = template_env.get_template(template_file_path)

                if re.match(FOR_PATTERN, template_file):
                    group = re.search(FOR_PATTERN, template_file)
                    item_tag = group.group(1)
                    items_tag = group.group(2)
                    item_file = group.group(3)

                    items = self.arguments.arguments.get(items_tag).split(' ')
                    for item in items:
                        temp_arguments = self.arguments.arguments.copy()
                        temp_arguments.__setitem__(item_tag, item)

                        output_file_path = output + \
                                           jinja2.Template(current_template_directory).render(
                                               self.arguments.arguments).replace(".", "/") + "/" + \
                                           jinja2.Template(item_file).render(temp_arguments)

                        template_current.stream(temp_arguments).dump(output_file_path)
                        print(Fg.NOTICE.value + "FILE " + Fg.RESET.value + output_file_path.replace("//", "/"))

                else:
                    output_file_path = output + \
                                       jinja2.Template(current_template_directory).render(self.arguments.arguments).replace(".", "/") + "/" + \
                                       jinja2.Template(template_file).render(self.arguments.arguments)

                    template_current.stream(self.arguments.arguments).dump(output_file_path)
                    print(Fg.NOTICE.value + "FILE " + Fg.RESET.value + output_file_path.replace("//", "/").replace(output, ""))

        PrintColor.log(Style.BOLD.value + Fg.SUCCESS.value + "FILES GENERATED")

    def get_input_template(self, template_dirs):
        input_string = input("template : ")
        if not input_string.isnumeric():
            PrintColor.log(Fg.FAIL.value + input_string + " is not a correct template index")
            return self.get_input_template(template_dirs)
        template_index = int(input_string)
        if template_index < 1 or template_index > len(template_dirs):
            PrintColor.log(Fg.FAIL.value + str(template_index) + " is not a correct template index")
            return self.get_input_template(template_dirs)
        else:
            return template_dirs[template_index - 1]

    def path(self):
        return self.TEMPLATES_REPOSITORY + self.template

    def template_path(self):
        return self.path() + "/template"

    def create_dir_from_template(self, directory_path_template, output):
        directory_path_r = jinja2.Template(directory_path_template).render(self.arguments.arguments).replace(".", "/")
        os.makedirs(directory_path_r)
        print(Fg.NOTICE.value + "DIR  " + Fg.RESET.value + directory_path_r.replace("//", "/").replace(output, ""))

    @staticmethod
    def from_argument_file(templates_repository, file):
        json_data = open(file).read()
        data = json.loads(json_data)

        template = Template(data.get("templates_repository"))
        template.template = data.get("template")

        arguments = Arguments()
        arguments.arguments = data.get("arguments")
        template.arguments = arguments

        return template

