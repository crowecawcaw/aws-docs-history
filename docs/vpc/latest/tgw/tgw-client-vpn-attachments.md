

# Client VPN attachments in AWS Transit Gateway
<a name="tgw-client-vpn-attachments"></a>

When you associate a Client VPN endpoint with a transit gateway, a Client VPN attachment is automatically created, allowing you to route traffic between your VPCs, on-premises networks, and Client VPN endpoints. AWS Transit Gateway supports cross-account Client VPN attachments, allowing accounts that the transit gateway is shared with to create their own Client VPN attachments.

After the Client VPN endpoint is associated with a transit gateway, you can view the attachment in the Transit Gateway console under **Transit gateway attachments**. The attachment will be listed with a type of **Client VPN**.

**Requirements and limitations**
+ Your transit gateway must have an assigned IPv4 or IPv6 CIDR block before you can create a Client VPN attachment.
+ Route table propagation must be enabled for Client VPN attachments to allow traffic between your Client VPN endpoint and transit gateway. See [Enable route propagation](https://docs.aws.amazon.com/vpc/latest/tgw/enable-tgw-route-propagation.html).

**Topics**
+ [Create a Client VPN attachment](create-client-vpn-attachment.md)
+ [View a Client VPN attachment](view-client-vpn-attachment.md)
+ [Delete a Client VPN attachment](delete-client-vpn-attachment.md)
+ [Accept or reject a Client VPN attachment](accept-reject-client-vpn-attachment.md)