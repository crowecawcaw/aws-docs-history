# DescribeDBClusterSnapshotAttributes

Returns a list of cluster snapshot attribute names and values for a manual DB
cluster snapshot.

When you share snapshots with other AWS accounts,
`DescribeDBClusterSnapshotAttributes` returns the `restore` attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If `all` is included in the list of values for the `restore` attribute, then the manual cluster snapshot is public and can be copied or restored by all AWS accounts.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterSnapshotIdentifier**

The identifier for the cluster snapshot to describe the attributes for.

Type: String

Required: Yes

## Response Elements

The following element is returned by the service.

**DBClusterSnapshotAttributesResult**

Detailed information about the attributes that are associated with a cluster
snapshot.

Type: [DBClusterSnapshotAttributesResult](API_DBClusterSnapshotAttributesResult.md "API_DBClusterSnapshotAttributesResult.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBClusterSnapshotNotFoundFault**

`DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/cli2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/boto3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterSnapshotAttributes.md")
