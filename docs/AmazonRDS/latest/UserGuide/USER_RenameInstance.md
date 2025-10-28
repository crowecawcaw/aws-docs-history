# Renaming a DB instance

You can rename a DB instance by using the AWS Management Console,
the AWS CLI `modify-db-instance` command,
or the Amazon RDS API `ModifyDBInstance` action. Renaming a DB instance can have far-reaching
effects. The following is a list of considerations before you rename a DB instance.

- When you rename a DB instance, the endpoint for the DB instance changes, because the URL
  includes the name you assigned to the DB instance. You should always redirect
  traffic from the old URL to the new one.
- When you rename a DB instance, the old DNS name that was used by the DB instance is
  immediately deleted, although it could remain cached for a few minutes. The new DNS
  name for the renamed DB instance becomes effective in about 10 minutes. The renamed
  DB instance is not available until the new name becomes effective.
- You cannot use an existing DB instance name when renaming an instance.
- All read replicas associated with a DB instance remain associated with that instance after it
  is renamed. For example, suppose you have a DB instance that serves your production
  database and the instance has several associated read replicas. If you rename the DB
  instance and then replace it in the production environment with a DB snapshot, the
  DB instance that you renamed will still have the read replicas associated with it.
- Metrics and events associated with the name of a DB instance are maintained if you reuse a DB
  instance name. For example, if you promote a read replica and rename it to be the
  name of the previous primary DB instance, the events and metrics associated with the primary DB instance are
  associated with the renamed instance.
- DB instance tags remain with the DB instance, regardless of renaming.
- DB snapshots are retained for a renamed DB instance.

###### Note

A DB instance is an isolated database environment running in the cloud. A DB instance can host multiple databases,
or a single Oracle database with multiple schemas. For information about changing a database name, see the documentation
for your DB engine.

## Renaming to replace an existing DB instance

The most common reasons for renaming a DB instance are that you are promoting a read replica
or you are restoring data from a DB snapshot or point-in-time recovery (PITR). By renaming the database, you can
replace the DB instance without having to change any application code that references
the DB instance. In these cases, you would do the following:

1. Stop all traffic going to the primary DB instance. This can involve redirecting traffic from
   accessing the databases on the DB instance or some other way you want to use to
   prevent traffic from accessing your databases on the DB instance.
2. Rename the primary DB instance to a name that indicates it is no longer the primary DB instance as
   described later in this topic.
3. Create a new primary DB instance by restoring from a DB snapshot or by promoting a read
   replica, and then give the new instance the name of the previous primary DB instance.
4. Associate any read replicas with the new primary DB instance.

If you delete the old primary DB instance, you are responsible for deleting any unwanted DB
snapshots of the old primary DB instance.

For information about promoting a read replica, see [Promoting a read replica to be a standalone
DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

###### Important

The DB instance is rebooted when it is renamed. For RDS for SQL Server Multi-AZ instances with
AlwaysOn or Mirroring option enabled, a failover is expected when instance is rebooted after the rename operation.

###### To rename a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to rename.
4. Choose **Modify**.
5. In **Settings**, enter a new name for **DB instance
   identifier**.
6. Choose **Continue**.
7. To apply the changes immediately, choose **Apply immediately**. Choosing
   this option can cause an outage in some cases. For more information, see
   [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
8. On the confirmation page, review your changes.
   If they are correct, choose **Modify DB Instance**
   to save your changes.

Alternatively, choose **Back** to edit your changes,
or choose **Cancel** to cancel your changes.
To rename a DB instance,
use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md").
Provide the current `--db-instance-identifier` value
and `--new-db-instance-identifier` parameter with
the new name of the DB instance.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `DBInstanceIdentifier` \
    --new-db-instance-identifier `NewDBInstanceIdentifier`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `DBInstanceIdentifier` ^
    --new-db-instance-identifier `NewDBInstanceIdentifier`
```

To rename a DB instance, call Amazon RDS API operation
[`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") with the following parameters:

- `DBInstanceIdentifier` — existing name for the instance
- `NewDBInstanceIdentifier` — new name for the instance
