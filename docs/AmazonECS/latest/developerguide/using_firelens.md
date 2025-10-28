# Send Amazon ECS logs to an AWS service or AWS Partner

You can use FireLens for Amazon ECS to use task definition parameters to route logs to an AWS
service or AWS Partner Network (APN) destination for log storage and analytics. The AWS Partner Network is a
global community of partners that leverages programs, expertise, and resources to build,
market, and sell customer offerings. For more information see [AWS Partner](https://aws.amazon.com/partners/work-with-partners/ "https://aws.amazon.com/partners/work-with-partners/"). FireLens works with
Fluentd and
Fluent Bit. We provide the
AWS for Fluent Bit image or you can use your own Fluentd or
Fluent Bit image.

By default, Amazon ECS configures the container dependency so that the Firelens container
starts before any container that uses it. The Firelens container also stops after all
containers that use it stop.

To use this feature, you must create an IAM role for your tasks that provides the
permissions necessary to use any AWS services that the tasks require. For example, if a
container is routing logs to Firehose, the task requires permission to call the
`firehose:PutRecordBatch` API. For more information, see [Adding and Removing
IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

Your task might also require the Amazon ECS task execution role under the following conditions.
For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

- If your task is hosted on Fargate and you are pulling container
  images from Amazon ECR or referencing sensitive data from AWS Secrets Manager in your log
  configuration, then you must include the task execution IAM role.
- When you use a custom configuration file that's hosted in Amazon S3, your task
  execution IAM role must include the `s3:GetObject` permission.
  Consider the following when using FireLens for Amazon ECS:

- We recommend that you add `my_service_` to the log container name so
  that you can easily distinguish container names in the console.
- Amazon ECS adds a start container order dependency between the application containers
  and the FireLens container by default. When you specify a container
  order between the application containers and the FireLens container,
  then the default start container order is overridden.
- FireLens for Amazon ECS is supported for tasks that are hosted on both
  AWS Fargate on Linux and Amazon EC2 on Linux. Windows containers don't support
  FireLens.

For information about how to configure centralized logging for Windows containers,
see [Centralized logging for Windows containers on Amazon ECS using Fluent
Bit](https://aws.amazon.com/blogs/containers/centralized-logging-for-windows-containers-on-amazon-ecs-using-fluent-bit/ "https://aws.amazon.com/blogs/containers/centralized-logging-for-windows-containers-on-amazon-ecs-using-fluent-bit/").

- You can use AWS CloudFormation templates to configure FireLens for Amazon ECS. For
  more information, see [AWS::ECS::TaskDefinition FirelensConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.md") in the
  _AWS CloudFormation User Guide_
- FireLens listens on port `24224`, so to ensure that the
  FireLens log router isn't reachable outside of the task, you must not allow inbound
  traffic on port `24224` in the security group your task uses. For tasks
  that use the `awsvpc` network mode, this is the security group associated
  with the task. For tasks using the `host` network mode, this is the
  security group that's associated with the Amazon EC2 instance hosting the task. For tasks
  that use the `bridge` network mode, don't create any port mappings that
  use port `24224`.
- For tasks that use the `bridge` network mode, the container with the
  FireLens configuration must start before any application containers that rely on it
  start. To control the start order of your containers, use dependency conditions in
  your task definition. For more information, see [Container dependency](task_definition_parameters.md#container_definition_dependson "task_definition_parameters.md#container_definition_dependson").

###### Note

If you use dependency condition parameters in container definitions with a
FireLens configuration, ensure that each container has a `START` or
`HEALTHY` condition requirement.

- By default, FireLens adds the cluster and task definition name and
  the Amazon Resource Name (ARN) of the cluster as metadata keys to your stdout/stderr container logs.
  The following is an example of the metadata format.

```
"ecs_cluster": "`cluster-name`",
"ecs_task_arn": "arn:aws:ecs:`region`:`111122223333`:task/`cluster-name`/`f2ad7dba413f45ddb4EXAMPLE`",
"ecs_task_definition": "task-def-name:revision",
```

If you do not want the metadata in your logs, set
`enable-ecs-log-metadata` to `false` in the
`firelensConfiguration` section of the task definition.

```
"firelensConfiguration":{
   "type":"fluentbit",
   "options":{
      **"enable-ecs-log-metadata":"false"**,
      "config-file-type":"file",
      "config-file-value":"/extra.conf"
}
```

You can configure the FireLens container to run as a non-root user.
Consider the following:

- To configure the FireLens container to run as a non-root user, you
  must specify the user in one of the following formats:

      + `uid`
      + `uid:gid`
      + `uid:group`

  For more information about specifying a user in a container definition, see [ContainerDefinition](../APIReference/API_ContainerDefinition.md "../APIReference/API_ContainerDefinition.md") in the _Amazon Elastic Container Service API Reference_.

The FireLens container receives application logs over a
UNIX socket. The Amazon ECS agent uses the `uid` to assign
ownership of the socket directory to the FireLens container.

- Configuring the FireLens container to run as a non-root user is
  supported on Amazon ECS Agent version `1.96.0` and later, and Amazon ECS-optimized
  AMI version `v20250716` and later.
- When you specify a user for the FireLens container, the
  `uid` must be unique and not used for other processes belonging to
  other containers in the task or the container instance.
  For information about how to use multiple configuration files with Amazon ECS, including files
  that you host or files in Amazon S3, see [Init process for Fluent Bit on ECS, multi-config support](https://github.com/aws/aws-for-fluent-bit/tree/mainline/use_cases/init-process-for-fluent-bit "https://github.com/aws/aws-for-fluent-bit/tree/mainline/use_cases/init-process-for-fluent-bit").

For information about example configurations, see [Example Amazon ECS task definition: Route logs to FireLens](firelens-taskdef.md "firelens-taskdef.md").

For more information about configuring logs for high throughput, see [Configuring Amazon ECS logs for high
throughput](firelens-docker-buffer-limit.md "firelens-docker-buffer-limit.md").
