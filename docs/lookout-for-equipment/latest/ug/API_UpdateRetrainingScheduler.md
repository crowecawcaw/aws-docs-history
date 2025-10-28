On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# UpdateRetrainingScheduler

Updates a retraining scheduler.

## Request Syntax

```
{
   "LookbackWindow": "`string`",
   "ModelName": "`string`",
   "PromoteMode": "`string`",
   "RetrainingFrequency": "`string`",
   "RetrainingStartDate": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[LookbackWindow](#API_UpdateRetrainingScheduler_RequestSyntax "#API_UpdateRetrainingScheduler_RequestSyntax")**

The number of past days of data that will be used for retraining.

Type: String

Pattern: `^P180D$|^P360D$|^P540D$|^P720D$`

Required: No

**[ModelName](#API_UpdateRetrainingScheduler_RequestSyntax "#API_UpdateRetrainingScheduler_RequestSyntax")**

The name of the model whose retraining scheduler you want to update.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[PromoteMode](#API_UpdateRetrainingScheduler_RequestSyntax "#API_UpdateRetrainingScheduler_RequestSyntax")**

Indicates how the service will use new models. In `MANAGED` mode, new models
will automatically be used for inference if they have better performance than the current
model. In `MANUAL` mode, the new models will not be used [until they
are manually activated](versioning-model.md#model-activation "versioning-model.md#model-activation").

Type: String

Valid Values: `MANAGED | MANUAL`

Required: No

**[RetrainingFrequency](#API_UpdateRetrainingScheduler_RequestSyntax "#API_UpdateRetrainingScheduler_RequestSyntax")**

This parameter uses the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations "https://en.wikipedia.org/wiki/ISO_8601#Durations") standard to set the frequency at which you want retraining to occur in
terms of Years, Months, and/or Days (note: other parameters like Time are not currently
supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For
example, the following values are valid:

- P3M15D – Every 3 months and 15 days
- P2M – Every 2 months
- P150D – Every 150 days

Type: String

Length Constraints: Minimum length of 1. Maximum length of 10.

Pattern: `^P(\dY)?(\d{1,2}M)?(\d{1,3}D)?$`

Required: No

**[RetrainingStartDate](#API_UpdateRetrainingScheduler_RequestSyntax "#API_UpdateRetrainingScheduler_RequestSyntax")**

The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the
nearest UTC day.

Type: Timestamp

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/cli2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/boto3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateRetrainingScheduler.md")
