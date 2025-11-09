# P6 Supported DLAMIs

Below are the detailed requirements for running DLAMI on [Amazon EC2 P6-B200 Instances](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/") and
[Amazon EC2 P6e-GB200 Instances](https://aws.amazon.com/ec2/instance-types/p6/ "https://aws.amazon.com/ec2/instance-types/p6/")

## P6-B200 Supported DLAMIs

**The following software is required to operate P6-B200
instances:**

| Software                         | Minimum Version Requirement |
| -------------------------------- | --------------------------- |
| **Nvidia CUDA Toolkit**          | 12.8                        |
| **Nvidia Driver**                | R570                        |
| **NVLINK 5**                     | R570                        |
| **Linux Kernel**                 | 6.1                         |
| **Elastic Fabric Adapter (EFA)** | 1.41.0                      |
| **AWS OFI NCCL Plugin**          | 1.15.0                      |

## P6e-GB200 Supported DLAMIs

**The following software is required to operate
P6e-GB200 instances:**

| Software                         | Minimum Version Requirement |
| -------------------------------- | --------------------------- |
| **Nvidia CUDA Toolkit**          | 12.8                        |
| **Nvidia Driver**                | R570                        |
| **Linux Kernel**                 | 6.12                        |
| **Elastic Fabric Adapter (EFA)** | 1.42.0                      |
| **AWS OFI NCCL Plugin**          | 1.15.0                      |

## Confirm GPU Functionality

**To confirm functional GPUs:**

1. Run the following Nvidia GPU Device Query Test

```
`$` /usr/local/cuda/extras/demo_suite/deviceQuery
```

2. Confirm the Following output from the Device Query Run:

```
$ /usr/local/cuda/extras/demo_suite/deviceQuery
/usr/local/cuda/extras/demo_suite/deviceQuery Starting...

 CUDA Device Query (Runtime API)

Detected 8 CUDA Capable device(s)
...
deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.8, CUDA Runtime Version = 12.8, NumDevs = 8, Device0 = NVIDIA B200, Device1 = NVIDIA B200, Device2 = NVIDIA B200, Device3 = NVIDIA B200, Device4 = NVIDIA B200, Device5 = NVIDIA B200, Device6 = NVIDIA B200, Device7 = NVIDIA B200
Result = PASS
```

**To confirm functional NVIDIA Driver:**

1. Run the Nvidia System Management Interface

```
`$` nvidia-smi
```

2. Confirm the Following output from the System Management Interface

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.133.20             Driver Version: 570.133.20     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA B200                    Off |   00000000:51:00.0 Off |                    0 |
| N/A   32C    P0            145W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA B200                    Off |   00000000:52:00.0 Off |                    0 |
| N/A   30C    P0            140W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA B200                    Off |   00000000:62:00.0 Off |                    0 |
| N/A   31C    P0            139W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA B200                    Off |   00000000:63:00.0 Off |                    0 |
| N/A   29C    P0            139W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA B200                    Off |   00000000:75:00.0 Off |                    0 |
| N/A   31C    P0            141W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA B200                    Off |   00000000:76:00.0 Off |                    0 |
| N/A   31C    P0            141W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA B200                    Off |   00000000:86:00.0 Off |                    0 |
| N/A   32C    P0            141W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA B200                    Off |   00000000:87:00.0 Off |                    0 |
| N/A   30C    P0            138W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

**If you experience any issues with P6-B200 instances, please reach out
to AWS Support.**
