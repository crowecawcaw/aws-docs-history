

# Create a VPC peering connection
<a name="create-vpc-peering-connection"></a>

To create a VPC peering connection, first create a request to peer with another VPC. To activate the request, the owner of the accepter VPC must accept the request. The following peering connections are supported:
+ Between VPCs in the same account and Region
+ Between VPCs in the same account and different Regions
+ Between VPCs in different accounts and the same Region
+ Between VPCs in different accounts and Regions

For an inter-Region VPC peering connection, the request must be made from the Region of the requester VPC, and the request must be accepted from the Region of the accepter VPC. For more information, see [Accept or reject a VPC peering connection](accept-vpc-peering-connection.md).

**Topics**
+ [Prerequisites](#vpc-peering-connection-prerequisites)
+ [Create a peering connection using the console](#create-vpc-peering-connection-console)
+ [Create a peering connection using the command line](#create-vpc-peering-connection-command-line)

## Prerequisites
<a name="vpc-peering-connection-prerequisites"></a>
+ Review the [limitations](vpc-peering-basics.md#vpc-peering-limitations) for VPC peering connections.
+ Ensure that the VPCs do not have overlapping IPv4 CIDR blocks. If they overlap, the status of the VPC peering connection immediately goes to `failed`. This limitation applies even if the VPCs have unique IPv6 CIDR blocks.

## Create a peering connection using the console
<a name="create-vpc-peering-connection-console"></a>

Use the following procedure to create a VPC peering connection.

**To create a peering connection using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Choose **Create peering connection**.

1. (Optional) For **Name**, specify a name the VPC peering connection. This creates a tag with a key of Name and the value that you specify.

1. For **VPC ID (Requester)**, select a VPC from the current account.

1. Under **Select another VPC to peer with**, do the following:

   1. For **Account**, to peer with a VPC in another account, choose **Another account** and enter the account ID . Otherwise, keep **My account**.

   1. For **Region**, to peer with a VPC in another Region, choose **Another Region** and choose the Region . Otherwise, keep **This Region**.

   1. For **VPC ID (Accepter)**, select a VPC from the specified account and Region.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and tag value.

1. Choose **Create peering connection**.

1. The owner of the accepter account must accept the peering connection. For more information, see [Accept or reject a VPC peering connection](accept-vpc-peering-connection.md).

1. Update the route tables for both VPCs to enable communication between them. For more information, see [Update your route tables for a VPC peering connection](vpc-peering-routing.md).

## Create a peering connection using the command line
<a name="create-vpc-peering-connection-command-line"></a>

You can create a VPC peering connection using the following commands:
+ [create-vpc-peering-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-peering-connection.html) (AWS CLI)
+ [New-EC2VpcPeeringConnection](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcPeeringConnection.html) (AWS Tools for Windows PowerShell)