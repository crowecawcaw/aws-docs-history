

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Managing a FinSpace VPC connection
<a name="manage-vpc"></a>

**Important**  
Amazon FinSpace Dataset Browser will be discontinued on {{March 26, 2025}}. Starting {{November 29, 2023}}, FinSpace will no longer accept the creation of new Dataset Browser environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/) will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/) or contact [AWS Support](https://aws.amazon.com/contact-us/) to assist with your transition.

This section explains how to set up and remove a FinSpace virtual private cloud (VPC) connection.

## Prerequisites
<a name="cno-prereq"></a>

Before you proceed, complete the following prerequisites: 
+ Make sure that a FinSpace environment has been created. For more information, see [Setting up an Amazon FinSpace environment](https://docs.aws.amazon.com/finspace/latest/userguide/setting-up-for-amazon-finspace.html).
+ Make sure that a transit gateway has been created in AWS Transit Gateway. For more information, see [Create the transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html#step-create-tgw) in the *AWS Transit Gateway User Guide*.
+ Make sure that you’ve gathered the following information to create an Support case to request access:
  + FinSpace environment ID.
  + AWS Region of the FinSpace environment.
  + Transit gateway ID of the transit gateway that you will connect your FinSpace environment to.
  + The IP address range to use for the customer-facing side of the NAT gateway. This should be a /26 IP address range from the 100.64.0.0/10 range that is specified by RFC 6598.
  + (Optional) Custom DNS domain name – The name of the domain for which the DNS queries are forwarded to custom DNS server IP address.
  + (Optional) Custom DNS server IP address – The IP address that's routable from your transit gateway attachment.

## Considerations
<a name="cno-considerations"></a>

Before you get started with the setup, make sure that you review the following considerations:
+ The /26 IP address range for the routable subnets that is attached to the transit gateway must be from the 100.64.0.0/10 range specified by RFC 6598.
+ The /26 IP address range for the routable subnets that is attached to the transit gateway must be unique across FinSpace environments and your network that's connected to the same transit gateway. For example, you might have two FinSpace environments (environment-A and environment-B) that are connected to TGW-A. Ensure that the /26 CIDR provided for each environment is distinct across environment-A and environment-B, and your network connected to the TGW-A. 

## Setting up a VPC connection
<a name="setup-vpc"></a>

**To set up a VPC connection**

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support).

1. Open a technical support case to enable the VPC connection for FinSpace, and provide the following information: 
   + The FinSpace environment ID
   + The transit gateway ID
   + The AWS Region of the FinSpace environment
   + The /26 IP range to use for the customer-facing side of the NAT gateway
   + (Optional) The custom DNS domain name
   + (Optional) The custom DNS server IP address

   For more information, see [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide*.

1. Create a RAM share for your transit gateway to the FinSpace environment infrastructure account. For more information, see [Share a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-sharing) in the *AWS Transit Gateway User Guide*.

1. After verifying the support case, a FinSpace operator runs a setup program. This program accepts the RAM share request, disables internet in the FinSpace environment infrastructure account, and issues a VPC attachment request to your transit gateway.

1. When the request is complete, the FinSpace operator sends a notification, and adds the transit gateway attachment ID and the Availability Zone (AZ) to the VPC attachment request.

1. Accept the VPC attachment request that FinSpace issues to your transit gateway. For more information, see [Accept a shared attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-accept-shared-attachment) in the *AWS Transit Gateway User Guide*.

1. Configure the routing tables in your transit gateway traffic, and route to/from the subnets in the VPC that were attached in the VPC attachment.
**Note**  
Ensure that your transit gateway attachment is created with all the Availability Zones provided in the notification that you receive from the FinSpace operator. 

1. Ensure that the VPC connection setup is successful by following the steps in [Validating your VPC connection](vpc-validation.md).

## Removing a VPC connection
<a name="removing-vpc"></a>

**To remove an existing VPC connection**

1. Delete the transit gateway attachment from your transit gateway. For more information, see [Delete a VPC attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#delete-vpc-attachment) in the *AWS Transit Gateway User Guide*.

1. After removing the attachment, restore direct internet access to your FinSpace environment by creating a new technical support case that specifies the environment ID.

**Note**  
Deleting a FinSpace environment does not automatically delete the attachment. You must remove the attachment separately.

## Updating a VPC connection
<a name="updating-vpc"></a>

You cannot update an existing connection. To make changes to an existing connection, remove the old connection and create a new one.