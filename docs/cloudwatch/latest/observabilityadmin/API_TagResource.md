# TagResource

Adds or updates tags for a telemetry rule resource.

## Request Syntax

```
POST /TagResource HTTP/1.1
Content-type: application/json

{
   "ResourceARN": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ResourceARN](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The Amazon Resource Name (ARN) of the telemetry rule resource to tag.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: Yes

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The key-value pairs to add or update for the telemetry rule resource.

Type: String to string map

Map Entries: Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

Indicates you don't have permissions to perform the requested operation. The user or role
that is making the request must have at least one IAM permissions policy attached that grants
the required permissions. For more information, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
IAM user guide.

**amznErrorType**

The name of the exception.

HTTP Status Code: 400

**InternalServerException**

Indicates the request has failed to process because of an unknown server error,
exception, or failure.

**amznErrorType**

The name of the exception.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource (such as a telemetry rule) could not be found.

HTTP Status Code: 404

**ServiceQuotaExceededException**

The requested operation would exceed the allowed quota for the specified resource type.

**amznErrorType**

The name of the exception.

HTTP Status Code: 402

**TooManyRequestsException**

The request throughput limit was exceeded.

HTTP Status Code: 429

**ValidationException**

Indicates input validation failed. Check your request parameters and retry the request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/observabilityadmin-2018-05-10/TagResource.md "../../../goto/cli2/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/TagResource.md "../../../goto/DotNetSDKV3/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForGoV2/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForJavaScriptV3/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForKotlin/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForPHPV3/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/observabilityadmin-2018-05-10/TagResource.md "../../../goto/boto3/observabilityadmin-2018-05-10/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TagResource.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TagResource.md")
