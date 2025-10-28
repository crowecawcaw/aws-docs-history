# ClusterInList

A list of Amazon DocumentDB elastic clusters.

## Contents

###### Note

In the following list, the required parameters are described first.

**clusterArn**

The ARN identifier of the elastic cluster.

Type: String

Required: Yes

**clusterName**

The name of the elastic cluster.

Type: String

Required: Yes

**status**

The status of the elastic cluster.

Type: String

Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterInList.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterInList.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterInList.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterInList.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterInList.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterInList.md")
