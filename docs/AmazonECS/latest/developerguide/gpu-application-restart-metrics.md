

# GPU application restart metrics
<a name="gpu-application-restart-metrics"></a>

For Amazon ECS Managed Instances running NVIDIA GPU-enabled Amazon EC2 instance types, the `TaskGPURestartAppXidCount` and `ContainerGPURestartAppXidCount` metrics count NVIDIA Xid errors whose immediate-action resolution bucket is `RESTART_APP`. These Xids indicate application-level faults where NVIDIA recommends restarting the affected application rather than the instance. Use these metrics to detect transient GPU faults affecting a specific task or container without implying underlying hardware failure.

The following Xid codes are included. For the complete list and descriptions, see the [NVIDIA Xid Errors](https://docs.nvidia.com/deploy/xid-errors/index.html) documentation.



| Xid | Error type | 
| --- | --- | 
| 8 | GPU stopped processing | 
| 11 | Invalid or corrupted push buffer stream | 
| 13 | Graphics Engine Exception | 
| 25 | ECC page retirement in progress | 
| 31 | GPU memory page fault | 
| 32 | Invalid or corrupted push buffer stream | 
| 39 | Bus error | 
| 40 | Video processor exception | 
| 41 | Unexpected fault | 
| 60 | Video processor exception | 
| 68 | Video processor exception | 
| 69 | Graphics Engine class error | 
| 70 | CE user channel error | 
| 71 | GPU semaphore timeout | 
| 72 | GPU semaphore access error | 
| 75 | Inforom page blacklist event | 
| 76 | Display engine error | 
| 77 | Display engine error | 
| 80 | Corrupted data sent to GPU | 
| 82 | NVJPG error | 
| 83 | NVDEC error | 
| 84 | Mismatched SLI link | 
| 85 | Resource constraint | 
| 86 | Operating system error | 
| 88 | NVDEC error | 
| 89 | NVENC error | 
| 94 | Contained ECC error | 
| 96 | NVDEC error | 
| 97 | NVDEC error | 
| 98 | NVDEC error | 
| 99 | NVJPG error | 
| 100 | NVJPG error | 
| 101 | NVJPG error | 
| 102 | NVJPG error | 
| 103 | GSP RPC timeout | 
| 104 | GSP halt | 
| 105 | GSP error | 
| 126 | C2C NVLink replay error | 
| 127 | C2C NVLink error | 
| 128 | NVLink error | 
| 129 | NVLink recovery error | 
| 130 | NVLink fatal error | 
| 131 | NVLink non-fatal error | 
| 132 | NVLink error | 
| 133 | NVLink error | 
| 134 | NVLink error | 
| 135 | NVLink error | 
| 139 | GPU memory page retirement recording event | 