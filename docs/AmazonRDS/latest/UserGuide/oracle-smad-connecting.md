

# Configuring a Kerberos client and connecting to your DB instance
<a name="oracle-smad-connecting"></a>

After you complete the steps in [Setting up self-managed Active Directory](oracle-smad-setting-up.md), complete the following steps for each DB instance that you want to use with Kerberos authentication. You join the DB instance to your domain, create Oracle users for your Active Directory (AD) users, configure a Kerberos client, and then connect to the DB instance. If a client host is already configured for your domain, you don't need to repeat its Kerberos configuration in Step 3 for another DB instance. Make sure that the client host can reach the new DB instance over the database port.
+ [Step 1: Create or modify an Amazon RDS for Oracle DB instance](#oracle-smad.connecting.step1)
+ [Step 2: Create Kerberos authentication Oracle logins](#oracle-smad.connecting.step2)
+ [Step 3: Configure a Kerberos client](#oracle-smad.connecting.step3)
+ [Step 4: Connect to your DB instance](#oracle-smad.connecting.step4)

## Step 1: Create or modify an Amazon RDS for Oracle DB instance
<a name="oracle-smad.connecting.step1"></a>

You can join an Amazon RDS for Oracle DB instance to your self-managed AD domain in the following ways:
+ Create a new DB instance with the console, the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command, or the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) RDS API operation. For instructions, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.html).
+ Modify an existing DB instance with the console, the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) AWS CLI command, or the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) RDS API operation. For instructions, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.html).
+ Restore an Oracle DB instance from a DB snapshot using the console, the [restore-db-instance-from-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html) AWS CLI command, or the [RestoreDBInstanceFromDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html) RDS API operation. For instructions, see [Restoring to a DB instance](USER_RestoreFromSnapshot.html).
+ Restore an Oracle DB instance to a point-in-time using the console, the [restore-db-instance-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html) AWS CLI command, or the [RestoreDBInstanceToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html) RDS API operation. For instructions, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.html).
+ Create a read replica of an Oracle DB instance using the console, the [create-db-instance-read-replica](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance-read-replica.html) AWS CLI command, or the [CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html) RDS API operation. A read replica doesn't inherit the domain membership of its source, so specify the four domain parameters on the operation. For instructions, see [Creating a read replica](USER_ReadRepl.Create.html).

