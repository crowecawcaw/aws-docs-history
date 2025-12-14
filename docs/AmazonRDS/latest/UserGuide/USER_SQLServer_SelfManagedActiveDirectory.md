# Joining your DB instance to self-managed Active Directory

To join your RDS for SQL Server DB instance to your self-managed AD, follow these steps:

## Step 1: Create or modify a SQL Server DB instance

You can use the console, CLI, or RDS API to associate an RDS for SQL Server DB instance with a self-managed AD domain. You can do
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

When you use the AWS CLI, the following parameters are required for the DB instance to be
able to use the self-managed AD domain that you created:

- For the `--domain-fqdn` parameter, use the fully qualified domain name (FQDN)
  of your self-managed AD.
- For the `--domain-ou` parameter, use the OU that you created in your self-managed AD.
- For the `--domain-auth-secret-arn` parameter, use the value of the **Secret ARN** that you created in a previous step.
- For the `--domain-dns-ips` parameter, use the primary and secondary IPv4 addresses of the DNS servers for your self-managed AD.
  If you don't have a secondary DNS server IP address, enter the primary IP address twice.

The following example CLI commands show how to create, modify, and remove an RDS for SQL Server DB instance with a self-managed AD domain.

###### Important

If you modify a DB instance to join it to or remove it from a self-managed AD domain, a reboot of the DB instance
is required for the modification to take effect. You can choose to apply the changes immediately or wait until the next maintenance window. Choosing the **Apply Immediately** option
will cause downtime for a single-AZ DB instance. A multi-AZ DB instance will perform a failover before completing a reboot. For more information, see [Using the schedule modifications
setting](USER_ModifyInstance.md "USER_ModifyInstance.md").

The following CLI command creates a new RDS for SQL Server DB instance and joins it to a self-managed AD domain.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `my-DB-instance` \
    --db-instance-class `db.m5.xlarge` \
    --allocated-storage `50` \
    --engine `sqlserver-se` \
    --engine-version `15.00.4043.16.v1` \
    --license-model `license-included` \
    --master-username `my-master-username` \
    --master-user-password `my-master-password` \
    --domain-fqdn `my_AD_domain.my_AD.my_domain` \
    --domain-ou `OU=my-AD-test-OU,DC=my-AD-test,DC=my-AD,DC=my-domain` \
    --domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:my-AD-test-secret-123456"` \
    --domain-dns-ips `"10.11.12.13" "10.11.12.14"`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `my-DB-instance` ^
    --db-instance-class `db.m5.xlarge` ^
    --allocated-storage `50` ^
    --engine `sqlserver-se` ^
    --engine-version `15.00.4043.16.v1` ^
    --license-model `license-included` ^
    --master-username `my-master-username` ^
    --master-user-password `my-master-password` ^
    --domain-fqdn `my-AD-test.my-AD.mydomain` ^
    --domain-ou `OU=my-AD-test-OU,DC=my-AD-test,DC=my-AD,DC=my-domain` ^
    --domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:my-AD-test-secret-123456" \` ^
    --domain-dns-ips `"10.11.12.13" "10.11.12.14"`
```

The following CLI command modifies an existing RDS for SQL Server DB instance to use a self-managed AD domain.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-DB-instance` \
    --domain-fqdn `my_AD_domain.my_AD.my_domain` \
    --domain-ou `OU=my-AD-test-OU,DC=my-AD-test,DC=my-AD,DC=my-domain` \
    --domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:my-AD-test-secret-123456"` \
    --domain-dns-ips `"10.11.12.13" "10.11.12.14"`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-DBinstance` ^
    --domain-fqdn `my_AD_domain.my_AD.my_domain` ^
    --domain-ou `OU=my-AD-test-OU,DC=my-AD-test,DC=my-AD,DC=my-domain` ^
    --domain-auth-secret-arn `"arn:aws:secretsmanager:region:account-number:secret:my-AD-test-secret-123456"` ^
    --domain-dns-ips `"10.11.12.13" "10.11.12.14"`
