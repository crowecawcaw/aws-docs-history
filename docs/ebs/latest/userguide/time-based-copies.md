# Time-based copies for Amazon EBS snapshots and EBS-backed AMIs

Time-based copies can help you meet compliance or business requirements for data
replication by ensuring that your EBS snapshots and EBS-backed AMIs are copied, within
and across AWS Regions, in a specified timeframe. Time-based copies can also
help backup administrators meet stringent disaster recovery requirements (Recovery
Point Objectives and Recovery Time Objectives), and it improves development agility by
ensuring predictable copying times for snapshots and EBS-backed AMIs.

With time-based snapshot and EBS-backed AMI copy operations, you specify a completion
duration, between 15 minutes and 48 hours, in which the copy is to be completed. The
completion duration must be specified in 15 minute increments.

###### Topics

- [Quotas](#time-based-copies-quota "#time-based-copies-quota")
- [Determine your completion duration](#time-based-copies-how "#time-based-copies-how")
- [Considerations](#time-based-copies-considerations "#time-based-copies-considerations")
- [Monitoring](#time-based-copies-monitoring "#time-based-copies-monitoring")
- [Pricing and billing](#time-based-copies-pricing "#time-based-copies-pricing")

## Quotas

The following quotas apply to time-based snapshot and EBS-backed AMI copy operations:

| Quota                                     | Description                                                                                                                                                                                                                                                           | Quota value | Adjustable                                                                                                                                                                 |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snapshot copy operation throughput quota  | The maximum throughput that can be achieved by a single time-based<br>snapshot copy operation.<br>NoteFor AMI copy operations, the quota applies to each individual snapshot<br>associated with the AMI.                                                              | 500 MiB/s   | No                                                                                                                                                                         |
| Cumulative snapshot copy throughput quota | The maximum cumulative throughput that can be achieved by concurrent<br>time-based snapshot copy operations between a source and destination<br>Region.<br>NoteFor AMI copy operations, each individual snapshot associated with the AMI<br>counts towards the quota. | 2,000 MiB/s | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-E137849C "https://console.aws.amazon.com/servicequotas/home/services/ebs/quotas/L-E137849C") |

When you initiate a **time-based snapshot copy operation**,
you specify a completion duration. The throughput used by the request is determined by the
size of the snapshot data and the requested completion duration. For example, if you copy a
snapshot that has 225,000 MiB (0.214 TiB) of data, and you request a completion duration of
15 minutes, the throughput is 250 MiB/s (225,000 MiB ÷ 15 minutes = 250 MiB/s).

When you initiate a **time-based AMI copy operation**, the
completion duration you specify applies to each snapshot associated with the AMI. Because
each snapshot can have a different size, each snapshot is copied at a different throughput
to ensure that all snapshots are copied within the completion duration. For example, say you
have an AMI with the following associated snapshots:

- Snapshot 1: 200,000 MiB
- Snapshot 2: 500,000 MiB
- Snapshot 3: 450,000 MiB

If you initiate a time-based copy for this AMI and specify a completion duration of 60
minutes, the request uses the following throughput:

- Snapshot 1: 55.56 MiB/s (200,000 MiB ÷ 60 minutes = 55.56 MiB/s)
- Snapshot 2: 138.89 MiB/s (500,000 MiB ÷ 60 minutes = 138.89 MiB/s)
- Snapshot 3: 125 MiB/s (450,000 MiB ÷ 60 minutes = 125 MiB/s)

This means that the request uses 319.45 MiB/s of your cumulative snapshot copy throughput
quota to ensure that the copy completes in 60 minutes.

If you initiate a time-based snapshot or EBS-backed AMI copy request and your
available cumulative snapshot copy throughput quota is:

- greater than or equal to the required throughput rate, the copy completes
  within the requested completion duration.
- less than the required throughput rate but greater than zero, the request
  succeeds but it will take longer than you requested. The copy is completed using
  your available throughput quota.
- zero (quota reached), the request fails.

## Determine your completion duration

The minimum completion duration you can request for a time-based snapshot or
EBS-backed AMI copy operation is 15 minutes, and the maximum completion duration you
can request is 48 hours. The completion duration must be specified in 15 minute
increments.

###### Concurrent time-based snapshot copy operations

You can perform concurrent time-based snapshot copy operations between the same
source and destination Regions, as long as the combined throughput of all of the
concurrent operations is within your cumulative snapshot copy throughput quota (2,000
MiB/s by default).

To determine whether you can achieve your required completion duration for your
existing snapshots, divide the combined size of all of your snapshots by your required
completion duration to determine the required throughput rate.

###### Tip

If you don't know the exact size of the data in your snapshots, you can use the
full snapshot size as a proxy instead. To get the full snapshot size, use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") AWS CLI command.

```
required throughput rate = combined snapshot size ÷ required completion duration
```

If the required throughput rate is less than your cumulative snapshot copy throughput
quota, you can achieve your required completion duration. If the required throughput
rate is greater than your cumulative snapshot copy throughput quota, we recommend that
you request a quota increase that is at least 10% higher than your required throughput
rate.

###### Tip

The Amazon EC2 console provides a calculator that you can use to check how much snapshot data
you copied between two Regions over a specific period, and the minimum achievable completion
duration that you can achieve for that amount of data, based on a specific cumulative snapshot
copy throughput quota. The calculator uses the `SnapshotCopyBytesTransferred` CloudWatch
metric to calculate data copied between two Regions over a period. To open the calculator, in
the Amazon EC2 console navigation panel, select **Snapshots**, and
then choose **Actions**, **Launch copy
duration calculator**.

The snapshot copy duration calculator are not supported with AWS Outposts, Local Zones, and Wavelength
Zones.

###### Individual time-based snapshot copy operations

You can calculate the minimum completion duration for an individual time-based snapshot copy
operation by dividing the size of the snapshot data by the snapshot copy operation throughput
quota (500 MiB/s).

###### Tip

If you don't know the exact size of the data in your snapshots, you can use the
full snapshot size as a proxy instead. To get the full snapshot size, use the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") AWS CLI command.

```
minimum completion duration = Max(15 minutes, (snapshot data size ÷ 500 MiB/s)
```

For example, the minimum completion duration for a snapshot with 900,000 MiB of
data is 30 minutes.

```
minimum completion duration = Max(15 minutes, (900,000 MiB ÷ 500 MiB/s)
= Max(15 minutes, 30 minutes)
= 30 minutes
```

###### Time-based AMI copy operations

When you initiate a time-based AMI copy operation for an EBS-backed AMI with a single
associated snapshot, it behaves in the same way as an **individual
time-based snapshot copy operation**, and the same throughput limitations apply.

When you initiate a time-based AMI copy operation for an EBS-backed AMI with a multiple
associated snapshots, it behaves in the same way as **concurrent time-based
snapshot copy operations** and the same throughput limitations apply. Each associated
snapshot results in a separate snapshot copy request, each of which contributes to your cumulative
snapshot copy throughput quota. The completion duration that you specify applies to each
associated snapshot.

## Considerations

- You can initiate time-based snapshot and EBS-backed AMI copy operations when copying
  snapshots within the same Region or when copying snapshots across Regions.
- If you initiate two time-based copy operations for the same snapshot or AMI, the second
  copy operation's completion duration starts only after the first copy operation completes.
- Time-based copy operations and the snapshot copy duration calculator are not supported
  with AWS Outposts, Local Zones, and Wavelength Zones.

## Monitoring

You can monitor the progress of time-based snapshot and EBS-backed AMI copy operations
using the Amazon EC2 console and the AWS CLI. In the console, select the snapshot and then, in
the **Details tab**, inspect the **Progress** field. With the AWS CLI, inspect the `Progress` output
element in the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") command response.

You can check whether a time-based snapshot or EBS-backed AMI copy operation completed
within the requested completion duration by checking the difference between the
**Started** and **Completed**
times in the console, or `StartTime` and `CompletionTime` in the
`describe-snapshots` response.

You can also use the `copySnapshot` Amazon EventBridge event to monitor the outcome of
time-based copy operations. The event indicates whether the operation completed and whether
the requested completion duration was met. If the completion duration was not met, the event
includes more information about the cause. For more information, see [EBS snapshot events](ebs-cloud-watch-events.md#snapshot-events "ebs-cloud-watch-events.md#snapshot-events").

## Pricing and billing

###### Note

Similar to standard snapshot copy operations, if you copy a snapshot to a
new Region, a full (non-incremental) copy is created, which results in additional
storage costs. Subsequent copies of the same snapshot are incremental. Additionally,
if you use external or cross-region data transfers, additional Amazon EC2 data transfer
charges will apply.

Additional charges apply for time-based snapshot and EBS-backed AMI copy operations.
Time-based copy operations are charged at a rate that is based on the requested completion duration,
per GiB of snapshot data copied. The fixed rates are as follows:

###### Note

The completion duration must be specified in 15 minute increments. The minimum
completion duration is 15 minutes, and the maximum is 48 hours.

- 15 minutes — $0.020 per GiB of data
- 30 minutes and 45 minutes — $0.018 per GiB of data
- 1 hour to 1 hour 45 minutes — $0.016 per GiB of data
- 2 hours to 3 hours 45 minutes — $0.014 per GiB of data
- 4 hours to 7 hours 45 minutes — $0.012 per GiB of data
- 8 hours to 15 hours 45 minutes — $0.010 per GiB of data
- 16 hours or more — $0.005 per GiB of data

For example, if you copy a snapshot with 3,000 GiB of data with a
completion duration of 8 hours, you are billed $30 ($0.010 x 3,000 GiB).

If you initiate a time-based copy operation, but the requested completion duration is
not met due to you exceeding a quota, you are billed based on the actual completion duration
instead of the requested completion duration. For example, if you request a completion
duration of 1 hour, but the operation completes in 2 hours, you are billed based on the rate
for the 2 hour completion duration.

If Amazon EBS is not able to achieve the requested completion duration or if a request is
canceled due to service-side issues, you are not billed the additional charges for the
time-based snapshot copy operation.

If you delete the snapshot copy while the time-based snapshot copy operation is still in
progress, you are billed for the data copied up to that point at the rate corresponding to
the specified completion duration.
