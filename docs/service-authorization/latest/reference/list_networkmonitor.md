

# Actions, resources, and condition keys for Amazon CloudWatch Network Synthetic Monitor
<a name="list_networkmonitor"></a>

Amazon CloudWatch Network Synthetic Monitor (service prefix: `networkmonitor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/networkmonitor/networkmonitor.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch Network Synthetic Monitor](#list_networkmonitor-operations)
+ [Actions defined by Amazon CloudWatch Network Synthetic Monitor](#list_networkmonitor-actions-as-permissions)
+ [Resource types defined by Amazon CloudWatch Network Synthetic Monitor](#list_networkmonitor-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Network Synthetic Monitor](#list_networkmonitor-policy-keys)

## API operations defined by Amazon CloudWatch Network Synthetic Monitor
<a name="list_networkmonitor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_networkmonitor-actions-as-permissions).




- **   CreateMonitor  **
  - **IAM action:**  [networkmonitor:CreateMonitor](#list_networkmonitor-action-CreateMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmonitor:TagResource](#list_networkmonitor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProbe  **
  - **IAM action:**  [networkmonitor:CreateProbe](#list_networkmonitor-action-CreateProbe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmonitor:TagResource](#list_networkmonitor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteMonitor  **
  - **IAM action:**  [networkmonitor:DeleteMonitor](#list_networkmonitor-action-DeleteMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProbe  **
  - **IAM action:**  [networkmonitor:DeleteProbe](#list_networkmonitor-action-DeleteProbe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetMonitor  **
  - **IAM action:**  [networkmonitor:GetMonitor](#list_networkmonitor-action-GetMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProbe  **
  - **IAM action:**  [networkmonitor:GetProbe](#list_networkmonitor-action-GetProbe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMonitors  **
  - **IAM action:**  [networkmonitor:ListMonitors](#list_networkmonitor-action-ListMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [networkmonitor:ListTagsForResource](#list_networkmonitor-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [networkmonitor:TagResource](#list_networkmonitor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [networkmonitor:UntagResource](#list_networkmonitor-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMonitor  **
  - **IAM action:**  [networkmonitor:UpdateMonitor](#list_networkmonitor-action-UpdateMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProbe  **
  - **IAM action:**  [networkmonitor:UpdateProbe](#list_networkmonitor-action-UpdateProbe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CloudWatch Network Synthetic Monitor
<a name="list_networkmonitor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitor.html)  **
  - **Description:** Grants permission to create a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkmonitor-resource-monitor)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmonitor-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateProbe.html)  **
  - **Description:** Grants permission to create a probe
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmonitor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_networkmonitor-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteMonitor.html)  **
  - **Description:** Grants permission to delete a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteProbe.html)  **
  - **Description:** Grants permission to delete a probe
  - **Resource types (\*required):** [probe\*](#list_networkmonitor-resource-probe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetMonitor.html)  **
  - **Description:** Grants permission to get information about a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetProbe.html)  **
  - **Description:** Grants permission to get information about a probe
  - **Resource types (\*required):** [probe\*](#list_networkmonitor-resource-probe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMonitors](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListMonitors.html)  **
  - **Description:** Grants permission to list all monitors in an account and their statuses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [monitor](#list_networkmonitor-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [probe](#list_networkmonitor-resource-probe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [monitor](#list_networkmonitor-resource-monitor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmonitor-aws_TagKeys)
  - **Resource types (\*required):** [probe](#list_networkmonitor-resource-probe) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmonitor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmonitor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [monitor](#list_networkmonitor-resource-monitor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmonitor-aws_TagKeys)
  - **Resource types (\*required):** [probe](#list_networkmonitor-resource-probe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmonitor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMonitor](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateMonitor.html)  **
  - **Description:** Grants permission to update a monitor
  - **Resource types (\*required):** [monitor\*](#list_networkmonitor-resource-monitor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProbe](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateProbe.html)  **
  - **Description:** Grants permission to update a probe
  - **Resource types (\*required):** [probe\*](#list_networkmonitor-resource-probe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon CloudWatch Network Synthetic Monitor
<a name="list_networkmonitor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-working-with.html)  | arn:${Partition}:networkmonitor:${Region}:${Account}:monitor/${MonitorName} | [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_) | 
|  [probe](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-working-with.html)  | arn:${Partition}:networkmonitor:${Region}:${Account}:probe/${ProbeId} | [aws:ResourceTag/${TagKey}](#list_networkmonitor-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Network Synthetic Monitor
<a name="list_networkmonitor-policy-keys"></a>

Amazon CloudWatch Network Synthetic Monitor defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request | ArrayOfString | 