The DB instance must be in a virtual private cloud (VPC) that can reach your domain controllers. When you create or modify the DB instance, make sure that its security groups allow the traffic described in [Configure your network connectivity](oracle-smad-requirements.md#oracle-smad-requirements.configure-network).

### Using the console
<a name="oracle-smad.connecting.step1.console"></a>

1. In the **Database authentication** settings of the create, modify, restore, or create read replica page, choose **Password and Kerberos authentication**.

1. For **Kerberos authentication type**, choose **Self-managed Microsoft Active Directory**.

1. Enter the following values:
   + **Fully qualified domain name (FQDN)** – The FQDN of your domain, such as `corp.example.com`.
   + **Organizational unit (OU)** – The distinguished name of the OU that you created in Step 1 of [Setting up self-managed Active Directory](oracle-smad-setting-up.md), such as `OU=AWS-RDS-OU,DC=corp,DC=example,DC=com`. It must have one or more OU components followed by one or more DC components, and component values can't contain shell metacharacters $, `, \|, ; or control characters.
   + **Authorization secret ARN** – The Amazon Resource Name (ARN) of the secret that you created in Step 5 of [Setting up self-managed Active Directory](oracle-smad-setting-up.md).
   + **Primary DNS server IP** and **Secondary DNS server IP** – The IPv4 addresses of the DNS servers for your domain.

1. Complete the rest of the page, and choose **Create database**, **Modify DB instance**, **Restore DB instance**, or **Create read replica**.

### Using the AWS CLI
<a name="oracle-smad.connecting.step1.cli"></a>

When you use the AWS CLI, the following parameters are required for the DB instance to join your self-managed AD domain:
+ For `--domain-fqdn`, use the fully qualified domain name of your domain.
+ For `--domain-ou`, use the distinguished name of the OU that you created in Step 1 of [Setting up self-managed Active Directory](oracle-smad-setting-up.md). It must have one or more OU components followed by one or more DC components, and component values can't contain shell metacharacters $, `, \|, ; or control characters.
+ For `--domain-auth-secret-arn`, use the ARN of the secret that you created in Step 5 of [Setting up self-managed Active Directory](oracle-smad-setting-up.md).
+ For `--domain-dns-ips`, use the primary and secondary IPv4 addresses of the DNS servers for your domain. This parameter takes exactly two addresses. If you don't have a secondary DNS server, enter the primary address twice.

For example, the following command joins an existing DB instance to a self-managed AD domain.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier my-oracle-instance \
    --domain-fqdn corp.example.com \
    --domain-ou "OU=AWS-RDS-OU,DC=corp,DC=example,DC=com" \
    --domain-auth-secret-arn "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-ad-secret-AbCdEf" \
    --domain-dns-ips "10.0.1.100" "10.0.1.101"
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier my-oracle-instance ^
    --domain-fqdn corp.example.com ^
    --domain-ou "OU=AWS-RDS-OU,DC=corp,DC=example,DC=com" ^
    --domain-auth-secret-arn "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-ad-secret-AbCdEf" ^
    --domain-dns-ips "10.0.1.100" "10.0.1.101"
```

To verify that the domain join succeeded, run the following command and confirm that `Status` is `kerberos-enabled`.

```
aws rds describe-db-instances \
    --db-instance-identifier my-oracle-instance \
    --query 'DBInstances[0].DomainMemberships'
```

If the status is `enable-kerberos-failed`, see [Troubleshooting self-managed Active Directory for Amazon RDS for Oracle](oracle-smad-troubleshooting.md).

## Step 2: Create Kerberos authentication Oracle logins
<a name="oracle-smad.connecting.step2"></a>

After the DB instance reaches `kerberos-enabled`, use the Amazon RDS master user credentials to connect to the Oracle DB instance as you do any other DB instance. The DB instance is joined to your self-managed AD domain, so you can provision Oracle logins and users from the Microsoft Active Directory users in your domain. To manage database permissions, you grant and revoke standard Oracle permissions to these logins.

**To allow a Microsoft Active Directory user to authenticate with Oracle**

1. Connect to the Oracle DB instance using your Amazon RDS master user credentials.

1. Create an externally authenticated user in Oracle database. In the following example, replace `KRBUSER@CORP.EXAMPLE.COM` with the user name and domain name.

   ```
   CREATE USER "KRBUSER@CORP.EXAMPLE.COM" IDENTIFIED EXTERNALLY;
   GRANT CREATE SESSION TO "KRBUSER@CORP.EXAMPLE.COM";
   ```

1. Users (both humans and applications) from your domain can now connect to the Oracle DB instance from a domain-joined client machine using Kerberos authentication.

**Note**  
A read replica is read-only, so you can't create database users on it. Create externally identified users on the primary DB instance. Amazon RDS replicates them to the read replica, and your AD users can then connect to the read replica with Kerberos authentication.  
If a read replica is joined to a different domain than the primary DB instance, create the database user for the read replica's domain principal on the primary DB instance as well. Although that user can't authenticate on the primary DB instance, Amazon RDS replicates the user to the read replica, where the user can authenticate with Kerberos.

## Step 3: Configure a Kerberos client
<a name="oracle-smad.connecting.step3"></a>

To configure an Oracle client, meet the following requirements:
+ Create a configuration file named `krb5.conf` (Linux, macOS, or Unix) or `krb5.ini` (Windows) to point to the domain. Configure the Oracle client to use this configuration file.
+ Verify that traffic can flow between the client host and your AD domain controllers over DNS port 53 over TCP/UDP, Kerberos ports 88 and 464 over TCP, and LDAP port 389 over TCP.
+ Verify that traffic can flow between the client host and the DB instance over the database port.

The following is sample `krb5.conf` content:

```
[libdefaults]
 default_realm = CORP.EXAMPLE.COM

[realms]
 CORP.EXAMPLE.COM = {
  kdc = corp.example.com
  admin_server = corp.example.com
 }

[domain_realm]
 .corp.example.com = CORP.EXAMPLE.COM
 corp.example.com = CORP.EXAMPLE.COM
```

The following is sample `sqlnet.ora` content for a SQL\*Plus configuration:

```
SQLNET.AUTHENTICATION_SERVICES=(KERBEROS5PRE,KERBEROS5)
SQLNET.KERBEROS5_CONF=path_to_krb5.conf_file
SQLNET.KERBEROS5_CONF_MIT=TRUE
```

**Note**  
Set `SQLNET.KERBEROS5_CONF_MIT=TRUE` in the client's `sqlnet.ora` file when your `krb5.conf` file uses the MIT Kerberos configuration format, as the preceding example does. This parameter lets the database recognize the Kerberos ticket that MIT `kinit` cached. Without it, authentication fails even though `kinit` obtained a valid ticket. For more information about this parameter, see [Kerberos, SSL, and RADIUS Authentication Parameters](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/kerberos-ssl-and-radius-authentication-parameters.html#GUID-34BAFC7C-4B29-4F52-90B6-4F6B93580250) and [Configuring Kerberos Authentication](https://docs.oracle.com/cd/E15586_01/network.1111/e10746/asokerb.htm) in the Oracle Database documentation.

**Tip**  
If you are using a native Windows cache, you can also set the `SQLNET.KERBEROS5_CC_NAME` parameter to `OSMSFT://` or `MSLSA` in the `sqlnet.ora` file to use the credentials stored in the Microsoft Active Directory.

## Step 4: Connect to your DB instance
<a name="oracle-smad.connecting.step4"></a>

**To connect with SQL\*Plus**

1. At a command prompt, obtain a Kerberos ticket. Replace `KRBUSER@CORP.EXAMPLE.COM` with the AD user and domain name, and enter the AD password at the prompt.

   ```
   kinit KRBUSER@CORP.EXAMPLE.COM
   ```

1. Open SQL\*Plus and connect using the DNS name and port number for the Oracle DB instance. For more information about connecting to an Oracle DB instance in SQL\*Plus, see [Connecting to your DB instance using SQL\*Plus](USER_ConnectToOracleInstance.SQLPlus.html).