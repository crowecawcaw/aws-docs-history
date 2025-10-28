# Cluster

Returns information about a specific elastic cluster.

## Contents

###### Note

In the following list, the required parameters are described first.

**adminUserName**

The name of the elastic cluster administrator.

Type: String

Required: Yes

**authType**

The authentication type for the elastic cluster.

Type: String

Valid Values: `PLAIN_TEXT | SECRET_ARN`

Required: Yes

**clusterArn**

The ARN identifier of the elastic cluster.

Type: String

Required: Yes

**clusterEndpoint**

The URL used to connect to the elastic cluster.

Type: String

Required: Yes

**clusterName**

The name of the elastic cluster.

Type: String

Required: Yes

**createTime**

The time when the elastic cluster was created in Universal Coordinated Time (UTC).

Type: String

Required: Yes

**kmsKeyId**

The KMS key identifier to use to encrypt the elastic cluster.

Type: String

Required: Yes

**preferredMaintenanceWindow**

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

_Format_: `ddd:hh24:mi-ddd:hh24:mi`

Type: String

Required: Yes

**shardCapacity**

The number of vCPUs assigned to each elastic cluster shard. Maximum is 64.
Allowed values are 2, 4, 8, 16, 32, 64.

Type: Integer

Required: Yes

**shardCount**

The number of shards assigned to the elastic cluster. Maximum is 32.

Type: Integer

Required: Yes

**status**

The status of the elastic cluster.

Type: String

Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`

Required: Yes

**subnetIds**

The Amazon EC2 subnet IDs for the elastic cluster.

Type: Array of strings

Required: Yes

**vpcSecurityGroupIds**

A list of EC2 VPC security groups associated with thie elastic cluster.

Type: Array of strings

Required: Yes

**backupRetentionPeriod**

The number of days for which automatic snapshots are retained.

Type: Integer

Required: No

**preferredBackupWindow**

The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod`.

Type: String

Required: No

**shardInstanceCount**

The number of replica instances applying to all shards in the cluster.
A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

Type: Integer

Required: No

**shards**

The total number of shards in the cluster.

Type: Array of [Shard](API_elastic_Shard.md "API_elastic_Shard.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/Cluster.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/Cluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/Cluster.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/Cluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/Cluster.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/Cluster.md")
