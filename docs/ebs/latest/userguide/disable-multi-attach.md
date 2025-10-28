# Disable Multi-Attach for an Amazon EBS volume

You can disable Multi-Attach for an `io2` volume only if it is attached to no more than
one instance.

You can't disable Multi-Attach for `io1` volumes after creation.

Console

###### To disable Multi-Attach after creation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume and choose **Actions**,
   **Modify volume**.
4. For **Amazon EBS Multi-Attach**, clear **Enable
   Multi-Attach**.
5. Choose **Modify**.

AWS CLI

###### To disable Multi-Attach after creation

Use the [modify-volume](../../../cli/latest/reference/ec2/modify-volume.md "../../../cli/latest/reference/ec2/modify-volume.md")
command with the `-no-multi-attach-enabled` option.

```
aws ec2 modify-volume \
    --volume-id `vol-01234567890abcdef` \
    --no-multi-attach-enabled
```

PowerShell

###### To disable Multi-Attach after creation

Use the [Edit-EC2Volume](../../../powershell/latest/reference/items/Edit-EC2Volume.md "../../../powershell/latest/reference/items/Edit-EC2Volume.md") cmdlet with the `-MultiAttachEnabled`
parameter.

```
Edit-EC2Volume `
    -VolumeId `vol-01234567890abcdef` `
    -MultiAttachEnabled $false
```
