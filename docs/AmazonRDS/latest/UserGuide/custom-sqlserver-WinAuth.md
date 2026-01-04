# Setting up Windows Authentication for RDS Custom for SQL Server instances

We recommend creating a dedicated OU and service credentials scoped to that OU for any AWS account that owns an RDS Custom for SQL Server DB instance
joined to your AD domain. By dedicating an OU and service credentials, you avoid conflicting permissions and follow the principle of least privilege.

Active directory level group policies might conflict with AWS automations and permissions. We recommend selecting GPO's that apply only to
the OU that you create for RDS Custom for SQL Server.

- To create OU and AD domain user in your self-managed or on-premise AD, you can connect the domain controller as a domain administrator.
- To create users and groups in an Directory Service directory, you must be connected to a management instance and you must also be logged in as a user with privileges to create users and groups.
  For more information, see [User and group management in AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md") in the
  _AWS Directory Service Administration Guide_.
- To manage your Active Directory from Amazon EC2 Windows Server instance, you need to install the Active Directory domain services and Active Directory Lightweight Directory services tools on the EC2 instance. For more information,
  see [Installing Active Directory Administration Tools for AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md "../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md") in the _AWS Directory Service Administration Guide_.
- We recommend that you install these tools on a separate EC2 instance for administration, and not on your RDS Custom for SQL Server DB instance for ease of administration.
  The following are the requirements for an AD domain service account:

- You must have a service account in your AD domain with delegated permissions to join computers to the domain.
  A domain service account is a user account in your AD that has delegated permission to perform certain tasks.
- Delegate the following permissions to your domain service account in the Organizational Unit that you're joining your RDS Custom for SQL Server instance to:
  - Validated ability to write to the DNS host name
  - Validated ability to write to the service principal name
  - Create and delete computer objects

- For self-managed and on-premises AD, the domain service account must be a member of the "AWS Delegated Domain Name System Administrators" group.
- For AWS Managed Microsoft AD, the domain service account should be member of "DnsAdmins" group.
  These are the minimum set of permissions required to join computer objects to your self-managed AD and AWS Managed Microsoft AD.
  For more information, see [Error: Access is denied when non-administrator users who have been delegated control try to join computers to a domain controller](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/access-denied-when-joining-computers "https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/access-denied-when-joining-computers") in the Microsoft Windows Server documentation.

###### Important

Do not move computer objects that RDS Custom for SQL Server creates in the Organizational Unit (OU) after your DB instance is created.
Moving associated objects might cause your RDS Custom for SQL Server DB instance to become misconfigured.
If you need to move the computer objects created by Amazon RDS, use the
[ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") action to modify
the domain parameters with the desired location of the computer objects.

###### Topics

- [Step 1: Create an organizational unit (OU) in your AD](#custom-sqlserver-WinAuth.settingUp.CreateOU "#custom-sqlserver-WinAuth.settingUp.CreateOU")
- [Step 2: Create an AD domain user](#custom-sqlserver-WinAuth.settingUp.ADuser "#custom-sqlserver-WinAuth.settingUp.ADuser")
- [Step 3: Delegate control to the AD user in self-managed or AWS Managed Microsoft AD](#custom-sqlserver-WinAuth.settingUp.Delegate "#custom-sqlserver-WinAuth.settingUp.Delegate")
- [Step 4: Create a secret](#custom-sqlserver-WinAuth.settingUp.ASM "#custom-sqlserver-WinAuth.settingUp.ASM")
- [Step 5: Create or modify a RDS Custom for SQL Server DB instance](#custom-sqlserver-WinAuth.settingUp.CreateDBInstance "#custom-sqlserver-WinAuth.settingUp.CreateDBInstance")
- [Step 6: Create Windows Authentication SQL Server Login](#custom-sqlserver-WinAuth.settingUp.CreateLogins "#custom-sqlserver-WinAuth.settingUp.CreateLogins")
- [Step 7: Using Kerberos or NTLM Authentication](#custom-sqlserver-WinAuth.settingUp.KerbNTLM "#custom-sqlserver-WinAuth.settingUp.KerbNTLM")

## Step 1: Create an organizational unit (OU) in your AD

Use the following steps to create an organization unit in your AD:

###### Create an OU in your AD

1. Connect to your domain AD as a domain administrator.
2. Open **Active Directory Users and Computers** and select the domain where you want to create your OU.
3. Right-click the domain and choose **New**, then **Organization Unit**.
4. Enter a name for the OU.

Enable **Protect container from accidental deletion**. 5. Choose **OK**. Your new OU appears under your domain.

For AWS Managed Microsoft AD, the name of this OU is based off the NetBIOS name you typed when you created your directory.
This OU is owned by AWS and contains all of your AWS-related directory objects, which you are granted full control over.
By default, two child OUs exist under this OU, namely **Computers and Users**.
New OUs that RDS Custom creates are a child of the OU that is based off of the NetBIOS.

## Step 2: Create an AD domain user

The domain user credentials are used for the secret in Secrets Manager.

###### Create an AD domain user in your AD

1. Open **Active Directory Users and Computers** and select the domain
   and OU where you want to create the user.
2. Right-click the **Users** object and choose **New**, then **User**.
3. Enter a first name, last name, and login name for the user. Click **Next**.
4. Enter a password for the user. Don't select **User must change password at next login** or
   **Account is disabled.**. Click **Next**.
5. Click **OK**. You new user appears under your domain.

## Step 3: Delegate control to the AD user in self-managed or AWS Managed Microsoft AD

###### To delegate control to the AD domain user in your domain

1. Open **Active Directory Users and Computers** MMC snap-in and select your domain.
2. Right-click on the OU you created earlier and choose **Delegate Control**.
3. In the **Delegation Control Wizard**, click **Next**.
4. In **Users or Groups** section, click **Add**.
5. In **Select Users, Computers, or Groups**, enter the AD user you created and click **Check Names**. If your AD user check is successful, click **OK**.
6. In the **Users or Groups** section, confirm your AD user was added and click **Next**.
7. In the **Tasks to Delegate** section, choose **Create a custom task to delegate** and click **Next**.
8. In the **Active Directory Object Type** section:

Choose **ONly the following objects in the folder**.

Select **Computer Objects**

Select **Create selected objects in this folder**

Select **Delete selected objects in this folder** and click **Next**. 9. In the **Permissions** section:

Keep **General** selected.

Select **Validated write to DNS host name**.

Select **Validated write to service principal name** and click **Next**. 10. In **Completing the Delegation of Control Wizard**, confirm your settings and click **Finish**.

## Step 4: Create a secret

Create the secret in the same AWS account and Region that contains the RDS Custom for SQL Server DB instance that you want to include in your active
directory. Store credentials of the AD domain user created in [Step 2: Create an AD domain user](#custom-sqlserver-WinAuth.settingUp.ADuser "#custom-sqlserver-WinAuth.settingUp.ADuser").

Console

- In AWS Secrets Manager, choose **Store a new secret**.
- For **Secret type**, choose **Other type of secret**.
- For **Key/value pairs**, add two keys:
  - The first key, `SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME` and enter
    the name of your AD user (without the domain prefix) for the value.
  - For the second key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD` and enter the
    password for your AD user on your domain.

- For **Encryption key**, enter the same AWS KMS key you used to create RDS Custom for SQL Server instance.
- For **Secret name**, choose the secret name starting with `do-not-delete-rds-custom-`
  to allow your instance profile to access this secret. IF you want to choose a different name for the secret,
  update `RDSCustomInstanceProfile` to access **Secret name**.
- (Optional) For **Description**, enter a description for the secret name.
- Add the tags `Key="AWSRDSCustom",Value="custom-sqlserver"`
- Click **Save**, then **Next**.
- For **Configure rotation settings**, keep the default values and choose **Next**.
- Review the settings for the secret and click **Store**.
- Choose the new secret and copy the value for **Secret ARN**. We use this in the next step to set up you Active Directory.

CLI
Run the following command in your CLI to create a secret:

```
# Linux based
aws secretsmanager create-secret \
--name do-not-delete-rds-custom-`DomainUserCredentails` \
--description "Active directory user credentials for managing RDS Custom" \
--secret-string "{\"SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME\":\`"tester\"`,\"SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD\":\`"xxxxxxxx\"`}" \
--kms-key-id <RDSCustomKMSKey> \
--tags Key="AWSRDSCustom",Value="custom-sqlserver"

# Windows based
aws secretsmanager create-secret ^
--name do-not-delete-rds-custom-`DomainUserCredentails` ^
--description "Active directory user credentials for managing RDS Custom" ^
--secret-string "{\"SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME\":\`"tester\"`,\"SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD\":\`"xxxxxxxx\"`}" ^
--kms-key-id <RDSCustomKMSKey> ^
--tags Key="AWSRDSCustom",Value="custom-sqlserver"

```

## Step 5: Create or modify a RDS Custom for SQL Server DB instance

Create or modify a RDS Custom for SQL Server DB instance for use with your directory. You can use the
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

###### Note

If your RDS Custom for SQL Server instance is already joined to an AD manually, check the settings for [Network configuration port rules](custom-sqlserver-WinAuth.md "custom-sqlserver-WinAuth.md"),
[Network Validation](custom-sqlserver-WinAuth.md "custom-sqlserver-WinAuth.md"), and complete steps 1 though Step 4.
Update the `--domain-fqdn`, `--domain-ou`, and
`--domain-auth-secret-arn` to your AD, so that domain
join credentials and configurations are registered with
RDS Custom to monitor, register CNAME, and take recovery actions.

When you use the AWS CLI, the following parameters are required for the DB instance to be
able to use the directory that you created:

- For the `--domain-fqdn` parameter, use the fully qualified domain name
  of your self-managed AD.
- For the `--domain-ou` parameter, use the OU that you created in your self-managed AD.
- For the `--domain-auth-secret-arn` parameter, use the value of the **Secret ARN** that you created.

###### Important

If you modify a DB instance to join or remove from a self-managed AD domain or AWS Managed Microsoft AD,
a reboot of the DB instance is required for the modification to take effect. You can choose to
apply the changes immediately or wait until the next maintenance window.
Choosing the **Apply Immediately** option causes downtime for a single-AZ DB instance.
A Multi-AZ DB cluster performs a failover before completing a reboot. For more information, see
[Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

The following CLI command creates a new RDS Custom for SQL Server DB instance and joins it to self-managed or AWS Managed Microsoft AD domain.

For Linux, macOS, or Unix:

```
aws rds create-db-instance  \
--engine custom-sqlserver-se \
--engine-version 15.00.4312.2.v1 \
--db-instance-identifier `my-custom-instance` \
--db-instance-class db.m5.large \
--allocated-storage 100 --storage-type io1 --iops 1000 \
--master-username `my-master-username` \
--master-user-password `my-master-password` \
--kms-key-id  `my-RDSCustom-key-id` \
--custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance`  \
--domain-fqdn `"corp.example.com"` \
--domain-ou `"OU=RDSCustomOU,DC=corp,DC=example,DC=com"` \
--domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:do-not-delete-rds-custom-my-AD-test-secret-123456"` \
--db-subnet-group-name `my-DB-subnet-grp` \
--vpc-security-group-ids  `my-securitygroup-id` \
--no-publicly-accessible \
--backup-retention-period 3 \
--port 8200 \
--region us-west-2 \
--no-multi-az

```

For Windows:

```
aws rds create-db-instance  ^
--engine custom-sqlserver-se ^
--engine-version 15.00.4312.2.v1 ^
--db-instance-identifier `my-custom-instance` ^
--db-instance-class db.m5.large ^
--allocated-storage 100 --storage-type io1 --iops 1000 ^
--master-username`my-master-username` ^
--master-user-password `my-master-password` ^
--kms-key-id  `my-RDSCustom-key-id` ^
--custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance`  ^
--domain-fqdn `"corp.example.com"` ^
--domain-ou `"OU=RDSCustomOU,DC=corp,DC=example,DC=com"` ^
--domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:do-not-delete-rds-custom-my-AD-test-secret-123456"` ^
--db-subnet-group-name `my-DB-subnet-grp` ^
--vpc-security-group-ids  `my-securitygroup-id` ^
--no-publicly-accessible ^
--backup-retention-period 3 ^
--port 8200 ^
--region us-west-2 ^
--no-multi-az
```

###### Important

If your NetBIOS for AWS Managed Microsoft AD is **corpexample**, then it appears as an OU itself.
Any new OU created earlier will appear as a nested OU. For AWS Managed Microsoft AD, set `--domain-ou` to
`"OU=RDSCustomOU,OU=corpexample,DC=corp,DC=example,DC=com"`.

The following command modifies an existing RDS Custom for SQL Server DB instance to use an Active Directory domain.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --domain-fqdn `"corp.example.com"` \
    --domain-ou `"OU=RDSCustomOU,DC=corp,DC=example,DC=com"` \
    --domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:do-not-delete-rds-custom-my-AD-test-secret-123456"` \

```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --domain-fqdn `"corp.example.com"` ^
    --domain-ou `"OU=RDSCustomOU,DC=corp,DC=example,DC=com"` ^
    --domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:do-not-delete-rds-custom-my-AD-test-secret-123456"` ^

```

The following CLI command removes and RDS Custom for SQL Server DB instance from a Active Directory domain.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --disable-domain
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --disable-domain
```

When using the console to create or modify your instance, click on **Enable Microsoft SQL Server Windows Authentication** to see the following options.

![Microsoft SQL Server Windows Authentication directory](images/custom-sqs-WinAuth.png)

You are responsible to make sure your domain FQDN is resolving to the domain controller IP addresses. If domain controller IPs are not resolving,
domain join operations fail but RDS Custom for SQL Server instance creation succeeds. For troubleshooting information, see [Troubleshooting Active Directory](custom-sqlserver-WinAuth.md "custom-sqlserver-WinAuth.md").

## Step 6: Create Windows Authentication SQL Server Login

Use the Amazon RDS master user credentials to connect to the SQL Server DB instance as you do for any other DB instance.
Because the DB instance is joined to the AD domain, you can provision SQL Server logins and users.
You do this from the AD users and groups utility in your AD domain.
Database permissions are managed through standard SQL Server permissions granted
and revoked to these Windows logins.

For an AD user to authenticate with SQL Server, a SQL Server Windows login must exist
for the AD user or an Active Directory group that the user is a member of.
Fine-grained access control is handled through granting and revoking permissions on these SQL Server logins.
An AD user that doesn't have a SQL Server login or belong to an AD group
with such a login can't access the SQL Server DB instance.

The `ALTER ANY LOGIN` permission is required to create an AD SQL Server login.
If you haven't created any logins with this permission, connect as the DB instance's master user using
SQL Server Authentication and create your AD SQL Server logins
under the context of the master user.

You can run a data definition language (DDL) command such as the following to create a SQL Server login for an AD user or group.

```
USE [master]
GO
CREATE LOGIN [mydomain\myuser] FROM WINDOWS WITH DEFAULT_DATABASE = [master], DEFAULT_LANGUAGE = [us_english];
GO
```

Users (both humans and applications) from your domain can now connect to
the RDS Custom for SQL Server instance from a domain-joined client machine using Windows authentication.

## Step 7: Using Kerberos or NTLM Authentication

### NTLM authentication using RDS endpoint

Each Amazon RDS DB instance has an endpoint and each endpoint has a DNS name and port number for the DB instance. To connect to your DB instance
using a SQL client application, you need the DNS name and port number for your DB instance.
To authenticate using NTLM authentication, you must connect to the RDS endpoint.

During planned database maintenance or unplanned service disruption, Amazon RDS automatically fails over to the up-to-date
secondary database so operations can resume quickly without manual intervention. The primary and secondary instances use the same endpoint,
whose physical network address transitions to the secondary as part of the failover process. You don't have to reconfigure your application when a failover occurs.

### Kerberos authentication

Kerberos-based authentication for RDS Custom for SQL Server requires connections be made to a specific Service Principal Name (SPN).
However, after a failover event, the application might not be aware of the new SPN.
To address this, RDS Custom for SQL Server offers a Kerberos-based endpoint.

The Kerberos-based endpoint follows a specific format.
If your RDS endpoint is ``rds-instance-name`.`account-region-hash`.`aws-region`.rds.amazonaws.com`, 
 the corresponding Kerberos-based endpoint would be 
 ``rds-instance-name`.`account-region-hash`.`aws-region`.awsrds.`fully qualified domain name (FQDN)``.

For example, if the RDS endpoint is `ad-test.cocv6zwtircu.us-east-1.rds.amazonaws.com` and the
domain name is `corp-ad.company.com`, the Kerberos-based endpoint would be `ad-test.cocv6zwtircu.us-east-1.awsrds.corp-ad.company.com`.

This Kerberos-based endpoint can be used to authenticate with the SQL Server instance using Kerberos,
even after a failover event, as the endpoint is automatically updated to point to the new SPN of the primary SQL Server instance.

### Finding your CNAME

To find your CNAME, connect to your domain controller and open **DNS Manager**. Navigate to **Forward Lookup Zones** and your FQDN.

Navigate through **awsrds**, **aws-region**, and **account and region specific hash**.

If you are connecting the RDS Custom EC2 instance and trying to connect to the database locally using CNAME, your connection will use NTLM authentication instead of Kerberos.

If after connecting CNAME from remote client, an NTLM connection is returned, check if required ports are allowlisted.

To check if your connection is using Kerberos, run the following query:

```
SELECT net_transport, auth_scheme
    FROM sys.dm_exec_connections
    WHERE session_id = @@SSPID;
```
