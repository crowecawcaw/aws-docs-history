# Amazon EBS I/O characteristics and monitoring

On a given volume configuration, certain I/O characteristics drive the performance
behavior for your EBS volumes.

- SSD-backed volumes, General Purpose SSD (`gp2` and `gp3`) and Provisioned IOPS SSD (`io1` and `io2`), deliver consistent
  performance whether an I/O operation is random or sequential.
- HDD-backed volumes, Throughput Optimized HDD (`st1`) and Cold HDD (`sc1`), deliver optimal
  performance only when I/O operations are large and sequential.
  To understand how SSD and HDD volumes will perform in your application, it is important
  to know the connection between demand on the volume, the quantity of IOPS available to it,
  the time it takes for an I/O operation to complete, and the volume's throughput limits.

###### Topics

- [IOPS](#ebs-io-iops "#ebs-io-iops")
- [Volume queue length and latency](#ebs-io-volume-queue "#ebs-io-volume-queue")
- [I/O size and volume throughput limits](#ebs-io-size-throughput-limits "#ebs-io-size-throughput-limits")
- [Monitor I/O characteristics using CloudWatch](#ebs-io-metrics "#ebs-io-metrics")
- [Monitor real-time I/O performance statistics](#monitor-io-nvme "#monitor-io-nvme")
- [Related resources](#ebs-io-resources "#ebs-io-resources")

## IOPS

IOPS are a unit of measure representing input/output operations per second. The
operations are measured in KiB, and the underlying drive technology determines the maximum
amount of data that a volume type counts as a single I/O. I/O size is capped at 256 KiB for
SSD volumes and 1,024 KiB for HDD volumes because SSD volumes handle small or random I/O
much more efficiently than HDD volumes.

When small I/O operations are physically sequential, Amazon EBS attempts to merge them into
a single I/O operation up to the maximum I/O size. Similarly, when I/O operations are larger
than the maximum I/O size, Amazon EBS attempts to split them into smaller I/O operations. The
following table shows some examples.

| Volume type                           | Maximum I/O size | I/O operations from your application                                                                    | Number of IOPS  | Notes                                                                                     |
| ------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------- |
| SSD                                   | 256 KiB          | 1 x 1024 KiB I/O operation                                                                              | 4 (1,024÷256=4) | Amazon EBS splits the 1,024 KiB I/O operation into four smaller 256 KiB operations.       |
| 8 x sequential 32 KiB I/O operations  | 1 (8x32=256)     | Amazon EBS merges the eight sequential 32 KiB I/O operations into a single 256<br>KiB operation.        |
| 8 random 32 KiB I/O operations        | 8                | Amazon EBS counts random I/O operations separately.                                                     |
| HDD                                   | 1,024 KiB        | 1 x 1024 KiB I/O operation                                                                              | 1               | The I/O operation is already equal to the maximum I/O size. It is not merged or<br>split. |
| 8 x sequential 128 KiB I/O operations | 1 (8x128=1,024)  | Amazon EBS merges the eight sequential 128 KiB I/O operations into a single 1,024<br>KiB I/O operation. |
| 8 random 32 KiB I/O operations        | 8                | Amazon EBS counts random I/O operations separately.                                                     |

Consequently, when you create an SSD-backed volume supporting 3,000 IOPS (either by
provisioning an `io1` or `io2` volume with 3,000 IOPS, by sizing a `gp2` volume at 1,000
GiB, or by using a `gp3` volume), and you attach it to an EBS-optimized instance that
can provide sufficient bandwidth, you can transfer up to 3,000 I/Os of data per second,
with throughput determined by I/O size.

## Volume queue length and latency

The volume queue length is the number of pending I/O requests for a device. Latency is the
true end-to-end client time of an I/O operation, in other words, the time elapsed between
sending an I/O to EBS and receiving an acknowledgement from EBS that the I/O read or write
is complete. Queue length must be correctly calibrated with I/O size and latency to avoid
creating bottlenecks either on the guest operating system or on the network link to
EBS.

Optimal queue length varies for each workload, depending on your particular application's
sensitivity to IOPS and latency. If your workload is not delivering enough I/O requests to
fully use the performance available to your EBS volume, then your volume might not deliver the
IOPS or throughput that you have provisioned.

Transaction-intensive applications are sensitive to increased I/O latency and are well-suited
for SSD-backed volumes. You can maintain high IOPS while keeping latency down by maintaining a low
queue length and a high number of IOPS available to the volume. Consistently driving more IOPS to
a volume than it has available can cause increased I/O latency. For maximum consistency, a volume
must maintain an average queue depth (rounded to the nearest whole number) of one for every 1,000
provisioned IOPS in a minute. For example, for a volume provisioned with 3,000 IOPS, the queue
depth average must be 3.

Throughput-intensive applications are less sensitive to increased I/O latency, and are
well-suited for HDD-backed volumes. You can maintain high throughput to
HDD-backed volumes by maintaining a high queue length when performing large, sequential
I/O.

## I/O size and volume throughput limits

For SSD-backed volumes, if your I/O size is very large, you may experience a smaller
number of IOPS than you provisioned because you are hitting the throughput limit of the
volume. For example, a `gp2` volume under 1,000 GiB with burst credits available has an IOPS
limit of 3,000 and a volume throughput limit of 250 MiB/s. If you are using a
256 KiB I/O size, your volume reaches its throughput limit at 1000 IOPS (1000 x 256 KiB =
250 MiB). For smaller I/O sizes (such as 16 KiB), this same volume can sustain
3,000 IOPS because the throughput is well below 250 MiB/s. (These examples
assume that your volume's I/O is not hitting the throughput limits of the instance.) For
more information about the throughput limits for each EBS volume type, see [Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md").

For smaller I/O operations, you may see a higher-than-provisioned IOPS value as measured
from inside your instance. This happens when the instance operating system merges small I/O
operations into a larger operation before passing them to Amazon EBS.

If your workload uses sequential I/Os on HDD-backed `st1` and `sc1` volumes, you may
experience a higher than expected number of IOPS as measured from inside your instance. This
happens when the instance operating system merges sequential I/Os and counts them in 1,024
KiB-sized units. If your workload uses small or random I/Os, you may experience a lower
throughput than you expect. This is because we count each random, non-sequential I/O toward
the total IOPS count, which can cause you to hit the volume's IOPS limit sooner than
expected.

Whatever your EBS volume type, if you are not experiencing the IOPS or throughput you
expect in your configuration, ensure that your EC2 instance bandwidth is not the limiting
factor. You should always use a current-generation, EBS-optimized instance (or one that
includes 10 Gb/s network connectivity) for optimal performance. Another possible cause for
not experiencing the expected IOPS is that you are not driving enough I/O to the EBS
volumes.

## Monitor I/O characteristics using CloudWatch

You can monitor these I/O characteristics with each volume's [CloudWatch volume metrics](using_cloudwatch_ebs.md#ebs-volume-metrics "using_cloudwatch_ebs.md#ebs-volume-metrics").

###### Monitor for stalled I/O

`VolumeStalledIOCheck` monitors the status of
your EBS volumes to determine when your volumes are impaired. The metric is a binary value that
will return a `0` (pass) or a `1` (fail) status based on whether or not
the EBS volume can complete I/O operations.

If the `VolumeStalledIOCheck` metric fails, you can either wait for AWS to
resolve the issue, or you can take actions, such as replacing the affected volume or stopping
and restarting the instance to which the volume is attached. In most cases, when this metric
fails, EBS will automatically diagnose and recover your volume within a few minutes. You can
use the [Pause I/O](ebs-fis.md "ebs-fis.md")
action in AWS Fault Injection Service to run controlled experiments to test your architecture and monitoring
based on this metric to improve your resiliency to storage faults.

###### Monitor I/O latency for a volume

You can monitor the average latency for read and write operations for an Amazon EBS volume using the
`VolumeAvgReadLatency` and `VolumeAvgWriteLatency` metrics respectively. You can use
the [Latency Injection](ebs-fis-latency-injection.md "ebs-fis-latency-injection.md") action in AWS Fault Injection Service to run controlled
experiments to test your architecture and monitoring based on this metric to improve your resiliency to
storage performance degradation.

If your I/O latency is higher than you require, make sure that your application is not attempting to drive
more IOPS or throughput than you have provisioned for your volume. You can use the `VolumeAvgIOPS`
and `VolumeAvgThroughput` metrics to monitor the average IOPS and throughput driven to your volume
in a minute and then compare that with the volume's provisioned IOPS and throughput. If the volume does not
drive any operations during the minute, the metrics will report a value of zero (`0`). If bursts of
high IOPS or throughput occurred for a shorter time than the minute interval then the volume experiences
micro-bursting, but the average IOPS and throughput metrics may report that you are driving lower performance
than your volume's provisioned IOPS or througput limits. To identify whether your volume experiences performance
bursts in a given minute, you can use the `VolumeIOPSExceededCheck` and `VolumeThroughputExceededCheck`
metrics. You can monitor these metrics to determine whether your workload consistently attempted to drive IOPS
or throughput that is greater than your volume's provisioned performance in a given minute. If the driven IOPS
for any second within the minute consistently exceeds your volume's provisioned IOPS performance, the
`VolumeIOPSExceededCheck` metric returns `1`. If the driven throughput for any second
within the minute consistently exceeds your volume's provisioned throughput performance, the
`VolumeThroughputExceededCheck` metric returns `1`. If driven IOPS and throughput is
within your volume's provisioned performance, the metrics return `0`.

If your application requires a greater number of IOPS than your volume can provide, you should consider using
one of the following:

- A `gp3`, `io2`, or `io1` volume that is provisioned with enough IOPS to achieve the required latency
- A larger `gp2` volume that provides enough baseline IOPS performance

HDD-backed `st1` and `sc1` volumes are designed to perform best with workloads that
take advantage of the 1,024 KiB maximum I/O size. To determine your volume's average I/O size,
divide `VolumeWriteBytes` by `VolumeWriteOps`. The same calculation
applies to read operations. If average I/O size is below 64 KiB, increasing the size of the
I/O operations sent to an `st1` or `sc1` volume should improve performance.

###### Monitor burst bucket balance for `gp2`, `st1`, and `sc1` volumes

`BurstBalance` displays the burst bucket balance for `gp2`, `st1`, and `sc1`
volumes as a percentage of the remaining balance. When your burst bucket is depleted, volume
I/O (for `gp2` volumes) or volume throughput (for `st1` and `sc1` volumes) is throttled to the
baseline. Check the `BurstBalance` value to determine whether your volume is being
throttled for this reason. For a complete list of the available Amazon EBS metrics, see [Amazon CloudWatch metrics for Amazon EBS](using_cloudwatch_ebs.md "using_cloudwatch_ebs.md") and
[Amazon EBS metrics for Nitro-based instances](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md#ebs-metrics-nitro "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md#ebs-metrics-nitro").

## Monitor real-time I/O performance statistics

You can access real-time detailed performance statistics for Amazon EBS volumes that are
attached to Nitro-based Amazon EC2 instances.

You can combine these statistics to derive average latency and IOPS, or to check
whether I/O operations are completing. You can also view the total amount of time that
your application has exceeded your EBS volume's or the attached instance's provisioned
IOPS or throughput limits. By tracking increases in these statistics over time, you
can identify whether you need to increase your provisioned IOPS or throughput limits
to optimize your application's performance. The detailed performance statistics also
include histograms for read and write I/O operations, which provide a distribution of
your I/O latency by keeping track of the total number of I/O operations completed
within a latency band.

For more information, see [Amazon EBS detailed performance statistics](nvme-detailed-performance-stats.md "nvme-detailed-performance-stats.md").

## Related resources

For more information about Amazon EBS I/O characteristics, see the following re:Invent
presentation: [Amazon EBS: Designing
for Performance](https://www.youtube.com/watch?v=2wKgha8CZ_w "https://www.youtube.com/watch?v=2wKgha8CZ_w").
