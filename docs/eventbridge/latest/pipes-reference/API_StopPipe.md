# StopPipe

Stop an existing pipe.

## Request Syntax

```
POST /v1/pipes/`Name`/stop HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[Name](#API_StopPipe_RequestSyntax "#API_StopPipe_RequestSyntax")**

The name of the pipe.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[\.\-_A-Za-z0-9]+`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "***string***",
   "CreationTime": ***number***,
   "CurrentState": "***string***",
   "DesiredState": "***string***",
   "LastModifiedTime": ***number***,
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Arn](#API_StopPipe_ResponseSyntax "#API_StopPipe_ResponseSyntax")**

The ARN of the pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`

**[CreationTime](#API_StopPipe_ResponseSyntax "#API_StopPipe_ResponseSyntax")**

The time the pipe was created.

Type: Timestamp

**[CurrentState](#API_StopPipe_ResponseSyntax "#API_StopPipe_ResponseSyntax")**

The state the pipe is in.

Type: String

Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED`

**[DesiredState](#API_StopPipe_ResponseSyntax "#API_StopPipe_ResponseSyntax")**

The state the pipe should be in.

Type: String

Valid Values: `RUNNING | STOPPED`

**[LastModifiedTime](#API_StopPipe_ResponseSyntax "#API_StopPipe_ResponseSyntax")**

When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime "https://www.w3.org/TR/NOTE-datetime") (YYYY-MM-DDThh:mm:ss.sTZD).

Type: Timestamp

**[Name](#API_StopPipe_ResponseSyntax "#API_StopPipe_ResponseSyntax")**

The name of the pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[\.\-_A-Za-z0-9]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

An action you attempted resulted in an exception.

**resourceId**

The ID of the resource that caused the exception.

**resourceType**

The type of resource that caused the exception.

HTTP Status Code: 409

**InternalException**

This exception occurs due to unexpected causes.

**retryAfterSeconds**

The number of seconds to wait before retrying the action that caused the
exception.

HTTP Status Code: 500

**NotFoundException**

An entity that you specified does not exist.

HTTP Status Code: 404

**ThrottlingException**

An action was throttled.

**quotaCode**

The identifier of the quota that caused the exception.

**retryAfterSeconds**

The number of seconds to wait before retrying the action that caused the
exception.

**serviceCode**

The identifier of the service that caused the exception.

HTTP Status Code: 429

**ValidationException**

Indicates that an error has occurred while performing a validate operation.

**fieldList**

The list of fields for which validation failed and the corresponding failure
messages.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/pipes-2015-10-07/StopPipe.md "../../../goto/cli2/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/pipes-2015-10-07/StopPipe.md "../../../goto/DotNetSDKV3/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForCpp/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForGoV2/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForKotlin/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForPHPV3/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for Python](../../../goto/boto3/pipes-2015-10-07/StopPipe.md "../../../goto/boto3/pipes-2015-10-07/StopPipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/StopPipe.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/StopPipe.md")
