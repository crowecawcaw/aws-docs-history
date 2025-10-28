# AWS ParallelCluster shared storage considerations

Consider the following when working with shared storage in AWS ParallelCluster.

- Back up your file system data with [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") or
  another method to manage backups for all of your storage systems.
- To add shared storage, you add a shared storage section to your configuration file and create or update the cluster.
- To remove shared storage, you remove the shared storage section from your configuration file and update the cluster.
- To replace existing AWS ParallelCluster managed shared storage with new managed storage, change the value for [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") /
  [Name](SharedStorage-v3.md#yaml-SharedStorage-Name "SharedStorage-v3.md#yaml-SharedStorage-Name") and update the cluster.

###### Warning

By default, the existing AWS ParallelCluster managed storage and data is deleted when you perform the cluster update with a new `Name` parameter.
If you need to change `Name` and retain the existing managed shared storage data, make sure you either set the `DeletionPolicy` to `Retain`
or back up the data before you update the cluster.

- If you don't back up AWS ParallelCluster managed storage data and `DeletionPolicy` is `Delete`, your
  data is deleted when either your cluster is deleted or when your managed storage is removed from the cluster configuration and the cluster is updated.
- If you don't back up AWS ParallelCluster managed storage data and `DeletionPolicy` is `Retain`, your file system is
  detached before the cluster is deleted and can be re-attached to another cluster as an external file system. Your data is preserved.
- If AWS ParallelCluster managed storage is removed from the cluster configuration and `DeletionPolicy` is `Retain`,
  it can be re-attached to the cluster as an external file system with your cluster data preserved.
- Starting with AWS ParallelCluster version 3.4.0, you can enhance security for Amazon EFS file system mounts by configuring [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") / [EfsSettings](SharedStorage-v3.md#SharedStorage-v3-EfsSettings "SharedStorage-v3.md#SharedStorage-v3-EfsSettings") /
  [EncryptionInTransit](SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-EncryptionInTransit "SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-EncryptionInTransit") and [IamAuthorization](SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-IamAuthorization "SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-IamAuthorization") settings.
- When mounting an external filesystem to the /home directory, AWS ParallelCluster copies the contents of the head node's /home directory
  to the external filesystem. It copies existing data in the /home directory without overwriting existing files or directories on the external storage.
  This includes the cluster's SSH key for the default user in case it does not already exist on the external filesystem. Consequently all other clusters
  that mount the same external filesystem to their respective /home directory will also have the same SSH key for their default user of the cluster.
- In a multi-cluster environment that mounts the same external filesystem to the /home directories of clusters, SSH keys that grant access to the compute nodes,
  created on the head node by AWS ParallelCluster, are generated only once when the first cluster mounts the external filesystem to /home. All other clusters use
  the same SSH key. As a result, anyone possessing the SSH key for the default user of these shared clusters can access any cluster. All compute nodes allow
  connections using the initially generated key.
