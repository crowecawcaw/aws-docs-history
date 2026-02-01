# DescribeOrderableDBInstanceOptions

Returns a list of orderable instance options for the specified engine.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**Engine**

The name of the engine to retrieve instance options for.

Type: String

Required: Yes

**DBInstanceClass**

The instance class filter value. Specify this parameter to show only the available
offerings that match the specified instance class.

Type: String

Required: No

**EngineVersion**

The engine version filter value. Specify this parameter to show only the available
offerings that match the specified engine version.

Type: String

Required: No

**Filters.Filter.N**

This parameter is not currently supported.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**LicenseModel**

The license model filter value. Specify this parameter to show only the available
offerings that match the specified license model.

Type: String

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

**Vpc**

The virtual private cloud (VPC) filter value. Specify this parameter to show only the
available VPC or non-VPC offerings.

Type: Boolean

Required: No

## Response Elements

The following elements are returned by the service.

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

**OrderableDBInstanceOptions.OrderableDBInstanceOption.N**

The options that are available for a particular orderable instance.

Type: Array of [OrderableDBInstanceOption](API_OrderableDBInstanceOption.md "API_OrderableDBInstanceOption.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/cli2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/boto3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeOrderableDBInstanceOptions.md")
