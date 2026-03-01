# Define which container instances Amazon ECS uses for tasks

A task placement constraint is a rule about a container instance that Amazon ECS uses to
determine if the task is allowed to run on the instance. At least one container instance
must match the constraint. If there are no instances that match the constraint, the task
remains in a `PENDING` state. When you create a new service or update an existing
one, you can specify task placement constraints for the service's tasks.

You can specify task placement constraints in the service definition, task definition, or
task using the `placementConstraint` parameter.

```
"placementConstraints": [
    {
        "expression": "The expression that defines the task placement constraints",
        "type": "The placement constraint type to use"
    }
]
```

The following table describes how to use the parameters.

| Constraint type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Can be specified when                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `distinctInstance`Place each active task on a different<br>container<br>instance.Amazon ECS looks at the desired status of the tasks for the task placement. For example, if the desired status of the existing task is `STOPPED`, (but the last status isn’t), a new incoming task can be placed on the same instance despite the `distinctInstance` placement constraint. Therefore, you might see 2 tasks with last status of `RUNNING` on the same instance.Important We recommend that customers looking for strong isolation for their tasks<br>use Fargate. Fargate runs each task in a hardware virtualization<br>environment. This ensures that these containerized workloads do not share<br>network interfaces, Fargate ephemeral storage, CPU, or memory with other<br>tasks. For more information, see [Security Overview of AWS Fargate](https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf"). | • Running a task [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md")<br>• Creating a new service [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md"),                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `memberOf`Place tasks on container instances that<br>satisfy an expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | • Running a task [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md")<br>• Creating a new service [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md"),<br>• Creating a new task definition [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md")<br>• Creating a new revision of a task definition [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md")<br>• Updating a service [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md") |

When you use the `memberOf` constraint type, you can create an expression using
the cluster query language which defines the container instances where Amazon ECS can place
tasks. The expression is a way for you to group your container instances by attributes. The
expression goes in the `expression` parameter of
`placementConstraint`.

## Amazon ECS container instance attributes

You can add custom metadata to your container instances, known as
_attributes_. Each attribute has a name and an optional string
value. You can use the built-in attributes provided by Amazon ECS or define custom
attributes.

The following sections contain sample built-in, optional, and custom
attributes.

### Built-in attributes

Amazon ECS automatically applies the following attributes to your container
instances.

`ecs.ami-id`

The ID of the AMI used to launch the instance. An example value for
this attribute is `ami-1234abcd`.

`ecs.availability-zone`

The Availability Zone for the instance. An example value for this
attribute is `us-east-1a`.

`ecs.instance-type`

The instance type for the instance. An example value for this
attribute is `g2.2xlarge`.

`ecs.os-type`

The operating system for the instance. The possible values for this
attribute are `linux` and `windows`.

`ecs.os-family`

The operating system version for the instance.

For Linux instances, the valid value is `LINUX`. For
Windows instances, ECS sets the value in the
`WINDOWS_SERVER_<`OS*Release`>*<`FULL
 or CORE`>`format. The valid values are
`WINDOWS_SERVER_2022_FULL`,
 `WINDOWS_SERVER_2022_CORE`,
 `WINDOWS_SERVER_20H2_CORE`,
 `WINDOWS_SERVER_2019_FULL`,
 `WINDOWS_SERVER_2019_CORE`, and
 `WINDOWS_SERVER_2016_FULL`.

This is important for Windows containers and Windows containers on AWS Fargate because
the OS version of every Windows container must match that of the host.
If the Windows version of the container image is different than the
host, the container doesn't start. For more information, see [Windows container version compatibility](https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility?tabs=windows-server-2022%2Cwindows-11 "https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility?tabs=windows-server-2022%2Cwindows-11") on the Microsoft
documentation website.

If your cluster runs multiple Windows versions, you can ensure that a
task is placed on an EC2 instance running on the same version by using
the placement constraint: `memberOf(attribute:ecs.os-family ==
 WINDOWS_SERVER_<OS_Release>_<FULL or CORE>)`. For more
information, see [Retrieving Amazon ECS-optimized Windows AMI metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md").

`ecs.cpu-architecture`

The CPU architecture for the instance. Example values for this
attribute are `x86_64` and `arm64`.

`ecs.vpc-id`

The VPC the instance was launched into. An example value for this
attribute is `vpc-1234abcd`.

`ecs.subnet-id`

The subnet the instance is using. An example value for this attribute
is `subnet-1234abcd`.

###### Note

Amazon ECS Managed Instances supports the following subset of attributes:

- `ecs.subnet-id`
- `ecs.availability-zone`
- `ecs.instance-type`
- `ecs.cpu-architecture`

### Optional attributes

Amazon ECS may add the following attributes to your container instances.

`ecs.awsvpc-trunk-id`

If this attribute exists, the instance has a trunk network interface.
For more information, see [Increasing Amazon ECS Linux container instance network interfaces](container-instance-eni.md "container-instance-eni.md").

`ecs.outpost-arn`

If this attribute exists, it contains the Amazon Resource Name (ARN) of the Outpost.
For more information, see [Amazon Elastic Container Service on AWS Outposts](using-outposts.md "using-outposts.md").

`ecs.capability.external`

If this attribute exists, the instance is identified as an external
instance. For more information, see [Amazon ECS clusters for external instances](ecs-anywhere.md "ecs-anywhere.md").

### Custom attributes

You can apply custom attributes to your container instances. For example, you can
define an attribute with the name "stack" and a value of "prod".

When specifying custom attributes, you must consider the following.

- The `name` must contain between 1 and 128 characters and name
  may contain letters (uppercase and lowercase), numbers, hyphens,
  underscores, forward slashes, back slashes, or periods.
- The `value` must contain between 1 and 128 characters and may
  contain letters (uppercase and lowercase), numbers, hyphens, underscores,
  periods, at signs (@), forward slashes, back slashes, colons, or spaces. The
  value can't contain any leading or trailing whitespace.
