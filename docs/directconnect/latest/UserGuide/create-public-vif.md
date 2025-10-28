# Create an AWS Direct Connect public virtual interface

When you create a public virtual interface, it can take up to 72 business hours for us to
review and approve your request.

###### To provision a public virtual interface

1.  Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  In the navigation pane, choose **Virtual Interfaces**.
3.  Choose **Create virtual interface**.
4.  Under **Virtual interface type**, for
    **Type**, choose **Public**.
5.  Under **Public virtual interface settings**, do the
    following:
    1. For **Virtual interface name**, enter a name for
       the virtual interface.
    2. For **Connection**, choose the Direct Connect
       connection that you want to use for this interface.
    3. For **VLAN**, enter the ID number for your
       virtual local area network (VLAN).
    4. For **BGP ASN**, enter the Border Gateway Protocol
       Autonomous System Number (ASN) of your on-premises peer router for the new
       virtual interface.

    The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483647) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in AWS Direct Connect](long-asn-support.md "long-asn-support.md").

    ###### Note

    When establishing a BGP peering session with AWS over a public
    virtual interface, use `7224` as the ASN to establish
    the BGP session on the AWS side. The ASN on your router or customer
    gateway device should be different from that ASN.

6.  Under **Additional settings**, do the following:
    1. To configure an IPv4 BGP or an IPv6 peer, do the following:

    [IPv4] To configure an IPv4 BGP peer, choose
    **IPv4** and do one of the following:

        * To specify these IP addresses yourself, for **Your
         router peer ip**, enter the destination IPv4
         CIDR address to which Amazon should send traffic.
        * For **Amazon router peer IP**, enter the
         IPv4 CIDR address to use to send traffic to AWS.

    [IPv6] To configure an IPv6 BGP peer, choose
    **IPv6**. The peer IPv6 addresses are
    automatically assigned from Amazon's pool of IPv6 addresses.
    You cannot specify custom IPv6 addresses. 2. To provide your own BGP key, enter your BGP MD5 key.

    If you do not enter a value, we generate a BGP key. If you provided your own key, or if
    we generated the key for you, that value displays in the
    **BGP authentication key** column on the
    virtual interface details page of **Virtual
    interfaces**. 3. To advertise prefixes to Amazon, for **Prefixes you want
    to advertise**, enter the IPv4 CIDR destination
    addresses (separated by commas) to which traffic should be routed
    over the virtual interface.

    ###### Important

    You may add additional prefixes to an existing public VIF and advertise those by
    contacting [AWS
    support](https://aws.amazon.com/support/createCase "https://aws.amazon.com/support/createCase"). In your support case, provide a list of
    additional CIDR prefixes you want to add to the public VIF and
    advertise. 4. (Optional) Add or remove a tag.

    [Add a tag] Choose **Add tag** and do the
    following:

        * For **Key**, enter the key name.
        * For **Value**, enter the key
         value.

    [Remove a tag] Next to the tag, choose **Remove
    tag**.

7.  Choose **Create virtual interface**.
8.  Download the router configuration for your device. For more information,
    see [Download the router configuration file](vif-router-config.md "vif-router-config.md").

###### To create a public virtual interface using the command line or API

- [create-public-virtual-interface](../../../cli/latest/reference/directconnect/create-public-virtual-interface.md "../../../cli/latest/reference/directconnect/create-public-virtual-interface.md") (AWS CLI)
- [CreatePublicVirtualInterface](../APIReference/API_CreatePublicVirtualInterface.md "../APIReference/API_CreatePublicVirtualInterface.md") (AWS Direct Connect API)
