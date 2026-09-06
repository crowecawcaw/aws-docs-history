

# Actions, resources, and condition keys for AWS Performance Insights
<a name="list_pi"></a>

AWS Performance Insights (service prefix: `pi`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/performance-insights/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pi/pi.json) for this service.

**Topics**
+ [API operations defined by AWS Performance Insights](#list_pi-operations)
+ [Actions defined by AWS Performance Insights](#list_pi-actions-as-permissions)
+ [Resource types defined by AWS Performance Insights](#list_pi-resources-for-iam-policies)
+ [Condition keys for AWS Performance Insights](#list_pi-policy-keys)

## API operations defined by AWS Performance Insights
<a name="list_pi-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pi-actions-as-permissions).




- **   CreatePerformanceAnalysisReport  **
  - **IAM action:**  [pi:CreatePerformanceAnalysisReport](#list_pi-action-CreatePerformanceAnalysisReport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pi:TagResource](#list_pi-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeletePerformanceAnalysisReport  **
  - **IAM action:**  [pi:DeletePerformanceAnalysisReport](#list_pi-action-DeletePerformanceAnalysisReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDimensionKeys  **
  - **IAM action:**  [pi:DescribeDimensionKeys](#list_pi-action-DescribeDimensionKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDimensionKeyDetails  **
  - **IAM action:**  [pi:GetDimensionKeyDetails](#list_pi-action-GetDimensionKeyDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPerformanceAnalysisReport  **
  - **IAM action:**  [pi:GetPerformanceAnalysisReport](#list_pi-action-GetPerformanceAnalysisReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceMetadata  **
  - **IAM action:**  [pi:GetResourceMetadata](#list_pi-action-GetResourceMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceMetrics  **
  - **IAM action:**  [pi:GetResourceMetrics](#list_pi-action-GetResourceMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAvailableResourceDimensions  **
  - **IAM action:**  [pi:DescribeDimensionKeys](#list_pi-action-DescribeDimensionKeys)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [pi:GetDimensionKeyDetails](#list_pi-action-GetDimensionKeyDetails)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [pi:GetResourceMetrics](#list_pi-action-GetResourceMetrics)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [pi:ListAvailableResourceDimensions](#list_pi-action-ListAvailableResourceDimensions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListAvailableResourceMetrics  **
  - **IAM action:**  [pi:ListAvailableResourceMetrics](#list_pi-action-ListAvailableResourceMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPerformanceAnalysisReportRecommendations  **
  - **IAM action:**  [pi:ListPerformanceAnalysisReportRecommendations](#list_pi-action-ListPerformanceAnalysisReportRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPerformanceAnalysisReports  **
  - **IAM action:**  [pi:ListPerformanceAnalysisReports](#list_pi-action-ListPerformanceAnalysisReports)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [pi:ListTagsForResource](#list_pi-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [pi:ListTagsForResource](#list_pi-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [pi:TagResource](#list_pi-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [pi:UntagResource](#list_pi-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Performance Insights
<a name="list_pi-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreatePerformanceAnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_CreatePerformanceAnalysisReport.html)  **
  - **Description:** Grants permission to call CreatePerformanceAnalysisReport API to create a Performance Analysis Report for a specified DB instance
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pi-aws_TagKeys)
  - **Access level:** Write

- **   [DeletePerformanceAnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DeletePerformanceAnalysisReport.html)  **
  - **Description:** Grants permission to call DeletePerformanceAnalysisReport API to delete a Performance Analysis Report for a specified DB instance
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDimensionKeys](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DescribeDimensionKeys.html)  **
  - **Description:** Grants permission to call DescribeDimensionKeys API to retrieve the top N dimension keys for a metric for a specific time period
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)<br />[pi:Dimensions](#list_pi-pi_Dimensions)
  - **Access level:** Read

- **   [GetDimensionKeyDetails](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetDimensionKeyDetails.html)  **
  - **Description:** Grants permission to call GetDimensionKeyDetails API to retrieve the attributes of the specified dimension group
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)<br />[pi:Dimensions](#list_pi-pi_Dimensions)
  - **Access level:** Read

- **   [GetPerformanceAnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetPerformanceAnalysisReport.html)  **
  - **Description:** Grants permission to call GetPerformanceAnalysisReport API to retrieve a Performance Analysis Report for a specified DB instance
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceMetadata](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetadata.html)  **
  - **Description:** Grants permission to call GetResourceMetadata API to retrieve the metadata for different features
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetrics.html)  **
  - **Description:** Grants permission to call GetResourceMetrics API to retrieve PI metrics for a set of data sources, over a time period
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)<br />[pi:Dimensions](#list_pi-pi_Dimensions)
  - **Access level:** Read

- **   [ListAvailableResourceDimensions](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceDimensions.html)  **
  - **Description:** Grants permission to call ListAvailableResourceDimensions API to retrieve the dimensions that can be queried for each specified metric type on a specified DB instance
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAvailableResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceMetrics.html)  **
  - **Description:** Grants permission to call ListAvailableResourceMetrics API to retrieve metrics of the specified types that can be queried for a specified DB instance
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPerformanceAnalysisReportRecommendations](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListPerformanceAnalysisReportRecommendations.html)  **
  - **Description:** Grants permission to call ListPerformanceAnalysisReportRecommendations API to retrieve a Performance Analysis Report Recommendations for a specified DB instance
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPerformanceAnalysisReports](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListPerformanceAnalysisReports.html)  **
  - **Description:** Grants permission to call ListPerformanceAnalysisReports API to list Performance Analysis Reports for a specified DB instance
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to call ListTagsForResource API to list tags for a resource
  - **Resource types (\*required):** [metric-resource\*](#list_pi-resource-metric-resource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to call TagResource API to tag a resource
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pi-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to call UntagResource API to untag a resource
  - **Resource types (\*required):** [perf-reports-resource\*](#list_pi-resource-perf-reports-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pi-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Performance Insights
<a name="list_pi-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [metric-resource](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html)  | arn:${Partition}:pi:${Region}:${Account}:metrics/${ServiceType}/${Identifier} | [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_) | 
|  [perf-reports-resource](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html)  | arn:${Partition}:pi:${Region}:${Account}:perf-reports/${ServiceType}/${Identifier}/${ReportId} | [aws:ResourceTag/${TagKey}](#list_pi-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Performance Insights
<a name="list_pi-policy-keys"></a>

AWS Performance Insights defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [pi:Dimensions](#condition-keys-dimensions)  | Filters access by the requested dimensions | ArrayOfString | 