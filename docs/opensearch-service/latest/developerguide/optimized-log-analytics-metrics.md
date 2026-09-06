

# CloudWatch metrics
<a name="optimized-log-analytics-metrics"></a>

Amazon OpenSearch Service publishes the following CloudWatch metrics for domains running the Optimized engine. These metrics help you monitor native analytics engine performance, resource utilization, and ingestion health. For the full list of Amazon OpenSearch Service metrics, see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](managedomains-cloudwatchmetrics.md).


| Metric | Node type | Description | 
| --- | --- | --- | 
| NativeMemoryPressure | Hot, Warm, Coordinator | The percentage of native (off-heap) memory in use on the node. This metric is analogous to `JVMMemoryPressure` but measures memory consumed by the native analytics engine rather than the Java heap.<br />Relevant statistics: Maximum | 
| NativeRuntimeResidentMemory | Hot, Warm, Coordinator | The amount of resident memory, in bytes, consumed by the native analytics engine on the node.<br />Relevant statistics: Maximum, Average | 
| NativeSearchRuntimeCPUUtilization | Hot, Warm, Coordinator | The CPU utilization, as a percentage, of the DataFusion query execution engine on the node.<br />Relevant statistics: Maximum, Average | 
| ThreadpoolNativeSearchCPUQueue | Hot, Warm, Coordinator | The number of queued tasks in the native search CPU thread pool. If the queue size is consistently high, consider scaling your cluster.<br />Relevant statistics: Maximum | 
| ThreadpoolNativeSearchCPUThreads | Hot, Warm, Coordinator | The size of the native search CPU thread pool.<br />Relevant statistics: Maximum | 

**Note**  
The following metrics don't apply to Optimized domains because OpenSearch Dashboards is not available:  
`OpenSearchDashboardsHealthyNodes`
`OpensearchDashboardsReportingFailedRequestSysErrCount`
`OpensearchDashboardsReportingFailedRequestUserErrCount`
`OpensearchDashboardsReportingRequestCount`
`OpensearchDashboardsReportingSuccessCount`