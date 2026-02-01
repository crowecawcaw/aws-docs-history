# DeleteDBCluster

Deletes a previously provisioned cluster. When you delete a cluster, all automated backups for that cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified cluster are not deleted.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterIdentifier**

The cluster identifier for the cluster to be deleted. This parameter isn't case sensitive.

Constraints:

- Must match an existing `DBClusterIdentifier`.

Type: String

Required: Yes

**FinalDBSnapshotIdentifier**

The cluster snapshot identifier of the new cluster snapshot created when `SkipFinalSnapshot` is set to `false`.

###### Note

Specifying this parameter and also setting the `SkipFinalShapshot` parameter to `true` results in an error.

Constraints:

- Must be from 1 to 255 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Type: String

Required: No

**SkipFinalSnapshot**

Determines whether a final cluster snapshot is created before the cluster is deleted. If `true` is specified, no cluster snapshot is created. If `false` is specified, a cluster snapshot is created before the DB cluster is deleted.

###### Note

If `SkipFinalSnapshot` is `false`, you must specify a `FinalDBSnapshotIdentifier` parameter.

Default: `false`

Type: Boolean

Required: No

## Response Elements

The following element is returned by the service.

**DBCluster**

Detailed information about a cluster.

Type: [DBCluster](API_DBCluster.md "API_DBCluster.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/cli2/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/boto3/docdb-2014-10-31/DeleteDBCluster.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBCluster.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBCluster.md")
