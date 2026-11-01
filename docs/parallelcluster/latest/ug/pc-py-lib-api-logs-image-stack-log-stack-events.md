

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `get_image_stack_events`
<a name="pc-py-lib-api-logs-image-stack-log-stack-events"></a>

```
get_image_stack_events(image_id, region, next_token)
```

Get stack events for a given image.Parameters:

**`image_id` (required)**  
The image ID.

**`region`**  
The image AWS Region.

**`next_token`**  
The token for the next set of results.