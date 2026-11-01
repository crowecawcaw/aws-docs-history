

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `list_image_log_streams`
<a name="pc-py-lib-api-logs-image-stack-log-streams"></a>

```
list_image_log_streams(image_id, region, next_token)
```

List log streams for an image.Parameters:

**`image_id` (required)**  
The image ID.

**`region`**  
The image AWS Region.

**`next_token`**  
The token for the next set of results.