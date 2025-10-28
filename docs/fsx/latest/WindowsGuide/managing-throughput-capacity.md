# Managing throughput capacity

You can increase and decrease your file system's throughput capacity to help manage its performance at any time.
Throughput capacity is one of the dimensions that determines the speed at which the file server hosting your FSx for Windows File Server file system
can serve data. Higher levels of throughput capacity also come with higher levels of I/O operations per
second (IOPS) and a larger amount of cache memory on the file server. For more information, see [FSx for Windows File Server performance](performance.md "performance.md").

###### Topics

- [How throughput scaling works](#how-throughput-scaling-works "#how-throughput-scaling-works")
- [Knowing when to modify throughput capacity](#when-to-modify-throughput-capacity "#when-to-modify-throughput-capacity")
- [Modifying throughput capacity](increase-throughput-capacity.md "increase-throughput-capacity.md")
- [Monitoring throughput capacity updates](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md")

## How throughput scaling works

When you modify your file system's throughput capacity, Amazon FSx
switches out the file system's file server to one with more or less throughput behind the scenes. For Multi-AZ file systems, switching to a new file server triggers an
automatic failover and failback while Amazon FSx switches out the preferred and secondary file servers. Single-AZ file systems will be
unavailable for a few minutes while the file server is switched during throughput capacity scaling.
You are billed for the new amount of throughput capacity once it becomes available to your file
system.

###### Note

During a maintenance operation on the back end, system modifications (including throughput capacity modifications)
may be delayed. Maintenance operations can cause system modifications to queue up to be processed.

For Multi-AZ file systems, throughput capacity scaling results in an automatic failover and
failback while Amazon FSx switches out the preferred and secondary file servers. During file server replacements, which happen during throughput capacity scaling
as well as file system maintenance and an unplanned service disruption, any ongoing traffic to the file system will be served by the remaining file server. When the replaced file
server is back online, FSx for Windows will run a resynchronization job to ensure that data is synced back to the
newly replaced file server.

FSx for Windows is designed to minimize the impact of this resynchronization activity on application and users. However,
the resynchronization process involves synchronizing data in large blocks. This means that a large block of data can require
synchronization even if only a small portion is updated. Consequently, the amount of resynchronization depends not only
on the amount of data churn, but also the nature of the data churn on the file system. If your workload is write-heavy and IOPS-heavy, the
data synchronization process may take longer and require additional performance resources.

Your file system will continue to be available during this time, but in order to reduce the duration of data synchronization,
we recommend modifying throughput capacity during idle periods when there is minimal load on
your file system. We also recommend ensuring that your file system has sufficient throughput capacity to run the synchronization job in addition to your workload, in order to reduce the duration of
data synchronization. Lastly, we recommend testing the impact of failovers while your file system has a lighter load.

## Knowing when to modify throughput capacity

Amazon FSx integrates with Amazon CloudWatch, enabling you to monitor your file system's ongoing
throughput usage levels. The performance (throughput and IOPS) that you can drive through your
file system depends on your specific workload’s characteristics, along with your file
system’s throughput capacity, storage capacity, and storage type. You
can use CloudWatch metrics to determine which of these dimensions to change to improve performance. For
more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

FSx for Windows File Server provides performance alerts based on values of CloudWatch metrics for your file system in the Monitoring & performance
dashboard in the File system details page on the Amazon FSx console. This includes throughput capacity, and
other file system metrics that can benefit from throughput capacity increases. For more information, see
[Performance warnings and recommendations](monitoring-cloudwatch.md#performance-insights-FSxW "monitoring-cloudwatch.md#performance-insights-FSxW").

Configure your file system with sufficient throughput capacity to meet not only the expected traffic of your
workload, but also additional performance resources that are needed to support the features
you enable on your file system. For example, if you’re running data
deduplication, the throughput capacity that you select must provide enough memory to
run deduplication based on the storage that you have. If you’re using shadow copies,
increase throughput capacity to a value that's at least three times the value that's
expected to be driven by your workload to avoid Windows Server deleting your shadow
copies. For more information, see [Impact of throughput capacity on performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").
