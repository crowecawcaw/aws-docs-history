# Setting up Windows Authentication for

SQL Server DB instances

You use AWS Directory Service for Microsoft Active Directory, also called AWS Managed Microsoft AD, to set up Windows Authentication for a
SQL Server DB instance. To set up Windows Authentication, take the following steps.

## Step 1: Create a

directory using the AWS Directory Service for Microsoft Active Directory

Directory Service creates a fully managed, Microsoft Active Directory in the AWS Cloud. When you create
an AWS Managed Microsoft AD directory, Directory Service creates two domain controllers and Domain Name
Service (DNS) servers on your behalf. The directory servers are created in two
subnets in two different Availability Zones within a VPC. This redundancy helps
ensure that your directory remains accessible even if a failure occurs.

When you create an AWS Managed Microsoft AD directory, Directory Service performs the following
tasks on your behalf:

- Sets up a Microsoft Active Directory within the VPC.
- Creates a directory administrator account with the user name Admin and
  the specified password. You use this account to manage your directory.
- Creates a security group for the directory controllers.

When you launch an AWS Directory Service for Microsoft Active Directory, AWS creates an Organizational Unit (OU) that
contains all your directory's objects. This OU, which has the NetBIOS name that you
typed when you created your directory, is located in the domain root. The domain
root is owned and managed by AWS.

The _admin_ account that was created with your
AWS Managed Microsoft AD directory has permissions for the most common administrative activities
for your OU:

- Create, update, or delete users, groups, and computers.
- Add resources to your domain such as file or print servers, and then assign permissions
  for those resources to users and groups in your OU.
- Create additional OUs and containers.
- Delegate authority.
- Create and link group policies.
- Restore deleted objects from the Active Directory Recycle Bin.
- Run AD and DNS Windows PowerShell modules on the Active Directory Web Service.

The admin account also has rights to perform the following domain-wide activities:

- Manage DNS configurations (add, remove, or update records, zones, and forwarders).
- View DNS event logs.
- View security event logs.

###### To create a directory with AWS Managed Microsoft AD

1. In the [Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation
   pane, choose **Directories** and
   choose **Set up directory**.
2. Choose **AWS Managed Microsoft AD**. This is the only option currently
   supported for use with Amazon RDS.
3. Choose **Next**.
4. On the **Enter directory information** page, provide the following information:

**Edition**

Choose the edition that meets your requirements.

**Directory DNS name**

The fully qualified name for the directory, such as `corp.example.com`.
Names longer than 47 characters aren't supported by SQL
Server.

**Directory NetBIOS name**

An optional short name for the directory, such as `CORP`.

**Directory description**

An optional description for the directory.

**Admin password**

The password for the directory administrator. The directory
creation process creates an administrator account with the user
name Admin and this password.

The directory administrator password can't include the word `admin`.
The password is case-sensitive and must be 8–64 characters in
length. It must also contain at least one character from three
of the following four categories:

    * Lowercase letters (a-z)
    * Uppercase letters (A-Z)
    * Numbers (0-9)
    * Non-alphanumeric characters
     (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)

**Confirm password**

Retype the administrator password. 5. Choose **Next**. 6. On the **Choose VPC and subnets** page, provide the following information:

**VPC**

Choose the VPC for the directory.

###### Note

You can locate the directory and the DB instance in different VPCs, but if you do so,
make sure to enable cross-VPC traffic. For more information,
see [Step 4: Enable cross-VPC traffic
between the directory and the DB instance](#USER_SQLServerWinAuth.SettingUp.VPC-Peering "#USER_SQLServerWinAuth.SettingUp.VPC-Peering").

**Subnets**

Choose the subnets for the directory servers. The two subnets must be in different
Availability Zones. 7. Choose **Next**. 8. Review the directory information. If changes are needed, choose **Previous**. When the
information is correct, choose **Create directory**.

![Review and create page](images/WinAuth2.png)

It takes several minutes for the directory to be created. When it has been
successfully created, the **Status** value changes to
**Active**.

To see information about your directory, choose the directory ID in the directory listing.
Make a note of the **Directory ID**. You need this value when you
create or modify your SQL Server DB instance.

![Directory details page](images/WinAuth3.png)

## Step 2: Create the IAM role for

use by Amazon RDS

If you use the console to create your SQL Server DB instance, you can skip this step. If
you use the CLI or RDS API to create your SQL Server DB instance, you must create an
IAM role that uses the `AmazonRDSDirectoryServiceAccess` managed IAM
policy. This role allows Amazon RDS to make calls to the Directory Service for you.

If you are using a custom policy for joining a domain, rather than using the AWS-managed
`AmazonRDSDirectoryServiceAccess` policy, make sure that you allow
the `ds:GetAuthorizedApplicationDetails` action. This requirement is
effective starting July 2019, due to a change in the Directory Service API.

The following IAM policy, `AmazonRDSDirectoryServiceAccess`, provides access to
Directory Service.

###### Example IAM policy for providing access to Directory Service

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

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource-based trust relationships to limit
the service's permissions to a specific resource. This is the most effective way to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

You might use both global condition context keys and have the `aws:SourceArn` value contain the account ID. In
this case, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the
same account ID when used in the same statement.

- Use `aws:SourceArn` if you want cross-service access for a single resource.
- Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the
  cross-service use.

In the trust relationship, make sure to use the `aws:SourceArn` global condition context key with the full
Amazon Resource Name (ARN) of the resources accessing the role. For Windows Authentication, make sure to include the DB
instances, as shown in the following example.

###### Example trust relationship with global condition context key for Windows Authentication

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rds.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": [
 "arn:aws:rds:`Region`:`my_account_ID`:db:`db_instance_identifier`"
 ]
 }
 }
 }
 ]
}`

```

