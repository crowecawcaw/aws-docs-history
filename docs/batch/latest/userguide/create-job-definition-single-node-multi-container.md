

# Create a single-node job definition with multiple containers on Amazon EC2 resources
<a name="create-job-definition-single-node-multi-container"></a>

Complete the following steps to create a single-node job definition with multiple containers on Amazon Elastic Compute Cloud (Amazon EC2) resources.

**To create a new job definition on Amazon EC2 resources:**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. From the navigation bar, choose the AWS Region to use.

1. In the left navigation pane, choose **Job definitions**.

1. Choose **Create**.

1. For **Orchestration type,** choose **Amazon Elastic Compute Cloud (Amazon EC2)**.

1. For **Job definition structure**, turn off **Use legacy containerProperties structure** processing.

1. For **EC2 platform configuration**, turn off **Enable multi-node parallel** processing.

1. Choose **Next**.

1. In **General configuration** section, enter the following:

   1. For **Name**, enter a unique name for your job definition. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

   1. For **Execution timeout - *optional***, enter the timeout value (in seconds). The execution timeout is the length of time before an unfinished job is terminated. If an attempt exceeds the timeout duration, the attempt is stopped and moves to a `FAILED` status. For more information, see [Job timeouts](job_timeouts.md). The minimum value is 60 seconds.

   1. Turn on **Scheduling priority - *optional***. Enter a scheduling priority value between 0 and 100. Higher values are given higher priority.

   1. Expand **Tags - *optional*** and then choose **Add tag** to add tags to the resource. Enter a key and optional value, then choose **Add tag**.

   1. Turn on **Propagate tags** to propagate tags from the job and job definition to the Amazon ECS task.

1. In **Retry strategy - *optional*** section, enter the following:

   1. For **Job attempts**, enter the number of times that AWS Batch attempts to move the job to `RUNNABLE` status. Enter a number between 1 and 10.

   1. For **Retry strategy conditions**, choose **Add evaluate on exit**. Enter at least one parameter value and then choose an **Action**. For each set of conditions, **Action** must be set to either **Retry** or **Exit**. These actions mean the following:
      + **Retry** – AWS Batch retries until the number of job attempts that you specified is reached.
      + **Exit** – AWS Batch stops retrying the job.
**Important**  
If you choose **Add evaluate on exit**, you must configure at least one parameter and either choose an **Action** or choose **Remove evaluate on exit**.

1. In **Task properties** section, enter the following:

   1. For **Execution role - *conditional***, choose a role to allow Amazon ECS agents to make AWS API calls on your behalf. For more information on creating an **Execution role**, see [Tutorial: Create the IAM execution role](create-execution-role.md).

   1. Choose **Enable ECS execute command**, to enable access to the Amazon ECS container shell directly and bypass the host OS. You must choose a **Task role**.
