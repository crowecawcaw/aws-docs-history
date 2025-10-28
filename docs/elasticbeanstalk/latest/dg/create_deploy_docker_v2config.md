# Configuring the Dockerrun.aws.json v2 file

`Dockerrun.aws.json v2` is an Elastic Beanstalk configuration file that describes how to deploy a set of Docker containers hosted in an ECS cluster in an
Elastic Beanstalk environment. The Elastic Beanstalk platform creates an ECS _task definition_, which includes an ECS _container
definition_. These definitions are described in the `Dockerrun.aws.json` configuration file.

The container definition in the `Dockerrun.aws.json` file describes the containers to deploy to each Amazon EC2 instance in the ECS cluster. In
this case an Amazon EC2 instance is also referred to as a host _container instance_, because it hosts the Docker containers. The
configuration file also describes the data volumes to create on the host container instance for the Docker containers to mount. For more information and a
diagram of the components in an ECS managed Docker environment on Elastic Beanstalk, see the [ECS managed Docker platform overview](create_deploy_docker_ecs.md#create_deploy_docker_ecs_platform "create_deploy_docker_ecs.md#create_deploy_docker_ecs_platform") earlier in this chapter.

A `Dockerrun.aws.json` file can be used on its own or zipped up with additional source code in a single archive. Source code that is
archived with a `Dockerrun.aws.json` is deployed to Amazon EC2 container instances and accessible in the `/var/app/current/`
directory.

###### Topics

- [Dockerrun.aws.json v2](#create_deploy_docker_v2config_dockerrun "#create_deploy_docker_v2config_dockerrun")
- [Volume format](#create_deploy_docker_v2config_volume_format "#create_deploy_docker_v2config_volume_format")
- [Execution Role ARN format](#create_deploy_docker_v2config_executionRoleArn_format "#create_deploy_docker_v2config_executionRoleArn_format")
- [Container definition format](#create_deploy_docker_v2config_dockerrun_format "#create_deploy_docker_v2config_dockerrun_format")
- [Authentication format – using images from a private repository](#docker-multicontainer-dockerrun-privaterepo "#docker-multicontainer-dockerrun-privaterepo")
- [Example Dockerrun.aws.json v2](#create_deploy_docker_v2config_example "#create_deploy_docker_v2config_example")

## `Dockerrun.aws.json` v2

The `Dockerrun.aws.json` file includes the following sections:

**AWSEBDockerrunVersion**

Specifies the version number as the value `2` for ECS managed Docker environments.

**executionRoleArn**

Specifies the task execution IAM roles for different purposes and services associated with your account. For your application to use Elastic Beanstalk
[environment variables stored as secrets](AWSHowTo.secrets.md "AWSHowTo.secrets.md"), you’ll need to specify the ARN of a task execution
role that grants the required permissions. Other common use cases may also require this parameter. For more information, see [Execution Role ARN format](#create_deploy_docker_v2config_executionRoleArn_format "#create_deploy_docker_v2config_executionRoleArn_format").

**volumes**

Creates volumes from folders in the Amazon EC2 container instance, or from your source bundle (deployed to `/var/app/current`).
Mount these volumes to paths within your Docker containers using `mountPoints` in the `containerDefinitions` section.

**containerDefinitions**

An array of container definitions.

**authentication (optional)**

The location in Amazon S3 of a `.dockercfg` file that contains authentication data for a private repository.

The _containerDefinitions_ and _volumes_ sections of `Dockerrun.aws.json` use the same formatting as
the corresponding sections of an Amazon ECS task definition file. For more information about the task definition format and a full list of task definition
parameters, see [Amazon ECS task definitions](../../../AmazonECS/latest/developerguide/task_defintions.md "../../../AmazonECS/latest/developerguide/task_defintions.md") in the
_Amazon Elastic Container Service Developer Guide_.

## Volume format

The _volume_ parameter creates volumes from either folders in the Amazon EC2 container instance, or from your source bundle (deployed
to `/var/app/current`).

Volumes are specified in the following format:

```
"volumes": [
    {
      "name": "`volumename`",
      "host": {
        "sourcePath": "`/path/on/host/instance`"
      }
    }
  ],
```

Mount these volumes to paths within your Docker containers using `mountPoints` in the container definition.

Elastic Beanstalk configures additional volumes for logs, one for each container. These should be mounted by your Docker containers in order to write logs to
the host instance.

For more details, see the `mountPoints` field in the _Container definition format_ section that
follows.

## Execution Role ARN format

In order for your application to use Elastic Beanstalk [environment variables stored as secrets](AWSHowTo.secrets.md "AWSHowTo.secrets.md"), you'll need to
specify a task execution IAM role. The role must grant the Amazon ECS container permission to make AWS API calls on your behalf using AWS Secrets Manager secrets
or AWS Systems Manager Parameter Store parameters to reference sensitive data. For instructions to create a task execution IAM role with the required
permissions for your account, see [Amazon ECS task execution
IAM role](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the Amazon Elastic Container Service Developer Guide.

```
{
"AWSEBDockerrunVersion": 2,
  "executionRoleArn": "`arn:aws:iam::`111122223333`:role/`ecsTaskExecutionRole``",
```

### Additional permissions required for the Amazon ECS managed Docker platform

###### EC2 instance profile grants `iam:PassRole` to ECS

In order for your EC2 instance profile to be able to grant this role to the ECS container, you must include the `iam:PassRole`
permission demonstrated in the following example. The `iam:PassRole` allows the EC2 instances permission _to pass_
the task execution role to the ECS container.

In this example, we limit the EC2 instance to only pass the role to the ECS service. Although this condition is not required, we add it to follow
best practices to reduce the scope of the permission shared. We accomplish this with the `Condition` element.

###### Note

Any usage of the ECS IAM task execution role requires the `iam:PassRole` permission. There are other common use cases
that require the ECS task execution managed service role. For more information, see [Amazon ECS task execution IAM role](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the Amazon Elastic Container Service Developer Guide.

###### Example policy with `iam:PassRole` permission

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "`iam:PassRole`",
 "Resource": [
 "`arn:aws:iam::123456789012:role/ecs-task-execution-role`"
 ],
 "Condition": {
 "StringLike": {
 "`iam:PassedToService`": "`ecs-tasks.amazonaws.com`"
 }
 }
 }
 ]
}`

```

###### Granting secrets and parameters access to the Amazon ECS container agent

The Amazon ECS task execution IAM role also needs permissions to access the secrets and parameter stores. Similar to the requirements of the EC2
instance profile role, the ECS container agent requires permission to pull the necessary Secrets Manager or Systems Manager resources. For more information, see [Secrets Manager or Systems Manager permissions](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md#task-execution-secrets "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md#task-execution-secrets") in the
_Amazon Elastic Container Service Developer Guide_

###### Granting secrets and parameters access to the Elastic Beanstalk EC2 instances

To support secrets configured as environment variables, you'll also need to add permissions to your EC2 instance profile. For more information,
see [Fetching secrets and parameters to Elastic Beanstalk environment variables](AWSHowTo.secrets.md "AWSHowTo.secrets.md") and [Required IAM permissions for Secrets Manager](AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager "AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager").

The following examples combine the previous `iam:PassRole` example with the examples provided in the referenced [Required IAM permissions for Secrets Manager](AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager "AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager"). They add the
permissions that the EC2 instances require to access the AWS Secrets Manager and AWS Systems Manager stores to retrieve the secrets and parameter data to initialize the
Elastic Beanstalk environment variables that have been configured for secrets.

###### Example Secrets Manager policy combined with `iam:PassRole` permission

JSON

```
`{
 "Version": "`2012-10-17`",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "`iam:PassRole`",
 "Resource": [
 "`arn:aws:iam::123456789012:role/ecs-task-execution-role`"
 ],
 "Condition": {
 "StringLike": {
 "`iam:PassedToService`": "`ecs-tasks.amazonaws.com`"
 }
 }
 },
 {
 "Effect": "`Allow`",
 "Action": [
 "`secretsmanager:GetSecretValue`",
 "`kms:Decrypt`"
 ],
 "Resource": [
 "`arn:aws:secretsmanager:us-east-1:`111122223333`:secret:my-secret`",
 "`arn:aws:kms:us-east-1:`111122223333`:key/my-key`"
 ]
 }
 ]
}`

```

###### Example Systems Manager policy combined with `iam:PassRole` permission

JSON

```
`{
 "Version": "`2012-10-17`",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "`iam:PassRole`",
 "Resource": [
 "`arn:aws:iam::123456789012:role/ecs-task-execution-role`"
 ],
 "Condition": {
 "StringLike": {
 "`iam:PassedToService`": "`ecs-tasks.amazonaws.com`"
 }
 }
 },
 {
 "Effect": "`Allow`",
 "Action": [
 "`ssm:GetParameter`",
 "`kms:Decrypt`"
 ],
 "Resource": [
 "`arn:aws:ssm:us-east-1:`111122223333`:parameter/my-parameter`",
 "`arn:aws:kms:us-east-1:`111122223333`:key/my-key`"
 ]
 }
 ]
}`

```

## Container definition format

The following examples show a subset of parameters that are commonly used in the _containerDefinitions_ section. More optional
parameters are available.

The Beanstalk platform creates an ECS _task definition_, which includes an ECS _container definition_.
Beanstalk supports a sub-set of parameters for the ECS container definition. For more information, see [Container definitions](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definitions "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definitions") in the
_Amazon Elastic Container Service Developer Guide_.

A `Dockerrun.aws.json` file contains an array of one or more container definition objects with the following fields:

**name**

The name of the container. See [Standard
Container Definition Parameters](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#standard_container_definition_params "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#standard_container_definition_params") for information about the maximum length and allowed characters.

**image**

The name of a Docker image in an online Docker repository from which you're building a Docker container. Note these conventions:

- Images in official repositories on Docker Hub use a single name (for example, `ubuntu` or
  `mongo`).
- Images in other repositories on Docker Hub are qualified with an organization name (for example,
  `amazon/amazon-ecs-agent`.
- Images in other online repositories are qualified further by a domain name (for example,
  `quay.io/assemblyline/ubuntu`).

**environment**

An array of environment variables to pass to the container.

For example, the following entry defines an environment variable with the name `Container` and the value
`PHP`:

```
"environment": [
  {
    "name": "Container",
    "value": "PHP"
  }
],
```

**essential**

True if the task should stop if the container fails. Nonessential containers can finish or crash without affecting the rest of the containers
on the instance.

**memory**

Amount of memory on the container instance to reserve for the container. Specify a non-zero integer for one or both of the `memory`
or `memoryReservation` parameters in container definitions.

**memoryReservation**

The soft limit (in MiB) of memory to reserve for the container. Specify a non-zero integer for one or both of the `memory` or
`memoryReservation` parameters in container definitions.

**mountPoints**

Volumes from the Amazon EC2 container instance to mount, and the location on the Docker container file system at which to mount them. When you
mount volumes that contain application content, your container can read the data you upload in your source bundle. When you mount log volumes for
writing log data, Elastic Beanstalk can gather log data from these volumes.

Elastic Beanstalk creates log volumes on the container instance, one for each Docker container, at
`/var/log/containers/`containername``. These volumes are named
 `awseb-logs-`containername`` and should be mounted to the location within the container file
structure where logs are written.

For example, the following mount point maps the nginx log location in the container to the Elastic Beanstalk–generated volume for the
`nginx-proxy` container.

```
{
  "sourceVolume": "awseb-logs-nginx-proxy",
  "containerPath": "/var/log/nginx"
}
```

**portMappings**

Maps network ports on the container to ports on the host.

**links**

List of containers to link to. Linked containers can discover each other and communicate securely.

**volumesFrom**

Mount all of the volumes from a different container. For example, to mount volumes from a container named `web`:

```
"volumesFrom": [
  {
    "sourceContainer": "web"
  }
],
```

## Authentication format – using images from a private repository

The `authentication` section contains authentication data for a private repository. This entry is optional.

Add the information about the Amazon S3 bucket that contains the authentication file in the `authentication` parameter of the
`Dockerrun.aws.json` file. Make sure that the `authentication` parameter contains a valid Amazon S3 bucket and key. The Amazon S3
bucket must be hosted in the same region as the environment that is using it. Elastic Beanstalk will not download files from Amazon S3 buckets hosted in other
regions.

Uses the following format:

```
"authentication": {
    "bucket": "`amzn-s3-demo-bucket`",
    "key": "`mydockercfg`"
  },
```

For information about generating and uploading the authentication file, see [Authenticating with image repositories](docker-configuration.md "docker-configuration.md").

## Example Dockerrun.aws.json v2

The following snippet is an example that illustrates the syntax of the `Dockerrun.aws.json` file for an instance with two
containers.

```
{
  "AWSEBDockerrunVersion": 2,
  "volumes": [
    {
      "name": "php-app",
      "host": {
        "sourcePath": "/var/app/current/php-app"
      }
    },
    {
      "name": "nginx-proxy-conf",
      "host": {
        "sourcePath": "/var/app/current/proxy/conf.d"
      }
    }
  ],
  "containerDefinitions": [
    {
      "name": "php-app",
      "image": "php:fpm",
      "environment": [
        {
          "name": "Container",
          "value": "PHP"
        }
      ],
      "essential": true,
      "memory": 128,
      "mountPoints": [
        {
          "sourceVolume": "php-app",
          "containerPath": "/var/www/html",
          "readOnly": true
        }
      ]
    },
    {
      "name": "nginx-proxy",
      "image": "nginx",
      "essential": true,
      "memory": 128,
      "portMappings": [
        {
          "hostPort": 80,
          "containerPort": 80
        }
      ],
      "links": [
        "php-app"
      ],
      "mountPoints": [
        {
          "sourceVolume": "php-app",
          "containerPath": "/var/www/html",
          "readOnly": true
        },
        {
          "sourceVolume": "nginx-proxy-conf",
          "containerPath": "/etc/nginx/conf.d",
          "readOnly": true
        },
        {
          "sourceVolume": "awseb-logs-nginx-proxy",
          "containerPath": "/var/log/nginx"
        }
      ]
    }
  ]
}
```
