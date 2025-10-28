# Tutorial: Create a multi-node parallel job definition on Amazon EC2

resources

To create a multi-node parallel job definition on Amazon Elastic Compute Cloud (Amazon EC2) resources.

###### Note

To create a _single-node_ job definition, see [Create a single-node job definition on Amazon EC2
resources](create-job-definition-EC2.md "create-job-definition-EC2.md").

###### To create a multi-node parallel job definition on Amazon EC2 resources:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Job definitions**.
4. Choose **Create**.
5. For **Orchestration type,** choose **Amazon Elastic Compute Cloud
   (Amazon EC2)**.
6. For **Enable multi-node parallel**, turn on multi-node parallel.
7. For **Name**, enter a unique name for your job definition. The name can
   be up to 128 characters long, and can contain uppercase and lowercase letters, numbers, hyphens
   (-), and underscores (\_).
8. (Optional) For **Execution timeout**, specify the maximum number of
   seconds that you want job attempts to run. If an attempt exceeds the timeout duration, the
   attempt is stopped and moves to a `FAILED` status. For more information, see [Job timeouts](job_timeouts.md "job_timeouts.md").
9. (Optional) Turn on **Scheduling priority**. Enter a scheduling priority
   value between 0 and 100. Higher values are given higher priority over lower values.
10. (Optional) For **Job attempts**, enter the number of times that AWS Batch
    attempts to move the job to `RUNNABLE` status. Enter a number between 1 and
11.
12. (Optional) For **Retry strategy conditions**, choose **Add
    evaluate on exit**. Enter at least one parameter value and then choose an
    **Action**. For each set of conditions, **Action** must be
    set to either **Retry** or **Exit**. These actions mean the
    following:
    - Retry – AWS Batch retries until the number of job
      attempts that you specified is reached.
    - Exit – AWS Batch stops retrying the job.

###### Important

If you choose **Add evaluate on exit**, you must configure at least one
parameter and either choose an **Action** or choose **Remove evaluate
on exit**. 12. (Optional) Expand **Tags** and then choose **Add tag**
to add tags to the resource. Enter a key and optional value, and then choose **Add
tag**. You can also turn on **Propagate tags** to propagate tags
from the job and job definition to the Amazon ECS task. 13. Choose **Next page**. 14. For **Number of nodes**, enter the total number of nodes to use for your
job. 15. For **Main node**, enter the node index to use for the main node. The
default main node index is `0`. 16. For **Instance type**, choose an instance type.

###### Note