```

The following CLI command removes an RDS for SQL Server DB instance from a self-managed AD domain.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-DB-instance` \
    --disable-domain
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-DB-instance` ^
    --disable-domain
```

## Step 2: Using Kerberos or NTLM Authentication

### NTLM authentication

Each Amazon RDS DB instance has an endpoint and each endpoint has a DNS name and port number for the DB instance. To connect to your DB instance
using a SQL client application, you need the DNS name and port number for your DB instance.
To authenticate using NTLM authentication, you must connect to the RDS endpoint or the listener endpoint
if you are using a Multi-AZ deployment.

During planned database maintenance or unplanned service disruption, Amazon RDS automatically fails over to the up-to-date
secondary database so operations can resume quickly without manual intervention. The primary and secondary instances use the same endpoint,
whose physical network address transitions to the secondary as part of the failover process. You don't have to reconfigure your application when a failover occurs.

### Kerberos authentication

Kerberos-based authentication for RDS for SQL Server requires connections be made to a specific Service Principal Name (SPN).
However, after a failover event, the application might not be aware of the new SPN.
To address this, RDS for SQL Server offers a Kerberos-based endpoint.

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

![Modify the amount of storage for a DB instance](images/kerb-endpoint-selfManagedAD-RDSMS.png)

If after connecting CNAME from remote client, an NTLM connection is returned, check if required ports are allowlisted.

To check if your connection is using Kerberos, run the following query:

```
SELECT net_transport, auth_scheme
    FROM sys.dm_exec_connections
    WHERE session_id = @@SSPID;
```

If your instance returns an NTLM connection when you connect to a Kerberos endpoint,
verify your network configuration and user configurations. See
[Configure your network connectivity](USER_SQLServer_SelfManagedActiveDirectory.md#USER_SQLServer_SelfManagedActiveDirectory.Requirements.NetworkConfig "USER_SQLServer_SelfManagedActiveDirectory.md#USER_SQLServer_SelfManagedActiveDirectory.Requirements.NetworkConfig").

## Step 3: Create Windows Authentication SQL Server logins

Use the Amazon RDS master user credentials to connect to the SQL Server DB instance as you do
for any other DB instance. Because the DB instance is joined to the self-managed AD domain,
you can provision SQL Server logins and users. You do this from the AD
users and groups utility in your self-managed AD domain. Database permissions are managed through standard
SQL Server permissions granted and revoked to these Windows logins.

In order for a self-managed AD domain service account to authenticate with SQL Server, a SQL Server Windows login
must exist for the self-managed AD domain service account or a self-managed AD group that the user is a member of. Fine-grained access
control is handled through granting and revoking permissions on these SQL Server
logins. A self-managed AD domain service account that doesn't have a SQL Server login or belong to a self-managed AD group with
such a login can't access the SQL Server DB instance.

The ALTER ANY LOGIN permission is required to create a self-managed AD SQL Server login. If you haven't created any logins
with this permission, connect as the DB instance's master user using SQL Server Authentication and create your self-managed AD SQL Server logins under
the context of the master user.

You can run a data definition language (DDL) command such as the following to create a SQL Server login for an self-managed AD domain service account or group.

###### Note

Specify users and groups using the pre-Windows 2000 login name in the format ``my_AD_domain`\`my_AD_domain_user``.
You can't use a user principal name (UPN) in the format `my_AD_domain_user```@```my_AD_domain`.

```
USE [master]
GO
CREATE LOGIN [`my_AD_domain`\`my_AD_domain_user`] FROM WINDOWS WITH DEFAULT_DATABASE = [master], DEFAULT_LANGUAGE = [us_english];
GO
```

For more information, see [CREATE LOGIN (Transact-SQL)](https://msdn.microsoft.com/en-us/library/ms189751.aspx "https://msdn.microsoft.com/en-us/library/ms189751.aspx") in the Microsoft Developer Network documentation.

Users (both humans and applications) from your domain can now connect to the RDS for SQL Server instance from a self-managed AD domain-joined client machine using Windows authentication.
