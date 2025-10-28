End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Step 3: Stop your local simulation (optional on Windows)

###### Note

This step is required on Linux but optional on Windows.

1. Navigate to:

```
`sdk-folder`/Samples/sample-name/tools/local
```

2. Run the following command to stop your local simulation and delete any shared memory resources.

```
python stop-and-delete.py
```

This script will do the following:

    * Stop the local processes.
    * Delete the shared memory object (only needed on Linux).

###### stop-and-delete.py parameters

- -h, --help
  - List these parameters.

- --stop
  - Only attempt to stop the processes.

- --delete
  - Only attempt to delete the shared memory resources.

- --process
  - The name of the process to stop. Use this if your process name doesn't match the package name in the schema.

- --schema SCHEMA
  - What schema this invocation will use. Defaults to value of 'SCHEMA' in config.py.
