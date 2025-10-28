# Enable Multi-Attach for an Amazon EBS volume

Multi-Attach enabled volumes can be managed in much the same way that you would manage
any other Amazon EBS volume. However, in order to use the Multi-Attach functionality, you must
enable it for the volume.

When you create a new volume, Multi-Attach is disabled by default. You can enable
Multi-Attach when you create a volume.

You can also enable Multi-Attach for `io2` volumes after creation, but only if they
are not attached to any instances. You can't enable Multi-Attach for `io1` volumes
after creation.

After you enable Multi-Attach for a volume, you can attach the volume to an instance in the
same way that you attach any other EBS volume. For more information, see [Attach an Amazon EBS volume to an Amazon EC2 instance](ebs-attaching-volume.md "ebs-attaching-volume.md").

Console

###### To enable Multi-Attach during volume creation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Choose **Create volume**.
4. For **Volume type**, choose **Provisioned IOPS SSD
   (`io1`)** or **Provisioned IOPS SSD (`io2`)**.
5. For **Size** and **IOPS**, choose the
   required volume size and the number of IOPS to provision.
6. For **Availability Zone**, choose the same Availability Zone
   that the instances are in.
7. For **Amazon EBS Multi-Attach**, choose **Enable
   Multi-Attach**.
8. (Optional) For **Snapshot ID**, choose the snapshot from which to create
   the volume.
9. Set the encryption status for the volume.

If the selected snapshot is encrypted, or if your account is enabled for [encryption by default](encryption-by-default.md "encryption-by-default.md"), then encryption is automatically
enabled and you can't disable it. You can choose the KMS key to use to encrypt the
volume.

If the selected snapshot is unencrypted and your account is not enabled for encryption
by default, encryption is optional. To encrypt the volume, for **Encryption**,
choose **Encrypt this volume** and then select the KMS key to use to
encrypt the volume.

You can attach encrypted volumes only to instances that support Amazon EBS encryption. For
more information, see [Amazon EBS encryption](ebs-encryption.md "ebs-encryption.md"). 10. (Optional) To assign custom tags to the volume, in the **Tags**
section, choose **Add tag**, and then enter a tag key and value pair. 11. Choose **Create volume**.

###### To enable Multi-Attach after creation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume and choose **Actions**,
   **Modify volume**.
4. For **Amazon EBS Multi-Attach**, choose **Enable
   Multi-Attach**.
5. Choose **Modify**.

AWS CLI

###### To enable Multi-Attach during volume creation

Use the [create-volume](../../../cli/latest/reference/ec2/create-volume.md "../../../cli/latest/reference/ec2/create-volume.md")
command with the `--multi-attach-enabled` option.

```
aws ec2 create-volume \
    --volume-type io2 \
    --multi-attach-enabled \
    --size `100` \
    --iops `2000` \
    --region `us-west-2` \
    --availability-zone `us-west-2b`
```

###### To enable Multi-Attach after creation

Use the [modify-volume](../../../cli/latest/reference/ec2/modify-volume.md "../../../cli/latest/reference/ec2/modify-volume.md")
command with the `--multi-attach-enabled` option.

```
aws ec2 modify-volume \
    --volume-id `vol-01234567890abcdef` \
    --multi-attach-enabled
```

PowerShell

###### To enable Multi-Attach during volume creation

Use the [New-EC2Volume](../../../powershell/latest/reference/items/New-EC2Volume.md "../../../powershell/latest/reference/items/New-EC2Volume.md") cmdlet with the `-MultiAttachEnabled`
parameter.

```
New-EC2Volume `
    -VolumeType io2 `
    -MultiAttachEnabled $true `
    -Size `100` `
    -Iops `2000` `
    -Region `us-west-2` `
    -AvailabilityZone `us-west-2b`
```

###### To enable Multi-Attach after creation

Use the [Edit-EC2Volume](../../../powershell/latest/reference/items/Edit-EC2Volume.md "../../../powershell/latest/reference/items/Edit-EC2Volume.md") cmdlet with the `-MultiAttachEnabled`
parameter.

```
Edit-EC2Volume `
    -VolumeId `vol-01234567890abcdef` `
    -MultiAttachEnabled $true
```
