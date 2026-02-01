# DeleteCustomPlugin

Deletes a custom plugin.

## Request Syntax

```
DELETE /v1/custom-plugins/`customPluginArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[customPluginArn](#API_DeleteCustomPlugin_RequestSyntax "#API_DeleteCustomPlugin_RequestSyntax")**

The Amazon Resource Name (ARN) of the custom plugin that you want to delete.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "customPluginArn": "***string***",
   "customPluginState": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[customPluginArn](#API_DeleteCustomPlugin_ResponseSyntax "#API_DeleteCustomPlugin_ResponseSyntax")**

The Amazon Resource Name (ARN) of the custom plugin that you requested to delete.

Type: String

**[customPluginState](#API_DeleteCustomPlugin_ResponseSyntax "#API_DeleteCustomPlugin_ResponseSyntax")**

The state of the custom plugin.

Type: String

Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**BadRequestException**

HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then
retry it.

HTTP Status Code: 400

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

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/cli2/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/boto3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DeleteCustomPlugin.md")
