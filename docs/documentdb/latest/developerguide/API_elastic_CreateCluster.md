# CreateCluster

Creates a new Amazon DocumentDB elastic cluster and returns its cluster structure.

## Request Syntax

```
POST /cluster HTTP/1.1
Content-type: application/json

{
   "adminUserName": "`string`",
   "adminUserPassword": "`string`",
   "authType": "`string`",
   "backupRetentionPeriod": `number`,
   "clientToken": "`string`",
   "clusterName": "`string`",
   "kmsKeyId": "`string`",
   "preferredBackupWindow": "`string`",
   "preferredMaintenanceWindow": "`string`",
   "shardCapacity": `number`,
   "shardCount": `number`,
   "shardInstanceCount": `number`,
   "subnetIds": [ "`string`" ],
   "tags": {
      "`string`" : "`string`"
   },
   "vpcSecurityGroupIds": [ "`string`" ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[adminUserName](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The name of the Amazon DocumentDB elastic clusters administrator.

_Constraints_:

- Must be from 1 to 63 letters or numbers.
- The first character must be a letter.
- Cannot be a reserved word.

Type: String

Required: Yes

**[adminUserPassword](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The password for the Amazon DocumentDB elastic clusters administrator. The password can contain any printable ASCII characters.

_Constraints_:

- Must contain from 8 to 100 characters.
- Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).

Type: String

Required: Yes

**[authType](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The authentication type used to determine where to fetch the password used for accessing the elastic cluster.
Valid types are `PLAIN_TEXT` or `SECRET_ARN`.

Type: String

Valid Values: `PLAIN_TEXT | SECRET_ARN`

Required: Yes

**[clusterName](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The name of the new elastic cluster. This parameter is stored as
a lowercase string.

_Constraints_:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

_Example_: `my-cluster`

Type: String

Required: Yes

**[shardCapacity](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.

Type: Integer

Required: Yes

**[shardCount](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The number of shards assigned to the elastic cluster. Maximum is 32.

Type: Integer

Required: Yes

**[backupRetentionPeriod](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The number of days for which automatic snapshots are retained.

Type: Integer

Required: No

**[clientToken](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The client token for the elastic cluster.

Type: String

Required: No

**[kmsKeyId](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The KMS key identifier to use to encrypt the new elastic cluster.

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS
encryption key. If you are creating a cluster using the same Amazon account
that owns this KMS encryption key, you can use the KMS key alias instead
of the ARN as the KMS encryption key.

If an encryption key is not specified, Amazon DocumentDB uses the
default encryption key that KMS creates for your account. Your account
has a different default encryption key for each Amazon Region.

Type: String

Required: No

**[preferredBackupWindow](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The daily time range during which automated backups are created if automated backups are enabled, as determined by the `backupRetentionPeriod`.

Type: String

Required: No

**[preferredMaintenanceWindow](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

_Format_: `ddd:hh24:mi-ddd:hh24:mi`

_Default_: a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.

_Valid days_: Mon, Tue, Wed, Thu, Fri, Sat, Sun

_Constraints_: Minimum 30-minute window.

Type: String

Required: No

**[shardInstanceCount](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The number of replica instances applying to all shards in the elastic cluster.
A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

Type: Integer

Required: No

**[subnetIds](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The Amazon EC2 subnet IDs for the new elastic cluster.

Type: Array of strings

Required: No

**[tags](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

The tags to be assigned to the new elastic cluster.

Type: String to string map

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Required: No

**[vpcSecurityGroupIds](#API_elastic_CreateCluster_RequestSyntax "#API_elastic_CreateCluster_RequestSyntax")**

A list of EC2 VPC security groups to associate with the new
elastic cluster.

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

**[cluster](#API_elastic_CreateCluster_ResponseSyntax "#API_elastic_CreateCluster_ResponseSyntax")**

The new elastic cluster that has been created.

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/cli2/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/DotNetSDKV3/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/boto3/docdb-elastic-2022-11-28/CreateCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/CreateCluster.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/CreateCluster.md")
