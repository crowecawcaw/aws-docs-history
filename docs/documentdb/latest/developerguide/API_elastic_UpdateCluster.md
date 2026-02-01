# UpdateCluster

Modifies an elastic cluster. This includes updating admin-username/password,
upgrading the API version, and setting up a backup window and maintenance window

## Request Syntax

```
PUT /cluster/`clusterArn` HTTP/1.1
Content-type: application/json

{
   "adminUserPassword": "`string`",
   "authType": "`string`",
   "backupRetentionPeriod": `number`,
   "clientToken": "`string`",
   "preferredBackupWindow": "`string`",
   "preferredMaintenanceWindow": "`string`",
   "shardCapacity": `number`,
   "shardCount": `number`,
   "shardInstanceCount": `number`,
   "subnetIds": [ "`string`" ],
   "vpcSecurityGroupIds": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[clusterArn](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The ARN identifier of the elastic cluster.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[adminUserPassword](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The password associated with the elastic cluster administrator.
This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).

_Constraints_: Must contain from 8 to 100 characters.

Type: String

Required: No

**[authType](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The authentication type used to determine where to fetch the password used for accessing the elastic cluster.
Valid types are `PLAIN_TEXT` or `SECRET_ARN`.

Type: String

Valid Values: `PLAIN_TEXT | SECRET_ARN`

Required: No

**[backupRetentionPeriod](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The number of days for which automatic snapshots are retained.

Type: Integer

Required: No

**[clientToken](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The client token for the elastic cluster.

Type: String

Required: No

**[preferredBackupWindow](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The daily time range during which automated backups are created if automated backups are enabled, as determined by the `backupRetentionPeriod`.

Type: String

Required: No

**[preferredMaintenanceWindow](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

_Format_: `ddd:hh24:mi-ddd:hh24:mi`

_Default_: a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.

_Valid days_: Mon, Tue, Wed, Thu, Fri, Sat, Sun

_Constraints_: Minimum 30-minute window.

Type: String

Required: No

**[shardCapacity](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The number of vCPUs assigned to each elastic cluster shard.
Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.

Type: Integer

Required: No

**[shardCount](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The number of shards assigned to the elastic cluster. Maximum is 32.

Type: Integer

Required: No

**[shardInstanceCount](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The number of replica instances applying to all shards in the elastic cluster.
A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

Type: Integer

Required: No

**[subnetIds](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

The Amazon EC2 subnet IDs for the elastic cluster.

Type: Array of strings

Required: No

**[vpcSecurityGroupIds](#API_elastic_UpdateCluster_RequestSyntax "#API_elastic_UpdateCluster_RequestSyntax")**

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

**[cluster](#API_elastic_UpdateCluster_ResponseSyntax "#API_elastic_UpdateCluster_ResponseSyntax")**

Returns information about the updated elastic cluster.

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/cli2/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/boto3/docdb-elastic-2022-11-28/UpdateCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/UpdateCluster.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/UpdateCluster.md")
