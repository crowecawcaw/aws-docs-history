On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# CreateInferenceScheduler

Creates a scheduled inference. Scheduling an inference is setting up a continuous
real-time inference plan to analyze new measurement data. When setting up the schedule, you
provide an S3 bucket location for the input data, assign it a delimiter between separate
entries in the data, set an offset delay if desired, and set the frequency of inferencing.
You must also provide an S3 bucket location for the output data.

## Request Syntax

```
{
   "ClientToken": "`string`",
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
   "ModelName": "`string`",
   "RoleArn": "`string`",
   "ServerSideKmsKeyId": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

A unique identifier for the request. If you do not set the client request token, Amazon
Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[DataDelayOffsetInMinutes](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

The interval (in minutes) of planned delay at the start of each inference segment. For
example, if inference is set to run every ten minutes, the delay is set to five minutes and
the time is 09:08. The inference scheduler will wake up at the configured interval (which,
without a delay configured, would be 09:10) plus the additional five minute delay time (so
09:15) to check your Amazon S3 bucket. The delay provides a buffer for you to upload data at the
same frequency, so that you don't have to stop and restart the scheduler when uploading new
data.

For more information, see [Understanding
the inference process](understanding-inference-process.md "understanding-inference-process.md").

Type: Long

Valid Range: Minimum value of 0. Maximum value of 60.

Required: No

**[DataInputConfiguration](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

Specifies configuration information for the input data for the inference scheduler,
including delimiter, format, and dataset location.

Type: [InferenceInputConfiguration](API_InferenceInputConfiguration.md "API_InferenceInputConfiguration.md") object

Required: Yes

**[DataOutputConfiguration](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

Specifies configuration information for the output results for the inference scheduler,
including the S3 location for the output.

Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md "API_InferenceOutputConfiguration.md") object

Required: Yes

**[DataUploadFrequency](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

How often data is uploaded to the source Amazon S3 bucket for the input data. The value
chosen is the length of time between data uploads. For instance, if you select 5 minutes,
Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This
frequency also determines how often Amazon Lookout for Equipment runs inference on your data.

For more information, see [Understanding
the inference process](understanding-inference-process.md "understanding-inference-process.md").

Type: String

Valid Values: `PT5M | PT10M | PT15M | PT30M | PT1H`

Required: Yes

**[InferenceSchedulerName](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

The name of the inference scheduler being created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[ModelName](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

The name of the previously trained machine learning model being used to create the
inference scheduler.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[RoleArn](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source being
used for the inference.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

Required: Yes

**[ServerSideKmsKeyId](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

Provides the identifier of the AWS KMS key used to encrypt inference scheduler data by
Amazon Lookout for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

Required: No

**[Tags](#API_CreateInferenceScheduler_RequestSyntax "#API_CreateInferenceScheduler_RequestSyntax")**

Any tags associated with the inference scheduler.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "InferenceSchedulerArn": "***string***",
   "InferenceSchedulerName": "***string***",
   "ModelQuality": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[InferenceSchedulerArn](#API_CreateInferenceScheduler_ResponseSyntax "#API_CreateInferenceScheduler_ResponseSyntax")**

The Amazon Resource Name (ARN) of the inference scheduler being created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`

**[InferenceSchedulerName](#API_CreateInferenceScheduler_ResponseSyntax "#API_CreateInferenceScheduler_ResponseSyntax")**

The name of inference scheduler being created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[ModelQuality](#API_CreateInferenceScheduler_ResponseSyntax "#API_CreateInferenceScheduler_ResponseSyntax")**

Provides a quality assessment for a model that uses labels.
If Lookout for Equipment determines that the
model quality is poor based on training metrics, the value is
`POOR_QUALITY_DETECTED`. Otherwise, the value is
`QUALITY_THRESHOLD_MET`.

If the model is unlabeled, the model quality can't
be assessed and the value of `ModelQuality` is
`CANNOT_DETERMINE_QUALITY`. In this situation, you can get a model quality
assessment by adding labels to the input dataset and retraining the model.

For information about using labels with your models, see [Understanding labeling](understanding-labeling.md "understanding-labeling.md").

For information about improving the quality of a model, see [Best practices with
Amazon Lookout for Equipment](best-practices.md "best-practices.md").

Type: String

Valid Values: `QUALITY_THRESHOLD_MET | CANNOT_DETERMINE_QUALITY | POOR_QUALITY_DETECTED`

**[Status](#API_CreateInferenceScheduler_ResponseSyntax "#API_CreateInferenceScheduler_ResponseSyntax")**

Indicates the status of the `CreateInferenceScheduler` operation.

Type: String

Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`

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

**ServiceQuotaExceededException**

Resource limitations have been exceeded.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/cli2/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/boto3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateInferenceScheduler.md")
