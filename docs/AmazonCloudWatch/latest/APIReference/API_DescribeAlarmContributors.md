# DescribeAlarmContributors

Returns the information of the current alarm contributors that are in `ALARM` state. This operation returns details about the individual time series that contribute to the alarm's state.


## Request Parameters





**AlarmName** 


The name of the alarm for which to retrieve contributor information.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




**NextToken** 


The token returned by a previous call to indicate that there is more data available.


Type: String


Required: No




## Response Elements


The following elements are returned by the service.





**AlarmContributors** 


A list of alarm contributors that provide details about the individual time series contributing to the alarm's state.


Type: Array of [AlarmContributor](API_AlarmContributor.md "API_AlarmContributor.md") objects




**NextToken** 


The token that marks the start of the next batch of returned results.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidNextToken** 


The next token specified is invalid.





**message** 





HTTP Status Code: 400




**ResourceNotFoundException** 


The named resource does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmContributors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors")
