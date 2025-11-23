# Setting up to transport a PostgreSQL

database

Before you begin, make sure that your RDS for PostgreSQL DB instances meet the following requirements:

- The RDS for PostgreSQL DB instances for source and destination must run the same version of PostgreSQL.
- The destination DB can't have a database of the same name as the source DB that you want to transport.
- The account you use to run the transport needs `rds_superuser` privileges on both the source DB and the destination DB.
- The security group for the source DB instance must allow inbound access from the
  destination DB instance. This might already be the case if your source and destination
  DB instances are located in the VPC. For more information about security groups, see [Controlling access with security
  groups](Overview.md "Overview.md").
  Transporting databases from a source DB instance to a destination DB instance requires several changes to the DB parameter group associated with
  each instance. That means that you must create a custom DB parameter group for the
  source DB instance and create a custom DB parameter group for the destination DB instance.

###### Note

If your DB instances are already configured using custom
DB parameter groups, you can start with step 2 in the following procedure.

###### To configure the custom DB group parameters for transporting databases

For the following steps, use an account that has `rds_superuser` privileges.

1.  If the source and destination DB instances use a default DB parameter group, you need to create
    a custom DB parameter group using the appropriate version for your instances. You do this so
    you can change values for several parameters.
    For more information, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
2.  In the custom DB parameter group, change values for the following parameters:

        * `shared_preload_libraries` – Add `pg_transport` to the list of
         libraries.
        * `pg_transport.num_workers` – The default value is 3. Increase or reduce this
         value as needed for your database. For a 200 GB database, we recommend no larger than 8. Keep in mind that
         if you increase the default value for this parameter, you should also increase the value of `max_worker_processes`.
        * `pg_transport.work_mem` – The default value is either 128 MB or 256 MB, depending
         on the PostgreSQL version. The default setting can typically be left unchanged.
        * `max_worker_processes` – The value of this parameter needs to be set using the
         following calculation:



        ```
        (3 * pg_transport.num_workers) + 9
        ```

        This value is required on the destination to handle various background worker
         processes involved in the transport. To learn more about
         `max_worker_processes,` see [Resource Consumption](https://www.postgresql.org/docs/current/runtime-config-resource.html "https://www.postgresql.org/docs/current/runtime-config-resource.html") in the PostgreSQL documentation.

    For more information about `pg_transport` parameters, see [Transportable databases parameter reference](PostgreSQL.TransportableDB.md "PostgreSQL.TransportableDB.md") .

3.  Reboot the source RDS for PostgreSQL DB instance and the destination instance so that
    the settings for the parameters take effect.
4.  Connect to your RDS for PostgreSQL source DB instance.

```
psql --host=`source-instance`.`111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password
```

5. Remove extraneous extensions from the public schema of the DB instance. Only the `pg_transport`
   extension is allowed during the actual transport operation.
6. Install the `pg_transport` extension as follows:

```
`postgres=>` `CREATE EXTENSION pg_transport;`
`CREATE EXTENSION`
```

7. Connect to your RDS for PostgreSQL destination DB instance. Remove any extraneous extensions, and then install
   the `pg_transport` extension.

```
`postgres=>` `CREATE EXTENSION pg_transport;`
`CREATE EXTENSION`
```
