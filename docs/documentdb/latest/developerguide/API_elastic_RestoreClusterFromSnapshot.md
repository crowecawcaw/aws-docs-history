# RestoreClusterFromSnapshot

Restores an elastic cluster from a snapshot.

## Request Syntax

```
POST /cluster-snapshot/`snapshotArn`/restore HTTP/1.1
Content-type: application/json

{
   "clusterName": "`string`",
   "kmsKeyId": "`string`",
   "shardCapacity": `number`,
   "shardInstanceCount": `number`,
   "subnetIds": [ "`string`" ],
   "tags": {
      "`string`" : "`string`"
   },
   "vpcSecurityGroupIds": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[snapshotArn](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

The ARN identifier of the elastic cluster snapshot.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[clusterName](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

The name of the elastic cluster.

Type: String

Required: Yes

**[kmsKeyId](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

The KMS key identifier to use to encrypt the new Amazon DocumentDB elastic clusters cluster.

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
encryption key. If you are creating a cluster using the same Amazon account
that owns this KMS encryption key, you can use the KMS key alias instead
of the ARN as the KMS encryption key.

If an encryption key is not specified here, Amazon DocumentDB uses the
default encryption key that KMS creates for your account. Your account
has a different default encryption key for each Amazon Region.

Type: String

Required: No

**[shardCapacity](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

The capacity of each shard in the new restored elastic cluster.

Type: Integer

Required: No

**[shardInstanceCount](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

The number of replica instances applying to all shards in the elastic cluster.
A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

Type: Integer

Required: No

**[subnetIds](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

The Amazon EC2 subnet IDs for the elastic cluster.

Type: Array of strings

Required: No

**[tags](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

A list of the tag names to be assigned to the restored elastic cluster, in the form of an array of key-value pairs in which the key is the tag name and the value is the key value.

Type: String to string map

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: No

**[vpcSecurityGroupIds](#API_elastic_RestoreClusterFromSnapshot_RequestSyntax "#API_elastic_RestoreClusterFromSnapshot_RequestSyntax")**

A list of EC2 VPC security groups to associate with the elastic cluster.

Type: Array of strings

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "cluster": {
      "adminUserName": "***string***",
      "authType": "***string***",
      "backupRetentionPeriod": ***number***,
      "clusterArn": "***string***",
      "clusterEndpoint": "***string***",
      "clusterName": "***string***",
      "createTime": "***string***",
      "kmsKeyId": "***string***",
      "preferredBackupWindow": "***string***",
      "preferredMaintenanceWindow": "***string***",
      "shardCapacity": ***number***,
      "shardCount": ***number***,
      "shardInstanceCount": ***number***,
      "shards": [
         {
            "createTime": "***string***",
            "shardId": "***string***",
            "status": "***string***"
         }
      ],
      "status": "***string***",
      "subnetIds": [ "***string***" ],
      "vpcSecurityGroupIds": [ "***string***" ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[cluster](#API_elastic_RestoreClusterFromSnapshot_ResponseSyntax "#API_elastic_RestoreClusterFromSnapshot_ResponseSyntax")**

Returns information about a the restored elastic cluster.

Type: [Cluster](API_elastic_Cluster.md "API_elastic_Cluster.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/cli2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/boto3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/RestoreClusterFromSnapshot.md")
