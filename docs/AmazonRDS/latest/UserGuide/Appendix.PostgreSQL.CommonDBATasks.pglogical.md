# Reestablishing logical replication after a major upgrade

Before you can perform a major version upgrade of an
RDS for PostgreSQL DB instance that's set up as a
publisher node for logical replication, you must drop all replication slots, even those that
aren't active. We recommend that you temporarily divert database transactions from the
publisher node, drop the replication slots,
upgrade the RDS for PostgreSQL DB instance, and then
re-establish and restart replication.

The replication slots are hosted on the publisher node only.
The RDS for PostgreSQL subscriber node in a logical replication
scenario has no slots to drops, but it can't be upgraded to a major version while
it's designated as a subscriber node with a subscription to the publisher. Before
upgrading the RDS for PostgreSQL subscriber node, drop the subscription and the node. For more
information, see [Managing logical replication slots for RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.pglogical.md "Appendix.PostgreSQL.CommonDBATasks.pglogical.md").

## Determining that logical replication has been disrupted

You can determine that the replication process has been disrupted by querying either the
publisher node or the subscriber node, as follows.

###### To check the publisher node

- Use `psql` to connect to the publisher node, and then query the
  `pg_replication_slots` function. Note the value in the active column.
  Normally, this will return `t` (true), showing that replication is active. If
  the query returns `f` (false), it's an indication that replication to
  the subscriber has stopped.

```
SELECT slot_name,plugin,slot_type,active FROM pg_replication_slots;
 `slot_name | plugin | slot_type | active
-------------------------------------------+------------------+-----------+--------
 pgl_labdb_docs_labcb4fa94_docs_lab3de412c | pglogical_output | logical | f
(1 row)`
```

###### To check the subscriber node

On the subscriber node, you can check the status of replication in three different
ways.

- Look through the PostgreSQL logs on the subscriber node to find failure messages.
  The log identifies failure with messages that include exit code 1, as shown
  following.

```
2022-07-06 16:17:03 UTC::@:[7361]:LOG: background worker "pglogical apply 16404:2880255011" (PID 14610) exited with exit code 1
2022-07-06 16:19:44 UTC::@:[7361]:LOG: background worker "pglogical apply 16404:2880255011" (PID 21783) exited with exit code 1
```

- Query the `pg_replication_origin` function. Connect to the database on
  the subscriber node using `psql` and query the
  `pg_replication_origin` function, as follows.

```
SELECT * FROM pg_replication_origin;
 `roident | roname
---------+--------
(0 rows)`
```

The empty result set means that replication has been disrupted. Normally, you see
output such as the following.

```
   roident |                       roname
  ---------+----------------------------------------------------
         1 | pgl_labdb_docs_labcb4fa94_docs_lab3de412c
  (1 row)
```

- Query the `pglogical.show_subscription_status` function as shown in the
  following example.

```
SELECT subscription_name,status,slot_name FROM pglogical.show_subscription_status();
 `subscription_name | status | slot_name
---====----------------+--------+-------------------------------------
 docs_lab_subscription | down | pgl_labdb_docs_labcb4fa94_docs_lab3de412c
(1 row)`
```

This output shows that replication has been disrupted. Its status is
`down`. Normally, the output shows the status as
`replicating`.

If your logical replication process has been disrupted, you can re-establish replication
by following these steps.

###### To reestablish logical replication between publisher and subscriber nodes

To re-establish replication, you first disconnect the subscriber from the publisher
node and then re-establish the subscription, as outlined in these steps.

1. Connect to the subscriber node using `psql` as follows.

```
psql --host=`222222222222`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password --dbname=`labdb`
```

2. Deactivate the subscription by using the
   `pglogical.alter_subscription_disable` function.

```
SELECT pglogical.alter_subscription_disable('docs_lab_subscription',true);
 `alter_subscription_disable
----------------------------
 t
(1 row)`
```

3. Get the publisher node's identifier by querying the
   `pg_replication_origin`, as follows.

```
SELECT * FROM pg_replication_origin;
 `roident | roname
---------+-------------------------------------
 1 | pgl_labdb_docs_labcb4fa94_docs_lab3de412c
(1 row)`
```

4. Use the response from the previous step with the
   `pg_replication_origin_create` command to assign the identifier that can be
   used by the subscription when re-established.

```
SELECT pg_replication_origin_create('pgl_labdb_docs_labcb4fa94_docs_lab3de412c');
 `pg_replication_origin_create
------------------------------
 1
(1 row)`
```

5. Turn on the subscription by passing its name with a status of `true`, as
   shown in the following example.

```
SELECT pglogical.alter_subscription_enable('docs_lab_subscription',true);
 `alter_subscription_enable
---------------------------
 t
(1 row)`
```

Check the status of the node. Its status should be `replicating` as shown in
this example.

```
SELECT subscription_name,status,slot_name
  FROM pglogical.show_subscription_status();
 `subscription_name | status | slot_name
-------------------------------+-------------+-------------------------------------
 docs_lab_subscription | replicating | pgl_labdb_docs_lab98f517b_docs_lab3de412c
(1 row)`
```

Check the status of the subscriber's replication slot on the publisher node. The
slot's `active` column should return `t` (true), indicating that
replication has been re-established.

```
SELECT slot_name,plugin,slot_type,active
  FROM pg_replication_slots;
 `slot_name | plugin | slot_type | active
-------------------------------------------+------------------+-----------+--------
 pgl_labdb_docs_lab98f517b_docs_lab3de412c | pglogical_output | logical | t
(1 row)`
```
