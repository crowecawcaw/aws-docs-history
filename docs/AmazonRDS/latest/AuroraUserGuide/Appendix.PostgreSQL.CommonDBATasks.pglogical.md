# Setting up

logical replication for Aurora PostgreSQL DB cluster

The following procedure shows you how to start logical replication between two Aurora PostgreSQL DB clusters. The steps assume that both the source (publisher) and
the target (subscriber) have the `pglogical` extension set up as detailed in [Setting up the
pglogical extension](Appendix.PostgreSQL.CommonDBATasks.pglogical.md "Appendix.PostgreSQL.CommonDBATasks.pglogical.md").

###### Note

The `node_name` of a subscriber node can't start with `rds`.

###### To create the publisher node and define the tables to replicate

These steps assume that your Aurora PostgreSQL DB cluster has a
writer instance with a database that has one or more tables that you want to replicate to
another node. You need to recreate the table structure from the publisher on the subscriber,
so first, get the table structure if necessary. You can do that by using the
`psql` metacommand `\d `tablename`` and
then creating the same table on the subscriber instance. The following procedure creates an
example table on the publisher (source) for demonstration purposes.

1. Use `psql` to connect to the instance that has the table you want to use as
   a source for subscribers.

```
psql --host=`source-instance`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password --dbname=`labdb`

```

If you don't have an existing table that you want to replicate, you can create a
sample table as follows.

    1. Create an example table using the following SQL statement.



    ```
    CREATE TABLE docs_lab_table (a int PRIMARY KEY);
    ```
    2. Populate the table with generated data by using the following SQL
     statement.



    ```
    INSERT INTO docs_lab_table VALUES (generate_series(1,5000));
    `INSERT 0 5000`
    ```
    3. Verify that data exists in the table by using the following SQL statement.



    ```
    SELECT count(*) FROM docs_lab_table;
    ```

2. Identify this Aurora PostgreSQL DB cluster as the publisher node, as
   follows.

```
SELECT pglogical.create_node(
    node_name := '`docs_lab_provider`',
    dsn := 'host=`source-instance`.`aws-region`.rds.amazonaws.com port=5432 dbname=`labdb`');
 `create_node
-------------
 3410995529
(1 row)`
```

3. Add the table that you want to replicate to the default replication set. For more
   information about replication sets, see [Replication sets](https://github.com/2ndQuadrant/pglogical/tree/REL2_x_STABLE/docs#replication-sets "https://github.com/2ndQuadrant/pglogical/tree/REL2_x_STABLE/docs#replication-sets") in the pglogical documentation.

```
SELECT pglogical.replication_set_add_table('default', '`docs_lab_table`', 'true', NULL, NULL);
 `replication_set_add_table
 ---------------------------
 t
 (1 row)`
```

The publisher node setup is complete. You can now set up the subscriber node to receive
the updates from the publisher.

###### To set up the subscriber node and create a subscription to receive updates

These steps assume that the Aurora PostgreSQL DB cluster
has been set up with the
`pglogical` extension. For more information, see [Setting up the
pglogical extension](Appendix.PostgreSQL.CommonDBATasks.pglogical.md "Appendix.PostgreSQL.CommonDBATasks.pglogical.md").

1. Use `psql` to connect to the instance that you want to receive updates from
   the publisher.

```
psql --host=`target-instance`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password --dbname=`labdb`

```

2. On the subscriber Aurora PostgreSQL DB cluster,
   ,create the same table
   that exists on the publisher. For this example, the table is `docs_lab_table`.
   You can create the table as follows.

```
CREATE TABLE docs_lab_table (a int PRIMARY KEY);
```

3. Verify that this table is empty.

```
SELECT count(*) FROM docs_lab_table;
 `count
-------
 0
(1 row)`
```

4. Identify this Aurora PostgreSQL DB cluster as the subscriber node, as
   follows.

```
SELECT pglogical.create_node(
    node_name := '`docs_lab_target`',
    dsn := 'host=`target-instance`.`aws-region`.rds.amazonaws.com port=5432 sslmode=require dbname=`labdb` user=`postgres` password=`********`');
 `create_node
-------------
 2182738256
(1 row)`
```

5. Create the subscription.

```
SELECT pglogical.create_subscription(
   subscription_name := 'docs_lab_subscription',
   provider_dsn := 'host=`source-instance`.`aws-region`.rds.amazonaws.com port=5432 sslmode=require dbname=`labdb` user=`postgres` password=`*******`',
   replication_sets := ARRAY['default'],
   synchronize_data := true,
   forward_origins := '{}' );
 `create_subscription
---------------------
1038357190
(1 row)`
```

When you complete this step, the data from the table on the publisher is created in
the table on the subscriber. You can verify that this has occurred by using the following
SQL query.

```
SELECT count(*) FROM docs_lab_table;
 `count
-------
 5000
(1 row)`
```

From this point forward, changes made to the table on the publisher are replicated to the
table on the subscriber.
