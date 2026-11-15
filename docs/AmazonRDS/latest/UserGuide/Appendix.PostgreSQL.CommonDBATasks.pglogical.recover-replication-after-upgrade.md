

# Reestablishing logical replication after a major upgrade
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.recover-replication-after-upgrade"></a>

Whether a major version upgrade keeps your logical replication configuration depends on the PostgreSQL major version that you upgrade from.

**Source version earlier than 17** – The upgrade doesn't carry over the replication slots on the publisher node. Before you can perform a major version upgrade of an RDS for PostgreSQL DB instance that's set up as a publisher node for logical replication, you must drop all replication slots, even those that aren't active. The upgrade precheck stops the upgrade if any logical replication slot exists. Temporarily divert database transactions from the publisher node, drop the replication slots, upgrade the RDS for PostgreSQL DB instance, and then re-establish and restart replication.

**Source version 17 and later** – The upgrade can retain the logical replication slots on the publisher node, so you don't have to drop them. Before you start the upgrade, disable the subscriptions and make sure that each subscriber has consumed all changes from its slot. If a slot still holds unconsumed changes, the upgrade fails after the DB instance has been taken offline, and the DB instance returns to the source version. The parameter group for the target version must also set `rds.logical_replication` to `1`, so that `wal_level` stays `logical`. After the upgrade, enable the subscriptions again. For the full list of requirements, see [Upgrade](https://www.postgresql.org/docs/current/logical-replication-upgrade.html) on the PostgreSQL website.

Only the publisher node hosts replication slots. The RDS for PostgreSQL subscriber node has no slots to drop, and you can upgrade it independently of the publisher node. However, the upgrade changes the replication state on the subscriber node in the following ways.
+ **pglogical subscriptions** – For source versions earlier than 17, the upgrade precheck stops the upgrade while the database has pglogical nodes. Drop the subscription and the node before you upgrade, and re-create them afterward. For more information, see [Managing logical replication slots for RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.pglogical.handle-slots.md). For source version 17 and later, you can upgrade with the pglogical node and subscription in place. However, the upgrade doesn't preserve the replication origin that pglogical uses to track its position, regardless of the source version. After the upgrade, the subscription status is `down`. Use the following procedure to re-establish replication.
+ **Native subscriptions (`CREATE SUBSCRIPTION`)** – For source versions earlier than 17, the upgrade keeps the subscription but doesn't preserve its table list in `pg_subscription_rel` or its replication origin. If you enable the subscription after the upgrade, the apply worker starts and the slot on the publisher node shows as active, but no changes are applied to your tables and no error is logged. To register the tables again, run `ALTER SUBSCRIPTION ... REFRESH PUBLICATION`. Changes that the publisher node sent while the tables weren't registered are lost. To get a consistent copy, drop and re-create the subscription.

  For source version 17 and later, the upgrade preserves the table list and the replication origin. Disable the subscription before the upgrade and enable it afterward. Replication continues from where it stopped without copying the tables again.

The following procedure shows you how to determine that pglogical replication has been disrupted and how to resolve the issue.

## Determining that logical replication has been disrupted
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.recover-replication-after-upgrade.identifying-the-issue"></a>

You can determine that the replication process has been disrupted by querying either the publisher node or the subscriber node, as follows.

**To check the publisher node**
+ Use `psql` to connect to the publisher node, and then query the `pg_replication_slots` view. Note the value in the `active` column. Normally, this will return `t` (true), showing that replication is active. If the query returns `f` (false), it's an indication that replication to the subscriber has stopped. 

  ```
  SELECT slot_name,plugin,slot_type,active FROM pg_replication_slots;
                      slot_name              |      plugin      | slot_type | active
  -------------------------------------------+------------------+-----------+--------
   pgl_labdb_docs_labcb4fa94_docs_lab3de412c | pglogical_output | logical   | f
  (1 row)
  ```

**To check the subscriber node**

