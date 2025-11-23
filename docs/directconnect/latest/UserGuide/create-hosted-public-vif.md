# Create a hosted public virtual interface in Direct Connect

Before you begin,
ensure that you have read the information in [Prerequisites for virtual interfaces](WorkingWithVirtualInterfaces.md#vif-prerequisites "WorkingWithVirtualInterfaces.md#vif-prerequisites").

###### To create a hosted public virtual interface

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Virtual Interfaces**.
3. Choose **Create virtual interface**.
4. Under **Virtual interface type**, for **Type**, choose **Public**.
5. Under **Public Virtual Interface Settings**, do the following:
   1. For **Virtual interface name**, enter a name for the virtual interface.
   2. For **Connection**, choose the Direct Connect connection that you want to use for this interface.
   3. For **Virtual interface owner**, choose
      **Another AWS account**, and then for
      **Virtual interface owner**, enter the ID of
      the account to own this virtual interface.
   4. For **VLAN**, enter the ID number for your virtual local area network (VLAN).
   5. For **BGP ASN**, enter the Border Gateway Protocol Autonomous System
      Number of your on-premises peer router for the new virtual
      interface.

   The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in Direct Connect](long-asn-support.md "long-asn-support.md").

6. To configure an IPv4 BGP or an IPv6 peer, do the following:

[IPv4] To configure an IPv4 BGP peer, choose **IPv4** and do one of
the following:

    * To specify these IP addresses yourself, for **Your router peer ip**,
     enter the destination IPv4 CIDR address to which Amazon
     should send traffic.
    * For **Amazon router peer ip**, enter
     the IPv4 CIDR address to use to send traffic to AWS.

[IPv6] To configure an IPv6 BGP peer, choose **IPv6**. The peer IPv6 addresses are automatically
assigned from Amazon's pool of IPv6 addresses. You cannot specify custom IPv6 addresses. 7. To advertise prefixes to Amazon, for **Prefixes you want to
advertise**, enter the IPv4 CIDR destination addresses (separated by
commas) to which traffic should be routed over the virtual interface. 8. To provide your own key to authenticate the BGP session, under **Additional Settings**, for **BGP authentication key**, enter the key.

If you do not enter a value, then we generate a BGP key. 9. (Optional) Add or remove a tag.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.[Remove a tag] Next to the tag, choose **Remove tag**.

10. Choose **Create virtual interface**.
11. After the hosted virtual interface is accepted by the owner of the other AWS
    account, you can download the configuration file. For more information, see [Download the router configuration file](vif-router-config.md "vif-router-config.md").

###### To create a hosted public virtual interface using the command line or

API

- [allocate-public-virtual-interface](../../../cli/latest/reference/directconnect/allocate-public-virtual-interface.md "../../../cli/latest/reference/directconnect/allocate-public-virtual-interface.md") (AWS CLI)
- [AllocatePublicVirtualInterface](../APIReference/API_AllocatePublicVirtualInterface.md "../APIReference/API_AllocatePublicVirtualInterface.md") (Direct Connect API)
