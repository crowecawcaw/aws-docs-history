On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DeleteModel

Deletes a machine learning model currently available for Amazon Lookout for Equipment. This will prevent it
from being used with an inference scheduler, even one that is already set up.

## Request Syntax

```
{
   "ModelName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ModelName](#API_DeleteModel_RequestSyntax "#API_DeleteModel_RequestSyntax")**

The name of the machine learning model to be deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/cli2/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/boto3/lookoutequipment-2020-12-15/DeleteModel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DeleteModel.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DeleteModel.md")
