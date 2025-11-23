# Getting started with Simple AD

Simple AD creates a fully managed, Samba-based directory in the AWS cloud. When you
create a directory with Simple AD, Directory Service creates two domain controllers and DNS servers on
your behalf. The domain controllers are created in different subnets in an Amazon VPC this redundancy
helps ensures that your directory remains accessible even if a failure occurs.

###### Topics

- [Simple AD prerequisites](#prereq_simple "#prereq_simple")
- [Create your Simple AD](#how_to_create_simple_ad "#how_to_create_simple_ad")
- [What gets created with your Simple AD](simple_ad_what_gets_created.md "simple_ad_what_gets_created.md")

## Simple AD prerequisites

To create a Simple AD Active Directory, you need an Amazon VPC with the following:

- The VPC must have default hardware tenancy.

You can use IPv6 for your VPC. For more information, see [IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in
the _Amazon Virtual Private Cloud User Guide_.

- At least two subnets in two different Availability Zones and must be of same network
  type. The subnets must be in the same Classless Inter-Domain Routing (CIDR) range. If you
  want to extend or resize the VPC for your directory, then make sure to select both of the
  domain controller subnets for the extended VPC CIDR range. When you create a Simple AD,
  Directory Service creates two domain controllers and DNS servers on your behalf.
  - For more information about the CIDR range, see [IP addressing for your VPCs and
    subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the _Amazon VPC User Guide_.

- If you require LDAPS support with Simple AD, we recommend that you configure it
  using a Network Load Balancer connected to port 389. This model enables you to use a
  strong certificate for the LDAPS connection, simplify access to LDAPS through a single NLB
  IP address, and have automatic fail-over through the NLB. Simple AD does not support the
  use of self-signed certificates on port 636. For more information about how to configure
  LDAPS with Simple AD, see [How
  to configure an LDAPS endpoint for Simple AD](https://aws.amazon.com/blogs/security/how-to-configure-ldaps-endpoint-for-simple-ad/ "https://aws.amazon.com/blogs/security/how-to-configure-ldaps-endpoint-for-simple-ad/") in the _AWS Security
  Blog_.
- The following encryption types must be enabled in the directory:
  - RC4_HMAC_MD5
  - AES128_HMAC_SHA1
  - AES256_HMAC_SHA1
  - Future encryption types

  ###### Note

  Disabling these encryption types can cause communication issues with RSAT
  (Remote Server Administration Tools) and impact the availability or your
  directory.

- For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the
  _Amazon VPC User Guide_.

Directory Service uses a two VPC structure. The EC2 instances which make up your directory run outside
of your AWS account, and are managed by AWS. They have two network adapters,
`ETH0` and `ETH1`. `ETH0` is the management adapter, and
exists outside of your account. `ETH1` is created within your account.

The management IP range of your directory's `ETH0` network is chosen
programmatically to ensure it does not conflict with the VPC where your directory is deployed.
This IP range can be in either of the following pairs (as Directories run in two
subnets):

- 10.0.1.0/24 & 10.0.2.0/24
- 169.254.0.0/16
- 192.168.1.0/24 & 192.168.2.0/24

We avoid conflicts by checking the first octet of the `ETH1` CIDR. If it starts
with a 10, then we choose a 192.168.0.0/16 VPC with 192.168.1.0/24 and 192.168.2.0/24 subnets.
If the first octet is anything else other than a 10 we choose a 10.0.0.0/16 VPC with
10.0.1.0/24 and 10.0.2.0/24 subnets.

The selection algorithm does not include routes on your VPC. It is therefore possible to
have an IP routing conflict result from this scenario.

###### Important

If any of the Simple AD prerequisites are altered after your Simple AD is created,
your Simple AD can become **Impaired**. To resolve your Simple AD
**Impaired** status, you will need to contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Create your Simple AD

This procedure walks you through all the necessary steps to create a Simple AD. It is
intended to get you started with Simple AD quickly and easily, but is not intended to be
used in a large-scale production environment.

###### Steps

- [Prerequisites](#gsg_prereqs "#gsg_prereqs")
- [Creating and configuring your Amazon VPC for your
  Simple AD](#gsg_create_vpc "#gsg_create_vpc")
- [Creating your Simple AD](#gsg_create_directory "#gsg_create_directory")

### Prerequisites

This procedure assumes the following:

- You have an active AWS account.
- Your account has not reached its limit of Amazon VPCs for the Region in which you want to
  use Simple AD. For more information about VPC, see [What is Amazon VPC?](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md") and [Subnets in your VPC](../../../vpc/latest/userguide/VPC_Subnets.md#VPCSubnet "../../../vpc/latest/userguide/VPC_Subnets.md#VPCSubnet") in the
  _Amazon VPC User Guide_.
- You do not have an existing VPC in the Region with a CIDR of `10.0.0.0/16`.
- You are in a Region where Simple AD is available. For more information, see [Region availability for Directory Service](regions.md "regions.md").

For more information, see [Simple AD prerequisites](#prereq_simple "#prereq_simple").

### Creating and configuring your Amazon VPC for your

Simple AD

First, you will create and configure an Amazon VPC for use with your Simple AD. Before
starting this procedure, make sure you have completed the [Prerequisites](#gsg_prereqs "#gsg_prereqs").

The VPC you will create will have two public subnets. Directory Service requires two subnets in your
VPC, and each subnet must be in a different Availability Zone.

###### Create a VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the **VPC Dashboard**, choose **Create
   VPC**.
3. Under **VPC settings**, choose **VPC and
   more**.
4. Complete these fields as follows:
   - Keep **Auto-generated** selected under **Name tag
     auto-generation**. Change **project** to `ADS VPC`.
   - The **IPv4 CIDR block** should be `10.0.0.0/16`.
   - Keep **No IPv6 CIDR block** option selected.
   - The **Tenancy** should remain
     **Default**.
   - Select **2** for the **Number of Availability Zones
     (AZs)**.
   - Select **2** for the **Number of public
     subnets**. The **number of private subnets** can be
     changed to 0.
   - Choose **Customize subnet CIDR blocks** to configure the public
     subnet IP address range. The public subnet CIDR blocks should be `10.0.0.0/20` and `10.0.16.0/20`.

5. Choose **Create VPC**. It takes several minutes for the VPC to be
   created.

### Creating your Simple AD

To create a new Simple AD, perform the following steps. Before starting this
procedure, make sure you have completed the following in [Prerequisites](#gsg_prereqs "#gsg_prereqs") and [Creating and configuring your Amazon VPC for your
Simple AD](#gsg_create_vpc "#gsg_create_vpc").

###### Create a Simple AD

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose **Directories**
   and then choose **Set up directory**.
2. On the **Select directory type** page, choose
   **Simple AD**, and then choose **Next**.
3. On the **Enter directory information** page, provide the following
   information:

**Directory size**

Choose from either the **Small** or
**Large** size option. For more information about sizes, see
[Simple AD](directory_simple_ad.md "directory_simple_ad.md").

**Organization name**

A unique organization name for your directory that will be used to register
client devices.

This field is only available if you are creating your directory as part of
launching WorkSpaces.

**Directory DNS name**

The fully qualified name for the directory, such as `corp.example.com`.

**Directory NetBIOS name**

The short name for the directory, such as `CORP`.

**Administrator password**

The password for the directory administrator. The directory creation process
creates an administrator account with the username `Administrator` and this password.

The directory administrator password is case-sensitive and must be between 8
and 64 characters in length, inclusive. It must also contain at least one
character from three of the following four categories:

    * Lowercase letters (a-z)
    * Uppercase letters (A-Z)
    * Numbers (0-9)
    * Non-alphanumeric characters (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

**Confirm password**

Retype the administrator password.

###### Important

Be sure to save this password. Directory Service does not store this password, and it
cannot be retrieved. However, you can reset a password from the Directory Service console or
by using the [ResetUserPassword](../devguide/API_ResetUserPassword.md "../devguide/API_ResetUserPassword.md") API.

**Directory description**

An optional description for the directory. 4. On the **Choose VPC and subnets** page, provide the following
information, and then choose **Next**.

**VPC**

The VPC for the directory.

**Subnets**

Choose the subnets for the domain controllers. The two subnets must be in
different Availability Zones. 5. On the **Review & create** page, review the directory
information and make any necessary changes. When the information is correct, choose
**Create directory**. It takes several minutes for the directory to
be created. Once created, the **Status** value changes to
**Active**.

For more information on what is created with your Simple AD, see [What gets created with your Simple AD](simple_ad_what_gets_created.md "simple_ad_what_gets_created.md").
