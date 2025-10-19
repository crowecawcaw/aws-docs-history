# DescribeAlarmHistory

Retrieves the history for the specified alarm. You can filter the results by date
 range or item type. If an alarm name is not specified, the histories for either all
 metric alarms or all composite alarms are returned.

CloudWatch retains the history of an alarm even if you delete the alarm.

To use this operation and return information about a composite alarm, you must be
 signed on with the `cloudwatch:DescribeAlarmHistory` permission that is
 scoped to `*`. You can't return information about composite alarms if your
 `cloudwatch:DescribeAlarmHistory` permission has a narrower scope.


## Request Parameters





**AlarmContributorId** 


The unique identifier of a specific alarm contributor to filter the alarm history results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmName** 


The name of the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**AlarmTypes** 


Use this parameter to specify whether you want the operation to return metric alarms
 or composite alarms. If you omit this parameter, only metric alarms are returned.


Type: Array of strings


Valid Values: `CompositeAlarm | MetricAlarm`



Required: No




**EndDate** 


The ending date to retrieve alarm history.


Type: Timestamp


Required: No




**HistoryItemType** 


The type of alarm histories to retrieve.


Type: String


Valid Values: `ConfigurationUpdate | StateUpdate | Action | AlarmContributorStateUpdate | AlarmContributorAction`



Required: No




**MaxRecords** 


The maximum number of alarm history records to retrieve.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


The token returned by a previous call to indicate that there is more data
 available.


Type: String


Required: No




**ScanBy** 


Specified whether to return the newest or oldest alarm history first. Specify
 `TimestampDescending` to have the newest event history returned first,
 and specify `TimestampAscending` to have the oldest history returned
 first.


Type: String


Valid Values: `TimestampDescending | TimestampAscending`



Required: No




**StartDate** 


The starting date to retrieve alarm history.


Type: Timestamp


Required: No




## Response Elements


The following elements are returned by the service.





**AlarmHistoryItems** 


The alarm histories, in JSON format.


Type: Array of [AlarmHistoryItem](API_AlarmHistoryItem.md "API_AlarmHistoryItem.md") objects




**NextToken** 


The token that marks the start of the next batch of returned results.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidNextToken** 


The next token specified is invalid.





**message** 





HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmHistory")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmHistory "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmHistory")
