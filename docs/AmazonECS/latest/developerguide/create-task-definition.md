

# Creating an Amazon ECS task definition using the console
<a name="create-task-definition"></a>

You create a task definition so that you can define the application that you run as a task or service.

When you create a task definition for the external launch type, you need to create the task definition using JSON editor and set the `requiresCompatibilities` parameter to `EXTERNAL`.

You can create a task definition by using the console experience, or by specifying a JSON file. You can have Amazon Q provide recommendations when you use the JSON editor. For more information, see [Using Amazon Q Developer to provide task definition recommendations in the Amazon ECS console](using-amazon-q.md)

## JSON validation
<a name="json-validate-for-create"></a>

The Amazon ECS console JSON editor validates the following in the JSON file:
+ The file is a valid JSON file.
+ The file doesn't contain any extraneous keys.
+ The file contains the `familyName` parameter.
+ There is at least one entry under `containerDefinitions`.

## CloudFormation stacks
<a name="cloudformation-stack"></a>

The following behavior applies to task definitions that were created in the new Amazon ECS console before January 12, 2023.

When you create a task definition, the Amazon ECS console automatically creates a CloudFormation stack that has a name that begins with `ECS-Console-V2-TaskDefinition-`. If you used the AWS CLI or an AWS SDK to deregister the task definition, then you must manually delete the task definition stack. For more information, see [Deleting a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) in the *CloudFormation User Guide*.

Task definitions created after January 12, 2023, do not have a CloudFormation stack automatically created for them.

## Procedure
<a name="create-task-procedure"></a>

------
#### [ Amazon ECS console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Task definitions**.

1. On the **Create new task definition** menu, choose **Create new task definition**.

1. For **Task definition family**, specify a unique name for the task definition.

1. For **Launch type**, choose the application environment. The console default is **AWS Fargate** (which is serverless). Amazon ECS uses this value to perform validation to ensure that the task definition parameters are valid for the infrastructure type.

1. For **Operating system/Architecture**, choose the operating system and CPU architecture for the task. 

   To run your task on a 64-bit ARM architecture, choose **Linux/ARM64**. For more information, see [Runtime platform](task_definition_parameters.md#runtime-platform).

   To run your **AWS Fargate** tasks on Windows containers, choose a supported Windows operating system. For more information, see [Operating Systems and architectures](fargate-tasks-services.md#fargate-task-os).

1. For **Task size**, choose the CPU and memory values to reserve for the task. The CPU value is specified as vCPUs and memory is specified as GB.

   For tasks hosted on Fargate, the following table shows the valid CPU and memory combinations.


<table>
<thead>
  <tr><th> CPU value </th><th> Memory value </th><th> Operating systems supported for AWS Fargate </th></tr>
</thead>
<tbody>
  <tr><td> 256 (.25 vCPU) </td><td> 512 MiB, 1 GB, 2 GB </td><td> Linux </td></tr>
  <tr><td> 512 (.5 vCPU) </td><td> 1 GB, 2 GB, 3 GB, 4 GB </td><td> Linux </td></tr>
  <tr><td> 1024 (1 vCPU) </td><td> 2 GB, 3 GB, 4 GB, 5 GB, 6 GB, 7 GB, 8 GB </td><td> Linux, Windows </td></tr>
  <tr><td> 2048 (2 vCPU) </td><td> Between 4 GB and 16 GB in 1 GB increments </td><td> Linux, Windows </td></tr>
  <tr><td> 4096 (4 vCPU) </td><td> Between 8 GB and 30 GB in 1 GB increments </td><td> Linux, Windows </td></tr>
  <tr><td> 8192 (8 vCPU)  This option requires Linux platform <code>1.4.0</code> or later.  </td><td> Between 16 GB and 60 GB in 4 GB increments </td><td> Linux </td></tr>
  <tr><td> 16384 (16 vCPU)  This option requires Linux platform <code>1.4.0</code> or later.  </td><td> Between 32 GB and 120 GB in 8 GB increments </td><td> Linux </td></tr>
  <tr><td> 32768 (32 vCPU)  This option requires Linux platform <code>1.4.0</code> or later.  </td><td> 60 GB, 120 GB, 244 GB </td><td> Linux </td></tr>
</tbody>
</table>


   For tasks that use EC2 instances, or external instances, the supported task CPU values are between 128 CPU units (0.125 vCPUs) and 196608 CPU units (192 vCPUs).

   To specify the memory value in GB, enter **GB** after the value. For example, to set the **Memory value** to 3GB, enter **3GB**.
**Note**  
Task-level CPU and memory parameters are ignored for Windows containers.

1. For **Network mode**, choose the network mode to use. The default is **awsvpc** mode. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html).

   If you choose **bridge**, under **Port mappings**, for **Host port**, enter the port number on the container instance to reserve for your container.

1. (Optional) Expand the **Task roles** section to configure the AWS Identity and Access Management (IAM) roles for the task:

   1. For **Task role**, choose the IAM role to assign to the task. A task IAM role provides permissions for the containers in a task to call AWS API operations.

   1. For **Task execution role**, choose the role.

      For information about when to use a task execution role, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md). If you don't need the role, choose **None**.

