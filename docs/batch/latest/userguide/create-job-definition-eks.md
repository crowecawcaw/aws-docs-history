# Create a single-node job definition on Amazon EKS

resources

Complete the following steps to create a single-node job definition on Amazon Elastic Kubernetes Service (Amazon EKS).

###### To create a new job definition on Amazon EKS resources:

1.  Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2.  From the top navigation bar, choose the AWS Region to use.
3.  In the left navigation pane, choose **Job definitions**.
4.  Choose **Create**.
5.  For **Orchestration type**, choose **Elastic Kubernetes
    Service (EKS)**.
6.  For **Name**, enter a unique name for your job definition. The
    name can be up to 128 characters in length. It can contain uppercase and lowercase
    letters, numbers, hyphens (-), and underscores (\_).
7.  (Optional) For **Execution timeout**, enter the timeout value (in
    seconds). The execution timeout is the length of time before an unfinished job is
    terminated. If an attempt exceeds the timeout duration, the attempt is stopped and
    moves to a `FAILED` status. For more information, see [Job timeouts](job_timeouts.md "job_timeouts.md"). The minimum value is 60
    seconds.
8.  (Optional) Turn on **Scheduling priority**. Enter a scheduling
    priority value between 0 and 100. Higher values are given higher priority over lower
    values.
9.  (Optional) Expand **Tags**, and then choose **Add
    tag** to add tags to the resource.
