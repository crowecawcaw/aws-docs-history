# DescribeEvents

Returns events related to instances, security groups, snapshots, and DB parameter groups for the past 14 days. You can obtain events specific to a particular DB instance, security group, snapshot, or parameter group by providing the name as a parameter. By default, the events of the past hour are returned.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**Duration**

The number of minutes to retrieve events for.

Default: 60

Type: Integer

Required: No

**EndTime**

The end of the time interval for which to retrieve events, specified in ISO 8601
format.

Example: 2009-07-08T18:00Z

Type: Timestamp

Required: No

**EventCategories.EventCategory.N**

A list of event categories that trigger notifications for an event notification
subscription.

Type: Array of strings

Required: No

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

**SourceIdentifier**

The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.

Constraints:

- If `SourceIdentifier` is provided, `SourceType` must also be provided.
- If the source type is `DBInstance`, a
  `DBInstanceIdentifier` must be provided.
- If the source type is `DBSecurityGroup`, a
  `DBSecurityGroupName` must be provided.
- If the source type is `DBParameterGroup`, a
  `DBParameterGroupName` must be provided.
- If the source type is `DBSnapshot`, a
  `DBSnapshotIdentifier` must be provided.
- Cannot end with a hyphen or contain two consecutive hyphens.

Type: String

Required: No

**SourceType**

The event source to retrieve events for. If no value is specified, all events are returned.

Type: String

Valid Values: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot`

Required: No

**StartTime**

The beginning of the time interval to retrieve events for, specified in ISO 8601 format.

Example: 2009-07-08T18:00Z

Type: Timestamp

Required: No

## Response Elements

The following elements are returned by the service.

**Events.Event.N**

Detailed information about one or more events.

Type: Array of [Event](API_Event.md "API_Event.md") objects

**Marker**

An optional pagination token provided by a previous request. If this parameter is specified, the response
includes only records beyond the marker, up to the value specified by
`MaxRecords`.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeEvents.md "../../../goto/cli2/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeEvents.md "../../../goto/DotNetSDKV4/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeEvents.md "../../../goto/boto3/docdb-2014-10-31/DescribeEvents.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeEvents.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeEvents.md")
