# Create alarms to stop, terminate, reboot, or recover an EC2

instance

Using Amazon CloudWatch alarm actions, you can create alarms that automatically stop, terminate,
reboot, or recover your EC2 instances. You can use the stop or terminate actions
to help you save money when you no longer need an instance to be running. You can use the reboot
and recover actions to automatically reboot those instances or recover them onto new hardware if
a system impairment occurs.

There are a number of scenarios in which you might want to automatically stop or terminate
your instance. For example, you might have instances dedicated to batch payroll processing jobs
or scientific computing tasks that run for a period of time and then complete their work. Rather
than letting those instances sit idle (and accrue charges), you can stop or terminate them,
which helps you to save money. The main difference between using the stop and the terminate
alarm actions is that you can easily restart a stopped instance if you need to run it again
later. You can also keep the same instance ID and root volume. However, you cannot restart a
terminated instance. Instead, you must launch a new instance.

You can add the stop, terminate, or reboot, actions to any alarm that is set on an
Amazon EC2 per-instance metric, including basic and detailed monitoring metrics provided by Amazon CloudWatch
(in the AWS/EC2 namespace), in addition to any custom metrics that include the "InstanceId="
dimension, as long as the InstanceId value refers to a valid running Amazon EC2 instance. You can also add
the recover action to alarms that is set on any Amazon EC2 per-instance metric except for `StatusCheckFailed_Instance`.

###### Important

Alarms configured on Amazon EC2 metrics can temporarily enter the INSUFFICIENT_DATA state if
there are missing metric data points. This is rare, but can happen when the
metric reporting is interrupted, even when the Amazon EC2 instance is healthy. For alarms on Amazon EC2 metrics that are
configured to take stop, terminate, reboot, or recover actions, we recommend that you configure those
alarms to treat missing data as `missing`, and to have these alarms trigger only when in the ALARM state.

