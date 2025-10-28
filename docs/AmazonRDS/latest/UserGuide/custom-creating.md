# Logging in to your RDS Custom for Oracle database as

SYS

After you create your RDS Custom DB instance, you can log in to your Oracle database as user
`SYS`, which gives you `SYSDBA` privileges. You have the following
login options:

- Get the `SYS` password from Secrets Manager, and specify this password in your
  SQL client.
- Use OS authentication to log in to your database. In this case, you don't need a
  password.

## Finding the SYS password for your RDS Custom for Oracle

database

Your can log in to your Oracle database as `SYS` or `SYSTEM` or
by specifying the master user name in an API call. The password for `SYS` and
`SYSTEM` is stored in Secrets Manager.

The secret uses the naming format
`do-not-delete-rds-custom-`resource_id`-`uuid``
 or
 `rds-custom!oracle-do-not-delete-`resource_id`-`uuid``.
You can find the password using the AWS Management Console.

###### To find the SYS password for your database in Secrets Manager

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the RDS console, complete the following steps:
   1. In the navigation pane, choose
      **Databases**.
   2. Choose the name of your RDS Custom for Oracle DB instance.
   3. Choose **Configuration**.
   4. Copy the value underneath **Resource ID**.
      For example, you resource ID might be
      **db-ABC12CDE3FGH4I5JKLMNO6PQR7**.

3. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
4. In the Secrets Manager console, complete the following steps:
   1. In the left navigation pane, choose
      **Secrets**.
   2. Filter the secrets by the resource ID that you copied in step
      2.d.
   3. Choose the secret that uses the naming format
      **do-not-delete-rds-custom-`resource_id`-`uuid`**
      or
      **rds-custom!oracle-do-not-delete-`resource_id`-`uuid`**.
      The `resource_id` is the resource ID
      that you copied in step 2.d.

   For example, if your resource ID is
   **db-ABC12CDE3FGH4I5JKLMNO6PQR7** and your
   UUID is **1234ab**, your secret is named
   **do-not-delete-rds-custom-db-ABC12CDE3FGH4I5JKLMNO6PQR7-1234ab**
   or
   **rds-custom!oracle-do-not-delete-db-ABC12CDE3FGH4I5JKLMNO6PQR7-1234ab**. 4. In **Secret value**, choose
   **Retrieve secret value**. 5. In **Key/value**, copy the value for
   **password**.

5. Install SQL\*Plus on your DB instance and log in to your database as
   `SYS`. For more information, see [Step 3: Connect your SQL client to an
   Oracle DB instance](CHAP_GettingStarted.CreatingConnecting.md#CHAP_GettingStarted.Connecting.Oracle "CHAP_GettingStarted.CreatingConnecting.md#CHAP_GettingStarted.Connecting.Oracle").

## Logging in to your RDS Custom for Oracle database using

OS authentication

The OS user `rdsdb` owns the Oracle database binaries. You can switch to
the `rdsdb` user and log in to your RDS Custom for Oracle database without a
password.

1. Connect to your DB instance with AWS Systems Manager. For more information, see [Connecting to your RDS Custom DB instance using Session Manager](custom-creating.md "custom-creating.md").
2. Switch to the `rdsdb` user.

```
sudo su - rdsdb
```

3. Log in to your database using OS authentication. You can use `sqlplus / as sysdba` or the `sql` alias.

```
$ sqlplus / as sysdba

SQL*Plus: Release 21.0.0.0.0 - Production on Wed Apr 12 20:11:08 2023
Version 21.9.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.10.0.0.0
```

Alternatively, you can use the `sql` alias:

```
$ sql
```
