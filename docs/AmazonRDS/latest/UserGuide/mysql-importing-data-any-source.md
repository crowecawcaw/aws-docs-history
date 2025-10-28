# Importing data from any source to an

Amazon RDS for MySQL DB instance

With Amazon RDS, you can migrate existing MySQL data from any source to an RDS for MySQL DB
instance. You can transfer data from on-premises databases, other cloud providers, or
existing RDS for MySQL DB instances to your target RDS for MySQL DB instance. With this
functionality, you can consolidate databases, implement disaster recovery solutions, or
transition from self-managed databases. Common scenarios include moving from self-hosted
MySQL servers to fully managed Amazon RDS DB instances, consolidating multiple MySQL databases
into a single DB instance, or creating test environments with production data. The following
sections provide step-by-step instructions for importing your MySQL data using methods such
as `mysqldump`, backup files, or replication.

## Step 1: Create flat

files containing the data to be loaded

Use a common format, such as comma-separated values (CSV), to store the data to be
loaded. Each table must have its own file—you can't combine data for multiple
tables in the same file. Give each file the same name as the table it corresponds to.
The file extension can be anything you like. For example, if the table name is
`sales`, the file name could be `sales.csv` or
`sales.txt`.

If possible, order the data by the primary key of the table being loaded. Doing this
drastically improves load times and minimizes disk storage requirements.

The speed and efficiency of this procedure depends on keeping the size of the files
small. If the uncompressed size of any individual file is larger than 1 GiB, split it
into multiple files and load each one separately.

On Unix-like systems (including Linux), use the `split` command. For
example, the following command splits the `sales.csv` file into multiple
files of less than 1 GiB, splitting only at line breaks (-C 1024m). The names of the new
files include ascending numerical suffixes. The following command produces files with
names such as `sales.part_00` and `sales.part_01`.

```
split -C 1024m -d sales.csv sales.part_
```

Similar utilities are available for other operating systems.

