# Enabling the agent from the command line

If your application runs on a platform other than Lambda, install
`codeguru_profiler_agent` through `pip`.

```
pip install codeguru_profiler_agent
```

The only required configuration option to start the CodeGuru Profiler agent is the profiling group
name. You can find this in the **Settings** section of your profiling group.
You can use the credential profile name parameter to have the agent use credentials that are
different from the default credentials. For more information about credential profiles, see
[Shared credential files](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md"). You can specify these options as an environment variable
or as a command line option.

| Option                                | Environment variable                  | Command line option             |
| ------------------------------------- | ------------------------------------- | ------------------------------- |
| Profiling group name (required)       | `AWS_CODEGURU_PROFILER_GROUP_NAME`    | `-p, --profiling-group-name`    |
| Region                                | `AWS_CODEGURU_PROFILER_TARGET_REGION` | `-r, --region`                  |
| (Alternative) credential profile name | Not available                         | `-c, --credential-profile-name` |

The following is an example that uses environment variables. In this example,
`my_script.py` is your main script that you would otherwise call directly with
`python my_script.py`.

```
#!/bin/bash
export AWS_CODEGURU_PROFILER_GROUP_NAME=MyProfilingGroup
export AWS_CODEGURU_PROFILER_TARGET_REGION=us-west-2

python -m codeguru_profiler_agent my_script.py
```

The following is an example that uses command line arguments to specify the configuration
options.

```
python -m codeguru_profiler_agent -p MyProfilingGroup -r us-west-2 \
-c prod-credential-profile my_script.py
```

You can find more details about each command line option by running it with
`-h` to display the list of available options.
