

# Troubleshoot an unreachable Amazon EC2 instance
<a name="troubleshoot-unreachable-instance"></a>

The following information can help you troubleshoot unreachable Amazon EC2 instances. You can capture screenshots or access console output to help diagnose problems and determine if you should reboot your instance. For unreachable Windows instances, troubleshoot by reviewing screenshots returned by the service. 

**Topics**
+ [Instance reboot](#instance-console-rebooting)
+ [Instance console output](#instance-console-console-output)
+ [Capture a screenshot of an unreachable instance](#instance-console-screenshot)
+ [Common screenshots for Windows instances](ics-common.md)
+ [Instance recovery when a host computer fails](#instance-machine-failure)
+ [Instance appeared offline and unexpectedly rebooted](#troubleshoot-unavailable-instance-unexpected-reboot)

## Instance reboot
<a name="instance-console-rebooting"></a>

The ability to reboot instances that are otherwise unreachable is valuable for both troubleshooting and general instance management.

Just as you can reset a computer by pressing the reset button, you can reset EC2 instances using the Amazon EC2 console, CLI, or API. For more information, see [Reboot your Amazon EC2 instance](ec2-instance-reboot.md).

## Instance console output
<a name="instance-console-console-output"></a>

Console output is a valuable tool for problem diagnosis. It is especially useful for troubleshooting kernel problems and service configuration issues that could cause an instance to terminate or become unreachable before its SSH daemon can be started. 
+ **Linux instances** – The instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. The console output returns buffered information that was posted shortly after an instance transition state (start, stop, reboot, and terminate). The posted output is not continuously updated; only when it is likely to be of the most value.
+ **Windows instances** – The instance console output includes the last three system event log errors.

Only the instance owner can access the console output.

You can retrieve the latest serial console output during the instance lifecycle. This option is only supported on [Nitro-based instances](instance-types.md#instance-hypervisor-type).

------
#### [ Console ]

**To get console output**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the left navigation pane, choose **Instances**.

1. Select the instance.

1. Choose **Actions**, **Monitor and troubleshoot**, **Get system log**.

------
#### [ AWS CLI ]

**To get console output**  
Use the [get-console-output](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-console-output.html) command.

```
aws ec2 get-console-output --instance-id {{i-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To get console output**  
Use the [Get-EC2ConsoleOutput](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ConsoleOutput.html) cmdlet.

```
Get-EC2ConsoleOutput -InstanceId {{i-1234567890abcdef0}}
```

------

## Capture a screenshot of an unreachable instance
<a name="instance-console-screenshot"></a>

If you are unable to connect to your instance, you can capture a screenshot of your instance and view it as an image. The image can provide visibility as to the status of the instance, and allows for quicker troubleshooting.

You can generate screenshots while the instance is running or after it has crashed. The image is generated in JPG format and is no larger than 100 kb. There is no data transfer cost for the screenshot.

**Limitations**

This feature is not supported for the following:
+ Bare metal instances (instances of type `*.metal`)
+ Instance is using an NVIDIA GRID driver
+ [Instances powered by Arm-based Graviton processors](https://aws.amazon.com/ec2/graviton/#EC2_Instances_Powered_by_AWS_Graviton_Processors)
+ Windows instances on AWS Outposts
+ Windows instances on AWS Local Zones

**Region support**

This feature is not available in the following Regions:
+ Asia Pacific (Thailand)
+ Mexico (Central)
+ GovCloud Regions

------
#### [ Console ]

**To get a screenshot of an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the left navigation pane, choose **Instances**.

1. Select the instance to capture.

1. Choose **Actions**, **Monitor and troubleshoot**, **Get instance screenshot**.

1. Choose **Download**, or open the context (right-click) menu for the image to download and save it.

------
#### [ AWS CLI ]

**To capture a screenshot of an instance**  
Use the [get-console-screenshot](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-console-screenshot.html) command. The output is base64-encoded.

```
aws ec2 get-console-screenshot --instance-id {{i-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To capture a screenshot of an instance**  
Use the [Get-EC2ConsoleScreenshot](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ConsoleScreenshot.html) cmdlet. The output is base64-encoded.

```
Get-EC2ConsoleScreenshot -InstanceId {{i-1234567890abcdef0}}
```

------

## Instance recovery when a host computer fails
<a name="instance-machine-failure"></a>

If there is an unrecoverable issue with the hardware of an underlying host computer, AWS may schedule an instance stop event. You are notified of such an event ahead of time by email.

**To recover an Amazon EBS-backed instance running on a host computer that failed**

1. Back up any important data on your instance store volumes to Amazon EBS or Amazon S3.

1. Stop the instance.

1. Start the instance.

1. Restore any important data.

For more information, see [Stop and start Amazon EC2 instances](Stop_Start.md).

**To recover an instance with an instance store root volume running on a host computer that failed**

1. Create an AMI from the instance.

1. Upload the image to Amazon S3.

1. Back up important data to Amazon EBS or Amazon S3.

1. Terminate the instance.

1. Launch a new instance from the AMI.

1. Restore any important data to the new instance.

## Instance appeared offline and unexpectedly rebooted
<a name="troubleshoot-unavailable-instance-unexpected-reboot"></a>

If your instance appears to have been offline and then unexpectedly rebooted, it might have undergone automatic instance recovery. This happens when AWS detects that the instance is unavailable due to an underlying hardware or software issue, and either simplified automatic recovery or CloudWatch action based recovery is enabled on the instance.

During the recovery process, AWS attempts to restore the instance's availability by migrating it to different hardware. To verify whether automatic instance recovery occurred for your instance, see [Verify if automatic instance recovery occurred](verify-if-automatic-recovery-occurred.md).

**Note**  
If your workload or application is unresponsive, check whether it's running on the instance. If it's not, start it manually. To prevent this issue in the future, implement a recovery plan to ensure your workload or application functions properly after instance recovery.