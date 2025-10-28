# ListPipes

Get the pipes associated with this account. For more information about pipes, see [Amazon EventBridge Pipes](../userguide/eb-pipes.md "../userguide/eb-pipes.md") in the Amazon EventBridge User Guide.

## Request Syntax

```
GET /v1/pipes?CurrentState=`CurrentState`&DesiredState=`DesiredState`&Limit=`Limit`&NamePrefix=`NamePrefix`&NextToken=`NextToken`&SourcePrefix=`SourcePrefix`&TargetPrefix=`TargetPrefix` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[CurrentState](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

The state the pipe is in.

Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED`

**[DesiredState](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

The state the pipe should be in.

Valid Values: `RUNNING | STOPPED`

**[Limit](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

The maximum number of pipes to include in the response.

Valid Range: Minimum value of 1. Maximum value of 100.

**[NamePrefix](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

A value that will return a subset of the pipes associated with this account. For
example, `"NamePrefix": "ABC"` will return all endpoints with "ABC" in the
name.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[\.\-_A-Za-z0-9]+`

**[NextToken](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page.
Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination
token will return an HTTP 400 InvalidToken error.

Length Constraints: Minimum length of 1. Maximum length of 2048.

**[SourcePrefix](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

The prefix matching the pipe source.

Length Constraints: Minimum length of 1. Maximum length of 1600.

**[TargetPrefix](#API_ListPipes_RequestSyntax "#API_ListPipes_RequestSyntax")**

The prefix matching the pipe target.

Length Constraints: Minimum length of 1. Maximum length of 1600.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Pipes": [
      {
         "Arn": "***string***",
         "CreationTime": ***number***,
         "CurrentState": "***string***",
         "DesiredState": "***string***",
         "Enrichment": "***string***",
         "LastModifiedTime": ***number***,
         "Name": "***string***",
         "Source": "***string***",
         "StateReason": "***string***",
         "Target": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListPipes_ResponseSyntax "#API_ListPipes_ResponseSyntax")**

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page.
Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination
token will return an HTTP 400 InvalidToken error.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

**[Pipes](#API_ListPipes_ResponseSyntax "#API_ListPipes_ResponseSyntax")**

The pipes returned by the call.

Type: Array of [Pipe](API_Pipe.md "API_Pipe.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception occurs due to unexpected causes.

**retryAfterSeconds**

The number of seconds to wait before retrying the action that caused the
exception.

HTTP Status Code: 500

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

- [AWS Command Line Interface V2](../../../goto/cli2/pipes-2015-10-07/ListPipes.md "../../../goto/cli2/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/pipes-2015-10-07/ListPipes.md "../../../goto/DotNetSDKV3/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForCpp/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForGoV2/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForJavaScriptV3/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForKotlin/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForPHPV3/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for Python](../../../goto/boto3/pipes-2015-10-07/ListPipes.md "../../../goto/boto3/pipes-2015-10-07/ListPipes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/ListPipes.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/ListPipes.md")
