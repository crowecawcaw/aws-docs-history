

# AWS ParallelCluster reserved users and groups
<a name="users-and-groups-v3"></a>

AWS ParallelCluster creates a set of reserved Linux users and groups on all nodes to run its internal daemons and services, such as the Slurm scheduler and MUNGE authentication. These accounts are assigned UIDs and GIDs from a reserved block, `400`–`405`. AWS ParallelCluster assigns each account **by name** during node bootstrap, and relies on these names, UIDs, and GIDs remaining stable and consistent across every node in the cluster.

**Warning**  
Do not change the names, UIDs, GIDs, or ownership of the reserved users and groups listed on this page. Changing these values can cause cluster create, update, and delete (CRUD) operations and image build operations to fail. It can also break the AWS ParallelCluster management daemons at run time.

The following table lists the users and groups that AWS ParallelCluster creates and their default UIDs and GIDs. Each user has a matching primary group with the same name and ID, except for `pcluster-slurm-share`, which is a group with no associated user.


**AWS ParallelCluster reserved users and groups**  

| Name | Default UID | Default GID | Purpose | 
| --- | --- | --- | --- | 
| `pcluster-admin` | `400` | `400` | AWS ParallelCluster administrative and service user, and its matching primary group. Runs the management daemons (for example `clusterstatusmgtd` and `loginmgtd`) and the Slurm resume program. | 
| `slurm` | `401` | `401` | User and matching primary group for the Slurm scheduler daemons (`slurmctld`, `slurmd`, and `slurmdbd`). | 
| `munge` | `402` | `402` | User and matching primary group for the MUNGE authentication daemon, which Slurm uses to authenticate communication between nodes. | 
| `dcvextauth` | `403` | `403` | User and matching primary group for the Amazon DCV external authenticator. | 
| `pcluster-slurm-share` | Not applicable | `405` | Shared group used by the Slurm resume program. It has no associated user; the `slurm` and `pcluster-admin` users are members. | 

**Note**  
If you create additional users or groups of your own, we recommend that you assign them UIDs and GIDs outside the range that AWS ParallelCluster reserves, to avoid conflicts with these accounts.