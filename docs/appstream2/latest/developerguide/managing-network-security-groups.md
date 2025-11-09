# Security Groups in Amazon WorkSpaces Applications

You can provide additional access control to your VPC from streaming instances in a
fleet or an image builder in Amazon WorkSpaces Applications by associating them with VPC security groups.
Security groups that belong to your VPC allow you to control the network traffic between
WorkSpaces Applications streaming instances and VPC resources such as license servers, file servers, and
database servers. For more information, see [Security Groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the
_Amazon VPC User Guide_.

The rules that you define for your VPC security group are applied when the security
group is associated with a fleet or image builder. The security group rules determine
what network traffic is allowed from your streaming instances. For more information, see
[Security Group Rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the _Amazon VPC User Guide_.

You can associate up to five security groups while launching a new image builder or while
creating a new fleet. You can also associate security groups with an existing fleet or change
the security groups for a fleet (to change security groups for a fleet, you must first stop
the fleet). For more information, see [Working with Security Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups") in the
_Amazon VPC User Guide_.

If you don't select a security group, your image builder or fleet is associated with
the default security group for your VPC. For more information, see
[Default Security Group for Your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup "../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup") in the _Amazon VPC User Guide_.

Use these additional considerations when using security groups with WorkSpaces Applications.

- All end user data, such as internet traffic, home folder data, or application
  communication with VPC resources, are affected by the security groups associated
  with the streaming instance.
- Streaming pixel data is not affected by security groups.
- If you have enabled default internet access for your fleet or image builder,
  the rules of the associated security groups must allow internet access.
  You can create or edit rules for your security groups or create new security groups
  using the Amazon VPC console.

- **To associate security groups with an image
  builder** — Follow the instructions at [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").
- **To associate security groups with a
  fleet**

      + *While creating the fleet* — Follow the
       instructions at [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md").
      + *For an existing fleet* — Edit the fleet
       settings using the AWS Management Console.

  You can also associate security groups to your fleets using the AWS CLI and SDKs.

- **AWS CLI** — Use the
  [create-fleet](../../../cli/latest/reference/appstream/create-fleet.md "../../../cli/latest/reference/appstream/create-fleet.md") and [update-fleet](../../../cli/latest/reference/appstream/update-fleet.md "../../../cli/latest/reference/appstream/update-fleet.md") commands.
- **AWS SDKs** — Use the
  [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md") and [UpdateFleet](../APIReference/API_UpdateFleet.md "../APIReference/API_UpdateFleet.md") API
  operations.
  For more information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") and [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
