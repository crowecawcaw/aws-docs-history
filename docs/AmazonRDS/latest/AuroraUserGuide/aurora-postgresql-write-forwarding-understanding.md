# Working with local write forwarding for Aurora PostgreSQL

Using the following sections, you can check if a database cluster has local write forwarding enabled, view compatibility considerations, and
see configurable parameters and authentication setup. This information equips you with the details to utilize local write forwarding feature in Aurora PostgreSQL effectively.

###### Note

When a writer instance in a cluster using local write forwarding is restarted, any active, forwarded transactions
and queries on reader instances using local write forwarding are automatically closed. After the writer instance is available again, you can retry these transactions.

## Checking if a DB cluster has local write forwarding enabled

To determine that you can use local write forwarding in a DB cluster, confirm that the cluster has the attribute
`LocalWriteForwardingStatus` set to `enabled`.

In the AWS Management Console, on the **Configuration** tab of the details page for the cluster, you see the status
**Enabled** for **Local read replica write forwarding**.

To see the status of the local write forwarding setting for all of your clusters, run the following AWS CLI command.

```
aws rds describe-db-clusters \
--query '*[].{DBClusterIdentifier:DBClusterIdentifier,LocalWriteForwardingStatus:LocalWriteForwardingStatus}'

[
{
"LocalWriteForwardingStatus": "enabled",
"DBClusterIdentifier": "write-forwarding-test-cluster-1"
},
{
"LocalWriteForwardingStatus": "disabled",
"DBClusterIdentifier": "write-forwarding-test-cluster-2"
},
{
"LocalWriteForwardingStatus": "requested",
"DBClusterIdentifier": "test-global-cluster-2"
},
{
"LocalWriteForwardingStatus": "null",
"DBClusterIdentifier": "aurora-postgresql-v2-cluster"
}
]
```

A DB cluster can have the following values for `LocalWriteForwardingStatus`:

- `disabled` – Local write forwarding is disabled.
- `disabling` – Local write forwarding is in the process of being disabled.
- `enabled` – Local write forwarding is enabled.
- `enabling` – Local write forwarding is in the process of being enabled.
- `null` – Local write forwarding isn't available for this DB cluster.
- `requested` – Local write forwarding has been requested, but is not yet active.

## Default parameter settings for write forwarding

The Aurora cluster parameter groups include settings for the local write forwarding feature. Because these are cluster parameters,
all DB instances in each cluster have the same values for these variables. Details about these parameters are summarized in
the following table, with usage notes after the table.

| Parameter                                               | Scope   | Type         | Default value | Valid values                               |
| ------------------------------------------------------- | ------- | ------------ | ------------- | ------------------------------------------ |
| `apg_write_forward.connect_timeout`                     | Session | seconds      | 30            | 0–2147483647                               |
| `apg_write_forward.consistency_mode`                    | Session | enum         | Session       | `SESSION`, `EVENTUAL`, `GLOBAL`, and `OFF` |
| `apg_write_forward.idle_in_transaction_session_timeout` | Session | milliseconds | 86400000      | 0–2147483647                               |
| `apg_write_forward.idle_session_timeout`                | Session | milliseconds | 300000        | 0–2147483647                               |
| `apg_write_forward.max_forwarding_connections_percent`  | Global  | int          | 25            | 1–100                                      |

The `apg_write_forward.max_forwarding_connections_percent` parameter is the upper limit on database connection slots that can be used to handle queries forwarded from readers.
It is expressed as a percentage of the `max_connections` setting for the writer DB instance. For example, if `max_connections` is `800`
and `apg_write_forward.max_forwarding_connections_percent` is `10`, then the writer allows a maximum of 80 simultaneous forwarded sessions. These connections come from the
same connection pool managed by the `max_connections` setting. This setting applies only on the writer DB instance when the cluster has local write forwarding enabled.

Use the following settings to control local write forwarding requests:

- `apg_write_forward.consistency_mode` – A session-level parameter
  that controls the degree of read consistency on a read replica. Valid values are
  `SESSION`, `EVENTUAL`, `GLOBAL`, or `OFF`.
  By default, the value is set to `SESSION`. Setting the value to
  `OFF` disables local write forwarding in the session. To learn more about
  consistency levels, see [Consistency and isolation for local write forwarding in Aurora PostgreSQL](aurora-postgresql-write-forwarding-configuring.md#aurora-postgresql-write-forwarding-isolation "aurora-postgresql-write-forwarding-configuring.md#aurora-postgresql-write-forwarding-isolation"). This
  parameter is relevant only in reader instances that have local write forwarding enabled.
- `apg_write_forward.connect_timeout` – The maximum number of seconds the
  read replica waits when establishing a connection to the writer DB instance before
  giving up. A value of `0` means to wait indefinitely.
- `apg_write_forward.idle_in_transaction_session_timeout` – The number of milliseconds the writer DB instance waits for activity on a connection
  that's forwarded from a read replica that has an open transaction before closing it. If the session remains idle in transaction beyond this period, Aurora terminates the session.
  A value of `0` disables the timeout.
- `apg_write_forward.idle_session_timeout` – The number of milliseconds the writer DB instance waits for activity on a connection that's forwarded from a
  read replica before closing it. If the session remains idle beyond this period, Aurora terminates the session. A value of `0` disables the timeout.

## rdswriteforwarduser

The `rdswriteforwarduser` is a user that we will use to establish a connection between the read replica and the writer DB instance.

###### Note

`rdswriteforwarduser` inherits its CONNECT privileges to customer databases via the PUBLIC role. If the privileges for the PUBLIC role are revoked,
you will need to GRANT CONNECT privileges for the databases you need to forward writes to.
