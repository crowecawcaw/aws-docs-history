# Adding Neptune reader instances to a DB Cluster

In Neptune DB clusters, there is one primary DB instance and up to 15
Neptune reader instances. The primary DB instance supports read and write operations, and performs all
of the data modifications to the cluster volume. Neptune reader instances connect to the same storage
volume as the primary DB instance and support only read operations.

Use reader instances to offload read workloads from the primary DB instance.

We recommend that you distribute the primary instance and Neptune readers in your DB
cluster over multiple Availability Zones to improve the availability of your DB cluster.

The [following section](manage-console-create-replica.md "manage-console-create-replica.md")
describes how to create a reader instance in your DB cluster.
