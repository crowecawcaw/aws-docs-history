

# Data retrieval APIs for AWS X-Ray
<a name="awsx-ray"></a>

AWS X-Ray provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="xray-BatchGetTraceSummaryById"></a>[BatchGetTraceSummaryById](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console) | Retrieve metadata for a list of traces specified by ID | Read | 
| <a name="xray-BatchGetTraces"></a>[BatchGetTraces](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html) | Retrieve a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use GetTraceSummaries to get a list of trace IDs | List | 
| <a name="xray-CancelTraceRetrieval"></a>[CancelTraceRetrieval](API_CancelTraceRetrieval.html) | Cancel an ongoing trace retrieval job initiated by StartTraceRetrieval using the provided RetrievalToken. A successful cancellation will return an HTTP 200 response | Read | 
| <a name="xray-GetDistinctTraceGraphs"></a>[GetDistinctTraceGraphs](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console) | Retrieve distinct service graphs for one or more specific trace IDs | Read | 
| <a name="xray-GetEncryptionConfig"></a>[GetEncryptionConfig](https://docs.aws.amazon.com/xray/latest/api/API_GetEncryptionConfig.html) | Retrieve the current encryption configuration for X-Ray data | Read | 
| <a name="xray-GetGroup"></a>[GetGroup](https://docs.aws.amazon.com/xray/latest/api/API_GetGroup.html) | Retrieve group resource details | Read | 
| <a name="xray-GetGroups"></a>[GetGroups](https://docs.aws.amazon.com/xray/latest/api/API_GetGroups.html) | Retrieve all active group details | Read | 
| <a name="xray-GetIndexingRules"></a>[GetIndexingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetIndexingRules.html) | Retrieve all indexing rules. Indexing rules are used to determine the server-side sampling rate for spans ingested through the CloudWatchLogs destination and indexed by X-Ray | Read | 
| <a name="xray-GetInsight"></a>[GetInsight](https://docs.aws.amazon.com/xray/latest/api/API_GetInsight.html) | Retrieve the details of a specific insight | Read | 
| <a name="xray-GetInsightEvents"></a>[GetInsightEvents](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightEvents.html) | Retrieve the events of a specific insight | Read | 
| <a name="xray-GetInsightImpactGraph"></a>[GetInsightImpactGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightImpactGraph.html) | Retrieve the part of the service graph which is impacted for a specific insight | Read | 
| <a name="xray-GetInsightSummaries"></a>[GetInsightSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightSummaries.html) | Retrieve the summary of all insights for a group and time range with optional filters | Read | 
| <a name="xray-GetRetrievedTracesGraph"></a>[GetRetrievedTracesGraph](API_GetRetrievedTracesGraph.html) | Retrieve a service graph for traces based on the specified RetrievalToken from the Transaction Search CloudWatch log group | Read | 
| <a name="xray-GetSamplingRules"></a>[GetSamplingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html) | Retrieve all sampling rules | Read | 
| <a name="xray-GetSamplingStatisticSummaries"></a>[GetSamplingStatisticSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingStatisticSummaries.html) | Retrieve information about recent sampling results for all sampling rules | Read | 
| <a name="xray-GetSamplingTargets"></a>[GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) | Request a sampling quota for rules that the service is using to sample requests | Read | 
| <a name="xray-GetServiceGraph"></a>[GetServiceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetServiceGraph.html) | Retrieve a document that describes services that process incoming requests, and downstream services that they call as a result | Read | 
| <a name="xray-GetTimeSeriesServiceStatistics"></a>[GetTimeSeriesServiceStatistics](https://docs.aws.amazon.com/xray/latest/api/API_GetTimeSeriesServiceStatistics.html) | Retrieve an aggregation of service statistics defined by a specific time range bucketed into time intervals | Read | 
| <a name="xray-GetTraceGraph"></a>[GetTraceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceGraph.html) | Retrieve a service graph for one or more specific trace IDs | Read | 
| <a name="xray-GetTraceSegmentDestination"></a>[GetTraceSegmentDestination](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSegmentDestination.html) | Retrieve the current destination of data sent to PutTraceSegments and OpenTelemetry API | Read | 
| <a name="xray-GetTraceSummaries"></a>[GetTraceSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html) | Retrieve IDs and metadata for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to BatchGetTraces | Read | 
| <a name="xray-ListResourcePolicies"></a>[ListResourcePolicies](https://docs.aws.amazon.com/xray/latest/api/API_ListResourcePolicies.html) | List resource policies | List | 
| <a name="xray-ListRetrievedTraces"></a>[ListRetrievedTraces](API_ListRetrievedTraces.html) | Retrieve a list of traces for a given RetrievalToken from the Transaction Search CloudWatch log group | List | 
| <a name="xray-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/xray/latest/api/API_ListTagsForResource.html) | List tags for an X-Ray resource | List | 
| <a name="xray-StartTraceRetrieval"></a>[StartTraceRetrieval](API_StartTraceRetrieval) | Initiate a trace retrieval process using the specified time range and for the given trace IDs on the Transaction Search CloudWatch log group | Read | 