# Amazon EBS volume status checks

Volume status checks enable you to better understand, track, and manage potential
inconsistencies in the data on an Amazon EBS volume. They are designed to provide you with
the information that you need to determine whether your Amazon EBS volumes are impaired, and
to help you control how a potentially inconsistent volume is handled.

Volume status checks are automated tests that run every 5 minutes and return a pass or
fail status. If all checks pass, the status of the volume is `ok`. If a check
fails, the status of the volume is `impaired`. If the status is
`insufficient-data`, the checks may still be in progress on the volume.
You can view the results of volume status checks to identify any impaired volumes and
take any necessary actions.

When Amazon EBS determines that a volume's data is potentially inconsistent, the default is
that it disables I/O to the volume from any attached EC2 instances, which helps to
prevent data corruption. After I/O is disabled, the next volume status check fails, and
the volume status is `impaired`. In addition, you'll see an event that lets
you know that I/O is disabled, and that you can resolve the impaired status of the
volume by enabling I/O to the volume. We wait until you enable I/O to give you the
opportunity to decide whether to continue to let your instances use the volume, or to
run a consistency check using a command, such as **fsck** (Linux instances)
or **chkdsk** (Windows instances), before doing so.

###### Note

Volume status is based on the volume status checks, and does not reflect the
volume state. Therefore, volume status does not indicate volumes in the
`error` state (for example, when a volume is incapable of accepting
I/O.) For information about volume states, see [Volume states](ebs-describing-volumes.md#volume-state "ebs-describing-volumes.md#volume-state").

If the consistency of a particular volume is not a concern, and you'd prefer that the
volume be made available immediately if it's impaired, you can override the default
behavior by configuring the volume to automatically enable I/O. If you enable the
**Auto-Enable IO** volume attribute (`autoEnableIO` in
the API), the volume status check continues to pass. In addition, you'll see an event
that lets you know that the volume was determined to be potentially inconsistent, but
that its I/O was automatically enabled. This enables you to check the volume's
consistency or replace it at a later time.

The I/O performance status check compares actual volume performance to the expected
performance of a volume. It alerts you if the volume is performing below expectations.
This status check is available only for Provisioned IOPS SSD (`io1` and `io2`) and General Purpose SSD (`gp3`) volumes that
are attached to an instance. The status check is not valid for General Purpose SSD (`gp2`), Throughput Optimized HDD
(`st1`), Cold HDD (`sc1`), or Magnetic(`standard`) volumes. The I/O performance status
check is performed once every minute, and CloudWatch collects this data every 5 minutes. It
might take up to 5 minutes from the moment that you attach an `io1` or `io2` volume to
an instance for the status check to report the I/O performance status.

###### Important

While initializing Provisioned IOPS SSD volumes that were restored from snapshots, the
performance of the volume may drop below 50 percent of its expected level, which
causes the volume to display a `warning` state in the **I/O
Performance** status check. This is expected, and you can ignore the
`warning` state on Provisioned IOPS SSD volumes while you are initializing
them. For more information, see [Manually initialize the volumes after creation](initalize-volume.md#ebs-initialize "initalize-volume.md#ebs-initialize").

The following table lists statuses for Amazon EBS volumes.

| Volume status       | I/O enabled status                                                                                                                          | I/O performance status (`io1`, `io2`, and `gp3` volumes only)                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `ok`                | Enabled (I/O Enabled or I/O Auto-Enabled)                                                                                                   | Normal (Volume performance is as expected)                                                                                          |
| `warning`           | Enabled (I/O Enabled or I/O Auto-Enabled)                                                                                                   | Degraded (Volume performance is below expectations)<br>Severely Degraded (Volume performance is well below<br>expectations)         |
| `impaired`          | Enabled (I/O Enabled or I/O Auto-Enabled)<br>Disabled (Volume is offline and pending recovery, or is waiting<br>for the user to enable I/O) | Stalled (Volume performance is severely impacted)<br>Not Available (Unable to determine I/O performance because I/O is<br>disabled) |
| `insufficient-data` | Enabled (I/O Enabled or I/O Auto-Enabled)<br>Insufficient Data                                                                              | Insufficient Data                                                                                                                   |

Console

###### To view status checks

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.

The **Volume status** column displays the operational status of
each volume. 3. To view the status details of a specific volume, select it in the
grid and choose the **Status checks** tab. 4. If you have a volume with a failed status check (status is `impaired`),
see [Work with an impaired Amazon EBS volume](work_volumes_impaired.md "work_volumes_impaired.md").

Alternatively, you can choose **Events** in the navigator to view all
the events for your instances and volumes. For more information, see [Amazon EBS volume events](monitoring-vol-events.md "monitoring-vol-events.md").

AWS CLI

###### To view volume status information

Use the [describe-volume-status](../../../cli/latest/reference/ec2/describe-volume-status.md "../../../cli/latest/reference/ec2/describe-volume-status.md") command.

```
aws ec2 describe-volume-status --volume-ids `vol-01234567890abcdef`
```

Use the following example to identify impaired volumes.

```
aws ec2 describe-volume-status --filters Name=volume-status.status,Values=impaired
```

PowerShell

###### To view volume status information

Use the [Get-EC2VolumeStatus](../../../powershell/latest/reference/items/Get-EC2VolumeStatus.md "../../../powershell/latest/reference/items/Get-EC2VolumeStatus.md") cmdlet.

```
Get-EC2VolumeStatus -VolumeId `vol-01234567890abcdef`
```

Use the following example to identify impaired volumes.

```
Get-EC2VolumeStatus -Filter @{Name="volume-status.status"; Values="impaired"}
```
