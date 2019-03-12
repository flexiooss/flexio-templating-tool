import json
import re

from consolecolors.fg import Fg
from consolecolors.print_color import PrintColor


class Arguments:

    def __init__(self):
        self.arguments = {}

    def choose(self, template):
        json_data = open(template.path() + "/template.json").read()

        data = json.loads(json_data)
        self.arguments = {}
        for arg in data.get("arguments"):
            default_value = arg.get("defaultValue")
            if default_value is not None and default_value[0] == '@':
                default_value = self.arguments.get(default_value[1:])
            argument = arg.get("argument")
            value = self.get_input_value(arg, argument, default_value)
            self.arguments.__setitem__(argument, value)

    def get_input_value(self, arg, argument, default_value):
        if default_value is None:
            value = input(argument + " : ")
            if len(value) == 0:
                PrintColor.log(Fg.FAIL.value + argument + " should not be empty and has no default value")
                return self.get_input_value(arg, argument, default_value)
        else:
            value = input(argument + " [" + default_value + "] : ")
            if len(value) == 0:
                value = default_value
        regex = arg.get("format")
        if regex is not None:
            if not re.match(regex, value):
                PrintColor.log(Fg.FAIL.value + argument + "should match expression " + regex)
                return self.get_input_value(arg, argument, default_value)
        return value

    def print_colored(self):
        for key in self.arguments.keys():
            if self.arguments.get(key) is None:
                PrintColor.log(Fg.WARNING.value + key + " has no value")
            PrintColor.log(Fg.NOTICE.value + key + Fg.RESET.value + " : " + self.arguments.get(key))
