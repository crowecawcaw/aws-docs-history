# CopyClusterSnapshot

Copies a snapshot of an elastic cluster.

## Request Syntax

```
POST /cluster-snapshot/`snapshotArn`/copy HTTP/1.1
Content-type: application/json

{
   "copyTags": `boolean`,
   "kmsKeyId": "`string`",
   "tags": {
      "`string`" : "`string`"
   },
   "targetSnapshotName": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[snapshotArn](#API_elastic_CopyClusterSnapshot_RequestSyntax "#API_elastic_CopyClusterSnapshot_RequestSyntax")**

The Amazon Resource Name (ARN) identifier of the elastic cluster snapshot.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[targetSnapshotName](#API_elastic_CopyClusterSnapshot_RequestSyntax "#API_elastic_CopyClusterSnapshot_RequestSyntax")**

The identifier of the new elastic cluster snapshot to create from the source cluster snapshot.
This parameter is not case sensitive.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `elastic-cluster-snapshot-5`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Required: Yes

**[copyTags](#API_elastic_CopyClusterSnapshot_RequestSyntax "#API_elastic_CopyClusterSnapshot_RequestSyntax")**

Set to `true` to copy all tags from the source cluster snapshot to the target elastic cluster snapshot.
The default is `false`.

Type: Boolean

Required: No

**[kmsKeyId](#API_elastic_CopyClusterSnapshot_RequestSyntax "#API_elastic_CopyClusterSnapshot_RequestSyntax")**

The AWS KMS key ID for an encrypted elastic cluster snapshot.
The AWS KMS key ID is the Amazon Resource Name (ARN), AWS KMS key identifier, or the AWS KMS key alias for the AWS KMS encryption key.

If you copy an encrypted elastic cluster snapshot from your AWS account, you can specify a value for `KmsKeyId` to encrypt the copy with a new AWSS KMS encryption key.
If you don't specify a value for `KmsKeyId`, then the copy of the elastic cluster snapshot is encrypted with the same `AWS` KMS key as the source elastic cluster snapshot.

If you copy an unencrypted elastic cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.

Type: String

Required: No

**[tags](#API_elastic_CopyClusterSnapshot_RequestSyntax "#API_elastic_CopyClusterSnapshot_RequestSyntax")**

The tags to be assigned to the elastic cluster snapshot.

Type: String to string map

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "snapshot": {
      "adminUserName": "***string***",
      "clusterArn": "***string***",
      "clusterCreationTime": "***string***",
      "kmsKeyId": "***string***",
      "snapshotArn": "***string***",
      "snapshotCreationTime": "***string***",
      "snapshotName": "***string***",
      "snapshotType": "***string***",
      "status": "***string***",
      "subnetIds": [ "***string***" ],
      "vpcSecurityGroupIds": [ "***string***" ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[snapshot](#API_elastic_CopyClusterSnapshot_ResponseSyntax "#API_elastic_CopyClusterSnapshot_ResponseSyntax")**

Returns information about a specific elastic cluster snapshot.

Type: [ClusterSnapshot](API_elastic_ClusterSnapshot.md "API_elastic_ClusterSnapshot.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

An exception that occurs when there are not sufficient permissions to perform an action.

**message**

An error message explaining why access was denied.

HTTP Status Code: 403

**ConflictException**

There was an access conflict.

**resourceId**

The ID of the resource where there was an access conflict.

**resourceType**

The type of the resource where there was an access conflict.

HTTP Status Code: 409

**InternalServerException**

There was an internal server error.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource could not be located.

**message**

An error message describing the failure.

**resourceId**

The ID of the resource that could not be located.

**resourceType**

The type of the resource that could not be found.

HTTP Status Code: 404

**ServiceQuotaExceededException**

The service quota for the action was exceeded.

HTTP Status Code: 402

**ThrottlingException**

ThrottlingException will be thrown when request was denied due to request throttling.

**retryAfterSeconds**

The number of seconds to wait before retrying the operation.

HTTP Status Code: 429

**ValidationException**

A structure defining a validation exception.

**fieldList**

A list of the fields in which the validation exception occurred.

**message**

An error message describing the validation exception.

**reason**

The reason why the validation exception occurred (one of `unknownOperation`,
`cannotParse`, `fieldValidationFailed`, or `other`).

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/cli2/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/boto3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/CopyClusterSnapshot.md")
