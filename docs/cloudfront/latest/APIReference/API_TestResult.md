# TestResult

Contains the result of testing a CloudFront function with `TestFunction`.


## Contents





**ComputeUtilization** 


The amount of time that the function took to run as a percentage of the maximum
 allowed time. For example, a compute utilization of 35 means that the function completed
 in 35% of the maximum allowed time.


Type: String


Required: No




**FunctionErrorMessage** 


If the result of testing the function was an error, this field contains the error
 message.


Type: String


Required: No




**FunctionExecutionLogs** 


Contains the log lines that the function wrote (if any) when running the test.


Type: Array of strings


Required: No




**FunctionOutput** 


The event object returned by the function. For more information about the structure of
 the event object, see [Event
 object structure](../../../AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.md "../../../AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.md") in the *Amazon CloudFront Developer Guide*.


Type: String


Required: No




**FunctionSummary** 


Contains configuration information and metadata about the CloudFront function that was
 tested.


Type: [FunctionSummary](API_FunctionSummary.md "API_FunctionSummary.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TestResult "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TestResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TestResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TestResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TestResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TestResult")
