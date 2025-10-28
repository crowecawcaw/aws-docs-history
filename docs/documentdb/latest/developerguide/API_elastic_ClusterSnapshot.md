# ClusterSnapshot

Returns information about a specific elastic cluster snapshot.

## Contents

###### Note

In the following list, the required parameters are described first.

**adminUserName**

The name of the elastic cluster administrator.

Type: String

Required: Yes

**clusterArn**

The ARN identifier of the elastic cluster.

Type: String

Required: Yes

**clusterCreationTime**

The time when the elastic cluster was created in Universal Coordinated Time (UTC).

Type: String

Required: Yes

**kmsKeyId**

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key.
If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.
If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account.
Your account has a different default encryption key for each Amazon Region.

Type: String

Required: Yes

**snapshotArn**

The ARN identifier of the elastic cluster snapshot.

Type: String

Required: Yes

**snapshotCreationTime**

The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).

Type: String

Required: Yes

**snapshotName**

The name of the elastic cluster snapshot.

Type: String

Required: Yes

**status**

The status of the elastic cluster snapshot.

Type: String

Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`

Required: Yes

**subnetIds**

The Amazon EC2 subnet IDs for the elastic cluster.

Type: Array of strings

Required: Yes

**vpcSecurityGroupIds**

A list of EC2 VPC security groups to associate with the elastic cluster.

Type: Array of strings

Required: Yes

**snapshotType**

The type of cluster snapshots to be returned.
You can specify one of the following values:

- `automated` - Return all cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.
- `manual` - Return all cluster snapshots that you have manually created for your AWS account.

Type: String

Valid Values: `MANUAL | AUTOMATED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterSnapshot.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterSnapshot.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterSnapshot.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterSnapshot.md")
