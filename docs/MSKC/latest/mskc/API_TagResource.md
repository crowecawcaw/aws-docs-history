# TagResource

Attaches tags to the specified resource.

## Request Syntax

```
POST /v1/tags/`resourceArn` HTTP/1.1
Content-type: application/json

{
   "tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The Amazon Resource Name (ARN) of the resource to which you want to attach tags.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The tags that you want to attach to the resource.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**BadRequestException**

HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then
retry it.

HTTP Status Code: 400

**ConflictException**

HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your
request with another name.

HTTP Status Code: 409

**ForbiddenException**

HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your
request.

HTTP Status Code: 403

**InternalServerErrorException**

HTTP Status Code 500: Unexpected internal server error. Retrying your request might
resolve the issue.

HTTP Status Code: 500

**NotFoundException**

HTTP Status Code 404: Resource not found due to incorrect input. Correct your request
and then retry it.

HTTP Status Code: 404

**ServiceUnavailableException**

HTTP Status Code 503: Service Unavailable. Retrying your request in some time might
resolve the issue.

HTTP Status Code: 503

**TooManyRequestsException**

HTTP Status Code 429: Limit exceeded. Resource limit reached.

HTTP Status Code: 429

**UnauthorizedException**

HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be
validated.

HTTP Status Code: 401

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/TagResource.md "../../../goto/cli2/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kafkaconnect-2021-09-14/TagResource.md "../../../goto/DotNetSDKV3/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/TagResource.md "../../../goto/boto3/kafkaconnect-2021-09-14/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/TagResource.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/TagResource.md")