You can store the flat files anywhere. However, when you load the data in [Step 5](#mysql-importing-data-any-source-load-data "#mysql-importing-data-any-source-load-data"), you must invoke
the `mysql` shell from the same location where the files exist, or use the
absolute path for the files when you run `LOAD DATA LOCAL INFILE`.

## Step 2: Stop any

applications from accessing the target DB instance

Before starting a large load, stop all application activity from accessing the target
DB instance that you plan to load to. We recommend this particularly if other sessions
will be modifying the tables being loaded or tables that they reference. Doing this
reduces the risk of constraint violations occurring during the load and improves load
performance. It also makes it possible to restore the DB instance to the point just
before the load without losing changes made by processes not involved in the load.

Of course, this might not be possible or practical. If you can't stop applications
from accessing the DB instance before the load, take steps to ensure the availability
and integrity of your data. The specific steps required vary greatly depending upon
specific use cases and site requirements.

## Step 3: Create a DB

snapshot

If you plan to load data into a new DB instance that contains no data, you can skip
this step. Otherwise, we recommend that you create DB snapshots of the target Amazon RDS DB
instance both before and after the data load. Amazon RDS DB snapshots are complete backups of
your DB instance that you can use to restore your DB instance to a known state. When you
initiate a DB snapshot, I/O operations to your DB instance are momentarily suspended
while your database is backed up.

Creating a DB snapshot immediately before the load makes it possible for you to
restore the database to its state before the load, if you need to. A DB snapshot taken
immediately after the load protects you from having to load the data again in case of a
mishap. You can also use DB snapshots after the load to import data into new database
instances.

The following example runs the AWS CLI [create-db-snapshot](../../../cli/latest/reference/rds/create-db-snapshot.md "../../../cli/latest/reference/rds/create-db-snapshot.md")
command to create a DB snapshot of the `AcmeRDS` instance and give the DB
snapshot the identifier `"preload"`.

For Linux, macOS, or Unix:

```
aws rds create-db-snapshot \
    --db-instance-identifier `AcmeRDS` \
    --db-snapshot-identifier `preload`
```

For Windows:

```
aws rds create-db-snapshot ^
    --db-instance-identifier `AcmeRDS` ^
    --db-snapshot-identifier `preload`
```

You can also use the restore from DB snapshot functionality to create test DB
instances for dry runs or to undo changes made during the load.

Keep in mind that restoring a database from a DB snapshot creates a new DB instance
that, like all DB instances, has a unique identifier and endpoint. To restore the DB
instance without changing the endpoint, first delete the DB instance so that you can
reuse the endpoint.

For example, to create a DB instance for dry runs or other testing, you give the DB
instance its own identifier. In the example, `AcmeRDS-2`" is the identifier.
The example connects to the DB instance using the endpoint associated with
`AcmeRDS-2`. For more information, see [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md").

For Linux, macOS, or Unix:

```
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier `AcmeRDS-2` \
    --db-snapshot-identifier `preload`
```

For Windows:

```
aws rds restore-db-instance-from-db-snapshot ^
    --db-instance-identifier `AcmeRDS-2` ^
    --db-snapshot-identifier `preload`
```

To reuse the existing endpoint, first delete the DB instance and then give the
restored database the same identifier. For more information, see [delete-db-instance](../../../cli/latest/reference/rds/delete-db-instance.md "../../../cli/latest/reference/rds/delete-db-instance.md").

The following example also takes a final DB snapshot of the DB instance before
deleting it. This is optional but recommended.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance \
    --db-instance-identifier `AcmeRDS` \
    --final-db-snapshot-identifier `AcmeRDS-Final`

aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier `AcmeRDS` \
    --db-snapshot-identifier `preload`
```

For Windows:

```
aws rds delete-db-instance ^
    --db-instance-identifier `AcmeRDS` ^
    --final-db-snapshot-identifier `AcmeRDS-Final`

aws rds restore-db-instance-from-db-snapshot ^
    --db-instance-identifier `AcmeRDS` ^
    --db-snapshot-identifier `preload`
```

## Step 4

(Optional): Turn off Amazon RDS automated backups

###### Warning

Don't turn off automated backups if you need to perform point-in-time
recovery.

Turning off automated backups is a performance optimization and isn't required for
data loads. Turning off automated backups erases all existing backups. As a result,
after you turn off automated backups, point-in-time recovery isn't possible. Manual DB
snapshots aren't affected by turning off automated backups. All existing manual DB
snapshots are still available for restore.

Turning off automated backups reduces load time by about 25 percent and reduces the
amount of storage space required during the load. If you plan to load data into a new DB
instance that contains no data, turning off backups is an easy way to speed up the load
and avoid using the additional storage needed for backups. However, in some cases you
might plan to load into a DB instance that already contains data. If so, weigh the
benefits of turning off backups against the impact of losing the ability to perform
point-in-time-recovery.

DB instances have automated backups turned on by default (with a one day retention
period). To turn off automated backups, set the backup retention period to zero. After
the load, you can turn backups back on by setting the backup retention period to a
nonzero value. To turn on or turn off backups, Amazon RDS shuts the DB instance down and then
restarts it to turn MySQL logging on or off.

Run the AWS CLI `modify-db-instance` command to set the backup retention to
zero and apply the change immediately. Setting the retention period to zero requires a
DB instance restart, so wait until the restart has completed before proceeding. For more
information, see [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md").

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `AcmeRDS` \
    --apply-immediately \
    --backup-retention-period `0`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `AcmeRDS` ^
    --apply-immediately ^
    --backup-retention-period `0`
```

You can check the status of your DB instance with the AWS CLI [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command. The following example displays the DB
instance status of the `AcmeRDS` DB instance:

```
aws rds describe-db-instances --db-instance-identifier `AcmeRDS` --query "*[].{DBInstanceStatus:DBInstanceStatus}"
```

When the DB instance status is `available`, you're ready to proceed to
the next step.

## Step 5: Load the

data

To read rows from your flat files into the database tables, use the MySQL `LOAD
 DATA LOCAL INFILE` statement.

###### Note

You must invoke the `mysql` shell from the same location where your
flat files exist, or use the absolute path for the files when you run `LOAD
 DATA LOCAL INFILE`.

The following example shows how to load data from a file named `sales.txt`
into a table named `Sales` in the database:

```
mysql> LOAD DATA LOCAL INFILE 'sales.txt' INTO TABLE Sales FIELDS TERMINATED BY ' ' ENCLOSED BY '' ESCAPED BY '\\';
Query OK, 1 row affected (0.01 sec)
Records: 1  Deleted: 0  Skipped: 0  Warnings: 0
```

For more information about the `LOAD DATA` statement, see [LOAD DATA
Statement](https://dev.mysql.com/doc/refman/8.4/en/load-data.html "https://dev.mysql.com/doc/refman/8.4/en/load-data.html") in the MySQL documentation.

## Step 6: Turn

back on Amazon RDS automated backups

If you turned off Amazon RDS automated backups in [Step 4](#mysql-importing-data-any-source-turn-off-automated-backups "#mysql-importing-data-any-source-turn-off-automated-backups"),
after the load is finished, turn automated backups on by setting the backup retention
period back to its preload value. As noted in Step 4, Amazon RDS restarts the DB instance, so
be prepared for a brief outage.

The following example runs the AWS CLI [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
command to turn on automated backups for the `AcmeRDS` DB instance and set
the retention period to one day:

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `AcmeRDS` \
    --backup-retention-period `1` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `AcmeRDS` ^
    --backup-retention-period `1` ^
    --apply-immediately
```
