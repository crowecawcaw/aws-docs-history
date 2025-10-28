# Exported metrics reference

The following sections present comprehensive lists of metrics exported from
SageMaker HyperPod to Amazon Managed Service for Prometheus upon the successful configuration of the AWS CloudFormation stack for
SageMaker HyperPod observability. You can start monitoring these metrics visualized in the
Amazon Managed Grafana dashboards.

## Slurm exporter dashboard

Provides visualized information of Slurm clusters on SageMaker HyperPod.

**Types of metrics**

- **Cluster Overview:** Displaying the total
  number of nodes, jobs, and their states.
- **Job Metrics:** Visualizing job counts and
  states over time.
- **Node Metrics:** Showing node states,
  allocation, and available resources.
- **Partition Metrics:** Monitoring
  partition-specific metrics such as CPU, memory, and GPU utilization.
- **Job Efficiency:** Calculating job
  efficiency based on resources utilized.

**List of metrics**

| Metric name                               | Description                                                            |
| ----------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slurm_job_count`                         | Total number of jobs in the Slurm cluster                              |
| `slurm_job_state_count`                   | Count of jobs in each state (e.g., running, pending, completed)        |
| `slurm_node_count`                        | Total number of nodes in the Slurm cluster                             |
| `slurm_node_state_count`                  | Count of nodes in each state (e.g., idle, alloc, mix)                  |
| `slurm_partition_node_count`              | Count of nodes in each partition                                       |
| `slurm_partition_job_count`               | Count of jobs in each partition                                        |
| `slurm_partition_alloc_cpus`              | Total number of allocated CPUs in each partition                       |
| `slurm_partition_free_cpus`               | Total number of available CPUs in each partition                       |
| `slurm_partition_alloc_memory`            | Total allocated memory in each partition                               |
| `slurm_partition_free_memory`             | Total available memory in each partition                               |
| `slurm_partition_alloc_gpus`              | Total allocated GPUs in each partition                                 |
| `slurm_partition_free_gpus`               | Total available GPUs in each partition                                 | ## Node exporter dashboard Provides visualized information of system metrics collected by the [Prometheus node exporter](https://github.com/prometheus/node_exporter "https://github.com/prometheus/node_exporter") from the HyperPod cluster nodes. **Types of metrics** <br>• **System overview:** Displaying CPU load averages and memory usage. <br>• **Memory metrics:** Visualizing memory utilization including total memory, free memory, and swap space. <br>• **Disk usage:** Monitoring disk space utilization and availability. <br>• **Network traffic:** Showing network bytes received and transmitted over time. <br>• **File system metrics:** Analyzing file system usage and availability. <br>• **Disk I/O metrics:** Visualizing disk read and write activity. **List of metrics** For a complete list of metrics exported, see the [Node exporter](https://github.com/prometheus/node_exporter?tab=readme-ov-file#enabled-by-default "https://github.com/prometheus/node_exporter?tab=readme-ov-file#enabled-by-default") and [procfs](https://github.com/prometheus/procfs?tab=readme-ov-file "https://github.com/prometheus/procfs?tab=readme-ov-file") GitHub repositories. The following table shows a subset of the metrics that provides insights into system resource utilization such as CPU load, memory usage, disk space, and network activity. |
| Metric name                               | Description                                                            |
| ---                                       | ---                                                                    |
| `node_load1`                              | 1-minute load average                                                  |
| `node_load5`                              | 5-minute load average                                                  |
| `node_load15`                             | 15-minute load average                                                 |
| `node_memory_MemTotal`                    | Total system memory                                                    |
| `node_memory_MemFree`                     | Free system memory                                                     |
| `node_memory_MemAvailable`                | Available memory for allocation to processes                           |
| `node_memory_Buffers`                     | Memory used by the kernel for buffering                                |
| `node_memory_Cached`                      | Memory used by the kernel for caching file system data                 |
| `node_memory_SwapTotal`                   | Total swap space available                                             |
| `node_memory_SwapFree`                    | Free swap space                                                        |
| `node_memory_SwapCached`                  | Memory that once was swapped out, is swapped back in but still in swap |
| `node_filesystem_avail_bytes`             | Available disk space in bytes                                          |
| `node_filesystem_size_bytes`              | Total disk space in bytes                                              |
| `node_filesystem_free_bytes`              | Free disk space in bytes                                               |
| `node_network_receive_bytes`              | Network bytes received                                                 |
| `node_network_transmit_bytes`             | Network bytes transmitted                                              |
| `node_disk_read_bytes`                    | Disk bytes read                                                        |
| `node_disk_written_bytes`                 | Disk bytes written                                                     | ## NVIDIA DCGM exporter dashboard Provides visualized information of NVIDIA GPU metrics collected by the [NVIDIA DCGM exporter](https://github.com/NVIDIA/dcgm-exporter "https://github.com/NVIDIA/dcgm-exporter"). **Types of metrics** <br>• **GPU Overview:** Displaying GPU utilization, temperatures, power usage, and memory usage. <br>• **Temperature Metrics:** Visualizing GPU temperatures over time. <br>• **Power Usage:** Monitoring GPU power draw and power usage trends. <br>• **Memory Utilization:** Analyzing GPU memory usage including used, free, and total memory. <br>• **Fan Speed:** Showing GPU fan speeds and variations. <br>• **ECC Errors:** Tracking GPU memory ECC errors and pending errors. **List of metrics** The following table shows a list of the metrics that provides insights into the NVIDIA GPU health and performance, including clock frequencies, temperatures, power usage, memory utilization, fan speeds, and error metrics.                                                                                                                                                                                                                                                                                                                                                                                                |
| Metric name                               | Description                                                            |
| ---                                       | ---                                                                    |
| `DCGM_FI_DEV_SM_CLOCK`                    | SM clock frequency (in MHz)                                            |
| `DCGM_FI_DEV_MEM_CLOCK`                   | Memory clock frequency (in MHz)                                        |
| `DCGM_FI_DEV_MEMORY_TEMP`                 | Memory temperature (in C)                                              |
| `DCGM_FI_DEV_GPU_TEMP`                    | GPU temperature (in C)                                                 |
| `DCGM_FI_DEV_POWER_USAGE`                 | Power draw (in W)                                                      |
| `DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION`    | Total energy consumption since boot (in mJ)                            |
| `DCGM_FI_DEV_PCIE_REPLAY_COUNTER`         | Total number of PCIe retries                                           |
| `DCGM_FI_DEV_MEM_COPY_UTIL`               | Memory utilization (in %)                                              |
| `DCGM_FI_DEV_ENC_UTIL`                    | Encoder utilization (in %)                                             |
| `DCGM_FI_DEV_DEC_UTIL`                    | Decoder utilization (in %)                                             |
| `DCGM_FI_DEV_XID_ERRORS`                  | Value of the last XID error encountered                                |
| `DCGM_FI_DEV_FB_FREE`                     | Frame buffer memory free (in MiB)                                      |
| `DCGM_FI_DEV_FB_USED`                     | Frame buffer memory used (in MiB)                                      |
| `DCGM_FI_DEV_NVLINK_BANDWIDTH_TOTAL`      | Total number of NVLink bandwidth counters for all lanes                |
| `DCGM_FI_DEV_VGPU_LICENSE_STATUS`         | vGPU License status                                                    |
| `DCGM_FI_DEV_UNCORRECTABLE_REMAPPED_ROWS` | Number of remapped rows for uncorrectable errors                       |
| `DCGM_FI_DEV_CORRECTABLE_REMAPPED_ROWS`   | Number of remapped rows for correctable errors                         |
| `DCGM_FI_DEV_ROW_REMAP_FAILURE`           | Whether remapping of rows has failed                                   | ## EFA metrics dashboard Provides visualized information of the metrics from [Amazon Elastic Fabric Adapter (EFA)](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") equipped on P instances collected by the [EFA node exporter](https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation_and_observability/3.efa-node-exporter/README.md "https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation_and_observability/3.efa-node-exporter/README.md"). **Types of metrics** <br>• **EFA error metrics:** Visualizing errors such as allocation errors, command errors, and memory map errors. <br>• **EFA network traffic:** Monitoring received and transmitted bytes, packets, and work requests. <br>• **EFA RDMA performance:** Analyzing RDMA read and write operations, including bytes transferred and error rates. <br>• **EFA port lifespan:** Displaying the lifespan of EFA ports over time. <br>• **EFA keep-alive packets:** Tracking the number of keep-alive packets received. **List of metrics** The following table shows a list of the metrics that provides insights into various aspects of EFA operation, including errors, completed commands, network traffic, and resource utilization.                                                                             |
| Metric name                               | Description                                                            |
| ---                                       | ---                                                                    |
| `node_amazonefa_info`                     | Non-numeric data from /sys/class/infiniband/, value is always 1.       |
| `node_amazonefa_lifespan`                 | Lifespan of the port                                                   |
| `node_amazonefa_rdma_read_bytes`          | Number of bytes read with RDMA                                         |
| `node_amazonefa_rdma_read_resp_bytes`     | Number of read response bytes with RDMA                                |
| `node_amazonefa_rdma_read_wr_err`         | Number of read write errors with RDMA                                  |
| `node_amazonefa_rdma_read_wrs`            | Number of read rs with RDMA                                            |
| `node_amazonefa_rdma_write_bytes`         | Number of bytes written with RDMA                                      |
| `node_amazonefa_rdma_write_recv_bytes`    | Number of bytes written and received with RDMA                         |
| `node_amazonefa_rdma_write_wr_err`        | Number of bytes written with error RDMA                                |
| `node_amazonefa_rdma_write_wrs`           | Number of bytes written wrs RDMA                                       |
| `node_amazonefa_recv_bytes`               | Number of bytes received                                               |
| `node_amazonefa_recv_wrs`                 | Number of bytes received wrs                                           |
| `node_amazonefa_rx_bytes`                 | Number of bytes received                                               |
| `node_amazonefa_rx_drops`                 | Number of packets dropped                                              |
| `node_amazonefa_rx_pkts`                  | Number of packets received                                             |
| `node_amazonefa_send_bytes`               | Number of bytes sent                                                   |
| `node_amazonefa_send_wrs`                 | Number of wrs sent                                                     |
| `node_amazonefa_tx_bytes`                 | Number of bytes transmitted                                            |
| `node_amazonefa_tx_pkts`                  | Number of packets transmitted                                          | ## FSx for Lustre metrics dashboard Provides visualized information of the [metrics from Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/monitoring-cloudwatch.md "../../../fsx/latest/LustreGuide/monitoring-cloudwatch.md") file system collected by [Amazon CloudWatch](../../../fsx/latest/LustreGuide/monitoring-cloudwatch.md "../../../fsx/latest/LustreGuide/monitoring-cloudwatch.md"). ###### Note The Grafana FSx for Lustre dashboard utilizes Amazon CloudWatch as its data source, which differs from the other dashboards that you have configured to use Amazon Managed Service for Prometheus. To ensure accurate monitoring and visualization of metrics related to your FSx for Lustre file system, configure the FSx for Lustre dashboard to use Amazon CloudWatch as the data source, specifying the same AWS Region where your FSx for Lustre file system is deployed. **Types of metrics** <br>• **DataReadBytes:** The number of bytes for file system read operations. <br>• **DataWriteBytes:** The number of bytes for file system write operations. <br>• **DataReadOperations:** The number of read operations. <br>• **DataWriteOperations:** The number of write operations. <br>• **MetadataOperations:** The number of meta data operations. <br>• **FreeDataStorageCapacity:** The amount of available storage capacity.                |
