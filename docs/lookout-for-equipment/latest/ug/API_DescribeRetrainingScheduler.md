On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DescribeRetrainingScheduler

Provides a description of the retraining scheduler, including information such as the
model name and retraining parameters.

## Request Syntax

```
{
   "ModelName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ModelName](#API_DescribeRetrainingScheduler_RequestSyntax "#API_DescribeRetrainingScheduler_RequestSyntax")**

The name of the model that the retraining scheduler is attached to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

## Response Syntax

```
{
   "CreatedAt": ***number***,
   "LookbackWindow": "***string***",
   "ModelArn": "***string***",
   "ModelName": "***string***",
   "PromoteMode": "***string***",
   "RetrainingFrequency": "***string***",
   "RetrainingStartDate": ***number***,
   "Status": "***string***",
   "UpdatedAt": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreatedAt](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

Indicates the time and date at which the retraining scheduler was created.

Type: Timestamp

**[LookbackWindow](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

The number of past days of data used for retraining.

Type: String

Pattern: `^P180D$|^P360D$|^P540D$|^P720D$`

**[ModelArn](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

The ARN of the model that the retraining scheduler is attached to.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelName](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

The name of the model that the retraining scheduler is attached to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[PromoteMode](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

Indicates how the service uses new models. In `MANAGED` mode, new models are
used for inference if they have better performance than the current model. In
`MANUAL` mode, the new models are not used until they are [manually
activated](versioning-model.md#model-activation "versioning-model.md#model-activation").

Type: String

Valid Values: `MANAGED | MANUAL`

**[RetrainingFrequency](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

The frequency at which the model retraining is set. This follows the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations "https://en.wikipedia.org/wiki/ISO_8601#Durations")
guidelines.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 10.

Pattern: `^P(\dY)?(\d{1,2}M)?(\d{1,3}D)?$`

**[RetrainingStartDate](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the
nearest UTC day.

Type: Timestamp

**[Status](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

The status of the retraining scheduler.

Type: String

Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`

**[UpdatedAt](#API_DescribeRetrainingScheduler_ResponseSyntax "#API_DescribeRetrainingScheduler_ResponseSyntax")**

Indicates the time and date at which the retraining scheduler was updated.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/cli2/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/boto3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeRetrainingScheduler.md")
