

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `delete_cluster`
<a name="pc-py-lib-api-cluster-delete"></a>

```
delete_cluster(cluster_name, region, wait)
```

Delete a cluster in a given Region.Parameters:

**`cluster_name` (required)**  
The cluster name.

**`region`**  
The cluster AWS Region.

**`wait`**  
If set to `True`, waits for the operation to complete. The default is `False`.