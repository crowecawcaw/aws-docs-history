End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Detailed tutorial: Learn the details while

building the sample application

The [quick start tutorial](getting-started_quickstart.md "getting-started_quickstart.md") covered how to
build, start, stop, and delete a sample simulation using `quick-start.py` and
`stop-and-delete.py`. This tutorial will go over in detail how these scripts
work, and the additional parameters these scripts can take to maximize flexibility for
custom Weaver simulations.

###### Requirements

Before you begin, be sure that you completed the steps in [Setting up for SimSpace Weaver](setting-up.md "setting-up.md").

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

3. Find the `simulation_properties:` section at the beginning of the
   file:

```
simulation_properties:
  default_entity_index_key_type: "Vector3<f32>"

```

4. Insert the following 2 lines after the line
   `simulation_properties:`:

```
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"

```

5. Confirm that your `simulation_properties:` section is the same as
   the following:

```
simulation_properties:
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"
  default_entity_index_key_type: "Vector3<f32>"

```

6. Save the file and exit your text editor.

## Step 2: Start your

simulation

As show in the [quick start tutorial](getting-started_quickstart.md "getting-started_quickstart.md"),
the most basic steps to launch a sample simulation are:

1. Navigate to:

```
sdk-folder/Samples/PathfindingSample/tools/cloud
```

2. Run one of the follwing commands:
   - **Docker:**
     `python quick-start.py`
   - **WSL:**
     `python quick-start.py --al2`

This script automates common terminal commands, all of which can be executed manually
using the AWS CLI. These steps are:

1.  Upload the Weaver schema to S3.
    - SimSpace Weaver uses a schema to configure your simulation. The schema is
      a YAML-formatted plain text file. For more infomration, see [Configuring your simulation](working-with_configuring-simulation.md "working-with_configuring-simulation.md").

2.  Build and upload a custom container (optional).
    - If your schema defines a custom container, the quick-start script
      will build the docker image and upload it to Amazon ECR. For more
      information, see [Custom containers](working-with_custom-containers.md "working-with_custom-containers.md"). See the
      `PythonBubblesSample` schema for an example of this
      feature.

3.  Build the project.
    - `quick-start.py` calls the `build_project`
      function defined in `build.py`. This step will vary depending
      on the project. For the PathfindingSample, CMake is used. The CMake and
      Docker command for which can be found in `build.py`.

