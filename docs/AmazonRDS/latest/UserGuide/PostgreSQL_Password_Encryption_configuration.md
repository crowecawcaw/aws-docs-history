# Using SCRAM for PostgreSQL password encryption

The _Salted Challenge Response Authentication Mechanism
(SCRAM)_ is an alternative to PostgreSQL's default message digest (MD5)
algorithm for encrypting passwords. The SCRAM authentication mechanism is considered more secure
than MD5. To learn more about these two different approaches to securing passwords, see [Password Authentication](https://www.postgresql.org/docs/14/auth-password.html "https://www.postgresql.org/docs/14/auth-password.html") in
the PostgreSQL documentation.

We recommend that you use SCRAM rather than MD5 as the password encryption scheme for your

RDS for PostgreSQL DB instance.
It's a cryptographic challenge-response mechanism that uses
the scram-sha-256 algorithm for password authentication and encryption.

You might need to update libraries for your client applications to support SCRAM. For
example, JDBC versions before 42.2.0 don't support SCRAM. For more information, see [PostgreSQL JDBC
Driver](https://jdbc.postgresql.org/changelogs/2018-01-17-42.2.0-release/ "https://jdbc.postgresql.org/changelogs/2018-01-17-42.2.0-release/") in the PostgreSQL JDBC Driver documentation. For a list of other PostgreSQL
drivers and SCRAM support, see [List of drivers](https://wiki.postgresql.org/wiki/List_of_drivers "https://wiki.postgresql.org/wiki/List_of_drivers") in the PostgreSQL documentation.

RDS for PostgreSQL version 13.1 and higher support scram-sha-256. These
versions also let you configure your DB instance to require SCRAM, as discussed in the following
procedures.

## Setting up RDS for PostgreSQL DB instance to require SCRAM

you can
require the RDS for PostgreSQL DB instance to accept only passwords that use
the scram-sha-256 algorithm.

###### Important

For existing RDS Proxies with PostgreSQL databases, if you modify the database
authentication to use `SCRAM` only, the proxy becomes unavailable for up to 60
seconds. To avoid the issue, do one of the following:

- Ensure that the database allows both `SCRAM` and `MD5`
  authentication.
- To use only `SCRAM` authentication, create a new proxy, migrate your
  application traffic to the new proxy, then delete the proxy previously associated with
  the database.

Before making changes to your system, be sure you understand the complete process, as
follows:

- Get information about all roles and password encryption for all database users.
- Double-check the parameter settings for your
  RDS for PostgreSQL DB instance for the parameters that
  control password encryption.
- If your
  RDS for PostgreSQL DB instance uses a default parameter
  group, you need to create a custom
  DB parameter group and apply it to your
  RDS for PostgreSQL DB instance so that you can modify
  parameters when needed. If your
  RDS for PostgreSQL DB instance uses a custom parameter
  group, you can modify the necessary parameters later in the process, as needed.
- Change the `password_encryption` parameter to
  `scram-sha-256`.
- Notify all database users that they need to update their passwords. Do the same for
  your `postgres` account. The new passwords are encrypted and stored using the
  scram-sha-256 algorithm.
- Verify that all passwords are encrypted using as the type of encryption.
- If all passwords use scram-sha-256, you can change the
  `rds.accepted_password_auth_method` parameter from `md5+scram` to
  `scram-sha-256`.

###### Warning

After you change `rds.accepted_password_auth_method` to scram-sha-256 alone,
any users (roles) with `md5`–encrypted passwords can't connect.

### Getting ready to require SCRAM for your RDS for PostgreSQL DB instance

Before making any changes to your
RDS for PostgreSQL DB instance, check all existing
database user accounts. Also, check the type of encryption used for passwords. You can do
these tasks by using the `rds_tools` extension. To see which PostgreSQL versions
support `rds_tools`, see [Extension
versions for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-extensions.md "../PostgreSQLReleaseNotes/postgresql-extensions.md").

###### To get a list of database users (roles) and password encryption methods

1. Use `psql` to connect to
   your RDS for PostgreSQL DB instance, as shown in the
   following.

```
psql --host=`db-name.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password
```

2. Install the `rds_tools` extension.

```
`postgres=>` `CREATE EXTENSION rds_tools;`
`CREATE EXTENSION`
```

3. Get a listing of roles and encryption.

```
`postgres=>` SELECT * FROM
      rds_tools.role_password_encryption_type();
```

You see output similar to the following.

```
       rolname        | encryption_type
----------------------+-----------------
 pg_monitor           |
 pg_read_all_settings |
 pg_read_all_stats    |
 pg_stat_scan_tables  |
 pg_signal_backend    |
 lab_tester           | md5
 user_465             | md5
 postgres             | md5
(8 rows)

```

### Creating a custom DB parameter group

###### Note

If your
RDS for PostgreSQL DB instance already uses a custom
parameter group, you don't need to create a new one.

For an overview of parameter groups for Amazon RDS, see [Working with parameters on your RDS for PostgreSQL DB instance](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

The password encryption type used for passwords is set in one parameter,
`password_encryption`. The encryption that the
RDS for PostgreSQL DB instance allows is set in another
parameter, `rds.accepted_password_auth_method`. Changing either of these from the
default values requires that you create a custom
DB parameter group and apply it to your
instance.

You can also use the AWS Management Console or the RDS API to create a custom
DB parameter group. For more information, see

You can now associate the custom parameter group with your DB instance.

###### To create a custom DB parameter group

1. Use the `create-db-parameter-group` CLI command to create the custom DB parameter group. This example uses
   `postgres13` as the source for this custom parameter group.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group --db-parameter-group-name '`docs-lab-scram-passwords`' \
  --db-parameter-group-family postgres13  --description '`Custom parameter group for SCRAM`'

```

For Windows:

```
aws rds create-db-parameter-group --db-parameter-group-name "`docs-lab-scram-passwords`" ^
  --db-parameter-group-family postgres13  --description "`Custom DB parameter group for SCRAM`"

```

2. Use the `modify-db-instance` CLI command to apply this custom parameter group
   to your RDS for PostgreSQL DB cluster.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance --db-instance-identifier '`your-instance-name`' \
        --db-parameter-group-name "`docs-lab-scram-passwords`
```

For Windows:

```
aws rds modify-db-instance --db-instance-identifier "`your-instance-name`" ^
        --db-parameter-group-name "`docs-lab-scram-passwords`
```

To resynchronize your RDS for PostgreSQL DB instance with your custom DB parameter group,
you need to reboot the primary and all other instances of the cluster. To minimize
impact to your users, schedule this to occur during your regular maintenance
window.

### Configuring password encryption to use SCRAM

The password encryption mechanism used by an
RDS for PostgreSQL DB instance is set in the
DB parameter group in the
`password_encryption` parameter. Allowed values are unset, `md5`, or
`scram-sha-256`. The default value depends on the
RDS for PostgreSQL version, as follows:

- RDS for PostgreSQL 14 and above – Default is `scram-sha-256`
- RDS for PostgreSQL 13 – Default is `md5`

With a custom
DB parameter group attached to your
RDS for PostgreSQL DB instance, you can modify values for
the password encryption parameter.

![Following, the RDS console shows the default values for the password_encryption parameters for RDS for PostgreSQL.](images/rpg-pwd-encryption-md5-scram-1.png)

###### To change password encryption setting to scram-sha-256

- Change the value of password encryption to scram-sha-256, as shown following. The
  change can be applied immediately because the parameter is dynamic, so a restart
  isn't required for the change to take effect.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group --db-parameter-group-name \
  'docs-lab-scram-passwords' --parameters 'ParameterName=password_encryption,ParameterValue=scram-sha-256,ApplyMethod=immediate'
```

For Windows:

```
aws rds modify-db-parameter-group --db-parameter-group-name ^
  "docs-lab-scram-passwords" --parameters "ParameterName=password_encryption,ParameterValue=scram-sha-256,ApplyMethod=immediate"
```

### Migrating passwords for user roles to SCRAM

You can migrate passwords for user roles to SCRAM as described following.

###### To migrate database user (role) passwords from MD5 to SCRAM

1. Log in as the administrator user (default user name, `postgres`) as shown
   following.

```
psql --host=`db-name.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password
```

2. Check the setting of the `password_encryption` parameter on your
   RDS for PostgreSQL DB instance by using the following command.

```
`postgres=>` `SHOW password_encryption;`
 `password_encryption
---------------------
 md5
 (1 row)`

```

3. Change the value of this parameter to scram-sha-256. For more
   information, see [Configuring password encryption to use SCRAM](#PostgreSQL_Password_Encryption_configuration.configure-password-encryption "#PostgreSQL_Password_Encryption_configuration.configure-password-encryption").
4. Check the value again to make sure that it's now set to
   `scram-sha-256`, as follows.

```
`postgres=>` `SHOW password_encryption;`
 `password_encryption
---------------------
 scram-sha-256
 (1 row)`
```

5. Notify all database users to change their passwords. Be sure to also change your own
   password for account `postgres` (the database user with
   `rds_superuser` privileges).

```
`labdb=>` ALTER ROLE postgres WITH LOGIN PASSWORD 'change_me';
`ALTER ROLE`
```

6. Repeat the process for all databases on your
   RDS for PostgreSQL DB instance.

### Changing parameter to require SCRAM

This is the final step in the process. After you make the change in the following
procedure, any user accounts (roles) that still use `md5` encryption for
passwords can't log in to the
RDS for PostgreSQL DB instance.

The `rds.accepted_password_auth_method` specifies the encryption method that
the RDS for PostgreSQL DB instance accepts for a user password during the login process.
The default value is `md5+scram`, meaning that either method is accepted. In the
following image, you can find the default setting for this parameter.

![The RDS console showing the default and allowed values for the rds.accepted_password_auth_method parameters.](images/pwd-encryption-md5-scram-2.png)

The allowed values for this parameter are `md5+scram` or `scram`
alone. Changing this parameter value to `scram` makes this a requirement.

###### To change the parameter value to require SCRAM authentication for passwords

1. Verify that all database user passwords for all databases on your
   RDS for PostgreSQL DB instance use
   `scram-sha-256` for password encryption. To do so, query
   `rds_tools` for the role (user) and encryption type, as follows.

```
`postgres=>` `SELECT * FROM rds_tools.role_password_encryption_type();`
  `rolname | encryption_type
 ----------------------+-----------------
 pg_monitor |
 pg_read_all_settings |
 pg_read_all_stats |
 pg_stat_scan_tables |
 pg_signal_backend |
 lab_tester | scram-sha-256
 user_465 | scram-sha-256
 postgres | scram-sha-256
 ( rows)`
```

2. Repeat the query across all DB instances in your
   RDS for PostgreSQL DB instance.

If all passwords use scram-sha-256, you can proceed. 3. Change the value of the accepted password authentication to scram-sha-256, as
follows.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group --db-parameter-group-name 'docs-lab-scram-passwords' \
  --parameters 'ParameterName=rds.accepted_password_auth_method,ParameterValue=scram,ApplyMethod=immediate'
```

For Windows:

```
aws rds modify-db-parameter-group --db-parameter-group-name "docs-lab-scram-passwords" ^
  --parameters "ParameterName=rds.accepted_password_auth_method,ParameterValue=scram,ApplyMethod=immediate"
```
