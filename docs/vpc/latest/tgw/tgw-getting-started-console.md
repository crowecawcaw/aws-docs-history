

# Tutorial: Create an AWS Transit Gateway using the Amazon VPC Console
<a name="tgw-getting-started-console"></a>

In this tutorial, you'll learn how to use the Amazon VPC Console to create a transit gateway and connect two VPCs to it. You'll create the transit gateway, attach both VPCs, and then configure the necessary routes to enable communication between the transit gateway and your VPCs.

## Prerequisites
<a name="tgw-prerequisites"></a>
+ To demonstrate a simple example of using a transit gateway, create two VPCs in the same Region. The VPCs can neither have identical nor overlapping CIDRs. Launch one Amazon EC2 instance in each VPC. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the *Amazon VPC User Guide* and [Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance) in the *Amazon EC2 User Guide*.
+ You can't have identical routes pointing to two different VPCs. A transit gateway does not propagate the CIDRs of a newly attached VPC if an identical route exists in the transit gateway route tables.
+ Verify that you have the permissions required to work with transit gateways. For more information, see [Identity and access management in AWS Transit Gateway](transit-gateway-authentication-access-control.md).
+ You can't ping between hosts if you haven't added an ICMP rule to each of the host security groups. For more information, see [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the *Amazon VPC User Guide*.

**Topics**
+ [Prerequisites](#tgw-prerequisites)
+ [Step 1: Create the transit gateway](#step-create-tgw)
+ [Step 2: Attach your VPCs to your transit gateway](#step-attach-vpcs)
+ [Step 3: Add routes between the transit gateway and your VPCs](#step-add-routes)
+ [Step 4: Test the transit gateway](#step-test-tgw)
+ [Step 5: Delete the transit gateway](#step-delete-tgw)

## Step 1: Create the transit gateway
<a name="step-create-tgw"></a>

When you create a transit gateway, we create a default transit gateway route table and use it as the default association route table and the default propagation route table.

**To create a transit gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the Region selector, choose the Region that you used when you created the VPCs.

1. On the navigation pane, choose **Transit Gateways**.

1. Choose **Create transit gateway**.

1. (Optional) For **Name tag**, enter a name for the transit gateway. This creates a tag with "Name" as the key and the name that you specified as the value.

1. (Optional) For **Description**, enter a description for the transit gateway.

1. In **Configure the transit gateway** section, do the following:

   1. For **Amazon side Autonomous System Number (ASN)**, enter the private ASN for your transit gateway. This should be the ASN for the AWS side of a Border Gateway Protocol (BGP) session.

      The range is from 64512 to 65534 for 16-bit ASNs. 

      The range is from 4200000000 to 4294967294 for 32-bit ASNs. 

      If you have a multi-Region deployment, we recommend that you use a unique ASN for each of your transit gateways.

   1. (Optional) Choose whether to enable any of the following:
      +  **DNS support** for VPCs attached to this transit gateway. 
      + **VPN ECMP** support for VPN connections attached to the transit gateway. 
      + **Default route table association**, which automatically associates transit gateway attachments with this transit gateway's default route table.
      + **Default route table propagation**, which automatically propagates route table attachments to this transit gateway's default route table.
      + **Multicast support**, which allows you to create multicast domains in this transit gateway.

1. (Optional) In the **Configure-cross-account sharing options** section, choose whether to **Auto accept shared attachments**. If enabled, attachments are automatically accepted. Otherwise, you must accept or reject attachment requests.

1. (Optional) In the **Transit gateway CIDR blocks section**, add a size /24 CIDR block or larger for IPv4 addresses or /64 block or larger CIDR block for IPv6 addresses. You can associate any public or private IP address range, except for addresses in the 169.254.0.0/16 range, and ranges that overlap with the addresses for your VPC attachments and on-premises networks.
**Note**  
Transit gateway CIDR blocks are used if you are configuring Connect (GRE) attachments or PrivateIP VPNs. Transit Gateway assigns IPs for the Tunnel endpoints (GRE/PrivateIP VPN) from this range.

1. (Optional) Add key-value tags to this transit gateway to further help identify it.

   1. Choose **Add new tag**.

   1. Enter a **Key** name and associated **Value**.

   1. Choose **Add new tag** to add additional tags, or skip to the next step. 

1. Choose **Create transit gateway**. When the gateway is created, the initial state of the transit gateway is `pending`.

## Step 2: Attach your VPCs to your transit gateway
<a name="step-attach-vpcs"></a>

Wait until the transit gateway you created in the previous section shows as available before proceeding with creating an attachment. Create an attachment for each VPC.

Confirm that you have created two VPCs and launched an EC2 instance in each, as described in [Prerequisites](#tgw-prerequisites).

**Create a transit gateway attachment to a VPC**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Choose **Create transit gateway attachment**.

1. (Optional) For **Name tag**, enter a name for the attachment.

1. For **Transit gateway ID**, choose the transit gateway to use for the attachment.

1. For **Attachment type**, choose **VPC**.

1. Choose whether to enable **DNS support**. For this exercise, do not enable **IPv6 support**.

1. For **VPC ID**, choose the VPC to attach to the transit gateway.

1. For **Subnet IDs**, select one subnet for each Availability Zone to be used by the transit gateway to route traffic. You must select at least one subnet. You can select only one subnet per Availability Zone.

1. Choose **Create transit gateway attachment**.

Each attachment is always associated with exactly one route table. Route tables can be associated with zero to many attachments. To determine the routes to configure, decide on the use case for your transit gateway, and then configure the routes. For more information, see [Example transit gateway scenarios](how-transit-gateways-work.md#TGW_Scenarios).

## Step 3: Add routes between the transit gateway and your VPCs
<a name="step-add-routes"></a>

A route table includes dynamic and static routes that determine the next hop for associated VPCs based on the destination IP address of the packet. Configure a route that has a destination for non-local routes and the target of the transit gateway attachment ID. For more information, see [Routing for a transit gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-tgw) in the *Amazon VPC User Guide*.

**To add a route to a VPC route table**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Route Tables**.

1. Choose the route table associated with your VPC.

1. Choose the **Routes** tab, then choose **Edit routes**.

1. Choose **Add route**.

1. In the **Destination** column, enter the destination IP address range. For **Target**, choose **Transit Gateway**, and then choose the transit gateway ID.

1. Choose **Save changes**.

## Step 4: Test the transit gateway
<a name="step-test-tgw"></a>

You can confirm that the transit gateway was successfully created by connecting to an Amazon EC2 instance in each VPC, and then sending data between them, such as a ping command. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*.

## Step 5: Delete the transit gateway
<a name="step-delete-tgw"></a>

When you no longer need a transit gateway, you can delete it. 

You cannot delete a transit gateway that has resource attachments. If you try to delete a transit gateway with attachments, you'll be prompted to first delete those attachments before you can delete the transit gateway. As soon as the transit gateway is deleted, you stop incurring charges for it.

**To delete your transit gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateways**.

1. Select the transit gateway, and then choose **Actions**, **Delete transit gateway**. 

1. Enter **delete** and choose **Delete**.

   The **State** of the transit gateway on the **Transit gateways** page is **Deleting**. Once deleted the transit gateway is removed from the page. 