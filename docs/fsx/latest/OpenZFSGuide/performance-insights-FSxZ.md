# Performance warnings and recommendations

FSx for OpenZFS displays a warning for CloudWatch metrics when one of these metrics approaches
or crosses a predetermined threshold for multiple consecutive data points. These warnings
provide you with actionable recommendations that you can use to optimize your file system's
performance.

Warnings are accessible in several areas of the **Monitoring &
performance** dashboard on the Amazon FSx console. All active or recent Amazon FSx
performance warnings and CloudWatch alarms configured for the file system that are in an alarm state
appear in the **Monitoring & performance** panel in the
**Summary** section. The warning also appears in the section of the
dashboard where the metric graph is displayed.

You can create CloudWatch alarms for any of the Amazon FSx metrics. For more information, see
[Creating CloudWatch alarms to monitor metrics](creating_alarms.md "creating_alarms.md").

## Use performance warnings to improve file system performance

Amazon FSx provides actionable recommendations that you can use to optimize your file
system's performance. You can take the recommended action if you expect the issue to
continue, or if it's causing an impact to your file system's performance. Depending on which
metric has triggered a warning, you can resolve it by increasing the file system's
throughput capacity or storage capacity, as described in the following table.

| If there's a warning for this metric           | Do this                                                                                                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Network throughput – utilization               | [Increase throughput capacity](managing-throughput-capacity.md#increase-throughput-capacity "managing-throughput-capacity.md#increase-throughput-capacity") |
| File server > Disk IOPS – utilization          |
| File server > Disk throughput – utilization    |
| File server > Disk IOPS – burst balance        |
| File server > Disk throughput – burst balance  |
| File server > CPU utilization                  |
| Storage capacity utilization                   | [Increase storage capacity](managing-storage-capacity.md#increase-storage-capacity "managing-storage-capacity.md#increase-storage-capacity")                |
| Storage volume > Disk IOPS – utilization (SSD) | [Increase SSD IOPS](managing-storage-capacity.md#increase-storage-capacity "managing-storage-capacity.md#increase-storage-capacity")                        |

For more information about file system performance, see [Performance for Amazon FSx for OpenZFS](performance.md "performance.md").
