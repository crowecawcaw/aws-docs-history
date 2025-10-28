# Create alarms that stop, terminate, reboot, or recover an

instance

Using Amazon CloudWatch alarm actions, you can create alarms that automatically stop, terminate,
reboot, or recover your instances. You can use the stop or terminate actions to help you save
money when you no longer need an instance to be running. You can use the reboot and recover
actions to automatically reboot those instances or recover them onto new hardware if a system
impairment occurs.

###### Note

For Amazon CloudWatch alarms billing and pricing information, see [CloudWatch billing and
cost](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md") in the _Amazon CloudWatch User Guide_.

The `AWSServiceRoleForCloudWatchEvents` service-linked role enables AWS to
perform alarm actions on your behalf. The first time you create an alarm in the AWS Management Console, the
AWS CLI, or the IAM API, CloudWatch creates the service-linked role for you.

There are a number of scenarios in which you might want to automatically stop or terminate
your instance. For example, you might have instances dedicated to batch payroll processing jobs
or scientific computing tasks that run for a period of time and then complete their work. Rather
than letting those instances sit idle (and accrue charges), you can stop or terminate them,
which can help you to save money. The main difference between using the stop and the terminate
alarm actions is that you can easily start a stopped instance if you need to run it again later,
and you can keep the same instance ID and root volume. However, you cannot start a terminated
instance. Instead, you must launch a new instance. When an instance is stopped or terminated,
data on instance store volumes is lost.

You can add the stop, terminate, reboot, or recover actions to any alarm that is set on an
Amazon EC2 per-instance metric, including basic and detailed monitoring metrics provided by Amazon CloudWatch
(in the `AWS/EC2` namespace), as well as any custom metrics that include the
`InstanceId` dimension, as long as its value refers to a valid running Amazon EC2
instance.

###### Important

Status check alarms can temporarily enter the `INSUFFICIENT_DATA`
state if there are missing metric data points. Although rare, this can happen when there is
an interruption in the metric reporting systems, even when an instance is healthy. We recommend
that you treat the `INSUFFICIENT_DATA` state as missing data instead of an alarm
breach, especially when configuring the alarm to stop, terminate, reboot, or recover an instance.

###### Console support

You can create alarms using the Amazon EC2 console or the CloudWatch console. The procedures in this
documentation use the Amazon EC2 console. For procedures that use the CloudWatch console, see [Create alarms that stop, terminate, reboot, or
recover an instance](../../../AmazonCloudWatch/latest/monitoring/UsingAlarmActions.md "../../../AmazonCloudWatch/latest/monitoring/UsingAlarmActions.md") in the _Amazon CloudWatch User Guide_.

###### Permissions

You must have the `iam:CreateServiceLinkedRole` to create or modify an alarm
that performs EC2 alarm actions.

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Contents

- [Add stop actions to Amazon CloudWatch alarms](#AddingStopActions "#AddingStopActions")
- [Add terminate actions to Amazon CloudWatch alarms](#AddingTerminateActions "#AddingTerminateActions")
- [Add reboot actions to Amazon CloudWatch alarms](#AddingRebootActions "#AddingRebootActions")
- [Add recover actions to Amazon CloudWatch alarms](#AddingRecoverActions "#AddingRecoverActions")
- [Amazon CloudWatch alarm action scenarios](AlarmActionScenarios.md "AlarmActionScenarios.md")

## Add stop actions to Amazon CloudWatch alarms

You can create an alarm that stops an Amazon EC2 instance when a certain threshold has been
met. For example, you may run development or test instances and occasionally forget to shut
them off. You can create an alarm that is triggered when the average CPU utilization
percentage has been lower than 10 percent for 24 hours, signaling that it is idle and no
longer in use. You can adjust the threshold, duration, and period to suit your needs, plus you
can add an Amazon Simple Notification Service (Amazon SNS) notification so that you receive an email when the alarm is
triggered.

Instances that use an Amazon EBS volume as the root volume can be stopped or terminated,
whereas instances that use the instance store as the root volume can only be terminated. Data
on instance store volumes is lost when the instance is terminated or stopped.

###### To create an alarm to stop an idle instance (Amazon EC2 console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Actions**, **Monitor
   and troubleshoot**, **Manage CloudWatch alarms**.

Alternatively, you can choose the plus sign (
![Plus sign.](images/add-plus.png)
) in the **Alarm status** column. 4. On the **Manage CloudWatch alarms** page, do the
following:

    1. Choose **Create an alarm**.
    2. To receive an email when the alarm is triggered, for **Alarm
     notification**, choose an existing Amazon SNS topic. You first need to create an
     Amazon SNS topic using the Amazon SNS console. For more information, see [Using Amazon SNS for
     application-to-person (A2P) messaging](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md") in the *Amazon Simple Notification Service Developer Guide*.
    3. Toggle on **Alarm action**, and choose
     **Stop**.
    4. For **Group samples by** and **Type of data to
     sample**, choose a statistic and a metric. In this example, choose
     **Average** and **CPU utilization**.
    5. For **Alarm When** and **Percent**,
     specify the metric threshold. In this example, specify
     **<=** and **10** percent.
    6. For **Consecutive period** and **Period**,
     specify the evaluation period for the alarm. In this example, specify
     **1** consecutive period of **5
     Minutes**.
    7. Amazon CloudWatch automatically creates an alarm name for you. To change the name,
     for **Alarm name**, enter a new name. Alarm names must contain
     only ASCII characters.


    ###### Note

    You can adjust the alarm configuration based on your own requirements
     before creating the alarm, or you can edit them later. This includes the
     metric, threshold, duration, action, and notification settings. However, after
     you create an alarm, you cannot edit its name later.
    8. Choose **Create**.

## Add terminate actions to Amazon CloudWatch alarms

You can create an alarm that terminates an EC2 instance automatically when a certain
threshold has been met (as long as termination protection is not enabled for the instance).
For example, you might want to terminate an instance when it has completed its work, and you
don’t need the instance again. If you might want to use the instance later, you should stop
the instance instead of terminating it. Data on instance store volumes is lost when the
instance is terminated. For information about enabling and disabling termination protection
for an instance, see [Change instance termination
protection](Using_ChangingDisableAPITermination.md "Using_ChangingDisableAPITermination.md").

###### To create an alarm to terminate an idle instance (Amazon EC2 console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Actions**, **Monitor
   and troubleshoot**, **Manage CloudWatch alarms**.

Alternatively, you can choose the plus sign (
![Plus sign.](images/add-plus.png)
) in the **Alarm status** column. 4. On the **Manage CloudWatch alarms** page, do the
following:

    1. Choose **Create an alarm**.
    2. To receive an email when the alarm is triggered, for **Alarm
     notification**, choose an existing Amazon SNS topic. You first need to
     create an Amazon SNS topic using the Amazon SNS console. For more information,
     see [Using Amazon SNS for application-to-person (A2P) messaging](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md") in the
     *Amazon Simple Notification Service Developer Guide*.
    3. Toggle on **Alarm action**, and choose
     **Terminate**.
    4. For **Group samples by** and **Type of data to
     sample**, choose a statistic and a metric. In this example, choose
     **Average** and **CPU utilization**.
    5. For **Alarm When** and **Percent**,
     specify the metric threshold. In this example, specify **=>**
     and **10** percent.
    6. For **Consecutive period** and **Period**,
     specify the evaluation period for the alarm. In this example, specify
     **24** consecutive periods of **1
     Hour**.
    7. Amazon CloudWatch automatically creates an alarm name for you. To change the name,
     for **Alarm name**, enter a new name. Alarm names must contain
     only ASCII characters.


    ###### Note

    You can adjust the alarm configuration based on your own requirements
     before creating the alarm, or you can edit them later. This includes the
     metric, threshold, duration, action, and notification settings. However, after
     you create an alarm, you cannot edit its name later.
    8. Choose **Create**.

## Add reboot actions to Amazon CloudWatch alarms

You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and automatically reboots
the instance. The reboot alarm action is recommended for Instance Health Check failures (as
opposed to the recover alarm action, which is suited for System Health Check failures). An
instance reboot is equivalent to an operating system reboot. In most cases, it takes only a
few minutes to reboot your instance. When you reboot an instance, it remains on the same
physical host, so your instance keeps its public DNS name, private IP address, and any data on
its instance store volumes.

Rebooting an instance doesn't start a new instance billing period (with a minimum one-minute
charge), unlike stopping and restarting your instance. Data on instance store volumes is retained
when the instance is rebooted. The instance store volumes must be re-mounted into the filesystem
after a reboot. For more information, see [Reboot your Amazon EC2 instance](ec2-instance-reboot.md "ec2-instance-reboot.md").

###### Important

To avoid a race condition between the reboot and recover actions, avoid setting the same
number of evaluation periods for a reboot alarm and a recover alarm. We recommend that you
set reboot alarms to three evaluation periods of one minute each. For more information, see
[Evaluating an
alarm](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarm-evaluation "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarm-evaluation") in the _Amazon CloudWatch User Guide_.

###### To create an alarm to reboot an instance (Amazon EC2 console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Actions**, **Monitor
   and troubleshoot**, **Manage CloudWatch alarms**.

Alternatively, you can choose the plus sign (
![Plus sign.](images/add-plus.png)
) in the **Alarm status** column. 4. On the **Manage CloudWatch alarms** page, do the
following:

    1. Choose **Create an alarm**.
    2. To receive an email when the alarm is triggered, for **Alarm
     notification**, choose an existing Amazon SNS topic. You first need to
     create an Amazon SNS topic using the Amazon SNS console. For more information,
     see [Using Amazon SNS for application-to-person (A2P) messaging](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md") in the
     *Amazon Simple Notification Service Developer Guide*.
    3. Toggle on **Alarm action**, and choose
     **Reboot**.
    4. For **Group samples by** and **Type of data to
     sample**, choose a statistic and a metric. In this example, choose
     **Average** and **Status check failed:
     instance**.
    5. For **Consecutive period** and **Period**,
     specify the evaluation period for the alarm. In this example, enter
     **3** consecutive periods of **1 Minute**.
     If **1 Minute is disabled**, you must [enable detailed monitoring](manage-detailed-monitoring.md#enable-detailed-monitoring "manage-detailed-monitoring.md#enable-detailed-monitoring"), or you can choose **5 Minutes**
     instead.
    6. Amazon CloudWatch automatically creates an alarm name for you. To change the name,
     for **Alarm name**, enter a new name. Alarm names must contain
     only ASCII characters.
    7. Choose **Create**.

## Add recover actions to Amazon CloudWatch alarms

You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance. If the instance becomes
impaired due to an underlying hardware failure or a problem that requires AWS involvement to
repair, you can automatically recover the instance. Terminated instances cannot be recovered.
A recovered instance is identical to the original instance, including the instance ID, private
IP addresses, Elastic IP addresses, and all instance metadata.

CloudWatch prevents you from adding a recovery action to an alarm that is on an instance which
does not support recovery actions.

When the `StatusCheckFailed_System` alarm is triggered, and the recover action
is initiated, you are notified by the Amazon SNS topic that you chose when you created the alarm
and associated the recover action. During instance recovery, the instance is migrated during
an instance reboot, and any data that is in-memory is lost. When the process is complete,
information is published to the SNS topic you've configured for the alarm. Anyone who is
subscribed to this SNS topic receives an email notification that includes the status of the
recovery attempt and any further instructions. You notice an instance reboot on the recovered
instance.

###### Note

The recover action can be used only with `StatusCheckFailed_System`, not with
`StatusCheckFailed_Instance`.

The following problems can cause system status checks to fail:

- Loss of network connectivity
- Loss of system power
- Software issues on the physical host
- Hardware issues on the physical host that impact network reachability

The recover action is supported only on instances that meet certain characteristics. For
more information, see [Automatic instance recovery](ec2-instance-recover.md "ec2-instance-recover.md").

If your instance has a public IP address, it retains the public IP address after
recovery.

###### Important

To avoid a race condition between the reboot and recover actions, avoid setting the same
number of evaluation periods for a reboot alarm and a recover alarm. We recommend that you
set recover alarms to two evaluation periods of one minute each. For more information, see
[Evaluating an
alarm](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarm-evaluation "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarm-evaluation") in the _Amazon CloudWatch User Guide_.

###### To create an alarm to recover an instance (Amazon EC2 console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Actions**, **Monitor
   and troubleshoot**, **Manage CloudWatch alarms**.

Alternatively, you can choose the plus sign (
![Plus sign.](images/add-plus.png)
) in the **Alarm status** column. 4. On the **Manage CloudWatch alarms** page, do the
following:

    1. Choose **Create an alarm**.
    2. To receive an email when the alarm is triggered, for **Alarm
     notification**, choose an existing Amazon SNS topic. You first need to
     create an Amazon SNS topic using the Amazon SNS console. For more information,
     see [Using Amazon SNS for application-to-person (A2P) messaging](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md") in the
     *Amazon Simple Notification Service Developer Guide*.


    ###### Note

    Users must subscribe to the specified SNS topic to receive email
     notifications when the alarm is triggered. The AWS account root user always receives
     email notifications when automatic instance recovery actions occur, even if an SNS
     topic is not specified or the root user is not subscribed to the specified SNS
     topic.
    3. Toggle on **Alarm action**, and choose
     **Recover**.
    4. For **Group samples by** and **Type of data to
     sample**, choose a statistic and a metric. In this example, choose
     **Average** and **Status check failed:
     system**.
    5. For **Consecutive period** and **Period**,
     specify the evaluation period for the alarm. In this example, enter
     **2** consecutive periods of **1 Minute**.
     If **1 Minute is disabled**, you must [enable detailed monitoring](manage-detailed-monitoring.md#enable-detailed-monitoring "manage-detailed-monitoring.md#enable-detailed-monitoring"), or you can choose **5 Minutes**
     instead.
    6. Amazon CloudWatch automatically creates an alarm name for you. To change the name,
     for **Alarm name**, enter a new name. Alarm names must contain
     only ASCII characters.
    7. Choose **Create**.
