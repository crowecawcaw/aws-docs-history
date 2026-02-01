# CreateFramework

Creates a framework with one or more controls. A framework is a collection of controls
that you can use to evaluate your backup practices. By using pre-built customizable
controls to define your policies, you can evaluate whether your backup practices comply
with your policies and which resources are not yet in compliance.

## Request Syntax

```
POST /audit/frameworks HTTP/1.1
Content-type: application/json

{
   "FrameworkControls": [
      {
         "ControlInputParameters": [
            {
               "ParameterName": "`string`",
               "ParameterValue": "`string`"
            }
         ],
         "ControlName": "`string`",
         "ControlScope": {
            "ComplianceResourceIds": [ "`string`" ],
            "ComplianceResourceTypes": [ "`string`" ],
            "Tags": {
               "`string`" : "`string`"
            }
         }
      }
   ],
   "FrameworkDescription": "`string`",
   "FrameworkName": "`string`",
   "FrameworkTags": {
      "`string`" : "`string`"
   },
   "IdempotencyToken": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[FrameworkControls](#API_CreateFramework_RequestSyntax "#API_CreateFramework_RequestSyntax")**

The controls that make up the framework. Each control in the list has a name,
input parameters, and scope.

Type: Array of [FrameworkControl](API_FrameworkControl.md "API_FrameworkControl.md") objects

Required: Yes

**[FrameworkDescription](#API_CreateFramework_RequestSyntax "#API_CreateFramework_RequestSyntax")**

An optional description of the framework with a maximum of 1,024 characters.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

**[FrameworkName](#API_CreateFramework_RequestSyntax "#API_CreateFramework_RequestSyntax")**

The unique name of the framework. The name must be between 1 and 256 characters,
starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and
underscores (\_).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

Required: Yes

**[FrameworkTags](#API_CreateFramework_RequestSyntax "#API_CreateFramework_RequestSyntax")**

The tags to assign to the framework.

Type: String to string map

Required: No

**[IdempotencyToken](#API_CreateFramework_RequestSyntax "#API_CreateFramework_RequestSyntax")**

A customer-chosen string that you can use to distinguish between otherwise identical
calls to `CreateFrameworkInput`. Retrying a successful request with the same
idempotency token results in a success message with no action taken.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "FrameworkArn": "***string***",
   "FrameworkName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[FrameworkArn](#API_CreateFramework_ResponseSyntax "#API_CreateFramework_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Type: String

**[FrameworkName](#API_CreateFramework_ResponseSyntax "#API_CreateFramework_ResponseSyntax")**

The unique name of the framework. The name must be between 1 and 256 characters,
starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and
underscores (\_).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AlreadyExistsException**

The required resource already exists.

**Arn**

**Context**

**CreatorRequestId**

**Type**

HTTP Status Code: 400

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**LimitExceededException**

A limit in the request has been exceeded; for example, a maximum number of items allowed
in a request.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateFramework.md "../../../goto/cli2/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/CreateFramework.md "../../../goto/DotNetSDKV4/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateFramework.md "../../../goto/boto3/backup-2018-11-15/CreateFramework.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateFramework.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateFramework.md")
