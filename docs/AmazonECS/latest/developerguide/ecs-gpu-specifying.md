

# Specifying GPUs in an Amazon ECS task definition
<a name="ecs-gpu-specifying"></a>

To use the GPUs on a container instance and the Docker GPU runtime, make sure that you designate the number of GPUs your container requires in the task definition. You can specify an integer value, a decimal value for fractional GPUs, or `ALL`. When you specify `ALL`, all GPUs on the container instance are allocated to the container. When you specify a decimal value such as `0.25`, Amazon ECS places the task on a fractional GPU instance that provides the requested GPU capacity. As containers that support GPUs are placed, the Amazon ECS container agent pins the desired number of physical GPUs to the appropriate container. The number of GPUs reserved for all containers in a task cannot exceed the number of available GPUs on the container instance the task is launched on. For more information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md).

**Important**  
If your GPU requirements aren't specified in the task definition, the task uses the default Docker runtime.

The following shows the JSON format for the GPU requirements in a task definition:

```
{
  "containerDefinitions": [
     {
        ...
        "resourceRequirements" : [
            {
               "type" : "GPU", 
               "value" : "{{2}}"
            }
        ],
     },
...
}
```

You can also specify `ALL` as the value instead of a number to allocate all GPUs on the container instance to the container.

The following example demonstrates the syntax for a Docker container that specifies a GPU requirement. This container uses two GPUs, runs the `nvidia-smi` utility, and then exits.

```
{
  "containerDefinitions": [
    {
      "memory": 80,
      "essential": true,
      "name": "gpu",
      "image": "nvidia/cuda:11.0.3-base",
      "resourceRequirements": [
         {
           "type":"GPU",
           "value": "2"
         }
      ],
      "command": [
        "sh",
        "-c",
        "nvidia-smi"
      ],
      "cpu": 100
    }
  ],
  "family": "example-ecs-gpu"
}
```

The following example task definition shows a TensorFlow container that prints the number of available GPUs. The task runs on Amazon ECS Managed Instances, requires one GPU, and uses a `g4dn.xlarge` instance.

```
{
  "family": "tensorflow-gpu",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::account-id:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "tensorflow",
      "image": "tensorflow/tensorflow:latest-gpu",
      "essential": true,
      "command": [
        "python",
        "-c",
        "import tensorflow as tf; print('Num GPUs Available: ', len(tf.config.list_physical_devices('GPU')))"
      ],
      "resourceRequirements": [
        {
          "type": "GPU",
          "value": "1"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/tensorflow-gpu",
          "awslogs-region": "region",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": [
    "MANAGED_INSTANCES"
  ],
  "cpu": "4096",
  "memory": "8192",
}
```

## Specifying fractional GPUs
<a name="ecs-gpu-specifying-fractional"></a>

Amazon ECS supports fractional GPU scheduling with Amazon EC2 G6f instances. G6f instances provide hardware-partitioned fractions of an NVIDIA L4 GPU, where each instance exposes a fixed GPU slice (1/8, 1/4, or 1/2) with dedicated GPU memory and compute. To use a fractional GPU, specify a decimal value in your container definition's `resourceRequirements`:

```
"resourceRequirements": [
  {
    "type": "GPU",
    "value": "0.25"
  }
]
```

The supported fractional values and their corresponding G6f instance types are:


| GPU value | GPU fraction | GPU memory | Instance types | 
| --- | --- | --- | --- | 
| 0.125 | 1/8 GPU | 3 GB | g6f.large, g6f.xlarge | 
| 0.25 | 1/4 GPU | 6 GB | g6f.2xlarge | 
| 0.5 | 1/2 GPU | 12 GB | g6f.4xlarge, gr6f.4xlarge | 

The following example task definition runs a lightweight inference container on a fractional GPU with 1/4 of an NVIDIA L4 GPU (6 GB GPU memory):

```
{
  "family": "fractional-gpu-inference",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::account-id:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "inference",
      "image": "nvidia/cuda:12.0.0-base-ubuntu22.04",
      "essential": true,
      "command": ["nvidia-smi"],
      "resourceRequirements": [
        {
          "type": "GPU",
          "value": "0.25"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/fractional-gpu-inference",
          "awslogs-region": "region",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": [
    "MANAGED_INSTANCES"
  ],
  "cpu": "2048",
  "memory": "4096"
}
```
+ Only one container per task can request a fractional GPU value. If a container specifies a fractional GPU, no other container in that task definition can have a GPU resource requirement.
+ Integer values (`1`, `2`, etc.) are treated as full GPU requests and only place on instances with full GPU capacity. Decimal values (`0.125`, `0.25`, `0.5`) are treated as fractional GPU requests and place on instances with the corresponding fractional GPU partition.
+ You can include both fractional GPU instances (G6f) and full GPU instances (such as g5 or g6) in the same capacity provider. Amazon ECS routes tasks to the correct instance type based on the declared GPU value. You do not need separate capacity providers per GPU family.
+ You can use fractional GPU scheduling with Amazon ECS Managed Instances and Amazon ECS on Amazon EC2. Fargate and Amazon ECS Anywhere do not support fractional GPU scheduling.
+ For full GPU workloads, continue using integer values as before: `"value": "1"`.