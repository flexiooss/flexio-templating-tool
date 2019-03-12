import os
import shutil

from template.arguments import Arguments
from template.template import Template

TEMPLATES_REPOSITORY = "templates/"
TEMPLATE = "maven-codingmatters-api-client-only"
OUTPUT_DIRECTORY = "src/tests/output/maven-codingmatters-api-client-only/"

if os.path.exists(OUTPUT_DIRECTORY):
    shutil.rmtree(OUTPUT_DIRECTORY)
os.makedirs(OUTPUT_DIRECTORY)

arguments = Arguments()
arguments.arguments = {
    "artifactId": "test-artifact",
    "groupId": "io.flexio.archetypetest",
    "version": "1.0.0-SNAPSHOT",
    "package": "io.flexio.archetypetest",
    "apiNameCamelCase": "TestArtifact",
    "apiNameTiret": "test-artifact"
}

arguments.print_colored()
template = Template(TEMPLATES_REPOSITORY)
template.template = TEMPLATE
template.arguments = arguments
template.process(OUTPUT_DIRECTORY)