10. Choose **Next page**.
11. In the **EKS pod properties** section:
    1. For **Service account name**, enter an account that
       provides an identity for processes that run in a pod.
    2. Turn **Host network** on to use the
       Kubernetes
       pod network model and open a listening port for incoming
       connections. Turn this setting off for outgoing communications only.
    3. For **DNS policy**, choose one of the following:
       - No value (null) – The
         pod ignores the DNS settings from the
         Kubernetes environment.
       - Default – The
         pod inherits the name resolution configuration
         from the node that it runs on.

       ###### Note

       If a DNS policy isn't specified, **Default**
       isn't the default DNS policy. Instead,
       **ClusterFirst** is used.
       - ClusterFirst – Any DNS query
         that doesn't match the configured cluster domain suffix is forwarded
         to the upstream nameserver that's inherited from the node.
       - ClusterFirstWithHostNet –
         Use if **Host network** is turned on.

    4. (Optional) For **Volumes**, select **Add volume**,
       then:
       1. Add a **Name** for your volume.
       2. (Optional) Add the **Host path** for the directory on the host.
       3. (Optional) Add a **Medium** and a **Size limit** to
          configure a [Kubernetes emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir "https://kubernetes.io/docs/concepts/storage/volumes/#emptydir").
       4. (Optional) Provide a **Secret name** for the pod and whether the secret is
          **Optional**.
       5. (Optional) Define a **Claim name** to attach a Kubernetes [Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/ "https://kubernetes.io/docs/concepts/storage/persistent-volumes/") to the pod, and whether it is
          **Read only**.

    5. (Optional) For **Pod labels**, choose **Add pod
       labels**, then enter a name-value pair.

    ###### Important

    The prefix for a pod label can't contain `kubernetes.io/`,
    `k8s.io/`, or `batch.amazonaws.com/`. 6. (Optional) For **Pod annotations**, choose **Add
    annotations**, then enter a name-value pair.

    ###### Important

    The prefix for a pod annotation can't contain `kubernetes.io/`,
    `k8s.io/`, or `batch.amazonaws.com/`. 7. Choose **Next page**. 8. In the **Container configuration** section:

        1. For **Name**, enter a unique name for the
         container. The name must start with a letter or number, and can be
         up to 63 characters long. It can contain uppercase and lowercase
         letters, numbers, and hyphens (-).
        2. For **Image**, choose the Docker
         image to use for your job. By default, images in the Docker Hub
         registry are available. You can also specify other repositories with
         ``repository-url`/`image`:`tag``.
         The name can be up to 255 characters long. It can contain uppercase
         and lowercase letters, numbers, hyphens (-), underscores (\_), colons
         (:), periods (.), forward slashes (/), and number signs (#). This
         parameter maps to `Image` in the
         [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/")
         and the `IMAGE` parameter of [**docker run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/")


        ###### Note

        Docker image architecture must match the processor architecture of the compute resources that they're
         scheduled on. For example, ARM-based Docker images can only run on ARM-based compute resources.




        	* Images in Amazon ECR Public repositories use the full
        	 `registry/repository[:tag]` or
        	 `registry/repository[@digest]` naming
        	 conventions (for example,
        	 `public.ecr.aws/`registry_alias`/`my-web-app`:`latest``).
        	* Images in Amazon ECR repositories use the full
        	 `registry/repository[:tag]` naming convention
        	 (for example,
        	 ``aws_account_id`.dkr.ecr.`region`.amazonaws.com``/`my-web-app`:`latest``).
        	* Images in official repositories on Docker
        	 Hub use a single name (for example,
        	 `ubuntu` or `mongo`).
        	* Images in other repositories on Docker Hub
        	 are qualified with an organization name (for example,
        	 `amazon/amazon-ecs-agent`).
        	* Images in other online repositories are qualified further
        	 by a domain name (for example,
        	 `quay.io/assemblyline/ubuntu`).
        3. (Optional) For **Image pull policy**, choose when
         images are pulled.
        4. (Optional) For **Command**, enter a
         JSON command to pass to
         the container.
        5. (Optional) For **Arguments**, enter arguments to
         pass to the container. If an argument isn't provided, the container
         image command is used.

    9. (Optional) You can add parameters to the job definition as name-value
       mappings to override the job definition defaults. To add a parameter:
       1. For **Parameters**, enter a name-value pair, then
          choose **Add parameter**.

       ###### Important

       If you choose **Add parameter**, you must
       configure at least one parameter or choose **Remove
       parameter**

    10. In the **Environment configuration** section:
        1. For **vCPUs**, enter the number of vCPUs to
           reserve for the container. This parameter maps to
           `CpuShares` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate")
           section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `--cpu-shares`
           option to [**docker run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). Each vCPU is
           equivalent to 1,024 CPU shares. You must specify at least one
           vCPU.
        2. For **Memory**, enter the memory limit available
           to the container. If your container attempts to exceed the memory
           specified here, the container is stopped. This parameter maps to
           `Memory` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate")
           section of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `--memory`
           option to [**docker run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). You must specify at
           least 4 MiB of memory for a job.

        ###### Note

        To maximize your resource utilization, prioritize memory for
        jobs of a specific instance type. For more information, see
        [Compute resource memory management](memory-management.md "memory-management.md").

    11. (Optional) For **Environment variables**, choose
        **Add environment variable** to add environment
        variables as name-value pairs. These variables are passed to the
        container.
    12. (Optional) For **Volume mount**:
        1. Choose **Add volume mount**.
        2. Enter a **Name**, and then enter a
           **Mount path** in the container where the
           volume is mounted. Enter a **SubPath** to specify a
           sub-path inside the referenced volume instead of its root.
        3. Choose **Read only** to remove write permissions
           to the volume.
        4. Choose **Add volume mount**.

    13. (Optional) For **Run as user**, enter a user ID to run
        the container process.

    ###### Note

    The user ID must exist in the image for the container to run. 14. (Optional) For **Run as group**, enter a group ID to run
    the container process runtime.

    ###### Note

    The group ID must exist in the image for the container to run. 15. (Optional) To give your job's container elevated permissions on the host
    instance (similar to the `root` user), drag the
    **Privileged** slider to the right. This parameter maps
    to `Privileged` in the [Create a container](https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate "https://docs.docker.com/engine/api/v1.38/#operation/ContainerCreate") section
    of the [Docker Remote API](https://docs.docker.com/engine/api/v1.38/ "https://docs.docker.com/engine/api/v1.38/") and the `--privileged` option to [**docker run**](https://docs.docker.com/engine/reference/commandline/run/ "https://docs.docker.com/engine/reference/commandline/run/"). 16. (Optional) Turn on **Read-only root filesystem** to
    remove write access to the root filesystem. 17. (Optional) Turn on **Run as non-root** to run the
    containers in the pod as a non-root user.

    ###### Note

    If **Run as non-root** is turned on, the
    kubelet validates the image at runtime to verify that
    image doesn't run as UID 0. 18. Choose **Next page**.

12. For **Job definition review**, review the
    configuration steps. If you need to make changes, choose **Edit**. When you're finished, choose **Create job
    definition**.
