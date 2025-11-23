# Using Kerberos authentication for Amazon RDS for MySQL

You can use Kerberos authentication to authenticate users when they connect to your MySQL DB instance. The
DB instance works with AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to enable Kerberos authentication. When users
authenticate with a MySQL DB instance joined to the trusting domain, authentication requests are forwarded.
Forwarded requests go to the domain directory that you create with Directory Service.

Keeping all of your credentials in the same directory can save you time and effort. With this approach, you have
a centralized place for storing and managing credentials for multiple DB instances. Using a directory can
also improve your overall security profile.

## Region and version availability

Feature availability and support varies across specific versions of each database engine, and across AWS Regions.
For more information on version and Region availability of Amazon RDS with Kerberos authentication, see
[Supported
Regions and DB engines for Kerberos authentication in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

## Overview of Setting up Kerberos authentication for MySQL DB instances

To set up Kerberos authentication for a MySQL DB instance, complete the following general steps, described
in more detail later:

1. Use AWS Managed Microsoft AD to create an AWS Managed Microsoft AD directory. You can use the AWS Management Console, the
   AWS CLI, or the Directory Service to create the directory. For details about doing so,
   see [Create your AWS Managed Microsoft AD directory](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md") in the _AWS Directory Service Administration Guide_.
2. Create an AWS Identity and Access Management (IAM) role that uses the managed IAM policy
   `AmazonRDSDirectoryServiceAccess`. The role allows Amazon RDS to make calls to your directory.

For the role to allow access, the AWS Security Token Service (AWS STS) endpoint must be activated in the AWS Region for your
AWS account. AWS STS endpoints are active by default in all AWS Regions, and you can use them without any
further actions. For more information, see
[Activating and
deactivating AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate") in the _IAM User Guide_. 3. Create and configure users in the AWS Managed Microsoft AD directory using the Microsoft Active Directory
tools. For more information about creating users in your Active Directory, see
[Manage users and groups in AWS managed Microsoft
AD](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md") in the _AWS Directory Service Administration Guide_. 4. Create or modify a MySQL DB instance. If you use either the CLI or RDS API in the create request,
specify a domain identifier with the `Domain` parameter. Use the `d-*` identifier that
was generated when you created your directory and the name of the role that you created.

If you modify an existing MySQL DB instance to use Kerberos authentication, set the domain and IAM
role parameters for the DB instance. Locate the DB instance in the same VPC as the domain directory. 5. Use the Amazon RDS master user credentials to connect to the MySQL DB instance. Create the user in MySQL
using the `CREATE USER` clause `IDENTIFIED WITH 'auth_pam'`. Users that you create
this way can log in to the MySQL DB instance using Kerberos authentication.

## Setting up Kerberos authentication for MySQL DB instances

You use AWS Managed Microsoft AD to set up Kerberos authentication for a MySQL DB instance. To set up Kerberos
authentication, you take the following steps.

### Step 1: Create a directory using AWS Managed Microsoft AD

Directory Service creates a fully managed Active Directory in the AWS Cloud. When you create an
AWS Managed Microsoft AD directory, Directory Service creates two domain controllers and Domain Name System (DNS)
servers on your behalf. The directory servers are created in different subnets in a VPC.
This redundancy helps make sure that your directory remains accessible even if a failure
occurs.

When you create an AWS Managed Microsoft AD directory, Directory Service performs the following tasks on your behalf:

- Sets up an Active Directory within the VPC.
- Creates a directory administrator account with the user name Admin and the specified password. You use
  this account to manage your directory.

###### Note

Be sure to save this password. Directory Service doesn't store it. You can reset it, but you can't retrieve
it.

- Creates a security group for the directory controllers.

When you launch an AWS Managed Microsoft AD, AWS creates an Organizational Unit (OU) that contains all of your
directory's objects. This OU has the NetBIOS name that you typed when you created your directory and is
located in the domain root. The domain root is owned and managed by AWS.

The Admin account that was created with your AWS Managed Microsoft AD directory has permissions for the most common
administrative activities for your OU:

- Create, update, or delete users
- Add resources to your domain such as file or print servers, and then assign permissions for those
  resources to users in your OU
- Create additional OUs and containers
- Delegate authority
- Restore deleted objects from the Active Directory Recycle Bin
- Run AD and DNS Windows PowerShell modules on the Active Directory Web Service

The Admin account also has rights to perform the following domain-wide activities:

- Manage DNS configurations (add, remove, or update records, zones, and forwarders)
- View DNS event logs
- View security event logs

###### To create a directory with AWS Managed Microsoft AD

1. Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. In the navigation pane, choose **Directories** and choose **Set up
   Directory**.
3. Choose **AWS Managed Microsoft AD**. AWS Managed Microsoft AD is the only option that you
   can currently use with Amazon RDS.
4. Enter the following information:

**Directory DNS name**

The fully qualified name for the directory, such as
`corp.example.com`.

**Directory NetBIOS name**

The short name for the directory, such as `CORP`.

**Directory description**

(Optional) A description for the directory.

**Admin password**

The password for the directory administrator. The directory creation process creates an
administrator account with the user name Admin and this password.

The directory administrator password and can't include the word "admin."
The password is case-sensitive and must be 8–64 characters in length. It
must also contain at least one character from three of the following four
categories:

    * Lowercase letters (a–z)
    * Uppercase letters (A–Z)
    * Numbers (0–9)
    * Non-alphanumeric characters (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

**Confirm password**

The administrator password retyped. 5. Choose **Next**. 6. Enter the following information in the **Networking** section and then
choose **Next**:

**VPC**

The VPC for the directory. Create the MySQL DB instance in this same VPC.

**Subnets**

Subnets for the directory servers. The two subnets must be in different Availability Zones. 7. Review the directory information and make any necessary changes. When the information is correct, choose
**Create directory**.

![The Review & create window during directory creation in the Directory Service console.](images/WinAuth2.png)

It takes several minutes for the directory to be created. When it has been successfully created, the
**Status** value changes to **Active**.

To see information about your directory, choose the directory name in the directory
listing. Note the **Directory ID** value because you need this value when
you create or modify your MySQL DB instance.

![The Directory details section with Directory ID in the Directory Service console.](images/WinAuth3.png)

### Step 2: Create the IAM role for use by Amazon RDS

For Amazon RDS to call Directory Service for you, an IAM role that uses the managed IAM
policy `AmazonRDSDirectoryServiceAccess` is required. This role allows
Amazon RDS to make calls to the Directory Service.

When a DB instance is created using the AWS Management Console and the
console user has the `iam:CreateRole` permission, the console creates this
role automatically. In this case, the role name is `rds-directoryservice-kerberos-access-role`.
Otherwise, you must create the IAM role manually. When you create this IAM role, choose
`Directory Service`, and attach the AWS managed policy
`AmazonRDSDirectoryServiceAccess` to it.

For more information about creating IAM roles for a service, see
[Creating a role to delegate
permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Note

The IAM role used for Windows Authentication for RDS for SQL Server can't be used for
RDS for MySQL.

Optionally, you can create policies with the required permissions instead of using the
managed IAM policy `AmazonRDSDirectoryServiceAccess`. In this case, the
IAM role must have the following IAM trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "directoryservice.rds.amazonaws.com",
 "rds.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The role must also have the following IAM role policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ds:DescribeDirectories",
 "ds:AuthorizeApplication",
 "ds:UnauthorizeApplication",
 "ds:GetAuthorizedApplicationDetails"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

### Step 3: Create and configure users

You can create users with the Active Directory Users and Computers tool. This tool is part of the Active
Directory Domain Services and Active Directory Lightweight Directory Services tools. Users represent
individual people or entities that have access to your directory.

To create users in an Directory Service directory, you must be connected to an Amazon EC2 instance based on Microsoft
Windows. This instance must be a member of the Directory Service directory and be logged in as a user that has
privileges to create users. For more information, see
[Manage users and groups in AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/creating_ad_users_and_groups.md "../../../directoryservice/latest/admin-guide/creating_ad_users_and_groups.md") in the
_AWS Directory Service Administration Guide_.

### Step 4: Create or modify a MySQL DB instance

Create or modify a MySQL DB instance for use with your directory. You can use the
console, CLI, or RDS API to associate a DB instance with a directory. You can do
this in one of the following ways:

- Create a new MySQL DB instance using the console, the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") CLI command, or the [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
  RDS API operation.

For instructions, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

- Modify an existing MySQL DB instance using the console, the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") CLI command, or the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md")
  RDS API operation.

For instructions, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

- Restore a MySQL DB instance from a DB snapshot using the console, the [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md") CLI command, or the [RestoreDBInstanceFromDBSnapshot](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md") RDS API operation.

For instructions, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").

- Restore a MySQL DB instance to a point-in-time using the console, the [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md") CLI command, or the [RestoreDBInstanceToPointInTime](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md") RDS API operation.

For instructions, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

Kerberos authentication is only supported for MySQL DB instances in a VPC. The DB instance can be in the same VPC as the directory, or in a different VPC.
The DB instance must use a security group that allows egress within the directory's VPC so the DB instance can communicate with the directory.

When you use the console to create, modify, or restore a DB instance, choose **Password and Kerberos
authentication** in the **Database authentication** section. Choose **Browse
Directory** and then select the directory, or choose **Create a new directory**.

![The Database authentication section with Password and Kerberos authentication selected in the Amazon RDS console.](images/kerberos-authentication.png)

When you use the AWS CLI or RDS API, associate a DB instance with a directory. The following parameters are required for the
DB instance to use the domain directory you created:

- For the `--domain` parameter, use the domain identifier ("d-\*" identifier) generated when you created the
  directory.
- For the `--domain-iam-role-name` parameter, use the role you created that uses the managed IAM policy
  `AmazonRDSDirectoryServiceAccess`.

For example, the following CLI command modifies a DB instance to use a directory.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --domain d-`ID` \
    --domain-iam-role-name `role-name`

```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --domain d-`ID` ^
    --domain-iam-role-name `role-name`

```

###### Important

If you modify a DB instance to enable Kerberos authentication, reboot the DB instance
after making the change.

### Step 5: Create Kerberos authentication MySQL logins

Use the Amazon RDS master user credentials to connect to the MySQL DB instance as you do any other DB
instance. The DB instance is joined to the AWS Managed Microsoft AD domain. Thus, you can provision MySQL logins and
users from the Active Directory users in your domain. Database permissions are managed through
standard MySQL permissions that are granted to and revoked from these logins.

You can allow an Active Directory user to authenticate with MySQL. To do this, first
use the Amazon RDS master user credentials to connect to the MySQL DB instance as with any other
DB instance. After you're logged in, create an externally authenticated user with PAM
(Pluggable Authentication Modules) in MySQL by running the following command. Replace
`testuser` with the user name.

```
CREATE USER '`testuser`'@'%' IDENTIFIED WITH 'auth_pam';
```

Users (both humans and applications) from your domain can now connect to the DB instance from a
domain joined client machine using Kerberos authentication.

###### Important

We strongly recommended that clients use SSL/TLS connections when using PAM
authentication. If they don't use SSL/TLS connections, the password might be sent as clear
text in some cases. To require an SSL/TLS encrypted connection for your AD user, run the
following command and replace `testuser` with the
user name:

```
ALTER USER '`testuser`'@'%' REQUIRE SSL;
```

For more information, see [SSL/TLS support for MySQL DB instances on
Amazon RDS](MySQL.Concepts.md "MySQL.Concepts.md").

## Managing a DB instance in a domain

You can use the CLI or the RDS API to manage your DB instance and its relationship with your managed Active
Directory. For example, you can associate an Active Directory for Kerberos authentication and disassociate an
Active Directory to disable Kerberos authentication. You can also move a DB instance to be externally
authenticated by one Active Directory to another.

For example, using the Amazon RDS API, you can do the following:

- To reattempt enabling Kerberos authentication for a failed membership, use the
  `ModifyDBInstance` API operation and specify the current membership's
  directory ID.
- To update the IAM role name for membership, use the `ModifyDBInstance` API operation and specify
  the current membership's directory ID and the new IAM role.
- To disable Kerberos authentication on a DB instance, use the `ModifyDBInstance` API operation and
  specify `none` as the domain parameter.
- To move a DB instance from one domain to another, use the `ModifyDBInstance` API operation and
  specify the domain identifier of the new domain as the domain parameter.
- To list membership for each DB instance, use the `DescribeDBInstances` API operation.

### Understanding domain membership

After you create or modify your DB instance, it becomes a member of the domain. You can view the
status of the domain membership for the DB instance by running the
[describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") CLI command. The status
of the DB instance can be one of the following:

- `kerberos-enabled` – The DB instance has Kerberos authentication enabled.
- `enabling-kerberos` – AWS is in the process of enabling Kerberos authentication on
  this DB instance.
- `pending-enable-kerberos` – The enabling of Kerberos authentication is pending on this
  DB instance.
- `pending-maintenance-enable-kerberos` – AWS will attempt to enable Kerberos
  authentication on the DB instance during the next scheduled maintenance window.
- `pending-disable-kerberos` – The disabling of Kerberos authentication is pending on
  this DB instance.
- `pending-maintenance-disable-kerberos` – AWS will attempt to disable Kerberos
  authentication on the DB instance during the next scheduled maintenance window.
- `enable-kerberos-failed` – A configuration problem has prevented AWS
  from enabling Kerberos authentication on the DB instance. Check and fix your
  configuration before reissuing the DB instance modify command.
- `disabling-kerberos` – AWS is in the process of disabling Kerberos authentication on
  this DB instance.

A request to enable Kerberos authentication can fail because of a network connectivity issue or an incorrect
IAM role. For example, suppose that you create a DB instance or modify an existing DB instance and the attempt
to enable Kerberos authentication fails. If this happens, re-issue the modify command or modify the newly
created DB instance to join the domain.

## Connecting to MySQL with Kerberos authentication

To connect to MySQL with Kerberos authentication, you must log in using the Kerberos authentication type.

To create a database user that you can connect to using Kerberos authentication, use an `IDENTIFIED
 WITH` clause on the `CREATE USER` statement. For instructions, see
[Step 5: Create Kerberos authentication MySQL logins](#mysql-kerberos-setting-up.create-logins "#mysql-kerberos-setting-up.create-logins").

To avoid errors, use the MariaDB `mysql` client. You can download MariaDB software at [https://downloads.mariadb.org/](https://downloads.mariadb.org/ "https://downloads.mariadb.org/").

At a command prompt, connect to one of the endpoints associated with your MySQL DB instance. Follow the general procedures in
[Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md"). When you're prompted for the
password, enter the Kerberos password associated with that user name.

## Restoring a MySQL DB instance and adding it to a domain

You can restore a DB snapshot or complete a point-in-time restore for a MySQL DB instance
and then add it to a domain. After the DB instance is restored, modify the DB instance using
the process explained in [Step 4: Create or modify a MySQL DB instance](#mysql-kerberos-setting-up.create-modify "#mysql-kerberos-setting-up.create-modify") to add the DB instance to a
domain.

## Kerberos authentication MySQL limitations

The following limitations apply to Kerberos authentication for MySQL:

- Only an AWS Managed Microsoft AD is supported. However, you can join RDS for MySQL DB instances to
  shared Managed Microsoft AD domains owned by different accounts in the same AWS Region.
- You must reboot the DB instance after enabling the feature.
- The domain name length can't be longer than 61 characters.
- You can't enable Kerberos authentication and IAM authentication at the same
  time. Choose one authentication method or the other for your MySQL DB instance.
- Don't modify the DB instance port after enabling the feature.
- Don't use Kerberos authentication with read replicas.
- If you have auto minor version upgrade turned on for a MySQL DB instance that is using
  Kerberos authentication, you must turn off Kerberos authentication and then turn it back
  on after an automatic upgrade. For more information about auto minor version upgrades, see
  [Automatic minor version upgrades for RDS for MySQL](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md").
- To delete a DB instance with this feature enabled, first disable the feature. To do
  so, run the `modify-db-instance` CLI command for the DB instance and specify
  `none` for the `--domain` parameter.

If you use the CLI or RDS API to delete a DB instance with this feature enabled, expect a delay.

- RDS for MySQL doesn't support Kerberos authentication across a forest trust between your on-premise or self-hosted AD and the AWS Managed Microsoft AD.
