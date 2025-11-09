# Example of split cost allocation

data for accelerated instances

The purpose of the following example is to show you how split cost allocation data
is calculated by computing the cost of Kubernetes namespace and pods in Amazon EKS
clusters. The rates used throughout the example are for illustrative purposes
only.

You have the following usage in a single hour:

- Single EC2 instance that is running four pods across two namespaces, and
  you want to understand the costs of each namespace.
- The EC2 instance is p3.16xlarge with 8 GPU, 64 vCPU, and 488 GB
  RAM.
- Amortized cost of the instance is $10/hr.
  Split cost allocation data normalizes the cost per resource based on a relative
  ratio of GPU:(cpu: memory) of 9:1. This implies that a unit of GPU costs 9x as much
  as a unit of CPU and memory. CPU and memory are then assigned a weight of 9:1. For a
  non-accelerated EC2 instance, the current default behavior will be adopted which is
  cpu: memory weight defaults to 9:1.

## Step 1: Compute the unit cost

Based on the cpu and memory resources on the EC2 instance and using the ratio of mentioned above, Split Cost Allocation data first calculates the unit cost per GPU, vCPU-hr and GB-hr.

`GPU-Weight =9`

`GPU+Memory-Weight =1`

`CPU-Weight=1*.9=.9`

`Memory-Weight=1*0.1=0.1`

`Hourly-Instance-Cost=$10`

`GPU-Available=8`

`Memory-Available=488`

`CPU-Available=64`

`UnitCostPerResource = Hourly-Instance-Cost/(( GPU-Weight * GPU-Available) + (Memory-Weight * Memory-Available) + (CPU-Weight * CPU-Available)) 
 = $10/((9*8gpu)+ (0.1 * 488GB) + (.9 * 64vcpu)) = $0.056`

`Cost-per-GPU-Hour = GPU-Weight * UnitCostPerResource = 9 * $0.056 = $0.504`

`Cost-per-vcpu-Hour = CPU-Weight * UnitCostPerResource = .9 * $0.056 = $0.05`

`Cost-per-GB-Hour = Memory-Weight * UnitCostPerResource = .1 * $0.056 = $0.00506`

| Table 1: Unit cost calculation | Instance    | Instance Type | vCPU Available | GPU Available | \*\* | Memory Available | Amortized Cost per Hour | Cost per vCPU-Hour | Cost per GPU-Hour | Cost per GB-Hour |
| ------------------------------ | ----------- | ------------- | -------------- | ------------- | ---- | ---------------- | ----------------------- | ------------------ | ----------------- | ---------------- |
| Instance 1                     | p3.16xlarge | 64            | 8              |               | 488  | $10              | $0.05                   | $0.50              | 0.005             |

## Step 2: Calculate allocated and unused capacity

Allocated Capacity

The GPU, vcpu and Memory allocated to the Kubernetes Pod from the parent EC2 Instance, defined as the Maximum of (reserved, used) capacity

Instance Unused Capacity

The unused capacity of GPU, vcpu and Memory

`Pod1-Allocated-GPU = Max (1 GPU, 1 GPU) = 1 GPU`

`Pod1-Allocated-vcpu = Max (16 vcpu, 4 vcpu) = 16 vcpu`

`Pod1-Allocated-Memory = Max (100 GB, 60 GB) = 100 GB`

`Instance-Unused-GPU = Max (GPU-Available - SUM(Allocated-vcpu), 0)`

`= Max (8 – 8, 0) = 0`

`Instance-Unused-vcpu = Max (CPU-Available - SUM(Allocated-vcpu), 0)`

`= Max (16 – 18, 0) = 0`

`Instance-Unused-Memory = Max (Memory-Available - SUM(Allocated-Memory), 0)`

`= Max (488 – 440, 0) = 48 GB`

In this example, the instance has CPU over subscription, attributed to Pod 2 that used more GPU and vcpu that what was reserved.

| Table 2: Calculate Allocated and Unused Capacity | Pod Name    | Namespace | vcpu Reserved | vcpu Used | vcpu Allocated | GPU Reserved | GPU used | GPU Allocated | Memory Reserved | Memory Used | Memory Allocated |
| ------------------------------------------------ | ----------- | --------- | ------------- | --------- | -------------- | ------------ | -------- | ------------- | --------------- | ----------- | ---------------- |
| Pod 1                                            | Namespace 1 | 16        | 4             | 16        | 1              | 1            | 1        | 100           | 60              | 100         |
| Pod 2                                            | Namespace 2 | 16        | 18            | 18        | 2              | 3            | 3        | 100           | 140             | 140         |
| Pod 3                                            | Namespace 1 | 16        | 4             | 16        | 2              | 1            | 2        | 100           | 60              | 100         |
| Pod 4                                            | Namespace 2 | 16        | 4             | 16        | 2              | 2            | 2        | 100           | 40              | 100         |
| Unused                                           | Unused      | 0         | 34            | 0         | 1              | 1            | 0        | 88            | 188             | 48          |
| \*\*\*                                           |             | 64        | 32            | 66        | 8              | 8            | 8        | 488           | 488             | 488         |

