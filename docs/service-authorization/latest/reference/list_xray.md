

# Actions, resources, and condition keys for AWS X-Ray
<a name="list_xray"></a>

AWS X-Ray (service prefix: `xray`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/xray/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/xray/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/xray/xray.json) for this service.

**Topics**
+ [API operations defined by AWS X-Ray](#list_xray-operations)
+ [Actions defined by AWS X-Ray](#list_xray-actions-as-permissions)
+ [Permission-only actions for AWS X-Ray](#list_xray-permission-only-actions)
+ [Resource types defined by AWS X-Ray](#list_xray-resources-for-iam-policies)
+ [Condition keys for AWS X-Ray](#list_xray-policy-keys)

## API operations defined by AWS X-Ray
<a name="list_xray-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_xray-actions-as-permissions).




- **   BatchGetTraces  **
  - **IAM action:**  [xray:BatchGetTraces](#list_xray-action-BatchGetTraces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   CancelTraceRetrieval  **
  - **IAM action:**  [xray:CancelTraceRetrieval](#list_xray-action-CancelTraceRetrieval) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateGroup  **
  - **IAM action:**  [xray:CreateGroup](#list_xray-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [xray:TagResource](#list_xray-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSamplingRule  **
  - **IAM action:**  [xray:CreateSamplingRule](#list_xray-action-CreateSamplingRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [xray:TagResource](#list_xray-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteGroup  **
  - **IAM action:**  [xray:DeleteGroup](#list_xray-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [xray:DeleteResourcePolicy](#list_xray-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSamplingRule  **
  - **IAM action:**  [xray:DeleteSamplingRule](#list_xray-action-DeleteSamplingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetEncryptionConfig  **
  - **IAM action:**  [xray:GetEncryptionConfig](#list_xray-action-GetEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **IAM action:**  [xray:GetGroup](#list_xray-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroups  **
  - **IAM action:**  [xray:GetGroups](#list_xray-action-GetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIndexingRules  **
  - **IAM action:**  [xray:GetIndexingRules](#list_xray-action-GetIndexingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsight  **
  - **IAM action:**  [xray:GetInsight](#list_xray-action-GetInsight) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightEvents  **
  - **IAM action:**  [xray:GetInsightEvents](#list_xray-action-GetInsightEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightImpactGraph  **
  - **IAM action:**  [xray:GetInsightImpactGraph](#list_xray-action-GetInsightImpactGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightSummaries  **
  - **IAM action:**  [xray:GetInsightSummaries](#list_xray-action-GetInsightSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRetrievedTracesGraph  **
  - **IAM action:**  [xray:GetRetrievedTracesGraph](#list_xray-action-GetRetrievedTracesGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSamplingRules  **
  - **IAM action:**  [xray:GetSamplingRules](#list_xray-action-GetSamplingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSamplingStatisticSummaries  **
  - **IAM action:**  [xray:GetSamplingStatisticSummaries](#list_xray-action-GetSamplingStatisticSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSamplingTargets  **
  - **IAM action:**  [xray:GetSamplingTargets](#list_xray-action-GetSamplingTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceGraph  **
  - **IAM action:**  [xray:GetServiceGraph](#list_xray-action-GetServiceGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTimeSeriesServiceStatistics  **
  - **IAM action:**  [xray:GetTimeSeriesServiceStatistics](#list_xray-action-GetTimeSeriesServiceStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTraceGraph  **
  - **IAM action:**  [xray:GetTraceGraph](#list_xray-action-GetTraceGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTraceSegmentDestination  **
  - **IAM action:**  [xray:GetTraceSegmentDestination](#list_xray-action-GetTraceSegmentDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTraceSummaries  **
  - **IAM action:**  [xray:GetTraceSummaries](#list_xray-action-GetTraceSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResourcePolicies  **
  - **IAM action:**  [xray:ListResourcePolicies](#list_xray-action-ListResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRetrievedTraces  **
  - **IAM action:**  [xray:ListRetrievedTraces](#list_xray-action-ListRetrievedTraces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [xray:ListTagsForResource](#list_xray-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutEncryptionConfig  **
  - **IAM action:**  [xray:PutEncryptionConfig](#list_xray-action-PutEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutResourcePolicy  **
  - **IAM action:**  [xray:PutResourcePolicy](#list_xray-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTelemetryRecords  **
  - **IAM action:**  [xray:PutTelemetryRecords](#list_xray-action-PutTelemetryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTraceSegments  **
  - **IAM action:**  [xray:PutTraceSegments](#list_xray-action-PutTraceSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTraceRetrieval  **
  - **IAM action:**  [xray:StartTraceRetrieval](#list_xray-action-StartTraceRetrieval) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [xray:TagResource](#list_xray-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [xray:UntagResource](#list_xray-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateGroup  **
  - **IAM action:**  [xray:UpdateGroup](#list_xray-action-UpdateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIndexingRule  **
  - **IAM action:**  [xray:UpdateIndexingRule](#list_xray-action-UpdateIndexingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSamplingRule  **
  - **IAM action:**  [xray:UpdateSamplingRule](#list_xray-action-UpdateSamplingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTraceSegmentDestination  **
  - **IAM action:**  [xray:UpdateTraceSegmentDestination](#list_xray-action-UpdateTraceSegmentDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS X-Ray
<a name="list_xray-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetTraces](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html)  **
  - **Description:** Grants permission to retrieve a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use GetTraceSummaries to get a list of trace IDs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [CancelTraceRetrieval](API_CancelTraceRetrieval.html)  **
  - **Description:** Grants permission to cancel an ongoing trace retrieval job initiated by StartTraceRetrieval using the provided RetrievalToken. A successful cancellation will return an HTTP 200 response
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateGroup](https://docs.aws.amazon.com/xray/latest/api/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a group resource with a name and a filter expression
  - **Resource types (\*required):** [group\*](#list_xray-resource-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_xray-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_xray-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSamplingRule](https://docs.aws.amazon.com/xray/latest/api/API_CreateSamplingRule.html)  **
  - **Description:** Grants permission to create a rule to control sampling behavior for instrumented applications
  - **Resource types (\*required):** [sampling-rule\*](#list_xray-resource-sampling-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_xray-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_xray-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/xray/latest/api/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete a group resource
  - **Resource types (\*required):** [group\*](#list_xray-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/xray/latest/api/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete resource policies
  - **Resource types (\*required):** 
  - **Condition keys:** [xray:ResourcePolicyName](#list_xray-xray_ResourcePolicyName)
  - **Access level:** Write

- **   [DeleteSamplingRule](https://docs.aws.amazon.com/xray/latest/api/API_DeleteSamplingRule.html)  **
  - **Description:** Grants permission to delete a sampling rule
  - **Resource types (\*required):** [sampling-rule\*](#list_xray-resource-sampling-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEncryptionConfig](https://docs.aws.amazon.com/xray/latest/api/API_GetEncryptionConfig.html)  **
  - **Description:** Grants permission to retrieve the current encryption configuration for X-Ray data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/xray/latest/api/API_GetGroup.html)  **
  - **Description:** Grants permission to retrieve group resource details
  - **Resource types (\*required):** [group\*](#list_xray-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroups](https://docs.aws.amazon.com/xray/latest/api/API_GetGroups.html)  **
  - **Description:** Grants permission to retrieve all active group details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIndexingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetIndexingRules.html)  **
  - **Description:** Grants permission to retrieve all indexing rules. Indexing rules are used to determine the server-side sampling rate for spans ingested through the CloudWatchLogs destination and indexed by X-Ray
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsight](https://docs.aws.amazon.com/xray/latest/api/API_GetInsight.html)  **
  - **Description:** Grants permission to retrieve the details of a specific insight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsightEvents](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightEvents.html)  **
  - **Description:** Grants permission to retrieve the events of a specific insight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsightImpactGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightImpactGraph.html)  **
  - **Description:** Grants permission to retrieve the part of the service graph which is impacted for a specific insight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsightSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetInsightSummaries.html)  **
  - **Description:** Grants permission to retrieve the summary of all insights for a group and time range with optional filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRetrievedTracesGraph](API_GetRetrievedTracesGraph.html)  **
  - **Description:** Grants permission to retrieve a service graph for traces based on the specified RetrievalToken from the Transaction Search CloudWatch log group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSamplingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html)  **
  - **Description:** Grants permission to retrieve all sampling rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSamplingStatisticSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingStatisticSummaries.html)  **
  - **Description:** Grants permission to retrieve information about recent sampling results for all sampling rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html)  **
  - **Description:** Grants permission to request a sampling quota for rules that the service is using to sample requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetServiceGraph.html)  **
  - **Description:** Grants permission to retrieve a document that describes services that process incoming requests, and downstream services that they call as a result
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTimeSeriesServiceStatistics](https://docs.aws.amazon.com/xray/latest/api/API_GetTimeSeriesServiceStatistics.html)  **
  - **Description:** Grants permission to retrieve an aggregation of service statistics defined by a specific time range bucketed into time intervals
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTraceGraph](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceGraph.html)  **
  - **Description:** Grants permission to retrieve a service graph for one or more specific trace IDs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTraceSegmentDestination](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSegmentDestination.html)  **
  - **Description:** Grants permission to retrieve the current destination of data sent to PutTraceSegments and OpenTelemetry API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTraceSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html)  **
  - **Description:** Grants permission to retrieve IDs and metadata for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to BatchGetTraces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListResourcePolicies](https://docs.aws.amazon.com/xray/latest/api/API_ListResourcePolicies.html)  **
  - **Description:** Grants permission to list resource policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRetrievedTraces](API_ListRetrievedTraces.html)  **
  - **Description:** Grants permission to retrieve a list of traces for a given RetrievalToken from the Transaction Search CloudWatch log group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/xray/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an X-Ray resource
  - **Resource types (\*required):** [group](#list_xray-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sampling-rule](#list_xray-resource-sampling-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutEncryptionConfig](https://docs.aws.amazon.com/xray/latest/api/API_PutEncryptionConfig.html)  **
  - **Description:** Grants permission to update the encryption configuration for X-Ray data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/xray/latest/api/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update resource policies
  - **Resource types (\*required):** 
  - **Condition keys:** [xray:ResourcePolicyName](#list_xray-xray_ResourcePolicyName)
  - **Access level:** Write

- **   [PutSpans](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html)  **
  - **Description:** Grants permission to upload OpenTelemetry spans to AWS X-Ray
  - **Resource types (\*required):** 
  - **Condition keys:** [logs:LogGeneratingResourceArns](#list_xray-logs_LogGeneratingResourceArns)
  - **Access level:** Write

- **   [PutTelemetryRecords](https://docs.aws.amazon.com/xray/latest/api/API_PutTelemetryRecords.html)  **
  - **Description:** Grants permission to send AWS X-Ray daemon telemetry to the service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html)  **
  - **Description:** Grants permission to upload segment documents to AWS X-Ray. The X-Ray SDK generates segment documents and sends them to the X-Ray daemon, which uploads them in batches
  - **Resource types (\*required):** 
  - **Condition keys:** [logs:LogGeneratingResourceArns](#list_xray-logs_LogGeneratingResourceArns)
  - **Access level:** Write

- **   [StartTraceRetrieval](API_StartTraceRetrieval)  **
  - **Description:** Grants permission to initiate a trace retrieval process using the specified time range and for the given trace IDs on the Transaction Search CloudWatch log group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/xray/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to an X-Ray resource
  - **Resource types (\*required):** [group](#list_xray-resource-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_xray-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_xray-aws_TagKeys)
  - **Resource types (\*required):** [sampling-rule](#list_xray-resource-sampling-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_xray-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_xray-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/xray/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an X-Ray resource
  - **Resource types (\*required):** [group](#list_xray-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_xray-aws_TagKeys)
  - **Resource types (\*required):** [sampling-rule](#list_xray-resource-sampling-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_xray-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateGroup](https://docs.aws.amazon.com/xray/latest/api/API_UpdateGroup.html)  **
  - **Description:** Grants permission to update a group resource
  - **Resource types (\*required):** [group\*](#list_xray-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIndexingRule](https://docs.aws.amazon.com/xray/latest/api/API_UpdateIndexingRule.html)  **
  - **Description:** Grants permission to modify an indexing rule's configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSamplingRule](https://docs.aws.amazon.com/xray/latest/api/API_UpdateSamplingRule.html)  **
  - **Description:** Grants permission to modify a sampling rule's configuration
  - **Resource types (\*required):** [sampling-rule\*](#list_xray-resource-sampling-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTraceSegmentDestination](https://docs.aws.amazon.com/xray/latest/api/API_UpdateTraceSegmentDestination.html)  **
  - **Description:** Grants permission to modify the destination of data sent to PutTraceSegments and OpenTelemetry API
  - **Resource types (\*required):** 
  - **Condition keys:** [xray:TraceSegmentDestination](#list_xray-xray_TraceSegmentDestination)
  - **Access level:** Write



## Permission-only actions for AWS X-Ray
<a name="list_xray-permission-only-actions"></a>

The following actions are defined by AWS X-Ray but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [BatchGetTraceSummaryById](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console)  | Grants permission to retrieve metadata for a list of traces specified by ID |  |   | Read | 
|   [GetDistinctTraceGraphs](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console)  | Grants permission to retrieve distinct service graphs for one or more specific trace IDs |  |   | Read | 
|   [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html#CloudWatch-Unified-Cross-Account-Setup-permissions)  | Grants permission to share X-Ray resources with a monitoring account |  |   | Write | 
|   [PutSpansForIndexing](https://docs.aws.amazon.com/xray/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console)  | Grants permission to upload spans to AWS X-Ray to be indexed |  |   | Write | 

## Resource types defined by AWS X-Ray
<a name="list_xray-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [group](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-groups)  | arn:${Partition}:xray:${Region}:${Account}:group/${GroupName}/${Id} | [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_) | 
|  [sampling-rule](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-sampling)  | arn:${Partition}:xray:${Region}:${Account}:sampling-rule/${SamplingRuleName} | [aws:ResourceTag/${TagKey}](#list_xray-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS X-Ray
<a name="list_xray-policy-keys"></a>

AWS X-Ray defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [logs:LogGeneratingResourceArns](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsx-ray.html#awsx-ray-actions-as-permissions)  | Filters access by LogGeneratingResourceArn in the request | ArrayOfARN | 
|   [xray:ResourcePolicyName](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsx-ray.html#awsx-ray-actions-as-permissions)  | Filters access by PolicyName in the request | String | 
|   [xray:TraceSegmentDestination](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsx-ray.html#awsx-ray-actions-as-permissions)  | Filters access by TraceSegmentDestination type in the request | String | 