# Managing logical

replication slots for Aurora PostgreSQL

Before you can perform a major version upgrade on an Aurora PostgreSQL DB cluster's writer instance
that's serving as a
publisher node in a logical replication scenario, you must drop the replication slots on the
instance. The major version upgrade pre-check process notifies you that the upgrade can't
proceed until the slots are dropped.

To identify replication slots that were created using the `pglogical`
extension, log in to each database and get the name of the nodes. When you query the
subscriber node, you get both the publisher and the subscriber nodes in the output, as shown
in this example.

```
SELECT * FROM pglogical.node;
`node_id | node_name
------------+-------------------
 2182738256 | docs_lab_target
 3410995529 | docs_lab_provider
(2 rows)`
```

You can get the details about the subscription with the following query.

```
SELECT sub_name,sub_slot_name,sub_target
  FROM pglogical.subscription;
 `sub_name | sub_slot_name | sub_target
----------+--------------------------------+------------
 docs_lab_subscription | pgl_labdb_docs_labcb4fa94_docs_lab3de412c | 2182738256
(1 row)`
```

You can now drop the subscription, as follows.

```
SELECT pglogical.drop_subscription(subscription_name := 'docs_lab_subscription');
 `drop_subscription
-------------------
 1
(1 row)`
```

After dropping the subscription, you can delete the node.

```
SELECT pglogical.drop_node(node_name := 'docs-lab-subscriber');
 `drop_node
-----------
 t
(1 row)`
```

You can verify that the node no longer exists, as follows.

```
SELECT * FROM pglogical.node;
 `node_id | node_name
---------+-----------
(0 rows)`
```
