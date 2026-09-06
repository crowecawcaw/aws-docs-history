

# Database authentication with Amazon RDS
<a name="database-authentication"></a>

 Amazon RDS supports several ways to authenticate database users.

Password, Kerberos, and IAM database authentication use different methods of authenticating to the database. Therefore, a specific user can log in to a database using only one authentication method. 

For PostgreSQL, use only one of the following role settings for a user of a specific database: 
+ To use IAM database authentication, assign the `rds_iam` role to the user.
+ To use Kerberos authentication, assign the `rds_ad` role to the user.
+ To use password authentication, don't assign either the `rds_iam` or `rds_ad` roles to the user.

Don't assign both the `rds_iam` and `rds_ad` roles to a user of a PostgreSQL database either directly or indirectly by nested grant access. If the `rds_iam` role is added to the master user, IAM authentication takes precedence over password authentication so the master user has to log in as an IAM user.

**Important**  
We strongly recommend that you do not use the master user directly in your applications. Instead, adhere to the best practice of using a database user created with the minimal privileges required for your application.

**Topics**
+ [Password authentication](#password-authentication)
+ [IAM database authentication](#iam-database-authentication)
+ [Kerberos authentication](#kerberos-authentication)

## Password authentication
<a name="password-authentication"></a>

With *password authentication,* your database performs all administration of user accounts. You create users with SQL statements such as `CREATE USER`, with the appropriate clause required by the DB engine for specifying passwords. For example, in MySQL the statement is `CREATE USER` {{name}} `IDENTIFIED BY` {{password}}, while in PostgreSQL, the statement is `CREATE USER` {{name}} `WITH PASSWORD` {{password}}. 

With password authentication, your database controls and authenticates user accounts. If a DB engine has strong password management features, they can enhance security. Database authentication might be easier to administer using password authentication when you have small user communities. Because clear text passwords are generated in this case, integrating with AWS Secrets Manager can enhance security.

For information about using Secrets Manager with Amazon RDS , see [Creating a basic secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) and [Rotating secrets for supported Amazon RDS databases](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-rds.html) in the *AWS Secrets Manager User Guide*. For information about programmatically retrieving your secrets in your custom applications, see [Retrieving the secret value](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_retrieve-secret.html) in the *AWS Secrets Manager User Guide*. 

## IAM database authentication
<a name="iam-database-authentication"></a>

You can authenticate to your DB instance using AWS Identity and Access Management (IAM) database authentication. With this authentication method, you don't need to use a password when you connect to a DB instance . Instead, you use an authentication token.

For more information about IAM database authentication, including information about availability for specific DB engines, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.IAMDBAuth.md) .

## Kerberos authentication
<a name="kerberos-authentication"></a>

 Amazon RDS supports external authentication of database users using Kerberos and Microsoft Active Directory. Kerberos is a network authentication protocol that uses tickets and symmetric-key cryptography to eliminate the need to transmit passwords over the network. Kerberos has been built into Active Directory and is designed to authenticate users to network resources, such as databases.

 Amazon RDS support for Kerberos and Active Directory provides the benefits of single sign-on and centralized authentication of database users. You can keep your user credentials in Active Directory. Active Directory provides a centralized place for storing and managing credentials for multiple DB instances . 

To use credentials from your self-managed Active Directory, you need to setup a trust relationship to the Directory Service for Microsoft Active Directory that the DB instance is joined to.

 RDS for PostgreSQL and RDS for MySQL support one-way and two-way forest trust relationships with forest-wide authentication or selective authentication.

In some scenarios, you can configure Kerberos authentication over an external trust relationship. This requires your self-managed Active Directory to have additional settings. This includes but is not limited to [ Kerberos Forest Search Order](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/kfso-not-work-in-external-trust-event-is-17). 

Microsoft SQL Server and PostgreSQL DB instances support one-way and two-way forest trust relationships. Oracle DB instances support one-way and two-way external and forest trust relationships. For more information, see [When to create a trust relationship](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/setup_trust.html) in the *Directory Service Administration Guide*. 

For information about Kerberos authentication with a specific DB engine, see the following:
+  [Working with AWS Managed Active Directory with RDS for SQL Server](USER_SQLServerWinAuth.md) 
+  [Using Kerberos authentication for Amazon RDS for MySQL](mysql-kerberos.md) 
+  [Configuring Kerberos authentication for Amazon RDS for Oracle](oracle-kerberos.md) 
+  [Using Kerberos authentication with Amazon RDS for PostgreSQL](postgresql-kerberos.md) 
+  [Working with AWS Managed Active Directory with RDS for Db2](db2-managed-active-directory.md) .

**Note**  
Currently, Kerberos authentication isn't supported for MariaDB DB instances.