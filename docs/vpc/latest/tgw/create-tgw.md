# Create a transit gateway in AWS Transit Gateway

When you create a transit gateway, we create a default transit gateway route table and use it as the
default association route table and the default propagation route table. If you
choose not to create the default transit gateway route table, you can create one later on. For
more information about routes and route tables, see [Routing](how-transit-gateways-work.md#tgw-routing-overview "how-transit-gateways-work.md#tgw-routing-overview").

###### To create a transit gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit
   Gateways**.
3. Choose **Create transit gateway**.
4. For **Name tag**, optionally enter a name for the transit gateway.
   A name tag can make it easier to identify a specific gateway from the list
   of gateways. When you add a **Name tag**, a tag is created
   with a key of **Name** and with a value equal
   to the value you enter.
5. For **Description**, optionally enter a description for
   the transit gateway.
6. For **Amazon side Autonomous System Number (ASN)**, either leave the default value
   to use the default ASN or enter the private ASN
   for your transit gateway. This should be the ASN for the AWS side of a Border Gateway
   Protocol (BGP) session.

The range is 64512 to 65534 for 16-bit ASNs.

The range is 4200000000 to 4294967294 for 32-bit ASNs.

If you have a multi-Region deployment, we recommend that you use a unique
ASN for each of your transit gateways. 7. For **DNS support**, select this option if you need the VPC to
resolve public IPv4 DNS host names to private IPv4 addresses when queried from
instances in another VPC attached to the transit gateway. 8. For **Security Group Referencing support**, enable this feature
to reference a security group across VPCs attached to a transit gateway. For more
information about security group referencing see [Security group referencing](tgw-vpc-attachments.md#vpc-attachment-security "tgw-vpc-attachments.md#vpc-attachment-security"). 9. For **VPN ECMP support**, select this option if you need Equal Cost Multipath (ECMP)
routing support between VPN tunnels. If connections advertise the same
CIDRs, the traffic is distributed equally between them.

When you select this option, the advertised BGP ASN, then the BGP
attributes such as the AS-path, must be the same.

###### Note

To use ECMP, you must create a VPN connection that uses dynamic routing.
VPN connections that use static routing do not support ECMP. 10. For **Default route table association**, select this option to automatically associate transit gateway attachments
with the default route table for the transit gateway. 11. For **Default route table propagation**, select this option to automatically propagate transit gateway attachments
to the default route table for the transit gateway. 12. (Optional) To use the transit gateway as a router for multicast traffic, select
**Multicast support**. 13. (Optional) In the **Configure-cross-account sharing
options** section, choose whether to **Auto accept
shared attachments**. If enabled, attachments are automatically
accepted. Otherwise, you must accept or reject attachment requests.

For **Auto accept shared attachments**, select this option to automatically accept cross-account
attachments. 14. (Optional) For **Transit gateway CIDR blocks**, specify
one or more IPv4 or IPv6 CIDR blocks for your transit gateway.

You can specify a size /24 CIDR block or larger (for example, /23 or /22)
for IPv4, or a size /64 CIDR block or larger (for example, /63 or /62) for
IPv6. You can associate any public or private IP address range, except for
addresses in the 169.254.0.0/16 range, and ranges that overlap with the
addresses for your VPC attachments and on-premises networks.

###### Note

Transit gateway CIDR blocks are used if you are configuring Connect
(GRE) attachments or PrivateIP VPNs. Transit Gateway assigns IPs for the
Tunnel endpoints (GRE/PrivateIP VPN) from this range. 15. Choose **Create transit gateway**.

###### To create a transit gateway using the AWS CLI

Use the [create-transit-gateway](../../../cli/latest/reference/ec2/create-transit-gateway.md "../../../cli/latest/reference/ec2/create-transit-gateway.md") command.
