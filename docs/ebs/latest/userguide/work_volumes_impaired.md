

# Work with an impaired Amazon EBS volume
<a name="work_volumes_impaired"></a>

Use the following options if a volume is impaired because the volume's data is potentially inconsistent.

**Topics**
+ [Option 1: Perform a consistency check on the volume attached to its instance](#work_volumes_impaired_option1)
+ [Option 2: Perform a consistency check on the volume using another instance](#work_volumes_impaired_option2)
+ [Option 3: Delete the volume if you no longer need it](#work_volumes_impaired_option3)

## Option 1: Perform a consistency check on the volume attached to its instance
<a name="work_volumes_impaired_option1"></a>

The simplest option is to enable I/O and then perform a data consistency check on the volume while the volume is still attached to its Amazon EC2 instance.

**To perform a consistency check on an attached volume**

1. Stop any applications from using the volume.

1. Enable I/O on the volume. Use one of the following methods.

------
#### [ Console ]

**To enable I/O for a volume**

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. In the navigation pane, choose **Events**.

   1. Select the volume.

   1. Choose **Actions**, **Enable I/O**.

------
#### [ AWS CLI ]

**To enable I/O for a volume**  
Use the [enable-volume-io](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-volume-io.html) command.

   ```
   aws ec2 enable-volume-io --volume-id {{vol-01234567890abcdef}}
   ```

------
#### [ PowerShell ]

**To enable I/O for a volume**  
Use the [Enable-EC2VolumeIO](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2VolumeIO.html) cmdlet.

   ```
   Enable-EC2VolumeIO -VolumeId {{vol-01234567890abcdef}}
   ```

------

1. Check the data on the volume.

   1. Run the **fsck** (Linux instances) or **chkdsk** (Windows instances) command.

   1. (Optional) Review any available application or system logs for relevant error messages.

   1. If the volume has been impaired for more than 20 minutes, you can contact the AWS Support Center. Choose **Troubleshoot**, and then in the **Troubleshoot Status Checks** dialog box, choose **Contact Support** to submit a support case.

## Option 2: Perform a consistency check on the volume using another instance
<a name="work_volumes_impaired_option2"></a>

Use the following procedure to check the volume outside your production environment.

**Important**  
This procedure may cause the loss of write I/Os that were suspended when volume I/O was disabled.

**To perform a consistency check on a volume in isolation**

1. Stop any applications from using the volume.

1. Detach the volume from the instance. For more information, see [Detach an Amazon EBS volume from an Amazon EC2 instance](ebs-detaching-volume.md).

1. Enable I/O on the volume. Use one of the following methods.

------
#### [ Console ]

**To enable I/O for a volume**

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. In the navigation pane, choose **Events**.

   1. Select the volume that you detached in the previous step.

   1. Choose **Actions**, **Enable I/O**.

------
#### [ AWS CLI ]

**To enable I/O for a volume**  
Use the [enable-volume-io](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-volume-io.html) command.

   ```
   aws ec2 enable-volume-io --volume-id {{vol-01234567890abcdef}}
   ```

------
#### [ PowerShell ]

**To enable I/O for a volume**  
Use the [Enable-EC2VolumeIO](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2VolumeIO.html) cmdlet.

   ```
   Enable-EC2VolumeIO -VolumeId {{vol-01234567890abcdef}}
   ```

------

1. Attach the volume to another instance. For more information, see [Launch your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) and [Attach an Amazon EBS volume to an Amazon EC2 instance](ebs-attaching-volume.md).

1. Check the data on the volume.

   1. Run the **fsck** (Linux instances) or **chkdsk** (Windows instances) command.

   1. (Optional) Review any available application or system logs for relevant error messages.

   1. If the volume has been impaired for more than 20 minutes, you can contact the AWS Support Center. Choose **Troubleshoot**, and then in the troubleshooting dialog box, choose **Contact Support** to submit a support case.

## Option 3: Delete the volume if you no longer need it
<a name="work_volumes_impaired_option3"></a>

If you want to remove the volume from your environment, simply delete it. For information about deleting a volume, see [Delete an Amazon EBS volume](ebs-deleting-volume.md).

If you have a recent snapshot that backs up the data on the volume, you can create a new volume from the snapshot. For more information, see [Create an Amazon EBS volume](ebs-creating-volume.md).