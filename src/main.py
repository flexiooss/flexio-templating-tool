import argparse
import os

from template.template import Template
from template.git_templates_provider import GitTemplatesProvider

output_directory = "output/"
templates_repository = "/tmp/templates/templates/"

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=not os.path.exists(templates_repository))
group.add_argument('--dir', type=str, help='template directory')
group.add_argument('--git', type=str, help='template git repository')
parser.add_argument('--out', type=str, help='output directory')
parser.add_argument('--args', type=str, help='arguments file')
args = parser.parse_args()

if args.__getattribute__("dir") is not None:
    templates_repository = args.__getattribute__("dir") + "/templates/"
elif args.__getattribute__("git") is not None:
    template_provider = GitTemplatesProvider(args.__getattribute__("git"))
    templates_repository = template_provider.get_directory() + "/templates/"

if args.__getattribute__("out") is not None:
    output_directory = args.__getattribute__("out")


if args.__getattribute__("args") is not None:
    template = Template.from_argument_file(templates_repository, args.__getattribute__("args"))
else:
    template = Template(templates_repository)
    template.choose()

    confirm = False
    while not confirm:
        template.configure()
        confirm = template.confirm()

template.process(output_directory)
