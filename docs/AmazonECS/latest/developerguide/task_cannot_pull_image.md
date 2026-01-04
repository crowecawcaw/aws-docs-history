# CannotPullContainer task errors in Amazon ECS

The following errors indicate that the task failed to start because Amazon ECS can't retrieve
the specified container image.

###### Note

The 1.4 Fargate platform version truncates long error messages.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

###### Tip

You can use the [Amazon ECS MCP server](ecs-mcp-introduction.md "ecs-mcp-introduction.md")
with AI assistants to investigate image pull errors using natural language.

###### Errors

- [The task can’t pull the image. Check
  that the role has the permissions to pull images from the registry.](#pull-request-image-not-found "#pull-request-image-not-found")
- [The task cannot pull
  ‘image-name’ from the Amazon ECR repository
  ‘repository URI’. There is a connection issue between
  the task and Amazon ECR. Check your task network configuration.](#pull-image-io-timeout "#pull-image-io-timeout")
- [The task can’t pull the image.
  Check your network configuration](#pull-request-image-not-found-network "#pull-request-image-not-found-network")
- [CannotPullContainerError: pull image manifest has been retried 5 time(s): failed to resolve ref](#pull-request-image-tag "#pull-request-image-tag")
- [API error (500): Get https://111122223333.dkr.ecr.us-east-1.amazonaws.com/v2/: net/http: request canceled while waiting for connection](#request-canceled "#request-canceled")
- [API error](#pull-request-api-error "#pull-request-api-error")
- [write /var/lib/docker/tmp/GetImageBlob111111111: no space left on device](#pull-request-write-error "#pull-request-write-error")
- [ERROR: toomanyrequests: Too Many Requests or You have reached your pull rate limit.](#container-pull-too-many-requests "#container-pull-too-many-requests")
- [Error response from daemon: Get url: net/http:
  request canceled while waiting for connection](#container-pull-request-canceled-connection "#container-pull-request-canceled-connection")
- [ref pull has been retried 1 time(s): failed to copy: httpReaderSeeker: failed open: unexpected status code](#container-pull-failed-open "#container-pull-failed-open")
- [pull access denied](#container-pull-access-denied.title "#container-pull-access-denied.title")
- [pull command failed: panic: runtime error: invalid memory address or nil pointer dereference](#container-pull-runtime-error.title "#container-pull-runtime-error.title")
- [error pulling image conf/error pulling image configuration](#container-pull-pulling-image.title "#container-pull-pulling-image.title")
- [Context canceled](#container-pull-context-canceled "#container-pull-context-canceled")

## The task can’t pull the image. Check

that the role has the permissions to pull images from the registry.

This error indicates that the task can't pull the image specified in the task
definition because of permission issues.

To resolve this issue:

1. Check that the image exists in the `repository`.
   For information about viewing your images, see [Viewing image details in
   Amazon ECR](../../../AmazonECR/latest/userguide/image-info.md "../../../AmazonECR/latest/userguide/image-info.md") in the _Amazon Elastic Container Registry User
   Guide_.
2. Verify that the `role-arn` has the correct
   permissions to pull the image.

For information about how to update roles, see [Update permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management Use
Guide_.

The task uses one of the following roles:

    * For tasks with the Fargate, this is the task execution
     role. For information about the additional permissions for Amazon ECR, [Fargate tasks pulling
     Amazon ECR images over interface endpoints permissions](task_execution_IAM_role.md#task-execution-ecr-conditionkeys "task_execution_IAM_role.md#task-execution-ecr-conditionkeys").
    * For tasks with EC2, this is the container instance
     role. For information about the additional permissions for Amazon ECR, [Amazon ECR permissions](instance_IAM_role.md#container-instance-role-ecr "instance_IAM_role.md#container-instance-role-ecr").

## The task cannot pull

‘`image-name`’ from the Amazon ECR repository
‘`repository URI`’. There is a connection issue between
the task and Amazon ECR. Check your task network configuration.

This error indicates that the task can't connect to Amazon ECR. Check the connection to the `repository URI` repository.

For information about how to verify and resolve the issue, see [Verifying Amazon ECS stopped task connectivity](verify-connectivity.md "verify-connectivity.md").

## The task can’t pull the image.

Check your network configuration

This error indicates that the task can't connect to Amazon ECR.

For information about how to verify and resolve the issue, see [Verifying Amazon ECS stopped task connectivity](verify-connectivity.md "verify-connectivity.md").

## CannotPullContainerError: pull image manifest has been retried 5 time(s): failed to resolve ref

This error indicates that the task can't pull the image.

To resolve this, you can:

- Verify that the image specified in the task definition matches the image in
  the repository.
- Amazon ECS forces image version stability. If the original image is no longer available you get
  this error. The image tag is part of enforcing this behavior. Change the image
  in the task definition from using :latest as the tag to a specifc version. For
  more information, see [Container image
  resolution](deployment-type-ecs.md#deployment-container-image-stability "deployment-type-ecs.md#deployment-container-image-stability").

For information about how to verify and resolve the issue, see [Verifying Amazon ECS stopped task connectivity](verify-connectivity.md "verify-connectivity.md").

## API error (500): Get https://111122223333.dkr.ecr.us-east-1.amazonaws.com/v2/: net/http: request canceled while waiting for connection

This error indicates that a connection timed out, because a route to the
internet doesn't exist.

To resolve this issue, you can:

- For tasks in public subnets, specify **ENABLED**
  for **Auto-assign public IP** when launching the
  task. For more information, see [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md").
- For tasks in private subnets, specify
  **DISABLED** for **Auto-assign public
  IP** when launching the task, and configure a NAT
  gateway in your VPC to route requests to the internet. For more
  information, see [NAT
  Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the _Amazon VPC User Guide_.

## API error

This error indicates that there is a connection issue with the Amazon ECR
endpoint.

For information about how to resolve this issue, see [How
can I resolve the Amazon ECR error "CannotPullContainerError: API error" in
Amazon ECS](https://aws.amazon.com/premiumsupport/knowledge-center/ecs-pull-container-api-error-ecr/ "https://aws.amazon.com/premiumsupport/knowledge-center/ecs-pull-container-api-error-ecr/") on the Support website.

## write /var/lib/docker/tmp/`GetImageBlob111111111`: no space left on device

This error indicates that there is insufficient disk space.

To resolve this issue, free up disk space.

If you are using the Amazon ECS-optimized AMI, you can use the following command to
retrieve the 20 largest files on your file system:

```
du -Sh / | sort -rh | head -20
```

Example output:

```
5.7G    /var/lib/docker/containers/50501b5f4cbf90b406e0ca60bf4e6d4ec8f773a6c1d2b451ed8e0195418ad0d2
1.2G    /var/log/ecs
594M    /var/lib/docker/devicemapper/mnt/c8e3010e36ce4c089bf286a623699f5233097ca126ebd5a700af023a5127633d/rootfs/data/logs
...
```

In some cases, the root volume might be filled out by a running container. If
the container is using the default `json-file` log driver without a
`max-size` limit, it may be that the log file is responsible for
most of that space used. You can use the `docker ps` command to
verify which container is using the space by mapping the directory name from the
output above to the container ID. For example:

```
CONTAINER ID   IMAGE                            COMMAND             CREATED             STATUS              PORTS                            NAMES
50501b5f4cbf   amazon/amazon-ecs-agent:latest   "/agent"            4 days ago          Up 4 days                                            ecs-agent
```

By default, when using the `json-file` log driver, Docker
captures the standard output (and standard error) of all of your containers
and writes them in files using the JSON format. You can set the
`max-size` as a log driver option, which prevents the log
file from taking up too much space. For more information, see [JSON File logging driver](https://docs.docker.com/engine/logging/drivers/json-file/ "https://docs.docker.com/engine/logging/drivers/json-file/") in the Docker documentation.

The following is a container definition snippet showing how to use this
option:

```
{
    "log-driver": "json-file",
    "log-opts": {
        "max-size": "`256m`"
    }
}
```

An alternative, if your container logs are taking up too much disk space, is
to use the `awslogs` log driver. The `awslogs` log
driver sends the logs to CloudWatch, which frees up the disk space that would
otherwise be used for your container logs on the container instance. For
more information, see [Send Amazon ECS logs to CloudWatch](using_awslogs.md "using_awslogs.md") .

You might need to update the disk size that Docker can access.

For more information, see [CannotPullContainerError: no space left on device](https://repost.aws/questions/QUx6Ix1R1SSNisYSs1Sw8EBA/cannotpullcontainererror-no-space-left-on-device "https://repost.aws/questions/QUx6Ix1R1SSNisYSs1Sw8EBA/cannotpullcontainererror-no-space-left-on-device").

## ERROR: toomanyrequests: Too Many Requests or You have reached your pull rate limit.

This error indicates that there is a Docker Hub rate limiting.

If you receive one of the following errors, you're likely hitting the
Docker Hub rate limits:

For more information about the Docker Hub rate limits, see [Understanding Docker
Hub rate limiting](https://www.docker.com/increase-rate-limits "https://www.docker.com/increase-rate-limits").

If you have increased the Docker Hub rate limit and you need to
authenticate your Docker pulls for your container instances, see [Private registry authentication for container instances](private-auth-container-instances.md "private-auth-container-instances.md").

## Error response from daemon: Get `url`: net/http:

request canceled while waiting for connection

This error indicates that a connection timed out, because a route to the
internet doesn't exist.

To resolve this issue, you can:

- For tasks in public subnets, specify **ENABLED** for
  **Auto-assign public IP** when launching the task.
  For more information, see [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md").
- For tasks in private subnets, specify **DISABLED**
  for **Auto-assign public IP** when launching the task,
  and configure a NAT gateway in your VPC to route requests to the
  internet. For more information, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
  _Amazon VPC User Guide_.

## ref pull has been retried 1 time(s): failed to copy: httpReaderSeeker: failed open: unexpected status code

This error indicates that there was a failure when copying an image.

To resolve this issue, review one of the following articles:

- For Fargate tasks, see [How do I resolve the "cannotpullcontainererror" error for my
  Amazon ECS tasks on Fargate](https://aws.amazon.com/premiumsupport/knowledge-center/ecs-fargate-pull-container-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/ecs-fargate-pull-container-error/").
- For other tasks, see [How do I resolve the "cannotpullcontainererror" error for my
  Amazon ECS tasks](https://aws.amazon.com/premiumsupport/knowledge-center/ecs-pull-container-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/ecs-pull-container-error/").

## pull access denied

This error indicates that there is no access to the image.

To resolve this issue, you might need to authenticate your Docker client with
Amazon ECR For more information, see [Private registry
authentication](../../../AmazonECR/latest/userguide/registry_auth.md "../../../AmazonECR/latest/userguide/registry_auth.md") in the _Amazon ECR User
Guide_.

## pull command failed: panic: runtime error: invalid memory address or nil pointer dereference

This error indicates that there is no access to the image because of an
invalid memory address or nil pointer dereference.

To resolve this issue:

- Check that you have the security group rules to reach Amazon S3.
- When you use gateway endpoints, you must add a route in the route
  table to access the endpoint.

## error pulling image conf/error pulling image configuration

This error indicates a rate limit has been reached or there is a network error:

To resolve this issue, see [How can
I resolve the "CannotPullContainerError" error in my Amazon ECS EC2 Launch Type
Task](https://repost.aws/knowledge-center/ecs-pull-container-error "https://repost.aws/knowledge-center/ecs-pull-container-error").

## Context canceled

This error indicates that the context was cancelled.

The common cause for this error is because the VPC your task is using
doesn't have a route to pull the container image from Amazon ECR.
