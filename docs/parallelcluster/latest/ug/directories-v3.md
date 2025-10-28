# AWS ParallelCluster internal directories

There are several internal directories that AWS ParallelCluster uses to share data within the cluster.
The following directories are shared between the head node, compute nodes, and login nodes:

- `/opt/slurm`
- `/opt/intel`
- `/opt/parallelcluster/shared (only with compute nodes)`
- `/opt/parallelcluster/shared_login_nodes (only with login nodes)`
- `/home (unless specified in SharedStorage)`

###### Note

By default these directories are created on the head nodes EBS volume and shared as NFS
exports to the compute and login nodes. Starting from AWS ParallelCluster 3.8 you can enable
AWS ParallelCluster to create and manage an Amazon EFS filesystem to host and share these directories
by setting the [SharedStorageType](HeadNode-v3.md#yaml-HeadNode-SharedStorageType "HeadNode-v3.md#yaml-HeadNode-SharedStorageType") parameter
to efs.

When the cluster scales out, NFS exports via the EBS volume may pose performance bottlenecks.
Using EFS, you can avoid NFS exports as your cluster scales out and avoid the performance
bottlenecks associated with them.
