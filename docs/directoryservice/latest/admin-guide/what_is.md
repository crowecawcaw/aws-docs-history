# What is AWS Directory Service?

AWS Directory Service provides multiple ways to use Microsoft Active Directory (AD) with other AWS services.
Directories store information about users, groups, and devices, and administrators use them
to manage access to information and resources. AWS Directory Service provides multiple directory choices
for customers who want to use existing Microsoft AD or Lightweight Directory Access Protocol
(LDAP)–aware applications in the cloud. It also offers those same choices to
developers who need a directory to manage users, groups, devices, and access.

## AWS Directory Service options

AWS Directory Service includes several directory types to choose from. For more information,
select one of the following tabs:

AWS Directory Service for Microsoft Active Directory

Also known as AWS Managed Microsoft AD, AWS Directory Service for Microsoft Active Directory is powered by an actual Microsoft
Windows Server Active Directory (AD), managed by AWS in the AWS
Cloud. It enables you to migrate a broad range of Active Directory–aware
applications to the AWS Cloud. AWS Managed Microsoft AD works with Microsoft
SharePoint, Microsoft SQL Server Always On
Availability Groups, and many .NET applications. It also supports AWS
managed applications and services including [Amazon WorkSpaces](https://aws.amazon.com/workspaces/ "https://aws.amazon.com/workspaces/"), [Amazon WorkDocs](https://aws.amazon.com/workdocs/ "https://aws.amazon.com/workdocs/"), [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/"), [Amazon Chime](https://aws.amazon.com/chime/ "https://aws.amazon.com/chime/"), [Amazon Connect](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/"), and [Amazon Relational Database Service for Microsoft SQL
Server](https://aws.amazon.com/rds/sqlserver/ "https://aws.amazon.com/rds/sqlserver/") (Amazon RDS for SQL Server, Amazon RDS
for Oracle, and Amazon RDS for PostgreSQL).

