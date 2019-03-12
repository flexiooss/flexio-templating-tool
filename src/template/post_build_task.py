import json
from subprocess import Popen

from jinja2 import Template

from consolecolors.fg import Fg
from consolecolors.print_color import PrintColor
from consolecolors.style import Style


class PostBuildTask:

    @staticmethod
    def process(template, output):
        json_data = open(template.path() + "/template.json").read()
        tasks = json.loads(json_data).get("postBuildTasks")
        if tasks is None:
            return
        for task in tasks:
            working_directory = output + "/" + Template(task.get("workingDirectory")).render(template.arguments.arguments)
            task_path = template.path() + "/post_build_tasks/" + task.get("script")
            status = Popen(
                [task_path, working_directory]
            ).wait()
            if status == 0:
                PrintColor.log("TASK [" + task.get("task") + "] : " + Fg.NOTICE.value + "SUCCESS")
            else:
                PrintColor.log("TASK [" + task.get("task") + "] : " + Fg.FAIL.value + "FAILURE")

        PrintColor.log(Style.BOLD.value + Fg.SUCCESS.value + "POST BUILD TASKS COMPLETED")

