

# View system disk performance metrics for your Lightsail instance
<a name="amazon-lightsail-viewing-instance-disk-performance-metrics"></a>

You can monitor the read and write activity on your instance's system disk by using the system disk performance metrics that Amazon Lightsail reports for each instance. You can view these metrics on the **Metrics** tab of the instance management page. You can also create an alarm that notifies you when a metric crosses a threshold that you specify. For more information about alarms, see [Alarms](amazon-lightsail-alarms.md).

**Note**  
System disk performance metrics reflect activity on the instance's system disk only. They do not include activity on any attached disks.

**Contents**
+ [System disk performance metrics](#disk-performance-metrics)
+ [Understanding system disk performance limits](#disk-performance-limits)
+ [View system disk performance metrics](#viewing-disk-performance-metrics)
+ [Configure system disk performance alarms](amazon-lightsail-configure-disk-performance-alarms.md)
+ [Next steps](#next-steps-disk-performance-metrics)

## System disk performance metrics
<a name="disk-performance-metrics"></a>

You can view the following system disk performance metrics. Choose a metric in the **Select metric** dropdown under the **Metric graphs** heading on the instance **Metrics** tab to view its graph. View the graph over a longer period, such as the last two weeks, to see how the value changes over time.
+ **Disk read operations**. The number of read operations completed on the system disk during the period. A high value on the graph means your applications are reading heavily from the system disk. A sustained high value can mean the disk is serving as many read operations as it can, which can make your instance slow or unresponsive. A low value means there is little read activity, which is normal when your applications are mostly idle or are serving data from memory.
+ **Disk write operations**. The number of write operations completed on the system disk during the period. A high value on the graph means your applications are writing heavily to the system disk. A sustained high value can mean the disk is serving as many write operations as it can, which can make your instance slow or unresponsive. A low value means there is little write activity, which is normal when your applications are mostly idle.
+ **Disk read bytes**. The number of bytes read from the system disk during the period. A high value means a large volume of data is being read, such as during backups, media serving, or analytics. If the graph stays flat while your workload expects to read more data, the disk may be reaching its throughput limit. A low value means little data is being read.
+ **Disk write bytes**. The number of bytes written to the system disk during the period. A high value means a large volume of data is being written, such as during logging, backups, or data imports. If the graph stays flat while your workload expects to write more data, the disk may be reaching its throughput limit. A low value means little data is being written.
+ **Disk total read time**. The total number of seconds spent waiting for all read operations completed during the period. Compare this metric on the graph against disk read operations. A rising trend, especially when the number of read operations is not rising, means each read is taking longer and that the disk is a bottleneck, which can make your instance slow or unresponsive. A low value means reads are completing quickly.
+ **Disk total write time**. The total number of seconds spent waiting for all write operations completed during the period. Compare this metric on the graph against disk write operations. A rising trend, especially when the number of write operations is not rising, means each write is taking longer and that the disk is a bottleneck, which can make your instance slow or unresponsive. A low value means writes are completing quickly.
+ **Disk queue length**. The number of outstanding IOs (read and write requests) that are waiting to access the system disk. A high or growing value on the graph means requests are backing up because the disk cannot keep up with demand, which can slow your applications. A value at or near zero means the disk is keeping up with the requests being sent to it.

To get notified when a metric crosses a threshold that you specify, create an alarm. For more information, see [Configure system disk performance alarms for your Lightsail instance](amazon-lightsail-configure-disk-performance-alarms.md).

## Understanding system disk performance limits
<a name="disk-performance-limits"></a>

The performance that your system disk can reach is bounded by the lesser of two limits:
+ The limit of the system disk itself.
+ The limit that your instance plan places on storage throughput.

Because performance is bounded by the lesser of these two limits, raising only one of them does not improve performance when the other is the constraint. To raise the limit that your plan places on storage throughput, upgrade to a larger instance plan. For example, a smaller instance plan can place a storage ceiling that is lower than the limit of the system disk. In that case, the instance is the constraint, and moving to a larger instance plan raises that ceiling. If the system disk itself is the constraint, move data with heavy read or write activity to an attached disk instead. For more information, see [Respond to high system disk performance values](amazon-lightsail-configure-disk-performance-alarms.md#responding-to-disk-performance-issues).

When your disk reaches one of these limits, the graph for that metric stops rising and stays flat during busy periods, even if your workload needs more. Disk queue length and disk total read or write time often rise at the same time.

**Note**  
Operations and bytes are separate limits. Workloads with many small reads and writes reach the operations limit first. Workloads that read or write large amounts of data at once, such as backups or large file copies, reach the bytes limit first, even when the operations graph stays well below its limit. For more information, see [Amazon EBS I/O characteristics and monitoring](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-io-characteristics.html) in the *Amazon EBS User Guide*.

## View system disk performance metrics
<a name="viewing-disk-performance-metrics"></a>

Complete the following steps to view system disk performance metrics.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**.

1. Choose the name of the instance for which you want to view metrics.

1. Choose the **Metrics** tab on the instance management page.

1. Under **Metric graphs**, choose a system disk performance metric in the **Select metric** dropdown. For more information, see [System disk performance metrics](#disk-performance-metrics).

1. (Optional) Under **Time range**, choose a shorter or longer time range, such as **1 hour** or **2 weeks**.

The following image shows the **Select metric** dropdown on the **Metrics** tab. The system disk performance metrics are listed under **System disk**, and **Disk queue length** is selected.

![The Select metric dropdown on the Metrics tab, open to show the System disk group with Disk read operations, Disk write operations, Disk read bytes, Disk write bytes, Disk total read time, Disk total write time, and Disk queue length. Disk queue length is selected, and the graph behind the dropdown shows an alarm line.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-disk-queue-length-graph-alarm.png)


## Next steps
<a name="next-steps-disk-performance-metrics"></a>

There are a few additional tasks that you can perform for your instance:
+ To learn more about the metrics that Lightsail reports for your instance, see [Resource metrics](amazon-lightsail-resource-health-metrics.md).
+ To create alarms for these metrics and respond to high or low values, see [Configure system disk performance alarms for your Lightsail instance](amazon-lightsail-configure-disk-performance-alarms.md).
+ To learn how to set alarm thresholds for these metrics, see [Best practices for system disk performance alarms](amazon-lightsail-configure-disk-performance-alarms.md#disk-performance-alarms-best-practices).
+ To decide whether your instance needs a larger or smaller plan, see [Choose the right plan for your Lightsail instance](amazon-lightsail-right-size-instance.md).

**Topics**
+ [System disk performance metrics](#disk-performance-metrics)
+ [Understanding system disk performance limits](#disk-performance-limits)
+ [View system disk performance metrics](#viewing-disk-performance-metrics)
+ [Next steps](#next-steps-disk-performance-metrics)
+ [Configure disk performance alarms](amazon-lightsail-configure-disk-performance-alarms.md)