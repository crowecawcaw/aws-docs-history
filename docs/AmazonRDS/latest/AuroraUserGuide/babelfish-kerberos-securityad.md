# Setting up Kerberos authentication using

Active Directory security groups for Babelfish

Starting from Babelfish version 4.2.0, you can setup Kerberos authentication for
Babelfish with Active Directory security groups. The following are prerequisites to
complete for setting up Kerberos authentication using Active Directory:

- You must follow all the steps mentioned at [Kerberos authentication with Babelfish](babelfish-active-directory.md "babelfish-active-directory.md").
- Ensure that DB instance is associated with Active Directory. To verify this, you can
  view the status of the domain membership in the console or by running the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") AWS CLI command.

The status of the DB instance should be kerberos-enabled. For more information on
understanding domain membership, see [Understanding Domain
membership](postgresql-kerberos-managing.md#postgresql-kerberos-managing.understanding "postgresql-kerberos-managing.md#postgresql-kerberos-managing.understanding").

- Verify mappings between NetBIOS domain name and DNS domain name using the
  following query:

```

SELECT netbios_domain_name, fq_domain_name FROM babelfish_domain_mapping;
```

- Before proceeding further, verify Kerberos authentication using individual login
  works as expected. The connection using Kerberos authentication as an Active
  Directory user should be successful. If you face any issues, see [Frequently occurring errors](babelfish-active-directory.md#babelfish-active-directory-errors "babelfish-active-directory.md#babelfish-active-directory-errors").

## Setting up the pg_ad_mapping

extension

You must follow all the steps mentioned at [Setting up the pg_ad_mapping
extension](AD.Security.md#AD.Security.Groups.Setup "AD.Security.md#AD.Security.Groups.Setup") . To verify that the extension is
installed, run the following query from TDS endpoint:

```
`1>` SELECT extname, extversion FROM pg_extension where extname like 'pg_ad_mapping';
`2>` GO
extname       extversion
------------- ----------
pg_ad_mapping 0.1

(1 rows affected)
```

## Managing Group Logins

Create group logins by following the steps mentioned at [Managing Logins](babelfish-active-directory.md#babelfish-active-directory-login-managing "babelfish-active-directory.md#babelfish-active-directory-login-managing"). We recommend that the
login name be the same as the Active Directory (AD) security group name for easier
maintenance, although it's not mandatory. For example:

```
CREATE LOGIN [corp\accounts-group] FROM WINDOWS [WITH DEFAULT_DATABASE=database]
```

## Auditing and Logging

To determine the AD security principal identity, use the following commands:

```

`1>` select suser_name();
`2>` GO
suser_name
----------
corp\user1

(1 rows affected)

```

Currently, AD user identity isn't visible in the logs. You can turn on the
`log_connections` parameter to log DB session establishment. For more
information, see [log_connections](../../../prescriptive-guidance/latest/tuning-postgresql-parameters/log-connections.md "../../../prescriptive-guidance/latest/tuning-postgresql-parameters/log-connections.md"). The output includes the AD user identity as principal as
shown in the following example. The backend PID associated with this output can then
help attribute actions back to the actual AD user.

```
bbf_group_ad_login@babelfish_db:[615]:LOG: connection authorized: user=bbf_group_ad_login database=babelfish_db application_name=sqlcmd GSS (authenticated=yes, encrypted=yes, principal=user1@CORP.EXAMPLE.COM)
```
