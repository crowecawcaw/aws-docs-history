# Performing

logical replication for Amazon RDS for PostgreSQL

Starting with version 10.4, RDS for PostgreSQL supports the publication and subscription SQL
syntax that was introduced in PostgreSQL 10. To learn more, see [Logical
replication](https://www.postgresql.org/docs/current/logical-replication.html "https://www.postgresql.org/docs/current/logical-replication.html") in the PostgreSQL documentation.

###### Note

In addition to the native PostgreSQL logical replication feature introduced in
PostgreSQL 10, RDS for PostgreSQL also supports the `pglogical` extension. For
more information, see [Using pglogical to synchronize
data across instances](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

Following, you can find information about setting up logical replication for an
RDS for PostgreSQL DB instance.

###### Topics

- [Understanding logical replication and logical decoding](#PostgreSQL.Concepts.General.FeatureSupport.LogicalDecoding "#PostgreSQL.Concepts.General.FeatureSupport.LogicalDecoding")
- [Working with logical replication slots](#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplicationSlots "#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplicationSlots")
- [Replicating table level
  data using logical replication](#PostgreSQL.Concepts.LogicalReplication.Tables "#PostgreSQL.Concepts.LogicalReplication.Tables")

## Understanding logical replication and logical decoding

RDS for PostgreSQL supports the streaming of write-ahead log (WAL) changes using
PostgreSQL's logical replication slots. It also supports using logical decoding.
You can set up logical replication slots on your instance and stream database changes
through these slots to a client such as `pg_recvlogical`. You create logical
replication slots at the database level, and they support replication connections to a
single database.

The most common clients for PostgreSQL logical replication are AWS Database Migration Service or a
custom-managed host on an Amazon EC2 instance. The logical replication slot has no
information about the receiver of the stream. Also, there's no requirement that the
target be a replica database. If you set up a logical replication slot and don't
read from the slot, data can be written and quickly fill up your DB instance's
storage.

You turn on PostgreSQL logical replication and logical decoding for Amazon RDS with a
parameter, a replication connection type, and a security role. The client for logical
decoding can be any client that can establish a replication connection to a database on
a PostgreSQL DB instance.

###### To turn on logical decoding for an RDS for PostgreSQL DB instance

1. Make sure that the user account that you're using has these roles:
   - The `rds_superuser` role so you can turn on logical
     replication
   - The `rds_replication` role to grant permissions to manage
     logical slots and to stream data using logical slots

2. Set the `rds.logical_replication` static parameter to 1. As part of
   applying this parameter, also set the parameters `wal_level`,
   `max_wal_senders`, `max_replication_slots`, and
   `max_connections`. These parameter changes can increase WAL
   generation, so set the `rds.logical_replication` parameter only when
   you are using logical slots.
3. Reboot the DB instance for the static `rds.logical_replication`
   parameter to take effect.
4. Create a logical replication slot as explained in the next section. This
   process requires that you specify a decoding plugin. Currently, RDS for PostgreSQL
   supports the test_decoding and wal2json output plugins that ship with
   PostgreSQL.

For more information on PostgreSQL logical decoding, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/static/logicaldecoding-explanation.html "https://www.postgresql.org/docs/current/static/logicaldecoding-explanation.html").

## Working with logical replication slots

You can use SQL commands to work with logical slots. For example, the following
command creates a logical slot named `test_slot` using the default PostgreSQL
output plugin `test_decoding`.

```
`SELECT * FROM pg_create_logical_replication_slot('test_slot', 'test_decoding');`
`slot_name | xlog_position
-----------------+---------------
regression_slot | 0/16B1970
(1 row)`
```

To list logical slots, use the following command.

```
SELECT * FROM pg_replication_slots;
```

To drop a logical slot, use the following command.

```
`SELECT pg_drop_replication_slot('test_slot');`
`pg_drop_replication_slot
-----------------------
(1 row)`
```

For more examples on working with logical replication slots, see [Logical decoding examples](https://www.postgresql.org/docs/9.5/static/logicaldecoding-example.html "https://www.postgresql.org/docs/9.5/static/logicaldecoding-example.html") in the PostgreSQL documentation.

After you create the logical replication slot, you can start streaming. The following
example shows how logical decoding is controlled over the streaming replication
protocol. This example uses the program pg_recvlogical, which is included in the
PostgreSQL distribution. Doing this requires that client authentication is set up to
allow replication connections.

```
pg_recvlogical -d postgres --slot test_slot -U postgres
    --host -`instance-name.111122223333`.`aws-region`.rds.amazonaws.com
    -f -  --start
```

To see the contents of the `pg_replication_origin_status` view, query the
`pg_show_replication_origin_status` function.

```
`SELECT * FROM pg_show_replication_origin_status();`
`local_id | external_id | remote_lsn | local_lsn
----------+-------------+------------+-----------
(0 rows)`
```

## Replicating table level

data using logical replication

You can use logical replication to replicate data from source tables to target tables
in RDS for PostgreSQL. Logical replication first performs an initial load of existing data
from the source tables and then continues to replicate ongoing changes.

1. ###### Create the source tables

Connect to the source database in your RDS for PostgreSQL DB instance:

```

source=> CREATE TABLE testtab (slno int primary key);
CREATE TABLE

```

2. ###### Insert data into the source tables

```

source=> INSERT INTO testtab VALUES (generate_series(1,1000));
INSERT 0 1000

```

3. ###### Create a publication for source tables
   - Create a publication for the source tables:

   ```

   source=> CREATE PUBLICATION testpub FOR TABLE testtab;
   CREATE PUBLICATION

   ```

   - Use a SELECT query to verify the details of the publication that was
     created:

   ```

   source=> SELECT * FROM pg_publication;
     oid   | pubname | pubowner | puballtables | pubinsert | pubupdate | pubdelete | pubtruncate | pubviaroot
   --------+---------+----------+--------------+-----------+-----------+-----------+-------------+------------
    115069 | testpub |    16395 | f            | t         | t         | t         | t           | f
   (1 row)

   ```

   - Verify that the source tables are added to the publication:

   ```

   source=> SELECT * FROM pg_publication_tables;
   pubname | schemaname | tablename
   ---------+------------+-----------
    testpub | public     | testtab
   (1 rows)

   ```

   - To replicate all tables in a database, use:

   ```

   CREATE PUBLICATION testpub FOR ALL TABLES;

   ```

   - If the publication is already created for individual table and you
     need to add new table, you can run below query to add any new tables
     into the existing publication:

   ```

   ALTER PUBLICATION <publication_name> add table <new_table_name>;

   ```

4. ###### Connect to target database and create target tables
   - Connect to the target database in the target DB instance. Create the target
     tables with the same names as the source tables:

   ```

   target=> CREATE TABLE testtab (slno int primary key);
   CREATE TABLE

   ```

   - Make sure that there's no data present in the target tables by running
     a SELECT query on the target tables:

   ```

   target=> SELECT count(*) FROM testtab;
    count
   -------
        0
   (1 row)

   ```

5. ###### Create and verify subscription in target database
   - Create the subscription in the target database:

   ```

   target=> CREATE SUBSCRIPTION testsub
   CONNECTION 'host=<source RDS/host endpoint> port=5432 dbname=<source_db_name> user=<user> password=<password>'
   PUBLICATION testpub;
   NOTICE:  Created replication slot "testsub" on publisher
   CREATE SUBSCRIPTION

   ```

   - Use a SELECT query to verify that the subscription is enabled:

   ```

   target=> SELECT oid, subname, subenabled, subslotname, subpublications FROM pg_subscription;
     oid  | subname | subenabled | subslotname | subpublications
   -------+---------+------------+-------------+-----------------
    16434 | testsub | t          | testsub     | {testpub}
   (1 row)

   ```

   - When the subscription is created, it loads all data from the source
     tables to the target tables. Run a SELECT query on the target tables to
     verify that the initial data loads:

   ```

   target=> SELECT count(*) FROM testtab;
    count
   -------
     1000
   (1 row)

   ```

6. ###### Verify replication slot in source database

The creation of a subscription in the target database creates a replication
slot in the source database. Verify the replication slot details by running the
following SELECT query on the source database:

```

source=> SELECT * FROM pg_replication_slots;

slot_name |  plugin  | slot_type | datoid | database | temporary | active | active_pid | xmin | catalog_xmin | restart_lsn | confirmed_flush_lsn | wal_status | safe_wal_size
----------+----------+-----------+--------+----------+-----------+--------+------------+------+--------------+-------------+---------------------+------------+---------------
testsub   | pgoutput | logical   | 115048 | source   | f         | t      |        846 |      |         6945 | 58/B4000568 | 58/B40005A0         | reserved   |
(1 row)

```

7. ###### Testing replication
   - Test whether data changes in the source tables are being replicated to
     the target tables by inserting rows into the source tables:

   ```

   source=> INSERT INTO testtab VALUES(generate_series(1001,2000));
   INSERT 0 1000

   source=> SELECT count(*) FROM testtab;
    count
   -------
     2000
   (1 row)

   ```

   - Verify the number of rows in the target tables to confirm that new
     inserts are being replicated:

   ```

   target=> SELECT count(*) FROM testtab;
    count
   -------
     2000
   (1 row)

   ```

8. ###### Refreshing the subscription after adding tables
   - When you add new tables to an existing publication, it is mandatory to
     refresh the subscription for the changes to take effect:

   ```

   ALTER SUBSCRIPTION <subscription_name> REFRESH PUBLICATION;

   ```

   - This command fetches missing table information from the publisher and
     starts replication for tables that were added to the subscribed-to
     publications since the subscription was created or last
     refreshed.
