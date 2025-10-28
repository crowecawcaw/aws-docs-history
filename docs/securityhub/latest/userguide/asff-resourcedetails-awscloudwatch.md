# AwsCloudWatch resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsCloudWatch` resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsCloudWatchAlarm

The `AwsCloudWatchAlarm` object provides details about Amazon CloudWatch alarms that
watch a metric or perform an action when an alarm changes state.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsCloudWatchAlarm` object. To view descriptions of
`AwsCloudWatchAlarm` attributes, see [AwsCloudWatchAlarmDetails](../../1.0/APIReference/API_AwsCloudWatchAlarmDetails.md "../../1.0/APIReference/API_AwsCloudWatchAlarmDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsCloudWatchAlarm": {
	"ActionsEnabled": true,
	"AlarmActions": [
		"arn:aws:automate:region:ec2:stop",
		"arn:aws:automate:region:ec2:terminate"
	],
	"AlarmArn": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:sampleAlarm",
	"AlarmConfigurationUpdatedTimestamp": "2022-02-18T15:31:53.161Z",
	"AlarmDescription": "Alarm Example",
	"AlarmName": "Example",
	"ComparisonOperator": "GreaterThanOrEqualToThreshold",
	"DatapointsToAlarm": 1,
	"Dimensions": [{
		"Name": "InstanceId",
		"Value": "i-1234567890abcdef0"
	}],
	"EvaluateLowSampleCountPercentile": "evaluate",
	"EvaluationPeriods": 1,
	"ExtendedStatistic": "p99.9",
	"InsufficientDataActions": [
		"arn:aws:automate:region:ec2:stop"
	],
	"MetricName": "Sample Metric",
	"Namespace": "YourNamespace",
	"OkActions": [
		"arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Stop/1.0"
	],
	"Period": 1,
	"Statistic": "SampleCount",
	"Threshold": 12.3,
	"ThresholdMetricId": "t1",
	"TreatMissingData": "notBreaching",
	"Unit": "Kilobytes/Second"
}
```