**Important**  
The **ECS execute** command requires that file system be writable. 

   1. For **Task role**, choose an Amazon ECS Identity and Access Management (IAM) role to allow the container to make AWS API calls on your behalf. For more information see, [Amazon ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.

   1. For **IPC mode** choose `host`, `task`, or `none`. If `host` is specified, then all the containers that are within the tasks that specified the host IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If task is specified, all the containers that are within the specified task share the same IPC resources. If none is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.

   1. For **PID mode** choose `host` or `task`. For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task. If `host` is specified, all containers within the tasks that specified the host PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance. If `task` is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace for each container. 

1. In the **Consumable resource** section, enter the following:

   1. Enter a unique **Name** and the **Requested value**.

   1. You can add more consumable resources by choosing **Add consumable resource**.

1. In the **Storage** section, enter the following:

   1. Enter a **Name** and **Source path** for the volume and then choose **Add volume**. You can also choose to turn on Enable EFS.

   1. You can add more Volumes by choosing **Add volume**.

1. For **Parameters**, choose **Add parameters** to add parameter substitution placeholders as **Key** and optional **Value** pairs.

1. Choose **Next page**.

1. In the **Container configuration** section:

   1. For **Name**, enter a name for the container.

   1. For **Essential container**, enable if the container is essential.

   1. For **Image**, choose the Docker image to use for your job. By default, images in the Docker Hub registry are available. You can also specify other repositories with `{{repository-url}}/{{image}}:{{tag}}`. The name can be up to 225 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), underscores (\_), colons (:), forward slashes (/), and number signs (\#). This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/) and the `IMAGE` parameter of [**docker run**](https://docs.docker.com/engine/reference/commandline/run/).
**Note**  
Docker image architecture must match the processor architecture of the compute resources that they're scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.
      + Images in Amazon ECR Public repositories use the full `registry/repository[:tag]` or `registry/repository[@digest]` naming conventions (for example, `public.ecr.aws/{{registry_alias}}/{{my-web-app}}:{{latest}}`).
      + Images in Amazon ECR repositories use the full `registry/repository[:tag]` naming convention (for example, `{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com``/{{my-web-app}}:{{latest}}`).
      + Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or `mongo`).
      + Images in other repositories on Docker Hub are qualified with an organization name (for example, `amazon/amazon-ecs-agent`).
      + Images in other online repositories are qualified further by a domain name (for example, `quay.io/assemblyline/ubuntu`).

   1. For **Resource requirements** configure each of the following:

      1. For **vCPUs**, choose the number of CPUs for the container.

      1. For **Memory**, choose the amount of memory for the container.

      1. For **GPU - *optional***, choose the number of GPUs for the container.

   1. For **User**, enter the user name to use inside the container.

   1. Turn on **Enable read only filesystem** to remove write access to the volume.

   1. Turn on **Privileged** to give the job container elevated permissions on the host instance, similar to the root user. 

   1. For **Command**, enter the commands into the field as their **JSON** string array equivalent.

      This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate) section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/) and the `COMMAND` parameter to [**docker run**](https://docs.docker.com/engine/reference/commandline/run/). For more information about the Docker `CMD` parameter, see [https://docs.docker.com/engine/reference/builder/\#cmd](https://docs.docker.com/engine/reference/builder/#cmd).
**Note**  
You can use default values for parameter substitution and placeholders in your command. For more information, see [Parameters](job_definition_parameters.md#parameters).

   1. For **Repository credentials - *optional*** enter the ARN of the secret containing your credentials.

   1. For **Environment variables - *optional***, choose **Add environment variables** to add environment variables to pass to the container.

   1. In the **Linux parameters - *optional*** section:

      1. Turn on **Enable init process** to run an init process inside the container. 

      1. For **Shared memory size**, enter the size (in MiB) of the /dev/shm volume

      1. For **Max swap size**, enter the total amount of swap memory (in MiB) that the container can use.

      1. For **Swappiness** enter a value between 0 and 100 to indicate the swappiness behavior of the container. If you don't specify a value and swapping is enabled, the value defaults to 60. 

      1. For **Devices**, choose **Add device** to add a device:

         1. For **Container path**, specify the path of in the container instance to expose the device mapped to the host instance. If you keep this blank, the host path is used in the container.

         1. For **Host path**, specify the path of a device in the host instance.

         1. For **Permissions**, choose one or more permissions to apply to the device. The available permissions are **READ**, **WRITE**, and **MKNOD**.

      1. For **Tmpfs**, choose **Add tmpfs** to add a `tmpfs` mount.

   1. 
**Note**  
Firelens logging has to be done in a dedicated container. To configure Firelens logging:  
In every container, except your dedicated firelens container, set the **Logging driver** to `awsfirelens`
In your Firelens container set the **Firelens Configuration - optional** and the **Logging configuration - *optional*** to the logging destination

      In the **Firelens Configuration - optional** section:
**Important**  
AWS Batch enforces `host` network mode on non-MNP, non-FARGATE Amazon ECS jobs. [Root user is required](https://github.com/aws/aws-for-fluent-bit/blob/mainline/troubleshooting/debugging.md#amazon-ecs-firelens-root-is-required) for Amazon ECS Firelens. When running tasks that use the `host` network mode, Amazon ECS advises against running containers using the root user (UID 0) for [better security](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#network_mode). Therefore, all non-MNP, non-FARGATE ECS jobs with Firelens logging will not meet security best practice.

      1. For **Type**, choose either `fluentd` or `fluentbit`. 

      1. For **Options**, enter the name/value pair of the option. You can add more **Options** using **Added option**.

   1.  In the **Logging configuration - *optional*** section:

      1. For **Log driver**, choose the log driver to use. For more information about the available log drivers, see [LogConfiguration:logDriver](https://docs.aws.amazon.com/batch/latest/APIReference/API_LogConfiguration.html#Batch-Type-LogConfiguration-logDriver).
**Note**  
By default, the `awslogs` log driver is used.

      1. For **Options**, choose **Add option** to add an option. Enter a name-value pair, and then choose **Add option**.

      1. For **Secrets**, choose **Add secret**. Enter a name-value pair and then choose **Add secret** to add a secret.
**Tip**  
For more information, see [LogConfiguration:secretOptions](https://docs.aws.amazon.com/batch/latest/APIReference/API_LogConfiguration.html#Batch-Type-LogConfiguration-secretOptions).

   1. For **Mount points - *optional***, choose **Add mount points** to add mount points for data volumes. You must specify the source volume and container path. 

   1. For **Secrets - *optional***, choose **Add secret** to add a secret. Then, enter a name-value pair, and choose **Add secret**.
**Tip**  
For more information, see [LogConfiguration:secretOptions](https://docs.aws.amazon.com/batch/latest/APIReference/API_LogConfiguration.html#Batch-Type-LogConfiguration-secretOptions).

   1. For **Ulimits - *optional***, choose **Add ulimit** to add a `ulimits` value for the container. Enter **Name**, **Soft limit**, and **Hard limit** values, and then choose **Add ulimit**.

   1. For **Dependencies - *optional***, choose **Add container dependencies**. Choose the name of the container and it's state to determine when this container starts.

1. If you only have one container configured then you must choose **Add container** and complete configuring the new container. Otherwise, choose **Next** to review. 