# Flexio Templating Tool

## Template creation
A template is composed of 3 files/folders
* `template.json` configuration file
* `template` directory
* `post_build_tasks` directory (optional)

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
    },
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
`{{tagName}}`. `tagName` needs to be defined in the configuration file, otherwise the tag will be replaced by and empty string. 

### Post build tasks directory
```bash
#!/usr/bin/env bash
cd "$1"
```
The expected working directory, defined in the configuration file is provided as argument. Use `cd "$1"` to set it as working directory.