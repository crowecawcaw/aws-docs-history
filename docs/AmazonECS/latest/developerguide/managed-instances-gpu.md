# Use GPUs with Amazon ECS Managed Instances

Amazon ECS Managed Instances supports GPU-accelerated computing for workloads such as machine
learning, high-performance computing, and video processing through the following Amazon EC2
instance types. For more information about instance types supported by
Amazon ECS Managed Instances, see [Amazon ECS Managed Instances instance types](managed-instances-instance-types.md "managed-instances-instance-types.md").

The following is a subset of GPU-based instance types supported on Amazon ECS Managed Instances:

- `g4dn`: Powered by NVIDIA T4 GPUs, suitable for
  machine learning inference, computer vision, and graphics-intensive
  applications.
- `g5`: Powered by NVIDIA A10G GPUs, offering higher
  performance for graphics-intensive applications and machine learning
  workloads.
- `p3`: Powered by NVIDIA V100 GPUs, designed for
  high-performance computing and deep learning training.
- `p4d`: Powered by NVIDIA A100 GPUs, offering the
  highest performance for for machine learning training and high-performance
  computing.
  When you use GPU-enabled instance types with Amazon ECS Managed Instances, the
  NVIDIA drivers and CUDA toolkit are pre-installed on
  the instance, making it easier to run GPU-accelerated workloads.

## GPU-enabled instance selection

To select GPU-enabled instance types for your Amazon ECS Managed Instances workloads, use
the `instanceRequirements` object in the launch template of the capacity
provider. The following snippet shows the attributes that can be used for selecting
GPU-enabled instances.

```
{
  "instanceRequirements": {
    "acceleratorTypes": "gpu",
    "acceleratorCount": 1,
    "acceleratorManufacturers": ["nvidia"]
  }
}
```

The following snippet shows the attributes that can be used to specify GPU-enabled
instance types in the launch template.

```
{
  "instanceRequirements": {
    "allowedInstanceTypes": ["g4dn.xlarge", "p4de.24xlarge"]
  }
}
```

## GPU-enabled container images

To use GPUs in your containers, you need to use container images that contain the
necessary GPU libraries and tools. NVIDIA provides several pre-built
container images that you can use as a base for your GPU workloads, including the
following:

- `nvidia:cuda`: Base images with the CUDA toolkit
  for GPU computing.
- `tensorflow/tensorflow:latest-gpu`: TensorFlow
  with GPU support.
- `pytorch/pytorch:latest-cuda`: PyTorch with GPU
  support.

For an example task definition for Amazon ECS on Amazon ECS Managed Instances that involves the use
of GPUs, see [Specifying GPUs in an Amazon ECS task definition](ecs-gpu-specifying.md "ecs-gpu-specifying.md").
