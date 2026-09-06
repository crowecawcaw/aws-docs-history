

# Exported metrics reference
<a name="sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference"></a>

The following sections present comprehensive lists of metrics exported from SageMaker HyperPod to Amazon Managed Service for Prometheus upon the successful configuration of the CloudFormation stack for SageMaker HyperPod observability. You can start monitoring these metrics visualized in the Amazon Managed Grafana dashboards.

## Slurm exporter dashboard
<a name="sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference-slurm-exporter"></a>

Provides visualized information of Slurm clusters on SageMaker HyperPod.

**Types of metrics**
+ **Cluster Overview:** Displaying the total number of nodes, jobs, and their states.
+ **Job Metrics:** Visualizing job counts and states over time.
+ **Node Metrics:** Showing node states, allocation, and available resources.
+ **Partition Metrics:** Monitoring partition-specific metrics such as CPU, memory, and GPU utilization.
+ **Job Efficiency:** Calculating job efficiency based on resources utilized.

**List of metrics**


| Metric name | Description | 
| --- | --- | 
| slurm\_job\_count | Total number of jobs in the Slurm cluster | 
| slurm\_job\_state\_count | Count of jobs in each state (e.g., running, pending, completed) | 
| slurm\_node\_count  | Total number of nodes in the Slurm cluster | 
| slurm\_node\_state\_count  | Count of nodes in each state (e.g., idle, alloc, mix) | 
| slurm\_partition\_node\_count  | Count of nodes in each partition | 
| slurm\_partition\_job\_count  | Count of jobs in each partition | 
| slurm\_partition\_alloc\_cpus  | Total number of allocated CPUs in each partition | 
| slurm\_partition\_free\_cpus  | Total number of available CPUs in each partition | 
| slurm\_partition\_alloc\_memory  | Total allocated memory in each partition | 
| slurm\_partition\_free\_memory  | Total available memory in each partition | 
| slurm\_partition\_alloc\_gpus  | Total allocated GPUs in each partition | 
| slurm\_partition\_free\_gpus  | Total available GPUs in each partition | 

## Node exporter dashboard
<a name="sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference-node-exporter"></a>

