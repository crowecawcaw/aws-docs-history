# Create a single-node job definition on Amazon EC2

resources

Complete the following steps to create a single-node job definition on Amazon Elastic Compute Cloud (Amazon EC2) resources.

###### To create a new job definition on Amazon EC2 resources:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, choose the AWS Region to use.
3. In the left navigation pane, choose **Job definitions**.
4. Choose **Create**.
5. For **Orchestration type,** choose **Amazon Elastic Compute Cloud
   (Amazon EC2)**.
6. For **EC2 platform configuration**, turn off **Enable
   multi-node parallel** processing.
7. For **Name**, enter a unique name for your job definition. The name can
   be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers,
   hyphens (-), and underscores (\_).
8. (Optional) For **Execution timeout**, enter the timeout value (in
   seconds). The execution timeout is the length of time before an unfinished job is
   terminated. If an attempt exceeds the timeout duration, the attempt is stopped and moves to
   a `FAILED` status. For more information, see [Job timeouts](job_timeouts.md "job_timeouts.md"). The minimum value is 60 seconds.
9. (Optional) Turn on **Scheduling priority**. Enter a scheduling priority
   value between 0 and 100. Higher values are given higher priority.
10. (Optional) For **Job attempts**, enter the number of times that AWS Batch
    attempts to move the job to `RUNNABLE` status. Enter a number between 1 and
11.
12. (Optional) For **Retry strategy conditions**, choose **Add
    evaluate on exit**. Enter at least one parameter value and then choose an
    **Action**. For each set of conditions, **Action** must
    be set to either **Retry** or **Exit**. These actions mean
    the following:
    - Retry – AWS Batch retries until the number of
      job attempts that you specified is reached.
    - Exit – AWS Batch stops retrying the job.

###### Important

