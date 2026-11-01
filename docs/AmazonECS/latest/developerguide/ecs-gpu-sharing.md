

# Share GPUs on Amazon ECS
<a name="ecs-gpu-sharing"></a>

Many GPU workloads, such as inference and small model serving, use only a fraction of a GPU's compute and memory. Without sharing, the rest of that capacity sits idle. With Amazon ECS, you can share a single physical NVIDIA GPU across multiple containers so that you can pack more workloads onto the same hardware and reduce GPU waste.

With Amazon ECS, you can use NVIDIA Multi-Process Service (MPS) for GPU sharing. MPS is an NVIDIA CUDA feature that runs multiple processes concurrently on the same GPU, which improves GPU utilization and reduces context-switching overhead. MPS provides memory and compute partitioning, so each container gets a configurable memory limit and an optional compute ceiling.

Amazon ECS manages MPS for you. It starts the MPS daemon on GPU instances, places containers onto GPUs based on available memory, and enforces per-container limits.

MPS provides software-level sharing rather than hardware-level partitioning. For more information about MPS, see [Multi-Process Service](https://docs.nvidia.com/deploy/mps/index.html) in the NVIDIA documentation.

Amazon ECS supports GPU sharing with MPS on Amazon ECS Managed Instances and Amazon ECS on Amazon EC2.

## When to use GPU sharing
<a name="ecs-gpu-sharing-when"></a>

GPU sharing with MPS is well suited for:
+ Inference workloads, embedding generation, and small model serving that don't fully utilize a GPU
+ Multi-model serving where multiple models can share a single GPU
+ Development and testing environments
+ Running multiple lightweight GPU workloads on the same hardware to reduce cost

GPU sharing is not recommended for:
+ Large model training that needs the full GPU memory
+ Workloads that are sensitive to GPU faults from neighboring containers, because MPS is software-level sharing and all containers on a GPU share the same CUDA context
+ Workloads that require hardware-level isolation between processes

## How GPU sharing works
<a name="ecs-gpu-sharing-how"></a>

You configure GPU sharing in the container definition of a task definition. In each container's `resourceRequirements`, you provide a `sharingStrategy` with a GPU memory value instead of specifying an integer in `value` for a dedicated GPU.

When Amazon ECS places a task that uses GPU sharing, it adds up the GPU memory requested by all GPU containers in the task and looks for a GPU with enough free memory. All GPU containers within a single task are placed on the same physical GPU. If the task requests 4,000 MiB across two containers, Amazon ECS finds a single GPU with at least 4,000 MiB of remaining memory and places both containers there.

Multiple tasks can also share the same physical GPU. As long as a GPU has enough remaining memory, Amazon ECS can place additional tasks on it, even if those tasks come from different services. A task that shares a GPU and a task that uses a dedicated GPU can run on the same instance, on different GPUs.

On Amazon ECS Managed Instances, Amazon ECS monitors the health of GPUs and the MPS daemon on each instance. If Amazon ECS detects a GPU hardware failure or an MPS daemon failure, it drains the instance and replaces it. For more information about GPU auto repair, see [GPU auto repair for Amazon ECS managed instances](managed-instances-gpu-auto-repair.md).

## Configure GPU sharing
<a name="ecs-gpu-sharing-configure"></a>

To share a GPU, add a `sharingStrategy` object to the `resourceRequirements` of each GPU container in your task definition. The `sharingStrategy` object contains an `nvidiaMps` object with the following fields. For more information about `resourceRequirements`, see [Resource requirements](task_definition_parameters-managed-instances.md#container_definition_resourcerequirements-managed-instances).

`memory`  
Required: Yes  
The GPU memory limit for the container, in MiB. This value is a hard ceiling on the GPU memory that the container can use. The value must be greater than `0`.  
To find the total GPU memory available on an instance, use the `DescribeContainerInstances` API (the `totalMemoryInMiB` field) or check the GPU specifications for your instance type.

`maxComputePercent`  
Required: No  
The maximum percentage of GPU compute that the container can use, as an integer from `1` to `100`. This sets a ceiling on the container's GPU compute usage, not a reservation. When a container is idle, its unused compute is available to other containers on the same GPU, up to each of their own `maxComputePercent` values. If you don't specify this parameter, the container can use up to `100` percent.

Amazon ECS places tasks based on GPU memory only, so it doesn't account for compute when making placement decisions.

You can set the sharing strategy in the Amazon ECS console task-definition editor, or with JSON, the AWS CLI, or the API.

Amazon ECS sets the following reserved environment variables in each container that shares a GPU. Don't set these variables in your container definition.
+ `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT` for the memory limit
+ `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` for the compute ceiling

The following example task definition runs two inference containers that share one GPU with MPS, along with one non-GPU sidecar container. Each GPU container requests a different amount of GPU memory and compute.

In the following example, replace {{account-id}} with your AWS account ID.

```
{
  "family": "mps-inference",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::{{account-id}}:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "model-a",
      "image": "nvidia/cuda:12.0.0-base-ubuntu22.04",
      "essential": true,
      "resourceRequirements": [
        {
          "type": "GPU",
          "sharingStrategy": {
            "nvidiaMps": {
              "memory": 12288,
              "maxComputePercent": 50
            }
          }
        }
      ]
    },
    {
      "name": "model-b",
      "image": "nvidia/cuda:12.0.0-base-ubuntu22.04",
      "essential": true,
      "resourceRequirements": [
        {
          "type": "GPU",
          "sharingStrategy": {
            "nvidiaMps": {
              "memory": 8192,
              "maxComputePercent": 25
            }
          }
        }
      ]
    },
    {
      "name": "log-router",
      "image": "public.ecr.aws/aws-observability/aws-for-fluent-bit:stable",
      "essential": false
    }
  ],
  "requiresCompatibilities": [
    "MANAGED_INSTANCES"
  ],
  "cpu": "4096",
  "memory": "8192"
}
```

## Validation rules
<a name="ecs-gpu-sharing-validation"></a>

Amazon ECS applies the following rules to GPU sharing configurations:
+ A GPU resource requirement uses either `value` (a dedicated GPU) or `sharingStrategy` (a shared GPU), but not both. When you specify `sharingStrategy`, you must omit `value`.
+ All GPU containers in a task must use the same sharing strategy. If any container uses `sharingStrategy`, no other container in that task can request a dedicated GPU with `value`.
+ The `memory` value is required and must be greater than `0`.
+ The `maxComputePercent` value is optional. If you specify it, the value must be an integer from `1` to `100`.
+ For Amazon ECS Managed Instances, the task's `requiresCompatibilities` must include `MANAGED_INSTANCES`. For Amazon ECS on Amazon EC2, use the `EC2` launch type.
+ GPU sharing is not supported for task definitions that require `EXTERNAL` compatibility (Amazon ECS Anywhere).
+ You can't specify `sharingStrategy` in a container override. Container overrides in the `RunTask` and `StartTask` requests don't support GPU sharing configuration, so define `sharingStrategy` in the task definition instead. Services run the task definition as registered and aren't affected.

## Set up GPU sharing by launch type
<a name="ecs-gpu-sharing-setup"></a>

With Amazon ECS Managed Instances, Amazon ECS selects and manages the GPU instances for you. You don't need any setup beyond the task definition.

With Amazon ECS on Amazon EC2, launch a supported NVIDIA GPU instance with the Amazon ECS AL2023 GPU-optimized AMI. GPU sharing with MPS on Amazon ECS on Amazon EC2 requires Amazon ECS container agent version `1.107.0` or later and the Amazon ECS AL2023 GPU-optimized AMI version `20261019` or later. After the instance registers with your cluster, the task-definition configuration is the same as for Amazon ECS Managed Instances.

## Considerations
<a name="ecs-gpu-sharing-considerations"></a>
+ GPU sharing with MPS is supported on the G4dn, G5, G6, G6e, G7, G7e, P3, P4d, P5, P5e, P5en, and P6-B200 instance families. GPU sharing is not supported on AWS Fargate, Amazon ECS Express Mode, or Amazon ECS managed daemon tasks.
+ GPU sharing with MPS on Amazon ECS on Amazon EC2 requires Amazon ECS container agent version `1.107.0` or later and the Amazon ECS AL2023 GPU-optimized AMI version `20261019` or later.
+ Run a single GPU process per container when you use NVIDIA MPS for GPU sharing. For applications that require multiple GPU processes, configure the GPU memory requirement based on the combined peak memory usage of all processes. Use application-level controls to keep total consumption within the configured value. Amazon ECS uses this value to determine container placement on shared GPUs. As a result, multi-process applications can consume more GPU memory than configured, which can cause memory contention.
+ If one container triggers a fatal GPU error, such as an illegal memory access from a faulty GPU kernel, the containers sharing that physical GPU could be affected. Containers on other GPUs on the same instance aren't affected.
+ The `maxComputePercent` value is a ceiling, not a guaranteed reservation. When a container is idle, its unused compute is available to other containers on the same GPU, up to each of their own `maxComputePercent` values.
+ GPU sharing is not supported for task definitions that require `EXTERNAL` compatibility (Amazon ECS Anywhere).
+ Tasks from different services that use the same capacity provider can be placed on the same GPU. To prevent tasks from different services from sharing a GPU, use separate capacity providers or separate clusters for those services.
+ For GPUs shared with MPS, Amazon ECS doesn't emit the following per-task and per-container GPU metrics:
  + The `TaskGPUUtilization` and `ContainerGPUUtilization` metrics.
  + The `TaskGPUMemoryUtilization` and `ContainerGPUMemoryUtilization` metrics.
  + The `TaskGPUMemoryTotal` and `ContainerGPUMemoryTotal` metrics.
  + The `TaskGPUMemoryUsed` and `ContainerGPUMemoryUsed` metrics.
+ The following per-task and per-container GPU metrics remain available for GPUs shared with MPS:
  + The `TaskGPUPowerDraw` and `ContainerGPUPowerDraw` metrics.
  + The `TaskGPUTemperature` and `ContainerGPUTemperature` metrics.
  + The `TaskGPURestartAppXidCount` and `ContainerGPURestartAppXidCount` metrics.
+ Instance-level GPU metrics remain available, including `InstanceGPUUsageTotal` and `InstanceGPULimit`.

## Monitor GPU sharing
<a name="ecs-gpu-sharing-monitoring"></a>

You can confirm that a GPU is shared and track GPU usage with the Amazon ECS API and Amazon CloudWatch metrics.

### Confirm a GPU is shared
<a name="ecs-gpu-sharing-monitoring-confirm"></a>

To confirm that a GPU is shared, call the `DescribeContainerInstances` API. The response includes the `gpuDevices` field with the sharing mode, container count, and remaining memory for each GPU. The following is an example response.

```
{
  "containerInstances": [
    {
      "ec2InstanceId": "i-0c74b75400ab4228d",
      "runningTasksCount": 1,
      "gpuDevices": [
        {
          "gpuId": "GPU-70d3bdaf-8635-81e0-8e44-446248a92c83",
          "sharingMode": "NVIDIA_MPS",
          "totalMemoryInMiB": 22587,
          "remainingMemoryInMiB": 16587,
          "containerCount": 2
        }
      ]
    }
  ]
}
```

### View per-task configuration
<a name="ecs-gpu-sharing-monitoring-view"></a>

To view the sharing configuration for each task, call the `DescribeTasks` API. Each container's `gpuSharingStrategy` shows its memory and compute limits, and containers that share a GPU list the same value in `gpuIds`. The following is an example response.

```
{
  "tasks": [
    {
      "lastStatus": "RUNNING",
      "launchType": "MANAGED_INSTANCES",
      "containers": [
        {
          "name": "mps-a",
          "gpuIds": ["GPU-70d3bdaf-8635-81e0-8e44-446248a92c83"],
          "gpuSharingStrategy": { "nvidiaMps": { "memory": 4000, "maxComputePercent": 50 } }
        },
        {
          "name": "mps-b",
          "gpuIds": ["GPU-70d3bdaf-8635-81e0-8e44-446248a92c83"],
          "gpuSharingStrategy": { "nvidiaMps": { "memory": 2000, "maxComputePercent": 50 } }
        }
      ]
    }
  ]
}
```

### Track GPU usage
<a name="ecs-gpu-sharing-monitoring-track"></a>
+ **Higher task density**: With GPU sharing, more tasks run on the same instance. Use the `RunningTaskCount` metric to compare task counts per service before and after you enable sharing. For per-instance task density, use the `instance_number_of_running_tasks` metric, which CloudWatch Container Insights collects for each EC2 instance when you deploy the CloudWatch agent to collect EC2 instance-level metrics.
+ **Fewer GPUs for the same workload**: The `InstanceGPUUsageTotal` metric in CloudWatch Container Insights shows how many physical GPUs are in use. With MPS, the same workload uses fewer GPUs.
+ **Instance GPU headroom**: Compare `InstanceGPUUsageTotal` with `InstanceGPULimit` to see how full an instance is. With MPS, more tasks fit before an instance runs out of GPUs.