# Accept or reject an AWS Transit Gateway network

function attachment

You can use either the Amazon VPC console or the AWS Network Firewall CLI or API to accept or reject a
transit gateway network function attachment, including Network Firewall attachments. If you are the owner
of a transit gateway and someone has created a firewall attachment to your transit gateway from
another account, you need to accept or reject the attachment request.

To accept or reject a network function attachment using the Network Firewall CLI, see the
`AcceptNetworkFirewallTransitGatewayAttachment` or
`RejectNetworkFirewallTransitGatewayAttachment` APIs in the [_AWS Network Firewall API Reference_](../../../network-firewall/latest/APIReference/Welcome.md "../../../network-firewall/latest/APIReference/Welcome.md").

## Accept or reject a network function

attachment using the console

Use the Amazon VPC console to accept or reject a transit gateway network function
attachment.

###### To accept or reject a network function attachment using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateways**.
3. Choose **Transit gateway attachments**.
4. Select the attachment with a state of **Pending acceptance** and a type of **Network function**.
5. Choose **Actions**, and then choose either **Accept attachment** or **Reject attachment**.
6. In the confirmation dialog box, choose **Accept** or **Reject**.

If you accept the attachment, it becomes active and the firewall can inspect traffic. If you reject the attachment, it enters a rejected state and will eventually be deleted.
