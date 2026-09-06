

# Actions, resources, and condition keys for AWS CloudWatch RUM
<a name="list_rum"></a>

AWS CloudWatch RUM (service prefix: `rum`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rum/rum.json) for this service.

**Topics**
+ [API operations defined by AWS CloudWatch RUM](#list_rum-operations)
+ [Actions defined by AWS CloudWatch RUM](#list_rum-actions-as-permissions)
+ [Resource types defined by AWS CloudWatch RUM](#list_rum-resources-for-iam-policies)
+ [Condition keys for AWS CloudWatch RUM](#list_rum-policy-keys)

## API operations defined by AWS CloudWatch RUM
<a name="list_rum-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rum-actions-as-permissions).




- **   BatchCreateRumMetricDefinitions  **
  - **IAM action:**  [rum:BatchCreateRumMetricDefinitions](#list_rum-action-BatchCreateRumMetricDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteRumMetricDefinitions  **
  - **IAM action:**  [rum:BatchDeleteRumMetricDefinitions](#list_rum-action-BatchDeleteRumMetricDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetRumMetricDefinitions  **
  - **IAM action:**  [rum:BatchGetRumMetricDefinitions](#list_rum-action-BatchGetRumMetricDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAppMonitor  **
  - **IAM action:**  [rum:CreateAppMonitor](#list_rum-action-CreateAppMonitor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rum:TagResource](#list_rum-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAppMonitor  **
  - **IAM action:**  [rum:DeleteAppMonitor](#list_rum-action-DeleteAppMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [rum:DeleteResourcePolicy](#list_rum-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRumMetricsDestination  **
  - **IAM action:**  [rum:DeleteRumMetricsDestination](#list_rum-action-DeleteRumMetricsDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAppMonitor  **
  - **IAM action:**  [rum:GetAppMonitor](#list_rum-action-GetAppMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAppMonitorData  **
  - **IAM action:**  [rum:GetAppMonitorData](#list_rum-action-GetAppMonitorData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [rum:GetResourcePolicy](#list_rum-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAppMonitors  **
  - **IAM action:**  [rum:ListAppMonitors](#list_rum-action-ListAppMonitors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRumMetricsDestinations  **
  - **IAM action:**  [rum:ListRumMetricsDestinations](#list_rum-action-ListRumMetricsDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [rum:ListTagsForResource](#list_rum-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **IAM action:**  [rum:PutResourcePolicy](#list_rum-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRumEvents  **
  - **IAM action:**  [rum:PutRumEvents](#list_rum-action-PutRumEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRumMetricsDestination  **
  - **IAM action:**  [rum:PutRumMetricsDestination](#list_rum-action-PutRumMetricsDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rum.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [rum:TagResource](#list_rum-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [rum:UntagResource](#list_rum-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAppMonitor  **
  - **IAM action:**  [rum:UpdateAppMonitor](#list_rum-action-UpdateAppMonitor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRumMetricDefinition  **
  - **IAM action:**  [rum:UpdateRumMetricDefinition](#list_rum-action-UpdateRumMetricDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS CloudWatch RUM
<a name="list_rum-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html)  **
  - **Description:** Grants permission to create rum metric definitions
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.html)  **
  - **Description:** Grants permission to remove rum metric definitions
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.html)  **
  - **Description:** Grants permission to get rum metric definitions
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html)  **
  - **Description:** Grants permission to create appMonitor metadata
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rum-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rum-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.html)  **
  - **Description:** Grants permission to delete appMonitor metadata
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy attached to an app monitor
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.html)  **
  - **Description:** Grants permission to delete rum metrics destinations
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html)  **
  - **Description:** Grants permission to get appMonitor metadata
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAppMonitorData](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitorData.html)  **
  - **Description:** Grants permission to get appMonitor data
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve a resource policy attached to an app monitor
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAppMonitors](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html)  **
  - **Description:** Grants permission to list appMonitors metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRumMetricsDestinations](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListRumMetricsDestinations.html)  **
  - **Description:** Grants permission to list rum metrics destinations
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to an app monitor
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRumEvents](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html)  **
  - **Description:** Grants permission to put RUM events for appmonitor
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html)  **
  - **Description:** Grants permission to put rum metrics destinations
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag resources
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rum-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rum-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag resources
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rum-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html)  **
  - **Description:** Grants permission to update appmonitor metadata
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRumMetricDefinition](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.html)  **
  - **Description:** Grants permission to update rum metric definition
  - **Resource types (\*required):** [AppMonitorResource\*](#list_rum-resource-AppMonitorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CloudWatch RUM
<a name="list_rum-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AppMonitorResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/API_AppMonitor.html)  | arn:${Partition}:rum:${Region}:${Account}:appmonitor/${Name} | [aws:ResourceTag/${TagKey}](#list_rum-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CloudWatch RUM
<a name="list_rum-policy-keys"></a>

AWS CloudWatch RUM defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed the request on behalf of the IAM principal | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the tags associated with the resource that make the request on behalf of the IAM principal | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request on behalf of the IAM principal | ArrayOfString | 