

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `describe_cluster_instances`
<a name="pc-py-lib-api-fleet-describe-instances"></a>

```
describe_cluster_instances(cluster_name, region, next_token, node_type, queue_name)
```

Describe a cluster's instances.Parameters:

**`cluster_name` (required)**  
The cluster name.

**`region`**  
The cluster AWS Region.

**`next_token`**  
The token for the next set of results.

**`node_type`**  
Filters the instances by `node_type`.  
Valid values: `HeadNode` \| `ComputeNode`

**`queue_name`**  
Filters the instances by queue name.