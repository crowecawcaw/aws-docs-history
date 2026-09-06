

# Actions, resources, and condition keys for Network Flow Monitor
<a name="list_networkflowmonitor"></a>

Network Flow Monitor (service prefix: `networkflowmonitor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/networkflowmonitor/networkflowmonitor.json) for this service.

**Topics**
+ [API operations defined by Network Flow Monitor](#list_networkflowmonitor-operations)
+ [Actions defined by Network Flow Monitor](#list_networkflowmonitor-actions-as-permissions)
+ [Resource types defined by Network Flow Monitor](#list_networkflowmonitor-resources-for-iam-policies)
+ [Condition keys for Network Flow Monitor](#list_networkflowmonitor-policy-keys)

## API operations defined by Network Flow Monitor
<a name="list_networkflowmonitor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_networkflowmonitor-actions-as-permissions).




- **   CreateMonitor  **
  - **IAM action:**  [networkflowmonitor:CreateMonitor](#list_networkflowmonitor-action-CreateMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkflowmonitor:TagResource](#list_networkflowmonitor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateScope  **
  - **IAM action:**  [networkflowmonitor:CreateScope](#list_networkflowmonitor-action-CreateScope)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkflowmonitor:TagResource](#list_networkflowmonitor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteMonitor  **
  - **IAM action:**  [networkflowmonitor:DeleteMonitor](#list_networkflowmonitor-action-DeleteMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScope  **
  - **IAM action:**  [networkflowmonitor:DeleteScope](#list_networkflowmonitor-action-DeleteScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetMonitor  **
  - **IAM action:**  [networkflowmonitor:GetMonitor](#list_networkflowmonitor-action-GetMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResultsMonitorTopContributors  **
  - **IAM action:**  [networkflowmonitor:GetQueryResultsMonitorTopContributors](#list_networkflowmonitor-action-GetQueryResultsMonitorTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResultsWorkloadInsightsTopContributors  **
  - **IAM action:**  [networkflowmonitor:GetQueryResultsWorkloadInsightsTopContributors](#list_networkflowmonitor-action-GetQueryResultsWorkloadInsightsTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResultsWorkloadInsightsTopContributorsData  **
  - **IAM action:**  [networkflowmonitor:GetQueryResultsWorkloadInsightsTopContributorsData](#list_networkflowmonitor-action-GetQueryResultsWorkloadInsightsTopContributorsData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryStatusMonitorTopContributors  **
  - **IAM action:**  [networkflowmonitor:GetQueryStatusMonitorTopContributors](#list_networkflowmonitor-action-GetQueryStatusMonitorTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryStatusWorkloadInsightsTopContributors  **
  - **IAM action:**  [networkflowmonitor:GetQueryStatusWorkloadInsightsTopContributors](#list_networkflowmonitor-action-GetQueryStatusWorkloadInsightsTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryStatusWorkloadInsightsTopContributorsData  **
  - **IAM action:**  [networkflowmonitor:GetQueryStatusWorkloadInsightsTopContributorsData](#list_networkflowmonitor-action-GetQueryStatusWorkloadInsightsTopContributorsData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScope  **
  - **IAM action:**  [networkflowmonitor:GetScope](#list_networkflowmonitor-action-GetScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMonitors  **
  - **IAM action:**  [networkflowmonitor:ListMonitors](#list_networkflowmonitor-action-ListMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScopes  **
  - **IAM action:**  [networkflowmonitor:ListScopes](#list_networkflowmonitor-action-ListScopes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [networkflowmonitor:ListTagsForResource](#list_networkflowmonitor-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartQueryMonitorTopContributors  **
  - **IAM action:**  [networkflowmonitor:StartQueryMonitorTopContributors](#list_networkflowmonitor-action-StartQueryMonitorTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQueryWorkloadInsightsTopContributors  **
  - **IAM action:**  [networkflowmonitor:StartQueryWorkloadInsightsTopContributors](#list_networkflowmonitor-action-StartQueryWorkloadInsightsTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQueryWorkloadInsightsTopContributorsData  **
  - **IAM action:**  [networkflowmonitor:StartQueryWorkloadInsightsTopContributorsData](#list_networkflowmonitor-action-StartQueryWorkloadInsightsTopContributorsData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopQueryMonitorTopContributors  **
  - **IAM action:**  [networkflowmonitor:StopQueryMonitorTopContributors](#list_networkflowmonitor-action-StopQueryMonitorTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopQueryWorkloadInsightsTopContributors  **
  - **IAM action:**  [networkflowmonitor:StopQueryWorkloadInsightsTopContributors](#list_networkflowmonitor-action-StopQueryWorkloadInsightsTopContributors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopQueryWorkloadInsightsTopContributorsData  **
  - **IAM action:**  [networkflowmonitor:StopQueryWorkloadInsightsTopContributorsData](#list_networkflowmonitor-action-StopQueryWorkloadInsightsTopContributorsData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [networkflowmonitor:TagResource](#list_networkflowmonitor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [networkflowmonitor:UntagResource](#list_networkflowmonitor-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMonitor  **
  - **IAM action:**  [networkflowmonitor:UpdateMonitor](#list_networkflowmonitor-action-UpdateMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScope  **
  - **IAM action:**  [networkflowmonitor:UpdateScope](#list_networkflowmonitor-action-UpdateScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Network Flow Monitor
<a name="list_networkflowmonitor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateMonitor.html)  **
  - **Description:** Grants permission to create a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkflowmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkflowmonitor-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateScope.html)  **
  - **Description:** Grants permission to create a scope
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkflowmonitor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_networkflowmonitor-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteMonitor.html)  **
  - **Description:** Grants permission to delete a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_DeleteScope.html)  **
  - **Description:** Grants permission to delete a scope
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetMonitor.html)  **
  - **Description:** Grants permission to get information about a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResultsMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html)  **
  - **Description:** Grants permission to get the results of a query that retrieves top contributors data for a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResultsWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html)  **
  - **Description:** Grants permission to get the results of a query that retrieves top contributors for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResultsWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.html)  **
  - **Description:** Grants permission to get the results of a query that retrieves top contributors data points for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryStatusMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.html)  **
  - **Description:** Grants permission to get the status of a query that retrieves top contributors data for a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryStatusWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.html)  **
  - **Description:** Grants permission to get the status of a query that retrieves top contributors for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryStatusWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributorsData.html)  **
  - **Description:** Grants permission to get the status of a query that retrieves top contributors data points for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetScope.html)  **
  - **Description:** Grants permission to get information about a scope
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMonitors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListMonitors.html)  **
  - **Description:** Grants permission to list all monitors in an account and their statuses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScopes](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListScopes.html)  **
  - **Description:** Grants permission to get all scopes for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [monitor](#list_networkflowmonitor-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [scope](#list_networkflowmonitor-resource-scope) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Publish](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_Publish.html)  **
  - **Description:** Grants permission to publish a report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartQueryMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.html)  **
  - **Description:** Grants permission to start a query for retrieving top contributors data for a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartQueryWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributors.html)  **
  - **Description:** Grants permission to start a query for retrieving top contributors data for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartQueryWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryWorkloadInsightsTopContributorsData.html)  **
  - **Description:** Grants permission to start a query for retrieving top contributors data points for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopQueryMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.html)  **
  - **Description:** Grants permission to stop a query for retrieving top contributors data for a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopQueryWorkloadInsightsTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.html)  **
  - **Description:** Grants permission to stop a query for retrieving top contributors for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopQueryWorkloadInsightsTopContributorsData](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributorsData.html)  **
  - **Description:** Grants permission to stop a query for retrieving top contributors data points for workload insights
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [monitor](#list_networkflowmonitor-resource-monitor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkflowmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkflowmonitor-aws_TagKeys)
  - **Resource types (\*required):** [scope](#list_networkflowmonitor-resource-scope) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkflowmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkflowmonitor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [monitor](#list_networkflowmonitor-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkflowmonitor-aws_TagKeys)
  - **Resource types (\*required):** [scope](#list_networkflowmonitor-resource-scope) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkflowmonitor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMonitor](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateMonitor.html)  **
  - **Description:** Grants permission to update a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkflowmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateScope](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateScope.html)  **
  - **Description:** Grants permission to update a scope
  - **Resource types (\*required):** [scope\*](#list_networkflowmonitor-resource-scope)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Network Flow Monitor
<a name="list_networkflowmonitor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors.html)  | arn:${Partition}:networkflowmonitor:${Region}:${Account}:monitor/${MonitorName} | [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_) | 
|  [scope](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-organizations.html)  | arn:${Partition}:networkflowmonitor:${Region}:${Account}:scope/${ScopeId} | [aws:ResourceTag/${TagKey}](#list_networkflowmonitor-aws_ResourceTag___TagKey_) | 

## Condition keys for Network Flow Monitor
<a name="list_networkflowmonitor-policy-keys"></a>

Network Flow Monitor defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request | ArrayOfString | 