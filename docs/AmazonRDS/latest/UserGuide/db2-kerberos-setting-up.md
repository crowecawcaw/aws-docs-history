# Setting up Kerberos authentication

for Amazon RDS for Db2 DB instances

You use AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to set up Kerberos authentication
for an RDS for Db2 DB instance. To set up Kerberos authentication, follow these
steps:

###### Topics

- [Step 1: Create a directory
  using AWS Managed Microsoft AD](#db2-kerberos-setting-up.create-directory "#db2-kerberos-setting-up.create-directory")
- [Step 2: Create a
  trust](#db2-kerberos-setting-up-create-forest-trust "#db2-kerberos-setting-up-create-forest-trust")
- [Step 3: Create an IAM role for
  Amazon RDS to access Directory Service](#db2-kerberos-setting-up-create-iam-role "#db2-kerberos-setting-up-create-iam-role")
- [Step 4: Create and configure
  users](#db2-kerberos-setting-up.create-users "#db2-kerberos-setting-up.create-users")
- [Step 5: Create an RDS for Db2 admin
  group in AWS Managed Microsoft AD](#db2-kerberos-setting-up-vpc-peering "#db2-kerberos-setting-up-vpc-peering")
- [Step 6: Modify DB
  parameter](#db2-kerberos-setting-up-modify-db-parameter "#db2-kerberos-setting-up-modify-db-parameter")
- [Step 7: Create or modify an
  RDS for Db2 DB instance](#db2-kerberos-setting-up-create-modify "#db2-kerberos-setting-up-create-modify")
- [Step 8: Retrieve the
  Active Directory group SID in PowerShell](#db2-kerberos-setting-up-retrieve-ad-group-sid "#db2-kerberos-setting-up-retrieve-ad-group-sid")
- [Step 9: Add SID to
  GroupName mappings to your RDS for Db2 DB instance](#db2-kerberos-setting-up-add-sid-group-mapping "#db2-kerberos-setting-up-add-sid-group-mapping")
- [Step 10: Configure a Db2
  client](#db2-kerberos-setting-up-create-logins "#db2-kerberos-setting-up-create-logins")

## Step 1: Create a directory

using AWS Managed Microsoft AD

Directory Service creates a fully managed Active Directory in the AWS Cloud. When
you create an AWS Managed Microsoft AD directory, Directory Service creates two domain controllers and DNS
servers for you. The directory servers are created in different subnets in a VPC. This
redundancy helps ensure that your directory remains accessible even if a failure occurs.

When you create an AWS Managed Microsoft AD directory, Directory Service performs the following tasks on your
behalf:

- Sets up an Active Directory within your VPC.
- Creates a directory administrator account with the username `Admin`
  and the specified password. You use this account to manage your directory.

###### Important

Make sure to save this password. Directory Service doesn't store this password, and it
can't be retrieved or reset.

- Creates a security group for the directory controllers. The security group
  must permit communication with the RDS for Db2 DB instance.

When you launch AWS Directory Service for Microsoft Active Directory, AWS creates an organizational unit (OU) that
contains all of your directory's objects. This OU, which has the NetBIOS name that you
entered when you created your directory, is located in the domain root. The domain root
is owned and managed by AWS.

The `Admin` account that was created with your AWS Managed Microsoft AD directory has
permissions for the most common administrative activities for your OU:

- Create, update, or delete users.
- Add resources to your domain such as file or print servers, and then assign
  permissions for those resources to users in your OU.
- Create additional OUs and containers.
- Delegate authority.
- Restore deleted objects from the Active Directory Recycle Bin.
- Run Active Directory and Domain Name Service (DNS) modules for
  Windows PowerShell on the Directory Service.

The `Admin` account also has rights to perform the following domain-wide
activities:

- Manage DNS configurations (add, remove, or update records, zones, and
  forwarders).
- View DNS event logs.
- View security event logs.

###### To create a directory with AWS Managed Microsoft AD

1.  Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2.  Choose **Set up directory**.
3.  Choose **AWS Managed Microsoft AD**. AWS Managed Microsoft AD is the only option
    currently supported for use with Amazon RDS.
4.  Choose **\*\***Next**\*\***.
5.  On the **\*\***Enter directory
    information**\*\*** page, provide the
    following information:
    - **Edition** – Choose the edition that meets
      your requirements.
    - **Directory DNS name**– The fully qualified name for the directory, such
      as `corp.example.com`.
    - **Directory NetBIOS name**– An optional short name for the directory, such as
      `CORP`.
    - **Directory description** – An optional
      description for the directory.
    - **Admin password**– The password for the directory administrator. The
      directory creation process creates an administrator account with the
      username `Admin` and this password.

    The directory administrator password can't include the word "admin."
    The password is case-sensitive and must be 8–64 characters in
    length. It must also contain at least one character from three of the
    following four categories:

        + Lowercase letters (a–z)
        + Uppercase letters (A–Z)
        + Numbers (0–9)
        + Nonalphanumeric characters
         (~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/)


        + Confirm password – Retype the administrator password.


        ###### Important

        Make sure that you save this password. Directory Service doesn't store
         this password, and it can't be retrieved or reset.

6.  Choose **Next**.
7.  On the **Choose VPC and subnets** page, provide the following
    information:
    - **VPC** – Choose the VPC for the directory.
      You can create the RDS for Db2 DB instance in this same VPC or in a
      different VPC.
    - **Subnets** – Choose the subnets for the
      directory servers. The two subnets must be in different Availability
      Zones.

8.  Choose **Next**.
9.  Review the directory information. If changes are needed, choose
    **Previous** and make the changes. When the information is
    correct, choose **Create directory**.

![The Review & create window during directory creation in the Directory Service console.](images/db2-create-ADS-directory.png)

It takes several minutes for the directory to be created. When it has been
successfully created, the **Status** value changes to
**Active**.

To see information about your directory, choose the directory ID under
**Directory ID**. Make a note of the **Directory
ID** value. You need this value when you create or modify your RDS for Db2 DB
instance.

![The Directory details section with Directory ID in the Directory Service console.](images/db2-ADS-directory-details.png)

## Step 2: Create a

trust

If you plan to use AWS Managed Microsoft AD only, skip to [Step 3: Create an IAM role for
Amazon RDS to access Directory Service](#db2-kerberos-setting-up-create-iam-role "#db2-kerberos-setting-up-create-iam-role").

To enable Kerberos authentication using your self-managed Active Directory, you must
create a forest trust relationship between your self-managed Active Directory and the .
A forest trust is a trust relationship between a Microsoft AD and a self-managed Active
Directory and the AWS Managed Microsoft AD created in the previous step. The trust can also be
two-way, where both Active Directories trust each other. For more information about
setting up forest trusts using Directory Service, see [When to create a trust relationship](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.md "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.md") in the _AWS Directory
Service Administration Guide_.

## Step 3: Create an IAM role for

Amazon RDS to access Directory Service

For Amazon RDS to call Directory Service for you, your AWS account needs an IAM role that uses the
managed IAM policy `AmazonRDSDirectoryServiceAccess`. This role allows
Amazon RDS to make calls to Directory Service.

When you create a DB instance using the AWS Management Console and your console user account has
the `iam:CreateRole` permission, the console creates the needed IAM role
automatically. In this case, the role name is
`rds-directoryservice-kerberos-access-role`. Otherwise, you must create
the IAM role manually. When you create this IAM role, choose `Directory
 Service`, and attach the AWS managed policy
`AmazonRDSDirectoryServiceAccess` to it.

For more information about creating IAM roles for a service, see [Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

###### Note

The IAM role used for Windows Authentication for RDS for
Microsoft SQL Server can't be used for RDS for Db2.

As an alternative to using the `AmazonRDSDirectoryServiceAccess` managed policy,
you can create policies with the required permissions. In this case, the IAM role must
have the following IAM trust policy:

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

The role must also have the following IAM role policy:

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

## Step 4: Create and configure

users

You can create users by using the Active Directory Users and Computers
tool. This is one of the Active Directory Domain Services and
Active Directory Lightweight Directory Services tools. For more
information, see [Add Users and Computers to the Active Directory domain](https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/create-an-active-directory-server#add-users-and-computers-to-the-active-directory-domain "https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/create-an-active-directory-server#add-users-and-computers-to-the-active-directory-domain") in
the Microsoft documentation. In this case, users are individuals or other
entities, such as their computers, that are part of the domain and whose identities are
being maintained in the directory.

To create users in an Directory Service directory, you must be connected to a
Windows-based Amazon EC2 instance that's a member of the Directory Service directory.
At the same time, you must be signed in as a user that has privileges to create users.
For more information, see [Create a user](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.md") in the _AWS Directory Service Administration Guide_.

## Step 5: Create an RDS for Db2 admin

group in AWS Managed Microsoft AD

RDS for Db2 doesn't support Kerberos authentication for the master user or
the two Amazon RDS reserved users `rdsdb` and `rdsadmin`. Instead, you
need to create a new group called `masterdba` in AWS Managed Microsoft AD. For more
information, see [Create a Group Account in Active Directory](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-a-group-account-in-active-directory "https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-a-group-account-in-active-directory") in the
Microsoft documentation. Any users that you add to this group will
have master user privileges.

After you enable Kerberos authentication, the master user loses the
`masterdba` role. As a result, the master user won't be able to access
the instance local user group membership unless you disable Kerberos
authentication. To continue to use the master user with password login, create a user on
AWS Managed Microsoft AD with the same name as the master user. Then, add that user to the group
`masterdba`.

## Step 6: Modify DB

parameter

If you plan to use AWS Managed Microsoft AD only, skip to [Step 7: Create or modify an
RDS for Db2 DB instance](#db2-kerberos-setting-up-create-modify "#db2-kerberos-setting-up-create-modify").

To enable Kerberos authentication using your self-managed Active Directory, you must
set the parameter `rds.active_directory_configuration` to
`AWS_MANAGED_AD_WITH_TRUST` in your parameter group. By default, this
parameter is set to `AWS_MANAGED_AD` for using AWS Managed Microsoft AD
only.

For information about modifying DB parameters, see [Modifying the parameters in
parameter groups](db2-supported-parameters.md#db2-modifying-parameter-group-parameters "db2-supported-parameters.md#db2-modifying-parameter-group-parameters").

## Step 7: Create or modify an

RDS for Db2 DB instance

Create or modify an RDS for Db2 DB instance for use with your directory. You can use the
AWS Management Console, the AWS CLI, or the RDS API to associate a DB instance with a directory. You
can do this in one of the following ways:

- Create a new RDS for Db2 DB instance using the console, the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command, or the [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") API operation. For
  instructions, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- Modify an existing RDS for Db2 DB instance using the console, the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command, or the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API operation. For instructions, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
- Restore an RDS for Db2 DB instance from a DB snapshot using the console, the
  [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md") command, or
  the [RestoreDBInstanceFromDBSnapshot](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md") API operation. For
  instructions, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
- Restore an RDS for Db2 DB instance to a point-in-time using the console, the
  [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md") command, or the
  [RestoreDBInstanceToPointInTime](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md") API operation. For
  instructions, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

Kerberos authentication is only supported for RDS for Db2 DB instances in
a VPC. The DB instance can be in the same VPC as the directory, or in a different VPC.
The DB instance must use a security group that allows ingress and egress within the
directory's VPC so the DB instance can communicate with the directory.

When you use the console to create, modify, or restore a DB instance, choose
**Password and Kerberos authentication** in
the **Database authentication** section. Then choose
**Browse Directory**. Select the directory or choose
**Create directory** to use the Directory Service.

![The Database authentication section with Password and Kerberos authentication selected in the Amazon RDS console.](images/db2-database-authentication-directory.png)
When you use the AWS CLI, the following parameters are required for the DB
instance to be able to use the directory that you created:

- For the `--domain` parameter, use the domain identifier
  ("`d-*`" identifier) generated when you created the
  directory.
- For the `--domain-iam-role-name` parameter, use the role
  you created that uses the managed IAM policy
  `AmazonRDSDirectoryServiceAccess`.
  The following example modifies a DB instance to use a directory. Replace the
  following placeholders in the example with your own values:

- `db_instance_name` – The name of your
  RDS for Db2 DB instance.
- `directory_id` – The ID of the
  AWS Directory Service for Microsoft Active Directory directory that you created.
- `role_name` – The name of the IAM
  role that you created.

```
aws rds modify-db-instance --db-instance-identifier `db_instance_name` --domain d-`directory_id` --domain-iam-role-name `role_name`
```

###### Important

If you modify a DB instance to enable Kerberos authentication,
reboot the DB instance after making the change.

## Step 8: Retrieve the

Active Directory group SID in PowerShell

A security ID (SID) uniquely identifies a security principal or security group. When a
security group or account is created in Active Directory, Active Directory assigns a SID
to the group. To retrieve the AD security group SID from Active Directory, use the
`Get-ADGroup` cmdlet in a Windows client machine that is part of the
Active Directory domain. The `Identity` parameter specifies the Active
Directory group name that you want the SID for.

The following example returns the SID of the Active Directory group
`adgroup1`.

```
C:\Users\Admin> Get-ADGroup -Identity adgroup1 | select SID

             SID
-----------------------------------------------
S-1-5-21-3168537779-1985441202-1799118680-1612
```

You must generate this mapping for all the groups that are relevant to the
database.

## Step 9: Add SID to

GroupName mappings to your RDS for Db2 DB instance

You need to add the SID to GroupName mappings created in the previous step to your
RDS for Db2 DB instance. For each mapping, call the following stored procedure. Replace the
`SID` and `group_name` with your
own information.

```
db2 connect to rdsadmin
db2 "call rdsadmin.set_sid_group_mapping(?, '`SID`','`group_name`')"
```

For more information, see [rdsadmin.set_sid_group_mapping](db2-sp-granting-revoking-privileges.md#db2-sp-set-sid-group-mapping "db2-sp-granting-revoking-privileges.md#db2-sp-set-sid-group-mapping").

For information about checking the task status, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

## Step 10: Configure a Db2

client

###### To configure a Db2 client

1. Create an **/etc/krb5.conf** file (or equivalent)
   to point to the domain.

###### Note

For Windows operating systems, create a **C:\windows\krb5.ini** file. 2. Verify that traffic can flow between the client host and Directory Service. Use a network
utility such as Netcat for the following tasks:

    1. Verify traffic over DNS for port 53.
    2. Verify traffic over TCP/UDP for port 53 and for
     Kerberos, which includes ports 88 and 464 for
     Directory Service.

3. Verify that traffic can flow between the client host and the DB instance over
   the database port. You can use the command `db2` to connect and
   access the database.

The following example is /etc/krb5.conf file content for AWS Managed Microsoft AD:

```
[libdefaults]
default_realm = EXAMPLE.COM
[realms]
EXAMPLE.COM = {
kdc = example.com
admin_server = example.com
}
[domain_realm]
.example.com = EXAMPLE.COM
example.com = EXAMPLE.COM
```
