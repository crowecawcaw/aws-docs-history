

# Create a Connect peer in AWS Transit Gateway
<a name="create-tgw-connect-peer"></a>

You can create a Connect peer (GRE tunnel) for an existing Connect attachment. Before you begin, ensure that you have configured a transit gateway CIDR block. You can configure a transit gateway CIDR block when you [create](create-tgw.md) or [modify](tgw-modifying.md) a transit gateway. 

When you create the Connect peer, you must specify the GRE outer IP address on the appliance side of the Connect peer.

**To create a Connect peer using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the Connect attachment, and choose **Actions**, **Create connect peer**.

1. (Optional) For **Name tag**, specify a name tag for the Connect peer.

1. (Optional) For **Transit gateway GRE Address**, specify the GRE outer IP address for the transit gateway. By default, the first available address from the transit gateway CIDR block is used.

1. For **Peer GRE address**, specify the GRE outer IP address for the appliance side of the Connect peer.

1. For **BGP Inside CIDR blocks IPv4**, specify the range of inside IPv4 addresses that are used for BGP peering. Specify a /29 CIDR block from the `169.254.0.0/16` range.

1. (Optional) For **BGP Inside CIDR blocks IPv6**, specify the range of inside IPv6 addresses that are used for BGP peering. Specify a /125 CIDR block from the `fd00::/8` range.

1. (Optional) For **Peer ASN**, specify the Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. You can use an existing ASN assigned to your network. If you do not have one, you can use a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range. 

   The default is the same ASN as the transit gateway. If you configure the **Peer ASN** to be different than the transit gateway ASN (eBGP), you must configure ebgp-multihop with a time-to-live (TTL) value of 2.

1. Choose **Create connect peer**.

**To create a Connect peer using the AWS CLI**  
Use the [create-transit-gateway-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-connect-peer.html) command.