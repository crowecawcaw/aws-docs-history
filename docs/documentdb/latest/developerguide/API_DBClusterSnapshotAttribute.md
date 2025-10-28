# DBClusterSnapshotAttribute

Contains the name and values of a manual cluster snapshot attribute.

Manual cluster snapshot attributes are used to authorize other AWS accounts to restore a manual cluster snapshot.

## Contents

###### Note

In the following list, the required parameters are described first.

**AttributeName**

The name of the manual cluster snapshot attribute.

The attribute named `restore` refers to the list of AWS accounts that have permission to copy or restore the manual cluster snapshot.

Type: String

Required: No

**AttributeValues.AttributeValue.N**

The values for the manual cluster snapshot attribute.

If the `AttributeName` field is set to `restore`, then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If a value of `all` is in the list, then the manual cluster snapshot is public and available for any AWS account to copy or restore.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DBClusterSnapshotAttribute.md "../../../goto/SdkForCpp/docdb-2014-10-31/DBClusterSnapshotAttribute.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DBClusterSnapshotAttribute.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DBClusterSnapshotAttribute.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DBClusterSnapshotAttribute.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DBClusterSnapshotAttribute.md")
