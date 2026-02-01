On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DescribeInferenceScheduler

Specifies information about the inference scheduler being used, including name, model,
status, and associated metadata

## Request Syntax

```
{
   "InferenceSchedulerName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[InferenceSchedulerName](#API_DescribeInferenceScheduler_RequestSyntax "#API_DescribeInferenceScheduler_RequestSyntax")**

The name of the inference scheduler being described.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

## Response Syntax

```
{
   "CreatedAt": ***number***,
   "DataDelayOffsetInMinutes": ***number***,
   "DataInputConfiguration": {
      "InferenceInputNameConfiguration": {
         "ComponentTimestampDelimiter": "***string***",
         "TimestampFormat": "***string***"
      },
      "InputTimeZoneOffset": "***string***",
      "S3InputConfiguration": {
         "Bucket": "***string***",
         "Prefix": "***string***"
      }
   },
   "DataOutputConfiguration": {
      "KmsKeyId": "***string***",
      "S3OutputConfiguration": {
         "Bucket": "***string***",
         "Prefix": "***string***"
      }
   },
   "DataUploadFrequency": "***string***",
   "InferenceSchedulerArn": "***string***",
   "InferenceSchedulerName": "***string***",
   "LatestInferenceResult": "***string***",
   "ModelArn": "***string***",
   "ModelName": "***string***",
   "RoleArn": "***string***",
   "ServerSideKmsKeyId": "***string***",
   "Status": "***string***",
   "UpdatedAt": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreatedAt](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Specifies the time at which the inference scheduler was created.

Type: Timestamp

**[DataDelayOffsetInMinutes](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

A period of time (in minutes) by which inference on the data is delayed after the data
starts. For instance, if you select an offset delay time of five minutes, inference will
not begin on the data until the first data measurement after the five minute mark. For
example, if five minutes is selected, the inference scheduler will wake up at the
configured frequency with the additional five minute delay time to check the customer S3
bucket. The customer can upload data at the same frequency and they don't need to stop and
restart the scheduler when uploading new data.

Type: Long

Valid Range: Minimum value of 0. Maximum value of 60.

**[DataInputConfiguration](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Specifies configuration information for the input data for the inference scheduler,
including delimiter, format, and dataset location.

Type: [InferenceInputConfiguration](API_InferenceInputConfiguration.md "API_InferenceInputConfiguration.md") object

**[DataOutputConfiguration](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Specifies information for the output results for the inference scheduler, including
the output S3 location.

Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md "API_InferenceOutputConfiguration.md") object

**[DataUploadFrequency](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Specifies how often data is uploaded to the source S3 bucket for the input data. This
value is the length of time between data uploads. For instance, if you select 5 minutes,
Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This
frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In
this example, it starts once every 5 minutes.

Type: String

Valid Values: `PT5M | PT10M | PT15M | PT30M | PT1H`

**[InferenceSchedulerArn](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

The Amazon Resource Name (ARN) of the inference scheduler being described.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`

**[InferenceSchedulerName](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

The name of the inference scheduler being described.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[LatestInferenceResult](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Indicates whether the latest execution for the inference scheduler was Anomalous
(anomalous events found) or Normal (no anomalous events found).

Type: String

Valid Values: `ANOMALOUS | NORMAL`

**[ModelArn](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

The Amazon Resource Name (ARN) of the machine learning model of the inference scheduler
being described.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelName](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

The name of the machine learning model of the inference scheduler being described.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[RoleArn](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source for
the inference scheduler being described.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

**[ServerSideKmsKeyId](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Provides the identifier of the AWS KMS key used to encrypt inference scheduler data by
Amazon Lookout for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:aws[a-z\-]*:kms:[a-z0-9\-]*:\d{12}:[\w\-\/]+`

**[Status](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Indicates the status of the inference scheduler.

Type: String

Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`

**[UpdatedAt](#API_DescribeInferenceScheduler_ResponseSyntax "#API_DescribeInferenceScheduler_ResponseSyntax")**

Specifies the time at which the inference scheduler was last updated, if it was.

Type: Timestamp

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/cli2/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/boto3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeInferenceScheduler.md")
