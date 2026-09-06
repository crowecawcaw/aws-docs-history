

# Creating an Amazon ECS task definition using the console
<a name="create-task-definition"></a>

You create a task definition so that you can define the application that you run as a task or service.

When you create a task definition for the external launch type, you need to create the task definition using JSON editor and set the `requireCapabilities` parameter to `EXTERNAL`.

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html)

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html)

   1. (Optional) Choose **Add more containers** to add additional containers to the task definition. 

1. (Optional) The **Storage** section is used to expand the amount of ephemeral storage for tasks hosted on Fargate. You can also use this section to add a data volume configuration for the task.

   1. To expand the available ephemeral storage beyond the default value of 20 gibibytes (GiB) for your Fargate tasks, for **Amount**, enter a value up to 200 GiB.

1. (Optional) To add a data volume configuration for the task definition, choose **Add volume**, and then follow these steps.

   1. For **Volume name**, enter a name for the data volume. The data volume name is used when creating a container mount point.

   1. For **Volume configuration**, select whether you want to configure your volume when creating the task definition or during deployment.
**Note**  
Volumes that can be configured when creating a task definition include Bind mount, Docker, Amazon EFS, and Amazon FSx for Windows File Server. Volumes that can be configured at deployment when running a task, or when creating or updating a service include Amazon EBS.

   1. For **Volume type**, select a volume type compatible with the configuration type that you selected, and then configure the volume type.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html)

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