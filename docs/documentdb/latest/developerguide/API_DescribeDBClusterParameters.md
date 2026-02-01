# DescribeDBClusterParameters

Returns the detailed parameter list for a particular cluster parameter
group.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DBClusterParameterGroupName**

The name of a specific cluster parameter group to return parameter details for.

Constraints:

- If provided, must match the name of an existing `DBClusterParameterGroup`.

Type: String

Required: Yes

**Filters.Filter.N**

This parameter is not currently supported.

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

**Source**

A value that indicates to return only parameters for a specific source. Parameter sources can be `engine`, `service`, or `customer`.

Type: String

Required: No

## Response Elements

The following elements are returned by the service.

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

**Parameters.Parameter.N**

Provides a list of parameters for the cluster parameter group.

Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**DBParameterGroupNotFound**

`DBParameterGroupName` doesn't refer to an existing parameter group.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/cli2/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/boto3/docdb-2014-10-31/DescribeDBClusterParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterParameters.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeDBClusterParameters.md")
