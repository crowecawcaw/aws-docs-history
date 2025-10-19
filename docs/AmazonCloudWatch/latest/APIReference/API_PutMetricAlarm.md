# PutMetricAlarm

Creates or updates an alarm and associates it with the specified metric, metric
 math expression, anomaly detection model, or Metrics Insights query. For more
 information about using a Metrics Insights query for an alarm, see [Create
 alarms on Metrics Insights queries](../monitoring/Create_Metrics_Insights_Alarm.md "../monitoring/Create_Metrics_Insights_Alarm.md").

Alarms based on anomaly detection models cannot have Auto Scaling actions.

When this operation creates an alarm, the alarm state is immediately set to
 `INSUFFICIENT_DATA`. The alarm is then evaluated and its state is set
 appropriately. Any actions associated with the new state are then executed.

When you update an existing alarm, its state is left unchanged, but the update
 completely overwrites the previous configuration of the alarm.

If you are an IAM user, you must have Amazon EC2 permissions for
 some alarm operations:


* The `iam:CreateServiceLinkedRole` permission for all alarms with
 EC2 actions
* The `iam:CreateServiceLinkedRole` permissions to create an alarm
 with Systems Manager OpsItem or response plan actions.
The first time you create an alarm in the AWS Management Console, the AWS CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary
 service-linked role for you. The service-linked roles are called
 `AWSServiceRoleForCloudWatchEvents` and
 `AWSServiceRoleForCloudWatchAlarms_ActionSSM`. For more information, see
 [AWS service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role").

Each `PutMetricAlarm` action has a maximum uncompressed payload of 120
 KB.


**Cross-account alarms**


You can set an alarm on metrics in the current account, or in another account. To
 create a cross-account alarm that watches a metric in a different account, you must have
 completed the following pre-requisites:


* The account where the metrics are located (the *sharing
 account*) must already have a sharing role named **CloudWatch-CrossAccountSharingRole**. If it does not
 already have this role, you must create it using the instructions in **Set up a sharing account** in  [Cross-account cross-Region CloudWatch console](../monitoring/Cross-Account-Cross-Region.md#enable-cross-account-cross-Region "../monitoring/Cross-Account-Cross-Region.md#enable-cross-account-cross-Region"). The policy
 for that role must grant access to the ID of the account where you are creating
 the alarm.
* The account where you are creating the alarm (the *monitoring
 account*) must already have a service-linked role named **AWSServiceRoleForCloudWatchCrossAccount** to allow
 CloudWatch to assume the sharing role in the sharing account. If it
 does not, you must create it following the directions in **Set up a monitoring account** in  [Cross-account cross-Region CloudWatch console](../monitoring/Cross-Account-Cross-Region.md#enable-cross-account-cross-Region "../monitoring/Cross-Account-Cross-Region.md#enable-cross-account-cross-Region").

## Request Parameters





**ActionsEnabled** 


Indicates whether actions should be executed during any changes to the alarm state.
 The default is `TRUE`.


Type: Boolean


Required: No




**AlarmActions** 


The actions to execute when this alarm transitions to the `ALARM` state
 from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid
 values:



**EC2 actions:**




* `arn:aws:automate:*region*:ec2:stop`
* `arn:aws:automate:*region*:ec2:terminate`
* `arn:aws:automate:*region*:ec2:reboot`
* `arn:aws:automate:*region*:ec2:recover`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Stop/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Terminate/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Reboot/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Recover/1.0`


**Autoscaling action:**




* `arn:aws:autoscaling:*region*:*account-id*:scalingPolicy:*policy-id*:autoScalingGroupName/*group-friendly-name*:policyName/*policy-friendly-name*`


**Lambda actions:**




* Invoke the latest version of a Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*`
* Invoke a specific version of a Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*:*version-number*`
* Invoke a function by using an alias Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*:*alias-name*`


**SNS notification action:**




* `arn:aws:sns:*region*:*account-id*:*sns-topic-name*`


**SSM integration actions:**




* `arn:aws:ssm:*region*:*account-id*:opsitem:*severity*#CATEGORY=*category-name*`
* `arn:aws:ssm-incidents::*account-id*:responseplan/*response-plan-name*`


**Start a Amazon Q Developer operational investigation**




`arn:aws:aiops:*region*:*account-id*:investigation-group:*investigation-group-id*`



Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmDescription** 


The description for the alarm.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




**AlarmName** 


The name for the alarm. This name must be unique within the Region.


The name must contain only UTF-8 characters, and can't contain ASCII control
 characters


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




**ComparisonOperator** 


 The arithmetic operation to use when comparing the specified statistic and
 threshold. The specified statistic value is used as the first operand.


The values `LessThanLowerOrGreaterThanUpperThreshold`,
 `LessThanLowerThreshold`, and `GreaterThanUpperThreshold` are
 used only for alarms based on anomaly detection models.


Type: String


Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold | LessThanLowerOrGreaterThanUpperThreshold | LessThanLowerThreshold | GreaterThanUpperThreshold`



Required: Yes




**DatapointsToAlarm** 


The number of data points that must be breaching to trigger the alarm. This is used
 only if you are setting an "M out of N" alarm. In that case, this value is the M. For
 more information, see [Evaluating an Alarm](../monitoring/AlarmThatSendsEmail.md#alarm-evaluation "../monitoring/AlarmThatSendsEmail.md#alarm-evaluation") in the *Amazon CloudWatch User
 Guide*.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**Dimensions** 


The dimensions for the metric specified in `MetricName`.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**EvaluateLowSampleCountPercentile** 


 Used only for alarms based on percentiles. If you specify `ignore`, the
 alarm state does not change during periods with too few data points to be statistically
 significant. If you specify `evaluate` or omit this parameter, the alarm is
 always evaluated and possibly changes state no matter how many data points are
 available. For more information, see [Percentile-Based CloudWatch Alarms and Low Data Samples](../monitoring/AlarmThatSendsEmail.md#percentiles-with-low-samples "../monitoring/AlarmThatSendsEmail.md#percentiles-with-low-samples").


Valid Values: `evaluate | ignore`



Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**EvaluationPeriods** 


The number of periods over which data is compared to the specified threshold. If
 you are setting an alarm that requires that a number of consecutive data points be
 breaching to trigger the alarm, this value specifies that number. If you are setting an
 "M out of N" alarm, this value is the N.


Type: Integer


Valid Range: Minimum value of 1.


Required: Yes




**ExtendedStatistic** 


The extended statistic for the metric specified in `MetricName`. When
 you call `PutMetricAlarm` and specify a `MetricName`, you must
 specify either `Statistic` or `ExtendedStatistic` but not
 both.


If you specify `ExtendedStatistic`, the following are valid values:



* `p90`
* `tm90`
* `tc90`
* `ts90`
* `wm90`
* `IQM`
* `PR(*n*:*m*)` where n and m
 are values of the metric
* `TC(*X*%:*X*%)` where X is
 between 10 and 90 inclusive.
* `TM(*X*%:*X*%)` where X is
 between 10 and 90 inclusive.
* `TS(*X*%:*X*%)` where X is
 between 10 and 90 inclusive.
* `WM(*X*%:*X*%)` where X is
 between 10 and 90 inclusive.

For more information about these extended statistics, see [CloudWatch statistics definitions](../monitoring/Statistics-definitions.md "../monitoring/Statistics-definitions.md").


Type: String


Required: No




**InsufficientDataActions** 


The actions to execute when this alarm transitions to the
 `INSUFFICIENT_DATA` state from any other state. Each action is specified
 as an Amazon Resource Name (ARN). Valid values:



**EC2 actions:**




* `arn:aws:automate:*region*:ec2:stop`
* `arn:aws:automate:*region*:ec2:terminate`
* `arn:aws:automate:*region*:ec2:reboot`
* `arn:aws:automate:*region*:ec2:recover`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Stop/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Terminate/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Reboot/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Recover/1.0`


**Autoscaling action:**




* `arn:aws:autoscaling:*region*:*account-id*:scalingPolicy:*policy-id*:autoScalingGroupName/*group-friendly-name*:policyName/*policy-friendly-name*`


**Lambda actions:**




* Invoke the latest version of a Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*`
* Invoke a specific version of a Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*:*version-number*`
* Invoke a function by using an alias Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*:*alias-name*`


**SNS notification action:**




* `arn:aws:sns:*region*:*account-id*:*sns-topic-name*`


**SSM integration actions:**




* `arn:aws:ssm:*region*:*account-id*:opsitem:*severity*#CATEGORY=*category-name*`
* `arn:aws:ssm-incidents::*account-id*:responseplan/*response-plan-name*`

Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**MetricName** 


The name for the metric associated with the alarm. For each
 `PutMetricAlarm` operation, you must specify either
 `MetricName` or a `Metrics` array.


If you are creating an alarm based on a math expression, you cannot specify this
 parameter, or any of the `Namespace`, `Dimensions`,
 `Period`, `Unit`, `Statistic`, or
 `ExtendedStatistic` parameters. Instead, you specify all this information
 in the `Metrics` array.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Metrics** 


An array of `MetricDataQuery` structures that enable you to create an alarm
 based on the result of a metric math expression. For each `PutMetricAlarm`
 operation, you must specify either `MetricName` or a `Metrics`
 array.


Each item in the `Metrics` array either retrieves a metric or performs a
 math expression.


One item in the `Metrics` array is the expression that the alarm watches.
 You designate this expression by setting `ReturnData` to true for this object
 in the array. For more information, see [MetricDataQuery](API_MetricDataQuery.md "API_MetricDataQuery.md").


If you use the `Metrics` parameter, you cannot include the
 `Namespace`, `MetricName`, `Dimensions`,
 `Period`, `Unit`, `Statistic`, or
 `ExtendedStatistic` parameters of `PutMetricAlarm` in the same
 operation. Instead, you retrieve the metrics you are using in your math expression as
 part of the `Metrics` array.


Type: Array of [MetricDataQuery](API_MetricDataQuery.md "API_MetricDataQuery.md") objects


Required: No




**Namespace** 


The namespace for the metric associated specified in
 `MetricName`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: No




**OKActions** 


The actions to execute when this alarm transitions to an `OK` state from
 any other state. Each action is specified as an Amazon Resource Name (ARN). Valid
 values:



**EC2 actions:**




* `arn:aws:automate:*region*:ec2:stop`
* `arn:aws:automate:*region*:ec2:terminate`
* `arn:aws:automate:*region*:ec2:reboot`
* `arn:aws:automate:*region*:ec2:recover`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Stop/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Terminate/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Reboot/1.0`
* `arn:aws:swf:*region*:*account-id*:action/actions/AWS_EC2.InstanceId.Recover/1.0`


**Autoscaling action:**




* `arn:aws:autoscaling:*region*:*account-id*:scalingPolicy:*policy-id*:autoScalingGroupName/*group-friendly-name*:policyName/*policy-friendly-name*`


**Lambda actions:**




* Invoke the latest version of a Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*`
* Invoke a specific version of a Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*:*version-number*`
* Invoke a function by using an alias Lambda function:
 `arn:aws:lambda:*region*:*account-id*:function:*function-name*:*alias-name*`


**SNS notification action:**




* `arn:aws:sns:*region*:*account-id*:*sns-topic-name*`


**SSM integration actions:**




* `arn:aws:ssm:*region*:*account-id*:opsitem:*severity*#CATEGORY=*category-name*`
* `arn:aws:ssm-incidents::*account-id*:responseplan/*response-plan-name*`

Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**Period** 


The length, in seconds, used each time the metric specified in
 `MetricName` is evaluated. Valid values are 10, 20, 30, and any multiple of
 60.



`Period` is required for alarms based on static thresholds. If you are
 creating an alarm based on a metric math expression, you specify the period for each
 metric within the objects in the `Metrics` array.


Be sure to specify 10, 20, or 30 only for metrics that are stored by a
 `PutMetricData` call with a `StorageResolution` of 1. If you
 specify a period of 10, 20, or 30 for a metric that does not have sub-minute resolution, the
 alarm still attempts to gather data at the period rate that you specify. In this case,
 it does not receive data for the attempts that do not correspond to a one-minute data
 resolution, and the alarm might often lapse into INSUFFICENT\_DATA status. Specifying 10, 20,
 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than
 other alarms. For more information about pricing, see [Amazon CloudWatch
 Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").


An alarm's total current evaluation period can be no longer than seven days, so
 `Period` multiplied by `EvaluationPeriods` can't be more than
 604,800 seconds. For alarms with a period of less than one hour (3,600 seconds), the total evaluation period can't be longer than one day (86,400 seconds).


Type: Integer


Valid Range: Minimum value of 10.


Required: No




**Statistic** 


The statistic for the metric specified in `MetricName`, other than
 percentile. For percentile statistics, use `ExtendedStatistic`. When you call
 `PutMetricAlarm` and specify a `MetricName`, you must specify
 either `Statistic` or `ExtendedStatistic,` but not both.


Type: String


Valid Values: `SampleCount | Average | Sum | Minimum | Maximum`



Required: No




**Tags** 


A list of key-value pairs to associate with the alarm. You can associate as many as
 50 tags with an alarm. To be able to associate tags with the alarm when you create the
 alarm, you must have the `cloudwatch:TagResource` permission.


Tags can help you organize and categorize your resources. You can also use them to
 scope user permissions by granting a user permission to access or change only resources
 with certain tag values.


If you are using this operation to update an existing alarm, any tags you specify in
 this parameter are ignored. To change the tags of an existing alarm, use [TagResource](API_TagResource.md "API_TagResource.md") or [UntagResource](API_UntagResource.md "API_UntagResource.md").


To use this field to set tags for an alarm when you create it, you must be signed on
 with both the `cloudwatch:PutMetricAlarm` and
 `cloudwatch:TagResource` permissions.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




**Threshold** 


The value against which the specified statistic is compared.


This parameter is required for alarms based on static thresholds, but should not be
 used for alarms based on anomaly detection models.


Type: Double


Required: No




**ThresholdMetricId** 


If this is an alarm based on an anomaly detection model, make this value match the ID
 of the `ANOMALY_DETECTION_BAND` function.


For an example of how to use this parameter, see the **Anomaly
 Detection Model Alarm** example on this page.


If your alarm uses this parameter, it cannot have Auto Scaling actions.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**TreatMissingData** 


 Sets how this alarm is to handle missing data points. If
 `TreatMissingData` is omitted, the default behavior of
 `missing` is used. For more information, see [Configuring How CloudWatch Alarms Treats Missing Data](../monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data").


Valid Values: `breaching | notBreaching | ignore | missing`



###### Note

Alarms that evaluate metrics in the `AWS/DynamoDB` namespace always
 `ignore` missing data even if you choose a different option for
 `TreatMissingData`. When an `AWS/DynamoDB` metric has
 missing data, alarms that evaluate that metric remain in their current state.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Unit** 


The unit of measure for the statistic. For example, the units for the Amazon EC2
 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance
 receives on all network interfaces. You can also specify a unit when you create a custom
 metric. Units help provide conceptual meaning to your data. Metric data points that
 specify a unit of measure, such as Percent, are aggregated separately. If you are
 creating an alarm based on a metric math expression, you can specify the unit for each
 metric (if needed) within the objects in the `Metrics` array.


If you don't specify `Unit`, CloudWatch retrieves all unit types that
 have been published for the metric and attempts to evaluate the alarm. Usually, metrics
 are published with only one unit, so the alarm works as intended.


However, if the metric is published with multiple types of units and you don't
 specify a unit, the alarm's behavior is not defined and it behaves
 unpredictably.


We recommend omitting `Unit` so that you don't inadvertently specify an
 incorrect unit that is not published for this metric. Doing so causes the alarm to be
 stuck in the `INSUFFICIENT DATA` state.


Type: String


Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`



Required: No




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**LimitExceeded** 


The quota for alarms for this customer has already been reached.





**message** 





HTTP Status Code: 400




## Examples


### Static Threshold Alarm


The following example creates an alarm that notifies an SNS group when the
 CPUUtilization of a certain instance goes over 40% for three out of four
 periods.


#### Sample Request



```
{
    "Namespace": "AWS/EC2",
    "MetricName": "CPUUtilization",
    "Dimensions": [
        {
            "Name": "InstanceId",
            "Value": "i-1234567890abcdef0"
        }
    ],
    "AlarmActions": [
        "arn:aws:sns:us-west-1:123456789012:my_sns_topic"
    ],
    "ComparisonOperator": "GreaterThanThreshold",
    "DatapointsToAlarm": 3,
    "EvaluationPeriods": 4,
    "Period": 60,
    "Statistic": "Average",
    "Threshold": 40,
    "AlarmDescription": "CPU Utilization of i-1234567890abcdef0 with 40% as threshold",
    "AlarmName": "Instance i-1234567890abcdef0 CPU Utilization"
}
```

### Metric Math Function Alarm


The following example retrieves three metrics that each track a different
 type of connection error to a custom service. These error counts are first
 summed in one expression, then divided by total connection attempts in another
 expression. The alarm goes to the ALARM state if the error rate is over 40% for
 three consecutive periods, and notifies two different SNS groups.


#### Sample Request



```
{
    "AlarmActions": [
        "arn:aws:sns:us-west-1:123456789012:my_sns_topic",
        "arn:aws:sns:us-west-1:123456789012:my_other_sns_topic"
    ],
    "ComparisonOperator": "GreaterThanThreshold",
    "EvaluationPeriods": 3,
    "Threshold": 40,
    "AlarmDescription": "MyService Aggregate Connection Error Rate (Alarm at 40%)",
    "AlarmName": "MyService Connection Error Rate",
    "Metrics": [
        {
            "MetricStat": {
                "Metric": {
                    "MetricName": "ConnectionsFailed",
                    "Namespace": "MyService"
                },
                "Period": 60,
                "Stat": "Sum"
            },
            "Id": "m1",
            "ReturnData": "False"
        },
        {
            "MetricStat": {
                "Metric": {
                    "MetricName": "ConnectionsDropped",
                    "Namespace": "MyService"
                },
                "Period": 60,
                "Stat": "Sum"
            },
            "Id": "m2",
            "ReturnData": "False"
        },
        {
            "MetricStat": {
                "Metric": {
                    "MetricName": "RequestsThrottled",
                    "Namespace": "MyService"
                },
                "Period": 60,
                "Stat": "Sum"
            },
            "Id": "m3",
            "ReturnData": "False"
        },
        {
            "MetricStat": {
                "Metric": {
                    "MetricName": "ConnectionAttempts",
                    "Namespace": "MyService"
                },
                "Period": 60,
                "Stat": "Sum"
            },
            "Id": "m4",
            "ReturnData": "False"
        },
        {
            "Id": "error_total",
            "Expression": "m1+m2+m3",
            "ReturnData": "False"
        },
        {
            "Id": "error_rate",
            "Expression": "(error_total/m4)*100",
            "ReturnData": "true",
            "Label": "Total Connection Error Rate"
        }
    ]
}
```

### Anomaly Detection Model Alarm


The following example sets an alarm on an anomaly detection model. The Id
 of `m1` is assigned to the `CPUUtilization` metric of an
 instance. `t1` is the anomaly detection model function for that
 metric, and uses 3 standard deviations to set the width of the band. The setting
 of `ThresholdMetricId` is `t1` and the
 `ComparisonOperator` is
 `LessThanLowerOrGreaterThanUpperThreshold`, specifying that the
 alarm goes to alarm state when the metric value is outside the anomaly model
 band in either direction for two consecutive evaluation periods.


#### Sample Request



```
{
    "AlarmActions": [
        "arn:aws:sns:us-west-1:123456789012:my_sns_topic",
        "arn:aws:sns:us-west-1:123456789012:my_other_sns_topic"
    ],
    "AlarmName": "MyAlarmName",
    "AlarmDescription": "This alarm uses an anomaly detection model",
    "Metrics": [
        {
            "Id": "m1",
            "ReturnData": true,
            "MetricStat": {
                "Metric": {
                    "MetricName": "CPUUtilization",
                    "Namespace": "AWS/EC2",
                    "Dimensions": [
                        {
                            "Name": "instanceId",
                            "Value": "i-1234567890abcdef0"
                        }
                    ]
                },
                "Stat": "Average",
                "Period": 60
            }
        },
        {
            "Id": "t1",
            "Expression": "ANOMALY_DETECTION_BAND(m1, 3)"
        }
    ],
    "EvaluationPeriods": 2,
    "ThresholdMetricId": "t1",
    "ComparisonOperator": "LessThanLowerOrGreaterThanUpperThreshold"
}
```

### Metrics Insights query alarm


The following example sets an alarm on an Metrics Insights query.


#### Sample Request



```
{
    "AlarmActions": [
        "arn:aws:sns:us-west-1:123456789012:my_sns_topic",
        "arn:aws:sns:us-west-1:123456789012:my_other_sns_topic"
    ],
    "AlarmName": "MetricsInsightsAlarm",
    "AlarmDescription": "This alarm uses a Metrics Insights query",
    "Metrics": [
        {
            "Id": "m1",
            "Expression": "SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2", InstanceId)",
            "Period": 60,
            "Label": "Average CPUUtilization query"
        }
    ],
    "EvaluationPeriods": 1,
    "Threshold": 65,
    "ComparisonOperator": "GreaterThanThreshold"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricAlarm")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm")
