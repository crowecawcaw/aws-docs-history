

# Choose the right plan for your Lightsail instance
<a name="amazon-lightsail-right-size-instance"></a>

You can use the metrics that Amazon Lightsail reports for your instance to check whether its plan gives your workload enough CPU and disk performance, without paying for capacity that you don't use. Review your metrics over at least the last two weeks before you change plans, so that you see your busy periods as well as your quiet ones.

**Contents**
+ [Evaluate your instance plan](#right-size-evaluate-instance)
+ [Move your instance to a different plan](#right-size-change-plan)

## Evaluate your instance plan
<a name="right-size-evaluate-instance"></a>

Review each of the following before you decide that your instance needs a larger or smaller plan. One metric on its own doesn't show whether a plan fits. For example, an instance can place a light load on its disk even if its CPU is heavily used.
+ **CPU utilization and burst capacity**. If your instance operates in the burstable zone often or for long periods, it uses up its burst capacity, which can mean the plan is too small for your workload. For more information, see [Detect Lightsail instance bursting for optimal performance](amazon-lightsail-viewing-instance-burst-capacity.md).
+ **System disk performance**. If disk operations or bytes hold flat at the same level during busy periods while disk queue length climbs, the plan might be too small. If they stay low even during busy periods, the plan might be larger than you need. For examples of high and low values, see [Configure system disk performance alarms for your Lightsail instance](amazon-lightsail-configure-disk-performance-alarms.md).
+ **Memory**. Lightsail doesn't report memory usage as an instance metric. To check memory usage, connect to your instance and use a tool from your operating system, such as the `free` command on Linux or Task Manager on Windows.

For more information about the metrics that Lightsail reports for your instance, see [Monitor Lightsail instance performance with metrics](amazon-lightsail-viewing-instance-health-metrics.md).

## Move your instance to a different plan
<a name="right-size-change-plan"></a>

Lightsail does not change the plan of an existing instance in place. To move your instance to a larger or smaller plan, create a new instance from a snapshot of it.

**To move your instance to a different plan**

1. Create a snapshot of your instance. For more information, see [Snapshots](understanding-snapshots-in-amazon-lightsail.md).

1. Create a new instance from the snapshot, and choose the new plan.

1. Update your DNS, static IP, and any other resources to point to the new instance.

1. Delete the old instance when you no longer need it.

**Note**  
When you create an instance from a snapshot, the disk of the new instance must be equal to or larger than the disk of the original instance. Smaller Lightsail plans include smaller disks, so you can only move to a smaller plan whose disk is large enough to hold the original disk. If every smaller plan has a disk that is smaller than your current disk, you cannot move to a smaller plan this way.