

# Create a transit gateway-attached firewall from a shared transit gateway
<a name="create-tgw-firewall"></a>

The process to create a transit gateway-attached firewall involves multiple AWS services, including AWS Network Firewall, AWS Transit Gateway, and AWS RAM. In scenarios where the Transit Gateway owner and Network Firewall owner are different AWS accounts, the Network Firewall account owner depends on the Transit Gateway owner to share a transit gateway with them.

**Note**  
*This* guide focuses on the Network Firewall portions of the larger cross-service process and assumes you are an AWS Network Firewall account owner who has a transit gateway shared with them. For information on creating a transit gateway-attached firewall without needing to share between different AWS accounts, see [Creating a firewall in AWS Network Firewall](creating-firewall.md).

## Use multiple AWS services to create a transit gateway-attached firewall (overview)
<a name="detailed-instructions-tg-ram"></a>

The following procedure is an overview of all the service-specific processes needed to create transit gateway-attached firewall. For more detailed instructions specific to Transit Gateway and AWS RAM, see the related service documentation linked in each respective step. 

1. The transit gateway owner shares their transit gateway through AWS RAM with the firewall owner's account. For more information, see [Shareable AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-vpc) in the *AWS RAM User Guide*.

1. The firewall owner accepts the AWS RAM share invitation for the transit gateway. For more information, see [Access shared resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html) in the *AWS RAM User Guide*.

1. The firewall owner creates a firewall using the shared transit gateway, which creates a pending transit gateway attachment. For detailed steps, see [Accept a shared transit gateway to create a transit gateway-attached firewall](#accept-shared-tgw-firewall).
**Note**  
This step in the process is covered in this guide.

1. The transit gateway owner accepts the transit gateway attachment (unless auto-accept attachments is enabled on their transit gateway). For more information, see [Accept a shared attachment using Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/acccept-tgw-attach.html) in the *Amazon VPC Developer Guide*.

## Accept a shared transit gateway to create a transit gateway-attached firewall
<a name="accept-shared-tgw-firewall"></a>

**Prerequisites**  
Verify that the Transit Gateway account owner has already created a transit gateway and shared it with your account using AWS RAM.

For information on other things to consider before you create a transit gateway-attached firewall, see [Considerations for transit gateway-attached firewalls](tgw-firewall-considerations.md)

**To accept a shared transit gateway in Network Firewall**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. From the **Actions** menu, choose **Accept the transit gateway attachment**.

1. Review the following details in the dialog box:
   + The firewall name
   + Status (whether it has been accepted by this account)
   + Account ID of the firewall owner
   + Transit Gateway ID

1. Choose **Accept**.

1. Review the firewall configuration details, then choose **Create firewall**.

**After you accept a shared transit gateway attachment**  
The steps in this guide are only part of a larger process that involves AWS Network Firewall, AWS Transit Gateway, and AWS RAM. When a you complete the previous steps within the Network Firewall console, the transit gateway-attached firewall enters a `Pending` state. You can proceed to [Working with transit gateway-attached firewalls](working-with-tgw-firewalls.md) to begin configuring your transit gateway-attached firewall while you wait for the transit gateway owner to accept or reject it.