# Getting started with AWS Managed Microsoft AD

AWS Managed Microsoft AD creates a fully managed, Microsoft Active Directory in the AWS Cloud and is powered by Windows
Server 2019 and operates at the 2012 R2 Forest and Domain functional levels. When you create a
directory with AWS Managed Microsoft AD, AWS Directory Service creates two domain controllers and adds the DNS service on
your behalf. The domain controllers are created in different subnets in an Amazon VPC this redundancy
helps ensure that your directory remains accessible even if a failure occurs. If you need more
domain controllers, you can add them later. For more information, see [Deploying additional domain controllers for your
AWS Managed Microsoft AD](ms_ad_deploy_additional_dcs.md "ms_ad_deploy_additional_dcs.md").

For a demo and overview of AWS Managed Microsoft AD, see the following YouTube
video.

###### Topics

- [Prerequisites for creating a
  AWS Managed Microsoft AD](#ms_ad_getting_started_prereqs "#ms_ad_getting_started_prereqs")
- [AWS IAM Identity Center prerequisites](#prereq_aws_sso_ms_ad "#prereq_aws_sso_ms_ad")
- [Multi-factor authentication prerequisites](#prereq_mfa_ad "#prereq_mfa_ad")
- [Creating your AWS Managed Microsoft AD](#ms_ad_getting_started_create_directory "#ms_ad_getting_started_create_directory")
- [What gets created with your
  AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md")
- [AWS Managed Microsoft AD Administrator account and
  group permissions](ms_ad_getting_started_admin_account.md "ms_ad_getting_started_admin_account.md")

## Prerequisites for creating a

AWS Managed Microsoft AD

To create an AWS Managed Microsoft AD Active Directory, you need an Amazon VPC with the following:

- At least two subnets. Each of the subnets must be in a different Availability Zone and
  must be of same network type.

You can use IPv6 for your VPC. For more information, see [IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in
the _Amazon Virtual Private Cloud User Guide_.

- The VPC must have default hardware tenancy.
- You cannot create a AWS Managed Microsoft AD in a VPC using addresses in the 198.18.0.0/15 address
  space.

If you need to integrate your AWS Managed Microsoft AD domain with an existing on-premises Active Directory
domain, you must have the Forest and Domain functional levels for your on-premises domain set
to Windows Server 2003 or higher.

AWS Directory Service uses a two VPC structure. The EC2 instances which make up your directory run outside
of your AWS account, and are managed by AWS. They have two network adapters,
`ETH0` and `ETH1`. `ETH0` is the management adapter, and
exists outside of your account. `ETH1` is created within your account.

The management IP range of your directory's ETH0 network is 198.18.0.0/15.

For a tutorial on how to create the AWS environment and AWS Managed Microsoft AD, see [AWS Managed Microsoft AD test lab tutorials](ms_ad_tutorial_test_lab.md "ms_ad_tutorial_test_lab.md").

## AWS IAM Identity Center prerequisites

If you plan to use IAM Identity Center with AWS Managed Microsoft AD, you need to ensure that the following are
true:

- Your AWS Managed Microsoft AD directory is set up in your AWS organization's
  management account.
- Your instance of IAM Identity Center is in the same Region where your AWS Managed Microsoft AD directory is set
  up.

For more information, see [IAM Identity Center prerequisites](../../../singlesignon/latest/userguide/prereqs.md "../../../singlesignon/latest/userguide/prereqs.md")
in the _AWS IAM Identity Center User Guide_.

## Multi-factor authentication prerequisites

To support multi-factor authentication with your AWS Managed Microsoft AD directory, you must
configure either your on-premises or cloud-based [Remote Authentication Dial-In User
Service](https://en.wikipedia.org/wiki/RADIUS "https://en.wikipedia.org/wiki/RADIUS") (RADIUS) server in the following way so that it can accept requests from
your AWS Managed Microsoft AD directory in AWS.

1. On your RADIUS server, create two RADIUS clients to represent both of the AWS Managed Microsoft AD
   domain controllers (DCs) in AWS. You must configure both clients using the following
   common parameters (your RADIUS server may vary):
   - **Address (DNS or IP)**: This is the DNS address for
     one of the AWS Managed Microsoft AD DCs. Both DNS addresses can be found in the AWS Directory
     Service Console on the **Details** page of the
     AWS Managed Microsoft AD directory in which you plan to use MFA. The DNS addresses displayed
     represent the IP addresses for both of the AWS Managed Microsoft AD DCs that are used by
     AWS.

   ###### Note

   If your RADIUS server supports DNS addresses, you must create only one RADIUS
   client configuration. Otherwise, you must create one RADIUS client configuration for
   each AWS Managed Microsoft AD DC.
   - **Port number**: Configure the port number for which
     your RADIUS server accepts RADIUS client connections. The standard RADIUS port is
   1812.
   - **Shared secret**: Type or generate a shared secret
     that the RADIUS server will use to connect with RADIUS clients.
   - **Protocol**: You might need to configure the
     authentication protocol between the AWS Managed Microsoft AD DCs and the RADIUS server. Supported
     protocols are PAP, CHAP MS-CHAPv1, and MS-CHAPv2. MS-CHAPv2 is recommended because it
     provides the strongest security of the three options.
   - **Application name**: This may be optional in some
     RADIUS servers and usually identifies the application in messages or reports.

2. Configure your existing network to allow inbound traffic from the RADIUS clients
   (AWS Managed Microsoft AD DCs DNS addresses, see Step 1) to your RADIUS server port.
3. Add a rule to the Amazon EC2 security group in your AWS Managed Microsoft AD domain that allows inbound
   traffic from the RADIUS server DNS address and port number defined previously. For more
   information, see [Adding rules to a security group](../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule "../../../AWSEC2/latest/UserGuide/using-network-security.md#adding-security-group-rule") in the _EC2 User
   Guide_.

For more information about using AWS Managed Microsoft AD with MFA, see [Enabling multi-factor authentication for AWS Managed Microsoft AD](ms_ad_mfa.md "ms_ad_mfa.md").

## Creating your AWS Managed Microsoft AD

To create a new AWS Managed Microsoft AD Active Directory, perform the following steps. Before starting this
procedure, make sure that you have completed the prerequisites identified in [Prerequisites for creating a
AWS Managed Microsoft AD](#ms_ad_getting_started_prereqs "#ms_ad_getting_started_prereqs").

###### To create an AWS Managed Microsoft AD

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose **Directories**
   and then choose **Set up directory**.
2. On the **Select directory type** page, choose
   **AWS Managed Microsoft AD**, and then choose **Next**.
3. On the **Enter directory information** page, provide the following
   information:

**Edition**

Choose from either the **Standard Edition** or
**Enterprise Edition** of AWS Managed Microsoft AD. For more information
about editions, see [AWS Directory Service for Microsoft Active Directory](what_is.md#microsoftad "what_is.md#microsoftad").

**Directory DNS name**

The fully qualified name for the directory, such as
`corp.example.com`.

###### Note

If you plan on using Amazon Route 53 for DNS, the domain name of your AWS Managed Microsoft AD
must be different than your Route 53 domain name. DNS resolution issues can occur if
Route 53 and AWS Managed Microsoft AD share the same domain name.

**Directory NetBIOS name**

The short name for the directory, such as `CORP`.

**Directory description**

An optional description for the directory. This description can be changed after
creating your AWS Managed Microsoft AD.

**Admin password**

The password for the directory administrator. The directory creation process
creates an administrator account with the user name `Admin` and this
password. You can change the Admin password after creating your AWS Managed Microsoft AD.

The password cannot include the word "admin."

The directory administrator password is case-sensitive and must be between 8 and
64 characters in length, inclusive. It must also contain at least one character from
three of the following four categories:

    * Lowercase letters (a-z)
    * Uppercase letters (A-Z)
    * Numbers (0-9)
    * Non-alphanumeric characters (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

**Confirm password**

Retype the administrator password.

**(Optional) User and group management**

To enable AWS Managed Microsoft AD user and group management from the AWS Management Console, select
**Manage user and group management in the AWS Management Console**. For more
information on how to use user and group management, see [Manage AWS Managed Microsoft AD users and groups with
the AWS Management Console, AWS CLI, or AWS Tools for PowerShell](ms_ad_manage_users_groups_procedures.md "ms_ad_manage_users_groups_procedures.md"). 4. On the **Choose VPC and subnets** page, provide the following
information, and then choose **Next**.

**VPC**

Select the VPC for the directory.

**Network type**

The Internet Protocol (IP) addressing system associated with your VPC and
subnets.

Select the CIDR block associated to your existing VPC. Resources in your subnet
can be configured to use IPv4 only, IPv6 only, or both IPv4 and IPv6 (dual-stack).
For more information, see [Compare IPv4 and IPv6](../../../vpc/latest/userguide/ipv4-ipv6-comparison.md "../../../vpc/latest/userguide/ipv4-ipv6-comparison.md")
in the _Amazon Virtual Private Cloud User Guide_.

**Subnets**

Select the subnets for the domain controllers. The two subnets must be in
different Availability Zones. 5. On the **Review & create** page, review the directory information
and make any necessary changes. When the information is correct, choose **Create
directory**. Creating the directory takes 20 to 40 minutes. Once created, the
**Status** value changes to **Active**.

For more information on what is created with your AWS Managed Microsoft AD, see the following:

- [What gets created with your
  AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md")
- [AWS Managed Microsoft AD Administrator account and
  group permissions](ms_ad_getting_started_admin_account.md "ms_ad_getting_started_admin_account.md")

**Related AWS Security blog articles**

- [How to delegate administration of your AWS Managed Microsoft AD directory to your on-premises Active Directory
  users](https://aws.amazon.com/blogs/security/how-to-delegate-administration-of-your-aws-managed-microsoft-ad-directory-to-your-on-premises-active-directory-users/ "https://aws.amazon.com/blogs/security/how-to-delegate-administration-of-your-aws-managed-microsoft-ad-directory-to-your-on-premises-active-directory-users/")
- [How to configure even stronger password policies to help meet your security standards by
  using AWS Directory Service for AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/how-to-configure-even-stronger-password-policies-to-help-meet-your-security-standards-by-using-aws-directory-service-for-microsoft-active-directory/ "https://aws.amazon.com/blogs/security/how-to-configure-even-stronger-password-policies-to-help-meet-your-security-standards-by-using-aws-directory-service-for-microsoft-active-directory/")
- [How to increase the redundancy and performance of your AWS Directory Service for AWS Managed Microsoft AD by adding
  Domain controllers](https://aws.amazon.com/blogs/security/how-to-increase-the-redundancy-and-performance-of-your-aws-directory-service-for-microsoft-ad-directory-by-adding-domain-controllers/ "https://aws.amazon.com/blogs/security/how-to-increase-the-redundancy-and-performance-of-your-aws-directory-service-for-microsoft-ad-directory-by-adding-domain-controllers/")
- [How to enable the use of remote desktops by deploying Microsoft remote desktop licensing
  manager on AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/how-to-enable-the-use-of-remote-desktops-by-deploying-microsoft-remote-desktop-licensing-manager-on-aws-microsoft-ad/ "https://aws.amazon.com/blogs/security/how-to-enable-the-use-of-remote-desktops-by-deploying-microsoft-remote-desktop-licensing-manager-on-aws-microsoft-ad/")
- [How to access the AWS Management Console using AWS Managed Microsoft AD and your on-premises
  credentials](https://aws.amazon.com/blogs/security/how-to-access-the-aws-management-console-using-aws-microsoft-ad-and-your-on-premises-credentials/ "https://aws.amazon.com/blogs/security/how-to-access-the-aws-management-console-using-aws-microsoft-ad-and-your-on-premises-credentials/")
- [How to enable multi-factor authentication for AWS services by using AWS Managed Microsoft AD and
  on-premises credentials](https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/ "https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/")
- [How to easily log on to AWS services by using your on-premises Active Directory](https://aws.amazon.com/blogs/security/how-to-easily-log-on-to-aws-services-by-using-your-on-premises-active-directory/ "https://aws.amazon.com/blogs/security/how-to-easily-log-on-to-aws-services-by-using-your-on-premises-active-directory/")
