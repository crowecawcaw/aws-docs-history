# DescribeCustomPlugin

A summary description of the custom plugin.

## Request Syntax

```
GET /v1/custom-plugins/`customPluginArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[customPluginArn](#API_DescribeCustomPlugin_RequestSyntax "#API_DescribeCustomPlugin_RequestSyntax")**

Returns information about a custom plugin.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "***string***",
   "customPluginArn": "***string***",
   "customPluginState": "***string***",
   "description": "***string***",
   "latestRevision": {
      "contentType": "***string***",
      "creationTime": "***string***",
      "description": "***string***",
      "fileDescription": {
         "fileMd5": "***string***",
         "fileSize": ***number***
      },
      "location": {
         "s3Location": {
            "bucketArn": "***string***",
            "fileKey": "***string***",
            "objectVersion": "***string***"
         }
      },
      "revision": ***number***
   },
   "name": "***string***",
   "stateDescription": {
      "code": "***string***",
      "message": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[creationTime](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

The time that the custom plugin was created.

Type: Timestamp

**[customPluginArn](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

The Amazon Resource Name (ARN) of the custom plugin.

Type: String

**[customPluginState](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

The state of the custom plugin.

Type: String

Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING`

**[description](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

The description of the custom plugin.

Type: String

**[latestRevision](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

The latest successfully created revision of the custom plugin. If there are no
successfully created revisions, this field will be absent.

Type: [CustomPluginRevisionSummary](API_CustomPluginRevisionSummary.md "API_CustomPluginRevisionSummary.md") object

**[name](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

The name of the custom plugin.

Type: String

**[stateDescription](#API_DescribeCustomPlugin_ResponseSyntax "#API_DescribeCustomPlugin_ResponseSyntax")**

Details about the state of a custom plugin.

Type: [StateDescription](API_StateDescription.md "API_StateDescription.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/cli2/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/boto3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/DescribeCustomPlugin.md")
