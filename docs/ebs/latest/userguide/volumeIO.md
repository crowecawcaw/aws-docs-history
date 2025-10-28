# Auto-enable I/O for impaired Amazon EBS volumes

When Amazon EBS determines that a volume's data is potentially inconsistent, it disables
I/O to the volume from any attached EC2 instances by default. This causes the volume
status check to fail, and creates a volume status event that indicates the cause of the
failure. If the consistency of a particular volume is not a concern, and you prefer that
the volume be made available immediately if it's **impaired**, you can
override the default behavior by configuring the volume to automatically enable I/O. If
you enable the **Auto-Enabled IO** volume attribute
(`autoEnableIO` in the API), I/O between the volume and the instance is
automatically re-enabled and the volume's status check will pass. In addition, you'll
see an event that lets you know that the volume was in a potentially inconsistent state,
but that its I/O was automatically enabled. When this event occurs, you should check the
volume's consistency and replace it if necessary. For more information, see [Amazon EBS volume events](monitoring-vol-events.md "monitoring-vol-events.md").

Console

###### To view the Auto-Enabled IO attribute of a volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume and choose the **Status checks** tab.

The **Auto-enabled I/O** field displays the current setting
(**Enabled** or **Disabled**) for the selected
volume.

###### To modify the Auto-Enabled IO attribute of a volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume and choose **Actions**, **Manage
   auto-enabled I/O**.
4. To automatically enable I/O for an impaired volume, select the **Auto-enable
   I/O for impaired volumes** check box. To disable the feature, clear the check
   box.
5. Choose **Update**.

AWS CLI

###### To view the autoEnableIO attribute of a volume

Use the [describe-volume-attribute](../../../cli/latest/reference/ec2/describe-volume-attribute.md "../../../cli/latest/reference/ec2/describe-volume-attribute.md") command.

```
aws ec2 describe-volume-attribute \
    --attribute autoEnableIO \
    --volume-id `vol-01234567890abcdef`
```

The following is example output.

```
{
    "AutoEnableIO": {
        "Value": true
    },
    "VolumeId": "vol-01234567890abcdef"
}
```

###### To modify the autoEnableIO attribute of a volume

Use the [modify-volume-attribute](../../../cli/latest/reference/ec2/modify-volume-attribute.md "../../../cli/latest/reference/ec2/modify-volume-attribute.md") command.

```
aws ec2 modify-volume-attribute \
    --auto-enable-io \
    --volume-id `vol-01234567890abcdef`
```

PowerShell

###### To view the autoEnableIO attribute of a volume

Use the [Get-EC2VolumeAttribute](../../../powershell/latest/reference/items/Get-EC2VolumeAttribute.md "../../../powershell/latest/reference/items/Get-EC2VolumeAttribute.md") cmdlet.

```
(Get-EC2VolumeAttribute `
    -Attribute autoEnableIO `
    -VolumeId `vol-01234567890abcdef`).AutoEnableIO
```

The following is example output.

```
True
```

###### To modify the autoEnableIO attribute of a volume

Use the [Edit-EC2VolumeAttribute](../../../powershell/latest/reference/items/Edit-EC2VolumeAttribute.md "../../../powershell/latest/reference/items/Edit-EC2VolumeAttribute.md") cmdlet.

```
Edit-EC2VolumeAttribute `
    -AutoEnableIO $true `
    -VolumeId `vol-01234567890abcdef`
```
