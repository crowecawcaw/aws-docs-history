# Key resources and components

Create the following resources in your AWS account before you set up your game
hosting resources with Amazon GameLift Servers FleetIQ. As a best practice, develop and test your game server
deployment with these resources before using them through a game server group.

- **Amazon Machine Image (AMI).** An AMI is a
  template for a specific software configuration that you want to launch with your
  Amazon EC2 instances. For game hosting, your AMI includes an operating system, your
  game server binaries or container, and other runtime software that your game
  server requires. For more information about creating an AMI, refer to [Amazon Machine Images](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") in the
  Amazon EC2 User Guide. AMIs are Region-specific. You can copy an AMI from one Region
  to another, as described in [Copying
  AMIs](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md") in the _Amazon EC2 User
  Guide_.
- **Amazon EC2 launch template.** A launch template
  provides instructions for launching and managing instances in an Auto Scaling group. It
  specifies an AMI, provides a list of suitable instance types, and sets network,
  security, and other properties. For more information about creating a launch
  template, see [Launching an
  Instance from a Launch Template](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md") in the _Amazon EC2 User Guide_. Launch templates are
  Region-specific.
- **AWS IAM role.** An IAM role defines a set of
  permissions that allow limited access to AWS resources. A trusted entity, such
  as another AWS service, can assume the role and inherit its permissions. When
  using Amazon GameLift Servers FleetIQ, you must provide an IAM role with a managed policy that allows
  Amazon GameLift Servers FleetIQ to create and access Auto Scaling groups and EC2 instance resources in
  your AWS account. IAM roles are not Region-specific.
  Amazon GameLift Servers FleetIQ manages the following resources directly and has direct authority over
  them.

- **Amazon GameLift Servers game server group**. A game server
  group contains configuration settings that define how Amazon GameLift Servers FleetIQ works with a
  corresponding Auto Scaling group to deliver low-cost game hosting. Game server groups
  are Region-specfic. When you create a game server group in a Region, a new Auto
  Scaling group is automatically created in your AWS account in the same Region.
  The game server group is linked to the Auto Scaling group and has access (by
  assuming the IAM role) to manage and modify some of its settings. A game server
  group is a long-lived resource; developers should expect to create them
  infrequently. A game server group is also a functional grouping resource for
  game servers that are hosted on instances in the Auto Scaling group and
  registered with Amazon GameLift Servers FleetIQ.
- **Amazon GameLift Servers game server.** A game server resource
  represents a game execution that is running on an instance associated with a
  Amazon GameLift Servers FleetIQ game server group. This resource is created when a game server
  registers with Amazon GameLift Servers FleetIQ and identifies the game server group it belongs to.
  Amazon GameLift Servers FleetIQ tracks the utilization status and claim status of each registered game
  server, which enables it to monitor game server availability. Game servers are
  Region-specific in that they are associated with a Region-specific game server
  group. When your game requests a new game server, it specifies the game server
  group and Region.
  These resources are created through Amazon GameLift Servers FleetIQ resources. They are created in your AWS
  account and you have full control of them.

- **Amazon EC2 Auto Scaling group.** An Auto Scaling
  group launches and manages a collection of EC2 instances, and automatically
  scales group capacity. With Amazon GameLift Servers FleetIQ, there is a one-to-one relationship between
  the game server group and the Auto Scaling group. While you can update all
  settings for an Auto Scaling group, Amazon GameLift Servers FleetIQ periodically overrides and updates
  certain settings as part of its logic to balance Spot Instances for game hosting
  viability. For more information, see [AutoScalingGroup](../../../autoscaling/ec2/userguide/AutoScalingGroup.md "../../../autoscaling/ec2/userguide/AutoScalingGroup.md") in the
  _Amazon EC2 Auto Scaling User Guide_. Auto Scaling groups are
  Region-specific; they are created in the same Region as the game server
  group.
- **Amazon EC2 Instance.** An instance is a virtual
  server in the cloud. Instance types have specific hardware configurations that
  specify compute, memory, disk, and network resources. They are typically
  launched by an Auto Scaling group with an AMI. Instances can be Spot or On-Demand,
  depending on availability. With Amazon GameLift Servers FleetIQ, instances run one or multiple game
  server processes, each of which can host multiple game sessions. Instances are
  Region-specific in that they are associated with a Region-specific Auto Scaling
  group.
