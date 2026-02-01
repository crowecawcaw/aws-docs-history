# CreateWorkerConfiguration

Creates a worker configuration using the specified properties.

## Request Syntax

```
POST /v1/worker-configurations HTTP/1.1
Content-type: application/json

{
   "description": "`string`",
   "name": "`string`",
   "propertiesFileContent": "`string`",
   "tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[description](#API_CreateWorkerConfiguration_RequestSyntax "#API_CreateWorkerConfiguration_RequestSyntax")**

A summary description of the worker configuration.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: No

**[name](#API_CreateWorkerConfiguration_RequestSyntax "#API_CreateWorkerConfiguration_RequestSyntax")**

The name of the worker configuration.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

**[propertiesFileContent](#API_CreateWorkerConfiguration_RequestSyntax "#API_CreateWorkerConfiguration_RequestSyntax")**

Base64 encoded contents of connect-distributed.properties file.

Type: String

Required: Yes

**[tags](#API_CreateWorkerConfiguration_RequestSyntax "#API_CreateWorkerConfiguration_RequestSyntax")**

The tags you want to attach to the worker configuration.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "***string***",
   "latestRevision": {
      "creationTime": "***string***",
      "description": "***string***",
      "revision": ***number***
   },
   "name": "***string***",
   "workerConfigurationArn": "***string***",
   "workerConfigurationState": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[creationTime](#API_CreateWorkerConfiguration_ResponseSyntax "#API_CreateWorkerConfiguration_ResponseSyntax")**

The time that the worker configuration was created.

Type: Timestamp

**[latestRevision](#API_CreateWorkerConfiguration_ResponseSyntax "#API_CreateWorkerConfiguration_ResponseSyntax")**

The latest revision of the worker configuration.

Type: [WorkerConfigurationRevisionSummary](API_WorkerConfigurationRevisionSummary.md "API_WorkerConfigurationRevisionSummary.md") object

**[name](#API_CreateWorkerConfiguration_ResponseSyntax "#API_CreateWorkerConfiguration_ResponseSyntax")**

The name of the worker configuration.

Type: String

**[workerConfigurationArn](#API_CreateWorkerConfiguration_ResponseSyntax "#API_CreateWorkerConfiguration_ResponseSyntax")**

The Amazon Resource Name (ARN) that Amazon assigned to the worker configuration.

Type: String

**[workerConfigurationState](#API_CreateWorkerConfiguration_ResponseSyntax "#API_CreateWorkerConfiguration_ResponseSyntax")**

The state of the worker configuration.

Type: String

Valid Values: `ACTIVE | DELETING`

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

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/cli2/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/boto3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/CreateWorkerConfiguration.md")
