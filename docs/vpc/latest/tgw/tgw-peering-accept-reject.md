

# Accept or reject a peering attachment request in AWS Transit Gateway
<a name="tgw-peering-accept-reject"></a>

When created, a transit gateway peering attachment is automatically created in a `pendingAcceptance` state and remains in this state indefinitely until it's either accepted or rejected. To activate the peering attachment, the owner of the accepter transit gateway must accept the peering attachment request, even if both transit gateways are in the same account. Accept the peering attachment request from the Region that the accepter transit gateway is located in. Alternatively, if you reject the peering attachment, you must reject the request from the Region that the accepter transit gateway is located in.

**To accept a peering attachment request using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the transit gateway peering attachment that's pending acceptance.

1. Choose **Actions**, **Accept transit gateway attachment**.

1. Add the static route to the transit gateway route table. For more information, see [Create a static route in AWS Transit Gateway](tgw-create-static-route.md).

**To reject a peering attachment request using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the transit gateway peering attachment that's pending acceptance.

1. Choose **Actions**, **Reject transit gateway attachment**.

**To accept or reject a peering attachment using the AWS CLI**  
Use the [accept-transit-gateway-peering-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/accept-transit-gateway-peering-attachment.html) and [reject-transit-gateway-peering-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/reject-transit-gateway-peering-attachment.html) commands.