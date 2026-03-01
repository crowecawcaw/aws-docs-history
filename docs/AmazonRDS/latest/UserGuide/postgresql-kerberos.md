# Using Kerberos authentication with Amazon RDS for PostgreSQL

You can use Kerberos to authenticate users when they connect to your DB
instance running PostgreSQL. To do so, configure your
DB instance to use AWS Directory Service for Microsoft Active Directory for Kerberos authentication.
AWS Directory Service for Microsoft Active Directory is also called AWS Managed Microsoft AD. It's a feature available with Directory Service. To
learn more, see [What is Directory Service?](../../../directoryservice/latest/admin-guide/what_is.md "../../../directoryservice/latest/admin-guide/what_is.md") in the
_AWS Directory Service Administration Guide_.

To start, create an AWS Managed Microsoft AD directory to store user credentials. Then, provide to
your PostgreSQL DB instance the Active Directory's domain and other information. When users
authenticate with the PostgreSQL DB instance, authentication requests are forwarded to the
AWS Managed Microsoft AD directory.

Keeping all of your credentials in the same directory can save you time and effort. You
have a centralized location for storing and managing credentials for multiple DB instances.
Using a directory can also improve your overall security profile.

In addition, you can access credentials from your own on-premises Microsoft Active
Directory. To do so, create a trusting domain relationship so that the AWS Managed Microsoft AD
directory trusts your on-premises Microsoft Active Directory. In this way, your users can
access your PostgreSQL instances with the same Windows single sign-on (SSO)
experience as when they access workloads in your on-premises network.

A database can use password authentication or password
authentication with either Kerberos or AWS Identity and Access Management (IAM) authentication. For more
information about IAM authentication, see [IAM database authenticationfor MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md").

###### Note

RDS for PostgreSQL doesn't support Kerberos authentication for Active Directory groups.

###### Topics

- [Region and version availability](#postgresql-kerberos.RegionVersionAvailability "#postgresql-kerberos.RegionVersionAvailability")
- [Overview of Kerberos authentication for PostgreSQL DB instances](#postgresql-kerberos-overview "#postgresql-kerberos-overview")
- [Setting up Kerberos authentication for PostgreSQL DB instances](postgresql-kerberos-setting-up.md "postgresql-kerberos-setting-up.md")
- [Managing an RDS for PostgreSQL DB instance in an Active Directory domain](postgresql-kerberos-managing.md "postgresql-kerberos-managing.md")
- [Connecting to PostgreSQL with Kerberos authentication](postgresql-kerberos-connecting.md "postgresql-kerberos-connecting.md")

## Region and version availability

Feature availability and support varies across specific versions
of each database engine, and across AWS Regions. For more information on version and
Region availability of RDS for PostgreSQL with Kerberos authentication, see [Supported Regions and DB engines for Kerberos authentication in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

## Overview of Kerberos authentication for PostgreSQL DB instances

To set up Kerberos authentication for a PostgreSQL DB instance, take the following
steps, described in more detail later:

1. Use AWS Managed Microsoft AD to create an AWS Managed Microsoft AD directory. You can use the
   AWS Management Console, the AWS CLI, or the Directory Service API to create the directory. Make sure to
   open the relevant outbound ports on the directory security group so that the
   directory can communicate with the instance.
2. Create a role that provides Amazon RDS access to
   make calls to your AWS Managed Microsoft AD directory. To do so, create an AWS Identity and Access Management (IAM)
   role that uses the managed IAM policy
   `AmazonRDSDirectoryServiceAccess`.

For the IAM role to allow access, the AWS Security Token Service (AWS STS) endpoint must be
activated in the correct AWS Region for your AWS account. AWS STS endpoints
are active by default in all AWS Regions, and you can use them without any
further actions. For more information, see [Activating and deactivating AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate") in the
_IAM User Guide_. 3. Create and configure users in the AWS Managed Microsoft AD directory using the Microsoft
Active Directory tools. For more information about creating users in your Active
Directory, see [Manage
users and groups in AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md") in the
_Directory Service Administration Guide_. 4. If you plan to locate the directory and the DB instance in different AWS
accounts or virtual private clouds (VPCs), configure VPC peering. For more
information, see [What is VPC
peering?](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md") in the _Amazon VPC Peering Guide_. 5. Create or modify a PostgreSQL DB
instance either from the console, CLI, or
RDS API using one of the following methods:

    * [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md")
    * [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md")
    * [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md")
    * [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md")

You can locate the instance in the same Amazon Virtual Private Cloud (VPC) as the
directory or in a different AWS account or VPC. When you create or modify the
PostgreSQL DB instance, do the following:

    * Provide the domain identifier (`d-*` identifier) that was
     generated when you created your directory.
    * Provide the name of the IAM role that you created.
    * Ensure that the DB instance security group can receive inbound traffic
     from the directory security group.

6. Use the RDS master user credentials to connect to the PostgreSQL DB instance. Create the user in PostgreSQL to be identified
   externally. Externally identified users can log in to the PostgreSQL DB instance using Kerberos authentication.