## Step 3: Compute the split usage and utilization ratios

Split usage ratio

The percentage of CPU or memory used by the Kubernetes pod compared to the overall CPU or memory available on the EC2 instance.

Unused ratio

The percentage of CPU or memory used by the Kubernetes pod compared to the overall CPU or memory used on the EC2 instance (that is, not factoring in the unused CPU or memory on the instance).

The percentage of CPU or memory used by the Kubernetes Pod compared to the overall CPU or memory available on the EC2 Instance.

`Pod1-GPU-Utilization-Ratio = Allocated-GPU / Total-GPU`

`= 1 gpu / 8 gpu = 0.125`

`Pod1-vcpu-Utilization-Ratio = Allocated-vcpu / Total-vcpu`

`= 16 vcpu / 66 vcpu = 0.24`

`Pod1-Memory-Utilization-Ratio = Allocated-GB / Total-GB`

`= 100 GB/ 488GB = 0.205`

`Pod1-GPU-Split-Ratio = Pod1-GPU-Utilization-Ratio / (Total-GPU-Utilization-Ratio – Instance-Unused-GPU). Set to 0 if Instance-Unused-GPU = 0`

`= 0 since Instance-Unused-GPU is 0`

`Pod1-vcpu-Split-Ratio = Pod1-CPU-Utilization-Ratio / (Total-CPU-Utilization-Ratio – Instance-Unused-CPU). Set to 0 if Instance-Unused-CPU = 0`

`= 0 since Instance-Unused-CPU is 0`

`Pod1-Memory-Split-Ratio = Pod-Memory-Utilization-Ratio / (Total-Utilization-Ratio – Instance-Unused-Memory). Set to 0 if Instance-Unused-Memory = 0`

`= 0.204/ (1-0.102) = 0.227`

| Table 3: Compute Utilization ratios | Pod Name    | Namespace | vcpu Utilization | vcpu Split Ratio | GPU Utilization | GPU Split Ratio | Memory Utilization | Memory Split Ratio |
| ----------------------------------- | ----------- | --------- | ---------------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ |
| Pod 1                               | Namespace 1 | 0.242     | 0                | 0.125            | 0               | 0.205           | 0.227              |
| Pod 2                               | Namespace 2 | 0.277     | 0                | 0.375            | 0               | 0.287           | 0.318              |
| Pod 3                               | Namespace 1 | 0.242     | 0                | 0.25             | 0               | 0.205           | 0.227              |
| Pod 4                               | Namespace 2 | 0.242     | 0                | 0.25             | 0               | 0.205           | 0.227              |
| Unused                              | Unused      | 0         |                  |                  |                 | 0.098           |                    |
|                                     |             | 1         | 0                | 1                | 0               | 1               | 1                  |

## Step 4: Compute the split cost and unused costs

Split Cost

The pay per use cost allocation of the EC2 Instance cost based on allocated CPU and memory usage by the Kubernetes Pods

Unused Instance Cost

The cost of unused CPU or memory resources on the instance

`Pod1-Split-Cost = (Pod1-GPU-Utilization-Ratio * GPU-Available * Cost per GPU-Hour) + (Pod1-vcpu-Utilization-Ratio * vcpu-Available * Cost per vcpu-Hour) + (Pod1-Memory-Utilization-Ratio * Memory-Available * Cost per GB-Hour)`

`= (.125*8gpu*$0.504) + (0.242 * 64 vcpu * $0.05) + (0.204 * 488GB * $0.00506) = 0.504+ 0.774 + 0.503 = $1.85`

`Pod1-Unused-Cost = (GPU-Split-Ratio * Unused-Cost) + (vcpu-Split-Ratio * Unused-Cost) + (Memory-Split-Ratio * Unused-Cost)`

`= (0*0*8*$0.504) + (0 * $0.05) + (0.227 *.102*488GB*$.00506) = $0.06`

`Pod1-Total-Split-Cost = Pod1-Split-Cost + Pod1-Unused-Cost = $1.85 + $0.06 = $1.91`

[Note: Unused cost = Unused util ratio \* Total resource \* resource hourly cost]

| Table 4 - Summary of the Split and Unused costs calculated each hour for all Pods running within the cluster | Pod Name    | Namespace | Split Cost | Unused Cost | Total Cost |
| ------------------------------------------------------------------------------------------------------------ | ----------- | --------- | ---------- | ----------- | ---------- |
| Pod 1                                                                                                        | Namespace 1 | $1.85     | $0.06      | $1.91       |
| Pod 2                                                                                                        | Namespace 2 | $3.18     | $0.09      | $3.26       |
| Pod 3                                                                                                        | Namespace 1 | $2.35     | $0.06      | $2.41       |
| Pod 4                                                                                                        | Namespace 2 | $2.35     | $0.06      | $2.41       |
| Total                                                                                                        |             |           |            | $10         |
