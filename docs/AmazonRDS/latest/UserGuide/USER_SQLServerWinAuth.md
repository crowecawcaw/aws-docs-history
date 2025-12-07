# Working with AWS Managed Active Directory with RDS for SQL Server

You can use AWS Managed Microsoft AD to authenticate users with Windows Authentication when they connect to your
RDS for SQL Server DB instance. The DB instance works with AWS Directory Service for Microsoft Active Directory,
also called AWS Managed Microsoft AD, to enable Windows Authentication. When users authenticate with a
SQL Server DB instance joined to the trusting domain, authentication requests are forwarded
to the domain directory that you create with Directory Service.

## Region and version availability

Amazon RDS supports using only AWS Managed Microsoft AD for Windows Authentication. RDS doesn't support using AD Connector. For more information, see the following:

- [Application
  compatibility policy for AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_app_compatibility.md "../../../directoryservice/latest/admin-guide/ms_ad_app_compatibility.md")
- [Application
  compatibility policy for AD Connector](../../../directoryservice/latest/admin-guide/ad_connector_app_compatibility.md "../../../directoryservice/latest/admin-guide/ad_connector_app_compatibility.md")

For information on version and Region availability, see
[Kerberos authentication with RDS for SQL Server](Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.sq "Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.sq").

## Overview of setting up Windows

authentication

Amazon RDS uses mixed mode for Windows Authentication. This approach means that the _master user_ (the name and password used to create your SQL
Server DB instance) uses SQL Authentication. Because the master user account is a privileged
credential, you should restrict access to this account.

To get Windows Authentication using an on-premises or self-hosted Microsoft Active Directory,
create a forest trust. The trust can be one-way or two-way. For more information on setting
up forest trusts using Directory Service, see [When to create a trust
relationship](../../../directoryservice/latest/admin-guide/ms_ad_setup_trust.md "../../../directoryservice/latest/admin-guide/ms_ad_setup_trust.md") in the _AWS Directory Service Administration Guide_.

To set up Windows authentication for a SQL Server DB instance, do the following steps,
explained in greater detail in [Setting up Windows Authentication for
SQL Server DB instances](USER_SQLServerWinAuth.md "USER_SQLServerWinAuth.md"):

1. Use AWS Managed Microsoft AD, either from the AWS Management Console or Directory Service API, to create an AWS Managed Microsoft AD
   directory.
2. If you use the AWS CLI or Amazon RDS API to create your SQL Server DB instance, create an
   AWS Identity and Access Management (IAM) role. This role uses the managed IAM policy
   `AmazonRDSDirectoryServiceAccess` and allows Amazon RDS to make calls to
   your directory. If you use the console to create your SQL Server DB instance, AWS
   creates the IAM role for you.

For the role to allow access, the AWS Security Token Service (AWS STS) endpoint must be activated in the AWS
Region for your AWS account. AWS STS endpoints are active by default in all AWS
Regions, and you can use them without any further actions. For more information, see
[Managing
AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md") in the _IAM User Guide_. 3. Create and configure users and groups in the AWS Managed Microsoft AD directory using the Microsoft Active Directory tools. For
more information about creating users and groups in your Active Directory, see [Manage users and groups in AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md") in the _AWS Directory Service Administration Guide_. 4. If you plan to locate the directory and the DB instance in different VPCs, enable cross-VPC
traffic. 5. Use Amazon RDS to create a new SQL Server DB instance either from the console, AWS CLI, or Amazon RDS
API. In the create request, you provide the domain identifier ("`d-*`"
identifier) that was generated when you created your directory and the name of the
role you created. You can also modify an existing SQL Server DB instance to use
Windows Authentication by setting the domain and IAM role parameters for the DB
instance. 6. Use the Amazon RDS master user credentials to connect to the SQL Server DB instance as you do
any other DB instance. Because the DB instance is joined to the AWS Managed Microsoft AD domain,
you can provision SQL Server logins and users from the Active Directory users and
groups in their domain. (These are known as SQL Server "Windows" logins.) Database
permissions are managed through standard SQL Server permissions granted and revoked
to these Windows logins.

When you create a domain-connected RDS for SQL Server DB instance using the Amazon RDS console, AWS automatically creates the
`rds-directoryservice-access-role` IAM role. This role is essential for managing domain-connected instances
and is required for the following operations:

- Making configuration changes to domain-connected SQL Server instances
- Managing Active Directory integration settings
- Performing maintenance operations on domain-joined instances

###### Important

If you delete the `rds-directoryservice-access-role` IAM role, you can't make
changes to your domain-connected SQL Server instance through the Amazon RDS console or API. Attempting to modify the
instance results in an error message stating: **`You don't have permission to iam:CreateRole. To request 
 access, copy the following text and send it to your AWS administrator.`**

This error occurs because Amazon RDS needs to recreate the role to manage the domain connection, but lacks the
necessary permissions. Additionally, this error is not logged in CloudTrail, which can make troubleshooting
more difficult.

If you accidentally delete the `rds-directoryservice-access-role`, you must have
`iam:CreateRole` permissions to recreate it before you can make any changes to your domain-connected
SQL Server instance. To recreate the role manually, ensure it has the `AmazonRDSDirectoryServiceAccess`
managed policy attached and the appropriate trust relationship that allows the RDS service to assume the role.

## Restoring a SQL Server DB instance and then adding it to a domain

You can restore a DB snapshot or do point-in-time recovery (PITR) for a SQL Server DB instance and then add it to a domain. Once
the DB instance is restored, modify the instance using the process explained in [Step 5: Create or modify a SQL Server DB instance](USER_SQLServerWinAuth.md#USER_SQLServerWinAuth.SettingUp.CreateModify "USER_SQLServerWinAuth.md#USER_SQLServerWinAuth.SettingUp.CreateModify") to add
the DB instance to a domain.
