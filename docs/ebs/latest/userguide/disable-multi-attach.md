

# Disable Multi-Attach for an Amazon EBS volume
<a name="disable-multi-attach"></a>

You can disable Multi-Attach for an `io2` volume only if it is attached to no more than one instance.

You can't disable Multi-Attach for `io1` volumes after creation.

------
#### [ Console ]

**To disable Multi-Attach after creation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Volumes**.

1. Select the volume and choose **Actions**, **Modify volume**.

1. For **Amazon EBS Multi-Attach**, clear **Enable Multi-Attach**.

1. Choose **Modify**.

------
#### [ AWS CLI ]

**To disable Multi-Attach after creation**  
Use the [modify-volume](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-volume.html) command with the `-no-multi-attach-enabled` option.

```
aws ec2 modify-volume \
    --volume-id {{vol-01234567890abcdef}} \
    --no-multi-attach-enabled
```

------
#### [ PowerShell ]

**To disable Multi-Attach after creation**  
Use the [Edit-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2Volume.html) cmdlet with the `-MultiAttachEnabled` parameter.

```
Edit-EC2Volume `
    -VolumeId {{vol-01234567890abcdef}} `
    -MultiAttachEnabled $false
```

------