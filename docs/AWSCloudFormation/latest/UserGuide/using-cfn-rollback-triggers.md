# Roll back your CloudFormation stack on alarm
 breach with rollback triggers

With rollback triggers, you can have AWS CloudFormation monitor the state of your application during
 stack creation and updating, and roll back that operation if the application breaches the
 threshold of the alarms you've specified. For each rollback trigger you create, you specify
 the CloudWatch alarm that CloudFormation should monitor. CloudFormation monitors the specified alarms
 during the stack create or update operation, and for the specified amount of time after all
 resources have been deployed. If any of the alarms goes to `ALARM` state during
 the stack operation or the monitoring period, CloudFormation rolls back the entire stack
 operation.

You can set a monitoring time from the default of 0 up to 180 minutes. During this time,
 CloudFormation monitors all the rollback triggers after the stack creation or update operation
 deploys all necessary resources. If any of the alarms goes to `ALARM` state
 during the stack operation or this monitoring period, CloudFormation rolls back the entire stack
 operation. Then, for update operations, if the monitoring period expires without any alarms
 going to `ALARM` state, CloudFormation proceeds to dispose of old resources as usual.
 If you set a monitoring time but don't specify any rollback triggers, CloudFormation still waits
 the specified period of time before cleaning up old resources for update operations. You can
 use this monitoring period to perform any manual stack validation desired, and manually
 cancel the stack creation or update as necessary. If you set a monitoring time of 0 minutes,
 CloudFormation still monitors the rollback triggers during stack creation and update operations
 and rolls back the operation if an alarm goes to `ALARM` state. Then, for update
 operations with no breaching alarms, it begins disposing of old resources immediately once
 the operation completes.

By default, CloudFormation only rolls back stack operations if an alarm goes to
 `ALARM` state, not `INSUFFICIENT_DATA` state. To have CloudFormation
 roll back the stack operation if an alarm goes to `INSUFFICIENT_DATA` state as
 well, edit the CloudWatch alarm to treat missing data as `breaching`. For more
 information, see [Configuring how CloudWatch alarms treat missing data](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data") in the
 *Amazon CloudWatch User Guide*.

CloudFormation doesn't monitor rollback triggers when it rolls back a stack during an update
 operation.

You can add a maximum of 5 rollback triggers. To add a rollback trigger, specify the
 Amazon Resource Name (ARN) of the CloudWatch alarm. Currently, `AWS::CloudWatch::Alarm`
 and `AWS::CloudWatch::CompositeAlarm` types can be used as rollback triggers. For
 more information about CloudWatch alarms, see [Using CloudWatch
 alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in *Amazon CloudWatch User Guide*.

If a given CloudWatch alarm is missing, the entire stack operation fails and rolls back.

Be aware that access to CloudWatch requires credentials. Those credentials must have permissions
 to access AWS resources, such as retrieving CloudWatch metric data about your resources. For
 more information, see [Authentication and access control for CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in
 *Amazon CloudWatch User Guide*.


## Add rollback triggers during stack
 creation or updating


###### To add rollback triggers during stack creation or update (console)

1. When creating or updating a stack, on the **Configure stack
 options** page, under **Advanced options**, expand
 the **Rollback configuration** section.
2. Enter a monitoring time between `0` – `180`
 minutes. The default value is `0`.
3. Specify the ARN of the CloudWatch alarm or composite alarm you want to use as a
 rollback trigger, and choose **Add CloudWatch alarm ARN**.


For example, the following is an ARN for a CloudWatch alarm or composite alarm,
 `arn:aws:cloudwatch:`us-east-1`:`123456789012`:alarm:`MyAlarmName``.
4. Choose **Next** and review the details of your stack.
5. When you're ready, choose **Submit** to create or update the
 stack.

###### To add rollback triggers during stack creation or update (AWS CLI)


Use the [create-stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html") or [update-stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack.html") command with the
 `--rollback-configuration` option.


For example, the following **update-stack** command sets
 `MyCompositeAlarm` as a rollback trigger with a 5-minute
 monitoring period:



```
aws cloudformation update-stack --stack-name `MyStack` \
  --use-previous-template \
  --rollback-configuration \
  "RollbackTriggers=[{Arn=arn:aws:cloudwatch:`us-east-1`:`123456789012`:alarm:`MyCompositeAlarm`,Type=`AWS::CloudWatch::CompositeAlarm`}],MonitoringTimeInMinutes=`5`"
```

## Add rollback triggers to a
 change set


To add rollback triggers to a change set (console)

1. When creating a change set, on the **Configure stack
 options** page, under **Advanced options**, expand
 the **Rollback configuration** section.
2. Enter a monitoring time between `0` – `180`
 minutes. The default value is `5`.
3. Specify the ARN of the CloudWatch alarm or composite alarm you want to use as a
 rollback trigger, and choose **Add CloudWatch alarm ARN**.


For example, the following is an ARN for a CloudWatch alarm or composite alarm,
 `arn:aws:cloudwatch:`us-east-1`:123456789012:alarm:`MyAlarmName``.
4. Choose **Next** and review the details of your change
 set.
5. When you're ready, choose **Create change set** to create the
 change set.

###### To add rollback triggers to a change set (AWS CLI)


Use the [create-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-change-set.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-change-set.html") command with the
 `--rollback-configuration` option.


## View rollback triggers for a
 stack


To view rollback triggers for a stack, see the **Rollback
 configuration** section.


1. On the **Stacks** page, choose the stack you want to view
 from the list on the left.
2. On the **Stack info** tab, expand the **Rollback
 configuration** section to view the rollback triggers.

## View rollback triggers for
 a change set


To view rollback triggers for a change set, see the **Rollback
 configuration** section.


1. On the **Stacks** page, choose the stack you want to view
 from the list on the left.
2. Choose the **Change sets** tab, and then choose the change set you
 want to view.
3. Choose the **Input** tab, and view the **Rollback
 configuration** section.
