# Software requirements for P6 instances

Below are the detailed requirements for running DLAMI on P6 instances.

###### Topics

- [P6-B200 requirements](#dlami-support-p6-b200 "#dlami-support-p6-b200")
- [P6e-GB200 requirements](#dlami-support-p6e-gb200 "#dlami-support-p6e-gb200")
- [P6-B300 requirements](#dlami-support-p6-b300 "#dlami-support-p6-b300")
- [GPU Functionality Test](#dlami-p6-testing "#dlami-p6-testing")

## P6-B200 requirements

The following software is required to operate P6-B200 instances:

| Software                         | Minimum Version Requirement |
| -------------------------------- | --------------------------- |
| **Nvidia CUDA Toolkit**          | 12.8                        |
| **Nvidia Driver**                | R570                        |
| **NVLINK 5**                     | R570                        |
| **Linux Kernel**                 | 6.1                         |
| **Elastic Fabric Adapter (EFA)** | 1.41.0                      |
| **AWS OFI NCCL Plugin**          | 1.15.0                      |

## P6e-GB200 requirements

The following software is required to operate P6e-GB200 instances:

| Software                         | Minimum Version Requirement |
| -------------------------------- | --------------------------- |
| **Nvidia CUDA Toolkit**          | 12.8                        |
| **Nvidia Driver**                | R570                        |
| **Linux Kernel**                 | 6.12                        |
| **Elastic Fabric Adapter (EFA)** | 1.42.0                      |
| **AWS OFI NCCL Plugin**          | 1.15.0                      |

## P6-B300 requirements

The following software is required to operate P6-B300 instances:

| Software                         | Minimum Version Requirement |
| -------------------------------- | --------------------------- |
| **Nvidia CUDA Toolkit**          | 13.0                        |
| **Nvidia Driver**                | R580                        |
| **NVLINK 5**                     | R580                        |
| **Linux Kernel**                 | 6.1                         |
| **Elastic Fabric Adapter (EFA)** | 1.44.0                      |
| **AWS OFI NCCL Plugin**          | 1.17.1                      |

## Confirm GPU Functionality

**To confirm functional GPUs:**

1. Run the following Nvidia GPU Device Query Test.

```
`$` /usr/local/cuda/extras/demo_suite/deviceQuery
```

2. Confirm the output from the Device Query Test. The following is example output for p6-B200.

```
/usr/local/cuda/extras/demo_suite/deviceQuery Starting...

 CUDA Device Query (Runtime API)

Detected 8 CUDA Capable device(s)
...
deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.8, CUDA Runtime Version = 12.8, NumDevs = 8, Device0 = NVIDIA B200, Device1 = NVIDIA B200, Device2 = NVIDIA B200, Device3 = NVIDIA B200, Device4 = NVIDIA B200, Device5 = NVIDIA B200, Device6 = NVIDIA B200, Device7 = NVIDIA B200
Result = PASS
```

**To confirm functional NVIDIA Driver:**

1. Run the Nvidia System Management Interface.

```
`$` nvidia-smi
```

2. Confirm the output from the System Management Interface. The following is example output for p6-B200.

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

###### Note

If you experience any issues, contact AWS Support.
