# Clusters in AWS CloudHSM

A cluster is a collection of individual hardware security modules (HSM) that AWS CloudHSM keeps in sync. When
you perform a task or operation on one HSM in a cluster, the other HSMs in that cluster are
automatically kept up to date.

You can manage your AWS CloudHSM clusters from the [AWS CloudHSM
console](https://console.aws.amazon.com/cloudhsm/ "https://console.aws.amazon.com/cloudhsm/") or one of the [AWS SDKs or command line
tools](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/"). For more information, see the following topics.

To create a cluster, see [Getting started](getting-started.md "getting-started.md").

The following topics provide more information about clusters.

###### Topics

- [Cluster architecture](cluster-architecture.md "cluster-architecture.md")
- [Cluster synchronization](cluster-synchronization.md "cluster-synchronization.md")
- [Cluster high availability and load
  balancing](cluster-high-availability-load-balancing.md "cluster-high-availability-load-balancing.md")
- [Cluster modes](cluster-hsm-types.md "cluster-hsm-types.md")
- [HSM types](hsm-types.md "hsm-types.md")
- [Connecting to the cluster](cluster-connect.md "cluster-connect.md")
- [Scaling HSMs](add-remove-hsm.md "add-remove-hsm.md")
- [Deleting a cluster](delete-cluster.md "delete-cluster.md")
- [Creating clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md")
- [Migrating HSM cluster types](cluster-hsm-type-modification.md "cluster-hsm-type-modification.md")
