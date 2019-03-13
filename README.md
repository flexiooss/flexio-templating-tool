# Flexio Templating Tool

## Usage
```bash
./flexio-template-tool.sh (--dir DIR | --git GIT) [--out OUT] [--args ARGS]
```
You have to specify a templates repository. It can be a local directory (`--dir your/repo`), or in a GIT repository (`--git http://your-repo.git`).
The specified repository must contain at its root a directory named `templates` which contains properly formatted templates (see  [Template creation](#template-creation)).  
You can choose an output directory with the `--out` option.  
You can also choose your arguments directly from a file, specified with the `--args` option.
The argument file should be formatted that way :
```json
{
  "template": "your_template_name",
  "arguments": {
    "yourArgument": "argument value"
  }
}
```

## Requirement
* Python 3.7  
* TODO

```bash
apt install python3.7
apt install python3-venv
apt install python3.7-venv
```

## Template creation
A template is composed of 3 files/folders
* [`template.json`](#configuration-file) configuration file
* [`template directory`](#template-directory) 
* [`post_build_tasks`](#post-build-tasks-directory) directory (optional)

You can use the template template (new_template), which is located in this project's git repository, to generate a basic template.

### Configuration file
```json
{
  "arguments":
  [
    {
      "argument": "argumentName",
      "defaultValue": "argument Default Value",
      "format": "^[a-z][\\.a-z0-9]*[a-z0-9]$"
    },
    {
      "argument": "directory",
      "defaultValue": "/dev/null",
      "format": "^[a-z][\\.a-z0-9]*[a-z0-9]$"
    }
  ],
  "postBuildTasks": [
    {
      "task": "Task Name",
      "script": "a_script.sh",
      "workingDirectory": "{{directory}}"
    }
  ]
}

```
### Template directory
Every file and directory in the Template Repository will be copied in the output directory and template tags will be replaced by their values.
A template tag can be placed in file names, directory names, and files content. A tag is formatted as follows :
`{{tagName}}`. `tagName` needs to be defined in the configuration file, otherwise the tag will be replaced by an empty string. 

### Post build tasks directory
```bash
#!/usr/bin/env bash
cd "$1"
```
The expected working directory, defined in the configuration file is provided as argument. Use `cd "$1"` to set it as working directory.

### Template syntax
The template engine uses Jinja2 syntax (See [Jinja](jinja.pocoo.org/docs)). Is is used for both files content, and files/directories names.  
The only exception is the use of the FOR loop, which is normal in files content, not available for directories names and different for files names. 
The FOR syntax for files names is the following:
```
FOR item in {{items}}:{{item}}.txt
``` 
This will create a new file for each item of the variable `items`.