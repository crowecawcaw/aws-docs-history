On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# UpdateInferenceScheduler

Updates an inference scheduler.

## Request Syntax

```
{
   "DataDelayOffsetInMinutes": `number`,
   "DataInputConfiguration": {
      "InferenceInputNameConfiguration": {
         "ComponentTimestampDelimiter": "`string`",
         "TimestampFormat": "`string`"
      },
      "InputTimeZoneOffset": "`string`",
      "S3InputConfiguration": {
         "Bucket": "`string`",
         "Prefix": "`string`"
      }
   },
   "DataOutputConfiguration": {
      "KmsKeyId": "`string`",
      "S3OutputConfiguration": {
         "Bucket": "`string`",
         "Prefix": "`string`"
      }
   },
   "DataUploadFrequency": "`string`",
   "InferenceSchedulerName": "`string`",
   "RoleArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DataDelayOffsetInMinutes](#API_UpdateInferenceScheduler_RequestSyntax "#API_UpdateInferenceScheduler_RequestSyntax")**

A period of time (in minutes) by which inference on the data is delayed after the data
starts. For instance, if you select an offset delay time of five minutes, inference will
not begin on the data until the first data measurement after the five minute mark. For
example, if five minutes is selected, the inference scheduler will wake up at the
configured frequency with the additional five minute delay time to check the customer S3
bucket. The customer can upload data at the same frequency and they don't need to stop and
restart the scheduler when uploading new data.

Type: Long

Valid Range: Minimum value of 0. Maximum value of 60.

Required: No

**[DataInputConfiguration](#API_UpdateInferenceScheduler_RequestSyntax "#API_UpdateInferenceScheduler_RequestSyntax")**

Specifies information for the input data for the inference scheduler, including
delimiter, format, and dataset location.

Type: [InferenceInputConfiguration](API_InferenceInputConfiguration.md "API_InferenceInputConfiguration.md") object

Required: No

**[DataOutputConfiguration](#API_UpdateInferenceScheduler_RequestSyntax "#API_UpdateInferenceScheduler_RequestSyntax")**

Specifies information for the output results from the inference scheduler, including
the output S3 location.

Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md "API_InferenceOutputConfiguration.md") object

Required: No

**[DataUploadFrequency](#API_UpdateInferenceScheduler_RequestSyntax "#API_UpdateInferenceScheduler_RequestSyntax")**

How often data is uploaded to the source S3 bucket for the input data. The value chosen
is the length of time between data uploads. For instance, if you select 5 minutes, Amazon
Lookout for Equipment will upload the real-time data to the source bucket once every 5
minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on
your data. In this example, it starts once every 5 minutes.

Type: String

Valid Values: `PT5M | PT10M | PT15M | PT30M | PT1H`

Required: No

**[InferenceSchedulerName](#API_UpdateInferenceScheduler_RequestSyntax "#API_UpdateInferenceScheduler_RequestSyntax")**

The name of the inference scheduler to be updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[RoleArn](#API_UpdateInferenceScheduler_RequestSyntax "#API_UpdateInferenceScheduler_RequestSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source for
the inference scheduler.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**ConflictException**

The request could not be completed due to a conflict with the current state of the
target resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/cli2/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/boto3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateInferenceScheduler.md")
