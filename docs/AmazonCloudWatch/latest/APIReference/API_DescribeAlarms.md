# DescribeAlarms

Retrieves the specified alarms. You can filter the results by specifying a prefix
 for the alarm name, the alarm state, or a prefix for any action.

To use this operation and return information about composite alarms, you must be
 signed on with the `cloudwatch:DescribeAlarms` permission that is scoped to
 `*`. You can't return information about composite alarms if your
 `cloudwatch:DescribeAlarms` permission has a narrower scope.


## Request Parameters





**ActionPrefix** 


Use this parameter to filter the results of the operation to only those alarms that
 use a certain alarm action. For example, you could specify the ARN of an SNS topic to
 find all alarms that send notifications to that topic.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmNamePrefix** 


An alarm name prefix. If you specify this parameter, you receive information about
 all alarms that have names that start with this prefix.


If this parameter is specified, you cannot specify
 `AlarmNames`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**AlarmNames** 


The names of the alarms to retrieve information about.


Type: Array of strings


Array Members: Maximum number of 100 items.


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**AlarmTypes** 


Use this parameter to specify whether you want the operation to return metric alarms
 or composite alarms. If you omit this parameter, only metric alarms are returned, even
 if composite alarms exist in the account.


For example, if you omit this parameter or specify `MetricAlarms`, the
 operation returns only a list of metric alarms. It does not return any composite alarms,
 even if composite alarms exist in the account.


If you specify `CompositeAlarms`, the operation returns only a list of
 composite alarms, and does not return any metric alarms.


Type: Array of strings


Valid Values: `CompositeAlarm | MetricAlarm`



Required: No




**ChildrenOfAlarmName** 


If you use this parameter and specify the name of a composite alarm, the operation
 returns information about the "children" alarms of the alarm you specify. These are the
 metric alarms and composite alarms referenced in the `AlarmRule` field of the
 composite alarm that you specify in `ChildrenOfAlarmName`. Information about
 the composite alarm that you name in `ChildrenOfAlarmName` is not
 returned.


If you specify `ChildrenOfAlarmName`, you cannot specify any other
 parameters in the request except for `MaxRecords` and `NextToken`.
 If you do so, you receive a validation error.


###### Note

Only the `Alarm Name`, `ARN`, `StateValue`
 (OK/ALARM/INSUFFICIENT\_DATA), and `StateUpdatedTimestamp` information are
 returned by this operation when you use this parameter. To get complete information
 about these alarms, perform another `DescribeAlarms` operation and
 specify the parent alarm names in the `AlarmNames` parameter.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**MaxRecords** 


The maximum number of alarm descriptions to retrieve.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


The token returned by a previous call to indicate that there is more data
 available.


Type: String


Required: No




**ParentsOfAlarmName** 


If you use this parameter and specify the name of a metric or composite alarm, the
 operation returns information about the "parent" alarms of the alarm you specify. These
 are the composite alarms that have `AlarmRule` parameters that reference the
 alarm named in `ParentsOfAlarmName`. Information about the alarm that you
 specify in `ParentsOfAlarmName` is not returned.


If you specify `ParentsOfAlarmName`, you cannot specify any other
 parameters in the request except for `MaxRecords` and `NextToken`.
 If you do so, you receive a validation error.


###### Note

Only the Alarm Name and ARN are returned by this operation when you use this
 parameter. To get complete information about these alarms, perform another
 `DescribeAlarms` operation and specify the parent alarm names in the
 `AlarmNames` parameter.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**StateValue** 


Specify this parameter to receive information only about alarms that are currently
 in the state that you specify.


Type: String


Valid Values: `OK | ALARM | INSUFFICIENT_DATA`



Required: No




## Response Elements


The following elements are returned by the service.





**CompositeAlarms** 


The information about any composite alarms returned by the operation.


Type: Array of [CompositeAlarm](API_CompositeAlarm.md "API_CompositeAlarm.md") objects




**MetricAlarms** 


The information about any metric alarms returned by the operation.


Type: Array of [MetricAlarm](API_MetricAlarm.md "API_MetricAlarm.md") objects




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarms")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarms "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarms")
