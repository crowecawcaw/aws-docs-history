# Work with an impaired Amazon EBS volume

Use the following options if a volume is impaired because the volume's data
is potentially inconsistent.

###### Options

- [Option 1: Perform a consistency check on the volume
  attached to its instance](#work_volumes_impaired_option1 "#work_volumes_impaired_option1")
- [Option 2: Perform a consistency check on the volume
  using another instance](#work_volumes_impaired_option2 "#work_volumes_impaired_option2")
- [Option 3: Delete the volume if you no longer need
  it](#work_volumes_impaired_option3 "#work_volumes_impaired_option3")

## Option 1: Perform a consistency check on the volume

attached to its instance

The simplest option is to enable I/O and then perform a data consistency check on
the volume while the volume is still attached to its Amazon EC2 instance.

###### To perform a consistency check on an attached volume

1. Stop any applications from using the volume.
2. Enable I/O on the volume. Use one of the following methods.

Console

###### To enable I/O for a volume

    1. Open the Amazon EC2 console at
     [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
    2. In the navigation pane, choose **Events**.
    3. Select the volume.
    4. Choose **Actions**, **Enable I/O**.

AWS CLI

###### To enable I/O for a volume

Use the [enable-volume-io](../../../cli/latest/reference/ec2/enable-volume-io.md "../../../cli/latest/reference/ec2/enable-volume-io.md") command.

```
aws ec2 enable-volume-io --volume-id `vol-01234567890abcdef`
```

PowerShell

###### To enable I/O for a volume

Use the [Enable-EC2VolumeIO](../../../powershell/latest/reference/items/Enable-EC2VolumeIO.md "../../../powershell/latest/reference/items/Enable-EC2VolumeIO.md") cmdlet.

```
Enable-EC2VolumeIO -VolumeId `vol-01234567890abcdef`
```

3. Check the data on the volume.
   1. Run the **fsck** (Linux instances) or **chkdsk**
      (Windows instances) command.
   2. (Optional) Review any available application or system logs for
      relevant error messages.
   3. If the volume has been impaired for more than 20 minutes, you can
      contact the AWS Support Center. Choose
      **Troubleshoot**, and then in the
      **Troubleshoot Status Checks** dialog box,
      choose **Contact Support** to submit a support
      case.

## Option 2: Perform a consistency check on the volume

using another instance

Use the following procedure to check the volume outside your production
environment.

###### Important

This procedure may cause the loss of write I/Os that were suspended when
volume I/O was disabled.

###### To perform a consistency check on a volume in isolation

1. Stop any applications from using the volume.
2. Detach the volume from the instance. For more information, see [Detach an Amazon EBS volume from an Amazon EC2 instance](ebs-detaching-volume.md "ebs-detaching-volume.md").
3. Enable I/O on the volume. Use one of the following methods.

Console

###### To enable I/O for a volume

    1. Open the Amazon EC2 console at
     [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
    2. In the navigation pane, choose **Events**.
    3. Select the volume that you detached in the previous step.
    4. Choose **Actions**, **Enable I/O**.

AWS CLI

###### To enable I/O for a volume

Use the [enable-volume-io](../../../cli/latest/reference/ec2/enable-volume-io.md "../../../cli/latest/reference/ec2/enable-volume-io.md") command.

```
aws ec2 enable-volume-io --volume-id `vol-01234567890abcdef`
```

PowerShell

###### To enable I/O for a volume

Use the [Enable-EC2VolumeIO](../../../powershell/latest/reference/items/Enable-EC2VolumeIO.md "../../../powershell/latest/reference/items/Enable-EC2VolumeIO.md") cmdlet.

```
Enable-EC2VolumeIO -VolumeId `vol-01234567890abcdef`
```

4. Attach the volume to another instance. For more information, see [Launch your instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") and
   [Attach an Amazon EBS volume to an Amazon EC2 instance](ebs-attaching-volume.md "ebs-attaching-volume.md").
5. Check the data on the volume.
   1. Run the **fsck** (Linux instances) or **chkdsk**
      (Windows instances) command.
   2. (Optional) Review any available application or system logs for
      relevant error messages.
   3. If the volume has been impaired for more than 20 minutes, you can
      contact the AWS Support Center. Choose
      **Troubleshoot**, and then in the
      troubleshooting dialog box, choose **Contact
      Support** to submit a support case.

## Option 3: Delete the volume if you no longer need

it

If you want to remove the volume from your environment, simply delete it. For
information about deleting a volume, see [Delete an Amazon EBS volume](ebs-deleting-volume.md "ebs-deleting-volume.md").

If you have a recent snapshot that backs up the data on the volume, you can create
a new volume from the snapshot. For more information, see [Create an Amazon EBS volume](ebs-creating-volume.md "ebs-creating-volume.md").
