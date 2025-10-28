# Working with shared subnets

This section describes how to work with shared subnets in the AWS console and AWS CLI.

###### Contents

- [Share a subnet](#vpc-sharing-share-subnet "#vpc-sharing-share-subnet")
- [Unshare a shared subnet](#vpc-sharing-stop-share-subnet "#vpc-sharing-stop-share-subnet")
- [Identify the owner of a shared subnet](#vpc-sharing-view-owner "#vpc-sharing-view-owner")

## Share a subnet

You can share non-default subnets with other accounts within your organization as
follows. In addition, you can share security groups across AWS Organizations. For more
information, see [Share security groups with AWS Organizations](security-group-sharing.md "security-group-sharing.md").

###### To share a subnet using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. Select your subnet and choose **Actions**, **Share
   subnet**.
4. Select your resource share and choose **Share subnet**.

###### To share a subnet using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") and
[associate-resource-share](../../../cli/latest/reference/ram/associate-resource-share.md "../../../cli/latest/reference/ram/associate-resource-share.md") commands.

### Map subnets across Availability Zones

To ensure that resources are distributed across the Availability Zones for a Region,
we independently map Availability Zones to names for each account. For example, the
Availability Zone `us-east-1a` for your AWS account might not have the same
location as `us-east-1a` for another AWS account.

To coordinate Availability Zones across accounts for VPC sharing, you must use an
_AZ ID_, which is a unique and consistent identifier for an Availability
Zone. For example, `use1-az1` is the AZ ID for one of the Availability Zones in
the `us-east-1` Region. Use AZ IDs to determine the location of resources in one
account relative to another account. You can view the AZ ID for each subnet in the Amazon VPC
console.

The following diagram illustrates two accounts with different mappings of Availability
Zone code to AZ ID.

![Two accounts with different mappings of Availability Zone code to AZ ID.](images/availability-zone-mapping.png)

## Unshare a shared subnet

The owner can unshare a shared subnet with participants at any time. After the owner
unshares a shared subnet, the following rules apply:

- Existing participant resources continue to run in the unshared subnet. AWS managed
  services (for example, Elastic Load Balancing) that have automated/managed workflows (such as auto scaling
  or node replacement) may require continuous access to the shared subnet for some resources.
- Participants can no longer create new resources in the unshared subnet.
- Participants can modify, describe, and delete their resources that are in the
  subnet.
- If participants still have resources in the unshared subnet, the owner cannot delete
  the shared subnet or the shared-subnet VPC. The owner can only delete the subnet or
  shared-subnet VPC after the participants delete all the resources in the unshared
  subnet.

###### To unshare a subnet using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. Select your subnet and choose **Actions**, **Share
   subnet**.
4. Choose **Actions**, **Stop sharing**.

###### To unshare a subnet using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Identify the owner of a shared subnet

Participants can view the subnets that have been shared with them by using the Amazon VPC
console, or the command line tool.

###### To identify a subnet owner using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**. The
   **Owner** column displays the subnet owner.

###### To identify a subnet owner using the AWS CLI

Use the [describe-subnets](../../../cli/latest/reference/ec2/describe-subnets.md "../../../cli/latest/reference/ec2/describe-subnets.md") and
[describe-vpcs](../../../cli/latest/reference/ec2/describe-vpcs.md "../../../cli/latest/reference/ec2/describe-vpcs.md") commands, which
include the ID of the owner in their output.