The instance type that you choose applies to all nodes. 17. For **Parameters**, choose **Add parameters** to add
parameter substitution placeholders as **Key** and optional
**Value** pairs. 18. In the **Node ranges** section:

    1. Select **Add node range**. This creates a **Node
     range** section.
    2. For **Target nodes**, specify the range for your node group, using
     ``range_start`:`range_end``
     notation.


    You can create up to five node ranges for the nodes that you specified for your job.
     Node ranges use the index value for a node, and the node index begins at 0. Make sure that
     range end index value of your final node group is one less than the number of nodes that you
     specified. For example, suppose that you specified 10 nodes, and you want to use a single
     node group. Then, your end range is 9.
    3. For **Image**, choose the Docker image to use for your
     job. By default, images in the Docker Hub registry are available. You can also
     specify other repositories with
     ``repository-url`/`image`:`tag``.
     The name can be up to 225 characters long. It can contain uppercase and lowercase letters,
     numbers, hyphens (-), underscores (\_), colons (:), forward slashes (/), and number signs (#).
     This parameter maps to `Image` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section
     of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `IMAGE` parameter of [**docker
     run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/").


    ###### Note

    Docker image architecture must match the processor architecture of the compute resources that they're
     scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.




    	* Images in Amazon ECR Public repositories use the full `registry/repository[:tag]`
    	 or `registry/repository[@digest]` naming conventions (for example,
    	 `public.ecr.aws/`registry_alias`/`my-web-app`:`latest``).
    	* Images in Amazon ECR repositories use the full `registry/repository[:tag]`
    	 naming convention. For example,
    	 ``aws_account_id`.dkr.ecr.`region`.amazonaws.com``/`my-web-app`:`latest``
    	* Images in official repositories on Docker Hub use a single name (for
    	 example, `ubuntu` or `mongo`).
    	* Images in other repositories on Docker Hub are qualified with an
    	 organization name (for example, `amazon/amazon-ecs-agent`).
    	* Images in other online repositories are qualified further by a domain name (for
    	 example, `quay.io/assemblyline/ubuntu`).
    4. For **Command**, enter the commands into the field as their **JSON** string array equivalent.


    This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate")
     section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `COMMAND` parameter to [**docker
     run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). For more information about the Docker
     `CMD` parameter, see [https://docs.docker.com/engine/reference/builder/#cmd](https://docs.docker.com/engine/reference/builder/#cmd "https://docs.docker.com/engine/reference/builder/#cmd").


    ###### Note

    You can use default values for parameter substitution and placeholders in your command.
     For more information, see [Parameters](job_definition_parameters.md#parameters "job_definition_parameters.md#parameters").
    5. For **vCPUs**, specify the number of vCPUs to reserve for the
     container. This parameter maps to `CpuShares` in the
     [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the
     `--cpu-shares` option to [**docker
     run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). Each vCPU is equivalent to 1,024 CPU shares. You must specify at
     least one vCPU.
    6. For **Memory**, specify the hard limit (in MiB) of memory to present to
     the job's container. If your container attempts to exceed the memory specified here, the
     container is stopped. This parameter maps to `Memory` in the
     [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the
     `--memory` option to [**docker
     run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). You must specify at least 4 MiB of memory for a job.


    ###### Note

    To maximize your resource utilization, you can provide your jobs as much memory as
     possible for a particular instance type. For more information, see [Compute resource memory management](memory-management.md "memory-management.md").
    7. (Optional) For **Number of GPUs**, specify the number of GPUs your job
     uses. The job runs on a container with the specified number of GPUs that are pinned to that
     container.
    8. (Optional) For **Job role**, you can specify an IAM role that
     provides the container in your job with permissions to use the AWS APIs. This feature uses
     Amazon ECS IAM roles for task functionality. For more information including configuration
     prerequisites, see [IAM Roles for Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md")
     in the *Amazon Elastic Container Service Developer Guide*.


    ###### Note

    For jobs that are running on Fargate resources, a job role is required.


    ###### Note

    Only roles that have the **Amazon Elastic Container Service Task Role** trust relationship
     are shown here. For more information about creating an IAM role for your AWS Batch jobs, see
     [Creating an
     IAM Role and Policy for your Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role "../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role") in the
     *Amazon Elastic Container Service Developer Guide*.
    9. (Optional) For **Execution role**, specify an IAM role that grants
     the Amazon ECS container agents permission to make AWS API calls on your behalf. This feature
     uses Amazon ECS IAM roles for task functionality. For more information, see [Amazon ECS task execution IAM roles](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the *Amazon Elastic Container Service Developer Guide*.

19. (Optional) Expand **Additional configuration**:
    1.  For **Environment variables**, choose **Add environment
        variable** to add environment variables as name-value pairs. These variables are
        passed to the container.
    2.  For **Job role configuration**, you can specify an IAM role that
        provides the container in your job with permissions to use the AWS APIs. This feature uses
        Amazon ECS IAM roles for task functionality. For more information including configuration
        prerequisites, see [IAM Roles for Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md")
        in the _Amazon Elastic Container Service Developer Guide_.

    ###### Note

    For jobs that are running on Fargate resources, a job role is required.

    ###### Note

    Only roles that have the **Amazon Elastic Container Service Task Role** trust relationship
    are shown here. For more information about how to create an IAM role for your AWS Batch
    jobs, see [Creating an IAM Role and Policy for your Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role "../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role") in the
    _Amazon Elastic Container Service Developer Guide_. 3. For **Execution role**, specify an IAM role that grants the Amazon ECS
    container agents permission to make AWS API calls on your behalf. This feature uses Amazon ECS
    IAM roles for task functionality. For more information, see [Amazon ECS task execution IAM
    roles](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the _Amazon Elastic Container Service Developer Guide_.

20. In the **Security Configuration** section:
    1.  (Optional) To give your job's container elevated privileges on the host instance
        (similar to the `root` user), turn on **Privileged**. This
        parameter maps to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section
        of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `--privileged` option to [**docker
        run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/").
    2.  (Optional) For **User**, enter the user name to use inside the
        container. This parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate")
        section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `--user` option to [**docker
        run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/").
    3.  (Optional) For **Secrets**, choose **Add secret** to
        add secrets as a name-value pairs. These secrets are exposed in the container. For more
        information, see [LogConfiguration:secretOptions](../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions "../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions").

21. In the **Linux configuration** section:
    1.  Turn on **Enable read only filesystem** to remove write access to the
        volume.
    2.  (Optional) Turn on **Enable init process** to run an
        `init` process inside the container. This process forwards signals and reaps
        processes.
    3.  For **Shared memory size**, enter the size (in MiB) of the
        `/dev/shm` volume.
    4.  For **Max swap size**, enter the total amount of swap memory (in MiB)
        that the container can use.
    5.  For **Swappiness** enter a value between 0 and 100 to indicate the
        swappiness behavior of the container. If you don't specify a value and swapping is enabled,
        value defaults to 60. For more information, see [LinuxParameters:swappiness](../APIReference/API_LinuxParameters.md#Batch-Type-LinuxParameters-swappiness "../APIReference/API_LinuxParameters.md#Batch-Type-LinuxParameters-swappiness").
    6.  (Optional) For **Devices**, choose **Add device** to
        add a device:
        1. For **Container path**, specify the path of in the container instance
           to expose the device mapped to the host instance. If you keep this blank, the host path is
           used in the container.
        2. For **Host path**, specify the path of a device in the host
           instance.
        3. For **Permissions**, choose one or more permissions to apply to the
           device. The available permissions are **READ**,
           **WRITE**, and **MKNOD**.

22. (Optional) For **Mount points**, choose **Add mount points
    configuration** to add mount points for data volumes. You must specify the source
    volume and container path. These mount points are passed to the Docker daemon on
    a container instance. You can also choose to make the volume **Read
    only**.
23. (Optional) For **Ulimits configuration**, choose **Add
    ulimit** to add a `ulimits` value for the container. Enter
    **Name**, **Soft limit**, and **Hard
    limit** values, and then choose **Add ulimit**.
24. (Optional) For **Volumes configuration**, choose **Add
    volume** to create a list of volumes to pass to the container. Enter
    **Name** and **Source path** for the volume and then choose
    **Add volume**. You can also choose to turn on **Enable
    EFS**.
25. (Optional) For **Tmpfs**, choose **Add tmpfs** to add a
    `tmpfs` mount.
26. In the **Task properties** section:
    1.  For **Execution role - conditional**, choose a role to allow Amazon ECS
        agents to make AWS API calls on your behalf. For more information on creating an
        **Execution role**, see [Tutorial: Create the IAM execution role](create-execution-role.md "create-execution-role.md").
    2.  ###### Important

    To use **ECS execute command** your compute environment must meet the [compute environment considerations for multi node parallel
    jobs](mnp-ce.md "mnp-ce.md").

    Choose **Enable ECS execute command**, to enable access to the Amazon ECS
    container shell directly and bypass the host OS. You must choose a **Task
    role**.

    ###### Important

    The **ECS execute** command requires that file system be writable. 3. For **Task role**, choose an Amazon ECS Identity and Access Management (IAM)
    role to allow the container to make AWS API calls on your behalf. For more information see,
    [Amazon ECS
    task IAM role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") in the _Amazon Elastic Container Service Developer Guide_.

27. (Optional) In the **Logging configuration** section:
    1.  For **Log driver**, choose the log driver to use. For more information
        about the available log drivers, see [LogConfiguration:logDriver](../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-logDriver "../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-logDriver").

    ###### Note

    By default, the `awslogs` log driver is used. 2. For **Options**, choose **Add option** to add an
    option. Enter a name-value pair, and then choose **Add option**. 3. For **Secrets**, choose **Add secret**. Enter a
    name-value pair and then choose **Add secret** to add a secret.

    ###### Tip

    For more information, see [LogConfiguration:secretOptions](../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions "../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions").

28. Choose **Next page**.
29. For **Job definition review**, review the configuration
    steps. If you need to make changes, choose **Edit**. When you're
    finished, choose **Create job definition**.
