# Amazon EBS detailed performance statistics

Amazon EBS NVMe block devices vend real-time, high-resolution I/O performance statistics
for Amazon EBS volumes attached to Nitro-based Amazon EC2 instances. These statistics are presented
as aggregated counters that are retained for the duration of the volume's attachment to
the instance. The statistics provide details about the cumulative number of operations,
bytes sent and received, and time spent on read and write I/O operations. Additionally,
the statistics include histograms for read and write I/O operations, and the total time
your application has exceeded the EBS volume or attached instance's provisioned IOPS or
throughput limits.

You can collect these statistics at a granularity of up to 1 second intervals. If
requests are made more frequently than 1 second intervals, the NVMe driver might queue
the requests, along with other admin commands, to be processed at a later time.

###### Considerations

- The statistics are supported for all Amazon EBS volume types.
- The statistics are supported only for volumes attached to [instances built on the
  AWS Nitro System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md").
- The statistics are available for Multi-Attach enabled volumes. When viewing
  statistics for a Multi-Attach enabled volume, the statistics are specific to
  that instance attachment, and reflect only that instance's usage.
- The statistics are available at no additional cost.

## Statistics

The Amazon EBS NVMe block device vends the following statistics:

| Statistic name                               | Full name                                                        | Type          | Description                                                                                                                         |
| -------------------------------------------- | ---------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `total_read_ops`                             | Total read operations                                            | Counter       | The total number of completed read operations.                                                                                      |
| `total_write_ops`                            | Total write operations                                           | Counter       | The total number of completed write operations.                                                                                     |
| `total_read_bytes`                           | Total read bytes                                                 | Counter       | The total number of read bytes transferred.                                                                                         |
| `total_write_bytes`                          | Total write bytes                                                | Counter       | The total number of write bytes transferred.                                                                                        |
| `total_read_time`                            | Total read time                                                  | Counter       | The total time spent, in microseconds, by all completed read operations.                                                            |
| `total_write_time`                           | Total write time                                                 | Counter       | The total time spent, in microseconds, by all completed write operations.                                                           |
| `ebs_volume_performance_exceeded_iops`       | Total time demand exceeded volume provisioned IOPS               | Counter       | The total time, in microseconds, that IOPS demand exceeded the volume's provisioned<br>IOPS performance.                            |
| `ebs_volume_performance_exceeded_tp`         | Total time demand exceeded volume provisioned throughput         | Counter       | The total time, in microseconds, that throughput demand exceeded the volume's<br>provisioned throughput performance.                |
| `ec2_instance_ebs_performance_exceeded_iops` | Total time demand exceeded EC2 instance's IOPS performance       | Counter       | The total time, in microseconds, that the EBS volume exceeded the attached Amazon EC2<br>instance's maximum IOPS performance.       |
| `ec2_instance_ebs_performance_exceeded_tp`   | Total time demand exceeded EC2 instance's throughput performance | Counter       | The total time, in microseconds, that the EBS volume exceeded the attached Amazon EC2<br>instance's maximum throughput performance. |
| `volume_queue_length`                        | Volume queue length                                              | Point in time | The number of read and write operations waiting to be completed.                                                                    |
| `read_io_latency_histogram`                  | Read I/O histogram                                               | Histogram \*  | The number of read operations completed within each latency bin, in microseconds.                                                   |
| `write_io_latency_histogram`                 | Write I/O histogram                                              | Histogram \*  | The number of write operations completed within each latency bin, in microseconds.                                                  |

###### Note

\* Histogram statistics represent only I/O operations that have completed successfully. Stalled or
impaired I/O operations are not included, but will be evident in the `volume_queue_length`
statistics, which is presented as a point-in-time statistic.

## Accessing the statistics

The statistics must be accessed directly from the instance to which the Amazon EBS volume is attached.
You can access the statistics using one of the following methods.

Amazon CloudWatch
You can configure the Amazon CloudWatch agent to collect the statistics from your instance and
make them available as custom metrics in CloudWatch. You can then use the metrics in CloudWatch to
analyze I/O patterns, track performance trends, create custom dashboards, and set up
automated alarms based on performance thresholds.

For more information about configuring the CloudWatch agent, see the following:

- [Create the CloudWatch agent configuration file](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md")
- [Collect Amazon EBS NVMe driver metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EBS-Collect.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EBS-Collect.md")

With the Amazon CloudWatch Observability EKS add-on version `4.1.0` and later, the
statistics are automatically collected when the Amazon EBS CSI driver metrics are enabled. For
more information, see [Amazon EBS NVMe driver metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EBS "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-enhanced-EKS.md#Container-Insights-metrics-EBS").

ebsnvme script
The `ebsnvme` script can be found in the [amazon-ec2-utils Github repo](https://github.com/amazonlinux/amazon-ec2-utils "https://github.com/amazonlinux/amazon-ec2-utils").

###### To access the statistics

1. Connect to the instance to which the volume is attached.
2. Download the `ebsnvme` script from the `amazon-ec2-utils` Github repo.

```
wget https://raw.githubusercontent.com/amazonlinux/amazon-ec2-utils/refs/heads/main/ebsnvme
```

3. Modify the permissions for the script to make it executable.

```
sudo chmod +x ./ebsnvme
```

4. Run the `ebsnvme` script and specify the device name for the volume.

```
sudo ./ebsnvme stats /dev/`nvme0n1`
```

nvme-cli tool

###### To access the statistics

1. Connect to the instance to which the volume is attached.
2. Amazon Linux AMIs released after November 12, 2024 include the latest version of the
   `nvme-cli` tool. If you are using an older Amazon Linux AMI, update the
   `nvme-cli` tool.

```
sudo yum install nvme-cli
```

3. Run the following command and specify the device name for the volume.

```
nvme amzn stats /dev/`nvme0n1`
```

Prometheus
You can monitor the statistics with Prometheus, an open-source monitoring application,
and Amazon Managed Service for Prometheus. This makes it easier to monitor Amazon EBS volumes across container and Kubernetes
environments at scale. With Amazon EBS CSI driver version v1.37.0 and later, the detailed performance
statistics are exposed as a Prometheus-compatible `/metrics` endpoint for exporting
into Prometheus.

For more information, see [Ingest metrics to your Amazon Managed Service for Prometheus
workspace](../../../prometheus/latest/userguide/AMP-ingest-methods.md "../../../prometheus/latest/userguide/AMP-ingest-methods.md") in the _Amazon Managed Service for Prometheus User Guide_.

nvme_amzn.exe tool

###### To access the statistics

1. Connect to the instance to which the volume is attached.
2. Make sure that you're using AWSNVMe driver version `1.7.0` or later.
   For more information about updating the AWSNVMe driver, see [AWS NVMe drivers](../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md "../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md").
3. Get the disk number for the EBS volume. For more information, see [Map Amazon EBS volumes to NVMe device names](identify-nvme-ebs-device.md "identify-nvme-ebs-device.md")
4. Run the following command as Administrator and specify the disk number for the
   volume.

```
.\nvme_amzn.exe stats `disk_number`
```