1. (Optional) Expand the **Task placement** section to add placement contraints. Task placement constraints allow you to filter the container instances used for the placement of your tasks using built-in or custom attributes.

1. (Optional) Expand the **Fault injection** section to enable fault injection. Fault injection lets you test how your application responds to certain impairment scenarios.

1. For each container to define in your task definition, complete the following steps.

   1. For **Name**, enter a name for the container.

   1. For **Image URI**, enter the image to use to start a container. Images in the Amazon ECR Public Gallery registry can be specified by using the Amazon ECR Public registry name only. For example, if `public.ecr.aws/ecs/amazon-ecs-agent:latest` is specified, the Amazon Linux container hosted on the Amazon ECR Public Gallery is used. For all other repositories, specify the repository by using either the `repository-url/image:tag` or `repository-url/image@digest` formats.

   1. If your image is in a private registry outside of Amazon ECR, under **Private registry**, turn on **Private registry authentication**. Then, in **Secrets Manager ARN or name**, enter the Amazon Resource Name (ARN) of the secret.

   1. For **Essential container**, if your task definition has two or more containers defined, you can specify whether the container should be considered essential. When a container is marked as **Essential**, if that container stops, then the task is stopped. Each task definition must contain at least one essential container.

   1. A port mapping allows the container to access ports on the host to send or receive traffic. Under **Port mappings**, do one of the following: 
      + When you use the **awsvpc** network mode, for **Container port** and **Protocol**, choose the port mapping to use for the container.
      + When you use the **bridge** network mode, for **Container port** and **Protocol**, choose the port mapping to use for the container.

      Choose **Add more port mappings** to specify additional container port mappings.

   1. To give the container read-only access to its root file system, for **Read only root file system**, select **Read only**.

   1. (Optional) To define the container-level CPU, GPU, and memory limits that are different from task-level values, under **Resource allocation limits**, do the following:
      + For **CPU**, enter the number of CPU units that the Amazon ECS container agent reserves for the container.
      + For **GPU**, enter the number of GPU units for the container instance. 

        An Amazon EC2 instance with GPU support has 1 GPU unit for every GPU. For more information, see [Amazon ECS task definitions for GPU workloads](ecs-gpu.md).
      + For **Memory hard limit**, enter the amount of memory, in GB, to present to the container. If the container attempts to exceed the hard limit, the container stops.
      + The Docker 20.10.0 or later daemon reserves a minimum of 6 mebibytes (MiB) of memory for a container, so don't specify fewer than 6 MiB of memory for your containers.

        The Docker 19.03.13-ce or earlier daemon reserves a minimum of 4 MiB of memory for a container, so don't specify fewer than 4 MiB of memory for your containers.
      + For **Memory soft limit**, enter the soft limit (in GB) of memory to reserve for the container. 

        When system memory is under contention, Docker attempts to keep the container memory to this soft limit. If you don't specify task-level memory, you must specify a non-zero integer for one or both of **Memory hard limit** and **Memory soft limit**. If you specify both, **Memory hard limit** must be greater than **Memory soft limit**. 

        This feature is not supported on Windows containers.

   1. (Optional) Expand the **Environment variables** section to specify environment variables to inject into the container. You can specify environment variables either individually by using key-value pairs or in bulk by specifying an environment variable file that's hosted in an Amazon S3 bucket. For information about how to format an environment variable file, see [Pass an individual environment variable to an Amazon ECS container](taskdef-envfiles.md).

      When you specify an environment variable for secret storage, for **Key**, enter the secret name. Then for **ValueFrom**, enter the full ARN of the Systems Manager Parameter Store secret or Secrets Manager secret 

   1. (Optional) Select the **Use log collection** option to specify a log configuration. For each available log driver, there are log driver options to specify. The default option sends container logs to Amazon CloudWatch Logs. The other log driver options are configured by using AWS FireLens. For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md).

      The following describes each container log destination in more detail.
      + **Amazon CloudWatch** – Configure the task to send container logs to CloudWatch Logs. The default log driver options are provided, which create a CloudWatch log group on your behalf. To specify a different log group name, change the driver option values.
      + **Export logs to Splunk** – Configure the task to send container logs to the Splunk driver that sends the logs to a remote service. You must enter the URL to your Splunk web service. The Splunk token is specified as a secret option because it can be treated as sensitive data.
      + **Export logs to Amazon Data Firehose** – Configure the task to send container logs to Firehose. The default log driver options are provided, which sends log to an Firehose delivery stream. To specify a different delivery stream name, change the driver option values.
      + **Export logs to Amazon Kinesis Data Streams** – Configure the task to send container logs to Kinesis Data Streams. The default log driver options are provided, which send logs to a Kinesis Data Streams stream. To specify a different stream name, change the driver option values.
      + **Export logs to Amazon OpenSearch Service** – Configure the task to send container logs to an OpenSearch Service domain. The log driver options must be provided.
      + **Export logs to Amazon S3** – Configure the task to send container logs to an Amazon S3 bucket. The default log driver options are provided, but you must specify a valid Amazon S3 bucket name.

   1. (Optional) Configure additional container parameters.


