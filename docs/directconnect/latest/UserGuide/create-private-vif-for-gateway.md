# Create a private virtual

interface to the Direct Connect gateway

To connect your Direct Connect connection to the remote VPC, you must create a private
virtual interface for your connection. Specify the Direct Connect gateway to which
to connect. You can create a private virtual interface using either the Direct Connect console or using the command line or API.

###### Note

If you're accepting a hosted private virtual interface, you can associate it
with a Direct Connect gateway in your account. For more information, see [Accept a hosted virtual interface](accepthostedvirtualinterface.md "accepthostedvirtualinterface.md").

###### To provision a private virtual interface to a Direct Connect gateway

1.  Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
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

    The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](long-asn-support.md "long-asn-support.md").

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
    assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses. 2. To change the maximum transmission unit (MTU) from 1500 (default) to 9001 (jumbo frames), select
    **Jumbo MTU (MTU size 9001)**. 3. (Optional) Under **Enable SiteLink**, choose **Enabled** to enable direct connectivity between Direct Connect points of presence. 4. (Optional) Add or remove a tag.

    [Add a tag] Choose **Add tag** and do the following:

        * For **Key**, enter the key name.
        * For **Value**, enter the key value.

    [Remove a tag] Next to the tag, choose **Remove tag**.

7.  Choose **Create virtual interface**.
    After you've created the virtual interface, you can download the router
    configuration for your device. For more information, see [Download the router configuration file](vif-router-config.md "vif-router-config.md").

###### To create a private virtual interface using the command line or API

- [create-private-virtual-interface](../../../cli/latest/reference/directconnect/create-private-virtual-interface.md "../../../cli/latest/reference/directconnect/create-private-virtual-interface.md")
  (AWS CLI)
- [CreatePrivateVirtualInterface](../APIReference/API_CreatePrivateVirtualInterface.md "../APIReference/API_CreatePrivateVirtualInterface.md") (Direct Connect
  API)

###### To view the virtual interfaces that are attached to a Direct Connect gateway

using the command line or API

- [describe-direct-connect-gateway-attachments](../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-attachments.md "../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-attachments.md")
  (AWS CLI)
- [DescribeDirectConnectGatewayAttachments](../APIReference/API_DescribeDirectConnectGatewayAttachments.md "../APIReference/API_DescribeDirectConnectGatewayAttachments.md")
  (Direct Connect API)