On the subscriber node, you can check the status of replication in three different ways.
+ Look through the PostgreSQL logs on the subscriber node to find failure messages. The log identifies failure with messages that include exit code 1, as shown following.

  ```
  2022-07-06 16:17:03 UTC::@:[7361]:LOG: background worker "pglogical apply 16404:2880255011" (PID 14610) exited with exit code 1
  2022-07-06 16:19:44 UTC::@:[7361]:LOG: background worker "pglogical apply 16404:2880255011" (PID 21783) exited with exit code 1
  ```
+ Connect to the database on the subscriber node using `psql` and query the `pg_replication_origin` view, as follows.

  ```
  SELECT * FROM pg_replication_origin;
   roident | roname
  ---------+--------
  (0 rows)
  ```

  The empty result set means that replication has been disrupted. Normally, you see output such as the following.

  ```
     roident |                       roname
    ---------+----------------------------------------------------
           1 | pgl_labdb_docs_labcb4fa94_docs_lab3de412c
    (1 row)
  ```
+ Query the `pglogical.show_subscription_status` function as shown in the following example.

  ```
  SELECT subscription_name,status,slot_name FROM pglogical.show_subscription_status();
       subscription_name | status |              slot_name
  ---====----------------+--------+-------------------------------------
   docs_lab_subscription | down   | pgl_labdb_docs_labcb4fa94_docs_lab3de412c
  (1 row)
  ```

  This output shows that replication has been disrupted. Its status is `down`. Normally, the output shows the status as `replicating`.

If your logical replication process has been disrupted, you can re-establish replication by following these steps.

**To reestablish logical replication between publisher and subscriber nodes**

To re-establish replication, you first disconnect the subscriber from the publisher node and then re-establish the subscription, as outlined in these steps. 

1. Connect to the subscriber node using `psql` as follows.

   ```
   psql --host={{222222222222}}.{{aws-region}}.rds.amazonaws.com --port=5432 --username={{postgres}} --password --dbname={{labdb}}
   ```

1. Deactivate the subscription by using the `pglogical.alter_subscription_disable` function.

   ```
   SELECT pglogical.alter_subscription_disable('docs_lab_subscription',true);
    alter_subscription_disable
   ----------------------------
    t
   (1 row)
   ```

1. Get the publisher node's identifier by querying the `pg_replication_origin`, as follows.

   ```
   SELECT * FROM pg_replication_origin;
    roident |               roname
   ---------+-------------------------------------
          1 | pgl_labdb_docs_labcb4fa94_docs_lab3de412c
   (1 row)
   ```

1. Use the response from the previous step with the `pg_replication_origin_create` command to assign the identifier that can be used by the subscription when re-established. 

   ```
   SELECT pg_replication_origin_create('pgl_labdb_docs_labcb4fa94_docs_lab3de412c');
     pg_replication_origin_create
   ------------------------------
                               1
   (1 row)
   ```

1. Turn on the subscription by passing its name with a status of `true`, as shown in the following example.

   ```
   SELECT pglogical.alter_subscription_enable('docs_lab_subscription',true);
     alter_subscription_enable
   ---------------------------
    t
   (1 row)
   ```

Check the status of the node. Its status should be `replicating` as shown in this example.

```
SELECT subscription_name,status,slot_name
  FROM pglogical.show_subscription_status();
             subscription_name |   status    |              slot_name
-------------------------------+-------------+-------------------------------------
 docs_lab_subscription         | replicating | pgl_labdb_docs_lab98f517b_docs_lab3de412c
(1 row)
```

Check the status of the subscriber's replication slot on the publisher node. The slot's `active` column should return `t` (true), indicating that replication has been re-established.

```
SELECT slot_name,plugin,slot_type,active
  FROM pg_replication_slots;
                    slot_name              |      plugin      | slot_type | active
-------------------------------------------+------------------+-----------+--------
 pgl_labdb_docs_lab98f517b_docs_lab3de412c | pglogical_output | logical   | t
(1 row)
```