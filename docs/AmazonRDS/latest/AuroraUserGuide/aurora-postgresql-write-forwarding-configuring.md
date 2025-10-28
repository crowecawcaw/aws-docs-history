# Configuring Aurora PostgreSQL for Local write forwarding

Using the following sections, you can enable local write forwarding for your Amazon Aurora PostgreSQL DB cluster, configuring
consistency levels, and managing transactions with write forwarding.

## Enabling local write forwarding

By default, local write forwarding isn't enabled for Aurora PostgreSQL DB clusters. You enable local write forwarding at the
cluster level, not at the instance level.

Using the AWS Management Console, select the **Turn on local write forwarding** check box under **Read
replica write forwarding** when you create or modify a DB cluster.

To enable local write forwarding with the AWS CLI, use the `--enable-local-write-forwarding` option. This option
works when you create a new DB cluster using the `create-db-cluster` command. It also works when you modify
an existing DB cluster using the `modify-db-cluster` command. You can disable local write forwarding by using the
`--no-enable-local-write-forwarding` option with these same CLI commands.

The following example creates an Aurora PostgreSQL DB cluster with local write forwarding enabled.

```

                        aws rds create-db-cluster \
                        --db-cluster-identifier write-forwarding-test-cluster \
                        `--enable-local-write-forwarding` \
                        --engine aurora-postgresql \
                        --engine-version `16.4` \
                        --master-username myuser \
                        --master-user-password mypassword \
                        --backup-retention 1

```

You then create writer and reader DB instances so that you can use write forwarding. For more information, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

To enable local write forwarding using the Amazon RDS API, set the `EnableLocalWriteForwarding` parameter to
`true`. This parameter works when you create a new DB cluster using the `CreateDBCluster`
operation. It also works when you modify an existing DB cluster using the `ModifyDBCluster` operation. You
can disable local write forwarding by setting the `EnableLocalWriteForwarding` parameter to
`false`.

### Enabling local write forwarding for database sessions

The `apg_write_forward.consistency_mode` parameter is a DB parameter and DB cluster parameter that enables write
forwarding. You can specify `SESSION`, `EVENTUAL`, `GLOBAL`, or `OFF` for the read consistency
level. To learn more about consistency levels, see [Consistency and isolation for local write forwarding in Aurora PostgreSQL](#aurora-postgresql-write-forwarding-isolation "#aurora-postgresql-write-forwarding-isolation").

The following rules apply to this parameter:

- The default value is `SESSION`.
- Local write forwarding is available only if you set `apg_write_forward.consistency_mode` to
  `EVENTUAL`, `SESSION`, or `GLOBAL`. This parameter is relevant only in reader
  instances of DB clusters that have local write forwarding enabled.
- Setting the value to `OFF` disables local write forwarding in the session.

## Consistency and isolation for local write forwarding in Aurora PostgreSQL

You can control the degree of read consistency on a read replica. You can adjust the read consistency level
to ensure that all forwarded write operations from your session are visible in the read replica before any subsequent queries.
You can also use this setting to ensure that queries on the read replica always see the most current updates from the writer DB instance.
This is so even for those submitted by other sessions or other clusters. To specify this type of behavior for your application, you
choose the appropriate value for the session-level parameter `apg_write_forward.consistency_mode`.
The `apg_write_forward.consistency_mode` parameter has an effect only on
read replicas that have local write forwarding enabled.

###### Note

For the `apg_write_forward.consistency_mode` parameter, you can specify the
value `SESSION`, `EVENTUAL`, `GLOBAL`, or `OFF`.
By default, the value is set to `SESSION`. Setting the value to
`OFF` disables write forwarding.

As you increase the consistency level, your application spends more time waiting for
changes to be propagated to read replicas. You can choose the balance between lower latency and ensuring that changes made in other locations are fully available before
your queries run.

With each available consistency mode setting, the effect is as follows:

- `SESSION` – A session on a read replica that uses local write
  forwarding see the results of all changes made in that session. The changes are visible regardless of whether
  the transaction is committed. If necessary, the query waits for the results of forwarded write operations to
  be replicated to the current reader DB instance. It doesn't wait for updated results from write operations performed
  in other sessions within the current DB cluster.
- `EVENTUAL` – A session on a read replica that uses local write forwarding might see data that is slightly stale due to replication lag. Results of write operations in the
  same session aren't visible until the write operation is performed on the writer DB instance and replicated
  to the read replica. The query doesn't wait for the updated results to be available. Thus, it might
  retrieve the older data or the updated data, depending on the timing of the statements and the amount of
  replication lag.
- `GLOBAL` – A session on a read replica sees changes made by
  that session. It also sees all committed changes from both the writer DB instance and other read replicas.
  Each query might wait for a period that varies depending on the amount of session lag. The query
  proceeds when the read replica is up-to-date with all committed data from the writer DB instance, as of the
  time that the query began.

###### Note

The global consistency mode impacts the latency of queries executed within a session. It will perform a wait even when the session has not sent any write queries.

- `OFF` – Local write forwarding is disabled.

In sessions that use write forwarding, you can use the `REPEATABLE READ` and `READ COMMITTED` isolation levels. However, the `SERIALIZABLE` isolation level isn't supported.

For more information about all the parameters involved with write forwarding, see [Default parameter settings for write forwarding](aurora-postgresql-write-forwarding-understanding.md#aurora-postgresql-write-forwarding-params "aurora-postgresql-write-forwarding-understanding.md#aurora-postgresql-write-forwarding-params").

## Transaction access modes with write forwarding

If the transaction access mode is set to read only, local write forwarding isn't used. You can set the access mode to
read write only while you’re connected to a DB cluster and session that has local write forwarding enabled.

For more information on the transaction access modes, see [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "https://www.postgresql.org/docs/current/sql-set-transaction.html").