If you choose **Add evaluate on exit**, you must configure at least
one parameter and either choose an **Action** or choose **Remove
evaluate on exit**. 12. (Optional) Expand **Tags** and then choose **Add tag**
to add tags to the resource. Enter a key and optional value, then choose **Add
tag**. 13. (Optional) Turn on **Propagate tags** to propagate tags from the job
and job definition to the Amazon ECS task. 14. Choose **Next page**. 15. In the **Container configuration** section:

    1. For **Image**, choose the Docker image to use for
     your job. By default, images in the Docker Hub registry are available.
     You can also specify other repositories with
     ``repository-url`/`image`:`tag``.
     The name can be up to 225 characters in length. It can contain uppercase and lowercase
     letters, numbers, hyphens (-), underscores (\_), colons (:), forward slashes (/), and
     number signs (#). This parameter maps to `Image` in the
     [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the
     `IMAGE` parameter of [**docker
     run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/").


    ###### Note

    Docker image architecture must match the processor architecture of the compute resources that they're
     scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.




    	* Images in Amazon ECR Public repositories use the full
    	 `registry/repository[:tag]` or
    	 `registry/repository[@digest]` naming conventions (for example,
    	 `public.ecr.aws/`registry_alias`/`my-web-app`:`latest``).
    	* Images in Amazon ECR repositories use the full `registry/repository[:tag]`
    	 naming convention (for example,
    	 ``aws_account_id`.dkr.ecr.`region`.amazonaws.com``/`my-web-app`:`latest``).
    	* Images in official repositories on Docker Hub use a single name
    	 (for example, `ubuntu` or `mongo`).
    	* Images in other repositories on Docker Hub are qualified with an
    	 organization name (for example, `amazon/amazon-ecs-agent`).
    	* Images in other online repositories are qualified further by a domain name (for
    	 example, `quay.io/assemblyline/ubuntu`).
    2. For **Command**, enter the commands into the field as their **JSON** string array equivalent.


    This parameter maps to `Cmd` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate")
     section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `COMMAND` parameter to [**docker
     run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). For more information about the Docker
     `CMD` parameter, see [https://docs.docker.com/engine/reference/builder/#cmd](https://docs.docker.com/engine/reference/builder/#cmd "https://docs.docker.com/engine/reference/builder/#cmd").


    ###### Note

    You can use default values for parameter substitution and placeholders in your
     command. For more information, see [Parameters](job_definition_parameters.md#parameters "job_definition_parameters.md#parameters").
    3. (Optional) For **Execution role**, specify an IAM role that
     grants the Amazon ECS container agents permission to make AWS API calls on your behalf.
     This feature uses Amazon ECS IAM roles for tasks. For more information, see [Amazon ECS task
     execution IAM roles](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the *Amazon Elastic Container Service Developer Guide*.
    4. For **Job Role configuration**, choose an IAM role that has
     permissions to the AWS APIs. This feature uses Amazon ECS IAM roles for tasks. For more
     information, see [IAM Roles for
     Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") in the *Amazon Elastic Container Service Developer Guide*.


    ###### Note

    Only roles that have the **Amazon Elastic Container Service Task Role** trust
     relationship are shown here. For more information about creating an IAM role for
     your AWS Batch jobs, see [Creating an
     IAM Role and Policy for your Tasks](../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role "../../../AmazonECS/latest/developerguide/task-iam-roles.md#create_task_iam_policy_and_role") in the
     *Amazon Elastic Container Service Developer Guide*.

16. For **Parameters**, choose **Add parameters** to
    add parameter substitution placeholders as **Key** and optional
    **Value** pairs.
17. In the **Environment configuration** section:
    1.  For **vCPUs**, enter the number of vCPUs to reserve for the
        container. This parameter maps to `CpuShares` in the
        [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the
        `--cpu-shares` option to [**docker
        run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). Each vCPU is equivalent to 1,024 CPU shares. You must specify
        at least one vCPU.
    2.  For **Memory**, enter the memory limit available to the container.
        If your container attempts to exceed the amount of memory that you specify here, the
        container is stopped. This parameter maps to `Memory` in the
        [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the
        `--memory` option to [**docker
        run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). You must specify at least 4 MiB of memory for a job.

    ###### Note

    To maximize your resource utilization, prioritize memory for jobs of a specific
    instance type. For more information, see [Compute resource memory management](memory-management.md "memory-management.md"). 3. For **Number of GPUs**, choose the number of GPUs to reserve for
    the container. 4. (Optional) For **Environment variables**, choose **Add
    environment variable** to add environment variables as name-value pairs.
    These variables are passed to the container. 5. (Optional) For **Secrets**, choose **Add secret**
    to add secrets as a name-value pairs. These secrets are exposed in the container. For
    more information, see [LogConfiguration:secretOptions](../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions "../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions").

18. Choose **Next page**.
19. In the **Linux configuration** section:
    1.  For **User**, enter the user name to use inside the container. This
        parameter maps to `User` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of
        the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `--user` option to [**docker
        run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/").
    2.  (Optional) To give the job container elevated permissions on the host instance
        (similar to the `root` user), drag the **Privileged** slider
        to the right. This parameter maps to `Privileged` in the
        [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the
        `--privileged` option to [**docker
        run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/").
    3.  (Optional) Turn on **Enable init process** to run an
        `init` process inside the container. This process forwards signals and
        reaps processes.

20. (Optional) In the **Filesystem configuration** section:
    1.  Turn on **Enable read only filesystem** to remove write access to
        the volume.
    2.  For **Shared memory size**, enter the size (in MiB) of the
        `/dev/shm` volume.
    3.  For **Max swap size**, enter the total amount of swap memory (in
        MiB) that the container can use.
    4.  For **Swappiness** enter a value between 0 and 100 to indicate the
        swappiness behavior of the container. If you don't specify a value and swapping is
        enabled, the value defaults to 60. For more information, see [LinuxParameters:swappiness](../APIReference/API_LinuxParameters.md#Batch-Type-LinuxParameters-swappiness "../APIReference/API_LinuxParameters.md#Batch-Type-LinuxParameters-swappiness").
    5.  (Optional) Expand **Additional configuration**.
    6.  (Optional) For **Tmpfs**, choose **Add tmpfs** to
        add a `tmpfs` mount.
    7.  (Optional) For **Devices**, choose **Add device**
        to add a device:
        1. For **Container path**, specify the path of in the container
           instance to expose the device mapped to the host instance. If you keep this blank,
           the host path is used in the container.
        2. For **Host path**, specify the path of a device in the host
           instance.
        3. For **Permissions**, choose one or more permissions to apply to
           the device. The available permissions are **READ**,
           **WRITE**, and **MKNOD**.

    8.  (Optional) For **Volumes configuration**, choose **Add
        volume** to create a list of volumes to pass to the container. Enter
        **Name** and **Source path** for the volume and then
        choose **Add volume**. You can also choose to turn on **Enable
        EFS**.
    9.  (Optional) For **Mount points**, choose **Add mount points
        configuration** to add mount points for data volumes. You must specify the
        source volume and container path. These mount points are passed to the Docker
        daemon on a container instance. You can also choose to make the volume
        **Read only**.
    10. (Optional) For **Ulimits configuration**, choose **Add
        ulimit** to add a `ulimits` value for the container. Enter
        **Name**, **Soft limit**, and **Hard
        limit** values, and then choose **Add ulimit**.

21. In the **Task properties** section:
    1.  For **Execution role - conditional**, choose a role to allow Amazon ECS
        agents to make AWS API calls on your behalf. For more information on creating an
        **Execution role**, see [Tutorial: Create the IAM execution role](create-execution-role.md "create-execution-role.md").
    2.  Choose **Enable ECS execute command**, to enable access to the
        Amazon ECS container shell directly and bypass the host OS. You must choose a **Task
        role**.

    ###### Important

    The **ECS execute** command requires that file system be
    writable. 3. For **Task role**, choose an Amazon ECS Identity and Access Management
    (IAM) role to allow the container to make AWS API calls on your behalf. For more
    information see, [Amazon ECS task IAM role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") in the
    _Amazon Elastic Container Service Developer Guide_.

22. (Optional) In the **Logging configuration** section:
    1.  For **Log driver**, choose the log driver to use. For more
        information about the available log drivers, see [LogConfiguration:logDriver](../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-logDriver "../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-logDriver").

    ###### Note

    By default, the `awslogs` log driver is used. 2. For **Options**, choose **Add option** to add an
    option. Enter a name-value pair, and then choose **Add option**. 3. For **Secrets**, choose **Add secret**. Enter a
    name-value pair and then choose **Add secret** to add a secret.

    ###### Tip

    For more information, see [LogConfiguration:secretOptions](../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions "../APIReference/API_LogConfiguration.md#Batch-Type-LogConfiguration-secretOptions").

23. Choose **Next page**.
24. For **Job definition review**, review the configuration
    steps. If you need to make changes, choose **Edit**. When
    you're finished, choose **Create job definition**.
