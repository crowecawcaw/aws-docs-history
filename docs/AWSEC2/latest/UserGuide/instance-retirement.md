# Instance retirement

An instance is scheduled to be retired when AWS detects irreparable failure of the
underlying hardware that hosts the instance. The instance root volume type determines the
behavior of instance retirement:

- If your instance root volume is an Amazon EBS volume, the instance is stopped, and you
  can start it again at any time. Starting the stopped instance migrates it to new
  hardware.
- If your instance root volume is an instance store volume, the instance is
  terminated, and can't be used again.
  For more information about the types of instance events, see [Scheduled events for Amazon EC2
  instances](monitoring-instances-status-check_sched.md "monitoring-instances-status-check_sched.md").

###### Contents

- [Identify instances scheduled for retirement](#instance-retirement-identify "#instance-retirement-identify")
- [Actions to take for EBS-backed
  instances scheduled for retirement](#instance-retirement-actions-EBS "#instance-retirement-actions-EBS")
- [Actions to take for instance-store backed instances scheduled for retirement](#instance-retirement-actions-instance-store "#instance-retirement-actions-instance-store")

## Identify instances scheduled for retirement

If your instance is scheduled for retirement, you receive an email prior to the event
with the instance ID and retirement date. You can also check for instances that are
scheduled for retirement.

###### Important

If an instance is scheduled for retirement, we recommend that you take action as
soon as possible, because the instance might already be unreachable. For more
information, see [Check if your instance is reachable](#check-instance "#check-instance").

###### Options to identify instances scheduled for retirement

- [Monitor the email for the account contacts](#identify-by-email "#identify-by-email")
- [Check your instances](#identify-in-console-cli "#identify-in-console-cli")

### Monitor the email for the account contacts

If an instance is scheduled for retirement, the primary contact for the
account and the operations contact receive an email prior to the event.
This email includes the instance ID and scheduled retirement date. For more
information, see [Update the primary contact for your AWS account](../../../accounts/latest/reference/manage-acct-update-contact-primary.md "../../../accounts/latest/reference/manage-acct-update-contact-primary.md") and [Update the alternate contacts for your AWS account](../../../accounts/latest/reference/manage-acct-update-contact-alternate.md "../../../accounts/latest/reference/manage-acct-update-contact-alternate.md") in the
_AWS Account Management Reference Guide_.

### Check your instances

If you use an email account that you do not check regularly, you might miss
an instance retirement notification. You can check whether any of your instances
are scheduled for retirement at any time.

Console

###### To identify instances scheduled for retirement

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **EC2 Dashboard**. Under
   **Scheduled events**, you can see the events that are
   associated with your Amazon EC2 instances and volumes, organized by
   Region.

![Scheduled events](images/dashboard-scheduled-events.png) 3. If you have an instance with a scheduled event listed, select its link below the
Region name to go to the **Events** page. 4. The **Events** page lists all resources that have events
associated with them. To view instances that are scheduled for retirement,
select **Instance resources** from the first filter list,
and then **Instance stop or retirement** from the second
filter list. 5. If the filter results show that an instance is scheduled for retirement, select
it, and note the date and time in the **Start time** field in the
details pane. This is your instance retirement date.

AWS CLI

###### To find instances scheduled for retirement

Use the following [describe-instance-status](../../../cli/latest/reference/ec2/describe-instance-status.md "../../../cli/latest/reference/ec2/describe-instance-status.md")
command. Repeat in each Region where you have running instances.

```
aws ec2 describe-instance-status --filters Name=event.code,Values=instance-retirement
```

PowerShell

###### To find instances scheduled for retirement

Use the [Get-EC2InstanceStatus](../../../powershell/latest/reference/items/Get-EC2InstanceStatus.md "../../../powershell/latest/reference/items/Get-EC2InstanceStatus.md")
cmdlet. Repeat in each Region where you have running instances.

```
Get-EC2InstanceStatus -Filter @{Name="event.code"; Values="instance-retirement"}
```

## Actions to take for EBS-backed

instances scheduled for retirement

To preserve the data on your retiring instance, you can perform one of the following
actions. It's important that you take this action before the instance retirement date to
prevent unforeseen downtime and data loss.

For Linux instances, if you are not sure whether your instance is backed by EBS or
instance store, see [Root volumes for your Amazon EC2 instances](RootDeviceStorage.md "RootDeviceStorage.md").

Check if your instance is
reachable

When you are notified that your instance is scheduled for retirement, we recommend
that you take the following action as soon as possible:

- Check if your instance is reachable by either [connecting to](connect.md "connect.md") or pinging your instance.
- If your instance is reachable, you should plan to stop/start your instance at
  an appropriate time before the scheduled retirement date, when the impact is
  minimal. For more information about stopping and starting your instance, and
  what to expect when your instance is stopped, such as the effect on public,
  private, and Elastic IP addresses that are associated with your instance, see
  [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md"). Note that data on
  instance store volumes is lost when you stop and start your instance.
- If your instance is unreachable, you should take immediate action and perform
  a [stop/start](Stop_Start.md "Stop_Start.md") to recover your instance.
- Alternatively, if you want to [terminate](terminating-instances.md "terminating-instances.md") your instance, plan to do so as soon as possible so that
  you stop incurring charges for the instance.

###### Create a backup of your instance

Create an EBS-backed AMI from your instance so that you have a backup. To ensure
data integrity, stop the instance before you create the AMI. You can wait for the
scheduled retirement date when the instance is stopped, or stop the instance
yourself before the retirement date. You can start the instance again at any time.
For more information, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

###### Launch a replacement instance

After you create an AMI from your instance, you can use the AMI to launch a
replacement instance. From the Amazon EC2 console, select your new AMI and then choose
**Launch instance from AMI**. Configure the parameters for your
instance and then choose **Launch instance**. For more information
about each field, see [Launch an EC2 instance using the launch
instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

## Actions to take for instance-store backed instances scheduled for retirement

To preserve the data on your retiring instance, you can perform one of the
following actions. It's important that you take this action before the instance
retirement date to prevent unforeseen downtime and data loss.

###### Warning

If your instance has an instance store root volume and it passes its retirement date, it is
terminated and you cannot recover the instance or any data that was stored on it.
Regardless of the root volume type of your instance, the data on instance store
volumes is lost when the instance is retired, even if the volumes are attached to an
instance with an EBS root volume.

###### Check if your instance is reachable

When you are notified that your instance is scheduled for retirement, we recommend
that you take the following action as soon as possible:

- Check if your instance is reachable by either [connecting](connect-to-linux-instance.md "connect-to-linux-instance.md") to or pinging your
  instance.
- If your instance is unreachable, there is likely very little that can be
  done to recover your instance. For more information, see [Troubleshoot an unreachable Amazon EC2 instance](troubleshoot-unreachable-instance.md "troubleshoot-unreachable-instance.md"). AWS will
  terminate your instance on the scheduled retirement date, so, for an
  unreachable instance, you can immediately [terminate](terminating-instances.md "terminating-instances.md") the instance
  yourself.

###### Launch a replacement instance

Create an Amazon S3-backed AMI from your instance using the AMI tools, as described
in [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md"). From the Amazon EC2 console, select
your new AMI and then choose **Launch instance from AMI**.
Configure the parameters for your instance and then choose **Launch
instance**. For more information about each field, see [Launch an EC2 instance using the launch
instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

###### Convert your instance to an EBS-backed instance

Transfer your data to an EBS volume, take a snapshot of the volume, and then create
AMI from the snapshot. You can launch a replacement instance from your new AMI. For
more information, see [Convert your Amazon S3-backed AMI to an
EBS-backed AMI](Using_ConvertingS3toEBS.md "Using_ConvertingS3toEBS.md").
