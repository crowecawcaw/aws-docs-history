

# Work with NAT gateways
<a name="nat-gateway-working-with"></a>

You can use the Amazon VPC console to create and manage your NAT gateways.

**Topics**
+ [Control the use of NAT gateways](#nat-gateway-iam)
+ [Create a NAT gateway](#nat-gateway-creating)
+ [Edit secondary IP address associations](#nat-gateway-edit-secondary)
+ [Tag a NAT gateway](#nat-gateway-tagging)
+ [Delete a NAT gateway](#nat-gateway-deleting)
+ [Command line overview](#nat-gateway-api-cli)

## Control the use of NAT gateways
<a name="nat-gateway-iam"></a>

By default, users do not have permission to work with NAT gateways. You can create an IAM role with a policy attached that grants users permissions to create, describe, and delete NAT gateways. For more information, see [Identity and access management for Amazon VPC](security-iam.md).

## Create a NAT gateway
<a name="nat-gateway-creating"></a>

Use the following procedure to create a NAT gateway.

**Related quotas**
+ You won't be able to create a public NAT gateway if you've exhausted the number of Elastic IP addresses allocated to your account. For more information, see [Elastic IP addresses](amazon-vpc-limits.md#vpc-limits-eips).
+ You can assign up to 8 private IPv4 addresses to your private NAT gateway. This limit is not adjustable.
+ You are limited to associating 2 Elastic IP addresses to your public NAT gateway by default. You can increase this limit by requesting a quota adjustment. For more information, see [Elastic IP addresses](amazon-vpc-limits.md#vpc-limits-eips).

**To create a NAT gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **NAT gateways**.

1. Choose **Create NAT gateway**.

1. (Optional) Specify a name for the NAT gateway. This creates a tag where the key is **Name** and the value is the name that you specify.

1. Select the subnet in which to create the NAT gateway.

1. For **Connectivity type**, leave the default **Public** selection to create a public NAT gateway or choose **Private** to create a private NAT gateway. For more information about the difference between a public and private NAT gateway, see [NAT gateways](vpc-nat-gateway.md).

1. If you chose **Public**, do the following; otherwise, skip to step 8:

   1. Choose an **Elastic IP allocation ID** to assign an Elastic IP address to the NAT gateway or choose **Allocate Elastic IP** to automatically allocate one for the public NAT gateway. You are limited to associating 2 Elastic IP addresses to your public NAT gateway by default. You can increase this limit by requesting a quota adjustment. For more information, see [Elastic IP addresses](amazon-vpc-limits.md#vpc-limits-eips).
**Important**  
When you assign an Elastic IP address to a public NAT gateway, the network border group of the EIP must match the network border group of the Availability Zone (AZ) that you're launching the public NAT gateway into. If it's not the same, the NAT gateway will fail to launch. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information, see [1. Allocate an Elastic IP address](WorkWithEIPs.md#allocate-eip). 

   1. (Optional) Choose **Additional settings** and, under **Private IP address - optional**, enter a private IPv4 address for the NAT gateway. If you don't enter an address, AWS will automatically assign a private IPv4 address to your NAT gateway at random from the subnet that your NAT gateway is in.

   1. Skip to step 11.

1. If you chose **Private**, for **Additional settings**, **Private IPv4 address assigning method**, choose one of the following:
   + **Auto-assign**: AWS chooses the primary private IPv4 address for the NAT gateway. For **Number of auto-assigned private IPv4 addresses**, you can optionally specify the number of secondary private IPv4 addresses for the NAT gateway. AWS chooses these IP addresses at random from the subnet for your NAT gateway.
   + **Custom**: For **Primary private IPv4 address**, choose the primary private IPv4 address for the NAT gateway. For **Secondary private IPv4 addresses**, you can optionally specify up to 7 secondary private IPv4 addresses for the NAT gateway.

1. If you chose **Custom** in Step 8, skip this step. If you chose **Auto-assign**, under **Number of auto-assigned private IP addresses**, choose the number of secondary IPv4 addresses that you want AWS assign to this private NAT gateway. You can choose up to 7 IPv4 addresses.
**Note**  
Secondary IPv4 addresses are optional and should be assigned or allocated when your workloads that use a NAT gateway exceed 55,000 concurrent connections to a single destination (the same destination IP, destination port, and protocol). Secondary IPv4 addresses increase the number of available ports, and therefore they increase the limit on the number of concurrent connections that your workloads can establish using a NAT gateway.

1. If you chose **Auto-assign** in Step 9, skip this step. If you chose **Custom**, do the following:

   1. Under **Primary private IPv4 address**, enter a private IPv4 address.

   1. Under **Secondary private IPv4 address**, enter up to 7 secondary private IPv4 addresses.

1. (Optional) To add a tag to the NAT gateway, choose **Add new tag** and enter the key name and value. You can add up to 50 tags.

1. Choose **Create a NAT gateway**.

1. The initial status of the NAT gateway is `Pending`. After the status changes to `Available`, the NAT gateway is ready for you to use. Be sure to update your route tables as needed. For examples, see [NAT gateway use cases](nat-gateway-scenarios.md).

If the status of the NAT gateway changes to `Failed`, there was an error during creation. For more information, see [NAT gateway creation fails](nat-gateway-troubleshooting.md#nat-gateway-troubleshooting-failed).

## Edit secondary IP address associations
<a name="nat-gateway-edit-secondary"></a>

Each IPv4 address can support up to 55,000 simultaneous connections to each unique destination. A unique destination is identified by a unique combination of destination IP address, the destination port, and protocol (TCP/UDP/ICMP). You can increase this limit by associating up to 8 IPv4 addresses to your NAT gateways (1 primary IPv4 address and 7 secondary IPv4 addresses). You are limited to associating 2 Elastic IP addresses to your public NAT gateway by default. You can increase this limit by requesting a quota adjustment. For more information, see [Elastic IP addresses](amazon-vpc-limits.md#vpc-limits-eips).

You can use the [NAT gateway CloudWatch metrics](metrics-dimensions-nat-gateway.md) *ErrorPortAllocation* and *PacketsDropCount* to determine if your NAT gateway is generating port allocation errors or dropping packets. To resolve this issue, add secondary IPv4 addresses to your NAT gateway.

**Considerations**
+ You can add secondary private IPv4 addresses when you create a private NAT gateway or after you create the NAT gateway using the procedure in this section. You can add Elastic IP addresses to public NAT gateways only after you create the NAT gateway by using the procedure in this section. 
+ Your NAT gateway can have up to 8 IPv4 addresses associated with it (1 primary IPv4 address and 7 secondary IPv4 addresses). You can assign up to 8 private IPv4 addresses to your private NAT gateway. You are limited to associating 2 Elastic IP addresses to your public NAT gateway by default. You can increase this limit by requesting a quota adjustment. For more information, see [Elastic IP addresses](amazon-vpc-limits.md#vpc-limits-eips).

**To edit secondary IPv4 address associations**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **NAT gateways**.

1. Select the NAT gateway whose secondary IPv4 address associations you want to edit.

1. Choose **Actions**, and then choose **Edit secondary IP address associations**.

1. If you are editing the secondary IPv4 address associations of a private NAT gateway, under **Action**, choose **Assign new IPv4 addresses** or **Unassign existing IPv4 addresses**. If you are editing the secondary IPv4 address associations of a public NAT gateway, under **Action**, choose **Associate new IPv4 addresses** or **Disassociate existing IPv4 addresses**.

1. Do one of the following:
   + If you chose to assign or associate new IPv4 addresses, do the following:

     1. This step is required. You must select a private IPv4 address. Choose the **Private IPv4 address assigning method**:
        + **Auto-assign**: AWS automatically chooses a primary private IPv4 address and you choose if you want AWS to assign up to 7 secondary private IPv4 addresses to assign to the NAT gateway. AWS automatically chooses and assigns them for you at random from the subnet that your NAT gateway is in.
        + **Custom**: Choose the primary private IPv4 address and up to 7 secondary private IPv4 addresses to assign to the NAT gateway.

     1. Under **Elastic IP allocation ID**, choose an Elastic IP address to add with a secondary IPv4 address. This step is required. You must select an Elastic IP address along with a private IPv4 address. If you chose **Custom** for the **Private IP address assigning method**, you also must enter a private IPv4 address for each Elastic IP address that you add.
**Important**  
When you assign a secondary EIP to a public NAT gateway, the network border group of the EIP must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. If it's not the same, the EIP will fail to assign. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information, see [1. Allocate an Elastic IP address](WorkWithEIPs.md#allocate-eip). 

     Your NAT gateway can have up to 8 IP addresses associated with it. If this is a public NAT gateway, there is a default quota limit for Elastic IP addresses per Region. For more information, see [Elastic IP addresses](amazon-vpc-limits.md#vpc-limits-eips).
   + If you chose to unassign or disassociate new IPv4 addresses, complete the following:

     1. Under **Existing secondary IP address to unassign**, select the secondary IP addresses that you want to unassign.

     1. (optional) Under **Connection drain duration**, enter the maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. If you don't enter a value, the default value is 350 seconds.

1. Choose **Save changes**.

If the status of the NAT gateway changes to `Failed`, there was an error during creation. For more information, see [NAT gateway creation fails](nat-gateway-troubleshooting.md#nat-gateway-troubleshooting-failed).

## Tag a NAT gateway
<a name="nat-gateway-tagging"></a>

You can tag your NAT gateway to help you identify it or categorize it according to your organization's needs. For information about working with tags, see [Tagging your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

Cost allocation tags are supported for NAT gateways. Therefore, you can also use tags to organize your AWS bill and reflect your own cost structure. For more information, see [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*. For more information about setting up a cost allocation report with tags, see [Monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html) in *About AWS Account Billing*. 

**To tag a NAT gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **NAT gateways**.

1. Select the NAT gateway that you want to tag and choose **Actions**. Then choose **Manage tags**.

1. Choose **Add new tag**, and define a **Key** and **Value** for the tag. You can add up to 50 tags.

1. Choose **Save**.

## Delete a NAT gateway
<a name="nat-gateway-deleting"></a>

If you no longer need a NAT gateway, you can delete it. After you delete a NAT gateway, its entry remains visible in the Amazon VPC console for about an hour, after which it's automatically removed. You can't remove this entry yourself.

Deleting a NAT gateway disassociates its Elastic IP address, but does not release the address from your account. If you delete a NAT gateway, the NAT gateway routes remain in a `blackhole` status until you delete or update the routes.

**To delete a NAT gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **NAT gateways**.

1. Select the radio button for the NAT gateway, and then choose **Actions**, **Delete NAT gateway**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

1. If you no longer need the Elastic IP address that was associated with a public NAT gateway, we recommend that you release it. For more information, see [5. Release an Elastic IP address](WorkWithEIPs.md#release-eip).

## Command line overview
<a name="nat-gateway-api-cli"></a>

You can perform the tasks described on this page using the command line.

**Assign a private IPv4 address to a private NAT gateway**
+ [assign-private-nat-gateway-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/assign-private-nat-gateway-address.html) (AWS CLI)
+ [Register-EC2PrivateNatGatewayAddress](https://docs.aws.amazon.com/powershell/latest/reference/items/Register-EC2PrivateNatGatewayAddress.html) (AWS Tools for Windows PowerShell)

**Associate Elastic IP addresses and private IPv4 addresses with a public NAT gateway**
+ [associate-nat-gateway-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-nat-gateway-address.html) (AWS CLI)
+ [Register-EC2NatGatewayAddress](https://docs.aws.amazon.com/powershell/latest/reference/items/Register-EC2NatGatewayAddress.html) (AWS Tools for Windows PowerShell)

**Create a NAT gateway**
+ [create-nat-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-nat-gateway.html) (AWS CLI)
+ [New-EC2NatGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2NatGateway.html) (AWS Tools for Windows PowerShell)

**Delete a NAT gateway**
+ [delete-nat-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-nat-gateway.html) (AWS CLI)
+ [Remove-EC2NatGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2NatGateway.html) (AWS Tools for Windows PowerShell)

**Describe a NAT gateway**
+ [describe-nat-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-nat-gateways.html) (AWS CLI)
+ [Get-EC2NatGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2NatGateway.html) (AWS Tools for Windows PowerShell)

**Disassociate secondary Elastic IP addresses from a public NAT gateway**
+ [disassociate-nat-gateway-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-nat-gateway-address.html) (AWS CLI)
+ [Unregister-EC2NatGatewayAddress](https://docs.aws.amazon.com/powershell/latest/reference/items/Unregister-EC2NatGatewayAddress.html) (AWS Tools for Windows PowerShell)

**Tag a NAT gateway**
+ [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) (AWS CLI)
+ [New-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Tag.html) (AWS Tools for Windows PowerShell)

**Unassign secondary IPv4 addresses from a private NAT gateway**
+ [unassign-private-nat-gateway-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/unassign-private-nat-gateway-address.html) (AWS CLI)
+ [Unregister-EC2PrivateNatGatewayAddress](https://docs.aws.amazon.com/powershell/latest/reference/items/Unregister-EC2PrivateNatGatewayAddress.html) (AWS Tools for Windows PowerShell)