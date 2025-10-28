# DescribePendingMaintenanceActions

Returns a list of resources (for example, instances) that have at least one pending
maintenance action.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**Filters.Filter.N**

A filter that specifies one or more resources to return pending maintenance actions
for.

Supported filters:

- `db-cluster-id` - Accepts cluster identifiers and cluster
  Amazon Resource Names (ARNs). The results list includes only pending maintenance
  actions for the clusters identified by these ARNs.
- `db-instance-id` - Accepts instance identifiers and instance
  ARNs. The results list includes only pending maintenance actions for the DB
  instances identified by these ARNs.

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

**ResourceIdentifier**

The ARN of a resource to return pending maintenance actions for.

Type: String

Required: No

## Response Elements

The following elements are returned by the service.

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

**PendingMaintenanceActions.ResourcePendingMaintenanceActions.N**

The maintenance actions to be applied.

Type: Array of [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md "API_ResourcePendingMaintenanceActions.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundFault**

The specified resource ID was not found.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/cli2/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/boto3/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribePendingMaintenanceActions.md")
