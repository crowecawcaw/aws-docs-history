# DeleteAlarms

Deletes the specified alarms. You can delete up to 100 alarms in one operation.
 However, this total can include no more than one composite alarm. For example, you could
 delete 99 metric alarms and one composite alarms with one operation, but you can't
 delete two composite alarms with one operation.

 If you specify any incorrect alarm names, the alarms you specify with correct names are still deleted. Other syntax errors might result
 in no alarms being deleted. To confirm that alarms were deleted successfully, you can use the
 [DescribeAlarms](API_DescribeAlarms.md "API_DescribeAlarms.md") operation after using `DeleteAlarms`.

###### Note

It is possible to create a loop or cycle of composite alarms, where composite
 alarm A depends on composite alarm B, and composite alarm B also depends on
 composite alarm A. In this scenario, you can't delete any composite alarm that is
 part of the cycle because there is always still a composite alarm that depends on
 that alarm that you want to delete.

To get out of such a situation, you must break the cycle by changing the rule of
 one of the composite alarms in the cycle to remove a dependency that creates the
 cycle. The simplest change to make to break a cycle is to change the
 `AlarmRule` of one of the alarms to `false`. 

Additionally, the evaluation of composite alarms stops if CloudWatch
 detects a cycle in the evaluation path. 


## Request Parameters





**AlarmNames** 


The alarms to be deleted. Do not enclose the alarm names in quote marks.


Type: Array of strings


Array Members: Maximum number of 100 items.


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ResourceNotFound** 


The named resource does not exist.





**message** 





HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarms")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms")
