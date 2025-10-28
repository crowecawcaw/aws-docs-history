# DescribeProtectedResource

Returns information about a saved resource, including the last time it was backed up,
its Amazon Resource Name (ARN), and the AWS service type of the saved
resource.

## Request Syntax

```
GET /resources/`resourceArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_DescribeProtectedResource_RequestSyntax "#API_DescribeProtectedResource_RequestSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "LastBackupTime": ***number***,
   "LastBackupVaultArn": "***string***",
   "LastRecoveryPointArn": "***string***",
   "LatestRestoreExecutionTimeMinutes": ***number***,
   "LatestRestoreJobCreationDate": ***number***,
   "LatestRestoreRecoveryPointCreationDate": ***number***,
   "ResourceArn": "***string***",
   "ResourceName": "***string***",
   "ResourceType": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LastBackupTime](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The date and time that a resource was last backed up, in Unix format and Coordinated
Universal Time (UTC). The value of `LastBackupTime` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[LastBackupVaultArn](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The ARN (Amazon Resource Name) of the backup vault
that contains the most recent backup recovery point.

Type: String

**[LastRecoveryPointArn](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The ARN (Amazon Resource Name) of the most recent
recovery point.

Type: String

**[LatestRestoreExecutionTimeMinutes](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The time, in minutes, that the most recent restore job took to complete.

Type: Long

**[LatestRestoreJobCreationDate](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The creation date of the most recent restore job.

Type: Timestamp

**[LatestRestoreRecoveryPointCreationDate](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The date the most recent recovery point was created.

Type: Timestamp

**[ResourceArn](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

An ARN that uniquely identifies a resource. The format of the ARN depends on the
resource type.

Type: String

**[ResourceName](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The name of the resource that belongs to the specified backup.

Type: String

**[ResourceType](#API_DescribeProtectedResource_ResponseSyntax "#API_DescribeProtectedResource_ResponseSyntax")**

The type of AWS resource saved as a recovery point; for example, an
Amazon EBS volume or an Amazon RDS database.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/cli2/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/DotNetSDKV3/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForCpp/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForGoV2/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForJavaV2/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForKotlin/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForPHPV3/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/boto3/backup-2018-11-15/DescribeProtectedResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeProtectedResource.md "../../../goto/SdkForRubyV3/backup-2018-11-15/DescribeProtectedResource.md")
