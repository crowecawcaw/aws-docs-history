# DBClusterRole

Describes an AWS Identity and Access Management (IAM) role that is associated with a
cluster.

## Contents

###### Note

In the following list, the required parameters are described first.

**RoleArn**

The Amazon Resource Name (ARN) of the IAMrole that is associated with the DB
cluster.

Type: String

Required: No

**Status**

Describes the state of association between the IAMrole and the cluster. The `Status` property returns one of the following values:

- `ACTIVE` - The IAMrole ARN is associated with the cluster and can be used to access other AWS services on your behalf.
- `PENDING` - The IAMrole ARN is being associated with the cluster.
- `INVALID` - The IAMrole ARN is associated with the cluster, but the cluster cannot assume the IAMrole to access other AWS services on your behalf.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DBClusterRole.md "../../../goto/SdkForCpp/docdb-2014-10-31/DBClusterRole.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DBClusterRole.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DBClusterRole.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DBClusterRole.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DBClusterRole.md")