<table>
<thead>
  <tr><th>To configure this option</th><th>Do this</th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>Restart policy</b><br />These options define a restart policy to restart a container when it exits.</td><td> Expand <b>Restart policy</b>, and then configure the following items:<ul><li> To enable a restart policy for the container, turn on <b>Enable Restart policy</b>. </li><li> For <b>Ignored exit codes</b>, specify a comma-separated list of integer container exit codes. If the container exits with any of the specified exit codes, Amazon ECS will not try to restart the container. If nothing is specified, Amazon ECS will not ignore any exit codes. </li><li> For <b>Attempt reset period</b>, specify an integer period of time, in seconds, that the container must run for before a restart can be attempted in the event of an exit. Amazon ECS can attempt to restart a container only once every <b>Attempt reset period</b> seconds. If nothing is specified, the container must run for 300 seconds before a restart can be attempted. </li></ul> </td><td></td></tr>
  <tr><td><b>HealthCheck</b><br />These are the commands that determine if a container is healthy. For more information, see <a href="healthcheck.md">Determine Amazon ECS task health using container health checks</a>.</td><td>Expand <b>HealthCheck</b>, and then configure the following items: <ul><li> For <b>Command</b>, enter a comma-separated list of commands. You can start the commands with <code>CMD</code> to run the command arguments directly, or <code>CMD-SHELL</code> to run the command with the container's default shell. If neither is specified, <code>CMD</code> is used.  </li><li> For <b>Interval</b>, enter the number of seconds between each health check. The valid values are between 5 and 30. </li><li> For <b>Timeout</b>, enter the period of time (in seconds) to wait for a health check to succeed before it's considered a failure. The valid values are between 2 and 60. </li><li> For <b>Start period</b>, enter the period of time (in seconds) to wait for a container to bootstrap before the health check commands run. The valid values are between 0 and 300. </li><li> For <b>Retries</b>, enter the number of times to retry the health check commands when there is a failure. The valid values are between 1 and 10. </li></ul></td><td></td></tr>
  <tr><td><b>Startup dependency ordering</b>This option defines dependencies for container startup and shutdown. A container can contain multiple dependencies.</td><td>Expand <b>Startup dependency ordering</b>, and then configure the following: <ol><li> Choose <b>Add container dependency</b>. </li><li> For <b>Container</b>, choose the container. </li><li> For<b> Condition</b>, choose the startup dependency condition. </li></ol> To add an additional dependency, choose <b>Add container dependency</b>.</td><td></td></tr>
  <tr><td><b>Container timeouts</b>These options determine when to start and stop a container.</td><td>Expand <b>Container timeouts</b>, and then configure the following: <ul><li> To configure the time to wait before giving up on resolving dependencies for a container, for <b>Start timeout</b>, enter the number of seconds. </li><li> To configure the time to wait before the container is stopped if it doesn't exit normally on its own, for <b>Stop timeout</b>, enter the number of seconds. </li></ul></td><td></td></tr>
  <tr><td><b>Container network settings</b>These options determine whether to use networking within a container.</td><td>Expand <b>Container network settings</b>, and then configure the following: <ul><li> To disable container networking, select <b>Turn off networking</b>. </li><li> To configure DNS server IP addresses that are presented to the container, in <b>DNS servers</b>, enter the IP address of each server on a separate line. </li><li> To configure DNS domains to search non-fully-qualified host names that are presented to the container, in <b>DNS search domains</b>, enter each domain on a separate line. <br />The pattern is <b>^[a-zA-Z0-9-.]{0,253}[a-zA-Z0-9]$</b>. </li><li> To configure the container host name, in <b>Host name</b>, enter the container goat name. </li><li> To add hostnames and IP address mappings that are appended to the <code>/etc/hosts</code> file on the container, choose <b>Add extra host</b>, and then for <b>Hostname</b> and <b>IP address</b>, enter the host name and IP address. </li></ul></td><td></td></tr>
  <tr><td><b>Docker configuration</b>These override the values in the Dockerfile.</td><td>Expand <b>Docker configuration</b>, and then configure the following items:<ul><li> For <b>Command</b>, enter an executable command for a container.  <br />This parameter maps to <code>Cmd</code> in the <a href="https://docs.docker.com/reference/api/engine/latest/#tag/Container/operation/ContainerCreate">Create a container</a> section of the Docker Remote API and the <code>COMMAND</code> option to <code>docker run</code>. This parameter overrides the <code>CMD</code> instruction in a <a href="https://docs.docker.com/engine/reference/builder/#workdir">https://docs.docker.com/engine/reference/builder/#workdir</a>. </li><li> For <b>Entry point</b>, enter the Docker ENTRYPOINT that is passed to the container. <br />This parameter maps to <code>Entrypoint</code> in the <a href="https://docs.docker.com/reference/api/engine/latest/#tag/Container/operation/ContainerCreate">Create a container</a> section of the Docker Remote API and the <code>--entrypoint</code> option to <code>docker run</code>. This parameter overrides the <code>ENTRYPOINT</code> instruction in a <a href="https://docs.docker.com/engine/reference/builder/#workdir">https://docs.docker.com/engine/reference/builder/#workdir</a>. </li><li> For <b>Working directory</b>, enter the directory that the container will run any entry point and command instructions provided.  <br />This parameter maps to <code>WorkingDir</code> in the <a href="https://docs.docker.com/reference/api/engine/latest/#tag/Container/operation/ContainerCreate">Create a container</a> section of the Docker Remote API and the <code>--workdir</code> option to <code>docker run</code>. This parameter overrides the <code>WORKDIR</code> instruction in a <a href="https://docs.docker.com/engine/reference/builder/#workdir">https://docs.docker.com/engine/reference/builder/#workdir</a>. </li></ul></td><td></td></tr>
  <tr><td><b>Resource limits (Ulimits)</b>These values overwrite the default resource quota setting for the operating system.<br />This parameter maps to <code>Ulimits</code> in the <a href="https://docs.docker.com/reference/api/engine/latest/#operation/ContainerCreate">Create a container</a> section of the <a href="https://docs.docker.com/reference/api/engine/latest/">Docker Remote API</a> and the <code>--ulimit</code> option to <a href="https://docs.docker.com/reference/cli/docker/container/run/">https://docs.docker.com/reference/cli/docker/container/run/</a>.</td><td> Expand <b>Resource limits (ulimits)</b>, and then choose <b>Add ulimit</b>. For <b>Limit name</b>, choose the limit. Then, for <b>Soft limit</b> and <b>Hard limit</b>, enter the values.<br />To add additional ulimits, choose <b>Add ulimit</b>.</td><td></td></tr>
  <tr><td><b>Docker labels</b>This option adds metadata to your container.<br />This parameter maps to <code>Labels</code> in the <a href="https://docs.docker.com/reference/api/engine/latest/#operation/ContainerCreate">Create a container</a> section of the <a href="https://docs.docker.com/reference/api/engine/latest/">Docker Remote API</a> and the <code>--label</code> option to <a href="https://docs.docker.com/reference/cli/docker/container/run/">https://docs.docker.com/reference/cli/docker/container/run/</a>. </td><td>Expand <b>Docker labels</b>, choose <b>Add key value pair</b>, and then enter the <b>Key</b> and <b>Value</b>.<br />To add additional Docker labels, choose <b>Add key value pair</b>.</td><td></td></tr>
