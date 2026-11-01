

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `get_cluster_stack_events`
<a name="pc-py-lib-api-logs-cluster-stack-log-stack-events"></a>

```
get_cluster_stack_events(cluster_name, region, next_token)
```

Get stack events for a given cluster.Parameters:

**`cluster_name` (required)**  
The cluster name.

**`region`**  
The cluster AWS Region.

**`next_token`**  
The token for the next set of results.