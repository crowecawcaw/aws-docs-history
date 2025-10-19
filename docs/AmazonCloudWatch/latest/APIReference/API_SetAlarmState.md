# SetAlarmState

Temporarily sets the state of an alarm for testing purposes. When the updated state
 differs from the previous value, the action configured for the appropriate state is
 invoked. For example, if your alarm is configured to send an Amazon SNS message when an
 alarm is triggered, temporarily changing the alarm state to `ALARM` sends an
 SNS message.

Metric alarms returns to their actual state quickly, often within seconds. Because
 the metric alarm state change happens quickly, it is typically only visible in the
 alarm's **History** tab in the Amazon CloudWatch console or
 through [DescribeAlarmHistory](API_DescribeAlarmHistory.md "API_DescribeAlarmHistory.md").

If you use `SetAlarmState` on a composite alarm, the composite alarm is
 not guaranteed to return to its actual state. It returns to its actual state only once
 any of its children alarms change state. It is also reevaluated if you update its
 configuration.

If an alarm triggers EC2 Auto Scaling policies or application Auto Scaling
 policies, you must include information in the `StateReasonData` parameter to
 enable the policy to take the correct action.


## Request Parameters





**AlarmName** 


The name of the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




**StateReason** 


The reason that this alarm is set to this specific state, in text format.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1023.


Required: Yes




**StateReasonData** 


The reason that this alarm is set to this specific state, in JSON format.


For SNS or EC2 alarm actions, this is just informational. But for EC2 Auto Scaling
 or application Auto Scaling alarm actions, the Auto Scaling policy uses the information
 in this field to take the correct action.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 4000.


Required: No




**StateValue** 


The value of the state.


Type: String


Valid Values: `OK | ALARM | INSUFFICIENT_DATA`



Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidFormat** 


Data was not syntactically valid JSON.





**message** 





HTTP Status Code: 400




**ResourceNotFound** 


The named resource does not exist.





**message** 





HTTP Status Code: 404




## Examples


### Example


The following example sets the alarm state to ALARM, and provides
 information inside of `StateReasonData` so that Auto Scaling actions
 can be performed correctly according to your Auto Scaling policies. 



```
{
    "AlarmName": "ExampleAlarmName",
    "StateValue": "ALARM",
    "StateReason": "Testing Alarm State",
    "StateReasonData": {
        "Version": "1.0",
        "QueryDate": "2018-10-31T14:32:52.031+0000",
        "StartDate": "2018-10-31T14:31:00.000+0000",
        "Statistic": "Average",
        "Period": 60,
        "RecentDatapoints": [
            100
        ],
        "Threshold": 50
    }
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/SetAlarmState")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/SetAlarmState "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/SetAlarmState")
