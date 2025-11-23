# Creating an Amazon ECS task definition using the

console

You create a task definition so that you can define the application that you run as a task or
service.

When you create a task definition for the external launch type, you need to create the task
definition using JSON editor and set the `requireCapabilities` parameter to
`EXTERNAL`.

You can create a task definition by using the console experience, or by specifying a JSON
file. You can have Amazon Q provide recommendations when you use the JSON editor. For more information, see [Using Amazon Q Developer to provide task definition recommendations in the Amazon ECS console](using-amazon-q.md "using-amazon-q.md")

## JSON validation

The Amazon ECS console JSON editor validates the following in the JSON file:

- The file is a valid JSON file.
- The file doesn't contain any extraneous keys.
- The file contains the `familyName` parameter.
- There is at least one entry under `containerDefinitions`.

## CloudFormation stacks

The following behavior applies to task definitions that were
created in the new Amazon ECS console before January 12, 2023.

When you create a task definition, the Amazon ECS console automatically creates a CloudFormation
stack that has a name that begins with `ECS-Console-V2-TaskDefinition-`. If you used the
AWS CLI or an AWS SDK to deregister the task definition, then you must manually delete the task
definition stack. For more information, see [Deleting a
stack](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the _CloudFormation User Guide_.

Task definitions created after January 12, 2023, do not have a CloudFormation stack
automatically created for them.

## Procedure

Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task
   definitions**.
3. On the **Create new task definition** menu,
   choose **Create new task definition**.
4. For **Task definition family**, specify a unique
   name for the task definition.
5. For **Launch type**, choose the application
   environment. The console default is
   **AWS Fargate** (which is serverless). Amazon ECS
   uses this value to perform validation to ensure that the task
   definition parameters are valid for the infrastructure type.
6. For **Operating system/Architecture**, choose the
   operating system and CPU architecture for the task.

To run your task on a 64-bit ARM architecture, choose
**Linux/ARM64**. For more information, see
[Runtime platform](task_definition_parameters.md#runtime-platform "task_definition_parameters.md#runtime-platform").

To run your **AWS Fargate** tasks on Windows
containers, choose a supported Windows operating system. For more
information, see [Operating Systems and architectures](fargate-tasks-services.md#fargate-task-os "fargate-tasks-services.md#fargate-task-os"). 7. For **Task size**, choose the CPU and memory
values to reserve for the task. The CPU value is specified as vCPUs
and memory is specified as GB.

For tasks hosted on Fargate, the following table shows the valid
CPU and memory combinations.

| CPU value                                                                      | Memory value                                | Operating systems supported for<br>AWS Fargate |
| ------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------- |
| 256 (.25 vCPU)                                                                 | 512 MiB, 1 GB, 2 GB                         | Linux                                          |
| 512 (.5 vCPU)                                                                  | 1 GB, 2 GB, 3 GB, 4 GB                      | Linux                                          |
| 1024 (1 vCPU)                                                                  | 2 GB, 3 GB, 4 GB, 5 GB, 6 GB, 7 GB, 8 GB    | Linux, Windows                                 |
| 2048 (2 vCPU)                                                                  | Between 4 GB and 16 GB in 1 GB increments   | Linux, Windows                                 |
| 4096 (4 vCPU)                                                                  | Between 8 GB and 30 GB in 1 GB increments   | Linux, Windows                                 |
| 8192 (8 vCPU)<br>NoteThis option requires Linux platform `1.4.0` or<br>later.  | Between 16 GB and 60 GB in 4 GB increments  | Linux                                          |
| 16384 (16vCPU)<br>NoteThis option requires Linux platform `1.4.0` or<br>later. | Between 32 GB and 120 GB in 8 GB increments | Linux                                          |

For tasks that use EC2 instances, or external instances, the supported task CPU values are between
128 CPU units (0.125 vCPUs) and 196608 CPU units (192 vCPUs).

To
specify the memory value in GB, enter **GB** after
the value. For example, to set the **Memory value**
to 3GB, enter **3GB**.

###### Note

Task-level CPU and memory parameters are ignored for Windows
containers. 8. For **Network mode**, choose the network mode to
use. The default is **awsvpc** mode. For more
information, see [Amazon ECS
task networking](task-networking.md "task-networking.md").

If you choose **bridge**, under **Port
mappings**, for **Host port**, enter
the port number on the container instance to reserve for your
container. 9. (Optional) Expand the **Task roles** section to
configure the AWS Identity and Access Management (IAM) roles for the task:

    1. For **Task role**, choose the IAM role
     to assign to the task. A task IAM role provides
     permissions for the containers in a task to call AWS API
     operations.
    2. For **Task execution role**, choose the
     role.


    For information about when to use a task execution role,
     see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md"). If you don't
     need the role, choose **None**.

10. (Optional) Expand the **Task placement** section
    to add placement contraints. Task placement constraints allow you to
    filter the container instances used for the placement of your tasks
    using built-in or custom attributes.
11. (Optional) Expand the **Fault injection** section
    to enable fault injection. Fault injection lets you test how your application
    responds to certain impairment scenarios.
12. For each container to define in your task definition, complete the
    following steps.
    1.  For **Name**, enter a name for the
        container.
    2.  For **Image URI**, enter the image to use
        to start a container. Images in the Amazon ECR Public Gallery
        registry can be specified by using the Amazon ECR Public registry
        name only. For example, if
        `public.ecr.aws/ecs/amazon-ecs-agent:latest`
        is specified, the Amazon Linux container hosted on the
        Amazon ECR Public Gallery is used. For all other repositories,
        specify the repository by using either the
        `repository-url/image:tag` or
        `repository-url/image@digest` formats.
    3.  If your image is in a private registry outside of Amazon ECR,
        under **Private registry**, turn on
        **Private registry authentication**.
        Then, in **Secrets Manager ARN or name**,
        enter the Amazon Resource Name (ARN) of the secret.
    4.  For **Essential container**, if your task
        definition has two or more containers defined, you can
        specify whether the container should be considered
        essential. When a container is marked as
        **Essential**, if that container stops,
        then the task is stopped. Each task definition must contain
        at least one essential container.
    5.  A port mapping allows the container to access ports on the
        host to send or receive traffic. Under **Port
        mappings**, do one of the following:

            * When you use the **awsvpc**
             network mode, for **Container
             port** and **Protocol**,
             choose the port mapping to use for the
             container.
            * When you use the **bridge**
             network mode, for **Container
             port** and **Protocol**,
             choose the port mapping to use for the
             container.

        Choose **Add more port mappings** to
        specify additional container port mappings.

    6.  To give the container read-only access to its root file
        system, for **Read only root file system**,
        select **Read only**.
    7.  (Optional) To define the container-level CPU, GPU, and
        memory limits that are different from task-level values,
        under **Resource allocation limits**, do
        the following:
        - For **CPU**, enter the number of
          CPU units that the Amazon ECS container agent reserves
          for the container.
        - For **GPU**, enter the number of
          GPU units for the container instance.

        An Amazon EC2 instance with GPU support has 1 GPU unit
        for every GPU. For more information, see [Amazon ECS task definitions for GPU workloads](ecs-gpu.md "ecs-gpu.md").
        - For **Memory hard limit**, enter
          the amount of memory, in GB, to present to the
          container. If the container attempts to exceed the
          hard limit, the container stops.
        - The Docker 20.10.0 or later daemon
          reserves a minimum of 6 mebibytes (MiB) of memory
          for a container, so don't specify fewer than 6 MiB
          of memory for your containers.

        The Docker 19.03.13-ce or earlier
        daemon reserves a minimum of 4 MiB of memory for a
        container, so don't specify fewer than 4 MiB of
        memory for your containers.
        - For **Memory soft limit**, enter
          the soft limit (in GB) of memory to reserve for the
          container.

        When system memory is under contention,
        Docker attempts to keep the
        container memory to this soft limit. If you don't
        specify task-level memory, you must specify a
        non-zero integer for one or both of **Memory
        hard limit** and **Memory soft
        limit**. If you specify both,
        **Memory hard limit** must be
        greater than **Memory soft limit**.

        This feature is not supported on Windows
        containers.

    8.  (Optional) Expand the **Environment
        variables** section to specify environment
        variables to inject into the container. You can specify
        environment variables either individually by using key-value
        pairs or in bulk by specifying an environment variable file
        that's hosted in an Amazon S3 bucket. For information about how
        to format an environment variable file, see [Pass an individual environment
        variable to an Amazon ECS container](taskdef-envfiles.md "taskdef-envfiles.md").

    When you specify an environment variable for secret
    storage, for **Key**, enter the secret
    name. Then for **ValueFrom**, enter the
    full ARN of the Systems Manager Parameter Store secret or Secrets Manager
    secret 9. (Optional) Select the **Use log
    collection** option to specify a log
    configuration. For each available log driver, there are log
    driver options to specify. The default option sends
    container logs to Amazon CloudWatch Logs. The other log driver options
    are configured by using AWS FireLens. For
    more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

    The following describes each container log destination in
    more detail.

        * **Amazon CloudWatch** – Configure
         the task to send container logs to CloudWatch Logs. The
         default log driver options are provided, which
         create a CloudWatch log group on your behalf. To specify a
         different log group name, change the driver option
         values.
        * **Export logs to
         Splunk** –
         Configure the task to send container logs to the
         Splunk driver that sends the logs
         to a remote service. You must enter the URL to your
         Splunk web service. The
         Splunk token is specified as a
         secret option because it can be treated as sensitive
         data.
        * **Export logs to Amazon Data Firehose**
         – Configure the task to send container logs
         to Firehose. The default log driver options are
         provided, which sends log to an Firehose delivery
         stream. To specify a different delivery stream name,
         change the driver option values.
        * **Export logs to Amazon Kinesis Data Streams**
         – Configure the task to send container logs
         to Kinesis Data Streams. The default log driver options are
         provided, which send logs to a Kinesis Data Streams stream. To
         specify a different stream name, change the driver
         option values.
        * **Export logs to Amazon OpenSearch Service**
         – Configure the task to send container logs
         to an OpenSearch Service domain. The log driver options must be
         provided.
        * **Export logs to Amazon S3** –
         Configure the task to send container logs to an Amazon S3
         bucket. The default log driver options are provided,
         but you must specify a valid Amazon S3 bucket
         name.

    10. (Optional) Configure additional container
        parameters.

    | To configure this option                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Restart policy**<br>These options define a restart policy to<br>restart a container when it exits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Expand **Restart<br>policy**, and then configure the<br>following items:<br>• To enable a restart policy for the<br>container, turn on **Enable Restart<br>policy**.<br>• For **Ignored exit codes**,<br>specify a comma-separated list of integer<br>container exit codes. If the container exits with<br>any of the specified exit codes, Amazon ECS will not try to<br>restart the container. If nothing is specified,<br>Amazon ECS will not ignore any exit codes.<br>• For **Attempt reset period**, specify an integer period of time,<br>in seconds, that the container must run for before a restart can be attempted in the event of an exit. Amazon ECS can attempt to restart a<br>container only once every \*_Attempt reset<br>period_<br>• seconds. If nothing is specified, the container must run for<br>300 seconds before a restart can be attempted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | **HealthCheck**<br>These are the commands that determine if a<br>container is healthy. For more information, see<br>[Determine Amazon ECS task health using container health<br>checks](healthcheck.md "healthcheck.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Expand **HealthCheck**,<br>and then configure the following items:<br>• For **Command**, enter a<br>comma-separated list of commands. You can start<br>the commands with `CMD` to run the<br>command arguments directly, or<br>`CMD-SHELL` to run the command with the<br>container's default shell. If neither is<br>specified, `CMD` is used.<br>• For **Interval**, enter the<br>number of seconds between each health check. The<br>valid values are between 5 and 30.<br>• For **Timeout**, enter the<br>period of time (in seconds) to wait for a health<br>check to succeed before it's considered a failure.<br>The valid values are between 2 and 60.<br>• For **Start period**, enter<br>the period of time (in seconds) to wait for a<br>container to bootstrap before the health check<br>commands run. The valid values are between 0 and<br>300.<br>• For **Retries**, enter the<br>number of times to retry the health check commands<br>when there is a failure. The valid values are<br>between 1 and 10.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | **Startup dependency<br>ordering**<br>This option defines dependencies for<br>container startup and shutdown. A container can<br>contain multiple dependencies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Expand **Startup dependency<br>ordering**, and then configure the<br>following:<br>1. Choose **Add container<br>dependency**.<br>2. For **Container**, choose<br>the container.<br>3. For **Condition**, choose<br>the startup dependency condition. To add an additional dependency,<br>choose **Add container<br>dependency**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | **Container<br>timeouts**These options determine<br>when to start and stop a container.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Expand **Container<br>timeouts**, and then configure the<br>following:<br>• To configure the time to wait before giving<br>up on resolving dependencies for a container, for<br>**Start timeout**, enter the<br>number of seconds.<br>• To configure the time to wait before the<br>container is stopped if it doesn't exit normally<br>on its own, for **Stop timeout**,<br>enter the number of seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | **Container network<br>settings**These options determine<br>whether to use networking within a<br>container.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Expand **Container network<br>settings**, and then configure the<br>following:<br>• To disable container networking, select<br>**Turn off networking**.<br>• To configure DNS server IP addresses that<br>are presented to the container, in **DNS<br>servers**, enter the IP address of each<br>server on a separate line.<br>• To configure DNS domains to search<br>non-fully-qualified host names that are presented<br>to the container, in **DNS search<br>domains**, enter each domain on a<br>separate line.<br>The pattern is<br>`^[a-zA-Z0-9-.]{0,253}[a-zA-Z0-9]$`.<br>• To configure the container host name, in<br>**Host name**, enter the<br>container goat name.<br>• To add hostnames and IP address mappings<br>that are appended to the `/etc/hosts`<br>file on the container, choose **Add extra<br>host**, and then for<br>**Hostname\*<br>• and **IP<br>address\*\*, enter the host name and IP<br>address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | **Docker<br>configuration**These override the<br>values in the<br>Dockerfile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Expand **Docker<br>configuration**, and then configure the<br>following items:<br>• For **Command**, enter an<br>executable command for a container.<br>This parameter maps to `Cmd` in<br>the [Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#tag/Container/operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#tag/Container/operation/ContainerCreate") section of the<br>Docker Remote API and the<br>`COMMAND` option to `docker<br>run`. This parameter overrides the<br>`CMD` instruction in a [Dockerfile](https://docs.docker.com/engine/reference/builder/#workdir "https://docs.docker.com/engine/reference/builder/#workdir").<br>• For **Entry point**, enter<br>the Docker ENTRYPOINT that is<br>passed to the container.<br>This parameter maps to<br>`Entrypoint` in the [Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#tag/Container/operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#tag/Container/operation/ContainerCreate") section of the<br>Docker Remote API and the<br>`--entrypoint` option to `docker<br>run`. This parameter overrides the<br>`ENTRYPOINT` instruction in a [Dockerfile](https://docs.docker.com/engine/reference/builder/#workdir "https://docs.docker.com/engine/reference/builder/#workdir").<br>• For **Working directory**,<br>enter the directory that the container will run<br>any entry point and command instructions provided.<br>This parameter maps to<br>`WorkingDir` in the [Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#tag/Container/operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#tag/Container/operation/ContainerCreate") section of the<br>Docker Remote API and the<br>`--workdir` option to `docker<br>run`. This parameter overrides the<br>`WORKDIR` instruction in a [Dockerfile](https://docs.docker.com/engine/reference/builder/#workdir "https://docs.docker.com/engine/reference/builder/#workdir"). |
    | **Resource limits (Ulimits)**These<br>values overwrite the default resource quota<br>setting for the operating system.This<br>parameter maps to `Ulimits` in the<br>[Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate") section of the<br>[Docker Remote API](https://docs.docker.com/reference/api/engine/version/v1.38/ "https://docs.docker.com/reference/api/engine/version/v1.38/") and the `--ulimit`<br>option to [docker run](https://docs.docker.com/reference/cli/docker/container/run/ "https://docs.docker.com/reference/cli/docker/container/run/"). | Expand **Resource limits<br>(ulimits)**, and then<br>choose **Add<br>ulimit**. For<br>**Limit name**, choose the limit.<br>Then, for **Soft limit\*<br>• and<br>**Hard limit**, enter the<br>values.<br>To add additional ulimits,<br>choose **Add<br>ulimit\*\*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | **Docker<br>labels**This option adds metadata<br>to your container.This parameter maps<br>to `Labels` in the<br>[Create a container](https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate "https://docs.docker.com/reference/api/engine/version/v1.38/#operation/ContainerCreate") section of the<br>[Docker Remote API](https://docs.docker.com/reference/api/engine/version/v1.38/ "https://docs.docker.com/reference/api/engine/version/v1.38/") and the `--label`<br>option to [docker run](https://docs.docker.com/reference/cli/docker/container/run/ "https://docs.docker.com/reference/cli/docker/container/run/").                                                      | Expand **Docker<br>labels**, choose **Add key value<br>pair**, and then enter the<br>**Key\*<br>• and<br>**Value**.<br>To add additional Docker<br>labels, choose **Add key value<br>pair\*\*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    11. (Optional) Choose **Add more containers**
        to add additional containers to the task definition.

13. (Optional) The **Storage** section is used to expand the amount of
    ephemeral storage for tasks hosted on Fargate. You can also use this
    section to add a data volume configuration for the task.
    1.  To expand the available ephemeral storage beyond the default value of 20
        gibibytes (GiB) for your Fargate tasks, for
        **Amount**, enter a value up to 200
        GiB.

14. (Optional) To add a data volume configuration for the task definition,
    choose **Add volume**, and then follow these
    steps.
    1.  For **Volume name**, enter a name for the
        data volume. The data volume name is used when creating a
        container mount point.
    2.  For **Volume configuration**, select whether
        you want to configure your volume when creating the task
        definition or during deployment.

    ###### Note

    Volumes that can be configured when creating a task definition include Bind mount,
    Docker, Amazon EFS, and Amazon FSx for Windows File Server.
    Volumes that can be configured at deployment when running a
    task, or when creating or updating a service include
    Amazon EBS. 3. For **Volume type**, select a volume type compatible with the
    configuration type that you selected, and then configure the
    volume type.

| Volume type                     | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bind mount**                  | 1. Choose **Add mount point**,<br>and then configure the following:<br>• For **Container**, choose<br>the container for the mount point.<br>• For **Source volume**,<br>choose the data volume to mount to the<br>container.<br>• For **Container path**,<br>enter the path on the container to mount the<br>volume.<br>• For **Read only**, select<br>whether the container has read-only access to the<br>volume.<br>2. To add additional mount points,<br>**Add mount point**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **EFS**                         | 1. For **File system ID**,<br>choose the Amazon EFS file system ID.<br>2. (Optional) For **Root<br>directory**, enter the directory within<br>the Amazon EFS file system to mount as the root<br>directory inside the host. If this parameter is<br>omitted, the root of the Amazon EFS volume is<br>used.<br>If you plan to use an EFS access point,<br>leave this field blank.<br>3. (Optional) For **Access<br>point**, choose the access point ID to<br>use.<br>4. (Optional) To encrypt the data between the<br>Amazon EFS file system and the Amazon ECS host or to use the<br>task execution role when mounting the volume,<br>choose **Advanced<br>configurations**, and then configure the<br>following:<br>• To encrypt the data between the Amazon EFS file<br>system and the Amazon ECS host, select<br>**Transit encryption**, and then<br>for **Port**, enter the port to<br>use when sending encrypted data between the Amazon ECS<br>host and the Amazon EFS server. If you don't specify a<br>transit encryption port, it uses the port<br>selection strategy that the Amazon EFS mount helper<br>uses. For more information, see [EFS<br>Mount Helper](../../../efs/latest/ug/efs-mount-helper.md "../../../efs/latest/ug/efs-mount-helper.md") in the<br>_Amazon Elastic File System User Guide_.<br>• To use the Amazon ECS task IAM role defined in<br>a task definition when mounting the Amazon EFS file<br>system, select **IAM<br>authorization**.<br>5. Choose **Add mount point**,<br>and then configure the following:<br>• For **Container**, choose<br>the container for the mount point.<br>• For **Source volume**,<br>choose the data volume to mount to the<br>container.<br>• For **Container path**,<br>enter the path on the container to mount the<br>volume.<br>• For **Read only**, select<br>whether the container has read-only access to the<br>volume.<br>6. To add additional mount points,<br>**Add mount point**. |
| **Docker**                      | 1. For **Driver**, enter the<br>Docker volume configuration.<br>Windows containers support only the use of the<br>**local\*<br>• driver. To use bind<br>mounts, specify a host.<br>2. For **Scope**, choose the<br>volume lifecycle.<br>• To have the lifecycle last when the task<br>starts and stops, choose<br>**Task**.<br>• To have the volume persist after the task<br>stops, choose **Shared**.<br>3. Choose **Add mount point**,<br>and then configure the following:<br>• For **Container**, choose<br>the container for the mount point.<br>• For **Source volume**,<br>choose the data volume to mount to the<br>container.<br>• For **Container path**,<br>enter the path on the container to mount the<br>volume.<br>• For **Read only**, select<br>whether the container has read-only access to the<br>volume.<br>4. To add additional mount points,<br>**Add mount point\*\*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **FSx for Windows File Server** | 1. For **File system ID**,<br>choose the FSx for Windows File Server file system ID.<br>2. For **Root directory**,<br>enter the directory, enter the directory within<br>the FSx for Windows File Server file system to mount as the root<br>directory inside the host.<br>3. For **Credential<br>parameter**, choose how the credentials<br>are stored.<br>• To use AWS Secrets Manager, enter the Amazon Resource Name (ARN) of a<br>Secrets Manager secret.<br>• To use AWS Systems Manager, enter the Amazon Resource Name (ARN) of a<br>Systems Manager parameter.<br>4. For **Domain**, enter the<br>fully qualified domain name that's hosted by an<br>AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) directory or a<br>self-hosted EC2 Active Directory.<br>5. Choose **Add mount point**,<br>and then configure the following:<br>• For **Container**, choose<br>the container for the mount point.<br>• For **Source volume**,<br>choose the data volume to mount to the<br>container.<br>• For **Container path**,<br>enter the path on the container to mount the<br>volume.<br>• For **Read only**, select<br>whether the container has read-only access to the<br>volume.<br>6. To add additional mount points,<br>**Add mount point**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Amazon EBS**                  | 1. Choose **Add mount point**,<br>and then configure the following:<br>• For **Container**, choose<br>the container for the mount point.<br>• For **Source volume**,<br>choose the data volume to mount to the<br>container.<br>• For **Container path**,<br>enter the path on the container to mount the<br>volume.<br>• For **Read only**, select<br>whether the container has read-only access to the<br>volume.<br>2. To add additional mount points,<br>**Add mount point**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

15. To add a volume from another container, choose **Add
    volume from**, and then configure the following:
    - For **Container**, choose the
      container.
    - For **Source**, choose the container
      which has the volume you want to mount.
    - For **Read only**, select whether the
      container has read-only access to the volume.

16. (Optional) To configure your application trace and metric
    collection settings by using the AWS Distro for
    OpenTelemetry integration, expand
    **Monitoring**, and then select **Use
    metric collection** to collect and send metrics for
    your tasks to either Amazon CloudWatch or Amazon Managed Service for Prometheus. When this option is
    selected, Amazon ECS creates an AWS Distro for
    OpenTelemetry container sidecar that is preconfigured to
    send the application metrics. For more information, see [Correlate Amazon ECS application performance using application
    metrics](metrics-data.md "metrics-data.md").
    1.  When **Amazon CloudWatch** is selected, your
        custom application metrics are routed to CloudWatch as custom
        metrics. For more information, see [Exporting application metrics to
        Amazon CloudWatch](application-metrics-cloudwatch.md "application-metrics-cloudwatch.md").

    ###### Important

    When exporting application metrics to Amazon CloudWatch, your
    task definition requires a task IAM role with the
    required permissions. For more information, see [Required IAM permissions for
    AWS Distro for OpenTelemetry integration with Amazon CloudWatch](application-metrics-cloudwatch.md#application-metrics-cloudwatch-iam "application-metrics-cloudwatch.md#application-metrics-cloudwatch-iam"). 2. When you select **Amazon Managed Service for Prometheus (Prometheus libraries
    instrumentation)**, your task-level CPU,
    memory, network, and storage metrics and your custom
    application metrics are routed to Amazon Managed Service for Prometheus. For
    **Workspace remote write endpoint**,
    enter the remote write endpoint URL for your
    Prometheus workspace. For
    **Scraping target**, enter the host and
    port the AWS Distro for OpenTelemetry
    collector can use to scrape for metrics data. For more
    information, see [Exporting application metrics to
    Amazon Managed Service for Prometheus](application-metrics-prometheus.md "application-metrics-prometheus.md").

    ###### Important

    When exporting application metrics to Amazon Managed Service for Prometheus, your
    task definition requires a task IAM role with the
    required permissions. For more information, see [Required IAM permissions for
    AWS Distro for OpenTelemetry integration with Amazon Managed Service for Prometheus](application-metrics-prometheus.md#application-metrics-prometheus-iam "application-metrics-prometheus.md#application-metrics-prometheus-iam"). 3. When you select **Amazon Managed Service for Prometheus (OpenTelemetry
    instrumentation)**, your task-level CPU,
    memory, network, and storage metrics and your custom
    application metrics are routed to Amazon Managed Service for Prometheus. For
    **Workspace remote write endpoint**,
    enter the remote write endpoint URL for your
    Prometheus workspace. For more
    information, see [Exporting application metrics to
    Amazon Managed Service for Prometheus](application-metrics-prometheus.md "application-metrics-prometheus.md").

    ###### Important

    When exporting application metrics to Amazon Managed Service for Prometheus, your
    task definition requires a task IAM role with the
    required permissions. For more information, see [Required IAM permissions for
    AWS Distro for OpenTelemetry integration with Amazon Managed Service for Prometheus](application-metrics-prometheus.md#application-metrics-prometheus-iam "application-metrics-prometheus.md#application-metrics-prometheus-iam").

17. (Optional) Expand the **Tags** section to add
    tags, as key-value pairs, to the task definition.
    - [Add a tag] Choose **Add tag**, and then
      do the following:
      - For **Key**, enter the key
        name.
      - For **Value**, enter the key
        value.

    - [Remove a tag] Next to the tag, choose **Remove
      tag**.

18. Choose **Create** to register the task
    definition.

Amazon ECS console JSON editor

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task
   definitions**.
3. On the **Create new task definition** menu,
   choose **Create new task definition with
   JSON**.
4. In the JSON editor box, edit your JSON file,

The JSON must pass the validation checks specified in [JSON validation](#json-validate-for-create "#json-validate-for-create"). 5. Choose **Create**.
