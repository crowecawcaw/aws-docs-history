

# Configure system disk performance alarms for your Lightsail instance
<a name="amazon-lightsail-configure-disk-performance-alarms"></a>

You can create an alarm that notifies you when a system disk performance metric crosses a threshold that you specify. For more information about the metrics, see [View system disk performance metrics for your Lightsail instance](amazon-lightsail-viewing-instance-disk-performance-metrics.md).

For details about each alarm setting, such as the threshold, frequency, and duration, see [Create Lightsail instance metric alarms](amazon-lightsail-adding-instance-health-metric-alarms.md).

**Contents**
+ [Best practices for system disk performance alarms](#disk-performance-alarms-best-practices)
+ [How alarms evaluate system disk performance metrics](#disk-performance-alarm-periods)
+ [Create a system disk performance metric alarm](#creating-disk-performance-alarms)
+ [Respond to high system disk performance values](#responding-to-disk-performance-issues)
+ [Respond to low system disk performance values](#responding-to-low-disk-performance-values)

## Best practices for system disk performance alarms
<a name="disk-performance-alarms-best-practices"></a>

The Lightsail console doesn't show a normal range for system disk performance metrics, because a level that is normal for one workload can be high for another. Before you configure an alarm for one of these metrics, view the metric over the last two weeks and identify its low, mid, and high levels.

We recommend that you create two alarms for each system disk performance metric that you want to monitor, based on the levels that you observe:
+ **A high threshold alarm** that notifies you when the metric rises well above its usual high level.
+ **A low threshold alarm** that notifies you when the metric drops well below its usual low level, such as when read operations stop because your application has no traffic.

You can create up to two alarms per metric, and Lightsail alarms are free. If you set a high threshold in the low range, you get more frequent alarm notifications, some of which might be unnecessary. If you set it in the high range, you get less frequent alarm notifications, but each one is more likely to be worth investigating. For suggested alarm settings, see [Suggested alarm settings](#suggested-disk-alarm-thresholds).

## How alarms evaluate system disk performance metrics
<a name="disk-performance-alarm-periods"></a>

The graphs show totals for 5 minute periods when you choose the 1 hour or 6 hours time range, which is how alarms evaluate these metrics. Longer time ranges add up longer periods, such as 1 hour for each data point in the 1 week and 2 weeks views, so the values on those graphs are larger.

Because of this, read the values that you base an alarm threshold on from the 1 hour or 6 hours view. Values from those views can be compared directly with the threshold that you enter. Values from the longer views are not comparable.

## Create a system disk performance metric alarm
<a name="creating-disk-performance-alarms"></a>

Complete the following steps to create a system disk performance metric alarm.

**To open the alarm form for a system disk performance metric**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**.

1. Choose the name of the instance for which you want to create an alarm.

1. Choose the **Metrics** tab on the instance management page.

1. Under **Metric graphs**, choose a system disk performance metric in the **Select metric** dropdown.

1. In the **Alarms for** section for the metric, choose **Create alarm**.

**To configure and create the alarm**

1. For **Rule**, choose a comparison operator. The options are **Greater than or equal to**, **Greater than**, **Less than**, and **Less than or equal to**.

1. For **Threshold**, enter the value that triggers the alarm. For suggested settings, see [Suggested alarm settings](#suggested-disk-alarm-thresholds).

1. For **Frequency (times)**, enter the number of times that the metric must cross the threshold to trigger the alarm.

1. For **Duration**, choose the hours and minutes within which the metric must cross the threshold that number of times. You can choose from 5 minutes up to 24 hours, in 5 minute increments. The summary that follows these fields shows the condition that changes the alarm state to **In alarm**.

1. (Optional) Under **Also notify me by**, select **Email** to also get an email when the alarm is triggered. If you have not added an email contact in the AWS Region of your instance, the console prompts you to add one. For more information, see [Metric notifications](amazon-lightsail-notifications.md).

   If you select **Email**, you can also select **Send me a notification when the alarm is no longer triggered** under **Additional notifications**.

1. (Optional) Expand **Advanced settings** to choose how the alarm treats missing data points.

1. Choose **Save** to create the alarm.

The following image shows an alarm configured for the Disk read operations metric, with a threshold of 480,000 operations, a frequency of 2 times, and a duration of 20 minutes.

![The alarm configuration panel showing a Disk read operations alarm with Rule set to Greater than, Threshold set to 480,000, Frequency set to 2, and Duration set to 20 minutes.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-disk-read-operations-alarm-panel.png)


Any alarms that you configure for a metric show up on the graph for that metric. Each alarm appears as a line at its threshold, marked with a numbered alarm icon at the right edge of the graph.

The following image shows an example Disk read operations graph over a 1 hour period with two alarms. Each data point is the total number of read operations in a 5 minute period. Alarm 1 is a high threshold alarm at 50 read operations, shown as a dashed line. Alarm 2 is a low threshold alarm at 0, which notifies you when there is no read activity. In this example, read operations stay at 0 for most of the hour, then rise to about 40.

![Disk read operations graph with the 1 hour time range selected and two alarms. Alarm 1 is a dashed line at 50 and Alarm 2 is at 0. The Total read operations per 5 minutes line stays at 0, then rises to about 40.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-disk-read-operations-graph.png)


## Respond to high system disk performance values
<a name="responding-to-disk-performance-issues"></a>

If an alarm indicates that your system disk performance is consistently high, or that read and write times are rising, check the graph for the pattern that matches your metric. Read the values from your own graph in the 1 hour or 6 hours view, which shows totals for the same 5 minute periods that alarms evaluate. For more information, see [How alarms evaluate system disk performance metrics](#disk-performance-alarm-periods).
+ **Disk read operations**. During busy periods, reads hold flat at the same level for hours, and disk queue length climbs at the same time. The disk is serving as many read operations as it can.
+ **Disk write operations**. During busy periods, writes hold flat at the same level for hours, and disk queue length climbs at the same time. The disk is serving as many write operations as it can.
+ **Disk read bytes**. During a backup, the graph flattens at the same level and won't go higher, even though the backup could move more data. The disk has reached its bytes limit. (Disk read operations might look low at the same time because a backup reads data in large pieces.)
+ **Disk write bytes**. During a data import, the graph flattens at the same level and won't go higher. The disk has reached its bytes limit.
+ **Disk total read time**. Read operations hold flat, but disk total read time keeps climbing from one period to the next. Each read is waiting longer because the disk is at its limit, which can make your instance slow or unresponsive.
+ **Disk total write time**. Write operations hold flat, but disk total write time keeps climbing from one period to the next. Each write is waiting longer because the disk is at its limit, which can make your instance slow or unresponsive.
+ **Disk queue length**. Disk queue length climbs and stays high during busy periods, while read and write operations hold flat. Requests are backing up because the disk cannot keep up with demand, which slows your applications.

**Note**  
Read and write operations share the same limit, and so do read and write bytes. Each alarm watches the read metric or the write metric separately, so if your workload mixes reads and writes, the combined activity can reach the limit before either alarm triggers. To catch this case, also create a disk queue length alarm.

For any of these patterns, consider the following options.
+ **Move data with heavy read or write activity to an attached disk.** Attaching a disk to your instance and moving activity to it reduces the load on the system disk. For more information, see [Add and use an attached disk](#add-block-storage-disk-for-disk-performance).
+ **Upgrade to a larger instance plan.** A larger instance plan can raise the storage throughput limit that your plan places on the instance. This helps when the plan, rather than the disk itself, is the constraint. To change your plan, see [Choose the right plan for your Lightsail instance](amazon-lightsail-right-size-instance.md).

### Suggested alarm settings
<a name="suggested-disk-alarm-thresholds"></a>

Set each threshold based on the levels that you observe on your own graph over the last two weeks. For more information, see [Best practices for system disk performance alarms](#disk-performance-alarms-best-practices). Alarms evaluate these metrics as a total over each 5 minute period, so set thresholds as totals per 5 minutes, not per second values.

For a high threshold alarm, use the following settings as a starting point:
+ **Rule**: Greater than
+ **Frequency (times)**: 2
+ **Duration**: 20 minutes

The following image shows a high threshold alarm for the Disk read operations metric with these settings.

![The alarm configuration panel showing a Disk read operations alarm with Rule set to Greater than, Threshold set to 480,000, Frequency set to 2, and Duration set to 20 minutes.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-disk-read-operations-alarm-panel.png)


**Note**  
Disk total read time and disk total write time do not have a limit that depends on your plan. For these metrics, start with the value that the console fills in when you create an alarm, which is greater than 60 seconds. Then adjust the threshold based on your graph.

### Add and use an attached disk
<a name="add-block-storage-disk-for-disk-performance"></a>

An attached disk is a separate disk that you attach to your instance. Moving data with heavy read or write activity to it takes that load off the system disk, so the system disk metrics fall. To add a disk and move data to it, do the following:

1. Create a disk in the same AWS Region and Availability Zone as your instance, and attach it to the instance. For more information, see [Create and attach additional block storage disks to your Linux based Lightsail instances](create-and-attach-additional-block-storage-disks-linux-unix.md).

1. Connect to your instance, and then format and mount the new disk so that your operating system can use it. The tutorial in the previous step includes the exact commands.

1. Move the data that drives your read or write load, such as a database directory, log files, or media files, to the new disk. Update your application so that it reads and writes from the new location.

1. On the **Metrics** tab, confirm that the system disk metrics fall after you move the data.

**Note**  
Do not rely on system disk performance metrics alone to decide whether to upgrade your instance plan. Review other metrics, such as CPU utilization, to understand the overall load on your instance. For example, an instance can have high CPU load while placing only a light read and write load on the system disk.

## Respond to low system disk performance values
<a name="responding-to-low-disk-performance-values"></a>

If an alarm indicates that a metric stays low, check the graph for the pattern that matches your metric. Read the values from your own graph in the 1 hour or 6 hours view.
+ **Disk read operations**. Reads stay low even during your busy periods. If your other disk metrics and your CPU utilization are also low, the instance might be larger than you need.
+ **Disk write operations**. Writes stay low even during your busy periods. If your other disk metrics and your CPU utilization are also low, the instance might be larger than you need.
+ **Disk read bytes**. Reads stay low even during your busy periods. If your other disk metrics and your CPU utilization are also low, the instance might be larger than you need.
+ **Disk write bytes**. Writes stay low even during your busy periods. If your other disk metrics and your CPU utilization are also low, the instance might be larger than you need.
+ **Disk total read time**. Disk total read time stays near 1 second per period even during busy hours, so reads complete quickly and the disk has headroom. This value is healthy and is not by itself a reason to downsize. Base a downsizing decision on disk read operations, disk read bytes, and CPU utilization.
+ **Disk total write time**. Disk total write time stays near 1 second per period even during busy hours, so writes complete quickly and the disk has headroom. This value is healthy and is not by itself a reason to downsize. Base a downsizing decision on disk write operations, disk write bytes, and CPU utilization.
+ **Disk queue length**. Disk queue length stays at or near 0 over the last two weeks, so the disk is easily keeping up with demand. This value is healthy and is not by itself a reason to downsize. Base a downsizing decision on disk operations, disk bytes, and CPU utilization.

For any of these patterns, consider the following options.
+ **Move to a smaller instance plan.** If your disk operations, disk bytes, and CPU utilization all stay low, a smaller instance plan might fit your workload. Base the decision on those metrics, not on disk total read time, disk total write time, or disk queue length alone. To change your plan, see [Choose the right plan for your Lightsail instance](amazon-lightsail-right-size-instance.md).