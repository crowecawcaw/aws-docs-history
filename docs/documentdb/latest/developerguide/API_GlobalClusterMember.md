# GlobalClusterMember

A data structure with information about any primary and secondary clusters associated with an Amazon DocumentDB global clusters.

## Contents

###### Note

In the following list, the required parameters are described first.

**DBClusterArn**

The Amazon Resource Name (ARN) for each Amazon DocumentDB cluster.

Type: String

Required: No

**IsWriter**

Specifies whether the Amazon DocumentDB cluster is the primary cluster (that is, has read-write capability) for the Amazon DocumentDB global cluster with which it is associated.

Type: Boolean

Required: No

**Readers.member.N**

The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Amazon DocumentDB global cluster.

Type: Array of strings

Required: No

**SynchronizationStatus**

The status of synchronization of each Amazon DocumentDB cluster in the global cluster.

Type: String

Valid Values: `connected | pending-resync`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/GlobalClusterMember.md "../../../goto/SdkForCpp/docdb-2014-10-31/GlobalClusterMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/GlobalClusterMember.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/GlobalClusterMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/GlobalClusterMember.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/GlobalClusterMember.md")
