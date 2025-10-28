On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# UpdateActiveModelVersion

Sets the active model version for a given machine learning model.

## Request Syntax

```
{
   "ModelName": "`string`",
   "ModelVersion": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ModelName](#API_UpdateActiveModelVersion_RequestSyntax "#API_UpdateActiveModelVersion_RequestSyntax")**

The name of the machine learning model for which the active model version is being
set.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[ModelVersion](#API_UpdateActiveModelVersion_RequestSyntax "#API_UpdateActiveModelVersion_RequestSyntax")**

The version of the machine learning model for which the active model version is being
set.

Type: Long

Valid Range: Minimum value of 1.

Required: Yes

## Response Syntax

```
{
   "CurrentActiveVersion": ***number***,
   "CurrentActiveVersionArn": "***string***",
   "ModelArn": "***string***",
   "ModelName": "***string***",
   "PreviousActiveVersion": ***number***,
   "PreviousActiveVersionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CurrentActiveVersion](#API_UpdateActiveModelVersion_ResponseSyntax "#API_UpdateActiveModelVersion_ResponseSyntax")**

The version that is currently active of the machine learning model for which the active
model version was set.

Type: Long

Valid Range: Minimum value of 1.

**[CurrentActiveVersionArn](#API_UpdateActiveModelVersion_ResponseSyntax "#API_UpdateActiveModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the machine learning model version that is the current
active model version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[ModelArn](#API_UpdateActiveModelVersion_ResponseSyntax "#API_UpdateActiveModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the machine learning model for which the active model
version was set.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelName](#API_UpdateActiveModelVersion_ResponseSyntax "#API_UpdateActiveModelVersion_ResponseSyntax")**

The name of the machine learning model for which the active model version was
set.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[PreviousActiveVersion](#API_UpdateActiveModelVersion_ResponseSyntax "#API_UpdateActiveModelVersion_ResponseSyntax")**

The previous version that was active of the machine learning model for which the active
model version was set.

Type: Long

Valid Range: Minimum value of 1.

**[PreviousActiveVersionArn](#API_UpdateActiveModelVersion_ResponseSyntax "#API_UpdateActiveModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the machine learning model version that was the
previous active model version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/cli2/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/boto3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/UpdateActiveModelVersion.md")
