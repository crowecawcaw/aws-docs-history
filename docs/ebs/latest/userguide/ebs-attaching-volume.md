# Attach an Amazon EBS volume to an Amazon EC2 instance

You can attach an available EBS volume to one or more of your instances that is in the
same Availability Zone as the volume.

For information about adding EBS volumes to your instance at launch, see
[instance block device mapping](../../../AWSEC2/latest/UserGuide/block-device-mapping-concepts.md#instance-block-device-mapping "../../../AWSEC2/latest/UserGuide/block-device-mapping-concepts.md#instance-block-device-mapping").

###### Considerations

- The maximum number of Amazon EBS volumes that you can attach to an instance depends on the
  instance type. If you exceed the volume attachment limit for an instance type, the attachment
  request fails with the `AttachmentLimitExceeded` error. For more information,
  see [Instance
  volume limits](../../../AWSEC2/latest/UserGuide/volume_limits.md "../../../AWSEC2/latest/UserGuide/volume_limits.md").
- You can attach volumes to instances that are in the same Availability Zone only.
- Multi-Attach enabled volumes can be attached to up to 16 instances. For more
  information, see [Attach an EBS volume to multiple EC2 instances using Multi-Attach](ebs-volumes-multi.md "ebs-volumes-multi.md").
- If the volume has an AWS Marketplace product code:
  - You can attach it to a stopped instance only.
  - You must be subscribed to the AWS Marketplace code that is on the volume.
  - The instance's configuration, such as its type and operating system, must support
    that specific AWS Marketplace code. For example, you cannot take a volume from a Windows
    instance and attach it to a Linux instance.
  - AWS Marketplace codes are copied from the volume to the instance.

- This device name you specify is used by Amazon EC2. The block device driver can mount the
  device with a device name that is different from the one you specify. For more information,
  see [Device
  names for volumes on Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/device_naming.md "../../../AWSEC2/latest/UserGuide/device_naming.md").
- In some cases, a volume other than the volume attached to `/dev/xvda`
  or `/dev/sda` can become the root volume for the instance. This can happen
  if you attach the root volume of another instance, or a volume created from the
  snapshot of a root volume, to an instance with an existing root volume. For more
  information, see [Boot from the wrong volume](../../../AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.md "../../../AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.md").

Console

###### To attach an EBS volume to an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume to attach and choose **Actions**, **Attach
   volume**.
4. For **Instance**, enter the ID of the instance or select
   the instance from the list of options.
5. For **Device name**, do one of the following:
   - For a root volume, select the required device name from the **Reserved
     for root volume** section of the list. Typically `/dev/sda1` or
     `/dev/xvda` for Linux instances depending on the AMI, or `/dev/sda1`
     for Windows instances.
   - For data volumes, select an available device name from the **Recommended for
     data volumes** section of the list.
   - To use a custom device name, select **Specify a custom device name**
     and then enter the device name to use.

6. Choose **Attach volume**.
7. Connect to the instance and mount the volume. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md "ebs-using-volumes.md").

AWS CLI

###### To attach an EBS volume to an instance

Use the [attach-volume](../../../cli/latest/reference/ec2/attach-volume.md "../../../cli/latest/reference/ec2/attach-volume.md") command.
The following example attaches the specified volume to the specified instance using the
specified device name.

```
aws ec2 attach-volume \
    --volume-id `vol-01234567890abcdef` \
    --instance-id `i-1234567890abcdef0` \
    --device `/dev/sdf`
```

PowerShell

###### To attach an EBS volume to an instance

Use the [Add-EC2Volume](../../../powershell/latest/reference/items/Add-EC2Volume.md "../../../powershell/latest/reference/items/Add-EC2Volume.md") cmdlet.
The following example attaches the specified volume to the specified instance using the
specified device name.

```
Add-EC2Volume `
    -VolumeId `vol-01234567890abcdef` `
    -InstanceId `i-1234567890abcdef0` `
    -Device `/dev/sdf`
```
