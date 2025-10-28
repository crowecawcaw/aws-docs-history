# Amazon EBS volume events

When Amazon EBS determines that a volume's data is potentially inconsistent, it disables
I/O to the volume from any attached EC2 instances by default. This causes the volume
status check to fail, and creates a volume status event that indicates the cause of the
failure.

To automatically enable I/O on a volume with potential data inconsistencies, change
the setting of the **Auto-Enabled IO** volume attribute
(`autoEnableIO` in the API). For more information about changing this
attribute, see [Work with an impaired Amazon EBS volume](work_volumes_impaired.md "work_volumes_impaired.md").

Each event includes a start time that indicates the time at which the event occurred,
and a duration that indicates how long I/O for the volume was disabled. The end time is
added to the event when I/O for the volume is enabled.

###### Volume status events

`Awaiting Action: Enable IO`

Volume data is potentially inconsistent. I/O is disabled for the volume
until you explicitly enable it. The event description changes to **IO
Enabled** after you explicitly enable I/O.

`IO Enabled`

I/O operations were explicitly enabled for this volume.

`IO Auto-Enabled`

I/O operations were automatically enabled on this volume after an event
occurred. We recommend that you check for data inconsistencies before
continuing to use the data.

`Normal`

For `io1`, `io2`, and `gp3` volumes only. Volume performance is as expected.

`Degraded`

For `io1`, `io2`, and `gp3` volumes only. Volume performance is below expectations.

`Severely Degraded`

For `io1`, `io2`, and `gp3` volumes only. Volume performance is well below
expectations.

`Stalled`

For `io1`, `io2`, and `gp3` volumes only. Volume performance is severely impacted.

If you have a volume where I/O is disabled, see [Work with an impaired Amazon EBS volume](work_volumes_impaired.md "work_volumes_impaired.md"). If you have a volume where I/O performance
is below normal, this might be a temporary condition due to an action you have taken
(for example, creating a snapshot of a volume during peak usage, running the volume on
an instance that cannot support the I/O bandwidth required, accessing data on the volume
for the first time, etc.).

Console

###### To view events for your volumes

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Events**. All instances and
   volumes that have events are listed.
3. You can filter by volume to view only volume status. You can also filter on
   specific status types.
4. Select a volume to view its specific event.

AWS CLI

###### To view events for your volumes

Use the [describe-volume-status](../../../cli/latest/reference/ec2/describe-volume-status.md "../../../cli/latest/reference/ec2/describe-volume-status.md") command.

```
aws ec2 describe-volume-status --volume-ids `vol-01234567890abcdef`
```

PowerShell

###### To view events for your volumes

Use the [Get-EC2VolumeStatus](../../../powershell/latest/reference/items/Get-EC2VolumeStatus.md "../../../powershell/latest/reference/items/Get-EC2VolumeStatus.md") cmdlet.

```
Get-EC2VolumeStatus -VolumeId `vol-01234567890abcdef`
```
