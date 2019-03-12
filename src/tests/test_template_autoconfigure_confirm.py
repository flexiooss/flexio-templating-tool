import os
import shutil

from template.arguments import Arguments
from template.template import Template

TEMPLATES_REPOSITORY = "templates/"
OUTPUT_DIRECTORY = "src/tests/output/autoconfigure/"

if os.path.exists(OUTPUT_DIRECTORY):
    shutil.rmtree(OUTPUT_DIRECTORY)
os.makedirs(OUTPUT_DIRECTORY)

template = Template(TEMPLATES_REPOSITORY)
template.template = "maven-codingmatters-api"

confirm = False
while not confirm:
    arguments = Arguments()
    arguments.arguments = {
        "artifactId": "test-artifact",
        "groupId": "io.flexio.archetypetest",
        "version": "1.0.0-SNAPSHOT",
        "package": "io.flexio.archetypetest",
        "apiNameCamelCase": "TestArtifact",
        "apiNameTiret": "test-artifact"
    }
    template.arguments = arguments

    confirm = template.confirm()

template.process(OUTPUT_DIRECTORY)
