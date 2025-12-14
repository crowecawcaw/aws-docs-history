# How

to perform a major version upgrade for RDS for PostgreSQL

We recommend the following process when performing a major version upgrade on
an Amazon RDS for PostgreSQL database:

1.  **Have a version-compatible parameter
    group ready** – If you are using a
    custom parameter group, you have two options. You can
    specify a default parameter group for the new DB engine
    version. Or you can create your own custom parameter group
    for the new DB engine version. For more information, see
    [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md") and
    [Working with DB cluster parameter groups for Multi-AZ DB clusters](USER_WorkingWithDBClusterParamGroups.md "USER_WorkingWithDBClusterParamGroups.md").
2.  **Check for unsupported database
    classes** – Check that your
    database's instance class is compatible with the
    PostgreSQL version you are upgrading to. For more
    information, see [Supported DB engines for DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").
3.  **Check for unsupported
    usage:**
    - **Prepared
      transactions** – Commit or roll
      back all open prepared transactions before
      attempting an upgrade.

    You can use the following query to verify that
    there are no open prepared transactions on your
    database.

    ```
    SELECT count(*) FROM pg_catalog.pg_prepared_xacts;
    ```

    - **Reg\* data
      types** – Remove all uses of the
      \*reg\** data types before
      attempting an upgrade. Except for
      `regtype` and `regclass`,
      you can't upgrade the *reg\*\*
      data types. The `pg_upgrade` utility
      can't persist this data type, which is used by
      Amazon RDS to do the upgrade.

    To verify that there are no uses of
    unsupported \*reg\*\* data types,
    use the following query for each database.

    ```

    SELECT count(*) FROM pg_catalog.pg_class c, pg_catalog.pg_namespace n, pg_catalog.pg_attribute a
      WHERE c.oid = a.attrelid
          AND NOT a.attisdropped
          AND a.atttypid IN ('pg_catalog.regproc'::pg_catalog.regtype,
                             'pg_catalog.regprocedure'::pg_catalog.regtype,
                             'pg_catalog.regoper'::pg_catalog.regtype,
                             'pg_catalog.regoperator'::pg_catalog.regtype,
                             'pg_catalog.regconfig'::pg_catalog.regtype,
                             'pg_catalog.regdictionary'::pg_catalog.regtype)
          AND c.relnamespace = n.oid
          AND n.nspname NOT IN ('pg_catalog', 'information_schema');

    ```

4.  **Check for invalid
    databases:**

        * Ensure there are no invalid databases. The
         `datconnlimit` column in the
         `pg_database` catalog includes a value
         of `-2` to mark databases as invalid
         that were interrupted during a `DROP
         DATABASE` operation.


        Use the following query to check for invalid
         databases:



        ```
        SELECT datname FROM pg_database WHERE datconnlimit = - 2;
        ```
        * The previous query returns invalid database
         names. You can use `DROP DATABASE
         `invalid_db_name`;`
         to drop invalid databases. You can also use the
         following command to drop invalid
         databases:



        ```
        SELECT 'DROP DATABASE ' || quote_ident(datname) || ';' FROM pg_database WHERE datconnlimit = -2 \gexec
        ```

    For more information about invalid databases, see [Understanding the behavior of autovacuum with
    invalid databases](appendix.postgresql.commondbatasks.md "appendix.postgresql.commondbatasks.md").

5.  **Handle logical replication
    slots** – An upgrade can't
    occur if the database has any logical replication slots.
    Logical replication slots are typically used for AWS DMS
    migration and for replicating tables from the database to
    data lakes, BI tools, and other targets. Before upgrading,
    make sure that you know the purpose of any logical
    replication slots that are in use, and confirm that
    it's okay to delete them. If the logical replication
    slots are still being used, you shouldn't delete them,
    and you can't proceed with the upgrade.

If the logical replication slots aren't needed, you can
delete them using the following SQL:

```
SELECT * FROM pg_replication_slots WHERE slot_type NOT LIKE 'physical';
SELECT pg_drop_replication_slot(slot_name);
```

Logical replication setups that use the `pglogical`
extension also need to have slots dropped for a successful
major version upgrade. For information about how to identify
and drop slots created using the `pglogical`
extension, see [Managing logical
replication slots for RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.pglogical.md "Appendix.PostgreSQL.CommonDBATasks.pglogical.md"). 6. **Handle read replicas** –
An upgrade of a Single-AZ DB instance or Multi-AZ DB instance deployment
also upgrades the in-Region read replicas
along with the primary DB instance. Amazon RDS doesn't upgrade Multi-AZ DB cluster
read replicas.

You can't upgrade read replicas separately. If you could,
it could lead to situations where the primary and replica
databases have different PostgreSQL major versions. However,
read replica upgrades might increase downtime on the primary
DB instance. To prevent a read replica upgrade, promote the
replica to a standalone instance or delete it before
starting the upgrade process.

The upgrade process recreates the read replica's
parameter group based on the read replica's current
parameter group. You can apply a custom parameter group to a
read replica only after the upgrade completes by modifying
the read replica. For more information about read replicas,
see [Working with read replicas for
Amazon RDS for PostgreSQL](USER_PostgreSQL.Replication.md "USER_PostgreSQL.Replication.md"). 7. **Handle large objects** – In PostgreSQL, large objects (also known as BLOBs) are used to store and manage large binary objects (like files, images, videos, etc.) that are larger than the maximum size allowed for regular column data types. For more information see [PostgreSQL Large Objects documentation](https://www.postgresql.org/docs/current/largeobjects.html "https://www.postgresql.org/docs/current/largeobjects.html").

An upgrade can run out of memory and fail if there are millions of large objects and the instance cannot handle them during an upgrade. The PostgreSQL major version upgrade process comprises of two broad phases: dumping the schema via pg_dump and restoring it through pg_restore. If your database has millions of large objects you need to ensure your instance has sufficient memory to handle the pg_dump and pg_restore during an upgrade and scale it to a larger instance type.

Before you begin an upgrade, check if your database is having any large objects. The catalog `pg_largeobject_metadata` holds metadata associated with large objects. The actual large object data is stored in `pg_largeobject`. Use the following query to check for the number of large objects:

```
SELECT count(*) FROM pg_largeobject_metadata;
```

To cleanup existing large objects or orphaned large objects, see [Managing large objects with the lo module](../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md "../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md").

When planning a major version upgrade, we recommend using an instance type with at least 32 GB of memory if your database contains 25 to 30 million large objects. This recommendation is based on our tests and can vary depending on your specific workload and database configuration. If your database includes additional objects (such as tables, indexes, or materialized views), we recommend selecting a larger instance type to ensure optimal performance during the upgrade process. 8. **Handle zero-ETL integrations**
– If you have an existing [zero-ETL integration](zero-etl.md "zero-etl.md"), [delete it](zero-etl.md "zero-etl.md") before
performing a major version upgrade. Then, after completing
the upgrade, recreate the integration. 9. **Perform a backup** – We
recommend that you perform a backup before performing the
major version upgrade so that you have a known restore point
for your database. If your backup retention period is
greater than 0, the upgrade process creates DB snapshots of
your database before and after upgrading. To change your
backup retention period, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md") and
[Modifying a Multi-AZ DB cluster for Amazon RDS](modify-multi-az-db-cluster.md "modify-multi-az-db-cluster.md").

To perform a backup manually, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md") and [Creating a Multi-AZ DB cluster snapshot for Amazon RDS](USER_CreateMultiAZDBClusterSnapshot.md "USER_CreateMultiAZDBClusterSnapshot.md"). 10. **Upgrade certain extensions before a
major version upgrade** – If you
plan to skip a major version with the upgrade, you need to
update certain extensions _before_
performing the major version upgrade. For example, upgrading
from versions 9.5.x or 9.6.x to version 11.x skips a major
version. The extensions to update include PostGIS and
related extensions for processing spatial data.

    * `address_standardizer`
    * `address_standardizer_data_us`
    * `postgis_raster`
    * `postgis_tiger_geocoder`
    * `postgis_topology`

You cannot directly upgrade to PostgreSQL version 17 if you
are using `rdkit` version 4.6.0 and lower, and
PostgreSQL version 16 and lower, due to `rdkit`
incompatibility. Below are the upgrade options:

    * If you are on PostgreSQL version 13 and lower,
     you need to perform a major version upgrade to
     version 14.14 and higher 14 versions, 15.9 and
     higher 15 versions, or 16.5 and higher 16 versions
     first, and then perform the version upgrade to
     PostgreSQL 17.
    * If you are on PostgreSQL version 14, 15, or
     16, you need to perform a minor version upgrade to
     14.14 and higher 14 versions, 15.9 and higher 15
     versions, or 16.5 and higher 16 versions, and then
     upgrade to PostgreSQL version 17.

Run the following command for each extension that you're
using:

```
ALTER EXTENSION `PostgreSQL-extension` UPDATE TO '`new-version`';
```

For more information, see [Upgrading PostgreSQL extensions in RDS for PostgreSQL databases](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md"). To learn more about upgrading PostGIS, see [Step 6: Upgrade the
PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update "Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update"). 11. **Drop certain extensions before the major
version upgrade** – An upgrade that
skips a major version to version 11.x doesn't support
updating the `pgRouting` extension. Upgrading
from versions 9.4.x, 9.5.x, or 9.6.x to versions 11.x skips
a major version. It's safe to drop the
`pgRouting` extension and then reinstall
it to a compatible version after the upgrade. For the
extension versions you can update to, see [Supported
PostgreSQL extension versions](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md").

The `tsearch2` and `chkpass` extensions
are no longer supported for PostgreSQL versions 11 or later.
If you are upgrading to version 11.x, drop the
`tsearch2`, and `chkpass`
extensions before the upgrade. 12. **Drop unknown data types**
– Drop `unknown` data types depending on
the target version.

PostgreSQL version 10 stopped supporting the
`unknown` data type. If a version 9.6
database uses the `unknown` data type, an upgrade
to a version 10 shows an error message such as the
following:

```
Database instance is in a state that cannot be upgraded: PreUpgrade checks failed:
The instance could not be upgraded because the 'unknown' data type is used in user tables.
Please remove all usages of the 'unknown' data type and try again."
```

To find the `unknown` data type in your database so
you can remove the offending column or change it to a
supported data type, use the following SQL:

```
SELECT DISTINCT data_type FROM information_schema.columns WHERE data_type ILIKE 'unknown';
```

13. **Perform an upgrade dry run**
    – We highly recommend testing a major version upgrade
    on a duplicate of your production database before attempting
    the upgrade on your production database. You can monitor the
    execution plans on the duplicate test database for any
    possible execution plan regressions and to evaluate its
    performance. To create a duplicate test instance, you can
    either restore your database from a recent snapshot or do a
    point-in-time restore of your database to its latest
    restorable time.

For more information, see [Restoring from a snapshot](USER_RestoreFromSnapshot.md#USER_RestoreFromSnapshot.Restoring "USER_RestoreFromSnapshot.md#USER_RestoreFromSnapshot.Restoring") or
[Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md"). For Multi-AZ DB clusters, see [Restoring from a
snapshot to a Multi-AZ DB cluster](USER_RestoreFromMultiAZDBClusterSnapshot.md "USER_RestoreFromMultiAZDBClusterSnapshot.md") or [Restoring a Multi-AZ DB cluster to a specified time](USER_PIT.md "USER_PIT.md").

For details on performing the upgrade, see [Manually upgrading the engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual").

In upgrading a version 9.6 database to version 10, be aware
that PostgreSQL 10 enables parallel queries by default. You
can test the impact of parallelism
_before_ the upgrade by changing
the `max_parallel_workers_per_gather` parameter
on your test database to 2.

###### Note

The default value for
`max_parallel_workers_per_gather`
parameter in the `default.postgresql10`
DB parameter group is 2.

For more information, see [Parallel Query](https://www.postgresql.org/docs/10/parallel-query.html "https://www.postgresql.org/docs/10/parallel-query.html") in the PostgreSQL
documentation. To disable parallelism on version 10, set the
`max_parallel_workers_per_gather`
parameter to 0.

During the major version upgrade, the `public` and
`template1` databases and the
`public` schema in every database are
temporarily renamed. These objects appear in the logs with
their original name and a random string appended. The string
is appended so that custom settings such as
`locale` and `owner` are
preserved during the major version upgrade. After the
upgrade completes, the objects are renamed back to their
original names.

###### Note

During the major version upgrade process, you can't do
a point-in-time restore of your DB instance or Multi-AZ DB cluster.
After Amazon RDS performs the upgrade, it takes an
automatic backup of the database. You can perform a
point-in-time restore to times before the upgrade
began and after the automatic backup of your
database has completed. 14. **If an upgrade fails with precheck
procedure errors, resolve the issues**
– During the major version upgrade process, Amazon RDS for
PostgreSQL first runs a precheck procedure to identify any
issues that might cause the upgrade to fail. The precheck
procedure checks all potential incompatible conditions
across all databases in the instance.

If the precheck encounters an issue, it creates a log event
indicating the upgrade precheck failed. The precheck process
details are in an upgrade log named
`pg_upgrade_precheck.log` for all the
databases of a database. Amazon RDS appends a timestamp to the
file name. For more information about viewing logs, see
[Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md").

If a read replica upgrade fails at precheck, replication on
the failed read replica is broken and the read replica is
put in the terminated state. Delete the read replica and
recreate a new read replica based on the upgraded primary DB
instance.

Resolve all of the issues identified in the precheck log and
then retry the major version upgrade. The following is an
example of a precheck log.

```
------------------------------------------------------------------------
Upgrade could not be run on Wed Apr 4 18:30:52 2018
-------------------------------------------------------------------------
The instance could not be upgraded from 9.6.11 to 10.6 for the following reasons.
Please take appropriate action on databases that have usage incompatible with the requested major engine version upgrade and try the upgrade again.

* There are uncommitted prepared transactions. Please commit or rollback all prepared transactions.* One or more role names start with 'pg_'. Rename all role names that start with 'pg_'.

* The following issues in the database 'my"million$"db' need to be corrected before upgrading:** The ["line","reg*"] data types are used in user tables. Remove all usage of these data types.
** The database name contains characters that are not supported by RDS for PostgreSQL. Rename the database.
** The database has extensions installed that are not supported on the target database version. Drop the following extensions from your database: ["tsearch2"].

* The following issues in the database 'mydb' need to be corrected before upgrading:** The database has views or materialized views that depend on 'pg_stat_activity'. Drop the views.
```

15. **If a read replica upgrade fails while
    upgrading the database, resolve the issue**
    – A failed read replica is placed in the
    `incompatible-restore` state and
    replication is terminated on the database. Delete the read
    replica and recreate a new read replica based on the
    upgraded primary DB instance.

###### Note

Amazon RDS doesn't upgrade read replicas for Multi-AZ DB clusters. If you
perform a major version upgrade on a Multi-AZ DB cluster, then the
replication state of its read replicas changes to
**terminated**.

A read replica upgrade might fail for the following
reasons:

    * It was unable to catch up with the primary
     DB instance even after a wait time.
    * It was in a terminal or incompatible lifecycle
     state such as storage-full, incompatible-restore,
     and so on.
    * When the primary DB instance upgrade started, there
     was a separate minor version upgrade running on
     the read replica.
    * The read replica used incompatible
     parameters.
    * The read replica was unable to communicate
     with the primary DB instance to synchronize the data
     folder.

16. **Upgrade your production
    database** – When the dry-run major
    version upgrade is successful, you should be able to upgrade
    your production database with confidence. For more
    information, see [Manually upgrading the engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual").
17. Run the `ANALYZE` operation to refresh the
    `pg_statistic` table. You should do this
    for every database on all your PostgreSQL databases.
    Optimizer statistics aren't transferred during a major
    version upgrade, so you need to regenerate all statistics to
    avoid performance issues. Run the command without any
    parameters to generate statistics for all regular tables in
    the current database, as follows:

```
ANALYZE VERBOSE;
```

The `VERBOSE` flag is optional, but using it shows
you the progress. For more information, see [ANALYZE](https://www.postgresql.org/docs/10/sql-analyze.html "https://www.postgresql.org/docs/10/sql-analyze.html") in the PostgreSQL documentation.

When analyzing specific tables instead of using ANALYZE
VERBOSE, run the ANALYZE command for each table as
follows:

```
ANALYZE `table_name`;
```

For partitioned tables, always analyze the parent table. This
process:

    * Automatically samples rows across all
     partitions
    * Updates statistics for each partition
     recursively
    * Maintains essential planning statistics at the
     parent level

While parent tables store no actual data, analyzing them is
vital for query optimization. Running ANALYZE only on
individual partitions can lead to poor query performance
since the optimizer won't have the comprehensive statistics
needed for efficient cross-partition planning.

###### Note

Run ANALYZE on your system after the upgrade to avoid
performance issues.
After the major version upgrade is complete, we recommend the
following:

- A PostgreSQL upgrade doesn't upgrade any PostgreSQL
  extensions. To upgrade extensions, see [Upgrading PostgreSQL extensions in RDS for PostgreSQL databases](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").
- Optionally, use Amazon RDS to view two logs that the
  `pg_upgrade` utility produces. These are
  `pg_upgrade_internal.log` and
  `pg_upgrade_server.log`. Amazon RDS appends a
  timestamp to the file name for these logs. You can view
  these logs as you can any other log. For more information,
  see [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md").

You can also upload the upgrade logs to Amazon CloudWatch Logs. For more
information, see [Publishing
PostgreSQL logs to Amazon CloudWatch Logs](USER_LogAccess.Concepts.md#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs "USER_LogAccess.Concepts.md#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs").

- To verify that everything works as expected, test your
  application on the upgraded database with a similar
  workload. After the upgrade is verified, you can delete this
  test instance.