For more information about how you can configure CloudWatch to act on missing metrics that have alarms set
on them, see [Configuring how CloudWatch alarms treat missing
data](AlarmThatSendsEmail.md#alarms-and-missing-data "AlarmThatSendsEmail.md#alarms-and-missing-data").

To set up a CloudWatch alarm action that can reboot, stop, or terminate an instance, you must use a service-linked IAM role,
_AWSServiceRoleForCloudWatchEvents_. The AWSServiceRoleForCloudWatchEvents IAM
role enables AWS to perform alarm actions on your behalf.

To create the service-linked role for CloudWatch Events, use the following command:

```
aws iam create-service-linked-role --aws-service-name events.amazonaws.com
```

###### Console support

You can create alarms using the CloudWatch console or the Amazon EC2 console.
The procedures in this documentation use the CloudWatch console.
For procedures that use the Amazon EC2 console, see [Create alarms that stop, terminate, reboot, or rcover an instance](../../../AWSEC2/latest/UserGuide/UsingAlarmActions.md "../../../AWSEC2/latest/UserGuide/UsingAlarmActions.md")
in the _Amazon EC2 User Guide_.

###### Permissions

If you are using an AWS Identity and Access Management (IAM) account to create or modify an alarm that performs
EC2 actions or Systems Manager OpsItem actions, you must
have the `iam:CreateServiceLinkedRole` permission.

###### Contents

- [Adding stop actions to Amazon CloudWatch alarms](#AddingStopActions "#AddingStopActions")
- [Adding terminate actions to Amazon CloudWatch alarms](#AddingTerminateActions "#AddingTerminateActions")
- [Adding reboot actions to Amazon CloudWatch alarms](#AddingRebootActions "#AddingRebootActions")
- [Adding recover actions to Amazon CloudWatch alarms](#AddingRecoverActions "#AddingRecoverActions")
- [Viewing the history of triggered alarms and actions](#ViewAlarmHistory "#ViewAlarmHistory")

## Adding stop actions to Amazon CloudWatch alarms

You can create an alarm that stops an Amazon EC2 instance when a certain threshold has been
met. For example, you may run development or test instances and occasionally forget to shut
them off. You can create an alarm that is triggered when the average CPU utilization
percentage has been lower than 10 percent for 24 hours, signaling that it is idle and no
longer in use. You can adjust the threshold, duration, and period to suit your needs, plus
you can add an SNS notification, so that you will receive an email when the
alarm is triggered.

Amazon EC2 instances that use an Amazon Elastic Block Store volume as the root device can be stopped or
terminated, whereas instances that use the instance store as the root device can only be
terminated.

###### To create an alarm to stop an idle instance using the Amazon CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select Metric**.
5. For **AWS namespaces**, choose **EC2**.
6. Do the following:
   1. Choose **Per-Instance Metrics**.
   2. Select the check box in the row with the correct instance and the **CPUUtilization** metric.
   3. Choose the **Graphed metrics** tab.
   4. For the statistic, choose **Average**.
   5. Choose a period (for example, `1 Hour`).
   6. Choose **Select metric**.

7. Under **Conditions**, do the following:
   1. Choose **Static**.
   2. Under **Whenever CPUUtilization is**, choose **Lower**.
   3. For **than**, type `10`.
   4. Choose **Next**.
   5. Under **Notification**, for **Send notification
      to**, choose an existing SNS topic or create a new one.

   To create an SNS topic, choose **New list**. For **Send
   notification to**, type a name for the SNS topic (for example,
   Stop_EC2_Instance). For **Email list**, type a comma-separated list
   of email addresses to be notified when the alarm changes to the `ALARM`
   state. Each email address is sent a topic subscription confirmation email. You must
   confirm the subscription before notifications can be sent to an email address. 6. Choose **Add EC2 Action**. 7. For **Alarm state trigger**, choose **In alarm**.
   For **Take the following action**, choose **Stop
   this instance**. 8. Choose **Next**. 9. Enter a name and description for the alarm. The name must contain only ASCII
   characters. Then choose **Next**. 10. Under **Preview and create**, confirm that the information and conditions are what you want, then
   choose **Create alarm**.

## Adding terminate actions to Amazon CloudWatch alarms

You can create an alarm that terminates an EC2 instance automatically when a certain
threshold has been met (as long as termination protection is not enabled for the instance).
For example, you might want to terminate an instance when it has completed its work, and you
don't need the instance again. If you might want to use the instance later, you should stop
the instance instead of terminating it. For information about enabling and disabling
termination protection for an instance, see [Enabling Termination Protection for an Instance](../../../AWSEC2/latest/UserGuide/Using_ChangingDisableAPITermination.md "../../../AWSEC2/latest/UserGuide/Using_ChangingDisableAPITermination.md") in the
_Amazon EC2 User Guide_.

###### To create an alarm to terminate an idle instance using the Amazon CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **Create
   Alarm**.
3. For the **Select Metric** step, do the following:
   1. Under **EC2 Metrics**, choose **Per-Instance Metrics**.
   2. Select the row with the instance and the **CPUUtilization** metric.
   3. For the statistic, choose **Average**.
   4. Choose a period (for example, `1 Hour`).
   5. Choose **Next**.

4. For the **Define Alarm** step, do the following:
   1. Under **Alarm Threshold**, type a unique name for the alarm (for example,
      Terminate EC2 instance) and a description of the alarm (for example, Terminate EC2 instance
      when CPU is idle for too long). Alarm names must contain only ASCII characters.
   2. Under **Whenever**, for **is**, choose **<**
      and type `10`. For **for**, type `24`
      consecutive periods.

   A graphical representation of the threshold is shown under **Alarm
   Preview**. 3. Under **Notification**, for **Send notification
   to**, choose an existing SNS topic or create a new one.

   To create an SNS topic, choose **New list**. For **Send
   notification to**, type a name for the SNS topic (for example,
   Terminate_EC2_Instance). For **Email list**, type a comma-separated
   list of email addresses to be notified when the alarm changes to the
   `ALARM` state. Each email address is sent a topic subscription
   confirmation email. You must confirm the subscription before notifications can be sent
   to an email address. 4. Choose **EC2 Action**. 5. For **Whenever this alarm**, choose **State is
   ALARM**. For **Take this action**, choose
   **Terminate this instance**. 6. Choose **Create Alarm**.

## Adding reboot actions to Amazon CloudWatch alarms

You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and automatically reboots
the instance. The reboot alarm action is recommended for Instance Health Check failures (as
opposed to the recover alarm action, which is suited for System Health Check failures). An
instance reboot is equivalent to an operating system reboot. In most cases, it takes only a
few minutes to reboot your instance. When you reboot an instance, it remains on the same
physical host, so your instance keeps its public DNS name, private IP address, and any data on
its instance store volumes.

Rebooting an instance doesn't start a new instance billing hour, unlike stopping and
restarting your instance. For more information about rebooting an instance, see [Reboot Your Instance](../../../AWSEC2/latest/UserGuide/ec2-instance-reboot.md "../../../AWSEC2/latest/UserGuide/ec2-instance-reboot.md") in the
_Amazon EC2 User Guide_.

###### Important

To avoid a race condition between the reboot and recover actions, avoid
setting the same evaluation period for both a reboot alarm and a recover alarm. We recommend that you set
reboot alarms to three evaluation periods of one minute each.

###### To create an alarm to reboot an instance using the Amazon CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **Create
   Alarm**.
3. For the **Select Metric** step, do the following:
   1. Under **EC2 Metrics**, choose **Per-Instance Metrics**.
   2. Select the row with the instance and the **StatusCheckFailed_Instance** metric.
   3. For the statistic, choose **Minimum**.
   4. Choose a period (for example, `1 Minute`).
   5. Choose
      **Next**.

4. For the **Define Alarm** step, do the following:
   1. Under **Alarm Threshold**, type a unique name for the alarm (for example,
      Reboot EC2 instance) and a description of the alarm (for example, Reboot EC2 instance when
      health checks fail). Alarm names must contain only ASCII characters.
   2. Under **Whenever**, for **is**, choose **>**
      and type `0`. For **for**, type `3`
      consecutive periods.

   A graphical representation of the threshold is shown under **Alarm
   Preview**. 3. Under **Notification**, for **Send notification
   to**, choose an existing SNS topic or create a new one.

   To create an SNS topic, choose **New list**. For **Send
   notification to**, type a name for the SNS topic (for example,
   Reboot_EC2_Instance). For **Email list**, type a comma-separated list
   of email addresses to be notified when the alarm changes to the `ALARM`
   state. Each email address is sent a topic subscription confirmation email. You must
   confirm the subscription before notifications can be sent to an email address. 4. Choose **EC2 Action**. 5. For **Whenever this alarm**, choose **State is
   ALARM**. For **Take this action**, choose **Reboot
   this instance**. 6. Choose **Create Alarm**.

## Adding recover actions to Amazon CloudWatch alarms

You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and automatically
recovers the instance if it becomes impaired due to an underlying hardware failure or a
problem that requires AWS involvement to repair. Terminated instances cannot be recovered. A
recovered instance is identical to the original instance, including the instance ID, private
IP addresses, Elastic IP addresses, and all instance metadata.

When the `StatusCheckFailed_System` alarm is triggered, and the recover
action is initiated, you will be notified by the Amazon SNS topic that you chose when you
created the alarm and associated the recover action. During instance recovery, the instance
is migrated during an instance reboot, and any data that is in-memory is lost. When the
process is complete, information is published to the SNS topic you've configured for the
alarm. Anyone who is subscribed to this SNS topic will receive an email notification that
includes the status of the recovery attempt and any further instructions. You will notice an
instance reboot on the recovered instance.

The recover action can be used only with `StatusCheckFailed_System`, not with `StatusCheckFailed_Instance`.

Examples of problems that cause system status checks to fail include:

- Loss of network connectivity
- Loss of system power
- Software issues on the physical host
- Hardware issues on the physical host that impact network reachability

The recover action is supported only on some instance types. For more information about supported instance types
and other requirements, see
[Recover your instance](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md") and
[Requirements](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md#requirements-for-recovery "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md#requirements-for-recovery").

###### Important

To avoid a race condition between the reboot and recover actions, avoid setting the same evaluation period
for both a reboot alarm and a recover alarm. We recommend that you set recover alarms to
two evaluation periods of one minute each and reboot alarms to three evaluation periods of one minute each.

###### To create an alarm to recover an instance using the Amazon CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All alarms**.
3. Choose **Create
   Alarm**.
4. Choose **Select Metric** and then do the following:
   1. Choose **EC2 Metrics**, **Per-Instance Metrics**.
   2. Select the row with the instance and the **StatusCheckFailed_System** metric, and then choose **Select metric**.
   3. For the statistic, choose **Minimum**.
   4. Choose a period (for example, `1 Minute`).

   ###### Important

   To avoid a race condition between the reboot and recover actions, avoid
   setting the same evaluation period for both a reboot alarm and a recover alarm. We recommend that you set
   recover alarms to two evaluation periods of one minute each.

5. For **Conditions**, do the following:
   1. Under **Threshold type**, choose **Static**.
   2. Under **Whenever**, choose **Greater**
      and enter `0` for **than...**.
   3. Choose **Additional configuration**, then for **Datapoints to alarm**
      specify 2 **out of** 2.

6. Choose **Next**.
7. Under **Notification**, do the following:
   1. For **Alarm state trigger**, choose **In alarm**.
   2. For **Send notification
      to the following SNS topic**, choose an existing SNS topic or create a new one.
   3. Choose **Add EC2 Action**.
   4. For **Alarm state trigger**, choose **In alarm**.
   5. For **Take the following action**, choose
      **Recover this instance**.
   6. Choose **Next**.

8. For **Alarm name**, type a unique name for the alarm (for example,
   `Recover EC2 instance`) and a description of the alarm (for example, `Recover EC2 instance when 
health checks fail`). Alarm names must contain only ASCII characters.
9. Choose **Next**.
10. Choose **Create Alarm**.

## Viewing the history of triggered alarms and actions

You can view alarm and action history in the Amazon CloudWatch console. Amazon CloudWatch keeps the last 30 days of alarm and action history.

###### To view the history of triggered alarms and actions

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms** and select an alarm.
3. To view the most recent state transition along with the time and metric values, choose
   **Details**.
4. To view the most recent history entries, choose **History**.
