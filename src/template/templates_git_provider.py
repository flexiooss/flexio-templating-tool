import os
import shutil
from subprocess import Popen


class TemplatesProvider:

    def __init__(self, git_repository):
        self.target_path = "/tmp/templates"

        if os.path.exists(self.target_path):
            shutil.rmtree(self.target_path)
        os.makedirs(self.target_path)
        Popen(["git", "clone", git_repository, self.target_path, "--quiet"]).wait()

    def get_directory(self):
        return self.target_path
