# DescribeDBClusters

Returns information about provisioned Amazon DocumentDB clusters. This API
operation supports pagination. For certain management features
such as cluster and instance lifecycle management, Amazon DocumentDB leverages
operational technology that is shared with Amazon RDS and Amazon
Neptune. Use the `filterName=engine,Values=docdb` filter
parameter to return only Amazon DocumentDB clusters.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterIdentifier**

The user-provided cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn't case sensitive.

Constraints:

- If provided, must match an existing `DBClusterIdentifier`.

Type: String

Required: No

**Filters.Filter.N**

A filter that specifies one or more clusters to describe.

Supported filters:

- `db-cluster-id` - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list only includes information about the clusters identified by these ARNs.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

Required: No

**MaxRecords**

The maximum number of records to include in the response. If more records exist than
the specified `MaxRecords` value, a pagination token (marker) is included
in the response so that the remaining results can be retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

Type: Integer

Required: No

## Response Elements

The following elements are returned by the service.

**DBClusters.DBCluster.N**

A list of clusters.

Type: Array of [DBCluster](API_DBCluster.md "API_DBCluster.md") objects

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBClusterNotFoundFault**

`DBClusterIdentifier` doesn't refer to an existing cluster.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/cli2/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/boto3/docdb-2014-10-31/DescribeDBClusters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusters.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusters.md")
