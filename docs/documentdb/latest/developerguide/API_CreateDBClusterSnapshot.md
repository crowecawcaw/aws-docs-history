# CreateDBClusterSnapshot

Creates a snapshot of a cluster.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterIdentifier**

The identifier of the cluster to create a snapshot for. This
parameter is not case sensitive.

Constraints:

- Must match the identifier of an existing
  `DBCluster`.

Example: `my-cluster`

Type: String

Required: Yes

**DBClusterSnapshotIdentifier**

The identifier of the cluster snapshot. This parameter is stored
as a lowercase string.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster-snapshot1`

Type: String

Required: Yes

**Tags.Tag.N**

The tags to be assigned to the cluster snapshot.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

## Response Elements

The following element is returned by the service.

**DBClusterSnapshot**

Detailed information about a cluster snapshot.

Type: [DBClusterSnapshot](API_DBClusterSnapshot.md "API_DBClusterSnapshot.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBClusterNotFoundFault**

`DBClusterIdentifier` doesn't refer to an existing cluster.

HTTP Status Code: 404

**DBClusterSnapshotAlreadyExistsFault**

You already have a cluster snapshot with the given identifier.

HTTP Status Code: 400

**InvalidDBClusterSnapshotStateFault**

The provided value isn't a valid cluster snapshot state.

HTTP Status Code: 400

**InvalidDBClusterStateFault**

The cluster isn't in a valid state.

HTTP Status Code: 400

**SnapshotQuotaExceeded**

The request would cause you to exceed the allowed number of snapshots.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/cli2/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForCpp/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForGoV2/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForKotlin/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/boto3/docdb-2014-10-31/CreateDBClusterSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateDBClusterSnapshot.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/CreateDBClusterSnapshot.md")
