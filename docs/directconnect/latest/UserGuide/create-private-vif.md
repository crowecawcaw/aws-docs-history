# Create an AWS Direct Connect private virtual interface

You can provision a private virtual interface to a virtual private gateway in the
same Region as your AWS Direct Connect connection. For more information about provisioning a
private virtual interface to an AWS Direct Connect gateway, see [AWS Direct Connect gateways](direct-connect-gateways.md "direct-connect-gateways.md").

If you use the VPC wizard to create a VPC, route propagation is automatically
enabled for you. With route propagation, routes are automatically populated to the
route tables in your VPC. If you choose, you can disable route propagation. For more
information, see [Enable Route
Propagation in Your Route Table](../../../vpc/latest/userguide/SetUpVPNConnections.md#vpn-configure-routing "../../../vpc/latest/userguide/SetUpVPNConnections.md#vpn-configure-routing") in the
_Amazon VPC User Guide_.

The maximum transmission unit (MTU) of a network connection is the size, in bytes,
of the largest permissible packet that can be passed over the connection. The MTU of
a private virtual interface can be either 1500 or 9001 (jumbo frames). The MTU of a
transit virtual interface can be either 1500 or 8500 (jumbo frames). You can specify
the MTU when you create the interface or update it after you create it. Setting the
MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause
an update to the underlying physical connection if it wasn't updated to support
jumbo frames. Updating the connection disrupts network connectivity for all virtual
interfaces associated with the connection for up to 30 seconds. To check whether a
connection or virtual interface supports jumbo frames, select it in the AWS Direct Connect
console and find **Jumbo Frame Capable** on the
**Summary** tab.

###### To provision a private virtual interface to a VPC

1.  Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  In the navigation pane, choose **Virtual Interfaces**.
3.  Choose **Create virtual interface**.
4.  Under **Virtual interface type**, choose **Private**.
5.  Under **Private virtual interface settings**, do the following:
    1. For **Virtual interface name**, enter a name for the virtual interface.
    2. For **Connection**, choose the Direct Connect connection that you want to use for this interface.
    3. For **Virtual interface owner**, choose **My AWS account** if the virtual interface is for your AWS account.
    4. For **Direct Connect gateway**, select the Direct Connect gateway.
    5. For **VLAN**, enter the ID number for your virtual
       local area network (VLAN).
    6. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System Number of your on-premises peer router for the new virtual interface.

    The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in AWS Direct Connect](long-asn-support.md "long-asn-support.md").

6.  Under **Additional Settings**, do the following:
    1. To configure an IPv4 BGP or an IPv6 peer, do the following:

    [IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of
    the following:

        * To specify these IP addresses yourself, for **Your router peer ip**,
         enter the destination IPv4 CIDR address to which Amazon
         should send traffic.
        * For **Amazon router peer ip**, enter
         the IPv4 CIDR address to use to send traffic to
         AWS.


        ###### Important

        When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.



        	+ For more information about RFC 1918, see
        	 [Address Allocation for Private
        	 Internets](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918").
        	+ For more information about RFC 3927, see
        	 [Dynamic Configuration of IPv4 Link-Local
        	 Addresses](https://datatracker.ietf.org/doc/html/rfc3927 "https://datatracker.ietf.org/doc/html/rfc3927").

    [IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically
    assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses. 2. To change the maximum transmission unit (MTU) from 1500 (default) to 8500
    (jumbo frames), select **Jumbo MTU (MTU size 8500)**. 3. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence. 4. (Optional) Add or remove a tag.

    [Add a tag] Choose **Add tag** and do the following:

        * For **Key**, enter the key name.
        * For **Value**, enter the key value.

    [Remove a tag] Next to the tag, choose **Remove tag**.

7.  Choose **Create virtual interface**.
8.  Download the router configuration for your device. For more information,
    see [Download the router configuration file](vif-router-config.md "vif-router-config.md").

###### To create a private virtual interface using the command line or API

- [create-private-virtual-interface](../../../cli/latest/reference/directconnect/create-private-virtual-interface.md "../../../cli/latest/reference/directconnect/create-private-virtual-interface.md") (AWS CLI)
- [CreatePrivateVirtualInterface](../APIReference/API_CreatePrivateVirtualInterface.md "../APIReference/API_CreatePrivateVirtualInterface.md") (AWS Direct Connect API)
