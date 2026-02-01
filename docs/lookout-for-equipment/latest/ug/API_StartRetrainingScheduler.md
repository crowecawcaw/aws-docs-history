On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# StartRetrainingScheduler

Starts a retraining scheduler.

## Request Syntax

```
{
   "ModelName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ModelName](#API_StartRetrainingScheduler_RequestSyntax "#API_StartRetrainingScheduler_RequestSyntax")**

The name of the model whose retraining scheduler you want to start.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

## Response Syntax

```
{
   "ModelArn": "***string***",
   "ModelName": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ModelArn](#API_StartRetrainingScheduler_ResponseSyntax "#API_StartRetrainingScheduler_ResponseSyntax")**

The ARN of the model whose retraining scheduler is being started.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelName](#API_StartRetrainingScheduler_ResponseSyntax "#API_StartRetrainingScheduler_ResponseSyntax")**

The name of the model whose retraining scheduler is being started.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[Status](#API_StartRetrainingScheduler_ResponseSyntax "#API_StartRetrainingScheduler_ResponseSyntax")**

The status of the retraining scheduler.

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

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/cli2/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/boto3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/StartRetrainingScheduler.md")
