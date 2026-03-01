# Storing Amazon ECS container instance configuration in Amazon S3

Amazon ECS container agent configuration is controlled with the environment variable. Linux variants of the Amazon ECS-optimized AMI look for
these variables in `/etc/ecs/ecs.config` when the container agent
starts and configure the agent accordingly. Non-sensative environment variables,
such as `ECS_CLUSTER`, can be passed to the container instance at launch
through Amazon EC2 user data and written to this file without consequence. However, other
sensitive information, such as your AWS credentials or the
`ECS_ENGINE_AUTH_DATA` variable, should never be passed to an instance in
user data or written to `/etc/ecs/ecs.config` in a way that would
allow them to show up in a `.bash_history` file.

Storing configuration information in a private bucket in Amazon S3 and granting read-only
access to your container instance IAM role is a secure and convenient way to allow
container instance configuration at launch. You can store a copy of your
`ecs.config` file in a private bucket. You can then use Amazon EC2
user data to install the AWS CLI and copy your configuration information to
`/etc/ecs/ecs.config` when the instance launches.

###### To store an `ecs.config` file in Amazon S3

1. You must grant the container instance role (**ecsInstanceRole**) permissions
   to have read only access to Amazon S3. You can do this by assigning the
   **AmazonS3ReadOnlyAccess** to the
   `ecsInstanceRole` role. For information about how to attach a
   policy to a role, see [Update permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management User Guide_
2. Create an `ecs.config` file with valid Amazon ECS agent
   configuration variables using the following format. This example configures
   private registry authentication. For more information, see [Using non-AWS container images in Amazon ECS](private-auth.md "private-auth.md").

```
ECS_ENGINE_AUTH_TYPE=dockercfg
ECS_ENGINE_AUTH_DATA={"https://index.docker.io/v1/":{"auth":"`zq212MzEXAMPLE7o6T25Dk0i`","email":"`email@example.com`"}}
```

###### Note

For a full list of available Amazon ECS agent configuration variables, see
[Amazon ECS Container Agent](https://github.com/aws/amazon-ecs-agent/blob/master/README.md "https://github.com/aws/amazon-ecs-agent/blob/master/README.md") on GitHub. 3. To store your configuration file, create a private bucket in Amazon S3. For more
information, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_. 4. Upload the `ecs.config` file to your S3 bucket. For more
information, see [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the
_Amazon Simple Storage Service User Guide_.

###### To load an `ecs.config` file from Amazon S3 at launch

1. Complete the earlier procedures in this section to allow read-only Amazon S3 access
   to your container instances and store an `ecs.config` file in a
   private S3 bucket.
2. Launch new container instances and use the following example script in the EC2
   User data. The script installs the AWS CLI and copies your configuration file to
   `/etc/ecs/ecs.config`. For more information, see [Launching an Amazon ECS Linux container instance](launch_container_instance.md "launch_container_instance.md").

```
#!/bin/bash
yum install -y aws-cli
aws s3 cp s3://`your_bucket_name`/ecs.config /etc/ecs/ecs.config
```
