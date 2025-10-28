# DBClusterMember

Contains information about an instance that is part of a cluster.

## Contents

###### Note

In the following list, the required parameters are described first.

**DBClusterParameterGroupStatus**

Specifies the status of the cluster parameter group for this member of the DB
cluster.

Type: String

Required: No

**DBInstanceIdentifier**

Specifies the instance identifier for this member of the cluster.

Type: String

Required: No

**IsClusterWriter**

A value that is `true` if the cluster member is the primary instance for
the cluster and `false` otherwise.

Type: Boolean

Required: No

**PromotionTier**

A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
primary instance after a failure of the existing primary instance.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DBClusterMember.md "../../../goto/SdkForCpp/docdb-2014-10-31/DBClusterMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DBClusterMember.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DBClusterMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DBClusterMember.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DBClusterMember.md")
