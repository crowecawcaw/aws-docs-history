

# Accept or reject a Client VPN attachment in AWS Transit Gateway
<a name="accept-reject-client-vpn-attachment"></a>

If a Client VPN endpoint in another account creates an attachment to your transit gateway, you must accept or reject the attachment request before traffic can flow.

**To accept or reject a Client VPN attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit gateways**.

1. Choose **Transit gateway attachments**.

1. Select the attachment with a state of **Pending acceptance** and a type of **Client VPN**.

1. Choose **Actions**, and then choose either **Accept attachment** or **Reject attachment**.

1. In the confirmation dialog box, choose **Accept** or **Reject**.

If you accept the attachment, it becomes active and AWS Transit Gateway will begin processing traffic to and from the Client VPN endpoint. If you reject the attachment, it enters a rejected state and will eventually be deleted.

**To accept a Client VPN attachment using the AWS CLI**  
Use the [accept-transit-gateway-client-vpn-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/accept-transit-gateway-client-vpn-attachment.html) command.

**To reject a Client VPN attachment using the AWS CLI**  
Use the [reject-transit-gateway-client-vpn-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/reject-transit-gateway-client-vpn-attachment.html) command.