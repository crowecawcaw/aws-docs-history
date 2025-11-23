# Windows user setup for Amazon EC2 High Availability for SQL Server

###### Note

You only need to perform the steps in this section if you choose to use the default,
built-in `[NT AUTHORITY\SYSTEM]` user as described in [Step 3: Store SQL Server credentials in AWS Secrets Manager](sql-high-availability-get-started.md#sql-high-availability-secret "sql-high-availability-get-started.md#sql-high-availability-secret"). If you choose to store custom SQL Server
credentials in AWS Secrets Manager, these Windows user setup steps are not required.

Amazon EC2 High Availability for SQL Server uses AWS Systems Manager (SSM) to connect to Amazon EC2 instances and obtain SQL Server
High Availability metadata. The SSM command runs under the context of the default local user on the Amazon EC2
instance: `NT AUTHORITY\SYSTEM`. If you performed post-launch lockdowns
on your SQL Server instances by removing certain default SQL Server permissions and built-in groups,
you may need to perform a few steps to grant required permissions to `NT AUTHORITY\SYSTEM`.

Additionally, when enabling your Amazon EC2 instances for SQL HA standby detection,
you can optionally provide an AWS secret containing credentials to a Windows domain user or local
user on your Amazon EC2 instances other than the default local user, `NT AUTHORITY\SYSTEM`.
The service uses this provided Windows user to connect to all SQL Server instances on the Amazon EC2
instance and run SQL Server queries to obtain High Availability metadata. This guide explains how to either grant
required permissions to `NT AUTHORITY\SYSTEM`, or how to create a Windows domain or
local user with least permissions required for the service to process Amazon EC2 instances enabled for
SQL HA standby detection, and how to create an AWS secret containing credentials for this user.

###### Topics

- [Option 1: Grant required permissions to the [NT AUTHORITY\SYSTEM] user](#sql-ha-default-local-user "#sql-ha-default-local-user")
- [Option 2: Create new domain user with required permissions](#sql-ha-domain-user "#sql-ha-domain-user")
- [Option 3: Create new local user with require permissions](#sql-ha-local-user "#sql-ha-local-user")

## Option 1: Grant required permissions to the [NT AUTHORITY\SYSTEM] user

This section covers the most straightforward setup to begin enabling Amazon EC2 instances for
SQL HA standby detection. If you follow this section, you need not provide an AWS secret
when enabling your Amazon EC2 instances for SQL HA standby detection, since SSM will use the
default local user `NT AUTHORITY\SYSTEM` to authenticate into SQL Server.

Since SQL Server license-included AMIs allow `NT AUTHORITY\SYSTEM` to authenticate
into SQL Server by default, the following steps may not be required to enable your instances for
SQL HA standby detection. However, if you performed post-launch lockdowns on your
SQL Server instances, you may need to grant least permissions back to `NT AUTHORITY\SYSTEM`
for the service to obtain High Availability metadata.

###### To grant SQL Server access for NT AUTHORITY\SYSTEM

The following steps need to be repeated on every SQL Server instance on the Amazon EC2 instance.
Amazon EC2 SQL HA obtains High Availability metadata on all SQL Server installs on the Amazon EC2 instance, so the
default local user needs to be able to query SQL Server across all SQL Server instances.

- Connect to your Amazon EC2 instance and open SQL Server Management Studio, then run the
  following SQL Server command on each SQL Server instance. This command creates a SQL Server login
  for `NT AUTHORITY\SYSTEM` and grants minimal read-only SQL Server permissions
  for this user.

```
-- Create SQL Server login for default local user
IF NOT EXISTS (SELECT name FROM master.sys.server_principals WHERE name = 'NT AUTHORITY\SYSTEM')
BEGIN
    CREATE LOGIN [NT AUTHORITY\SYSTEM] FROM WINDOWS WITH DEFAULT_DATABASE=[master]
END

USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.sysusers WHERE name = 'NT AUTHORITY\SYSTEM')
BEGIN
    CREATE USER [NT AUTHORITY\SYSTEM] FOR LOGIN [NT AUTHORITY\SYSTEM]
END
GO

-- Grant database permissions
USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.database_principals WHERE name = 'db_role_ec2_sql_ha')
BEGIN
    CREATE ROLE [db_role_ec2_sql_ha]
END

GRANT VIEW DATABASE STATE to [db_role_ec2_sql_ha]
GO

ALTER ROLE [db_role_ec2_sql_ha] ADD MEMBER [NT AUTHORITY\SYSTEM]
GO

-- Grant server permissions
USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.server_principals WHERE name = 'svr_role_ec2_sql_ha')
BEGIN
    CREATE SERVER ROLE [svr_role_ec2_sql_ha]
END

GRANT VIEW SERVER STATE TO [svr_role_ec2_sql_ha]
GRANT VIEW ANY DEFINITION TO [svr_role_ec2_sql_ha]
GRANT VIEW ANY DATABASE TO [svr_role_ec2_sql_ha]
GO

ALTER SERVER ROLE [svr_role_ec2_sql_ha] ADD MEMBER [NT AUTHORITY\SYSTEM]
GO
```

Your default local user setup is complete. You can now enable SQL HA standby detection
for your Amazon EC2 instances.

## Option 2: Create new domain user with required permissions

This section covers how to create a Windows domain user with the necessary permissions to
connect to SQL Server and obtain High Availability metadata. This option is preferred over creating a new local
user, as the domain user can be used for any Amazon EC2 instance joined to the domain. This allows
you to supply just one AWS secret for multiple Amazon EC2 instances enabled for SQL HA standby
detection.

###### To create and configure a domain user

1. **Create a domain user**

This step differs based on the type of Active Directory (AD) being used, and assumes
the Amazon EC2 instances you wish to enable for SQL HA standby detection are already joined
to this domain. For an AWS managed Microsoft AD, use the following AWS AWS CLI commands
to create a new domain user. Replace `username` and
`password` with your desired username and password.

```
aws ds-data create-user \
    --directory-id `directory-id` \
    --sam-account-name "`username`"
```

Then assign a password to the domain user:

```
aws ds reset-user-password \
    --directory-id `directory-id` \
    --user-name "`username`" \
    --new-password "`password`"
```

2. **Create an AWS secret containing credentials**

Save the Windows domain user credentials to an AWS secret. The domain user's username
must be saved in the following format: ``directory-netBIOS-name`\`username``.
The `directory-netBIOS-name` is the directory NetBIOS name of your AD.

```
aws secretsmanager create-secret \
    --name "domain-user-credentials" \
    --description "Domain user credentials for EC2 SQL HA standby detection." \
    --secret-string "{\"username\":\"`directory-netBIOS-name`\\`username`\",\"password\":\"`password`\"}"
```

3. **Grant SQL Server access for domain user**

Connect to your Amazon EC2 instance and open SQL Server Management Studio, then run the following
SQL Server command on each SQL Server instance. Replace `username` with the
username you selected and `directory-netBIOS-name` with the AD's
directory NetBIOS name.

```
-- Create SQL Server login for domain user
IF NOT EXISTS (SELECT name FROM master.sys.server_principals WHERE name = '`directory-netBIOS-name`\`username`')
BEGIN
    CREATE LOGIN [`directory-netBIOS-name`\`username`] FROM WINDOWS WITH DEFAULT_DATABASE=[master]
END

USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.sysusers WHERE name = '`directory-netBIOS-name`\`username`')
BEGIN
    CREATE USER [`directory-netBIOS-name`\`username`] FOR LOGIN [`directory-netBIOS-name`\`username`]
END
GO

-- Grant database permissions
USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.database_principals WHERE name = 'db_role_ec2_sql_ha')
BEGIN
    CREATE ROLE [db_role_ec2_sql_ha]
END

GRANT VIEW DATABASE STATE to [db_role_ec2_sql_ha]
GO

ALTER ROLE [db_role_ec2_sql_ha] ADD MEMBER [`directory-netBIOS-name`\`username`]
GO

-- Grant server permissions
USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.server_principals WHERE name = 'svr_role_ec2_sql_ha')
BEGIN
    CREATE SERVER ROLE [svr_role_ec2_sql_ha]
END

GRANT VIEW SERVER STATE TO [svr_role_ec2_sql_ha]
GRANT VIEW ANY DEFINITION TO [svr_role_ec2_sql_ha]
GRANT VIEW ANY DATABASE TO [svr_role_ec2_sql_ha]
GO

ALTER SERVER ROLE [svr_role_ec2_sql_ha] ADD MEMBER [`directory-netBIOS-name`\`username`]
GO
```

Your domain user setup is complete. When enabling Amazon EC2 instances for SQL HA standby
detection, you can supply the ARN for the AWS secret you created.

## Option 3: Create new local user with require permissions

This section covers how to create a Windows local user restricted to a single Amazon EC2 instance
with the necessary permissions to connect to SQL Server and obtain High Availability metadata.

###### To create and configure a local user

1. **Create a local user on the Amazon EC2 instance**

Connect to your Amazon EC2 instance and open PowerShell as Administrator, then execute the
following command. Replace `username` and `password`
with your desired username and password.

```
New-LocalUser -Name "`username`" -Password (ConvertTo-SecureString "`password`" -AsPlainText -Force) -Description "Local user for EC2 SQL HA standby detection."
```

2. **Create an AWS secret containing credentials**

Save the Windows local user credentials to an AWS secret.

```
aws secretsmanager create-secret \
    --name "local-user-credentials" \
    --description "Local user credentials for EC2 SQL HA standby detection." \
    --secret-string "{\"username\":\"`username`\",\"password\":\"`password`\"}"
```

3. **Grant SQL Server access for local user**

Connect to your Amazon EC2 instance and open SQL Server Management Studio, then run the following
SQL Server command on each SQL Server instance. Replace `username` with the
username you selected and `COMPUTERNAME` with the Amazon EC2 instance
computer name. You can retrieve the computer name with the PowerShell command
`$env:COMPUTERNAME`.

```
-- Create SQL Server login for local user
IF NOT EXISTS (SELECT name FROM master.sys.server_principals WHERE name = '`COMPUTERNAME`\`username`')
BEGIN
    CREATE LOGIN [`COMPUTERNAME`\`username`] FROM WINDOWS WITH DEFAULT_DATABASE=[master]
END

USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.sysusers WHERE name = '`COMPUTERNAME`\`username`')
BEGIN
    CREATE USER [`COMPUTERNAME`\`username`] FOR LOGIN [`COMPUTERNAME`\`username`]
END
GO

-- Grant database permissions
USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.database_principals WHERE name = 'db_role_ec2_sql_ha')
BEGIN
    CREATE ROLE [db_role_ec2_sql_ha]
END

GRANT VIEW DATABASE STATE to [db_role_ec2_sql_ha]
GO

ALTER ROLE [db_role_ec2_sql_ha] ADD MEMBER [`COMPUTERNAME`\`username`]
GO

-- Grant server permissions
USE [master]
GO

IF NOT EXISTS (SELECT name FROM master.sys.server_principals WHERE name = 'svr_role_ec2_sql_ha')
BEGIN
    CREATE SERVER ROLE [svr_role_ec2_sql_ha]
END

GRANT VIEW SERVER STATE TO [svr_role_ec2_sql_ha]
GRANT VIEW ANY DEFINITION TO [svr_role_ec2_sql_ha]
GRANT VIEW ANY DATABASE TO [svr_role_ec2_sql_ha]
GO

ALTER SERVER ROLE [svr_role_ec2_sql_ha] ADD MEMBER [`COMPUTERNAME`\`username`]
GO
```

Your local user setup is complete. When enabling Amazon EC2 instances for SQL HA standby
detection, you can supply the ARN for the AWS secret you created.
