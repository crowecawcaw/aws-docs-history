

# Actions, resources, and condition keys for Amazon Lookout for Metrics
<a name="list_lookoutmetrics"></a>

Amazon Lookout for Metrics (service prefix: `lookoutmetrics`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lookoutmetrics/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lookoutmetrics/lookoutmetrics.json) for this service.

**Topics**
+ [Actions defined by Amazon Lookout for Metrics](#list_lookoutmetrics-actions-as-permissions)
+ [Resource types defined by Amazon Lookout for Metrics](#list_lookoutmetrics-resources-for-iam-policies)
+ [Condition keys for Amazon Lookout for Metrics](#list_lookoutmetrics-policy-keys)

## Actions defined by Amazon Lookout for Metrics
<a name="list_lookoutmetrics-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ActivateAnomalyDetector.html)  **
  - **Description:** Grants permission to activate an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BackTestAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_BackTestAnomalyDetector.html)  **
  - **Description:** Grants permission to run a backtest with an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAlert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_CreateAlert.html)  **
  - **Description:** Grants permission to create an alert for an anomaly detector
  - **Resource types (\*required):** [Alert\*](#list_lookoutmetrics-resource-Alert) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_CreateAnomalyDetector.html)  **
  - **Description:** Grants permission to create an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMetricSet](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_CreateMetricSet.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Resource types (\*required):** [MetricSet\*](#list_lookoutmetrics-resource-MetricSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Access level:** Write

- **   [DeactivateAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DeactivateAnomalyDetector.html)  **
  - **Description:** Grants permission to deactivate an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAlert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DeleteAlert.html)  **
  - **Description:** Grants permission to delete an alert
  - **Resource types (\*required):** [Alert\*](#list_lookoutmetrics-resource-Alert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DeleteAnomalyDetector.html)  **
  - **Description:** Grants permission to delete an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAlert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DescribeAlert.html)  **
  - **Description:** Grants permission to get details about an alert
  - **Resource types (\*required):** [Alert\*](#list_lookoutmetrics-resource-Alert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAnomalyDetectionExecutions](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DescribeAnomalyDetectionExecutions.html)  **
  - **Description:** Grants permission to get information about an anomaly detection job
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DescribeAnomalyDetector.html)  **
  - **Description:** Grants permission to get details about an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMetricSet](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DescribeMetricSet.html)  **
  - **Description:** Grants permission to get details about a dataset
  - **Resource types (\*required):** [MetricSet\*](#list_lookoutmetrics-resource-MetricSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectMetricSetConfig](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_DetectMetricSetConfig.html)  **
  - **Description:** Grants permission to detect metric set config from data source
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnomalyGroup](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_GetAnomalyGroup.html)  **
  - **Description:** Grants permission to get details about a group of affected metrics
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataQualityMetrics](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_GetDataQualityMetrics.html)  **
  - **Description:** Grants permission to get data quality metrics for an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFeedback](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_GetFeedback.html)  **
  - **Description:** Grants permission to get feedback on affected metrics for an anomaly group
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSampleData](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_GetSampleData.html)  **
  - **Description:** Grants permission to get a selection of sample records from an Amazon S3 datasource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAlerts](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAlerts.html)  **
  - **Description:** Grants permission to get a list of alerts for a detector
  - **Resource types (\*required):** [AnomalyDetector](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAnomalyDetectors](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAnomalyDetectors.html)  **
  - **Description:** Grants permission to get a list of anomaly detectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAnomalyGroupRelatedMetrics](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAnomalyGroupRelatedMetrics.html)  **
  - **Description:** Grants permission to get a list of related measures in an anomaly group
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAnomalyGroupSummaries](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAnomalyGroupSummaries.html)  **
  - **Description:** Grants permission to get a list of anomaly groups
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAnomalyGroupTimeSeries](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAnomalyGroupTimeSeries.html)  **
  - **Description:** Grants permission to get a list of affected metrics for a measure in an anomaly group
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMetricSets](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListMetricSets.html)  **
  - **Description:** Grants permission to get a list of datasets
  - **Resource types (\*required):** [AnomalyDetector](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get a list of tags for a detector, dataset, or alert
  - **Resource types (\*required):** [Alert](#list_lookoutmetrics-resource-Alert) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AnomalyDetector](#list_lookoutmetrics-resource-AnomalyDetector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MetricSet](#list_lookoutmetrics-resource-MetricSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutFeedback](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_PutFeedback.html)  **
  - **Description:** Grants permission to add feedback for an affected metric in an anomaly group
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a detector, dataset, or alert
  - **Resource types (\*required):** [Alert](#list_lookoutmetrics-resource-Alert) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Resource types (\*required):** [AnomalyDetector](#list_lookoutmetrics-resource-AnomalyDetector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Resource types (\*required):** [MetricSet](#list_lookoutmetrics-resource-MetricSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutmetrics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a detector, dataset, or alert
  - **Resource types (\*required):** [Alert](#list_lookoutmetrics-resource-Alert) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Resource types (\*required):** [AnomalyDetector](#list_lookoutmetrics-resource-AnomalyDetector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Resource types (\*required):** [MetricSet](#list_lookoutmetrics-resource-MetricSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutmetrics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAlert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_UpdateAlert.html)  **
  - **Description:** Grants permission to update an alert for an anomaly detector
  - **Resource types (\*required):** [Alert\*](#list_lookoutmetrics-resource-Alert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_UpdateAnomalyDetector.html)  **
  - **Description:** Grants permission to update an anomaly detector
  - **Resource types (\*required):** [AnomalyDetector\*](#list_lookoutmetrics-resource-AnomalyDetector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMetricSet](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_UpdateMetricSet.html)  **
  - **Description:** Grants permission to update a dataset
  - **Resource types (\*required):** [MetricSet\*](#list_lookoutmetrics-resource-MetricSet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Lookout for Metrics
<a name="list_lookoutmetrics-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Alert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_AlertSummary.html)  | arn:${Partition}:lookoutmetrics:${Region}:${Account}:Alert:${AlertName} | [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_) | 
|  [AnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_AnomalyDetectorSummary.html)  | arn:${Partition}:lookoutmetrics:${Region}:${Account}:AnomalyDetector:${AnomalyDetectorName} | [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_) | 
|  [MetricSet](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_MetricSetSummary.html)  | arn:${Partition}:lookoutmetrics:${Region}:${Account}:MetricSet/${AnomalyDetectorName}/${MetricSetName} | [aws:ResourceTag/${TagKey}](#list_lookoutmetrics-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Lookout for Metrics
<a name="list_lookoutmetrics-policy-keys"></a>

Amazon Lookout for Metrics defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 