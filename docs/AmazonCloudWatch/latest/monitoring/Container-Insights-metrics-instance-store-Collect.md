# Collect Amazon EC2 instance store 
 volume NVMe driver metrics

For CloudWatch agent to collect AWS NVMe driver metrics for instance store volumes attached to 
 an Amazon EC2 instance, add the `diskio` section inside the `metrics_collected` 
 section of the CloudWatch agent configuration file.

Additionally, the CloudWatch agent binary requires `ioctl` permissions for NVMe driver 
 devices to collect metrics from attached instance store volumes.

The following metrics can be collected. 



| Metric | Metric name in CloudWatch | Description |
| --- | --- | --- |
| `instance_store_total_read_ops` | `diskio_instance_store_total_read_ops` | The total number of completed read operations. |
| `instance_store_total_write_ops` | `diskio_instance_store_total_write_ops` | The total number of completed write operations. |
| `instance_store_total_read_bytes` | `diskio_instance_store_total_read_bytes` | The total number of read bytes transferred. |
| `instance_store_total_write_bytes` | `diskio_instance_store_total_write_bytes` | The total number of write bytes transferred. |
| `instance_store_total_read_time` | `diskio_instance_store_total_read_time` | The total time spent, in microseconds, by all completed read operations. |
| `instance_store_total_write_time` | `diskio_instance_store_total_write_time` | The total time spent, in microseconds, by all completed write operations. |
| `instance_store_performance_exceeded_iops` | `diskio_instance_store_performance_exceeded_iops` | The total time, in microseconds, that IOPS demand exceeded the volume's IOPS maximum performance. |
| `instance_store_performance_exceeded_tp` | `diskio_instance_store_performance_exceeded_tp` | The total time, in microseconds, that throughput demand exceeded the volume's maximum throughput performance. |
| `instance_store_volume_queue_length` | `diskio_instance_store_volume_queue_length` | The number of read and write operations waiting to be completed. |
