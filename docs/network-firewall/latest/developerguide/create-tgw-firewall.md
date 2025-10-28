# Create a transit gateway-attached firewall from a shared transit gateway

The process to create a transit gateway-attached firewall involves multiple AWS services, including AWS Network Firewall, AWS Transit Gateway, and AWS RAM. In scenarios where
the Transit Gateway owner and Network Firewall owner are different AWS accounts, the Network Firewall account owner depends on the Transit Gateway owner to share a
transit gateway with them.

###### Note

_This_ guide focuses on the Network Firewall portions of the larger cross-service process and assumes you are an AWS Network Firewall account
owner who has a transit gateway shared with them.
For information on creating a transit gateway-attached firewall without needing to share between different AWS accounts,
see [Creating a firewall in AWS Network Firewall](creating-firewall.md "creating-firewall.md").

The following procedure is an overview of all the service-specific processes needed to create transit gateway-attached firewall.
For more detailed instructions specific to Transit Gateway and AWS RAM, see the related service documentation linked in each respective step.

1. The transit gateway owner shares their transit gateway through AWS RAM with the firewall owner's account.
   For more information, see
   [Shareable AWS resources](../../../ram/latest/userguide/shareable.md#shareable-vpc "../../../ram/latest/userguide/shareable.md#shareable-vpc") in the
   _AWS RAM User Guide_.
2. The firewall owner accepts the AWS RAM share invitation for the transit gateway. For more information,
   see [Access shared resources](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md")
   in the _AWS RAM User Guide_.
3. The firewall owner creates a firewall using the shared transit gateway, which creates a pending
   transit gateway attachment. For detailed steps, see [Accept a shared transit gateway to create a transit gateway-attached firewall](#accept-shared-tgw-firewall "#accept-shared-tgw-firewall").

###### Note

This step in the process is covered in this guide. 4. The transit gateway owner accepts the transit gateway attachment (unless auto-accept attachments is enabled
on their transit gateway). For more information, see [Accept a shared attachment using Amazon VPC Transit Gateways](../../../vpc/latest/tgw/acccept-tgw-attach.md "../../../vpc/latest/tgw/acccept-tgw-attach.md") in
the _Amazon VPC Developer Guide_.

## Accept a shared transit gateway to create a transit gateway-attached firewall

###### Prerequisites

Verify that the Transit Gateway account owner has already created a transit gateway and shared it with your account using AWS RAM.

For information on other things to consider before you create a transit gateway-attached firewall, see [Considerations for transit gateway-attached firewalls](tgw-firewall-considerations.md "tgw-firewall-considerations.md")

###### To accept a shared transit gateway in Network Firewall

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. From the **Actions** menu, choose **Accept the transit gateway attachment**.
4. Review the following details in the dialog box:
   - The firewall name
   - Status (whether it has been accepted by this account)
   - Account ID of the firewall owner
   - Transit Gateway ID

5. Choose **Accept**.
6. Review the firewall configuration details, then choose **Create firewall**.

###### After you accept a shared transit gateway attachment

The steps in this guide are only part of a larger process that involves AWS Network Firewall, AWS Transit Gateway, and AWS RAM.
When a you complete the previous steps within the Network Firewall console, the transit gateway-attached firewall enters a `Pending` state.
You can proceed to [Working with transit gateway-attached firewalls](working-with-tgw-firewalls.md "working-with-tgw-firewalls.md") to begin
configuring your transit gateway-attached firewall while you wait for the transit gateway owner to accept or reject it.
