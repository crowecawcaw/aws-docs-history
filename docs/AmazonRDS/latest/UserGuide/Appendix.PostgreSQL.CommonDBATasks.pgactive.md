# Setting up

active-active replication for RDS for PostgreSQL DB instances

The following procedure shows you how to start active-active replication between two
RDS for PostgreSQL DB instances where `pgactive` is available. To run the
multi-region high availability example, you need to deploy Amazon RDS for PostgreSQL instances
in two different regions and set up VPC Peering. For more information, see [VPC
peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md").

###### Note

Sending traffic between multiple regions may incur additional costs.

These steps assume that the RDS for PostgreSQL DB instance has been enabled with the
`pgactive` extension. For more information, see [Initializing the
pgactive extension capability](Appendix.PostgreSQL.CommonDBATasks.pgactive.md "Appendix.PostgreSQL.CommonDBATasks.pgactive.md").

###### To configure the first RDS for PostgreSQL DB instance with the `pgactive`

extension

The following example illustrates how the `pgactive` group is created, along
with other steps required to create the `pgactive` extension on the RDS for PostgreSQL
DB instance.

1. Use `psql` or another client tool to connect to your first RDS for PostgreSQL
   DB instance.

```
psql --host=`firstinstance.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password=`PASSWORD` --dbname=`postgres`

```

2. Create a database on the RDS for PostgreSQL instance using the following command:

```
`postgres=>` CREATE DATABASE `app`;
```

3. Switch connection to the new database using the following command:

```
\c `app`
```

4. Create and populate a sample table using the following SQL statements:
   1. Create an example table using the following SQL statement.

   ```
   `app=>` CREATE SCHEMA inventory;
   CREATE TABLE inventory.products (
   id int PRIMARY KEY, product_name text NOT NULL,
   created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP);
   ```

   2. Populate the table with some sample data by using the following SQL
      statement.

   ```
   `app=>` INSERT INTO inventory.products (id, product_name)
   VALUES (1, 'soap'), (2, 'shampoo'), (3, 'conditioner');

   ```

   3. Verify that data exists in the table by using the following SQL statement.

   ```
    `app=>`SELECT count(*) FROM inventory.products;
   `count
   -------
    3`
   ```

5. Create `pgactive` extension on the existing database.

```
`app=>` CREATE EXTENSION pgactive;
```

6. To securely create and initialize the pgactive group use the following
   commands:

```
`app=>`
-- connection info for endpoint1
CREATE SERVER pgactive_server_endpoint1
    FOREIGN DATA WRAPPER pgactive_fdw
    OPTIONS (host '<endpoint1>', dbname 'app');
CREATE USER MAPPING FOR postgres
    SERVER pgactive_server_endpoint1
    OPTIONS (user 'postgres', password '<password>');
      -- connection info for endpoint2
CREATE SERVER pgactive_server_endpoint2
    FOREIGN DATA WRAPPER pgactive_fdw
    OPTIONS (host '<endpoint2>', dbname 'app');
CREATE USER MAPPING FOR postgres
    SERVER pgactive_server_endpoint2
    OPTIONS (user 'postgres', password '<password>');

```

Now you can initialize the replication group and add this first instance:

```

SELECT pgactive.pgactive_create_group(
    node_name := `'endpoint1-app'`,
    node_dsn := 'user_mapping=postgres pgactive_foreign_server=pgactive_server_endpoint1'

);

```

Use the following commands as an alternate but less secure method to create and
initialize the pgactive group:

```
`app=>` SELECT pgactive.pgactive_create_group(
    node_name := `'node1-app'`,
    node_dsn := 'dbname=`app` host=`firstinstance.111122223333`.`aws-region`.rds.amazonaws.com user=`postgres` password=`PASSWORD`');
```

node1-app is the name that you assign to uniquely identify a node in the
`pgactive` group.

###### Note

To perform this step successfully on a DB instance that is publicly accessible, you must
turn on the `rds.custom_dns_resolution` parameter by setting it to
`1`. 7. To check if the DB instance is ready, use the following command:

```
`app=>` SELECT pgactive.pgactive_wait_for_node_ready();
```

If the command succeeds, you can see the following output:

```

`pgactive_wait_for_node_ready
------------------------------
(1 row)`
```

###### To configure the second RDS for PostgreSQL instance and join it to the `pgactive`

group

The following example illustrates how you can join an RDS for PostgreSQL DB instance to the
`pgactive` group, along with other steps that are required to create the
`pgactive` extension on the DB instance.

These steps assume that another
RDS for PostgreSQL DB instances has been set up with the
`pgactive` extension. For more information, see [Initializing the
pgactive extension capability](Appendix.PostgreSQL.CommonDBATasks.pgactive.md "Appendix.PostgreSQL.CommonDBATasks.pgactive.md").

1. Use `psql` to connect to the instance that you want to receive updates from
   the publisher.

```
psql --host=`secondinstance.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password=`PASSWORD` --dbname=`postgres`

```

2. Create a database on the second RDS for PostgreSQL DB instance using the following
   command:

```
`postgres=>` CREATE DATABASE `app`;
```

3. Switch connection to the new database using the following command:

```
\c `app`
```

4. Create the `pgactive` extension on the existing database.

```
`app=>` CREATE EXTENSION pgactive;
```

5. Join the RDS for PostgreSQL second DB instance to the
   `pgactive` group in a more secure way using the following commands:

```

-- connection info for endpoint1
CREATE SERVER pgactive_server_endpoint1
    FOREIGN DATA WRAPPER pgactive_fdw
    OPTIONS (host '<endpoint1>', dbname 'app');
CREATE USER MAPPING FOR postgres
    SERVER pgactive_server_endpoint1
    OPTIONS (user 'postgres', password '<password>');

-- connection info for endpoint2
CREATE SERVER pgactive_server_endpoint2
    FOREIGN DATA WRAPPER pgactive_fdw
    OPTIONS (host '<endpoint2>', dbname 'app');
CREATE USER MAPPING FOR postgres
    SERVER pgactive_server_endpoint2
    OPTIONS (user 'postgres', password '<password>');

```

```

SELECT pgactive.pgactive_join_group(
    node_name := 'endpoint2-app',
    node_dsn := 'user_mapping=postgres pgactive_foreign_server=pgactive_server_endpoint2',
    join_using_dsn := 'user_mapping=postgres pgactive_foreign_server=pgactive_server_endpoint1'
);

```

Use the following commands as an alternate but less secure method to join the RDS for PostgreSQL second DB instance to the `pgactive` group

```
`app=>` SELECT pgactive.pgactive_join_group(
node_name := `'node2-app'`,
node_dsn := 'dbname=`app` host=`secondinstance.111122223333`.`aws-region`.rds.amazonaws.com user=`postgres` password=`PASSWORD`',
join_using_dsn := 'dbname=`app` host=`firstinstance.111122223333`.`aws-region`.rds.amazonaws.com user=`postgres` password=`PASSWORD`');
```

node2-app is the name that you assign to uniquely identify a node in the
`pgactive` group. 6. To check if the DB instance is ready, use the following command:

```
`app=>` SELECT pgactive.pgactive_wait_for_node_ready();
```

If the command succeeds, you can see the following output:

```

`pgactive_wait_for_node_ready
------------------------------
(1 row)`
```

If the first RDS for PostgreSQL database is relatively large, you can see
`pgactive.pgactive_wait_for_node_ready()` emitting the progress report of the
restore operation. The output looks similar to the following:

```
`NOTICE: restoring database 'app', 6% of 7483 MB complete
NOTICE: restoring database 'app', 42% of 7483 MB complete
NOTICE: restoring database 'app', 77% of 7483 MB complete
NOTICE: restoring database 'app', 98% of 7483 MB complete
NOTICE: successfully restored database 'app' from node node1-app in 00:04:12.274956
 pgactive_wait_for_node_ready
------------------------------
(1 row)`
```

From this point forward, `pgactive` synchronizes the data between the two
DB instances. 7. You can use the following command to verify if the database of the second DB instance has
the data:

```
`app=>` SELECT count(*) FROM inventory.products;
```

If the data is successfully synchronized, you’ll see the following output:

```
`count
-------
 3`
```

8. Run the following command to insert new values:

```
`app=>` INSERT INTO inventory.products (id, product_name) VALUES (4, 'lotion');
```

9. Connect to the database of the first DB instance and run the following query:

```
`app=>` SELECT count(*) FROM inventory.products;
```

If the active-active replication is initialized, the output is similar to the
following:

```
`count
-------
 4`
```

###### To detach and remove a DB instance from the `pgactive` group

You can detach and remove a DB instance from the `pgactive` group using these
steps:

1. You can detach the second DB instance from the first DB instance using the following
   command:

```
`app=>` SELECT * FROM pgactive.pgactive_detach_nodes(ARRAY[‘`node2-app`']);
```

2. Remove the `pgactive` extension from the second DB instance using the following
   command:

```
`app=>` SELECT * FROM pgactive.pgactive_remove();
```

To forcefully remove the extension:

```
`app=>` SELECT * FROM pgactive.pgactive_remove(true);
```

3. Drop the extension using the following command:

```
`app=>` DROP EXTENSION pgactive;
```