4.  Upload the build artifacts to S3.
    - You can check your S3 buckets to make sure that all of the uploads
      succeeded. For more information on using Amazon S3, see [Creating,
      configuring, and working with Amazon S3 buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md") in the
      _Amazon Simple Storage Service User Guide_.
    - The sample application zips and S3 bucket use the following name
      format:
      - `weaver-sample-bucket-account-number-region`
      - Spatial app: `ProjectNameSpatial.zip`
      - View (custom) app: `ProjectNameView.zip`

5.  Start the Simulation.
    - This is a wrapper around the `aws simspaceweaver
start-simulation` AWS CLI call. For more information, see the
      [AWS CLI Command
      Reference](../../../cli/latest/reference/simspaceweaver.md "../../../cli/latest/reference/simspaceweaver.md") for SimSpace Weaver.
    - The script will loop until the simulation status is either
      `STARTED` or `FAILED`. It can take a few
      minutes for a simulation to start.

6.  Get the simulation details.
    - The DescribeSimulation
      API provides details about your simulation, including its state. A
      simulation can be in one of the following states:

    ###### Simulation life cycle states

        1. `STARTING` –
         Initial state after you call StartSimulation
        2. `STARTED` –
         all spatial apps are launched and healthy
        3. `STOPPING` –
         Initial state after you call StopSimulation
        4. `STOPPED` –
         All compute resources are stopped
        5. `DELETING` –
         Initial state after you call DeleteSimulation
        6. `DELETED` –
         All resources assigned to the simulation are deleted
        7. `FAILED` –
         The simulation had a critical error/failure and stopped
        8. `SNAPSHOT_IN_PROGRESS` – A [snapshot](working-with_snapshots.md "working-with_snapshots.md") is in
         progress

    ###### To get your simulation details

        1. Call the ListSimulations API.



        ```
        aws simspaceweaver list-simulations
        ```

        The script should display details about your each of your
         simulations, similar to the following:



        ```

        {
            "Status": "STARTED",
            "CreationTime": 1664921418.09,
            "Name": "MyProjectSimulation_22-10-04_22_10_15",
            "Arn": "arn:aws:simspaceweaver:us-west-2:111122223333:simulation/MyProjectSimulation_22-10-04_22_10_15",
            "TargetStatus": "STARTED"
        }

        ```
        2. Call DescribeSimulation to get your
         simulation details. Substitute
         `simulation-name`
         with the Name of
         your simulation from the output of the previous step.



        ```
        aws simspaceweaver describe-simulation --simulation `simulation-name`
        ```

        The script should display more details about the simulation
         that you specified, similar to the following:



        ```

        {
            "Status": "STARTED",
            "CreationTime": 1664921418.09,
            "Name": "MyProjectSimulation_22-10-04_22_10_15",
            "Arn": "arn:aws:simspaceweaver:us-west-2:111122223333:simulation/MyProjectSimulation_22-10-04_22_10_15",
            "TargetStatus": "STARTED"
        }

        ```

7.  Start custom apps.
    - SimSpace Weaver doesn't manage the lifecycle of custom apps. You must start
      your custom apps. It's best practice to start your custom apps before
      you start your simulation clock, but you can start custom apps after you
      start the clock.

    You can call the StartApp API to start your custom apps.

    ```
    aws simspaceweaver start-app --simulation `simulation-name` --name `app-name` --domain `domain-name`
    ```

    The StartApp API call
    will create and start a new instance of the custom app using the name
    that you provide. If you provide the name of an app that already exists
    then you will receive an error. If you want to restart a particular app
    (instance), you must first stop that app and delete it.

    ###### Note

    The status of your simulation must be `STARTED` before
    you can start custom apps.

    The sample application provides the `ViewApp` custom app to
    view your simulation. This app provides you with a static IP address and
    port number to connect the simulation clients (you will do this in a
    later step in this tutorial). You can think of a domain as a class of apps that
    have the same executable code and launch options. The app name identifies the instance
    of the app. For more information on SimSpace Weaver concepts, see [Key concepts for SimSpace Weaver](what-is_key-concepts.md "what-is_key-concepts.md").

    You can use the DescribeApp API to check the status of a custom
    app after you start it.

    ```
    aws simspaceweaver describe-app --simulation `simulation-name` --app `app-name` --domain `domain-name`
    ```

    ###### To start the view app in this tutorial

        1. Call StartApp
         for `ViewApp`.



        ```
        aws simspaceweaver start-app --simulation `simulation-name` --name ViewApp --domain MyViewDomain
        ```
        2. Call DescribeApp to check the status of your
         custom app.



        ```
        aws simspaceweaver describe-app --simulation `simulation-name` --app ViewApp --domain MyViewDomain
        ```

    After the status of your custom app (instance) is
    `STARTED`, the output of DescribeApp will include the IP address and
    port number for that custom app (instance). In the following example
    output, the IP address is the value of `Address` and the port
    number is the value of `Actual` in the
    `EndpointInfo` block.

    ```


    {
        "Status": "STARTED",
        "Domain": "MyViewDomain",
        "TargetStatus": "STARTED",
        "Simulation": "MyProjectSimulation_22-10-04_22_10_15",
        "LaunchOverrides": {
            "LaunchCommands": []
        },
        "EndpointInfo": {
            "IngressPortMappings": [
                {
                    "Declared": 7000,
                    "Actual": 4321
                }
            ],
            "Address": "198.51.100.135"
        },
        "Name": "ViewApp"
    }


    ```

    ###### Note

    The value of `Declared`
    is the port number that your app code should bind to. The value of `Actual` is the port
    number that SimSpace Weaver exposes to clients to connect to your app. SimSpace Weaver maps the
    `Declared` port to the `Actual` port.

    ###### Note

    You can use the the procedure described at [Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md") to get the IP address and
    port number of any started custom app.

8.  Start the clock.
    - When you first create your simulation, it has a clock but the clock
      isn't running. When your clock isn't running, your simulation won't
      update its state. After you start the clock, it will begin sending ticks
      to your apps. Each tick, your spatial apps step through the entities
      they own and commit the results to SimSpace Weaver

    ###### Note

    It can take 30-60 seconds to start the clock.

    Call the StartClock
    API.

    ```
    aws simspaceweaver start-clock --simulation `simulation-name`
    ```

    ###### Note

    The StartClock API
    uses your `simulation-name`,
    which you can find using the ListSimulations API:

    ```
    aws simspaceweaver list-simulations
    ```

###### quick-start parameters

- -h, --help
  - List these parameters.

- --clean
  - Delete the contents of the build directory before building.

- --al2
  - Builds directly on the native machine instead of Docker. Only use this if running in an Amazon Linux 2 environment, such as WSL.

- --uploadonly
  - Only upload the schema and app zips to Amazon S3, don't start the simulation.

- --nobuild
  - Skip rebuilding the project.

- --nocontainer
  - Skip rebuilding the simulation container listed in the schema.

- --consoleclient
  - Automatically build and connect the console client listed in config.py.

- --schema SCHEMA
  - What schema this invocation will use. Defaults to value of 'SCHEMA' in config.py.

- --name NAME
  - What name the simulation will have. Defaults to the value of 'PROJECT_NAME'-date-time in config.py.

## Step 3: Check the logs

(optional)

SimSpace Weaver writes simulation management messages and the console output
from your apps to Amazon CloudWatch Logs. For more information on working with logs, see
[Working with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs
User Guide_.

Each simulation that you create has its own log group
in CloudWatch Logs. The name of the log group is specified in the simulation schema.
In the following schema snippet, the value of `log_destination_service`
is `logs`. This means that the value of `log_destination_resource_name`
is the name of a log group. In this case, the log group is `MySimulationLogs`.

```


simulation_properties:
  log_destination_service: "logs"
  log_destination_resource_name: "MySimulationLogs"
  default_entity_index_key_type: "Vector3<f32>"


```

You can also use the DescribeSimulation API to find the
name of the log group for simulation after you start it.

```
aws simspaceweaver describe-simulation --simulation `simulation-name`
```

The following example shows the part of the output from DescribeSimulation
that describes the logging configuration. The name of the log group is shown at the end of the
`LogGroupArn`.

```


    "LoggingConfiguration": {
        "Destinations": [
            {
                "CloudWatchLogsLogGroup": {
                    "LogGroupArn": "arn:aws:logs:us-west-2:111122223333:log-group:MySimulationLogs"
                }
            }
        ]
    },


```

Each simulation log group contains several log streams:

- Management log stream – simulation
  management messages produced by the SimSpace Weaver service.

```
/sim/management
```

- Errors log stream – error
  messages produced by the SimSpace Weaver service. This log stream only
  exists if there are errors. SimSpace Weaver stores errors written by your apps
  in their own app log streams (see the following log streams).

```
/sim/errors
```

- Spatial app log streams (1 for each spatial app
  on each worker) – console output produced by spatial apps. Each spatial app
  writes to its own log stream. The `spatial-app-id` is
  all characters after the trailing slash at the end of the `worker-id`.

```
/domain/`spatial-domain-name`/app/worker-`worker-id`/`spatial-app-id`
```

- Custom app log streams (1 for each custom app instance)
  – console output produced by custom apps. Each custom app instance writes
  to its own log stream.

```
/domain/`custom-domain-name`/app/`custom-app-name`/`random-id`
```

- Service app log streams (1 for each service app
  instance) – console output produced by service apps. Each service app
  writes to its own log stream. The `service-app-id` is
  all characters after the trailing slash at the end of the `service-app-name`.

```
/domain/`service-domain-name`/app/`service-app-name`/`service-app-id`
```

###### Note

The sample application doesn't have service apps.

## Step 4: View your simulation

The SimSpace Weaver app SDK provides different options to view the sample application.
You can use the sample console client if you don't have any local support for Unreal
Engine development. The instructions for the Unreal Engine client assume that you are
using Windows.

The console client displays a list of entity events as they occur. The client gets the
entity event information from the `ViewApp`. If your console client displays the list of
events, then it confirms network connectivity with the `ViewApp` and activity in your
simulation.

The `PathfindingSample` simulation creates stationary and moving entities on a
2-dimensional plane. The moving entities move around the stationary entities. The Unreal
Engine client provides a visualization of the entity events.

### Console client

The console client can be automatically built and connected when launching a sample with `quick-start.py` if you include the `--consoleclient` option. To build and connect the console client after `quick-start.py` has already been called, do the following:

Navigate to:

```
sdk-folder/Clients/TCP/CppConsoleClient
```

Run the script to build and connect the client:

```
python start_client.py --host ip-address --port port-number
```

The script will do the following:

1. Build the console client with CMake.
2. Launch the built executable with the given IP address and port number.

```
.\WeaverNngConsoleClient.exe --url tcp://`ip-address:port-number`
```

### Unreal Engine client

See [Launching the Unreal Engine view client](working-with_unreal-client.md "working-with_unreal-client.md").

## Step 5: Stop and delete your simulation

Navigate to:

```
sdk-folder/Samples/PathfindingSample/tools/cloud
```

Find the names of your simulations:

```
aws simspaceweaver list-simulations
```

Stop and delete the simulation:

```
python stop-and-delete.py --simulation simulation-name
```

The script `stop-and-delete.py` will do the following:

1. Call the AWS CLI command to stop a simulation.
   - `aws simspaceweaver stop-simulation`
   - For more information, see [AWS CLI Command Reference](../../../cli/latest/reference/simspaceweaver/stop-simulation.md "../../../cli/latest/reference/simspaceweaver/stop-simulation.md") for SimSpace Weaver.

2. Call the AWS CLI command to delete a simulation.
   - `aws simpaceweaver delete-simulation`
   - For more information, see [AWS CLI Command Reference](../../../cli/latest/reference/simspaceweaver/delete-simulation.md "../../../cli/latest/reference/simspaceweaver/delete-simulation.md") for SimSpace Weaver.

###### stop-and-delete parameters

- -h, --help
  - List these parameters.

- --simulation SIMULATION
  - The name of the simulation to stop-and-delete

- --stop
  - Only stop the simulation. Doesn't delete it.

- --delete
  - Only delete a simulation. Will only work if he simulation is either `STOPPED` or `FAILED`.

## Troubleshooting

See [Troubleshooting](getting-started_quickstart.md#getting-started_quickstart_troubleshooting "getting-started_quickstart.md#getting-started_quickstart_troubleshooting") in the quick start tutorial.