</tbody>
</table>


   1. (Optional) Choose **Add more containers** to add additional containers to the task definition. 

1. (Optional) The **Storage** section is used to expand the amount of ephemeral storage for tasks hosted on Fargate. You can also use this section to add a data volume configuration for the task.

   1. To expand the available ephemeral storage beyond the default value of 20 gibibytes (GiB) for your Fargate tasks, for **Amount**, enter a value up to 200 GiB.

1. (Optional) To add a data volume configuration for the task definition, choose **Add volume**, and then follow these steps.

   1. For **Volume name**, enter a name for the data volume. The data volume name is used when creating a container mount point.

   1. For **Volume configuration**, select whether you want to configure your volume when creating the task definition or during deployment.
**Note**  
Volumes that can be configured when creating a task definition include Bind mount, Docker, Amazon EFS, and Amazon FSx for Windows File Server. Volumes that can be configured at deployment when running a task, or when creating or updating a service include Amazon EBS.

   1. For **Volume type**, select a volume type compatible with the configuration type that you selected, and then configure the volume type.


<table>
<thead>
  <tr><th>Volume type</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>Bind mount</b></td><td> <ol><li> Choose <b>Add mount point</b>, and then configure the following: <ul><li> For <b>Container</b>, choose the container for the mount point. </li><li> For <b>Source volume</b>, choose the data volume to mount to the container. </li><li> For <b>Container path</b>, enter the path on the container to mount the volume. </li><li> For <b>Read only</b>, select whether the container has read-only access to the volume. </li></ul> </li><li> To add additional mount points, <b>Add mount point</b>. </li></ol> </td><td></td></tr>
  <tr><td><b>EFS</b></td><td> <ol><li> For <b>File system ID</b>, choose the Amazon EFS file system ID. </li><li> (Optional) For <b>Root directory</b>, enter the directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used. <br />If you plan to use an EFS access point, leave this field blank. </li><li> (Optional) For <b>Access point</b>, choose the access point ID to use. </li><li> (Optional) To encrypt the data between the Amazon EFS file system and the Amazon ECS host or to use the task execution role when mounting the volume, choose <b>Advanced configurations</b>, and then configure the following: <ul><li> To encrypt the data between the Amazon EFS file system and the Amazon ECS host, select <b>Transit encryption</b>, and then for <b>Port</b>, enter the port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html">EFS Mount Helper</a> in the <i>Amazon Elastic File System User Guide</i>. </li><li> To use the Amazon ECS task IAM role defined in a task definition when mounting the Amazon EFS file system, select <b>IAM authorization</b>. </li></ul> </li><li> Choose <b>Add mount point</b>, and then configure the following: <ul><li> For <b>Container</b>, choose the container for the mount point. </li><li> For <b>Source volume</b>, choose the data volume to mount to the container. </li><li> For <b>Container path</b>, enter the path on the container to mount the volume. </li><li> For <b>Read only</b>, select whether the container has read-only access to the volume. </li></ul> </li><li> To add additional mount points, <b>Add mount point</b>. </li></ol> </td><td></td></tr>
  <tr><td><b>Docker</b></td><td> <ol><li> For <b>Driver</b>, enter the Docker volume configuration. Windows containers support only the use of the <b>local</b> driver. To use bind mounts, specify a host. </li><li> For <b>Scope</b>, choose the volume lifecycle.  <ul><li> To have the lifecycle last when the task starts and stops, choose <b>Task</b>. </li><li> To have the volume persist after the task stops, choose <b>Shared</b>. </li></ul> </li><li> Choose <b>Add mount point</b>, and then configure the following: <ul><li> For <b>Container</b>, choose the container for the mount point. </li><li> For <b>Source volume</b>, choose the data volume to mount to the container. </li><li> For <b>Container path</b>, enter the path on the container to mount the volume. </li><li> For <b>Read only</b>, select whether the container has read-only access to the volume. </li></ul> </li><li> To add additional mount points, <b>Add mount point</b>. </li></ol> </td><td></td></tr>
  <tr><td><b>FSx for Windows File Server</b></td><td> <ol><li> For <b>File system ID</b>, choose the FSx for Windows File Server file system ID. </li><li> For <b>Root directory</b>, enter the directory, enter the directory within the FSx for Windows File Server file system to mount as the root directory inside the host. </li><li> For <b>Credential parameter</b>, choose how the credentials are stored.  <ul><li> To use AWS Secrets Manager, enter the Amazon Resource Name (ARN) of a Secrets Manager secret. </li><li> To use AWS Systems Manager, enter the Amazon Resource Name (ARN) of a Systems Manager parameter. </li></ul> </li><li> For <b>Domain</b>, enter the fully qualified domain name that's hosted by an AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) directory or a self-hosted EC2 Active Directory. </li><li> Choose <b>Add mount point</b>, and then configure the following: <ul><li> For <b>Container</b>, choose the container for the mount point. </li><li> For <b>Source volume</b>, choose the data volume to mount to the container. </li><li> For <b>Container path</b>, enter the path on the container to mount the volume. </li><li> For <b>Read only</b>, select whether the container has read-only access to the volume. </li></ul> </li><li> To add additional mount points, <b>Add mount point</b>. </li></ol> </td><td></td></tr>
  <tr><td><b>Amazon EBS</b></td><td> <ol><li> Choose <b>Add mount point</b>, and then configure the following: <ul><li> For <b>Container</b>, choose the container for the mount point. </li><li> For <b>Source volume</b>, choose the data volume to mount to the container. </li><li> For <b>Container path</b>, enter the path on the container to mount the volume. </li><li> For <b>Read only</b>, select whether the container has read-only access to the volume. </li></ul> </li><li> To add additional mount points, <b>Add mount point</b>. </li></ol> </td><td></td></tr>
