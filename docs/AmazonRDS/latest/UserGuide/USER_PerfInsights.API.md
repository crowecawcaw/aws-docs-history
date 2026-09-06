

# Retrieving metrics with the Performance Insights API for Amazon RDS
<a name="USER_PerfInsights.API"></a>

When you enable detailed per-query and database counter metrics, the API provides visibility into instance performance. Amazon CloudWatch Logs provides the authoritative source for vended monitoring metrics for AWS services.

Database Insights offers a domain-specific view of database load measured as average active sessions (AAS). This metric appears to API consumers as a two-dimensional time-series dataset. The time dimension of the data provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, such as `SQL`, `Wait-event`, `User`, or `Host`, measured at that time point.

Amazon CloudWatch Database Insights monitors your Amazon RDS DB instance so that you can analyze and troubleshoot database performance. One way to view Database Insights data is in the AWS Management Console. Performance Insights also provides a public API so that you can query your own data. You can use the API to do the following:
+ Offload data into a database
+ Add Database Insights data to existing monitoring dashboards
+ Build monitoring tools

To use the Performance Insights API, enable detailed per-query and database counter metrics on one of your Amazon RDS DB instances. For information about enabling detailed per-query and database counter metrics, see [Enabling and disabling detailed per-query and database counter metrics](USER_PerfInsights.Enabling.md). For more information about the Performance Insights API, see the [Amazon RDS Performance Insights API Reference](https://docs.aws.amazon.com/performance-insights/latest/APIReference/Welcome.html).

The Performance Insights API provides the following operations.



|  Performance Insights action  |  AWS CLI command  |  Description  | 
| --- | --- | --- | 
| [`CreatePerformanceAnalysisReport`](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_CreatePerformanceAnalysisReport.html) | [`aws pi create-performance-analysis-report`](https://docs.aws.amazon.com/cli/latest/reference/pi/CreatePerformanceAnalysisReport.html) | Creates a performance analysis report for a specific time period for the DB instance. The result is `AnalysisReportId` which is the unique identifier of the report. | 
| [`DeletePerformanceAnalysisReport`](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DeletePerformanceAnalysisReport.html) | [`aws pi delete-performance-analysis-report`](https://docs.aws.amazon.com/cli/latest/reference/pi/DeletePerformanceAnalysisReport.html) | Deletes a performance analysis report. | 
| [`DescribeDimensionKeys`](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DescribeDimensionKeys.html) | [`aws pi describe-dimension-keys`](https://docs.aws.amazon.com/cli/latest/reference/pi/describe-dimension-keys.html) | Retrieves the top N dimension keys for a metric for a specific time period. | 
| [`GetDimensionKeyDetails`](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetDimensionKeyDetails.html) | [`aws pi get-dimension-key-details`](https://docs.aws.amazon.com/cli/latest/reference/pi/get-dimension-key-details.html) | Retrieves the attributes of the specified dimension group for a DB instance or data source. For example, if you specify a SQL ID, and if the dimension details are available, `GetDimensionKeyDetails` retrieves the full text of the dimension `db.sql.statement` associated with this ID. This operation is useful because `GetResourceMetrics` and `DescribeDimensionKeys` don't support retrieval of large SQL statement text.  | 
| [`GetPerformanceAnalysisReport`](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetPerformanceAnalysisReport.html) | [`aws pi get-performance-analysis-report`](https://docs.aws.amazon.com/cli/latest/reference/pi/GetPerformanceAnalysisReport.html) | Retrieves the report including the insights for the report. The result includes the report status, report ID, report time details, insights, and recommendations. | 
| [GetResourceMetadata](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetadata.html) | [`aws pi get-resource-metadata`](https://docs.aws.amazon.com/cli/latest/reference/pi/get-resource-metadata.html) | Retrieve the metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance.  | 
| [`GetResourceMetrics`](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetrics.html) | [`aws pi get-resource-metrics`](https://docs.aws.amazon.com/cli/latest/reference/pi/get-resource-metrics.html) | Retrieves Performance Insights metrics for a set of data sources over a time period. You can provide specific dimension groups and dimensions, and provide aggregation and filtering criteria for each group. | 
| [ListAvailableResourceDimensions](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceDimensions.html) | [`aws pi list-available-resource-dimensions`](https://docs.aws.amazon.com/cli/latest/reference/pi/list-available-resource-dimensions.html) | Retrieve the dimensions that can be queried for each specified metric type on a specified instance.  | 
| [ListAvailableResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceMetrics.html) | [`aws pi list-available-resource-metrics`](https://docs.aws.amazon.com/cli/latest/reference/pi/list-available-resource-metrics.html) | Retrieve all available metrics of the specified metric types that can be queried for a specified DB instance. | 
| `[ListPerformanceAnalysisReports](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListPerformanceAnalysisReports.html)` | [`aws pi list-performance-analysis-reports`](https://docs.aws.amazon.com/cli/latest/reference/pi/list-performance-analysis-reports.html) | Retrieves all the analysis reports available for the DB instance. The reports are listed based on the start time of each report. | 
| `[ListTagsForResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListTagsForResource.html)` | [`aws pi list-tags-for-resource`](https://docs.aws.amazon.com/cli/latest/reference/pi/list-tags-for-resource.html) | Lists all the metadata tags added to the resource. The list includes the name and value of the tag. | 
| `[TagResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_TagResource.html)` | [`aws pi tag-resource`](https://docs.aws.amazon.com/cli/latest/reference/pi/tag-resource.html) | Adds metadata tags to the Amazon RDS resource. The tag includes a name and a value. | 
| `[UntagResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_UntagResource.html)` | [`aws pi untag-resource`](https://docs.aws.amazon.com/cli/latest/reference/pi/untag-resource.html) | Removes the metadata tag from the resource. | 

For more information about retrieving time-series metrics and AWS CLI examples for Performance Insights, see the following topics.

**Topics**
+ [Retrieving time-series metrics for Performance Insights](USER_PerfInsights.API.TimeSeries.md)
+ [AWS CLI examples for Performance Insights](USER_PerfInsights.API.Examples.md)