AWS Managed Microsoft AD is approved for applications in the
AWS Cloud that are subject to [U.S. Health Insurance
Portability and Accountability Act](https://www.hhs.gov/hipaa/for-professionals/index.html "https://www.hhs.gov/hipaa/for-professionals/index.html") (HIPAA) or [Payment Card
Industry Data Security Standard](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/") (PCI DSS) compliance when you
[enable compliance for
your directory](ms_ad_compliance.md "ms_ad_compliance.md").

All compatible applications work with user credentials that you store in
AWS Managed Microsoft AD, or you can [connect
to your existing AD infrastructure](ms_ad_connect_existing_infrastructure.md "ms_ad_connect_existing_infrastructure.md") with a trust and use
credentials from an Active Directory running on-premises or on EC2 Windows. If you
[join EC2 instances
to your AWS Managed Microsoft AD](ms_ad_join_instance.md "ms_ad_join_instance.md"), your users can access Windows workloads in
the AWS Cloud with the same Windows single sign-on (SSO) experience as
when they access workloads in your on-premises network.

AWS Managed Microsoft AD also supports federated use cases using Active Directory credentials.
Alone, AWS Managed Microsoft AD enables you to sign in to the [AWS Management Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/"). With [AWS IAM Identity Center](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/"), you can also
obtain short-term credentials for use with the AWS SDK and CLI, and use
preconfigured SAML integrations to sign in to many cloud applications. By
adding Microsoft Entra Connect (formerly known as Azure Active Directory Connect), and optionally Active Directory Federation Service (AD FS),
you can sign in to Microsoft Office 365 and other cloud
applications with credentials stored in AWS Managed Microsoft AD.

The service includes key features that enable you to [extend your
schema](ms_ad_schema_extensions.md "ms_ad_schema_extensions.md"), [manage password policies](ms_ad_password_policies.md "ms_ad_password_policies.md"), and [enable secure LDAP
communications](ms_ad_ldap.md "ms_ad_ldap.md") through Secure Socket Layer (SSL)/Transport Layer
Security (TLS). You can also [enable multi-factor authentication (MFA) for AWS Managed Microsoft AD](ms_ad_mfa.md "ms_ad_mfa.md") to
provide an additional layer of security when users access AWS applications
from the Internet. Because Active Directory is an LDAP directory, you can also use
AWS Managed Microsoft AD for Linux Secure Shell (SSH) authentication and for other
LDAP-enabled applications.

AWS provides monitoring, daily snapshots, and recovery as part of the
service—you [add
users and groups to AWS Managed Microsoft AD](ms_ad_manage_users_groups.md "ms_ad_manage_users_groups.md"), and administer Group Policy
using familiar Active Directory tools running on a Windows computer
joined to the AWS Managed Microsoft AD domain. You can also scale the directory by
[deploying
additional domain controllers](ms_ad_deploy_additional_dcs.md "ms_ad_deploy_additional_dcs.md") and help improve application
performance by distributing requests across a larger number of domain
controllers.

AWS Managed Microsoft AD is available in two editions: Standard and Enterprise.

- **Standard Edition:** AWS Managed Microsoft AD
  (Standard Edition) is optimized to be a primary directory for small
  and midsize businesses with up to 5,000 employees. It provides you
  enough storage capacity to support up to 30,000\* directory objects,
  such as users, groups, and computers.
- **Enterprise Edition:** AWS Managed Microsoft AD
  (Enterprise Edition) is designed to support enterprise organizations
  with up to 500,000\* directory objects.

\* Upper limits are approximations. Your directory may support more or less
directory objects depending on the size of your objects and the behavior and
performance needs of your applications.

**_When to
use_**

AWS Managed Microsoft AD is your best choice if you need actual Active Directory features to
support AWS applications or Windows workloads, including
Amazon Relational Database Service for Microsoft SQL Server. It's also best if you
want a standalone Active Directory in the AWS Cloud that supports Office 365 or you
need an LDAP directory to support your Linux applications. For more
information, see [AWS Managed Microsoft AD](directory_microsoft_ad.md "directory_microsoft_ad.md").

AD Connector

AD Connector is a proxy service that provides an easy way to connect
compatible AWS applications, such as Amazon WorkSpaces, Amazon Quick Suite, and [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") for Windows
Server instances, to your existing on-premises Microsoft Active Directory. With
AD Connector , you can simply [add one service account](prereq_connector.md#connect_delegate_privileges "prereq_connector.md#connect_delegate_privileges") to your Active Directory. AD Connector also
eliminates the need of directory synchronization or the cost and complexity
of hosting a federation infrastructure.

When you add users to AWS applications such as Amazon Quick Suite, AD Connector
reads your existing Active Directory to create lists of users and groups to select from.
When users log in to the AWS applications, AD Connector forwards sign-in
requests to your on-premises Active Directory domain controllers for authentication.
AD Connector works with many AWS applications and services including
[Amazon WorkSpaces](https://aws.amazon.com/workspaces/ "https://aws.amazon.com/workspaces/"), [Amazon WorkDocs](https://aws.amazon.com/workdocs/ "https://aws.amazon.com/workdocs/"), [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/"), [Amazon Chime](https://aws.amazon.com/chime/ "https://aws.amazon.com/chime/"), [Amazon Connect](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/"), and [Amazon WorkMail](https://aws.amazon.com/workmail/ "https://aws.amazon.com/workmail/"). You can also [join your
EC2 Windows instances](ad_connector_join_windows_instance.md "ad_connector_join_windows_instance.md") to your on-premises Active Directory
domain through AD Connector using [seamless
domain join](ad_connector_launching_instance.md "ad_connector_launching_instance.md"). AD Connector also allows your users to access the
AWS Management Console and manage AWS resources by logging in with their existing Active Directory
credentials. AD Connector is not compatible with RDS SQL Server.

You can also use AD Connector to [enable multi-factor
authentication](ad_connector_mfa.md "ad_connector_mfa.md") (MFA) for your AWS application users by
connecting it to your existing RADIUS-based MFA infrastructure. This
provides an additional layer of security when users access AWS
applications.

With AD Connector, you continue to manage your Active Directory as you do now. For
example, you add new users and groups and update passwords using standard
Active Directory administration tools in your on-premises Active Directory . This helps you
consistently enforce your security policies, such as password expiration,
password history, and account lockouts, whether users are accessing
resources on premises or in the AWS Cloud.

**_When to
use_**

AD Connector is your best choice when you want to use your existing
on-premises directory with compatible AWS services. For more information,
see [AD Connector](directory_ad_connector.md "directory_ad_connector.md").

Simple AD

Simple AD is a Microsoft Active Directory–_compatible_ directory from
AWS Directory Service that is powered by Samba 4. Simple AD supports basic Active Directory
features such as user accounts, group memberships, joining a Linux domain or
Windows based EC2 instances, Kerberos-based SSO, and
group policies. AWS provides monitoring, daily snap-shots, and recovery as
part of the service.

Simple AD is a standalone directory in the cloud, where you create and
manage user identities and manage access to applications. You can use many
familiar Active Directory–aware applications and tools that require basic Active Directory
features. Simple AD is compatible with the following AWS applications:
[Amazon WorkSpaces](https://aws.amazon.com/workspaces/ "https://aws.amazon.com/workspaces/"), [Amazon WorkDocs](https://aws.amazon.com/workdocs/ "https://aws.amazon.com/workdocs/"), [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/"), and [Amazon WorkMail](https://aws.amazon.com/workmail/ "https://aws.amazon.com/workmail/"). You can also sign in to
the AWS Management Console with Simple AD user accounts and to manage AWS resources.

Simple AD does not support multi-factor authentication (MFA), trust
relationships, DNS dynamic update, schema extensions, communication over
LDAPS, PowerShell AD cmdlets, or FSMO role transfer. Simple AD is not
compatible with RDS SQL Server. Customers who require the features of an
actual Microsoft Active Directory, or who envision using their directory with RDS SQL Server
should use AWS Managed Microsoft AD instead. Please verify your required applications
are fully compatible with Samba 4 before using Simple AD. For more
information, see [https://www.samba.org](https://www.samba.org "https://www.samba.org").

**_When to
use_**

You can use Simple AD as a standalone directory in the cloud to support
Windows workloads that need basic Active Directory features,
compatible AWS applications, or to support Linux workloads that need LDAP
service. For more information, see [Simple AD](directory_simple_ad.md "directory_simple_ad.md").

See [Region availability for AWS Directory Service](regions.md "regions.md") for a list of supported
directory types per Region.

## Which to choose

You can choose directory services with the features and scalability that best meets
your needs. Use the following table to help you determine which AWS Directory Service directory
option works best for your organization.

| What do you need to do?                                          | Recommended AWS Directory Service options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I need Active Directory or LDAP for my applications in the cloud | Use **AWS Directory Service for Microsoft Active Directory\*<br>• (Standard Edition or<br>Enterprise Edition) if you need an actual Microsoft Active Directory in the AWS<br>Cloud that supports Active Directory–aware workloads, or AWS<br>applications and services such as Amazon WorkSpaces and Amazon Quick Suite, or you<br>need LDAP support for Linux applications.<br>Use **AWS Directory Service for Microsoft Active Directory*<br>• (Hybrid Edition) to<br>extend your existing self-managed AD into the AWS Cloud with<br>AWS Directory Service<br>Use \*\*AD Connector*<br>• if you only need to allow<br>your on-premises users to log in to AWS applications and services<br>with their Active Directory credentials. You can also use AD Connector to join<br>Amazon EC2 instances to your existing Active Directory domain.<br>Use \*_Simple AD_<br>• if you need a low-scale,<br>low-cost directory with basic Active Directory compatibility that supports Samba<br>4–compatible applications, or you need LDAP compatibility for<br>LDAP-aware applications. |
| I develop SaaS applications                                      | Use \*_Amazon Cognito_<br>• if you develop high-scale SaaS<br>applications and need a scalable directory to manage and authenticate<br>your subscribers and that works with social media identities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

For more information about AWS Directory Service directory options, see [How to choose Active Directory solutions
on AWS](https://youtu.be/8xhHEtekgZ4?si=3wlSVnT-xgNylPPJ "https://youtu.be/8xhHEtekgZ4?si=3wlSVnT-xgNylPPJ").

## Working with Amazon EC2

A basic understanding of Amazon EC2 is essential to using AWS Directory Service. We recommend that you
begin by reading the following topics:

- [What is Amazon EC2?](../../../AWSEC2/latest/WindowsGuide/concepts.md "../../../AWSEC2/latest/WindowsGuide/concepts.md") in the
  _Amazon EC2 User Guide_.
- [Launch an Amazon EC2
  instance](../../../AWSEC2/latest/WindowsGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/WindowsGuide/LaunchingAndUsingInstances.md") in the _Amazon EC2 User Guide_.
- [Amazon EC2 security groups
  for your EC2 instances](../../../AWSEC2/latest/WindowsGuide/ec2-security-groups.md "../../../AWSEC2/latest/WindowsGuide/ec2-security-groups.md") in the
  _Amazon EC2 User Guide_.
- [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in
  the _Amazon VPC User Guide_.
- [Connect your VPC to remote
  networks using AWS Virtual Private Network](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the
  _Amazon VPC User Guide_.
