import os
import shutil

from template.arguments import Arguments
from template.template import Template

TEMPLATES_REPOSITORY = "templates/"
TEMPLATE = "new_template"
OUTPUT_DIRECTORY = "src/tests/output/new_template/"

if os.path.exists(OUTPUT_DIRECTORY):
    shutil.rmtree(OUTPUT_DIRECTORY)
os.makedirs(OUTPUT_DIRECTORY)

arguments = Arguments()
arguments.arguments = {
    "templateName": "aTemplate"
}

arguments.print_colored()
template = Template(TEMPLATES_REPOSITORY)
template.template = TEMPLATE
template.arguments = arguments
template.process(OUTPUT_DIRECTORY)
