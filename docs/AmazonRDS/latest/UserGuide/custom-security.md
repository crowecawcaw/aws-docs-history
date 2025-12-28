# Rotating RDS Custom for Oracle credentials for compliance

programs

Some compliance programs require database user credentials to change periodically, for
example, every 90 days. RDS Custom for Oracle automatically rotates credentials for some predefined
database users.

###### Topics

- [Automatic rotation of credentials for
  predefined users](#custom-security.cred-rotation.auto "#custom-security.cred-rotation.auto")
- [Guidelines for rotating user credentials](#custom-security.cred-rotation.guidelines "#custom-security.cred-rotation.guidelines")
- [Rotating user credentials
  manually](#custom-security.cred-rotation.manual "#custom-security.cred-rotation.manual")

## Automatic rotation of credentials for

predefined users

If your RDS Custom for Oracle DB instance is hosted in Amazon RDS, credentials for the following
predefined Oracle users rotate every 30 days automatically. Credentials for the
preceding users reside in AWS Secrets Manager.

| Database user      | Created by | Supported engine versions                                                              | Notes                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | ---------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SYS`              | Oracle     | custom-oracle-ee<br>custom-oracle-ee-cdb<br>custom-oracle-se2<br>custom-oracle-se2-cdb |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `SYSTEM`           | Oracle     | custom-oracle-ee<br>custom-oracle-ee-cdb<br>custom-oracle-se2<br>custom-oracle-se2-cdb |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `RDSADMIN`         | RDS        | custom-oracle-ee<br>custom-oracle-se2                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `C##RDSADMIN`      | RDS        | custom-oracle-ee-cdb<br>custom-oracle-se2-cdb                                          | User names with a `C##` prefix exist only in CDBs. For more information about<br>CDBs, see [Overview of Amazon RDS Custom for Oracle architecture](custom-creating.md#custom-creating.overview "custom-creating.md#custom-creating.overview").                                                                                                                                                                            |
| `RDS_DATAGUARD`    | RDS        | custom-oracle-ee                                                                       | This user exists only in read replicas, source databases for read replicas, and databases that you have physically migrated into RDS Custom using Oracle Data Guard.                                                                                                                                                                                                                                                      |
| `C##RDS_DATAGUARD` | RDS        | custom-oracle-ee-cdb                                                                   | This user exists only in read replicas, source databases for read replicas, and databases<br>that you have physically migrated into RDS Custom using Oracle Data<br>Guard. User names with a `C##` prefix exist only in CDBs.<br>For more information about CDBs, see [Overview of Amazon RDS Custom for Oracle architecture](custom-creating.md#custom-creating.overview "custom-creating.md#custom-creating.overview"). |

An exception to the automatic credential rotation is an RDS Custom for Oracle DB instance that you
have manually configured as a standby database. RDS only rotates credentials for
read replicas that you have created using the
`create-db-instance-read-replica` CLI command or
`CreateDBInstanceReadReplica` API.

## Guidelines for rotating user credentials

To make sure that your credentials rotate according to your compliance program, note the following guidelines:

- If your DB instance rotates credentials automatically, don't manually change or delete a secret, password file, or password for users listed in [Predefined Oracle users](#auto-rotation "#auto-rotation"). Otherwise, RDS Custom might place your DB instance outside of the support perimeter, which suspends automatic rotation.
- The RDS master user is not predefined, so you are responsible for either changing the password manually or setting up automatic rotation in Secrets Manager. For more information, see [Rotate AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md").

## Rotating user credentials

manually

For the following categories of databases, RDS doesn't automatically rotate the
credentials for the users listed in [Predefined Oracle
users](#auto-rotation "#auto-rotation"):

- A database that you configured manually to function as a standby
  database.
- An on-premises database.
- A DB instance that is outside of the support perimeter or in a state in which
  the RDS Custom automation can't run. In this case, RDS Custom also doesn't rotate
  keys.

If your database is in any of the preceding categories, you must rotate your user
credentials manually.

###### To rotate user credentials manually for a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In **Databases**, make sure that RDS isn't currently
   backing up your DB instance or performing operations such configuring high
   availability.
3. In the database details page, choose **Configuration**
   and note the Resource ID for the DB instance. Or you can use the AWS CLI command
   `describe-db-instances`.
4. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
5. In the search box, enter the resource ID of your database and search for a
   secret using either of the following naming conventions:

```
do-not-delete-rds-custom-`resource_id`-`uuid`
rds-custom!oracle-do-not-delete-`resource_id`-`uuid`
```

This secret stores the password for `RDSADMIN`,
`SYS`, and `SYSTEM`. The following sample keys are
for the DB instance with the resource ID
`db-ABCDEFG12HIJKLNMNOPQRS3TUVWX` and UUID
`123456`:

```
do-not-delete-rds-custom-db-ABCDEFG12HIJKLNMNOPQRS3TUVWX-123456
rds-custom!oracle-do-not-delete-db-ABCDEFG12HIJKLNMNOPQRS3TUVWX-123456
```

###### Important

If your DB instance is a read replica and uses the
`custom-oracle-ee-cdb` engine, two secrets exist with the
suffix
``db-resource_id`-`uuid``,
one for the master user and the other for `RDSADMIN`,
`SYS`, and `SYSTEM`. To find the correct
secret, run the following command on the host:

```
cat /opt/aws/rdscustomagent/config/database_metadata.json | python3 -c "import sys,json; print(json.load(sys.stdin)['dbMonitoringUserPassword'])"
```

The `dbMonitoringUserPassword` attribute indicates the
secret for `RDSADMIN`, `SYS`, and
`SYSTEM`. 6. If your DB instance exists in an Oracle Data Guard configuration, search for a
secret using either of the following naming conventions:

```
do-not-delete-rds-custom-`resource_id`-`uuid`-dg
rds-custom!oracle-do-not-delete-`resource_id`-`uuid`-dg
```

This secret stores the password for `RDS_DATAGUARD`. The
following sample keys are for the DB instance with the DB resource ID
`db-ABCDEFG12HIJKLNMNOPQRS3TUVWX` and UUID
**789012**:

```
do-not-delete-rds-custom-db-ABCDEFG12HIJKLNMNOPQRS3TUVWX-789012-dg
rds-custom!oracle-do-not-delete-db-ABCDEFG12HIJKLNMNOPQRS3TUVWX-789012-dg
```

7. For all database users listed in [Predefined
   Oracle users](#auto-rotation "#auto-rotation"), update the passwords by following the instructions
   in [Modify
   an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md").
8. If your database is a standalone database or a source database in an
   Oracle Data Guard configuration:
   1. Start your Oracle SQL client and log in as
      `SYS`.
   2. Run a SQL statement in the following form for each database user
      listed in [Predefined Oracle
      users](#auto-rotation "#auto-rotation"):

   ```
   ALTER USER `user-name` IDENTIFIED BY `pwd-from-secrets-manager` ACCOUNT UNLOCK;
   ```

   For example, if the new password for `RDSADMIN` stored
   in Secrets Manager is `pwd-123`, run the following
   statement:

   ```
   ALTER USER RDSADMIN IDENTIFIED BY pwd-123 ACCOUNT UNLOCK;
   ```

9. If your DB instance runs Oracle Database 12c Release 1 (12.1) and is managed by
   Oracle Data Guard, manually copy the password file (`orapw`) from
   the primary DB instance to each standby DB instance.

If your DB instance is hosted in Amazon RDS, the password file location is
`/rdsdbdata/config/orapw`. For databases that aren't hosted
in Amazon RDS, the default location is
`$ORACLE_HOME/dbs/orapw$ORACLE_SID` on Linux and UNIX and
`%ORACLE_HOME%\database\PWD%ORACLE_SID%.ora` on
Windows.
