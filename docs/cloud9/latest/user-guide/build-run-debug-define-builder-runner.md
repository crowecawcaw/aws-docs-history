AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Define a Builder or Runner

This topic shows how you can define a builder or runner. Before you define a builder or
runner, make sure you have [created a
builder or runner](build-run-debug.md#build-run-debug-create-builder-runner "build-run-debug.md#build-run-debug-create-builder-runner").

On the builder or runner tab that is displayed, use JSON to define the runner or builder. Start with the following code as a template.

For a builder, start with this code.

```
{
  "cmd": [],
  "info": "",
  "env": {},
  "selector": ""
}
```

For a runner, start with this code.

```
{
  "cmd": [],
  "script": "",
  "working_dir": "",
  "info": "",
  "env": {},
  "selector": "",
  "debugger": "",
  "debugport": ""
}
```

In the preceding code:

- `cmd`: Represents a comma-separated list of strings for AWS Cloud9 to run as a single command.

When AWS Cloud9 runs this command, each string in the list will be separated by a single space.
For example, AWS Cloud9 will run `"cmd": [ "ls", "$file", "$args"]` as `ls $file $args`, where AWS Cloud9 will replace `$file` with the full path to the
current file and `$args` with any arguments entered after the file name. For more information, see the list of supported variables later in this section.

- `script`: Represents a bash script (which can also be specified as an array of lines as
  needed for readability) that the runner executes in the terminal.
- `working_dir`: Represents the directory that the runner will run from.
- `info`: Represents any string of text you want to display to the user at the beginning
  of the run. This string can contain variables, for example
  `Running $project_path$file_name...`, where AWS Cloud9 will replace `$project_path` with the directory path of the current file and
  `$file_name` with the name portion of the current file. See the list of supported variables later in this section.
- `env`: Represents any array of command line arguments for AWS Cloud9 to use, for example:

```
"env": {
  "LANG": "en_US.UTF-8",
  "SHLVL": "1"
}
```

- `selector`: Represents any regular expression that you want AWS Cloud9 to use to identify the
  file names that apply to this runner.
  For example, you could specify `source.py` for Python files.
- `debugger`: Represents the name of any available debugger you want AWS Cloud9 to use that is
  compatible with this runner. For example, you could specify
  `v8` for the V8 debugger.
- `debugport`: Represents the port number you want AWS Cloud9 to use during debugging. For example,
  you could specify `15454` for the port number to use.
  The following table shows the variables you can use.

| **Variable**         | **Description**                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `$file_path`         | The directory of the current file, for example, `/home/ec2-user/environment` or `/home/ubuntu/environment`.                   |
| `$file`              | The full path to the current file, for example, `/home/ec2-user/environment/hello.py` or `/home/ubuntu/environment/hello.py`. |
| `$args`              | Any arguments entered after the file name, for example, `"5" "9"`.                                                            |
| `$file_name`         | The name portion of the current file, for example, `hello.py`.                                                                |
| `$file_extension`    | The extension of the current file, for example, `py`.                                                                         |
| `$file_base_name`    | The name of the current file without the file extension, for example, `hello`.                                                |
| `$packages`          | The full path to the packages folder.                                                                                         |
| `$project`           | The full path to the current project folder.                                                                                  |
| `$project_path`      | The directory of the current project file, for example, `/home/ec2-user/environment/` or `/home/ubuntu/environment/`.         |
| `$project_name`      | The name of the current project file without the file extension, for example, `my-demo-environment`.                          |
| `$project_extension` | The extension of the current project file.                                                                                    |
| `$project_base_name` | The name of the current project file without the extension.                                                                   |
| `$hostname`          | The hostname of the environment, for example, `192.0.2.0`.                                                                    |
| `$hostname_path`     | The hostname of the environment with the relative path to the project file, for example, `https://192.0.2.0/hello.js`.        |
| `$url`               | The full URL to access the environment, for example, `https://192.0.2.0.`.                                                    |
| `$port`              | The port assigned to the environment, for example, `8080`.                                                                    |
| `$ip`                | The IP address to run a process against the environment, for example, `0.0.0.0`.                                              |

As an example, the following builder file named `G++.build` defines a builder for GCC that runs
the **`g++`** command with the
`-o` option to compile the current file (for example, `hello.cpp`) into an object module.
Then it links the object module into a program
with the same name as the current file (for example, `hello`). Here the equivalent command is `g++
-o hello hello.cpp`.

```
{
  "cmd": [ "g++", "-o", "$file_base_name", "$file_name" ],
  "info": "Compiling $file_name and linking to $file_base_name...",
  "selector": "source.cpp"
}
```

As another example, the following runner file named `Python.run` defines a runner that uses Python to run the current file with
any arguments that were provided. For example, if the current file is named `hello.py` and the arguments `5` and `9` were provided, the
equivalent command is `python hello.py 5 9`.

```
{
  "cmd": [ "python", "$file_name", "$args" ],
  "info": "Running $file_name...",
  "selector": "source.py"
}
```

Finally, the following runner file named `Print Run Variables.run` defines a runner that simply outputs the value of each available variable and then stops.

```
{
  "info": "file_path = $file_path, file = $file, args = $args, file_name = $file_name, file_extension = $file_extension, file_base_name = $file_base_name, packages = $packages, project = $project, project_path = $project_path, project_name = $project_name, project_extension = $project_extension, project_base_name = $project_base_name, hostname = $hostname, hostname_path = $hostname_path, url = $url, port = $port, ip = $ip"
}
```
