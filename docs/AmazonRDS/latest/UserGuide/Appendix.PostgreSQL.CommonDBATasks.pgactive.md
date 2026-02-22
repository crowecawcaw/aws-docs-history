# Initializing the

pgactive extension capability

To initialize the `pgactive` extension capability on your RDS for PostgreSQL DB
instance, set the value of the `rds.enable_pgactive` parameter to `1`
and then create the extension in the database. Doing so automatically turns on the parameters
`rds.logical_replication` and `track_commit_timestamp` and sets the
value of `wal_level` to `logical`.

You must have permissions as the `rds_superuser` role to perform these
tasks.

You can use the AWS Management Console or the AWS CLI to create the required RDS for PostgreSQL DB instances. The
steps following assume that your RDS for PostgreSQL DB instance is associated with a custom DB
parameter group. For information about creating a custom DB parameter group, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### To initialize the pgactive extension capability

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose your RDS for PostgreSQL DB instance.
3. Open the **Configuration** tab for your RDS for PostgreSQL DB
   instance. In the instance details, find the **DB instance parameter
   group** link.
4. Choose the link to open the custom parameters associated with your RDS for PostgreSQL
   DB instance.
5. Find the `rds.enable_pgactive` parameter, and set it to `1`
   to initialize the `pgactive` capability.
6. Choose **Save changes**.
7. In the navigation pane of the Amazon RDS console, choose
   **Databases**.
8. Select your RDS for PostgreSQL DB instance, and then choose **Reboot**
   from the **Actions** menu.
9. Confirm the DB instance reboot so that your changes take effect.
10. When the DB instance is available, you can use `psql` or any other PostgreSQL
    client to connect to the RDS for PostgreSQL DB instance.

The following example assumes that your RDS for PostgreSQL DB instance has a default database
named `postgres`.

```
psql --host=`mydb.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password=`PASSWORD` --dbname=`postgres`

```

11. To verify that pgactive is initialized, run the following command.

```
`postgres=>``SELECT setting ~ 'pgactive'
FROM pg_catalog.pg_settings
WHERE name = 'shared_preload_libraries';`
```

If `pgactive` is in `shared_preload_libraries`, the
preceding command will return the following:

```

`?column?
----------
 t`
```

###### To initialize the pgactive extension capability

To initialize the `pgactive` using the AWS CLI, call the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md") operation to modify certain parameters in your
custom parameter group as shown in the following procedure.

1. Use the following AWS CLI command to set `rds.enable_pgactive` to
   `1` to initialize the `pgactive` capability for the
   RDS for PostgreSQL DB instance.

```
`postgres=>`aws rds modify-db-parameter-group \
   --db-parameter-group-name `custom-param-group-name` \
   --parameters "ParameterName=rds.enable_pgactive,ParameterValue=1,ApplyMethod=pending-reboot" \
   --region `aws-region`
```

2. Use the following AWS CLI command to reboot the RDS for PostgreSQL DB instance so that
   the `pgactive` library is initialized.

```
aws rds reboot-db-instance \
    --db-instance-identifier `your-instance` \
    --region `aws-region`
```

3. When the instance is available, use `psql` to connect to the RDS for PostgreSQL DB instance.

```
psql --host=`mydb.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=`master user` --password=`PASSWORD` --dbname=`postgres`

```

4. To verify that pgactive is initialized, run the following command.

```
`postgres=>``SELECT setting ~ 'pgactive'
FROM pg_catalog.pg_settings
WHERE name = 'shared_preload_libraries';`
```

If `pgactive` is in `shared_preload_libraries`, the
preceding command will return the following:

```

`?column?
----------
 t`
```
