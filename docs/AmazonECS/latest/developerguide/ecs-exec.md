# Monitor Amazon ECS containers with ECS Exec

With Amazon ECS Exec, you can directly interact with containers without needing to first
interact with the host container operating system, open inbound ports, or manage SSH keys.
You can use ECS Exec to run commands in or get a shell to a container running on an Amazon EC2
instance or on AWS Fargate. This makes it easier to collect diagnostic information and
quickly troubleshoot errors. For example, in a development context, you can use ECS Exec to
easily interact with various process in your containers and troubleshoot your applications.
And in production scenarios, you can use it to gain break-glass access to your containers to
debug issues.

You can run commands in a running Linux or Windows container using ECS Exec from the Amazon ECS
API, AWS Command Line Interface (AWS CLI), AWS SDKs, or the AWS Copilot CLI. For details on using ECS Exec, as well
as a video walkthrough, using the AWS Copilot CLI, see the [Copilot
GitHub documentation](https://aws.github.io/copilot-cli/docs/commands/svc-exec/ "https://aws.github.io/copilot-cli/docs/commands/svc-exec/").

You can also use ECS Exec to maintain stricter access control policies. By selectively
turning on this feature, you can control who can run commands and on which tasks they can
run those commands. With a log of each command and their output, you can use ECS Exec to view
which tasks were run and you can use CloudTrail to audit who accessed a container.

## Considerations

Consider the following when using ECS Exec:

- ECS Exec might not work as expected when running on operating systems not
  supported by Systems Manager. For information about the supported operating systems, see
  [Operating system types](../../../systems-manager/latest/userguide/operating-systems-and-machine-types.md#prereqs-os-linux "../../../systems-manager/latest/userguide/operating-systems-and-machine-types.md#prereqs-os-linux") in the _AWS Systems Manager
  User Guide_.
- ECS Exec is supported for tasks that run on the following infrastructure:
  - Linux containers on Amazon EC2 on any Amazon ECS-optimized AMI, including
    Bottlerocket
  - Linux and Windows containers on external instances (Amazon ECS
    Anywhere)
  - Linux and Windows containers on AWS Fargate
  - Windows containers on Amazon EC2 on the following Windows Amazon ECS-optimized
    AMIs (with the container agent version `1.56` or
    later):
    - Amazon ECS-optimized Windows Server 2022 Full AMI
    - Amazon ECS-optimized Windows Server 2022 Core AMI
    - Amazon ECS-optimized Windows Server 2019 Full AMI
    - Amazon ECS-optimized Windows Server 2019 Core AMI
    - Amazon ECS-optimized Windows Server 20H2 Core AMI

- If you configured an HTTP proxy for your task, set the `NO_PROXY`
  environment variable to `"NO_PROXY=169.254.169.254,169.254.170.2"` in
  order to bypass the proxy for EC2 instance metadata and IAM role traffic. If
  you don't configure the `NO_PROXY` environment variable, there can be
  failures when retrieving instance metadata or IAM role credentials from the
  metadata endpoint within the container. Setting the `NO_PROXY`
  environment variable as recommended filters the metadata and IAM traffic so
  that requests to `169.254.169.254 and 169.254.170.2` do not go
  through the `HTTP` proxy.
- ECS Exec and Amazon VPC
  - If you are using interface Amazon VPC endpoints with Amazon ECS, you must create
    the interface Amazon VPC endpoints for the Systems Manager Session Manager
    (`ssmmessages`). For more information about Systems Manager VPC
    endpoints, see [Use AWS PrivateLink to set up a VPC endpoint for Session
    Manager](../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md "../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md") in the _AWS Systems Manager User Guide_.
  - If you are using interface Amazon VPC endpoints with Amazon ECS, and you are
    using AWS KMS key for encryption, then you must create the interface
    Amazon VPC endpoint for AWS KMS key. For more information, see [Connecting to
    AWS KMS key through a VPC endpoint](../../../kms/latest/developerguide/kms-vpc-endpoint.md "../../../kms/latest/developerguide/kms-vpc-endpoint.md") in the _AWS Key Management Service Developer Guide_.
  - When you have tasks that run on Amazon EC2 instances, use
    `awsvpc` networking mode. If you don't have internet
    access (such as not configured to use a NAT gateway), you must create
    the interface Amazon VPC endpoints for the Systems Manager Session Manager
    (`ssmmessages`). For more information about
    `awsvpc` network mode considerations, see [Considerations](task-networking-awsvpc.md#linux "task-networking-awsvpc.md#linux"). For more information about Systems Manager VPC
    endpoints, see [Use AWS PrivateLink to set up a VPC endpoint for Session
    Manager](../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md "../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md") in the _AWS Systems Manager User Guide_.

- Amazon ECS Exec isn't supported for tasks running in an IPv6-only configuration.
  For more information about running tasks in an IPv6-only configuration, see
  [Amazon ECS task networking options for Fargate](fargate-task-networking.md "fargate-task-networking.md") and [Amazon ECS task networking options for EC2](task-networking.md "task-networking.md").
- ECS Exec and SSM
  - When a user runs commands on a container using ECS Exec, these commands
    are run as the `root` user. The SSM agent and its child
    processes run as root even when you specify a user ID for the
    container.
  - The SSM agent requires that the container file system can be written
    to in order to create the required directories and files. Therefore,
    making the root file system read-only using the
    `readonlyRootFilesystem` task definition parameter, or
    any other method, isn't supported.
  - While starting SSM sessions outside of the
    `execute-command` action is possible, this results in the
    sessions not being logged and being counted against the session limit.
    We recommend limiting this access by denying the
    `ssm:start-session` action using an IAM policy. For
    more information, see [Limiting access to the Start Session action](#ecs-exec-limit-access-start-session "#ecs-exec-limit-access-start-session").

- The following features run as a sidecar container. Therefore, you must specify
  the container name to run the command on.
  - Runtime Monitoring
  - Service Connect

- Users can run all of the commands that are available within the container
  context. The following actions might result in orphaned and zombie processes:
  terminating the main process of the container, terminating the command agent,
  and deleting dependencies. To cleanup zombie processes, we recommend adding the
  `initProcessEnabled` flag to your task definition.
- ECS Exec uses some CPU and memory. You'll want to accommodate for that when
  specifying the CPU and memory resource allocations in your task
  definition.
- You must be using AWS CLI version `1.22.3` or later or AWS CLI version
  `2.3.6` or later. For information about how to update the AWS CLI,
  see [Installing or
  updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide Version 2_.
- You can have only one ECS Exec session per process ID (PID) namespace. If you
  are [sharing a PID namespace in a task](task_definition_parameters.md#other_task_definition_params "task_definition_parameters.md#other_task_definition_params"), you can only start ECS Exec
  sessions into one container.
- The ECS Exec session has an idle timeout time of 20 minutes. This value can't be
  changed.
- You can't turn on ECS Exec for existing tasks. It can only be turned on for new
  tasks.
- You can't use ECS Exec when you use `run-task` to launch a task on a
  cluster that uses managed scaling with asynchronous placement (launch a task
  with no instance).
- You can't run ECS Exec against Microsoft Nano Server containers.

## Architecture

ECS Exec makes use of AWS Systems Manager (SSM) Session Manager to establish a connection with
the running container and uses AWS Identity and Access Management (IAM) policies to control access to running
commands in a running container. This is made possible by bind-mounting the necessary
SSM agent binaries into the container. The Amazon ECS or AWS Fargate agent is responsible
for starting the SSM core agent inside the container alongside your application code.
For more information, see [Systems Manager Session
Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md").

You can audit which user accessed the container using the `ExecuteCommand`
event in AWS CloudTrail and log each command (and their output) to Amazon S3 or Amazon CloudWatch Logs. To
encrypt data between the local client and container with your own encryption key, you
must provide the AWS Key Management Service (AWS KMS) key.

## Configuring ECS Exec

To use ECS Exec, you must first turn on the feature for your tasks and services, and then you can run commands in your containers.

### Optional task definition changes

If you set the task definition parameter `initProcessEnabled` to
`true`, this starts the init process inside the container. This
removes any zombie SSM agent child processes found. The following provides an
example.

```
`{
 "taskRoleArn": "`ecsTaskRole`",
 "networkMode": "awsvpc",
 "requiresCompatibilities": [
 "EC2",
 "FARGATE"
 ],
 "executionRoleArn": "`ecsTaskExecutionRole`",
 "memory": ".5 gb",
 "cpu": ".25 vcpu",
 "containerDefinitions": [
 {
 "name": "amazon-linux",
 "image": "amazonlinux:latest",
 "essential": true,
 "command": ["sleep","3600"],
 "linuxParameters": {
 **"initProcessEnabled": `true`**
 }
 }
 ],
 "family": "`ecs-exec-task`"
}`
```

### Turning on ECS Exec for your tasks and services

You can turn on the ECS Exec feature for your services and standalone tasks by
specifying the `--enable-execute-command` flag when using one of the
following AWS CLI commands: [`create-service`](../../../cli/latest/reference/ecs/create-service.md "../../../cli/latest/reference/ecs/create-service.md"), [`update-service`](../../../cli/latest/reference/ecs/update-service.md "../../../cli/latest/reference/ecs/update-service.md"), [`start-task`](../../../cli/latest/reference/ecs/start-task.md "../../../cli/latest/reference/ecs/start-task.md"),
or [`run-task`](../../../cli/latest/reference/ecs/run-task.md "../../../cli/latest/reference/ecs/run-task.md").

For example, if you run the following command, the ECS Exec feature is turned on for
a newly created service that runs on Fargate. For more information about creating
services, see [create-service](../../../cli/latest/reference/ecs/create-service.md "../../../cli/latest/reference/ecs/create-service.md").

```
`aws ecs create-service \
 --cluster `cluster-name` \
 --task-definition `task-definition-name` \
 --enable-execute-command \
 --service-name `service-name` \
 --launch-type FARGATE \
 --network-configuration "awsvpcConfiguration={subnets=[subnet-12344321],securityGroups=[sg-12344321],assignPublicIp=ENABLED}" \
 --desired-count 1`
```

After you turn on ECS Exec for a task, you can run the following command to confirm
the task is ready to be used. If the `lastStatus` property of the
`ExecuteCommandAgent` is listed as `RUNNING` and the
`enableExecuteCommand` property is set to `true`, then
your task is ready.

```
`aws ecs describe-tasks \
 --cluster `cluster-name` \
 --tasks `task-id``
```

The following output snippet is an example of what you might see.

```
{
    "tasks": [
        {
            ...
            "containers": [
                {
                    ...
                    "managedAgents": [
                        {
                            "lastStartedAt": "2021-03-01T14:49:44.574000-06:00",
                            "name": "ExecuteCommandAgent",
                            "lastStatus": "RUNNING"
                        }
                    ]
                }
            ],
            ...
            "enableExecuteCommand": true,
            ...
        }
    ]
}
```

### Running commands using ECS Exec

## Logging using ECS Exec

You can configure logging for ECS Exec sessions to capture commands and their output for auditing and troubleshooting purposes.

### Turning on logging in your tasks and services

###### Important

For more information about CloudWatch pricing, see [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). Amazon ECS
also provides monitoring metrics that are provided at no additional cost. For
more information, see [Monitor Amazon ECS using CloudWatch](cloudwatch-metrics.md "cloudwatch-metrics.md").

Amazon ECS provides a default configuration for logging commands run using ECS Exec. The
default is to send logs to CloudWatch Logs using the `awslogs` log driver that's
configured in your task definition. If you want to provide a custom configuration,
the AWS CLI supports a `--configuration` flag for both the
`create-cluster` and `update-cluster` commands. The
container image requires `script` and `cat` to be installed in
order to have command logs uploaded correctly to Amazon S3 or CloudWatch Logs. For more information
about creating clusters, see [create-cluster](../../../cli/latest/reference/ecs/create-cluster.md "../../../cli/latest/reference/ecs/create-cluster.md").

###### Note

This configuration only handles the logging of the
`execute-command` session. It doesn't affect logging of your
application.

The following example creates a cluster and then logs the output to your CloudWatch Logs
LogGroup named `cloudwatch-log-group-name` and your Amazon S3 bucket named
`s3-bucket-name`.

You must use an AWS KMS customer managed key to encrypt the log group when you set the
`CloudWatchEncryptionEnabled` option to `true`. For
information about how to encrypt the log group, see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md#encrypt-log-data-kms-policy "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md#encrypt-log-data-kms-policy"), in the
_Amazon CloudWatch Logs User
Guide_.

```
`aws ecs create-cluster \
 --cluster-name `cluster-name` \
 --configuration executeCommandConfiguration="{ \
 kmsKeyId=`string`, \
 logging=`OVERRIDE`, \
 logConfiguration={ \
 cloudWatchLogGroupName=`cloudwatch-log-group-name`, \
 cloudWatchEncryptionEnabled=`true`, \
 s3BucketName=`s3-bucket-name`, \
 s3EncryptionEnabled=`true`, \
 s3KeyPrefix=`demo` \
 } \
 }"`
```

The `logging` property determines the behavior of the logging
capability of ECS Exec:

- `NONE`: logging is turned off.
- `DEFAULT`: logs are sent to the configured `awslogs`
  driver. If the driver isn't configured, then no log is saved.
- `OVERRIDE`: logs are sent to the provided Amazon CloudWatch Logs LogGroup,
  Amazon S3 bucket, or both.

### IAM permissions required for Amazon CloudWatch Logs or Amazon S3 Logging

To enable logging, the Amazon ECS task role that's referenced in your task definition
needs to have additional permissions. These additional permissions can be added as a
policy to the task role. They're different depending on if you direct your logs to
Amazon CloudWatch Logs or Amazon S3.

Amazon CloudWatch Logs
The following example policy adds the required Amazon CloudWatch Logs
permissions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:us-east-1:111122223333:log-group:/aws/ecs/`cloudwatch-log-group-name`:*"
 }
 ]
}`

```

Amazon S3
The following example policy adds the required Amazon S3
permissions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": "arn:aws:s3:::`s3-bucket-name`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`s3-bucket-name`/*"
 }
 ]
 }`

```

### IAM permissions required for encryption using your own AWS KMS key (KMS key)

By default, the data transferred between your local client and the container uses
TLS 1.2 encryption that AWS provides. To further encrypt data using your own
KMS key, you must create a KMS key and add the `kms:Decrypt`
permission to your task IAM role. This permission is used by your container to
decrypt the data. For more information about creating a KMS key, see [Creating
keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").

You add the following inline policy to your task IAM role which requires the AWS KMS
permissions. For more information, see [ECS Exec permissions](task-iam-roles.md#ecs-exec-required-iam-permissions "task-iam-roles.md#ecs-exec-required-iam-permissions").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 }
 ]
}`

```

For the data to be encrypted using your own KMS key, the user or group using the
`execute-command` action must be granted the
`kms:GenerateDataKey` permission.

The following example policy for your user or group contains the required
permission to use your own KMS key. You must specify the Amazon Resource Name (ARN) of your
KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 }
 ]
}`

```

## Using IAM policies to limit access to ECS Exec

You limit user access to the execute-command API action by using one or more of the
following IAM policy condition keys:

- `aws:ResourceTag/`clusterTagKey``
- `ecs:ResourceTag/`clusterTagKey``
- `aws:ResourceTag/`taskTagKey``
- `ecs:ResourceTag/`taskTagKey``
- `ecs:container-name`
- `ecs:cluster`
- `ecs:task`
- `ecs:enable-execute-command`

With the following example IAM policy, users can run commands in containers that are
running within tasks with a tag that has an `environment` key and
`development` value and in a cluster that's named
`cluster-name`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:ExecuteCommand",
 "ecs:DescribeTasks"
 ],
 "Resource": [
 "arn:aws:ecs:us-east-1:`111122223333`:task/`cluster-name`/*",
 "arn:aws:ecs:us-east-1:`111122223333`:cluster/`cluster-name`"
 ],
 "Condition": {
 "StringEquals": {
 "ecs:ResourceTag/environment": "development"
 }
 }
 }
 ]
}`

```

With the following IAM policy example, users can't use the
`execute-command` API when the container name is
`production-app`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "`Deny`",
 "Action": [
 "ecs:ExecuteCommand"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ecs:container-name": "`production-app`"
 }
 }
 }
 ]
}`

```

With the following IAM policy, users can only launch tasks when ECS Exec is turned
off.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "`Allow`",
 "Action": [
 "ecs:RunTask",
 "ecs:StartTask",
 "ecs:CreateService",
 "ecs:UpdateService"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ecs:enable-execute-command": "`false`"
 }
 }
 }
 ]
}`

```

###### Note

Because the `execute-command` API action contains only task and cluster
resources in a request, only cluster and task tags are evaluated.

For more information about IAM policy condition keys, see [Actions, resources, and condition keys for Amazon Elastic Container Service](../../../service-authorization/latest/reference/list_amazonelasticcontainerservice.md "../../../service-authorization/latest/reference/list_amazonelasticcontainerservice.md")
in the _Service Authorization Reference_.

### Limiting access to the Start Session action

While starting SSM sessions on your container outside of ECS Exec is possible,
this could potentially result in the sessions not being logged. Sessions started
outside of ECS Exec also count against the session quota. We recommend limiting this
access by denying the `ssm:start-session` action directly for your Amazon ECS
tasks using an IAM policy. You can deny access to all Amazon ECS tasks or to specific
tasks based on the tags used.

The following is an example IAM policy that denies access to the
`ssm:start-session` action for tasks in all Regions with a specified
cluster name. You can optionally include a wildcard with the
`cluster-name`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ssm:StartSession",
 "Resource": [
 "arn:aws:ecs:us-east-1:`111122223333`:task/`cluster-name`/*"
 ]
 }
 ]
}`

```

The following is an example IAM policy that denies access to the
`ssm:start-session` action on resources in all Regions tagged with
tag key `Task-Tag-Key` and tag value `Exec-Task`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ssm:StartSession",
 "Resource": "arn:aws:ecs:*:*:task/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`Task-Tag-Key`": "`Exec-Task`"
 }
 }
 }
 ]
}`

```

## Troubleshooting ECS Exec

For additional troubleshooting help, see [Troubleshooting issues with
Exec](ecs-exec-troubleshooting.md "ecs-exec-troubleshooting.md").
