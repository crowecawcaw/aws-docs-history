

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `list_official_images`
<a name="pc-py-lib-api-logs-list-official-images"></a>

```
list_official_images(region,os, architecture)
```

Retrieve the list of official AWS ParallelCluster images.Parameters:

**`region`**  
The image AWS Region.

**`os`**  
Filters by operating system distribution. The default is no filtering.

**`architecture`**  
Filters by architecture. The default is no filtering.