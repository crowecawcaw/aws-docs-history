# Create an Direct Connect hosted transit virtual interface

###### To create a hosted transit virtual interface

###### Important

If you associate your transit gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the transit gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both the transit gateway and the Direct Connect gateway, the association request fails.

1.  Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  In the navigation pane, choose **Virtual Interfaces**.
3.  Choose **Create virtual interface**.
4.  Under **Virtual interface type**, for
    **Type**, choose **Transit**.
5.  Under **Transit virtual interface settings**, do the
    following:
    1. For **Virtual interface name**, enter a name for
       the virtual interface.
    2. For **Connection**, choose the Direct Connect
       connection that you want to use for this interface.
    3. For **Virtual interface owner**, choose
       **Another AWS account**, and then for
       **Virtual interface owner**, enter the ID of
       the account to own this virtual interface.
    4. For **VLAN**, enter the ID number for your
       virtual local area network (VLAN).
    5. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System
       Number of your on-premises peer router for the new virtual
       interface.

    The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](long-asn-support.md "long-asn-support.md").

6.  Under **Additional Settings**, do the following:
    1. To configure an IPv4 BGP or an IPv6 peer, do the following:

    [IPv4] To configure an IPv4 BGP peer, choose
    **IPv4** and do one of the following:

        * To specify these IP addresses yourself, for **Your
         router peer ip**, enter the destination IPv4
         CIDR address to which Amazon should send traffic.
        * For **Amazon router peer ip**, enter the
         IPv4 CIDR address to use to send traffic to AWS.


        ###### Important

        When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.



        	+ For more information about RFC 1918, see
        	 [Address Allocation for Private
        	 Internets](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918").
        	+ For more information about RFC 3927, see
        	 [Dynamic Configuration of IPv4 Link-Local
        	 Addresses](https://datatracker.ietf.org/doc/html/rfc3927 "https://datatracker.ietf.org/doc/html/rfc3927").

    [IPv6] To configure an IPv6 BGP peer, choose
    **IPv6**. The peer IPv6 addresses are
    automatically assigned from Amazon's pool of IPv6 addresses.
    You cannot specify custom IPv6 addresses. 2. To change the maximum transmission unit (MTU) from 1500 (default)
    to 8500 (jumbo frames), select **Jumbo MTU (MTU size 8500)**. 3. [Optional] Add a tag. Do the following:

    [Add a tag] Choose **Add tag** and do the
    following:

        * For **Key**, enter the key name.
        * For **Value**, enter the key
         value.

    [Remove a tag] Next to the tag, choose **Remove
    tag**.

7.  Choose **Create virtual interface**.
8.  After the hosted virtual interface is accepted by the owner of the other
    AWS account, you can download the router configuration file for your device. For more information, see [Download the router configuration file](vif-router-config.md "vif-router-config.md").

###### To create a hosted transit virtual interface using the command line or

API

- [allocate-transit-virtual-interface](../../../cli/latest/reference/directconnect/allocate-public-transit-interface.md "../../../cli/latest/reference/directconnect/allocate-public-transit-interface.md") (AWS CLI)
- [AllocateTransitVirtualInterface](../APIReference/API_AllocateTransitVirtualInterface.md "../APIReference/API_AllocateTransitVirtualInterface.md") (Direct Connect API)
