# Overview of launch templates in AWS PCS

There are [over 30 parameters
available](../../../AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.md "../../../AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.md") you can include in an EC2 launch template, controlling many aspects of
how instances are configured. Most are fully compatible with AWS PCS, but there are some
exceptions.

The following parameters of EC2 Launch template will be ignored by AWS PCS as these properties
have to be directly managed by the service:

- **Instance type/Specify instance type attributes**
  (`InstanceRequirements`) – AWS PCS does not support attribute-based instance
  selection.
- **Instance type** (`InstanceType`) –
  Specify instance types when you create a node group.
- **Advanced details/IAM instance profile**
  (`IamInstanceProfile`) – You provide this when you create or update the node
  group.
- **Advanced details/Disable API termination**
  (`DisableApiTermination`) – AWS PCS must control the lifecycle of node group
  instances it launches.
- **Advanced details/Disable API stop**
  (`DisableApiStop`) – AWS PCS must control the lifecycle of node group
  instances it launches.
- **Advanced details/Stop – Hibernate behavior**
  (`HibernationOptions`) – AWS PCS does not support instance
  hibernation.
- **Advanced details/Elastic GPU**
  (`ElasticGpuSpecifications`) – Amazon Elastic Graphics reached end of life on January 8, 2024.
- **Advanced details/Elastic inference**
  (`ElasticInferenceAccelerators`) – Amazon Elastic Inference is no longer available to new customers.
- **AAdvanced details/Specify CPU options/Threads per core**
  (`ThreadsPerCore`) – AWS PCS sets the number of threads per core to 1.
  These parameters have special requirements that support compatibility with AWS PCS:

- **User data**(`UserData`) – This must be
  multi-part encoded. See [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md "working-with_ec2-user-data.md").
- **Application and OS Images**(`ImageId`) –
  You can include this. However, if you specify an AMI ID when you create or update the node
  group, it will override the value in the launch template. The AMI you provide must be compatible
  with AWS PCS. For more information, see "[Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md "working-with_ami.md").
- **Network settings/Firewall (security
  groups)**(`SecurityGroups`) – A list of security group names can’t
  be set in an AWS PCS launch template. You can set a list of security group IDs
  (`SecurityGroupIds`), unless you define network interfaces in the launch template.
  Then, you must specify security group IDs for each interface. For more information,
  see [Security groups in AWS PCS](working-with_networking_sg.md "working-with_networking_sg.md").
- **Network settings/Advanced network
  configuration**(`NetworkInterfaces`) – If you use EC2 instances
  with a single network card, and don't require any specialized networking configuration,
  AWS PCS can configure instance networking for you. To configure multiple network cards
  or to enable Elastic Fabric Adapter on your instances, use `NetworkInterfaces`.
  Each network interface must have a list of security group IDs under `Groups`.
  For more information, see [Multiple network interfaces in
  AWS PCS](working-with_networking_multi-nic.md "working-with_networking_multi-nic.md").
- **Advanced details/Capacity
  reservation**(`CapacityReservationSpecification`) – This can be
  set, but cannot reference a specific `CapacityReservationId` when working with
  AWS PCS. You can, however, reference a capacity reservation group, where that group contains one or
  more capacity reservations. For more information, see [Capacity Reservations in AWS PCS](working-with_capacity-reservations.md "working-with_capacity-reservations.md").
