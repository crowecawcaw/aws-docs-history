# Increasing Amazon ECS Linux container instance network interfaces

###### Note

This feature is not available on Fargate.

Each task that uses the `awsvpc` network mode receives its own elastic network
interface (ENI), which is attached to the container instance that hosts it.
There is a default limit to the number of network interfaces that can be attached to an
Amazon EC2 instance, and the primary network interface counts as one. For example, by default a
`c5.large` instance may have up to three ENIs attached to it. The primary
network interface for the instance counts as one, so you can attach an additional two ENIs
to the instance. Because each task using the `awsvpc` network mode requires an
ENI, you can typically only run two such tasks on this instance
type.

Amazon ECS supports launching container instances with increased ENI density
using supported Amazon EC2 instance types. When you use these instance types and turn on the
`awsvpcTrunking` account setting, additional ENIs are available on newly
launched container instances. This configuration allows you to place more tasks on each
container instance. To use the console to turn on the feature, see [Modifying Amazon ECS account settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md"). To use the AWS CLI to turn on the feature, see [Managing Amazon ECS account settings using the AWS CLI](account-setting-management-cli.md "account-setting-management-cli.md").

For example, a `c5.large` instance with `awsvpcTrunking` has an
increased ENI limit of twelve. The container instance will have the primary
network interface and Amazon ECS creates and attaches a "trunk" network interface to the
container instance. So this configuration allows you to launch ten tasks on the container
instance instead of the current two tasks.

The trunk network interface is fully managed by Amazon ECS and is deleted when you either
terminate or deregister your container instance from the cluster. For more information, see
[Amazon ECS task networking options for EC2](task-networking.md "task-networking.md").

## Considerations

Consider the following when using the ENI trunking feature.

- Only Linux variants of the Amazon ECS-optimized AMI, or other Amazon Linux variants with
  version `1.28.1` or later of the container agent and version
  `1.28.1-2` or later of the ecs-init package, support the
  increased ENI limits. If you use the latest Linux variant of the
  Amazon ECS-optimized AMI, these requirements will be met. Windows containers are
  not supported at this time.
- Only new Amazon EC2 instances launched after enabling `awsvpcTrunking`
  receive the increased ENI limits and the trunk network interface.
  Previously launched instances do not receive these features regardless of the
  actions taken.
- Amazon EC2 instances must have resource-based IPv4 DNS requests turned off. To
  disable this option, clear the **Enable resource-based IPV4 (A record)
  DNS requests** option when you create a new instance in the Amazon EC2
  console. To disable this option using the AWS CLI, use the following
  command.

```
`aws ec2 modify-private-dns-name-options --instance-id `i-xxxxxxx` --no-enable-resource-name-dns-a-record --no-dry-run`
```

- Amazon EC2 instances in shared subnets are not supported. They will fail to
  register to a cluster if they are used.
- Your tasks must use the `awsvpc` network mode and the
  EC2. Tasks using Fargate
  always received a dedicated ENI regardless of how many are
  launched, so this feature is not needed.
- Your tasks must be launched in the same Amazon VPC as your container instance. Your
  tasks will fail to start with an attribute error if they are not within the same
  VPC.
- When launching a new container instance, the instance transitions to a
  `REGISTERING` status while the trunk elastic network interface is
  provisioned for the instance. If the registration fails, the instance
  transitions to a `REGISTRATION_FAILED` status. You can troubleshoot a
  failed registration by describing the container instance to view the
  `statusReason` field which describes the reason for the failure.
  The container instance then can be manually deregistered or terminated. Once the
  container instance is successfully deregistered or terminated, Amazon ECS will delete
  the trunk ENI.

###### Note

Amazon ECS emits container instance state change events which you can monitor
for instances that transition to a `REGISTRATION_FAILED` state.
For more information, see [Amazon ECS container instance state change events](ecs_container_instance_events.md "ecs_container_instance_events.md").

- Once the container instance is terminated, the instance transitions to a
  `DEREGISTERING` status while the trunk elastic network interface
  is deprovisioned. The instance then transitions to an `INACTIVE`
  status.
- If a container instance in a public subnet with the increased
  ENI limits is stopped and then restarted, the instance loses
  its public IP address, and the container agent loses its connection.
- When you enable `awsvpcTrunking`, container instances receive an
  additional ENI that uses the VPC's default security group, and is
  managed by Amazon ECS.

A default VPC comes with a public subnet in each Availability Zone, an
internet gateway, and settings to enable DNS resolution. The subnet is a public
subnet, because the main route table sends the subnet's traffic that is destined
for the internet to the internet gateway. You can make a default subnet into a
private subnet by removing the route from the destination 0.0.0.0/0 to the
internet gateway. However, if you do this, no container instance running in that
subnet can access the internet. You can add or delete security group rules to
control the traffic into and out of your subnets. For more information, see
[Security group
rules](../../../vpc/latest/userguide/security-group-rules.md "../../../vpc/latest/userguide/security-group-rules.md") in the _Amazon Virtual Private Cloud User
Guide_.

## Prerequisites

Before you launch a container instance with the increased ENI limits,
the following prerequisites must be completed.

- The service-linked role for Amazon ECS must be created. The Amazon ECS service-linked
  role provides Amazon ECS with the permissions to make calls to other AWS services
  on your behalf. This role is created for you automatically when you create a
  cluster, or if you create or update a service in the AWS Management Console. For more
  information, see [Using service-linked roles for Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md"). You can also create the
  service-linked role with the following AWS CLI command.

```
`aws iam create-service-linked-role --aws-service-name ecs.amazonaws.com`
```

- Your account or container instance IAM role must enable the
  `awsvpcTrunking` account setting. We recommend that you create 2
  container instance roles (`ecsInstanceRole`). You can then enable the
  `awsvpcTrunking` account setting for one role and use that role
  for tasks that require ENI trunking. For information about the container
  instance role, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").

After the prerequisites are met, you can launch a new container instance using one of
the supported Amazon EC2 instance types, and the instance will have the increased
ENI limits. For a list of supported instance types, see [Supported instances for increased Amazon ECS container network interfaces](eni-trunking-supported-instance-types.md "eni-trunking-supported-instance-types.md"). The container instance must
have version `1.28.1` or later of the container agent and version
`1.28.1-2` or later of the ecs-init package. If you use the latest Linux
variant of the Amazon ECS-optimized AMI, these requirements will be met. For more
information, see [Launching an Amazon ECS Linux container instance](launch_container_instance.md "launch_container_instance.md").

###### Important

Amazon EC2 instances must have resource-based IPv4 DNS requests turned off. To disable
this option, ensure the **Enable resource-based IPV4 (A record) DNS
requests** option is deselected when creating a new instance using the
Amazon EC2 console. To disable this option using the AWS CLI, use the following
command.

```
`aws ec2 modify-private-dns-name-options --instance-id `i-xxxxxxx` --no-enable-resource-name-dns-a-record --no-dry-run`
```

###### To view your container instances with increased ENI limits with the AWS CLI

Each container instance has a default network interface, referred to as a trunk
network interface. Use the following command to list your container instances with
increased ENI limits by querying for the
`ecs.awsvpc-trunk-id` attribute, which indicates it has a trunk
network interface.

- [list-attributes](../../../cli/latest/reference/ecs/list-attributes.md "../../../cli/latest/reference/ecs/list-attributes.md")
  (AWS CLI)

```
`aws ecs list-attributes \
 --target-type container-instance \
 --attribute-name ecs.awsvpc-trunk-id \
 --cluster `cluster_name` \
 --region `us-east-1``
```

- [Get-ECSAttributeList](../../../powershell/latest/reference/items/Get-ECSAttributeList.md "../../../powershell/latest/reference/items/Get-ECSAttributeList.md") (AWS Tools for Windows PowerShell)

```
`Get-ECSAttributeList -TargetType container-instance -AttributeName ecs.awsvpc-trunk-id -Region `us-east-1``
```
