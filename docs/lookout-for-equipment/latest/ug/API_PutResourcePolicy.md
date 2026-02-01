On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# PutResourcePolicy

Creates a resource control policy for a given resource.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "PolicyRevisionId": "`string`",
   "ResourceArn": "`string`",
   "ResourcePolicy": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_PutResourcePolicy_RequestSyntax "#API_PutResourcePolicy_RequestSyntax")**

A unique identifier for the request. If you do not set the client request token,
Amazon Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[PolicyRevisionId](#API_PutResourcePolicy_RequestSyntax "#API_PutResourcePolicy_RequestSyntax")**

A unique identifier for a revision of the resource policy.

Type: String

Length Constraints: Maximum length of 50.

Pattern: `[0-9A-Fa-f]+`

Required: No

**[ResourceArn](#API_PutResourcePolicy_RequestSyntax "#API_PutResourcePolicy_RequestSyntax")**

The Amazon Resource Name (ARN) of the resource for which the policy is being
created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:.+`

Required: Yes

**[ResourcePolicy](#API_PutResourcePolicy_RequestSyntax "#API_PutResourcePolicy_RequestSyntax")**

The JSON-formatted resource policy to create.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20000.

Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

Required: Yes

## Response Syntax

```
{
   "PolicyRevisionId": "***string***",
   "ResourceArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PolicyRevisionId](#API_PutResourcePolicy_ResponseSyntax "#API_PutResourcePolicy_ResponseSyntax")**

A unique identifier for a revision of the resource policy.

Type: String

Length Constraints: Maximum length of 50.

Pattern: `[0-9A-Fa-f]+`

**[ResourceArn](#API_PutResourcePolicy_ResponseSyntax "#API_PutResourcePolicy_ResponseSyntax")**

The Amazon Resource Name (ARN) of the resource for which the policy was created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:.+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/cli2/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/boto3/lookoutequipment-2020-12-15/PutResourcePolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/PutResourcePolicy.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/PutResourcePolicy.md")
