End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Step 1: Launch your local simulation

1. Navigate to

```
cd sdk-folder/Samples/sample-name/tools/local
```

2. Run the following command to build and launch your simulation locally.

```
python quick-start.py
```

This script will do the following:

    1. Build the project.




    	* `quick-start.py` calls the `build_project` function
    	 defined in build.py. This step will vary depending on the project. For
    	 the PathfindingSample, CMake is used. The CMake and Docker command for
    	 which can be found in build.py.
    2. Launch your local simulation




    	* The script will launch one local process for each spatial partition
    	 defined in the schema.
    	* The script will launch one process for each custom app defined in the
    	 schema.
    	* The spatial apps will be launched first, followed by the custom apps —
    	 each in the order they appear in the schema.

###### Important

When launching in an environment that does not support GUI, such as a console SSH
session, use the `--noappwindow` option to redirect all output to the current
terminal.

###### Important

For Linux users, the script assumes your system has the `xterm` command.
If your Linux distribution does not have the `xterm` command, use the
`--noappwindow` option to redirect all output to the current terminal.

- -h, --help
  - List these parameters.

- --clean
  - Delete the contents of the build directory before building.

- --nobuild
  - Skip rebuilding the project.

- --noappwindow
  - Don't open a new window for each app. Instead, redirect the stdout to the
    current terminal.

- --logfile
  - Write console output to a logs file.

- --consoleclient
  - Automatically connect the console client listed in the config.

- --schema SCHEMA
  - What schema this invocation will use. Defaults to 'SCHEMA' in
    config.py.