Provides visualized information of system metrics collected by the [Prometheus node exporter](https://github.com/prometheus/node_exporter) from the HyperPod cluster nodes.

**Types of metrics**
+ **System overview:** Displaying CPU load averages and memory usage.
+ **Memory metrics:** Visualizing memory utilization including total memory, free memory, and swap space.
+ **Disk usage:** Monitoring disk space utilization and availability.
+ **Network traffic:** Showing network bytes received and transmitted over time.
+ **File system metrics:** Analyzing file system usage and availability.
+ **Disk I/O metrics:** Visualizing disk read and write activity.

**List of metrics**

For a complete list of metrics exported, see the [Node exporter ](https://github.com/prometheus/node_exporter?tab=readme-ov-file#enabled-by-default) and [procfs](https://github.com/prometheus/procfs?tab=readme-ov-file) GitHub repositories. The following table shows a subset of the metrics that provides insights into system resource utilization such as CPU load, memory usage, disk space, and network activity.


| Metric name | Description | 
| --- | --- | 
|  node\_load1  | 1-minute load average | 
|  node\_load5  | 5-minute load average | 
|  node\_load15  | 15-minute load average | 
|  node\_memory\_MemTotal  | Total system memory | 
|  node\_memory\_MemFree  | Free system memory | 
|  node\_memory\_MemAvailable  | Available memory for allocation to processes | 
|  node\_memory\_Buffers  | Memory used by the kernel for buffering | 
|  node\_memory\_Cached  | Memory used by the kernel for caching file system data | 
|  node\_memory\_SwapTotal  | Total swap space available | 
|  node\_memory\_SwapFree  | Free swap space | 
|  node\_memory\_SwapCached  | Memory that once was swapped out, is swapped back in but still in swap | 
|  node\_filesystem\_avail\_bytes  | Available disk space in bytes | 
|  node\_filesystem\_size\_bytes  | Total disk space in bytes | 
|  node\_filesystem\_free\_bytes  | Free disk space in bytes | 
|  node\_network\_receive\_bytes  | Network bytes received | 
|  node\_network\_transmit\_bytes  | Network bytes transmitted | 
|  node\_disk\_read\_bytes  | Disk bytes read | 
|  node\_disk\_written\_bytes  | Disk bytes written | 

## NVIDIA DCGM exporter dashboard
<a name="sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference-nvidia-dcgm-exporter"></a>

Provides visualized information of NVIDIA GPU metrics collected by the [NVIDIA DCGM exporter](https://github.com/NVIDIA/dcgm-exporter).

**Types of metrics**
+ **GPU Overview:** Displaying GPU utilization, temperatures, power usage, and memory usage. 
+ **Temperature Metrics:** Visualizing GPU temperatures over time. 
+ **Power Usage:** Monitoring GPU power draw and power usage trends. 
+ **Memory Utilization:** Analyzing GPU memory usage including used, free, and total memory. 
+ **Fan Speed:** Showing GPU fan speeds and variations. 
+ **ECC Errors:** Tracking GPU memory ECC errors and pending errors.

**List of metrics**

The following table shows a list of the metrics that provides insights into the NVIDIA GPU health and performance, including clock frequencies, temperatures, power usage, memory utilization, fan speeds, and error metrics.


| Metric name | Description | 
| --- | --- | 
|  DCGM\_FI\_DEV\_SM\_CLOCK  | SM clock frequency (in MHz) | 
|  DCGM\_FI\_DEV\_MEM\_CLOCK  | Memory clock frequency (in MHz) | 
|  DCGM\_FI\_DEV\_MEMORY\_TEMP  | Memory temperature (in C) | 
|  DCGM\_FI\_DEV\_GPU\_TEMP  | GPU temperature (in C) | 
|  DCGM\_FI\_DEV\_POWER\_USAGE  | Power draw (in W) | 
|  DCGM\_FI\_DEV\_TOTAL\_ENERGY\_CONSUMPTION  | Total energy consumption since boot (in mJ) | 
|  DCGM\_FI\_DEV\_PCIE\_REPLAY\_COUNTER  | Total number of PCIe retries | 
|  DCGM\_FI\_DEV\_MEM\_COPY\_UTIL  | Memory utilization (in %) | 
|  DCGM\_FI\_DEV\_ENC\_UTIL  | Encoder utilization (in %) | 
|  DCGM\_FI\_DEV\_DEC\_UTIL  | Decoder utilization (in %) | 
|  DCGM\_FI\_DEV\_XID\_ERRORS  | Value of the last XID error encountered | 
|  DCGM\_FI\_DEV\_FB\_FREE  | Frame buffer memory free (in MiB) | 
|  DCGM\_FI\_DEV\_FB\_USED  | Frame buffer memory used (in MiB) | 
|  DCGM\_FI\_DEV\_NVLINK\_BANDWIDTH\_TOTAL  | Total number of NVLink bandwidth counters for all lanes | 
|  DCGM\_FI\_DEV\_VGPU\_LICENSE\_STATUS  | vGPU License status | 
|  DCGM\_FI\_DEV\_UNCORRECTABLE\_REMAPPED\_ROWS  | Number of remapped rows for uncorrectable errors | 
|  DCGM\_FI\_DEV\_CORRECTABLE\_REMAPPED\_ROWS  | Number of remapped rows for correctable errors | 
|  DCGM\_FI\_DEV\_ROW\_REMAP\_FAILURE  | Whether remapping of rows has failed | 

## EFA metrics dashboard
<a name="sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference-efa-exporter"></a>

Provides visualized information of the metrics from [Amazon Elastic Fabric Adapter (EFA)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) equipped on P instances collected by the [EFA node exporter](https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation_and_observability/3.efa-node-exporter/README.md).

**Types of metrics**
+ **EFA error metrics:** Visualizing errors such as allocation errors, command errors, and memory map errors.
+ **EFA network traffic:** Monitoring received and transmitted bytes, packets, and work requests.
+ **EFA RDMA performance:** Analyzing RDMA read and write operations, including bytes transferred and error rates.
+ **EFA port lifespan:** Displaying the lifespan of EFA ports over time.
+ **EFA keep-alive packets:** Tracking the number of keep-alive packets received.

**List of metrics**

The following table shows a list of the metrics that provides insights into various aspects of EFA operation, including errors, completed commands, network traffic, and resource utilization.


| Metric name | Description | 
| --- | --- | 
|  node\_amazonefa\_info  | Non-numeric data from /sys/class/infiniband/, value is always 1. | 
|  node\_amazonefa\_lifespan  | Lifespan of the port | 
|  node\_amazonefa\_rdma\_read\_bytes  | Number of bytes read with RDMA | 
|  node\_amazonefa\_rdma\_read\_resp\_bytes  | Number of read response bytes with RDMA | 
|  node\_amazonefa\_rdma\_read\_wr\_err  | Number of read write errors with RDMA | 
|  node\_amazonefa\_rdma\_read\_wrs  | Number of read rs with RDMA | 
|  node\_amazonefa\_rdma\_write\_bytes  | Number of bytes written with RDMA | 
|  node\_amazonefa\_rdma\_write\_recv\_bytes  | Number of bytes written and received with RDMA | 
|  node\_amazonefa\_rdma\_write\_wr\_err  | Number of bytes written with error RDMA | 
|  node\_amazonefa\_rdma\_write\_wrs  | Number of bytes written wrs RDMA | 
|  node\_amazonefa\_recv\_bytes  | Number of bytes received | 
|  node\_amazonefa\_recv\_wrs  | Number of bytes received wrs | 
|  node\_amazonefa\_rx\_bytes  | Number of bytes received | 
|  node\_amazonefa\_rx\_drops  | Number of packets dropped | 
|  node\_amazonefa\_rx\_pkts  | Number of packets received | 
|  node\_amazonefa\_send\_bytes  | Number of bytes sent | 
|  node\_amazonefa\_send\_wrs  | Number of wrs sent | 
|  node\_amazonefa\_tx\_bytes  | Number of bytes transmitted | 
|  node\_amazonefa\_tx\_pkts  | Number of packets transmitted | 

## FSx for Lustre metrics dashboard
<a name="sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference-fsx-exporter"></a>

Provides visualized information of the [metrics from Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html) file system collected by [Amazon CloudWatch](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html).

**Note**  
The Grafana FSx for Lustre dashboard utilizes Amazon CloudWatch as its data source, which differs from the other dashboards that you have configured to use Amazon Managed Service for Prometheus. To ensure accurate monitoring and visualization of metrics related to your FSx for Lustre file system, configure the FSx for Lustre dashboard to use Amazon CloudWatch as the data source, specifying the same AWS Region where your FSx for Lustre file system is deployed.

**Types of metrics**
+ **DataReadBytes:** The number of bytes for file system read operations.
+ **DataWriteBytes:** The number of bytes for file system write operations.
+ **DataReadOperations:** The number of read operations.
+ **DataWriteOperations:** The number of write operations.
+ **MetadataOperations:** The number of meta data operations.
+ **FreeDataStorageCapacity:** The amount of available storage capacity.