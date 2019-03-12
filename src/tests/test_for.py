import os
import shutil

from template.arguments import Arguments
from template.template import Template

TEMPLATES_REPOSITORY = "src/tests/templates/"
TEMPLATE = "template_test_for"
OUTPUT_DIRECTORY = "src/tests/output/test_for/"

if os.path.exists(OUTPUT_DIRECTORY):
    shutil.rmtree(OUTPUT_DIRECTORY)
os.makedirs(OUTPUT_DIRECTORY)

template = Template(TEMPLATES_REPOSITORY)
template.template = TEMPLATE
template.configure()
template.process(OUTPUT_DIRECTORY)
