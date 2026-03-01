# Task metadata available for Amazon ECS tasks on EC2

The Amazon ECS container agent provides a method to retrieve various task metadata and
[Docker stats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats "https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats"). This is referred to as the task metadata endpoint. The
following versions are available:

- Task metadata endpoint version 4 – Provides a variety of metadata and
  Docker stats to containers. Can also provide network rate data. Available for
  Amazon ECS tasks launched on Amazon EC2 Linux instances running at least version
  `1.39.0` of the Amazon ECS container agent. For Amazon EC2 Windows
  instances that use `awsvpc` network mode, the Amazon ECS container agent
  must be at least version `1.54.0`. For more information, see [Amazon ECS task metadata endpoint version 4](task-metadata-endpoint-v4.md "task-metadata-endpoint-v4.md").
- Task metadata endpoint version 3 – Provides a variety of metadata and
  Docker stats to containers. Available for Amazon ECS tasks launched on Amazon EC2 Linux
  instances running at least version `1.21.0` of the Amazon ECS container
  agent. For Amazon EC2 Windows instances that use `awsvpc` network mode,
  the Amazon ECS container agent must be at least version `1.54.0`. For more
  information, see [Amazon ECS task metadata endpoint version 3](task-metadata-endpoint-v3.md "task-metadata-endpoint-v3.md").
- Task metadata endpoint version 2 – Available for Amazon ECS tasks launched on
  Amazon EC2 Linux instances running at least version `1.17.0` of the Amazon ECS
  container agent. For Amazon EC2 Windows instances that use `awsvpc`
  network mode, the Amazon ECS container agent must be at least version
  `1.54.0`. For more information, see [Amazon ECS task metadata endpoint version 2](task-metadata-endpoint-v2.md "task-metadata-endpoint-v2.md").
  If your Amazon ECS task is hosted on Amazon EC2, or if your task uses the `host` network mode and is hosted on Amazon ECS Managed Instances, you can also access task host metadata using
  the [Instance Metadata Service (IMDS) endpoint](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md"). The following command, when run
  from within the instance hosting the task, lists the ID of the host instance.

```
 `curl http://169.254.169.254/latest/meta-data/`instance-id``
```

If your Amazon ECS task is hosted on Amazon EC2 and in an IPv6-only configuration, you can
access task host metadata using the IPv6 IMDS endpoint. The following command, when run
from within the instance hosting the task, lists the ID of the host instance over
IPv6.

```
 `curl http://[fd00:ec2::254]/latest/meta-data/`instance-id``
```

To access the IPv6 IMDS endpoint, enable the IPv6 IMDS endpoint on your container
instance and also configure the metadata service endpoint mode using the IMDS credential
provider for your chosen SDK to `IPv6`. For more information about enabling
the IPv6 IMDS endpoint for your container instance, see [Configure
the Instance Metadata Service options](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-options.md") in
_Amazon EC2 User Guide_. For more information about IMDS credential
provider for SDKs, see [IMDS credential
provider](../../../sdkref/latest/guide/feature-imds-credentials.md "../../../sdkref/latest/guide/feature-imds-credentials.md") in the _AWS SDKs and Tools Reference
Guide_.

###### Note

The IPv6 IMDS endpoint is not accessible when the `awsvpcTrunking`
account setting is enabled. To access container instance IAM role credentials when
`awsvpcTrunking` is enabled, you can use a task IAM role instead. For more
information about task IAM roles, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

The information you can obtain from the endpoint is divided into categories such as
`instance-id`. For more information about
the different categories of host instance metadata you can obtain using the endpoint,
see [Instance metadata categories](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md#instancedata-data-categories "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md#instancedata-data-categories") .
