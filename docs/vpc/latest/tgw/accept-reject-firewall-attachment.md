

# Accept or reject an AWS Transit Gateway network function attachment

How you accept or reject a network function attachment depends on its type.

## Accept or reject an AWS Network Firewall network function attachment
<a name="accept-reject-nf-attachment-nfw-console"></a>

An AWS Network Firewall owner can create a network function attachment to a transit gateway in another account. The transit gateway owner must then accept or reject the attachment. Use the Amazon VPC console or the `AcceptNetworkFirewallTransitGatewayAttachment` and `RejectNetworkFirewallTransitGatewayAttachment` APIs in the [*AWS Network Firewall API Reference*](https://docs.aws.amazon.com/network-firewall/latest/APIReference/Welcome.html).

**To accept or reject an AWS Network Firewall network function attachment using the console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#TransitGatewayAttachments).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway attachments**.

1. Select the attachment with a state of **Pending acceptance** and a type of **Network function**.

1. Choose **Actions**, and then choose **Accept attachment** or **Reject attachment**.

1. In the confirmation dialog box, choose **Accept** or **Reject**.

If you accept the attachment, it becomes active and the firewall can inspect traffic. If you reject it, the attachment enters the `rejected` state and is eventually deleted.

## Accept or reject a network function attachment of type Gateway Load Balancer
<a name="accept-reject-nf-attachment-gwlb-console"></a>

A network function attachment of type Gateway Load Balancer connects through a Gateway Load Balancer VPC endpoint service. If the endpoint service requires acceptance, the endpoint service owner accepts or rejects the endpoint connection. You don't need to take action when automatic acceptance is enabled.

**To accept or reject the endpoint connection using the console**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#EndpointServices).

1. In the navigation pane, choose **Endpoint services**.

1. Choose the endpoint service that fronts the firewall deployment.

1. Choose the **Endpoint connections** tab.

1. Select all pending endpoint connections identified by the transit gateway attachment ID.

1. Choose **Actions**, and then choose **Accept endpoint connection request** or **Reject endpoint connection request**.

1. When prompted for confirmation, enter **accept** and choose **Accept**, or enter **reject** and choose **Reject**.

For the AWS CLI, use `accept-vpc-endpoint-connections` or `reject-vpc-endpoint-connections` with `--service-id` and `--transit-gateway-attachment-ids`. For more information, see [Accept or reject connection requests](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html#accept-reject-connection-requests) in the *AWS PrivateLink Guide*.