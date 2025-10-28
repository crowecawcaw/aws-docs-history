# Enabling local write forwarding

By default, local write forwarding isn't enabled for Aurora MySQL DB clusters. You enable local write forwarding at the
cluster level, not at the instance level.

###### Important

You can also enable local write forwarding for cross-Region read replicas that use binary logging, but
write operations aren't forwarded to the source AWS Region. They're forwarded to the writer DB instance of the binlog read
replica cluster.

Use this method only if you have a use case for writing to the binlog read replica in
the secondary AWS Region. Otherwise, you might end up with a "split-brain" scenario where
replicated datasets are inconsistent with each other.

We recommend that you use global write forwarding with global databases, rather than local write forwarding on
cross-Region read replicas, unless absolutely necessary. For more information, see [Using write forwarding in an Amazon Aurora global database](aurora-global-database-write-forwarding.md "aurora-global-database-write-forwarding.md").

Using the AWS Management Console, select the **Turn on local write forwarding** check box under **Read
replica write forwarding** when you create or modify a DB cluster.

To enable write forwarding with the AWS CLI, use the `--enable-local-write-forwarding` option. This option
works when you create a new DB cluster using the `create-db-cluster` command. It also works when you modify
an existing DB cluster using the `modify-db-cluster` command. You can disable write forwarding by using the
`--no-enable-local-write-forwarding` option with these same CLI commands.

The following example creates an Aurora MySQL DB cluster with write forwarding enabled.

```
aws rds create-db-cluster \
  --db-cluster-identifier write-forwarding-test-cluster \
  `--enable-local-write-forwarding` \
  --engine aurora-mysql \
  --engine-version `8.0.mysql_aurora.3.04.0` \
  --master-username myuser \
  --master-user-password mypassword \
  --backup-retention 1
```

You then create writer and reader DB instances so that you can use write forwarding. For more information, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

To enable write forwarding using the Amazon RDS API, set the `EnableLocalWriteForwarding` parameter to
`true`. This parameter works when you create a new DB cluster using the `CreateDBCluster`
operation. It also works when you modify an existing DB cluster using the `ModifyDBCluster` operation. You
can disable write forwarding by setting the `EnableLocalWriteForwarding` parameter to
`false`.

## Enabling write forwarding for database sessions

The `aurora_replica_read_consistency` parameter is a DB parameter and DB cluster parameter that enables write
forwarding. You can specify `EVENTUAL`, `SESSION`, or `GLOBAL` for the read consistency
level. To learn more about consistency levels, see [Read consistency for write forwarding](aurora-mysql-write-forwarding-consistency.md "aurora-mysql-write-forwarding-consistency.md").

The following rules apply to this parameter:

- The default value is '' (null).
- Write forwarding is available only if you set `aurora_replica_read_consistency` to
  `EVENTUAL`, `SESSION`, or `GLOBAL`. This parameter is relevant only in reader
  instances of DB clusters that have write forwarding enabled.
- You can't set this parameter (when empty) or unset it (when already
  set) inside a multistatement transaction. You can change it from one valid value to
  another valid value during such a transaction, but we don't recommend this
  action.
