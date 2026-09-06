

# Cloned clusters in AWS CloudHSM
<a name="cloned-clusters"></a>

Use CloudHSM CLI to synchronize a cluster in a remote region, *if the cluster in that region was originally created from the backup of a cluster in another region*. Let's say you copied a cluster to another region (destination) and then later you want to synchronize changes from the original cluster (source). In scenarios like this, you use the [key replicate](cloudhsm_cli-key-replicate.md) and [user replicate](cloudhsm_cli-user-replicate.md) commands to synchronize the clusters. If you haven't installed CloudHSM CLI, see the instructions in [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md). 

## Related topics
<a name="clone-cluster-related"></a>
+ [user replicate](cloudhsm_cli-user-replicate.md)
+ [key replicate](cloudhsm_cli-key-replicate.md)
+ [Copying Backups Across Regions](copy-backup-to-region.md)