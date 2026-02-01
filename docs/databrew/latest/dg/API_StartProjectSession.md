# StartProjectSession

Creates an interactive session, enabling you to manipulate data in a DataBrew
project.

## Request Syntax

```
PUT /projects/`name`/startProjectSession HTTP/1.1
Content-type: application/json

{
   "AssumeControl": `boolean`
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_StartProjectSession_RequestSyntax "#API_StartProjectSession_RequestSyntax")**

The name of the project to act upon.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[AssumeControl](#API_StartProjectSession_RequestSyntax "#API_StartProjectSession_RequestSyntax")**

A value that, if true, enables you to take control of a session, even if a different
client is currently accessing the project.

Type: Boolean

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ClientSessionId": "***string***",
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_StartProjectSession_ResponseSyntax "#API_StartProjectSession_ResponseSyntax")**

The name of the project to be acted upon.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[ClientSessionId](#API_StartProjectSession_ResponseSyntax "#API_StartProjectSession_ResponseSyntax")**

A system-generated identifier for the session.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/StartProjectSession.md "../../../goto/cli2/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/StartProjectSession.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForCpp/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForGoV2/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForKotlin/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/StartProjectSession.md "../../../goto/boto3/databrew-2017-07-25/StartProjectSession.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/StartProjectSession.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/StartProjectSession.md")
