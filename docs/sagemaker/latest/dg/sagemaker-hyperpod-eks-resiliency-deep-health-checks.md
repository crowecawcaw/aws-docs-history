# Deep health

checks

SageMaker HyperPod performs _deep health checks_ on cluster instances
during the creation and update of HyperPod clusters. The deep health checks
ensure the reliability and stability of the SageMaker HyperPod clusters by thoroughly testing
the underlying hardware and infrastructure components before allowing the clusters to be
used for training machine learning models. This proactive approach helps identify and
mitigate potential issues early in the cluster lifecycle.

## List of

deep health checks done by SageMaker HyperPod

SageMaker HyperPod runs the following deep health checks.

**Instance-level deep health checks**

| Category    | Utility name                                                                                                                                                                                  | Instance type compatibility | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accelerator | GPU/NVLink count                                                                                                                                                                              | GPU                         | Verifies GPU/NVLink counts.                                                                                                                                                                                                                                                                                                                                                                       |
| Accelerator | [DCGM diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html "https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html") level 4 | GPU                         | Assesses the health and functionality of NVIDIA GPUs by running<br>DCGM (NVIDIA Data Center GPU Manager) diagnostics at level 4,<br>including additional memory tests.                                                                                                                                                                                                                            |
| Accelerator | Neuron sysfs                                                                                                                                                                                  | Trainium                    | For Trainium-powered instances, the health of the Neuron devices<br>is determined by reading counters from [Neuron sysfs](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-sysfs-user-guide.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-sysfs-user-guide.html") propagated directly by the Neuron<br>driver. |
| Accelerator | Neuron hardware check                                                                                                                                                                         | Trainium                    | Runs a training workload and verifies the results to test the hardware.                                                                                                                                                                                                                                                                                                                           |
| Accelerator | NCCOM local test                                                                                                                                                                              | Trainium                    | Evaluates the performance of collective communication operations<br>on single Trainium nodes                                                                                                                                                                                                                                                                                                      |
| Network     | EFA                                                                                                                                                                                           | GPU and Trainium            | Runs latency and bandwidth benchmarking on the attached EFA<br>device.                                                                                                                                                                                                                                                                                                                            |

**Cluster-level deep health checks**

| Category    | Utility name       | Instance type compatibility | Description                                                                                   |
| ----------- | ------------------ | --------------------------- | --------------------------------------------------------------------------------------------- |
| Accelerator | NCCL test          | GPU                         | Verifies the performance of collective communication operations<br>on multiple NVIDIA GPUs    |
| Accelerator | NCCOM cluster test | Trainium                    | Verifies the performance of collective communication operations<br>on multiple Trainium nodes |

## Logs from

the deep health checks

The following are example logs from the SageMaker HyperPod deep health checks.

**Cluster-level logs**

The cluster-level deep health check logs are stored in your CloudWatch log group at
`/aws/sagemaker/Clusters/**<cluster\_name>**/**<cluster\_id>**`

The log streams are logged at
`DeepHealthCheckResults/<log_stream_id>`.

As an example shown below, the deep health check output logs show the instance ID
that failed the checks with the cause of the failure.

```
{
    "level": "error",
    "ts": "2024-06-18T21:15:22Z",
    "msg": "Encountered FaultyInstance. Replace the Instance. Region: us-west-2, InstanceType: p4d.24xlarge. ERROR:Bandwidth has less than threshold: Expected minimum threshold :80,NCCL Test output Bw: 30"
}
```

**Instance-level logs**

The instance-level deep health check logs are stored at
`/var/log/aws/clusters/sagemaker-deep-health-check.log` on each node.
SSH into the node and open the log file by running the following command.

```
cat /var/log/aws/clusters/sagemaker-deep-health-check.log
```

The following is an example output of the hardware stress, [NVIDIA DCGM](https://developer.nvidia.com/dcgm "https://developer.nvidia.com/dcgm") stress, and EFA
connectivity test.

```
# Hardware Stress Test output

2024-08-20T21:53:58Z info Executing Hardware stress check with command: stress-ng, and args: [--cpu 32 --vm 2 --hdd 1 --fork 8 --switch 4 --timeout 60 --metrics]

2024-08-20T21:54:58Z info stress-ng success

2024-08-20T21:54:58Z    info    GpuPci Count check success

# DCGM Stress Test

2024-08-20T22:25:02Z    info    DCGM diagnostic health summary: dcgmCheckLevel: 0 dcgmVersion: 3.3.7 gpuDriverVersion: 535.183.01, gpuDeviceIds: [2237] replacementRequired: false rebootRequired:false

# EFA Loopback Test

2024-08-20T22:26:28Z    info    EFA Loopback check passed for device: rdmap0s29 . Output summary is MaxBw: 58.590000, AvgBw: 32.420000, MaxTypicalLat: 30.870000, MinTypicalLat: 20.080000, AvgLat: 21.630000
```

The following is an example output of the NCCL connectivity test.

```
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong

#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)

           8             2     float     sum      -1    353.9    0.00    0.00      0    304.2    0.00    0.00      0
          16             4     float     sum      -1    352.8    0.00    0.00      0    422.9    0.00    0.00      0
          32             8     float     sum      -1    520.0    0.00    0.00      0    480.3    0.00    0.00      0
          64            16     float     sum      -1    563.0    0.00    0.00      0    416.1    0.00    0.00      0
         128            32     float     sum      -1    245.1    0.00    0.00      0    308.4    0.00    0.00      0
         256            64     float     sum      -1    310.8    0.00    0.00      0    304.9    0.00    0.00      0
         512           128     float     sum      -1    304.9    0.00    0.00      0    300.8    0.00    0.00      0
        1024           256     float     sum      -1    509.3    0.00    0.00      0    495.4    0.00    0.00      0
        2048           512     float     sum      -1    530.3    0.00    0.00      0    420.0    0.00    0.00      0
        4096          1024     float     sum      -1    391.2    0.01    0.01      0    384.5    0.01    0.01      0
        8192          2048     float     sum      -1    328.5    0.02    0.02      0    253.2    0.03    0.03      0
       16384          4096     float     sum      -1    497.6    0.03    0.03      0    490.9    0.03    0.03      0
       32768          8192     float     sum      -1    496.7    0.07    0.07      0    425.0    0.08    0.08      0
       65536         16384     float     sum      -1    448.0    0.15    0.15      0    501.0    0.13    0.13      0
      131072         32768     float     sum      -1    577.4    0.23    0.23      0    593.4    0.22    0.22      0
      262144         65536     float     sum      -1    757.8    0.35    0.35      0    721.6    0.36    0.36      0
      524288        131072     float     sum      -1   1057.1    0.50    0.50      0   1019.1    0.51    0.51      0
     1048576        262144     float     sum      -1   1460.5    0.72    0.72      0   1435.6    0.73    0.73      0
     2097152        524288     float     sum      -1   2450.6    0.86    0.86      0   2583.1    0.81    0.81      0
     4194304       1048576     float     sum      -1   4344.5    0.97    0.97      0   4419.3    0.95    0.95      0
     8388608       2097152     float     sum      -1   8176.5    1.03    1.03      0   8197.8    1.02    1.02      0
    16777216       4194304     float     sum      -1    15312    1.10    1.10      0    15426    1.09    1.09      0
    33554432       8388608     float     sum      -1    30149    1.11    1.11      0    29941    1.12    1.12      0
    67108864      16777216     float     sum      -1    57819    1.16    1.16      0    58635    1.14    1.14      0
   134217728      33554432     float     sum      -1   115699    1.16    1.16      0   115331    1.16    1.16      0
   268435456      67108864     float     sum      -1   227507    1.18    1.18      0   228047    1.18    1.18      0
   536870912     134217728     float     sum      -1   453751    1.18    1.18      0   456595    1.18    1.18      0
  1073741824     268435456     float     sum      -1   911719    1.18    1.18      0   911808    1.18    1.18      0
  2147483648     536870912     float     sum      -1  1804971    1.19    1.19      0  1806895    1.19    1.19      0

2024-08-20T16:22:43.831-07:00

# Out of bounds values : 0 OK

2024-08-20T16:22:43.831-07:00

# Avg bus bandwidth    : 0.488398

2024-08-20T23:22:43Z    info    Nccl test successful. Summary: NcclMaxAlgoBw: 1.190000, NcclAvgAlgoBw: 0.488398, NcclThresholdAlgoBw: 1.180000, NcclOutOfBoundError: OK, NcclOperations: all_reduce_perf, NcclTotalDevices: 2, NcclNodes: 2, NcclClusterMessage:
```
