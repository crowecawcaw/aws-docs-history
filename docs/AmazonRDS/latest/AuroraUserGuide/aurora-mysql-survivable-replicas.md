# Rebooting an Aurora cluster with read availability

With the read availability feature, you can reboot the writer instance of your Aurora cluster without rebooting the reader
instances in the primary or secondary DB cluster. Doing so can help maintain high availability of the cluster for read
operations while you reboot the writer instance. You can reboot the reader instances later, on a schedule that's convenient
for you. For example, in a production cluster you might reboot the reader instances one at a time, starting only after the
reboot of the primary instance is finished. For each DB instance that you reboot, follow the procedure in [Rebooting a DB instance within an Aurora cluster](aurora-reboot-db-instance.md "aurora-reboot-db-instance.md").

The read availability feature for primary DB clusters is available in Aurora MySQL version 2.10 and higher. Read availability for
secondary DB clusters is available in Aurora MySQL version 3.06 and higher.

For Aurora PostgreSQL this feature is available by default in the following versions:

- 15.2 and higher 15 versions
- 14.7 and higher 14 versions
- 13.10 and higher 13 versions
- 12.14 and higher 12 versions
  For more information on the read availability feature in Aurora PostgreSQL, see [Improving the read availability of Aurora Replicas](AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Replicas.SRO "AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Replicas.SRO").

Before this feature, rebooting the primary instance caused a reboot for each reader instance at the same time. If your Aurora
cluster is running an older version, use the reboot procedure in [Rebooting an Aurora cluster without read availability](aurora-reboot-cluster.md "aurora-reboot-cluster.md") instead.

###### Note

The change to reboot behavior in Aurora DB clusters with read availability is different for Aurora global databases in
Aurora MySQL versions lower than 3.06. If you reboot the writer instance for the primary cluster in an Aurora global database,
the reader instances in the primary cluster remain available. However, the DB instances in any secondary clusters reboot at the
same time.

A limited version of the improved read availability feature is supported by Aurora global databases for Aurora PostgreSQL
versions 12.16, 13.12, 14.9, 15.4, and higher.

You frequently reboot the cluster after making changes to cluster parameter groups. You make parameter changes by following the
procedures in [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). Suppose that you reboot
the writer DB instance in an Aurora cluster to apply changes to cluster parameters. Some or all of the reader DB instances might
continue using the old parameter settings. However, the different parameter settings don't affect the data integrity of the
cluster. Any cluster parameters that affect the organization of data files are only used by the writer DB instance.

For example, in an Aurora MySQL cluster, you can update cluster parameters such as `binlog_format` and
`innodb_purge_threads` on the writer instance before the reader instances. Only the writer instance is writing
binary logs and purging undo records. For parameters that change how queries interpret SQL statements or query output, you might
need to take care to reboot the reader instances immediately. You do this to avoid unexpected application behavior during
queries. For example, suppose that you change the `lower_case_table_names` parameter and reboot the writer instance.
In this case, the reader instances might not be able to access a newly created table until they are all rebooted.

For a list of all the Aurora MySQL cluster parameters, see [Cluster-level parameters](AuroraMySQL.Reference.md#AuroraMySQL.Reference.Parameters.Cluster "AuroraMySQL.Reference.md#AuroraMySQL.Reference.Parameters.Cluster").

For a list of all the Aurora PostgreSQL cluster parameters, see [Aurora PostgreSQL cluster-level parameters](AuroraPostgreSQL.Reference.md#AuroraPostgreSQL.Reference.Parameters.Cluster "AuroraPostgreSQL.Reference.md#AuroraPostgreSQL.Reference.Parameters.Cluster").

###### Tip

Aurora MySQL might still reboot some of the reader instances along with the writer instance if your cluster is processing a
workload with high throughput.

The reduction in the number of reboots applies during failover operations also. Aurora MySQL only restarts the writer DB instance
and the failover target during a failover. Other reader DB instances in the cluster remain available to continue processing
queries through connections to the reader endpoint. Thus, you can improve availability during a failover by having more than
one reader DB instance in a cluster.
