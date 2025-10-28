For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QueryComputeRequest

A request to retrieve or update the compute capacity settings for querying data. QueryCompute is available only in the Asia Pacific (Mumbai) region.

## Contents

**ComputeMode**

The mode in which Timestream Compute Units (TCUs) are allocated and utilized within an account. Note that in the Asia Pacific (Mumbai) region, the API operation only recognizes the value `PROVISIONED`. QueryCompute is available only in the Asia Pacific (Mumbai) region.

Type: String

Valid Values: `ON_DEMAND | PROVISIONED`

Required: No

**ProvisionedCapacity**

Configuration object that contains settings for provisioned Timestream Compute Units (TCUs) in your account. QueryCompute is available only in the Asia Pacific (Mumbai) region.

Type: [ProvisionedCapacityRequest](API_query_ProvisionedCapacityRequest.md "API_query_ProvisionedCapacityRequest.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryComputeRequest.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryComputeRequest.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryComputeRequest.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryComputeRequest.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryComputeRequest.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryComputeRequest.md")
