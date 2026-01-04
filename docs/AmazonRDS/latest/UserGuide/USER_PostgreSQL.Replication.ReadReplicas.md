# Logical

decoding on a read replica

RDS for PostgreSQL supports logical replication from standbys with PostgreSQL 16.1. This
allows you to create logical decoding from a read-only standby that reduces the load on
the primary DB instance. You can achieve higher-availability for your applications that need
to synchronize data across multiple systems. This feature boosts the performance of your
data warehouse and data analytics.

Also, replication slots on a given standby persist the promotion of that standby to a
primary. This means that in the event of a primary DB instance failover or the promotion of a
standby to be the new primary, the replication slots will persist and the former standby
subscribers will not be affected.

###### To create logical decoding on a read replica

1. Turn on logical replication – To create
   logical decoding on a standby, you must turn on logical replication on your
   source DB instance and its physical replica. For more information, see [Read replica
   configuration with PostgreSQL](USER_PostgreSQL.Replication.ReadReplicas.md "USER_PostgreSQL.Replication.ReadReplicas.md").
   - To turn on logical replication for a newly
     created RDS for PostgreSQL DB instance – Create a new DB custom
     parameter group and set the static parameter
     `rds.logical_replication` to `1`. Then,
     associate this DB parameter group with the Source DB instance and its physical
     read replica. For more information, see [Associating a DB parameter group with a
     DB instance in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
   - To turn on logical replication for an existing
     RDS for PostgreSQL DB instance – Modify the DB custom parameter
     group of the source DB instance and its physical read replica to set the
     static parameter `rds.logical_replication` to `1`.
     For more information, see [Modifying parameters in a DB parameter group
     in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### Note

You must reboot the DB instance to apply these parameter changes.

You can use the following query to verify the values for
`wal_level` and `rds.logical_replication` on the
source DB instance and its physical read replica.

```
`Postgres=>``SELECT name,setting FROM pg_settings WHERE name IN ('wal_level','rds.logical_replication');`
            `name | setting
-------------------------+---------
 rds.logical_replication | on
 wal_level | logical
(2 rows)`
```

2. Create a table in the source database –
   Connect to the database in your source DB instance. For more information, see [Connecting to a DB instance running the
   PostgreSQL database engine](USER_ConnectToPostgreSQLInstance.md "USER_ConnectToPostgreSQLInstance.md").

Use the following queries to create table in your source database and to
insert values:

```
`Postgres=>`CREATE TABLE LR_test (a int PRIMARY KEY);
`CREATE TABLE`
```

```
`Postgres=>``INSERT INTO LR_test VALUES (generate_series(1,10000));`
`INSERT 0 10000`
```

3. Create a publication for the source table
   – Use the following query to create a publication for the table on the
   source DB instance.

```
`Postgres=>`CREATE PUBLICATION testpub FOR TABLE LR_test;
`CREATE PUBLICATION`
```

Use a SELECT query to verify the details of the publication that was created
on both the source DB instance and the physical read replica instance.

```
`Postgres=>`SELECT * from pg_publication;
             `oid | pubname | pubowner | puballtables | pubinsert | pubupdate | pubdelete | pubtruncate | pubviaroot
-------+---------+----------+--------------+-----------+-----------+-----------+-------------+------------
 16429 | testpub | 16413 | f | t | t | t | t | f
(1 row)`
```

4. Create a subscription from logical replica
   instance – Create another RDS for PostgreSQL DB instance as the logical
   replica instance. Make sure that VPC is setup correctly to ensure that this
   logical replica instance can access the physical read replica instance. For more
   information, see [Amazon VPC and Amazon RDS](USER_VPC.md "USER_VPC.md"). If your
   source DB instance is idle, connectivity issues might occur and the primary
   doesn't send the data to standby.

```
`Postgres=>``CREATE SUBSCRIPTION testsub CONNECTION 'host=`Physical replica host name` port=`port`
 dbname=`source_db_name` user=`user` password=`password`' PUBLICATION `testpub;``
`NOTICE: created replication slot "testsub" on publisher
CREATE SUBSCRIPTION`
```

```
`Postgres=>`CREATE TABLE LR_test (a int PRIMARY KEY);
`CREATE TABLE`
```

Use a SELECT query to verify the details of the subscription on the logical
replica instance.

```
`Postgres=>``SELECT oid,subname,subenabled,subslotname,subpublications FROM pg_subscription;`
            `oid | subname | subenabled | subslotname | subpublications
-------+---------+------------+-------------+-----------------
 16429 | testsub | t | testsub | {testpub}
(1 row)
postgres=> select count(*) from LR_test;
 count
-------
 10000
(1 row)`

```

5. Inspect logical replication slot state –
   You can only see the physical replication slot on your source DB instance.

```
`Postgres=>``select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;`
            `slot_name | slot_type | confirmed_flush_lsn
---------------------------------------------+-----------+---------------------
 rds_us_west_2_db_dhqfsmo5wbbjqrn3m6b6ivdhu4 | physical |
(1 row)`
```

However, on your read replica instance, you can see the logical replication
slot and the `confirmed_flush_lsn` value changes as the application
actively consumes logical changes.

```
`Postgres=>``select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;`
            `slot_name | slot_type | confirmed_flush_lsn
-----------+-----------+---------------------
 testsub | logical | 0/500002F0
(1 row)`
```

```
`Postgres=>``select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;`
            `slot_name | slot_type | confirmed_flush_lsn
-----------+-----------+---------------------
 testsub | logical | 0/5413F5C0
(1 row)`
```
