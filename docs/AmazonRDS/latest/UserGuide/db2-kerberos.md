# Using Kerberos authentication for

Amazon RDS for Db2

You can use Kerberos authentication to authenticate users when they connect
to your Amazon RDS for Db2 DB instance. In this configuration, your DB instance works with
AWS Directory Service for Microsoft Active Directory, also called AWS Managed Microsoft AD. You add the domain and other information of
your AWS Managed Microsoft AD directory to your RDS for Db2 DB instance. When users authenticate with an
RDS for Db2 DB instance joined to the trusting domain, authentication requests are forwarded to
the AWS Managed Microsoft AD directory that you created with Directory Service.

Keeping all of your credentials in the same directory can save you time and effort. With
this approach, you have a centralized place for storing and managing credentials for
multiple DB instances. Using a directory can also improve your overall security
profile.

In addition, you can access credentials from your own on-premises Microsoft Active
Directory. To do so, create a trusting domain relationship so that the AWS Managed Microsoft AD
directory trusts your on-premises Microsoft Active Directory. In this way, your users can
access your RDS for Db2 DB instances with the same Windows single sign-on (SSO) experience as
when they access workloads in your on-premises network.

For more information, see [What is Directory Service?](../../../directoryservice/latest/admin-guide/what_is.md "../../../directoryservice/latest/admin-guide/what_is.md") in the
_AWS Directory Service Administration Guide_.

For information about Kerberos authentication, see the following
topics:

###### Topics

- [Setting up Kerberos authentication
  for Amazon RDS for Db2 DB instances](db2-kerberos-setting-up.md "db2-kerberos-setting-up.md")
- [Connecting to Amazon RDS for Db2 with
  Kerberos authentication](db2-kerberos-connecting.md "db2-kerberos-connecting.md")

## Region and version availability

Feature availability and support varies across specific versions of each database
engine, and across AWS Regions. For more information about version and Region
availability of RDS for Db2 with Kerberos authentication, see [Supported
Regions and DB engines for Kerberos authentication in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

###### Note

Kerberos authentication isn't supported for DB instance classes
that are deprecated for RDS for Db2 DB instances. For more information, see [Amazon RDS for Db2 instance classes](Db2.Concepts.General.md "Db2.Concepts.General.md").

## Overview of Kerberos

authentication for RDS for Db2 DB instances

To set up Kerberos authentication for an RDS for Db2 DB instance, complete
the following general steps, which are described in more detail later:

1. Use AWS Managed Microsoft AD to create an AWS Managed Microsoft AD directory. You can use the
   AWS Management Console, the AWS Command Line Interface (AWS CLI), or Directory Service to create the directory. For more
   information, see [Create your AWS Managed Microsoft AD directory](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md") in the _AWS Directory Service Administration Guide_.
2. Create an AWS Identity and Access Management (IAM) role that uses the managed IAM policy
   `AmazonRDSDirectoryServiceAccess`. The IAM role allows Amazon RDS to
   make calls to your directory.

For the IAM role to allow access, the AWS Security Token Service (AWS STS) endpoint must be
activated in the correct AWS Region for your AWS account. AWS STS endpoints
are active by default in all AWS Regions, and you can use them without any
further actions. For more information, see [Activating and deactivating AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate") in the
_IAM User Guide_. 3. Create or modify an RDS for Db2 DB instance by using the AWS Management Console, the AWS CLI,
or the RDS API with one of the following methods:

    * Create a new RDS for Db2 DB instance using the console, the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command, or the [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") API operation. For instructions, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
    * Modify an existing RDS for Db2 DB instance using the console, the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command, or the
     [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API operation. For
     instructions, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
    * Restore an RDS for Db2 DB instance from a DB snapshot using the console,
     the [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md")
     command, or the [RestoreDBInstanceFromDBSnapshot](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md") API
     operation. For instructions, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
    * Restore an RDS for Db2 DB instance to a point-in-time using the console,
     the [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md") command,
     or the [RestoreDBInstanceToPointInTime](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md") API
     operation. For instructions, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

You can locate the DB instance in the same Amazon Virtual Private Cloud (VPC) as the directory or
in a different AWS account or VPC. When you create or modify the RDS for Db2 DB
instance, do the following tasks:

    * Provide the domain identifier (`d-*` identifier) that was generated when you created
     your directory.
    * Provide the name of the IAM role that you created.
    * Verify that the DB instance security group can receive inbound traffic
     from the directory security group.

4. Configure your Db2 client, and verify that traffic can flow between the client
   host and Directory Service for the following ports:
   - TCP/UDP port 53 – DNS
   - TCP 88 – Kerberos authentication
   - TCP 389 – LDAP
   - TCP 464 – Kerberos authentication

## Managing a DB instance in a domain

You can use the AWS Management Console, the AWS CLI, or the RDS API to manage your DB instance and its
relationship with your Microsoft Active Directory. For example, you can
associate an Active Directory to enable Kerberos authentication. You can also
remove the association for an Active Directory to disable Kerberos
authentication. You can also move a DB instance to be externally authenticated by one
Microsoft Active Directory to another.

For example, running the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") CLI command, you can perform the following
actions:

- Re-attempt enabling Kerberos authentication for a failed membership by
  specifying the current membership's directory ID for the `--domain`
  option.
- Disable Kerberos authentication on a DB instance by specifying
  `none` for the `--domain` option.
- Move a DB instance from one domain to another by specifying the domain identifier
  of the new domain for the `--domain` option.

### Understanding domain

membership

After you create or modify your DB instance, it becomes a member of the domain. You
can view the status of the domain membership in the console or by running the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command. The status of the DB
instance can be one of the following:

- `kerberos-enabled` – The DB instance has
  Kerberos authentication enabled.
- `enabling-kerberos` – AWS is in the process of enabling
  Kerberos authentication on this DB instance.
- `pending-enable-kerberos` – Enabling Kerberos
  authentication is pending on this DB instance.
- `pending-maintenance-enable-kerberos` – AWS will attempt
  to enable Kerberos authentication on the DB instance during the
  next scheduled maintenance window.
- `pending-disable-kerberos` – Disabling
  Kerberos authentication is pending on this DB
  instance.
- `pending-maintenance-disable-kerberos` – AWS will attempt
  to disable Kerberos authentication on the DB instance during the
  next scheduled maintenance window.
- `enable-kerberos-failed` – A configuration problem prevented
  AWS from enabling Kerberos authentication on the DB instance.
  Correct the configuration problem before re-issuing the command to modify the DB
  instance.
- `disabling-kerberos` – AWS is in the process of disabling
  Kerberos authentication on this DB instance.

A request to enable Kerberos authentication can fail because of a
network connectivity issue or an incorrect IAM role. In some cases, the attempt to
enable Kerberos authentication might fail when you create or modify a DB
instance. If this happens, verify that you are using the correct IAM role, and then
modify the DB instance to join the domain.
