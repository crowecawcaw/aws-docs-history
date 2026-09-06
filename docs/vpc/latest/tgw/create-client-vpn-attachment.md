

# Create a Client VPN attachment in AWS Transit Gateway
<a name="create-client-vpn-attachment"></a>

**Prerequisites**
+ You must have an existing transit gateway in your account.
+ Your transit gateway must have an assigned IPv4 or IPv6 CIDR block.

A Client VPN attachment is automatically created when you associate a Client VPN endpoint with a transit gateway.

**To create a Client VPN attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Client VPN endpoints**.

1. Choose **Create Client VPN endpoint**.

1. Select **Transit Gateway** as the association type and enter the Transit Gateway ID to use.

1. Choose **Create Client VPN endpoint**.

After you create the Client VPN attachment, it appears in the list of attachments with a resource type of **Client VPN** and an initial state of **Pending**. When the attachment is ready, the state changes to **Available**. If the transit gateway is in a different account, the attachment state is **Pending acceptance** until the transit gateway owner accepts it.

For more information about creating Client VPN endpoints, see [Getting Started with AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html).

**To create a Client VPN attachment using the AWS CLI**  
Use the [create-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-endpoint.html) command.