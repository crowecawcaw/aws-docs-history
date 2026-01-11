# Updating read replicas

with MySQL

Read replicas are designed to support read queries, but you might need occasional updates.
For example, you might need to add an index to optimize the specific types of
queries accessing the replica.

Although you can enable updates by setting the `read_only` parameter to
`0` in the DB parameter group for the read replica, we recommend that
you don't do so because it can cause problems if the read replica becomes
incompatible with the source DB instance. For maintenance operations, we recommend
that you use blue/green deployments. For more information, see [Using Blue/Green Deployments for database updates](blue-green-deployments.md "blue-green-deployments.md").

If you disable read-only on a read replica, change the value of the
`read_only` parameter back to `1` as soon as possible.
