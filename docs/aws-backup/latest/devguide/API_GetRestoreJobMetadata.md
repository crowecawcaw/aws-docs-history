# GetRestoreJobMetadata

This request returns the metadata for the specified restore job.

## Request Syntax

```
GET /restore-jobs/`restoreJobId`/metadata HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[restoreJobId](#API_GetRestoreJobMetadata_RequestSyntax "#API_GetRestoreJobMetadata_RequestSyntax")**

This is a unique identifier of a restore job within AWS Backup.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Metadata": {
      "***string***" : "***string***"
   },
   "RestoreJobId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Metadata](#API_GetRestoreJobMetadata_ResponseSyntax "#API_GetRestoreJobMetadata_ResponseSyntax")**

This contains the metadata of the specified backup job.

Type: String to string map

**[RestoreJobId](#API_GetRestoreJobMetadata_ResponseSyntax "#API_GetRestoreJobMetadata_ResponseSyntax")**

This is a unique identifier of a restore job within AWS Backup.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/cli2/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForCpp/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/boto3/backup-2018-11-15/GetRestoreJobMetadata.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreJobMetadata.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetRestoreJobMetadata.md")
