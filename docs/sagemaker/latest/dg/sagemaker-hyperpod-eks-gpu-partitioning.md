# Using GPU partitions in Amazon SageMaker HyperPod

Cluster administrators can choose how to maximize GPU utilization across their organization. You can enable GPU partitioning with NVIDIA Multi-Instance GPU (MIG) technology to partition GPU resources into smaller, isolated instances for better resource utilization. This capability provides the ability to run multiple smaller sized tasks concurrently on a single GPU instead of dedicating the entire hardware to a single, often underutilized task. This eliminates wasted compute power and memory.

GPU partitioning with MIG technology supports GPUs and allows you to partition a single supported GPU into up to seven separate GPU partitions. Each GPU partition has dedicated memory, cache, and compute resources, providing predictable isolation.

## Benefits

- **Improved GPU utilization** - Maximize compute efficiency by partitioning GPUs based on compute and memory requirements
- **Task isolation** - Each GPU partition operates independently with dedicated memory, cache, and compute resources
- **Task flexibility** - Support a mix of tasks on a single physical GPU, all running in parallel
- **Flexible setup management** - Support both Do-it-yourself (DIY) Kubernetes configurations using Kubernetes command-line client `kubectl`, and a managed solution with custom labels to easily configure and apply your labels associated with GPU partitions

## Supported Instance Types

GPU partitioning with MIG technology is supported on the following HyperPod instance types:

**A100 GPU Instances** - [https://aws.amazon.com/ec2/instance-types/p4/](https://aws.amazon.com/ec2/instance-types/p4/ "https://aws.amazon.com/ec2/instance-types/p4/")

- **ml.p4d.24xlarge** - 8 NVIDIA A100 GPUs (80GB HBM2e per GPU)
- **ml.p4de.24xlarge** - 8 NVIDIA A100 GPUs (80GB HBM2e per GPU)

**H100 GPU Instances** - [https://aws.amazon.com/ec2/instance-types/p5/](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/")

- **ml.p5.48xlarge** - 8 NVIDIA H100 GPUs (80GB HBM3 per GPU)

**H200 GPU Instances** - [https://aws.amazon.com/ec2/instance-types/p5/](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/")

- **ml.p5e.48xlarge** - 8 NVIDIA H200 GPUs (141GB HBM3e per GPU)
- **ml.p5en.48xlarge** - 8 NVIDIA H200 GPUs (141GB HBM3e per GPU)

**B200 GPU Instances** - [https://aws.amazon.com/ec2/instance-types/p6/](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/")

- **ml.p6b.48xlarge** - 8 NVIDIA B200 GPUs

## GPU partitions

NVIDIA MIG profiles define how GPUs are partitioned. Each profile specifies the compute and memory allocation per MIG instance. The following are the MIG profiles associated with each GPU type:

**A100 GPU (ml.p4d.24xlarge)**

| Profile   | Memory (GB) | Instances per GPU | Total per ml.p4d.24xlarge |
| --------- | ----------- | ----------------- | ------------------------- |
| `1g.5gb`  | 5           | 7                 | 56                        |
| `2g.10gb` | 10          | 3                 | 24                        |
| `3g.20gb` | 20          | 2                 | 16                        |
| `4g.20gb` | 20          | 1                 | 8                         |
| `7g.40gb` | 40          | 1                 | 8                         |

**H100 GPU (ml.p5.48xlarge)**

| Profile   | Memory (GB) | Instances per GPU | Total per ml.p5.48xlarge |
| --------- | ----------- | ----------------- | ------------------------ |
| `1g.10gb` | 10          | 7                 | 56                       |
| `1g.20gb` | 20          | 4                 | 32                       |
| `2g.20gb` | 20          | 3                 | 24                       |
| `3g.40gb` | 40          | 2                 | 16                       |
| `4g.40gb` | 40          | 1                 | 8                        |
| `7g.80gb` | 80          | 1                 | 8                        |

**H200 GPU (ml.p5e.48xlarge and ml.p5en.48xlarge)**

| Profile    | Memory (GB) | Instances per GPU | Total per ml.p5en.48xlarge |
| ---------- | ----------- | ----------------- | -------------------------- |
| `1g.18gb`  | 18          | 7                 | 56                         |
| `1g.35gb`  | 35          | 4                 | 32                         |
| `2g.35gb`  | 35          | 3                 | 24                         |
| `3g.71gb`  | 71          | 2                 | 16                         |
| `4g.71gb`  | 71          | 1                 | 8                          |
| `7g.141gb` | 141         | 1                 | 8                          |

###### Topics

- [Setting up GPU partitions on Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning-setup.md "sagemaker-hyperpod-eks-gpu-partitioning-setup.md")
- [Node Lifecycle and Labels](sagemaker-hyperpod-eks-gpu-partitioning-labels.md "sagemaker-hyperpod-eks-gpu-partitioning-labels.md")
- [Task Submission with MIG](sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md "sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md")
