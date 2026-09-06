

# Actions, resources, and condition keys for Amazon CloudWatch Internet Monitor
<a name="list_internetmonitor"></a>

Amazon CloudWatch Internet Monitor (service prefix: `internetmonitor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/internet-monitor/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/internetmonitor/internetmonitor.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch Internet Monitor](#list_internetmonitor-operations)
+ [Actions defined by Amazon CloudWatch Internet Monitor](#list_internetmonitor-actions-as-permissions)
+ [Permission-only actions for Amazon CloudWatch Internet Monitor](#list_internetmonitor-permission-only-actions)
+ [Resource types defined by Amazon CloudWatch Internet Monitor](#list_internetmonitor-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Internet Monitor](#list_internetmonitor-policy-keys)

## API operations defined by Amazon CloudWatch Internet Monitor
<a name="list_internetmonitor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_internetmonitor-actions-as-permissions).




- **   CreateMonitor  **
  - **IAM action:**  [internetmonitor:CreateMonitor](#list_internetmonitor-action-CreateMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [internetmonitor:TagResource](#list_internetmonitor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteMonitor  **
  - **IAM action:**  [internetmonitor:DeleteMonitor](#list_internetmonitor-action-DeleteMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetHealthEvent  **
  - **IAM action:**  [internetmonitor:GetHealthEvent](#list_internetmonitor-action-GetHealthEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInternetEvent  **
  - **IAM action:**  [internetmonitor:GetInternetEvent](#list_internetmonitor-action-GetInternetEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMonitor  **
  - **IAM action:**  [internetmonitor:GetMonitor](#list_internetmonitor-action-GetMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResults  **
  - **IAM action:**  [internetmonitor:GetQueryResults](#list_internetmonitor-action-GetQueryResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryStatus  **
  - **IAM action:**  [internetmonitor:GetQueryStatus](#list_internetmonitor-action-GetQueryStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListHealthEvents  **
  - **IAM action:**  [internetmonitor:ListHealthEvents](#list_internetmonitor-action-ListHealthEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInternetEvents  **
  - **IAM action:**  [internetmonitor:ListInternetEvents](#list_internetmonitor-action-ListInternetEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitors  **
  - **IAM action:**  [internetmonitor:ListMonitors](#list_internetmonitor-action-ListMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [internetmonitor:ListTagsForResource](#list_internetmonitor-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartQuery  **
  - **IAM action:**  [internetmonitor:StartQuery](#list_internetmonitor-action-StartQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StopQuery  **
  - **IAM action:**  [internetmonitor:StopQuery](#list_internetmonitor-action-StopQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [internetmonitor:TagResource](#list_internetmonitor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [internetmonitor:UntagResource](#list_internetmonitor-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMonitor  **
  - **IAM action:**  [internetmonitor:UpdateMonitor](#list_internetmonitor-action-UpdateMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CloudWatch Internet Monitor
<a name="list_internetmonitor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_CreateMonitor.html)  **
  - **Description:** Grants permission to create a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_internetmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_internetmonitor-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_DeleteMonitor.html)  **
  - **Description:** Grants permission to delete a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetHealthEvent](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetHealthEvent.html)  **
  - **Description:** Grants permission to get information about a health event for a specified monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInternetEvent](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetInternetEvent.html)  **
  - **Description:** Grants permission to get information about a specified internet event
  - **Resource types (\*required):** [InternetEvent\*](#list_internetmonitor-resource-InternetEvent)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetMonitor.html)  **
  - **Description:** Grants permission to get information about a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResults](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryResults.html)  **
  - **Description:** Grants permission to get results for a data query for a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryStatus](https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryStatus.html)  **
  - **Description:** Grants permission to get status for a data query for a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListHealthEvents](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListHealthEvents.html)  **
  - **Description:** Grants permission to list all health events for a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInternetEvents](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListInternetEvents.html)  **
  - **Description:** Grants permission to list all internet events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMonitors](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListMonitors.html)  **
  - **Description:** Grants permission to list all monitors in an account and their statuses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartQuery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_StartQuery.html)  **
  - **Description:** Grants permission to start a data query for a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StopQuery](https://docs.aws.amazon.com/internet-monitor/latest/api/API_StopQuery.html)  **
  - **Description:** Grants permission to stop a data query for a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_internetmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_internetmonitor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/internet-monitor/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_internetmonitor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMonitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_UpdateMonitor.html)  **
  - **Description:** Grants permission to update a monitor
  - **Resource types (\*required):** [Monitor\*](#list_internetmonitor-resource-Monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon CloudWatch Internet Monitor
<a name="list_internetmonitor-permission-only-actions"></a>

The following actions are defined by Amazon CloudWatch Internet Monitor but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html#CloudWatch-Unified-Cross-Account-Setup-permissions)  | Grants permission to share Internet Monitor resources with a monitoring account |  |   | Write | 

## Resource types defined by Amazon CloudWatch Internet Monitor
<a name="list_internetmonitor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [HealthEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html)  | arn:${Partition}:internetmonitor:${Region}:${Account}:monitor/${MonitorName}/health-event/${EventId} | [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_) | 
|  [InternetEvent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html)  | arn:${Partition}:internetmonitor::${Account}:internet-event/${InternetEventId} |   | 
|  [Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-components.html)  | arn:${Partition}:internetmonitor:${Region}:${Account}:monitor/${MonitorName} | [aws:ResourceTag/${TagKey}](#list_internetmonitor-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Internet Monitor
<a name="list_internetmonitor-policy-keys"></a>

Amazon CloudWatch Internet Monitor defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 