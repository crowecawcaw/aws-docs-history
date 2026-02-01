# DescribeFramework

Returns the framework details for the specified `FrameworkName`.

## Request Syntax

```
GET /audit/frameworks/`frameworkName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[frameworkName](#API_DescribeFramework_RequestSyntax "#API_DescribeFramework_RequestSyntax")**

The unique name of a framework.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "DeploymentStatus": "***string***",
   "FrameworkArn": "***string***",
   "FrameworkControls": [
      {
         "ControlInputParameters": [
            {
               "ParameterName": "***string***",
               "ParameterValue": "***string***"
            }
         ],
         "ControlName": "***string***",
         "ControlScope": {
            "ComplianceResourceIds": [ "***string***" ],
            "ComplianceResourceTypes": [ "***string***" ],
            "Tags": {
               "***string***" : "***string***"
            }
         }
      }
   ],
   "FrameworkDescription": "***string***",
   "FrameworkName": "***string***",
   "FrameworkStatus": "***string***",
   "IdempotencyToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

The date and time that a framework is created, in ISO 8601 representation. The value of `CreationTime` is accurate to milliseconds. For example,
2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind
UTC.

Type: Timestamp

**[DeploymentStatus](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

The deployment status of a framework. The statuses are:

`CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED |
 FAILED`

Type: String

**[FrameworkArn](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Type: String

**[FrameworkControls](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

The controls that make up the framework. Each control in the list has a name,
input parameters, and scope.

Type: Array of [FrameworkControl](API_FrameworkControl.md "API_FrameworkControl.md") objects

**[FrameworkDescription](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

An optional description of the framework.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `.*\S.*`

**[FrameworkName](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

The unique name of a framework.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

**[FrameworkStatus](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

A framework consists of one or more controls. Each control governs a resource, such as
backup plans, backup selections, backup vaults, or recovery points. You can also turn
AWS Config recording on or off for each resource. The statuses are:

- `ACTIVE` when recording is turned on for all resources governed by the
  framework.
- `PARTIALLY_ACTIVE` when recording is turned off for at least one
  resource governed by the framework.
- `INACTIVE` when recording is turned off for all resources governed by
  the framework.
- `UNAVAILABLE` when AWS Backup is unable to validate recording
  status at this time.

Type: String

**[IdempotencyToken](#API_DescribeFramework_ResponseSyntax "#API_DescribeFramework_ResponseSyntax")**

A customer-chosen string that you can use to distinguish between otherwise identical
calls to `DescribeFrameworkOutput`. Retrying a successful request with the same
idempotency token results in a success message with no action taken.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeFramework.md "../../../goto/cli2/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/DescribeFramework.md "../../../goto/DotNetSDKV4/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeFramework.md "../../../goto/boto3/backup-2018-11-15/DescribeFramework.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeFramework.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeFramework.md")