Create an IAM role using this IAM policy and trust relationship. For more information about creating IAM roles, see [Creating customer managed
policies](../../../IAM/latest/UserGuide/access_policies_managed-using.md#create-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#create-managed-policy-console") in the _IAM User Guide_.

## Step 3: Create and

configure users and groups

You can create users and groups with the Active Directory Users and Computers tool. This
tool is one of the Active Directory Domain Services and Active Directory Lightweight
Directory Services tools. Users represent individual people or entities that have
access to your directory. Groups are very useful for giving or denying privileges to
groups of users, rather than having to apply those privileges to each individual
user.

To create users and groups in an Directory Service directory, you must be connected to a Windows EC2
instance that is a member of the Directory Service directory. You must also be
logged in as a user that has privileges to create users and groups. For more
information, see [Add
users and groups (Simple AD and AWS Managed Microsoft AD)](../../../directoryservice/latest/admin-guide/creating_ad_users_and_groups.md "../../../directoryservice/latest/admin-guide/creating_ad_users_and_groups.md") in the
_AWS Directory Service Administration Guide_.

## Step 4: Enable cross-VPC traffic

between the directory and the DB instance

If you plan to locate the directory and the DB instance in the same VPC, skip this step and
move on to [Step 5: Create or modify a SQL Server DB instance](#USER_SQLServerWinAuth.SettingUp.CreateModify "#USER_SQLServerWinAuth.SettingUp.CreateModify").

If you plan to locate the directory and the DB instance in different VPCs, configure
cross-VPC traffic using VPC peering or [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md").

The following procedure enables traffic between VPCs using VPC peering. Follow the
instructions in [What is VPC peering?](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md")
in the _Amazon Virtual Private Cloud Peering
Guide_.

###### To enable cross-VPC traffic using VPC peering

1. Set up appropriate VPC routing rules to ensure that network traffic can flow both
   ways.
2. Ensure that the DB instance's security group can receive inbound traffic from the
   directory's security group.
3. Ensure that there is no network access control list (ACL) rule to block traffic.

If a different AWS account owns the directory, you must share the directory.

###### To share the directory between AWS accounts

1. Start sharing the directory with the AWS account that the DB instance will be created in by following the instructions in [Tutorial: Sharing your AWS Managed Microsoft AD
   directory for seamless EC2 domain-join](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.md "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.md") in the _Directory Service Administration Guide_.
2. Sign in to the Directory Service console using the account for the DB instance, and ensure that the
   domain has the `SHARED` status before proceeding.
3. While signed into the Directory Service console using the account for the DB instance, note the
   **Directory ID** value. You use this directory ID to
   join the DB instance to the domain.

## Step 5: Create or modify a SQL Server DB instance

Create or modify a SQL Server DB instance for use with your directory. You can use the
console, CLI, or RDS API to associate a DB instance with a directory. You can do
this in one of the following ways:

- Create a new SQL Server DB instance using the console, the
  [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") CLI command, or the
  [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") RDS API operation.

For instructions, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

- Modify an existing SQL Server DB instance using the console, the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") CLI command, or the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md")
  RDS API operation.

For instructions, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

- Restore a SQL Server DB instance from a DB snapshot using the console, the [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md") CLI command, or the [RestoreDBInstanceFromDBSnapshot](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md") RDS API operation.

For instructions, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").

- Restore a SQL Server DB instance to a point-in-time using the console, the [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md") CLI command, or the [RestoreDBInstanceToPointInTime](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md") RDS API operation.

For instructions, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

Windows Authentication is only supported for SQL Server DB instances in a VPC.

For the DB instance to be able to use the domain directory that you created, the following
is required:

- For **Directory**, you must choose the domain identifier
  (`d-`ID``) generated when you
  created the directory.
- Make sure that the VPC security group has an outbound rule that lets the DB instance
  communicate with the directory.

![Microsoft SQL Server Windows Authentication directory](images/WinAuth1.png)

When you use the AWS CLI, the following parameters are required for the DB instance to be
able to use the directory that you created:

- For the `--domain` parameter, use the domain identifier
  (`d-`ID``) generated when you
  created the directory.
- For the `--domain-iam-role-name` parameter, use the role that you created that
  uses the managed IAM policy
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

## Step 6: Create Windows Authentication SQL Server logins

Use the Amazon RDS master user credentials to connect to the SQL Server DB instance as you do
any other DB instance. Because the DB instance is joined to the AWS Managed Microsoft AD domain,
you can provision SQL Server logins and users. You do this from the Active Directory
users and groups in your domain. Database permissions are managed through standard
SQL Server permissions granted and revoked to these Windows logins.

For an Active Directory user to authenticate with SQL Server, a SQL Server Windows login
must exist for the user or a group that the user is a member of. Fine-grained access
control is handled through granting and revoking permissions on these SQL Server
logins. A user that doesn't have a SQL Server login or belong to a group with
such a login can't access the SQL Server DB instance.

The ALTER ANY LOGIN permission is required to create an Active Directory SQL Server login. If you haven't created any logins
with this permission, connect as the DB instance's master user using SQL Server Authentication.

Run a data definition language (DDL) command such as the following example to create a SQL Server login for an Active
Directory user or group.

###### Note

Specify users and groups using the pre-Windows 2000 login name in the format ``domainName`\`login_name``.
You can't use a user principal name (UPN) in the format `login_name```@```DomainName`.

You can only create a Windows Authentication login on an RDS for SQL Server instance by using T-SQL statements.
You can't use the SQL Server Management studio to create a Windows Authentication login.

```
USE [master]
GO
CREATE LOGIN [`mydomain`\`myuser`] FROM WINDOWS WITH DEFAULT_DATABASE = [master], DEFAULT_LANGUAGE = [us_english];
GO
```

For more information, see [CREATE LOGIN (Transact-SQL)](https://msdn.microsoft.com/en-us/library/ms189751.aspx "https://msdn.microsoft.com/en-us/library/ms189751.aspx") in the Microsoft Developer Network documentation.

Users (both humans and applications) from your domain can now connect to the RDS for SQL Server instance from a domain-joined client machine using Windows authentication.
