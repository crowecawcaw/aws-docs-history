End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Quick start tutorial for SimSpace Weaver

This tutorial guides you through the process to build and run a simulation on SimSpace Weaver
in minutes. We recommend that you begin with this tutorial and then go through the [detailed tutorial](getting-started_detailed.md "getting-started_detailed.md") afterward.

###### Requirements

Before you begin, be sure that you completed the steps in
[Setting up for SimSpace Weaver](setting-up.md "setting-up.md").

###### Note

The scripts used here are provided for your convenience and are NOT required. See the [detailed tutorial](getting-started_detailed.md "getting-started_detailed.md") for how these steps can be done manually.

## Step 1: Enable logging (optional)

###### To turn on logging

1. Navigate to:

```
`sdk-folder`/Samples/PathfindingSample/tools
```

2. Open the schema file in a text editor:

```
pathfinding-single-worker-schema.yaml
```

3. Find the `simulation_properties:` section at the beginning of the file:

```
simulation_properties:
  default_entity_index_key_type: "Vector3<f32>"

```

4. Insert the following 2 lines after the line `simulation_properties:`:

```
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"

```

5. Confirm that your `simulation_properties:` section is the same as the following:

```
simulation_properties:
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"
  default_entity_index_key_type: "Vector3<f32>"

```

6. Save the file and exit your text editor.

## Step 2: Quick-start with the console client (option 1)

Navigate to:

```
sdk-folder/Samples/PathfindingSample/tools/cloud
```

Run one of the following commands:

- Docker: `python quick-start.py --consoleclient`
- WSL: `python quick-start.py —-consoleclient --al2`

By default, this will launch a simulation with a single partition on a single worker. Other configurations can be launched by passing the `--schema {file name}.yaml` from the `/Samples/PathfindingSample/tools/` folder.

###### Note

See [Detailed tutorial: Learn the details while
building the sample application](getting-started_detailed.md "getting-started_detailed.md") for an in-depth explanation of what this script does.

## Step 2: Quick-start with the Unreal Engine client (option 2)

See [Launching the Unreal Engine view client](working-with_unreal-client.md "working-with_unreal-client.md").

## Stop and delete your simulation

Navigate to:

```
sdk-folder/Samples/PathfindingSample/tools/cloud
```

Find the names of your simulations:

```
aws simspaceweaver list-simulations
```

Stop and delete the simulation

```
python stop-and-delete.py --simulation `simulation-name`
```

## Troubleshooting

- **FileNotFoundError: cmake**

```
subprocess.run('cmake')
...
 FileNotFoundError: The system cannot find the file specified
```

    + **Resolution:** The script cannot find the command `cmake`. Please ensure you have the minimum recommended CMake version installed, and that it can be called with the `cmake` command in the PATH. Use the command `cmake -version` to verify.

- **ImportError: DLL load failed while importing libweaver_app_sdk_python_v1: The specified module could not be found.**
  - **Resolution:** This error occurs when the Python 3.9 is not being used to launch the Weaver Python SDK. Please ensure the python version associated with the “python” command is Python 3.9. You can check by running the `python --version` command.

- **Quick-start script appears stuck at after starting Docker Build.**
  - **Resolution:** Sometimes Docker needs a few minutes to warm up. If this issue persists for more than ~5 minutes, please restart Docker or your system.

- **target_compile_features no known features for CXX compiler "GNU":**
  - **Resolution:** Clear your Docker cache, delete the weaverappbuilder Docker image, delete your project build artifacts, and re run `setup.py`. This should reset your Docker environment and resolve the error.
