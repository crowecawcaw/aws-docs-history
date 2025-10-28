# Rebooting an Aurora cluster without read availability

Without the read availability feature, you reboot an entire Aurora DB cluster by rebooting
the writer DB instance of that cluster. To do so, follow the procedure in
[Rebooting a DB instance within an Aurora cluster](aurora-reboot-db-instance.md "aurora-reboot-db-instance.md").

Rebooting the writer DB instance also initiates a reboot for each reader DB instance in the cluster. That way,
any cluster-wide parameter changes are applied to all DB instances at the same time. However, the reboot of
all DB instances causes a brief outage for the cluster. The reader DB instances remain unavailable until the
writer DB instance finishes rebooting and becomes available.

This reboot behavior applies to all DB clusters created in Aurora MySQL version 2.09 and lower.

For Aurora PostgreSQL this behavior applies to the following versions:

- 14.6 and lower 14 versions
- 13.9 and lower 13 versions
- 12.13 and lower 12 versions
- All PostgreSQL 11 versions

In the RDS console, the writer DB instance has the value **Writer** under the
**Role** column on the **Databases** page. In the RDS CLI, the output of the
`describe-db-clusters` command includes a section `DBClusterMembers`. The
`DBClusterMembers` element representing the writer DB instance has a value of `true` for
the `IsClusterWriter` field.

###### Important

With the read availability feature, the reboot behavior is different in Aurora MySQL and Aurora PostgreSQL: the reader DB instances typically remain
available while you reboot the writer instance. Then you can reboot the reader instances at a convenient
time. You can reboot the reader instances on a staggered schedule if you want some reader instances to
always be available. For more information, see
[Rebooting an Aurora cluster with read availability](aurora-mysql-survivable-replicas.md "aurora-mysql-survivable-replicas.md").
