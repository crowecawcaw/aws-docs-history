# Amazon ECS task definition differences for Fargate

In order to use Fargate, you must configure your task definition to use the Fargate
launch type. There are additional considerations when using Fargate.

## Task definition parameters

Tasks that use Fargate don't support all of the Amazon ECS
task definition parameters that are available. Some parameters aren't supported at all,
and others behave differently for Fargate tasks.

The following task definition parameters are not valid in Fargate
tasks:

- `disableNetworking`
- `dnsSearchDomains`
- `dnsServers`
- `dockerSecurityOptions`
- `extraHosts`
- `gpu`
- `ipcMode`
- `links`
- `placementConstraints`
- `privileged`
- `maxSwap`
- `swappiness`

The following task definition parameters are valid in Fargate tasks, but
have limitations that should be noted:

- `linuxParameters` – When specifying Linux-specific options
  that are applied to the container, for `capabilities` the only
  capability you can add is `CAP_SYS_PTRACE`. The `devices`,
  `sharedMemorySize`, and `tmpfs` parameters are not
  supported. For more information, see [Linux parameters](task_definition_parameters.md#container_definition_linuxparameters "task_definition_parameters.md#container_definition_linuxparameters").
- `volumes` – Fargate tasks only support bind
  mount host volumes, so the `dockerVolumeConfiguration` parameter is
  not supported. For more information, see [Volumes](task_definition_parameters.md#volumes "task_definition_parameters.md#volumes").
- `cpu` - For Windows containers on AWS Fargate, the
  value cannot be less than 1 vCPU.
- `networkConfiguration` - Fargate tasks always use the
  `awsvpc` network mode.

To ensure that your task definition validates for use with Fargate, you
can specify the following when you register the task definition:

- In the AWS Management Console, for the **Requires Compatibilities** field,
  specify `FARGATE`.
- In the AWS CLI, specify the `--requires-compatibilities`
  option.
- In the Amazon ECS API, specify the `requiresCompatibilities`
  flag.

## Operating Systems and architectures

When you configure a task and container definition for AWS Fargate, you
must specify the Operating System that the container runs. The following Operating
Systems are supported for AWS Fargate:

- Amazon Linux 2

###### Note

Linux containers use only the kernel and kernel configuration from the
host Operating System. For example, the kernel configuration includes the
`sysctl` system controls. A Linux container image can be made
from a base image that contains the files and programs from any Linux
distribution. If the CPU architecture matches, you can run containers from
any Linux container image on any Operating System.

- Windows Server 2019 Full
- Windows Server 2019 Core
- Windows Server 2022 Full
- Windows Server 2022 Core

When you run Windows containers on AWS Fargate, you must have the X86_64
CPU architecture.

When you run Linux containers on AWS Fargate, you can use the X86_64 CPU
architecture, or the ARM64 architecture for your ARM-based applications. For more
information, see [Amazon ECS task definitions for 64-bit ARM workloads](ecs-arm64.md "ecs-arm64.md").

## Task CPU and memory

Amazon ECS task definitions for AWS Fargate require that you specify CPU and
memory at the task level. Most use cases are satisfied by only specifying these
resources at the task level. The table below shows the valid combinations of task-level
CPU and memory. You can specify memory values in the task definition as a string in MiB
or GB. For example, you can specify a memory value either as `3072` in MiB or
`3 GB` in GB. You can specify CPU values in the JSON file as a string in
CPU units or virtual CPUs (vCPUs). For example, you can specify a CPU value either as
`1024` in CPU units or `1 vCPU` in vCPUs.

| CPU value                                                                      | Memory value                                | Operating systems supported for<br>AWS Fargate |
| ------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------- |
| 256 (.25 vCPU)                                                                 | 512 MiB, 1 GB, 2 GB                         | Linux                                          |
| 512 (.5 vCPU)                                                                  | 1 GB, 2 GB, 3 GB, 4 GB                      | Linux                                          |
| 1024 (1 vCPU)                                                                  | 2 GB, 3 GB, 4 GB, 5 GB, 6 GB, 7 GB, 8 GB    | Linux, Windows                                 |
| 2048 (2 vCPU)                                                                  | Between 4 GB and 16 GB in 1 GB increments   | Linux, Windows                                 |
| 4096 (4 vCPU)                                                                  | Between 8 GB and 30 GB in 1 GB increments   | Linux, Windows                                 |
| 8192 (8 vCPU)<br>NoteThis option requires Linux platform `1.4.0` or<br>later.  | Between 16 GB and 60 GB in 4 GB increments  | Linux                                          |
| 16384 (16vCPU)<br>NoteThis option requires Linux platform `1.4.0` or<br>later. | Between 32 GB and 120 GB in 8 GB increments | Linux                                          |

## Task networking

Amazon ECS tasks for AWS Fargate require the `awsvpc` network mode,
which provides each task with an elastic network interface. When you run a task or
create a service with this network mode, you must specify one or more subnets to attach
the network interface and one or more security groups to apply to the network interface.

If you are using public subnets, decide whether to provide a public IP address for the
network interface. For a Fargate task in a public subnet to pull container
images, a public IP address needs to be assigned to the task's elastic network
interface, with a route to the internet or a NAT gateway that can route requests to the
internet. For a Fargate task in a private subnet to pull container images,
you need a NAT gateway in the subnet to route requests to the internet. When you host
your container images in Amazon ECR, you can configure Amazon ECR to use an interface VPC
endpoint. In this case, the task's private IPv4 address is used for the image pull. For
more information about Amazon ECR interface endpoints, see [Amazon ECR interface VPC
endpoints (AWS PrivateLink)](../../../AmazonECR/latest/userguide/vpc-endpoints.md "../../../AmazonECR/latest/userguide/vpc-endpoints.md") in the _Amazon Elastic Container Registry User Guide_.

The following is an example of the `networkConfiguration` section for a
Fargate service:

```
"networkConfiguration": {
   "awsvpcConfiguration": {
      "assignPublicIp": "ENABLED",
      "securityGroups": [ "`sg-12345678`" ],
      "subnets": [ "`subnet-12345678`" ]
   }
}
```

## Task resource limits

Amazon ECS task definitions for Linux containers on AWS Fargate support the
`ulimits` parameter to define the resource limits to set for a
container.

Amazon ECS task definitions for Windows on AWS Fargate do not support the
`ulimits` parameter to define the resource limits to set for a
container.

Amazon ECS tasks hosted on Fargate use the default
resource limit values set by the operating system with the exception of
the `nofile` resource limit parameter. The `nofile` resource limit sets a restriction on
the number of open files that a container can use. On Fargate, the default
`nofile` soft limit is `65535` and hard limit
is `65535`. You can set the values of both limits up to `1048576`.

The following is an example task definition snippet that shows how to define a custom
`nofile` limit that has been doubled:

```
"ulimits": [
    {
       "name": "nofile",
       "softLimit": `2048`,
       "hardLimit": `8192`
    }
]
```

For more information on the other resource limits that can be adjusted, see [Resource limits](task_definition_parameters.md#container_definition_limits "task_definition_parameters.md#container_definition_limits").

## Logging

### Event logging

Amazon ECS logs the actions that it takes to EventBridge. You can use Amazon ECS events for EventBridge to
receive near real-time notifications regarding the current state of your Amazon ECS
clusters, services, and tasks. Additionally, you can automate actions to respond to
these events. For more information, see [Automate responses to Amazon ECS errors using EventBridge](cloudwatch_event_stream.md "cloudwatch_event_stream.md").

### Task lifecycle logging

Tasks that run on Fargate publish timestamps to track the task through the
states of the task lifecycle. You can see the timestamps in the task details in the
AWS Management Console and by describing the task in the AWS CLI and SDKs. For example, you can use
the timestamps to evaluate how much time the task spent downloading the container
images and decide if you should optimize the container image size, or use Seekable
OCI indexes. For more information about container image practices, see [Best practices for Amazon ECS container images](container-considerations.md "container-considerations.md").

### Application logging

Amazon ECS task definitions for AWS Fargate support the
`awslogs`, `splunk`, and `awsfirelens` log
drivers for the log configuration.

The `awslogs` log driver configures your Fargate tasks to
send log information to Amazon CloudWatch Logs. The following shows a snippet of a task
definition where the `awslogs` log driver is configured:

```
"logConfiguration": {
   "logDriver": "awslogs",
   "options": {
      "awslogs-group" : "/ecs/fargate-task-definition",
      "awslogs-region": "us-east-1",
      "awslogs-stream-prefix": "ecs"
   }
}
```

For more information about using the `awslogs` log driver in a task
definition to send your container logs to CloudWatch Logs, see [Send Amazon ECS logs to CloudWatch](using_awslogs.md "using_awslogs.md").

For more information about the `awsfirelens` log driver in a task
definition, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

For more information about using the `splunk` log driver in a task
definition, see [splunk log driver](example_task_definitions.md#example_task_definition-splunk "example_task_definitions.md#example_task_definition-splunk").

## Task storage

For Amazon ECS tasks hosted on Fargate, the following storage types are
supported:

- Amazon EBS volumes provide cost-effective, durable, high-performance block
  storage for data-intensive containerized workloads. For more information, see
  [Use Amazon EBS volumes with Amazon ECS](ebs-volumes.md "ebs-volumes.md").
- Amazon EFS volumes for persistent storage. For more information, see [Use Amazon EFS volumes with Amazon ECS](efs-volumes.md "efs-volumes.md").
- Bind mounts for ephemeral storage. For more information, see [Use bind mounts with Amazon ECS](bind-mounts.md "bind-mounts.md").

## Lazy loading container images using Seekable OCI (SOCI)

Amazon ECS tasks on Fargate that use Linux platform version `1.4.0` can use
Seekable OCI (SOCI) to help start tasks faster.
With SOCI, containers only spend a few seconds on the image pull before
they can start, providing time for environment setup and application
instantiation while the image is downloaded in the background.
This is called _lazy loading_. When Fargate starts an Amazon ECS task, Fargate automatically detects
if a SOCI index exists for an image in the task and starts the container without waiting
for the entire image to be downloaded.

For containers that run without SOCI indexes, container images are downloaded completely before the container
is started. This behavior is the same on all other platform versions of Fargate and on the
Amazon ECS-optimized AMI on Amazon EC2 instances.

Seekable OCI (SOCI) is an open source technology developed by AWS that can launch
containers faster by lazily loading the container image. SOCI works by creating an index
(SOCI Index) of the files within an existing container image. This index helps to launch
containers faster, providing the capability to extract an
individual file from a container image before downloading the entire image.
The SOCI index must be stored as an artifact in the same repository as the image
within the container registry. You should only use SOCI indices from trusted sources,
as the index is the authoritative source for the contents of the image.

For more information, see [Introducing Seekable OCI for lazy loading container
images](https://aws.amazon.com/about-aws/whats-new/2022/09/introducing-seekable-oci-lazy-loading-container-images/ "https://aws.amazon.com/about-aws/whats-new/2022/09/introducing-seekable-oci-lazy-loading-container-images/").

Customers looking to use SOCI will only be able to use the SOCI index manifest v2.
Existing customers that have previously used SOCI on Fargate can continue to use the
SOCI Index Manifest v1, however we strongly advise those customers migrate to SOCI Index
Manifest v2. The SOCI Index Manifest v2 creates an explicit relationship between
container images and their SOCI indexes to ensure consistent deployments.

###### Considerations

If you want Fargate to use a SOCI index to lazily load container images in a
task, consider the following:

- Only tasks that run on Linux platform version `1.4.0` can use SOCI
  indexes. Tasks that run Windows containers on Fargate aren't supported.
- Tasks that run on X86_64 or ARM64 CPU architecture are supported.
- Container images in the task definition must be stored in a
  compatible image registry. The following lists the compatible registries:
  - Amazon ECR private registries.

- Only container images that use gzip compression, or are not
  compressed are supported. Container images that use zstd
  compression aren't supported.
- For SOCI Index Manifest v2, generating a SOCI index manifest modifies the container
  image manifest as we add an annotation for the SOCI index. This results in a new
  container image digest. The contents of the container images filesystem layers
  do not change.
- For SOCI Index Manifest v2, when the container image has already been stored in the
  container image repository, after a SOCI index has been generated, you need to
  repush the container image. Re-pushing a container image will not increase
  storage costs by duplicating the filesystem layers, it only uploads a new
  manifest file.
- We recommend that you try lazy loading with container images greater than
  250 MiB compressed in size. You are less likely to see a reduction in the time
  to load smaller images.
- Because lazy loading can change how long your tasks take to start, you might
  need to change various timeouts like the health check grace period for Elastic Load Balancing.
- If you want to prevent a container image from being lazy loaded, the container image will need to be repushed without a SOCI index attached.

###### Creating a Seekable OCI index

For a container image to be lazy loaded it needs a SOCI index (a metadata file)
created and stored in the container image repository along side the container image.
To create and push a SOCI index you can use the open source [soci-snapshotter CLI tool](https://github.com/awslabs/soci-snapshotter "https://github.com/awslabs/soci-snapshotter") on GitHub.
Or, you can deploy the CloudFormation AWS SOCI Index Builder. This is a serverless
solution that automatically creates and pushes a SOCI index when a container image
is pushed to Amazon ECR. For more information about the solution and the installation
steps, see [CloudFormation
AWS SOCI Index Builder](https://awslabs.github.io/cfn-ecr-aws-soci-index-builder/ "https://awslabs.github.io/cfn-ecr-aws-soci-index-builder/") on GitHub. The CloudFormation AWS SOCI Index
Builder is a way to automate getting started with SOCI, while the open source soci
tool has more flexibility around index generation and the ability to integrate index
generation in your continuous integration and continuous delivery (CI/CD)
pipelines.

###### Note

For the SOCI index to be created for an image, the image must exist in the
containerd image store on the computer running `soci-snapshotter`.
If the image is in the Docker image store, the image can't be found.

###### Verifying that a task used lazy loading

To verify that a task was lazily loaded using SOCI, check the task
metadata endpoint from inside the task. When you query the task metadata endpoint
version 4, there is a `Snapshotter` field in the default path for the
container that you are querying from. Additionally, there are
`Snapshotter` fields for each container in the `/task` path.
The default value for this field is `overlayfs`,
and this field is set to `soci` if SOCI is used. To verify that a container image has a SOCI Index Manifest v2 attached you can retrieve the Image Index from Amazon ECR using the AWS CLI.

```

IMAGE_REPOSITORY=r
IMAGE_TAG=latest

aws ecr batch-get-image \
    --repository-name=$IMAGE_REPOSITORY \
    --image-ids imageTag=$IMAGE_TAG \
    --query 'images[0].imageManifest' --output text | jq -r '.manifests[] | select(.artifactType=="application/vnd.amazon.soci.index.v2+json")'

```

To verify that a container image has a SOCI Index Manifest v1 attached you can use the OCI Referrers API.

```

ACCOUNT_ID=111222333444
AWS_REGION=us-east-1
IMAGE_REPOSITORY=nginx-demo
IMAGE_TAG=latest
IMAGE_DIGEST=$(aws ecr describe-images --repository-name $IMAGE_REPOSITORY --image-ids imageTag=$IMAGE_TAG --query 'imageDetails[0].imageDigest' --output text)
ECR_PASSWORD=$(aws ecr get-login-password)

curl \
    --silent \
    --user AWS:$ECR_PASSWORD \
    https://$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/v2/$IMAGE_REPOSITORY/referrers/$IMAGE_DIGEST?artifactType=application%2Fvnd.amazon.soci.index.v1%2Bjson | jq -r '.'

```
