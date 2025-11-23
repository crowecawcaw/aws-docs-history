# Delete an Amazon EBS volume

You can delete an Amazon EBS volume that you no longer need. After deletion, its data is gone
and the volume can't be attached to any instance. So before deletion, you can store a snapshot
of the volume, which you can use to re-create the volume later.

You can't delete a volume if it's attached to an instance. To delete a volume, you must
first detach it. For more information, see [Detach an Amazon EBS volume from an Amazon EC2 instance](ebs-detaching-volume.md "ebs-detaching-volume.md").

If you delete a volume that matches a Recycle Bin retention rule, the volume is
retained in the Recycle Bin instead of being immediately deleted. For more information, see
[Recycle Bin](recycle-bin.md "recycle-bin.md").

Console

###### To delete an EBS volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume. Verify that the volume is in the **Available**
   state.
4. Choose **Actions**, **Delete volume**.

If this option is disabled, the volume is attached to an instance and can't
be deleted. 5. When prompted for confirmation, enter `delete`, and then
choose **Delete**.

AWS CLI

###### To check whether an EBS volume is in use

Use the [describe-volumes](../../../cli/latest/reference/ec2/describe-volumes.md "../../../cli/latest/reference/ec2/describe-volumes.md") command. If the volume is in use, the state is
`in-use`. Otherwise, it is `available`.

```
aws ec2 describe-volumes \
    --volume-id `vol-01234567890abcdef` \
    --query Volumes[*].State \
    --output text
```

###### To delete an EBS volume

Use the [delete-volume](../../../cli/latest/reference/ec2/delete-volume.md "../../../cli/latest/reference/ec2/delete-volume.md") command.

```
aws ec2 delete-volume --volume-id `vol-01234567890abcdef`
```

PowerShell

###### To check whether an EBS volume is in use

Use the [Get-EC2Volume](../../../powershell/latest/reference/items/Get-EC2Volume.md "../../../powershell/latest/reference/items/Get-EC2Volume.md")
cmdlet. If the volume is in use, the state is `in-use`. Otherwise,
it is `available`.

```
(Get-EC2Volume `
    -VolumeId `vol-01234567890abcdef`).State.Value
```

###### To delete an EBS volume

Use the [Remove-EC2Volume](../../../powershell/latest/reference/items/Remove-EC2Volume.md "../../../powershell/latest/reference/items/Remove-EC2Volume.md") cmdlet.

```
Remove-EC2Volume -VolumeId `vol-01234567890abcdef`
```