</tbody>
</table>


1. To add a volume from another container, choose **Add volume from**, and then configure the following:
   + For **Container**, choose the container.
   + For **Source**, choose the container which has the volume you want to mount.
   + For **Read only**, select whether the container has read-only access to the volume.

1. (Optional) To configure your application trace and metric collection settings by using the AWS Distro for OpenTelemetry integration, expand **Monitoring**, and then select **Use metric collection** to collect and send metrics for your tasks to either Amazon CloudWatch or Amazon Managed Service for Prometheus. When this option is selected, Amazon ECS creates an AWS Distro for OpenTelemetry container sidecar that is preconfigured to send the application metrics. For more information, see [Correlate Amazon ECS application performance using application metrics](metrics-data.md).

   1. When **Amazon CloudWatch** is selected, your custom application metrics are routed to CloudWatch as custom metrics. For more information, see [Exporting application metrics to Amazon CloudWatch](application-metrics-cloudwatch.md).
**Important**  
When exporting application metrics to Amazon CloudWatch, your task definition requires a task IAM role with the required permissions. For more information, see [Required IAM permissions for AWS Distro for OpenTelemetry integration with Amazon CloudWatch](application-metrics-cloudwatch.md#application-metrics-cloudwatch-iam). 

   1. When you select **Amazon Managed Service for Prometheus (Prometheus libraries instrumentation)**, your task-level CPU, memory, network, and storage metrics and your custom application metrics are routed to Amazon Managed Service for Prometheus. For **Workspace remote write endpoint**, enter the remote write endpoint URL for your Prometheus workspace. For **Scraping target**, enter the host and port the AWS Distro for OpenTelemetry collector can use to scrape for metrics data. For more information, see [Exporting application metrics to Amazon Managed Service for Prometheus](application-metrics-prometheus.md).
**Important**  
When exporting application metrics to Amazon Managed Service for Prometheus, your task definition requires a task IAM role with the required permissions. For more information, see [Required IAM permissions for AWS Distro for OpenTelemetry integration with Amazon Managed Service for Prometheus](application-metrics-prometheus.md#application-metrics-prometheus-iam). 

   1. When you select **Amazon Managed Service for Prometheus (OpenTelemetry instrumentation)**, your task-level CPU, memory, network, and storage metrics and your custom application metrics are routed to Amazon Managed Service for Prometheus. For **Workspace remote write endpoint**, enter the remote write endpoint URL for your Prometheus workspace. For more information, see [Exporting application metrics to Amazon Managed Service for Prometheus](application-metrics-prometheus.md).
**Important**  
When exporting application metrics to Amazon Managed Service for Prometheus, your task definition requires a task IAM role with the required permissions. For more information, see [Required IAM permissions for AWS Distro for OpenTelemetry integration with Amazon Managed Service for Prometheus](application-metrics-prometheus.md#application-metrics-prometheus-iam). 

1. (Optional) Expand the **Tags** section to add tags, as key-value pairs, to the task definition.
   + [Add a tag] Choose **Add tag**, and then do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.
   + [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create** to register the task definition.

------
#### [ Amazon ECS console JSON editor ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Task definitions**.

1. On the **Create new task definition** menu, choose **Create new task definition with JSON**.

1. In the JSON editor box, edit your JSON file,

   The JSON must pass the validation checks specified in [JSON validation](#json-validate-for-create).

1. Choose **Create**.

------