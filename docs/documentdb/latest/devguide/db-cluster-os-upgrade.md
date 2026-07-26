# Updating a cluster's operating system

You can apply operating system (OS) updates across all instances in your cluster using the cluster-level `os-upgrade` maintenance action.
Amazon DocumentDB updates instances in a rolling manner, a few at a time, and updates the primary instance last to minimize failovers.
The update runs during the cluster maintenance window. After an instance receives an OS update, its buffer cache starts empty,
and queries on that instance can experience higher latency until the working set is repopulated from the storage volume.

To determine whether your cluster has a pending OS update, see [Determining pending maintenance](db-cluster-determine-pending-maintenance.md "db-cluster-determine-pending-maintenance.md").
For full details on OS updates, including console and CLI procedures, see [Amazon DocumentDB operating system updates](db-instance-maintain.md#os-system-updates "db-instance-maintain.md#os-system-updates").
