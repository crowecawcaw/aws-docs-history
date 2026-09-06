

# Working with shared subnets
<a name="vpc-sharing-share-subnet-working-with"></a>

This section describes how to work with shared subnets in the AWS console and AWS CLI.

**Topics**
+ [Share a subnet](#vpc-sharing-share-subnet)
+ [Unshare a shared subnet](#vpc-sharing-stop-share-subnet)
+ [Identify the owner of a shared subnet](#vpc-sharing-view-owner)

## Share a subnet
<a name="vpc-sharing-share-subnet"></a>

You can share non-default subnets with other accounts within your organization as follows. In addition, you can share security groups across AWS Organizations. For more information, see [Share security groups with AWS Organizations](security-group-sharing.md).

**To share a subnet using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Select your subnet and choose **Actions**, **Share subnet**. 

1. Select your resource share and choose **Share subnet**. 

**To share a subnet using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) and [associate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share.html) commands.

### Map subnets across Availability Zones
<a name="vpc-share-subnets-map-availability-zone"></a>

To ensure that resources are distributed across the Availability Zones for a Region, we independently map Availability Zones to names for each account. For example, the Availability Zone `us-east-1a` for your AWS account might not have the same location as `us-east-1a` for another AWS account.

To coordinate Availability Zones across accounts for VPC sharing, you must use an *AZ ID*, which is a unique and consistent identifier for an Availability Zone. For example, `use1-az1` is the AZ ID for one of the Availability Zones in the `us-east-1` Region. Use AZ IDs to determine the location of resources in one account relative to another account. You can view the AZ ID for each subnet in the Amazon VPC console.

The following diagram illustrates two accounts with different mappings of Availability Zone code to AZ ID.

![Two accounts with different mappings of Availability Zone code to AZ ID.](http://docs.aws.amazon.com/vpc/latest/userguide/images/availability-zone-mapping.png)


## Unshare a shared subnet
<a name="vpc-sharing-stop-share-subnet"></a>

The owner can unshare a shared subnet with participants at any time. After the owner unshares a shared subnet, the following rules apply:
+ Existing participant resources continue to run in the unshared subnet. AWS managed services (for example, Elastic Load Balancing) that have automated/managed workflows (such as auto scaling or node replacement) may require continuous access to the shared subnet for some resources.
+ Participants can no longer create new resources in the unshared subnet.
+ Participants can modify, describe, and delete their resources that are in the subnet.
+ If participants still have resources in the unshared subnet, the owner cannot delete the shared subnet or the shared-subnet VPC. The owner can only delete the subnet or shared-subnet VPC after the participants delete all the resources in the unshared subnet.

**To unshare a subnet using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Select your subnet and choose **Actions**, **Share subnet**. 

1. Choose **Actions**, **Stop sharing**. 

**To unshare a subnet using the AWS CLI**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

## Identify the owner of a shared subnet
<a name="vpc-sharing-view-owner"></a>

Participants can view the subnets that have been shared with them by using the Amazon VPC console, or the command line tool.

**To identify a subnet owner using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**. The **Owner** column displays the subnet owner.

**To identify a subnet owner using the AWS CLI**  
Use the [describe-subnets](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-subnets.html) and [describe-vpcs](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpcs.html) commands, which include the ID of the owner in their output.