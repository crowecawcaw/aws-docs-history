# DeleteDBClusterSnapshot

Deletes a cluster snapshot. If the snapshot is being copied, the copy operation is terminated.

###### Note

The cluster snapshot must be in the `available` state to be deleted.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterSnapshotIdentifier**

The identifier of the cluster snapshot to delete.

Constraints: Must be the name of an existing cluster snapshot in the `available` state.

Type: String

Required: Yes

## Response Elements

The following element is returned by the service.

**DBClusterSnapshot**

Detailed information about a cluster snapshot.

Type: [DBClusterSnapshot](API_DBClusterSnapshot.md "API_DBClusterSnapshot.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBClusterSnapshotNotFoundFault**

`DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.

HTTP Status Code: 404

**InvalidDBClusterSnapshotStateFault**

The provided value isn't a valid cluster snapshot state.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/cli2/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForCpp/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/boto3/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBClusterSnapshot.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBClusterSnapshot.md")
