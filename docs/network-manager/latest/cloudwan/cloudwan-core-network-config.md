# Configure the core network settings in an AWS Cloud WAN policy

version

The following steps guide you through configuring a core network for a policy version
using the **Policy versions** link on the AWS Network Manager console. For more
information about a core network in a policy version, see [Network configuration](cloudwan-create-policy-version.md#cloudwan-policy-config "cloudwan-create-policy-version.md#cloudwan-policy-config").

###### To configure network for a policy version

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. In **Choose policy view mode**, choose **Visual
   editor**.
7. The **Network configuration** displays general settings for the
   policy.
8. In **General settings,** choose **Edit**.
   1. The **Version** choose any of the following:
      - **2021.12** this version does not support routing policies or bgp community tag propagation through your core network
      - **2025.11** this version enables support for routing policies and bgp community tag propagation through your core network

   2. Choose any of the following:
      - **VPN ECMP support** if the core network should
        forward traffic over multiple-cost routes using VPN.
      - **DNS support** if you want to use DNS resolution
        for the core network.
      - **Security Group Referencing support** if you
        want to enable security group referencing for VPC attachments in the
        core network. For more information about security group referencing,
        see [Security group referencing](cloudwan-vpc-attachment.md#cloudwan-sg-referencing "cloudwan-vpc-attachment.md#cloudwan-sg-referencing").

   3. Choose **Edit general settings**.

9. In the **ASN ranges** section, do the following:
   1. Choose **Create**.
   2. For **ASN range**, enter the ASN range for the policy
      version. For example, enter `64512-65334`.

   ###### Note

   The **ASN range** is left-closed and right-open. This
   means that the leftmost number is included in the range but the rightmost
   number is not. For example, if you choose an ASN range of
   `64900-64903`, the actual available ASN range is
   `64900` through `64902`.
   `64903` is not included. 3. Choose **Create ASN range**.

10. In the **Inside CIDR blocks** section, do the following:
    1. Choose **Create**.
    2. For **CIDR**, enter the CIDR block that you want to use
       for BGP peering on Connect peers.
    3. Choose **Create inside CIDR block**.

11. In the **Edge locations** section, do the following:
    1. Choose **Create**.
    2. From the **Location** dropdown list, choose the
       **Region** where you want the Core Network Edge router
       to be created. You can choose only one Region.
    3. For **ASN**, enter the ASN number for the Region.

    ###### Note

    You can't change the ASN of a core network edge. Any transit gateway with the same ASN can't be peered to that core network edge. For example, if you have a core network edge with an ASN of `64512`, you can't peer any transit gateway that also has an ASN of `64512`. 4. For **Inside CIDR block**, enter the CIDR block that you
    want to use for BGP peering on Connect peers. You can enter multiple CIDR
    blocks by choosing **Add** for each block that you want to
    add. Choose **Remove** for any block that you don't
    want.

    ###### Note

    You can't leave any blank destination CIDR blocks. Choose
    **Remove** to delete any empty blocks. 5. Choose **Create edge locations**.
