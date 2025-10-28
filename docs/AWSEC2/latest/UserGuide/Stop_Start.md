# Stop and start Amazon EC2 instances

You can stop and start your instance if it has an Amazon EBS volume as its root volume. When you
stop an instance, it shuts down. When you start an instance, it is typically migrated to a
new underlying host computer and assigned a new public IPv4 address.

An instance stop can be user-initiated (where you manually stop the instance) or initiated
by AWS (in response to a scheduled stop event when AWS detects irreparable failure of
the underlying host for your instance).

For user-initiated stops, we recommend using the Amazon EC2 console, CLI, or API instead of
running the operating system stop command from your instance. When using Amazon EC2, if the
instance does not cleanly shut down within a few minutes, Amazon EC2 performs a hard shut down.
Furthermore, AWS CloudTrail creates an API record of when your instance was stopped.

This topic describes how to perform a user-initiated stop. For information about a stop
performed by AWS, see [Manage Amazon EC2 instances scheduled to
stop or retire](schedevents_actions_retire.md "schedevents_actions_retire.md").

When you stop an instance, it is not deleted. If you decide that you no longer need an
instance, you can terminate it. For more information, see [Terminate Amazon EC2 instances](terminating-instances.md "terminating-instances.md"). If you want to
hibernate an instance to save the contents from the instance memory (RAM), see [Hibernate your Amazon EC2 instance](Hibernate.md "Hibernate.md"). For distinctions between instance
lifecycle actions, see [Differences between instance states](ec2-instance-lifecycle.md#lifecycle-differences "ec2-instance-lifecycle.md#lifecycle-differences").

###### Contents

- [How it
  works](how-ec2-instance-stop-start-works.md "how-ec2-instance-stop-start-works.md")
- [Methods for stopping an instance](instance-stop-methods.md "instance-stop-methods.md")
- [Manually stop and
  start](#starting-stopping-instances "#starting-stopping-instances")
- [Automatically stop
  and start](#stop-start-ec2-instances-on-a-schedule "#stop-start-ec2-instances-on-a-schedule")
- [Find
  running and stopped instances](#find-running-and-stopped-instances-in-globalview "#find-running-and-stopped-instances-in-globalview")
- [Find the initial and most recent launch
  times](#find-initial-launch-time "#find-initial-launch-time")
- [Enable stop protection](ec2-stop-protection.md "ec2-stop-protection.md")

## Manually stop and start your

instances

You can stop and start your Amazon EBS-backed instances (instances with EBS root volumes).
You can't stop and start instances with an instance store root volume.

When using the default method to stop an instance, a graceful operating system (OS)
shutdown is attempted. You can bypass the graceful OS shutdown; however, this might risk
data integrity.

###### Warning

When you stop an instance, the data on any instance store volumes is erased.
Before you stop an instance, verify that you've copied any data that you need from
the instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.

[Linux instances] Using the OS **halt** command from an instance does
not initiate a shutdown. If you use the **halt** command, the instance
does not terminate; instead, it places the CPU into `HLT`, which suspends CPU
operation. The instance remains running.

You can initiate a shutdown using the OS **shutdown** or
**poweroff** commands. When you use an OS command, the instance stops
by default. You can change this behavior. For more information, see [Change instance
initiated shutdown behavior](Using_ChangingInstanceInitiatedShutdownBehavior.md "Using_ChangingInstanceInitiatedShutdownBehavior.md").

###### Note

If you stopped an Amazon EBS-backed instance and it appears "stuck" in the
`stopping` state, you can forcibly stop it. For more information, see
[Troubleshoot Amazon EC2 instance stop issues](TroubleshootingInstancesStopping.md "TroubleshootingInstancesStopping.md").

###### Stop and start methods

- [Stop an instance with a
  graceful OS shutdown](#stop-instance-with-graceful-os-shutdown "#stop-instance-with-graceful-os-shutdown")
- [Stop an instance and
  bypass the graceful OS shutdown](#stop-instance-bypass-graceful-os-shutdown "#stop-instance-bypass-graceful-os-shutdown")
- [Start an instance](#start-ec2-instance "#start-ec2-instance")

### Stop an instance with a

graceful OS shutdown

You can stop an instance using the default stop method, which includes an attempt
at a graceful OS shutdown. For more information, see [Default stop](instance-stop-methods.md#ec2-instance-default-stop "instance-stop-methods.md#ec2-instance-default-stop").

Console

###### To stop an instance using the default stop method

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**, and then select the
   instance.
3. Choose **Instance state**, **Stop instance**. If
   this option is disabled, either the instance is already stopped
   or its root volume is an instance store volume.
4. When prompted for confirmation, choose
   **Stop**. It can take a few minutes for the
   instance to stop.

AWS CLI

###### To stop an instance using the default stop method

Use the [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") command.

```
aws ec2 stop-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To stop an instance using the default stop method

Use the [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") cmdlet

```
Stop-EC2Instance -InstanceId `i-1234567890abcdef0`
```

### Stop an instance and

bypass the graceful OS shutdown

You can bypass the graceful OS shutdown when stopping an instance. For more
information, see [Stop with skip OS
shutdown](instance-stop-methods.md#ec2-instance-stop-with-skip-os-shutdown "instance-stop-methods.md#ec2-instance-stop-with-skip-os-shutdown").

###### Warning

Bypassing the graceful OS shutdown might result in data loss or corruption (for example,
memory contents not flushed to disk or loss of in-flight IOs) or skipped
shutdown scripts.

Console

###### To stop an instance and bypass the graceful OS shutdown

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**
   and select the instance.
3. Choose **Instance state**, **Stop
   instance**.
4. Under **Skip OS shutdown**, select the **Skip OS
   shutdown** checkbox. If you don't see this option
   in the console, it's not yet available in the console in the
   current Region. You can, however, access this feature using the
   AWS CLI or SDK, or try another Region in the console.
5. Choose **Stop**.

AWS CLI

###### To stop an instance and bypass the graceful OS shutdown

Use the [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md")
command with `--skip-os-shutdown`.

```
aws ec2 stop-instances \
    --instance-ids `i-1234567890abcdef0` \
    --skip-os-shutdown
```

PowerShell

###### To stop an instance and bypass the graceful OS shutdown

Use the [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md")
cmdlet with `-SkipOsShutdown $true`.

```
Stop-EC2Instance `
    -InstanceId `i-1234567890abcdef0` `
    -SkipOsShutdown $true
```

### Start an instance

You can start a stopped instance.

Console

###### To start an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. Select the instance, and choose **Instance
   state**, **Start
   instance**.

It can take a few minutes for the instance to enter the
`running` state.

AWS CLI

###### To start an instance

Use the [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") command.

```
aws ec2 start-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To start an instance

Use the [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") cmdlet.

```
Start-EC2Instance -InstanceId `i-1234567890abcdef0`
```

## Automatically stop and start

your instances

You can automate stopping and starting instances with the following services:

**Instance Scheduler on AWS**

You can use Instance Scheduler on AWS to automate the starting and
stopping of EC2 instances. For more information, see [How do
I use Instance Scheduler with CloudFormation to schedule EC2
instances?](https://repost.aws/knowledge-center/stop-start-instance-scheduler "https://repost.aws/knowledge-center/stop-start-instance-scheduler") Note that [additional
charges apply](../../../solutions/latest/instance-scheduler-on-aws/cost.md "../../../solutions/latest/instance-scheduler-on-aws/cost.md").

**AWS Lambda and an Amazon EventBridge rule**

You can use Lambda and an EventBridge rule to stop and start your instances on a
schedule. For more information, see [How do
I use Lambda to stop and start Amazon EC2 instances at regular
intervals?](https://repost.aws/knowledge-center/start-stop-lambda-eventbridge "https://repost.aws/knowledge-center/start-stop-lambda-eventbridge")

**Amazon EC2 Auto Scaling**

To ensure you have the correct number of Amazon EC2 instances available to
handle the load for an application, create Auto Scaling groups.
Amazon EC2 Auto Scaling ensures that your application always has the
right capacity to handle the traffic demand, and saves costs by launching
instances only when they are needed. Note that Amazon EC2 Auto Scaling
terminates, rather than stops, unneeded instances. To set up Auto Scaling
groups, see [Get started with Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.md").

## Find all running and

stopped instances

You can find all of your running and stopped instances across all AWS Regions on a
single page using [Amazon EC2 Global
View](https://console.aws.amazon.com/ec2globalview/home "https://console.aws.amazon.com/ec2globalview/home"). This capability is especially useful for taking inventory and finding
forgotten instances. For information about how to use Global View, see [View resources across Regions using AWS Global
View](global-view.md "global-view.md").

Alternatively, you can run a command or cmdlet in each Region where you have
instances.

AWS CLI

###### To get the number of EC2 instances in a Region

Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command to count the instances in the
current Region. You must run this command in each Region where you have
instances.

```
aws ec2 describe-instances \
    --region `us-east-2` \
    --query "length(Reservations[].Instances[])"
```

The following is example output.

```
27
```

###### To get summary info about your EC2 instances in a Region

Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command. You must run this command in
each Region where you have instances.

```
aws ec2 describe-instances \
    --region `us-east-2` \
    --query "Reservations[].Instances[].[InstanceId,InstanceType,PrivateIpAddress]" \
    --output table
```

The following is example output.

````
---------------------------------------------------------
|                   DescribeInstances                   | +---------------------+---------------+-----------------+
|  i-0e3e777f4362f1bf7|  t2.micro     |  10.0.12.9      |
|  i-09453945dcf1529e9|  t2.micro     |  10.0.143.213   |
|  i-08fd74f3f1595fdbd|  m7i.4xlarge  |  10.0.1.103     | +---------------------+---------------+-----------------+ ``` PowerShell ###### To get the number of EC2 instances in a Region Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet. ``` (Get-EC2Instance -Region `us-east-2`).Instances.Length ``` The following is example output. ``` 27 ``` ###### To get summary info about your EC2 instances in a Region Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet. You must run this command in each Region where you have instances. ``` (Get-EC2Instance).Instances | Select InstanceId, InstanceType, PrivateIpAddress ``` The following is example output. ``` InstanceId          InstanceType PrivateIpAddress ----------          ------------ ---------------- i-0e3e777f4362f1bf7 t2.micro     10.0.12.9 i-09453945dcf1529e9 t2.micro     10.0.143.213 i-08fd74f3f1595fdbd m7i.4xlarge  10.0.1.103 ``` ## Find the initial and most recent launch times When you describe an instance, the launch time for the instance is its most recent launch time. After you stop and start an instance, the launch time reflects the new instance start time. To find the initial launch time for an instance, even after stopping and starting it, view the time at which the primary network interface was attached to the instance. Console ###### To find the most recent launch time Select the instance and find **Launch time** under **Instance details** on the **Details** tab. ###### To find the initial launch time Select the instance and find the primary network interface (device index is 0) under **Network interfaces** on the **Networking** tab. AWS CLI ###### To find the initial and most recent launch times Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command to display both the initial launch time and the most recent launch time for the specified instance. ``` aws ec2 describe-instances \ --instance-id `i-1234567890abcdef0` \ --query 'Reservations[].Instances[].{InstanceID:InstanceId,InitialLaunch:NetworkInterfaces[0].Attachment.AttachTime,LastLaunch:LaunchTime}' ``` The following is example output. ``` [ { "InstanceID": "i-1234567890abcdef0", "InitialLaunch": "2024-04-19T00:47:08+00:00", "LastLaunch": "2024-05-27T06:24:06+00:00" } ] ``` PowerShell ###### To find the most recent launch time Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet. ``` (Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances.LaunchTime ``` The following is example output. ``` Monday, May 27, 2024 6:24:06 AM ``` ###### To find the initial launch time Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet. ``` (Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances.NetworkInterfaces.Attachment.AttachTime ``` The following is example output. ``` Friday, April 19, 2024 12:47:08 AM ```
````
