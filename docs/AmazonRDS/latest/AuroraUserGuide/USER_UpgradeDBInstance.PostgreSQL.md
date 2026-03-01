# Performing a major version upgrade

Major version upgrades might contain database changes that are not backward-compatible
with previous versions of the database. New functionality in a new version can cause
your existing applications to stop working correctly. To avoid issues, Amazon Aurora
doesn't apply major version upgrades automatically. Rather, we recommend that you
carefully plan for a major version upgrade by following these steps:

1. Choose the major version that you want from the list of available targets from
   those listed for your version in the table. You can get a precise list of
   versions available in your AWS Region for your current version by using the
   AWS CLI. For details, see [Getting a list of available versions in your AWS Region](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").
2. Verify that your applications work as expected on a trial deployment of the
   new version. For information about the complete process, see [Testing an upgrade of your production DB cluster to a new major version](#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary "#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary").
3. After verifying that your applications work as expected on the trial
   deployment, you can upgrade your cluster. For details, see [Upgrading the Aurora PostgreSQL engine to a new major version](#USER_UpgradeDBInstance.Upgrading.Manual "#USER_UpgradeDBInstance.Upgrading.Manual").

###### Note

You can perform a major version upgrade from Babelfish for Aurora PostgreSQL
13-based versions starting from 13.6 to Aurora PostgreSQL 14-based versions starting
from 14.6. Babelfish for Aurora PostgreSQL 13.4 and 13.5 don't support major
version upgrade.

You can get a list of engine versions available as major version upgrade targets for
your Aurora PostgreSQL DB cluster by querying your AWS Region using the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command, as follows.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
  --engine aurora-postgresql \
  --engine-version `version-number` \
  --query 'DBEngineVersions[].ValidUpgradeTarget[?IsMajorVersionUpgrade == `true`].{EngineVersion:EngineVersion}' \
  --output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
  --engine aurora-postgresql ^
  --engine-version `version-number` ^
  --query "DBEngineVersions[].ValidUpgradeTarget[?IsMajorVersionUpgrade == `true`].{EngineVersion:EngineVersion}" ^
  --output text
```

In some cases, the version that you want to upgrade to isn't a target for your
current version. In such cases, use the information in the [versions table](USER_UpgradeDBInstance.PostgreSQL.md#versions-table "USER_UpgradeDBInstance.PostgreSQL.md#versions-table") to perform minor version
upgrades until your cluster is at a version that has your chosen target in its row of
targets.

## Testing an upgrade of your production DB cluster to a new major version

Each new major version includes enhancements to the query optimizer that are
designed to improve performance. However, your workload might include queries that
result in a worse performing plan in the new version. That's why we recommend
that you test and review performance before upgrading in production. You can manage
query plan stability across versions by using the Query Plan Management (QPM)
extension, as detailed in [Ensuring plan stability after a major version upgrade](AuroraPostgreSQL.Optimize.md#AuroraPostgreSQL.Optimize.BestPractice.MajorVersionUpgrade "AuroraPostgreSQL.Optimize.md#AuroraPostgreSQL.Optimize.BestPractice.MajorVersionUpgrade").

Before upgrading your production Aurora PostgreSQL DB clusters to a new major version, we
strongly recommend that you test the upgrade to verify that all your applications
work correctly:

1. Have a version-compatible parameter group ready.

If you are using a custom DB instance or DB cluster parameter group, you can
choose from two options:

    1. Specify the default DB instance, DB cluster parameter group, or both
     for the new DB engine version.
    2. Create your own custom parameter group for the new DB engine
     version.

2. Check for invalid databases and drop any that exist.

The `datconnlimit` column in the `pg_database`
catalog includes a value of `-2` to mark as invalid any databases
that were interrupted during a `DROP DATABASE` operation. Use the
following query to check whether invalid databases exist.

```
SELECT
    datname
FROM
    pg_database
WHERE
    datconnlimit = - 2;
```

If the query returns database names, these databases are invalid. Use the
`DROP DATABASE invalid_db_name` statement to drop invalid
databases. You can use the following dynamic statement to drop all invalid
databases.

```
SELECT
    'DROP DATABASE ' || quote_ident(datname) || ';'
FROM
    pg_database
WHERE
    datconnlimit = -2 \gexec
```

3. Check for unsupported usage:
   - Commit or roll back all open prepared transactions before
     attempting an upgrade. You can use the following query to verify
     that there are no open prepared transactions on your instance.

   ```
   SELECT count(*) FROM pg_catalog.pg_prepared_xacts;
   ```

   - Remove all uses of the \*reg\** data types before
     attempting an upgrade. Except for `regtype` and
     `regclass`, you can't upgrade the
     *reg\*\* data types. The pg_upgrade utility
     (used by Amazon Aurora to do the upgrade) can't persist this data
     type. To learn more about this utility, see [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html "https://www.postgresql.org/docs/current/pgupgrade.html") in the PostgreSQL documentation.

   To verify that there are no uses of unsupported
   \*reg\*\* data types, use the following query
   for each database.

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

   - If you are upgrading an Aurora PostgreSQL version 10.18 or higher DB
     cluster that has the `pgRouting` extension installed,
     drop the extension before upgrading to version 12.4 or
     higher.

   If you are upgrading an Aurora PostgreSQL 10.x version that has the
   extension `pg_repack` version 1.4.3 installed, drop the
   extension before upgrading to any higher version.

4. Check for template1 and template0 databases.

For a successful upgrade, template 1 and template 0 databases must exist
and should be listed as a template. To check on this, use the following
command:

```
SELECT datname, datistemplate FROM pg_database;
                        `datname | datistemplate
-----------+---------------
template0 | t
rdsadmin | f
template1 | t
postgres | f`

```

In the command output, the `datistemplate` value for template1
and template0 databases should be `t`. 5. Drop logical replication slots.

The upgrade process can't proceed if the Aurora PostgreSQL DB cluster is using
any logical replication slots. Logical replication slots are typically used
for short-term data migration tasks, such as migrating data using AWS DMS or
for replicating tables from the database to data lakes, BI tools, or other
targets. Before upgrading, make sure that you know the purpose of any
logical replication slots that exist, and confirm that it's okay to
delete them. You can check for logical replication slots using the following
query:

```
SELECT * FROM pg_replication_slots;
```

If logical replication slots are still being used, you shouldn't
delete them, and you can't proceed with the upgrade. However, if the
logical replication slots aren't needed, you can delete them using the
following SQL:

```
SELECT pg_drop_replication_slot(`slot_name`);
```

Logical replication scenarios that use the `pglogical`
extension also need to have slots dropped from the publisher node for a
successful major version upgrade on that node. However, you can restart the
replication process from the subscriber node after the upgrade. For more
information, see [Reestablishing logical replication after a major upgrade](Appendix.PostgreSQL.CommonDBATasks.pglogical.md "Appendix.PostgreSQL.CommonDBATasks.pglogical.md"). 6. Perform a backup.

The upgrade process creates a DB cluster snapshot of your DB cluster during
upgrading. If you also want to do a manual backup before the upgrade
process, see [Creating a DB cluster snapshot](USER_CreateSnapshotCluster.md "USER_CreateSnapshotCluster.md") for more
information. 7. Upgrade certain extensions to the latest available version before
performing the major version upgrade. The extensions to update include the
following:

    * `pgRouting`
    * `postgis_raster`
    * `postgis_tiger_geocoder`
    * `postgis_topology`
    * `address_standardizer`
    * `address_standardizer_data_us`

Run the following command for each extension that's currently
installed.

```
ALTER EXTENSION `PostgreSQL-extension` UPDATE TO '`new-version`';
```

For more information, see [Upgrading PostgreSQL extensions](USER_UpgradeDBInstance.Upgrading.md "USER_UpgradeDBInstance.Upgrading.md"). To
learn more about upgrading PostGIS, see [Step 6: Upgrade the PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update "Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update"). 8. If you're upgrading to version 11.x, drop the extensions that it
doesn't support before performing the major version upgrade. The
extensions to drop include:

    * `chkpass`
    * `tsearch2`

9. Drop `unknown` data types, depending on your target
   version.

PostgreSQL version 10 doesn't support the `unknown` data
type. If a version 9.6 database uses the `unknown` data type, an
upgrade to version 10 shows an error message such as the following.

```
Database instance is in a state that cannot be upgraded: PreUpgrade checks failed:
The instance could not be upgraded because the 'unknown' data type is used in user tables.
Please remove all usages of the 'unknown' data type and try again."
```

To find the `unknown` data type in your database so that you
can remove such columns or change them to supported data types, use the
following SQL code for each database.

```
SELECT n.nspname, c.relname, a.attname
    FROM pg_catalog.pg_class c,
    pg_catalog.pg_namespace n,
    pg_catalog.pg_attribute a
    WHERE c.oid = a.attrelid AND NOT a.attisdropped AND
    a.atttypid = 'pg_catalog.unknown'::pg_catalog.regtype AND
    c.relkind IN ('r','m','c') AND
    c.relnamespace = n.oid AND
    n.nspname !~ '^pg_temp_' AND
    n.nspname !~ '^pg_toast_temp_' AND n.nspname NOT IN ('pg_catalog', 'information_schema');
```

10. Perform a dry-run upgrade.

We highly recommend testing a major version upgrade on a duplicate of your
production database before trying the upgrade on your production database.
You can monitor the execution plans on the duplicate test instance for any
possible execution plan regressions and to evaluate its performance. To
create a duplicate test instance, you can either restore your database from
a recent snapshot or clone your database. For more information, see [Restoring from a snapshot](aurora-restore-snapshot.md#aurora-restore-snapshot.Restoring "aurora-restore-snapshot.md#aurora-restore-snapshot.Restoring") or [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.md "Aurora.Managing.md").

For more information, see [Upgrading the Aurora PostgreSQL engine to a new major version](#USER_UpgradeDBInstance.Upgrading.Manual "#USER_UpgradeDBInstance.Upgrading.Manual"). 11. Upgrade your production instance.

When your dry-run major version upgrade is successful, you should be able
to upgrade your production database with confidence. For more information,
see [Upgrading the Aurora PostgreSQL engine to a new major version](#USER_UpgradeDBInstance.Upgrading.Manual "#USER_UpgradeDBInstance.Upgrading.Manual").

###### Note

During the upgrade process, Aurora PostgreSQL takes a DB cluster snapshot. You
can't do a point-in-time restore of your cluster during this
process. Later, you can perform a point-in-time restore to times before
the upgrade began and after the automatic snapshot of your instance has
completed. However, you can't perform a point-in-time restore to a
previous minor version.

For information about an upgrade in progress, you can use Amazon RDS to view
two logs that the pg_upgrade utility produces. These are
`pg_upgrade_internal.log` and
`pg_upgrade_server.log`. Amazon Aurora appends a timestamp to the
file name for these logs. You can view these logs as you can any other log.
For more information, see [Monitoring Amazon Aurora log files](USER_LogAccess.md "USER_LogAccess.md"). 12. Upgrade PostgreSQL extensions. The PostgreSQL upgrade process doesn't
upgrade any PostgreSQL extensions. For more information, see [Upgrading PostgreSQL extensions](USER_UpgradeDBInstance.Upgrading.md "USER_UpgradeDBInstance.Upgrading.md").

## Post-upgrade recommendations

After you complete a major version upgrade, we recommend the following:

- Run the `ANALYZE` operation to refresh the
  `pg_statistic` table. You should do this for every database
  on all your PostgreSQL DB instances. Optimizer statistics aren't
  transferred during a major version upgrade, so you need to regenerate all
  statistics to avoid performance issues. Run the command without any
  parameters to generate statistics for all regular tables in the current
  database, as follows:

```
ANALYZE VERBOSE;
```

The `VERBOSE` flag is optional, but using it shows you the
progress. For more information, see [ANALYZE](https://www.postgresql.org/docs/10/sql-analyze.html "https://www.postgresql.org/docs/10/sql-analyze.html") in the PostgreSQL documentation.

When analyzing specific tables instead of using ANALYZE VERBOSE, run the
ANALYZE command for each table as follows:

```
ANALYZE `table_name`;
```

For partitioned tables, always analyze the parent table. This
process:

    + Automatically samples rows across all partitions
    + Updates statistics for each partition recursively
    + Maintains essential planning statistics at the parent level

While parent tables store no actual data, analyzing them is vital for
query optimization. Running ANALYZE only on individual partitions can lead
to poor query performance since the optimizer won't have the comprehensive
statistics needed for efficient cross-partition planning.

###### Note

Run ANALYZE on your system after the upgrade to avoid performance
issues.

- If you upgraded to PostgreSQL version 10, run `REINDEX` on any
  hash indexes you have. Hash indexes were changed in version 10 and must be
  rebuilt. To locate invalid hash indexes, run the following SQL for each
  database that contains hash indexes.

```
SELECT idx.indrelid::regclass AS table_name,
   idx.indexrelid::regclass AS index_name
FROM pg_catalog.pg_index idx
   JOIN pg_catalog.pg_class cls ON cls.oid = idx.indexrelid
   JOIN pg_catalog.pg_am am ON am.oid = cls.relam
WHERE am.amname = 'hash'
AND NOT idx.indisvalid;
```

- We recommend that you test your application on the upgraded database with
  a similar workload to verify that everything works as expected. After the
  upgrade is verified, you can delete this test instance.

## Upgrading the Aurora PostgreSQL engine to a new major version

When you initiate the upgrade process to a new major version, Aurora PostgreSQL takes
a snapshot of the Aurora DB cluster before it makes any changes to your cluster. This
snapshot is created for major version upgrades only, not minor version upgrades.
When the upgrade process completes, you can find this snapshot among the manual
snapshots listed under **Snapshots** in the RDS console. The
snapshot name includes `preupgrade` as its prefix, the name of your
Aurora PostgreSQL DB cluster, the source version, the target version, and the date and
timestamp, as shown in the following example.

```
preupgrade-docs-lab-apg-global-db-12-8-to-13-6-2022-05-19-00-19
```

After the upgrade completes, you can use the snapshot that Aurora created and
stored in your manual snapshot list to restore the DB cluster to its previous version, if
necessary.

###### Tip

In general, snapshots provide many ways to restore your Aurora DB cluster to various
points in time. To learn more, see [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md") and [Restoring a DB cluster to a specified time](aurora-pitr.md "aurora-pitr.md"). However, Aurora PostgreSQL doesn't support
using a snapshot to restore to a previous minor version.

During the major version upgrade process, Aurora allocates a volume and clones the
source Aurora PostgreSQL DB cluster. If the upgrade fails for any reason, Aurora PostgreSQL uses
the clone to roll back the upgrade. After more than 15 clones of a source volume are
allocated, subsequent clones become full copies and take longer. This can cause the
upgrade process also to take longer. If Aurora PostgreSQL rolls back the upgrade, be
aware of the following:

- You might see billing entries and metrics for both the original volume and
  the cloned volume allocated during the upgrade. Aurora PostgreSQL cleans up the
  extra volume after the cluster backup retention window is beyond the time of
  the upgrade.
- The next cross-Region snapshot copy from this cluster will be a full copy
  instead of an incremental copy.

To safely upgrade the DB instances that make up your cluster, Aurora PostgreSQL uses
the pg_upgrade utility. After the writer upgrade completes, each reader instance
experiences a brief outage while it's upgraded to the new major version. To
learn more about this PostgreSQL utility, see [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html "https://www.postgresql.org/docs/current/pgupgrade.html")
in the PostgreSQL documentation.

You can upgrade your Aurora PostgreSQL DB cluster to a new version by using the AWS Management Console,
the AWS CLI, or the RDS API.

###### To upgrade the engine version of a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the DB cluster that you want to upgrade.
3. Choose **Modify**. The **Modify DB
   cluster** page appears.
4. For **Engine version**, choose the new
   version.
5. Choose **Continue** and check the summary of
   modifications.
6. To apply the changes immediately, choose **Apply
   immediately**. Choosing this option can cause an outage
   in some cases. For more information, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
7. On the confirmation page, review your changes. If they are
   correct, choose **Modify Cluster** to save your
   changes.

Or choose **Back** to edit your changes or
**Cancel** to cancel your changes.
To upgrade the engine version of a DB cluster, use the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md")
AWS CLI command. Specify the following parameters:

- `--db-cluster-identifier` – The name of the DB
  cluster.
- `--engine-version` – The version number of the
  database engine to upgrade to. For information about valid engine
  versions, use the AWS CLI [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.
- `--allow-major-version-upgrade` – A required
  flag when the `--engine-version` parameter is a different
  major version than the DB cluster's current major version.
- `--no-apply-immediately` – Apply changes during
  the next maintenance window. To apply changes immediately, use
  `--apply-immediately`.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `mydbcluster` \
    --engine-version `new_version` \
    --allow-major-version-upgrade \
    --no-apply-immediately
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `mydbcluster` ^
    --engine-version `new_version` ^
    --allow-major-version-upgrade ^
    --no-apply-immediately
```

To upgrade the engine version of a DB cluster, use the [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md")
operation. Specify the following parameters:

- `DBClusterIdentifier` – The name of the DB
  cluster, for example
  `mydbcluster`.
- `EngineVersion` – The version number of the
  database engine to upgrade to. For information about valid engine
  versions, use the [DescribeDBEngineVersions](../APIReference/API_DescribeDBEngineVersions.md "../APIReference/API_DescribeDBEngineVersions.md") operation.
- `AllowMajorVersionUpgrade` – A required flag
  when the `EngineVersion` parameter is a different major
  version than the DB cluster's current major version.
- `ApplyImmediately` – Whether to apply changes
  immediately or during the next maintenance window. To apply changes
  immediately, set the value to `true`. To apply changes
  during the next maintenance window, set the value to
  `false`.

### Major upgrades for global databases

For an Aurora global database cluster, the upgrade process upgrades all DB
clusters that make up your Aurora global database at the same time. It does so to
ensure that each runs the same Aurora PostgreSQL version. It also ensures that any
changes to system tables, data file formats, and so on, are automatically
replicated to all secondary clusters.

To upgrade a global database cluster to a new major version of Aurora PostgreSQL,
we recommend that you test your applications on the upgraded version, as
detailed in [Testing an upgrade of your production DB cluster to a new major version](#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary "#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary"). Be sure to prepare your DB cluster parameter group and DB parameter group
settings for each AWS Region in your Aurora global database before the upgrade
as detailed in [step 1.](#step-1 "#step-1") of [Testing an upgrade of your production DB cluster to a new major version](#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary "#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary").

If your Aurora PostgreSQL global database cluster has a recovery point objective
(RPO) set for its `rds.global_db_rpo` parameter, make sure to reset
the parameter before upgrading. The major version upgrade process doesn't
work if the RPO is turned on. By default, this parameter is turned off. For more
information about Aurora PostgreSQL global databases and RPO, see [Managing RPOs for Aurora PostgreSQL–based global databases](aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery "aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery").

If you verify that your applications can run as expected on the trial
deployment of the new version, you can start the upgrade process. To do so, see
[Upgrading the Aurora PostgreSQL engine to a new major version](#USER_UpgradeDBInstance.Upgrading.Manual "#USER_UpgradeDBInstance.Upgrading.Manual"). Be sure to choose
the top-level item from the **Databases** list in the RDS
console, **Global database**, as shown in the following
image.

![Console image showing an Aurora global database, an Aurora Serverless DB cluster, and another Aurora PostgreSQL DB cluster](images/aurora-global-database-plus-other.png)

As with any modification, you can confirm that you want the process to proceed
when prompted.

![Console image showing prompt to confirm the upgrade process for an Aurora PostgreSQL DB cluster](images/aurora-global-db-apg-upgrade-2.png)

Rather than using the console, you can start the upgrade process by using the
AWS CLI or the RDS API. As with the console, you operate on the Aurora global
database cluster rather than any of its constituents, as follows:

- Use the [modify-global-cluster](../../../cli/latest/reference/rds/modify-global-cluster.md "../../../cli/latest/reference/rds/modify-global-cluster.md") AWS CLI command to start the upgrade
  for your Aurora global database by using the AWS CLI.
- Use the [ModifyGlobalCluster](../APIReference/API_ModifyGlobalCluster.md "../APIReference/API_ModifyGlobalCluster.md") API to start the upgrade.
