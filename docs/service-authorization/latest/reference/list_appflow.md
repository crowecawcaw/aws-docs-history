

# Actions, resources, and condition keys for Amazon AppFlow
<a name="list_appflow"></a>

Amazon AppFlow (service prefix: `appflow`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appflow/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appflow/1.0/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appflow/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appflow/appflow.json) for this service.

**Topics**
+ [API operations defined by Amazon AppFlow](#list_appflow-operations)
+ [Actions defined by Amazon AppFlow](#list_appflow-actions-as-permissions)
+ [Permission-only actions for Amazon AppFlow](#list_appflow-permission-only-actions)
+ [Resource types defined by Amazon AppFlow](#list_appflow-resources-for-iam-policies)
+ [Condition keys for Amazon AppFlow](#list_appflow-policy-keys)

## API operations defined by Amazon AppFlow
<a name="list_appflow-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appflow-actions-as-permissions).




- **   CancelFlowExecutions  **
  - **IAM action:**  [appflow:CancelFlowExecutions](#list_appflow-action-CancelFlowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectorProfile  **
  - **IAM action:**  [appflow:CreateConnectorProfile](#list_appflow-action-CreateConnectorProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appflow:DescribeConnector](#list_appflow-action-DescribeConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appflow.amazonaws.com, redshift.amazonaws.com / **Access level:** Write

- **   CreateFlow  **
  - **IAM action:**  [appflow:CreateFlow](#list_appflow-action-CreateFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appflow:TagResource](#list_appflow-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [appflow:UseConnectorProfile](#list_appflow-action-UseConnectorProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appflow.amazonaws.com / **Access level:** Write

- **   DeleteConnectorProfile  **
  - **IAM action:**  [appflow:DeleteConnectorProfile](#list_appflow-action-DeleteConnectorProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlow  **
  - **IAM action:**  [appflow:DeleteFlow](#list_appflow-action-DeleteFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConnector  **
  - **IAM action:**  [appflow:DescribeConnector](#list_appflow-action-DescribeConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnectorEntity  **
  - **IAM action:**  [appflow:DescribeConnectorEntity](#list_appflow-action-DescribeConnectorEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnectorProfiles  **
  - **IAM action:**  [appflow:DescribeConnectorProfiles](#list_appflow-action-DescribeConnectorProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnectors  **
  - **IAM action:**  [appflow:DescribeConnectors](#list_appflow-action-DescribeConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlow  **
  - **IAM action:**  [appflow:DescribeFlow](#list_appflow-action-DescribeFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlowExecutionRecords  **
  - **IAM action:**  [appflow:DescribeFlowExecutionRecords](#list_appflow-action-DescribeFlowExecutionRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectorEntities  **
  - **IAM action:**  [appflow:ListConnectorEntities](#list_appflow-action-ListConnectorEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectors  **
  - **IAM action:**  [appflow:ListConnectors](#list_appflow-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlows  **
  - **IAM action:**  [appflow:ListFlows](#list_appflow-action-ListFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [appflow:ListTagsForResource](#list_appflow-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterConnector  **
  - **IAM action:**  [appflow:RegisterConnector](#list_appflow-action-RegisterConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetConnectorMetadataCache  **
  - **IAM action:**  [appflow:ResetConnectorMetadataCache](#list_appflow-action-ResetConnectorMetadataCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFlow  **
  - **IAM action:**  [appflow:StartFlow](#list_appflow-action-StartFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopFlow  **
  - **IAM action:**  [appflow:StopFlow](#list_appflow-action-StopFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [appflow:TagResource](#list_appflow-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UnregisterConnector  **
  - **IAM action:**  [appflow:UnRegisterConnector](#list_appflow-action-UnRegisterConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [appflow:UntagResource](#list_appflow-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnectorProfile  **
  - **IAM action:**  [appflow:UpdateConnectorProfile](#list_appflow-action-UpdateConnectorProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appflow.amazonaws.com, redshift.amazonaws.com / **Access level:** Write

- **   UpdateConnectorRegistration  **
  - **IAM action:**  [appflow:UpdateConnectorRegistration](#list_appflow-action-UpdateConnectorRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlow  **
  - **IAM action:**  [appflow:UpdateFlow](#list_appflow-action-UpdateFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appflow:UseConnectorProfile](#list_appflow-action-UseConnectorProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appflow.amazonaws.com / **Access level:** Write



## Actions defined by Amazon AppFlow
<a name="list_appflow-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelFlowExecutions](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CancelFlowExecutions.html)  **
  - **Description:** Grants permission to cancel in-progress executions of an Amazon AppFlow flow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html)  **
  - **Description:** Grants permission to create a login profile to be used with Amazon AppFlow flows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFlow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateFlow.html)  **
  - **Description:** Grants permission to create an Amazon AppFlow flow
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appflow-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnectorProfiles.html)  **
  - **Description:** Grants permission to delete a login profile configured in Amazon AppFlow
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFlow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DeleteFlow.html)  **
  - **Description:** Grants permission to delete an Amazon AppFlow flow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appflow-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeConnector](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnector.html)  **
  - **Description:** Grants permission to describe a connector registered in Amazon AppFlow
  - **Resource types (\*required):** [connector\*](#list_appflow-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConnectorEntity](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnectorEntity.html)  **
  - **Description:** Grants permission to describe all fields for an object in a login profile configured in Amazon AppFlow
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConnectorProfiles](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnectorProfiles.html)  **
  - **Description:** Grants permission to describe all login profiles configured in Amazon AppFlow
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConnectors](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnectors.html )  **
  - **Description:** Grants permission to describe all connectors supported by Amazon AppFlow
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFlow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeFlow.html)  **
  - **Description:** Grants permission to describe a specific flow configured in Amazon AppFlow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlowExecutionRecords](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeFlowExecutionRecords.html)  **
  - **Description:** Grants permission to describe all flow executions for a flow configured in Amazon AppFlow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListConnectorEntities](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListConnectorEntities.html)  **
  - **Description:** Grants permission to list all objects for a login profile configured in Amazon AppFlow
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectors](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to list all connectors supported in Amazon AppFlow
  - **Resource types (\*required):** [connector\*](#list_appflow-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFlows](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListFlows.html)  **
  - **Description:** Grants permission to list all flows configured in Amazon AppFlow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a flow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RegisterConnector](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_RegisterConnector.html)  **
  - **Description:** Grants permission to register an Amazon AppFlow connector
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appflow-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Access level:** Write

- **   [ResetConnectorMetadataCache](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ResetConnectorMetadataCache.html)  **
  - **Description:** Grants permission to resets metadata of connector entities that Amazon AppFlow stored in its cache
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartFlow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_StartFlow.html)  **
  - **Description:** Grants permission to activate (for scheduled and event-triggered flows) or run (for on-demand flows) a flow configured in Amazon AppFlow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopFlow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_StopFlow.html)  **
  - **Description:** Grants permission to deactivate a scheduled or event-triggered flow configured in Amazon AppFlow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a flow or a connector
  - **Resource types (\*required):** [connector](#list_appflow-resource-connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appflow-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Resource types (\*required):** [flow](#list_appflow-resource-flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appflow-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnRegisterConnector](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UnregisterConnector.html)  **
  - **Description:** Grants permission to un-register a connector in Amazon AppFlow
  - **Resource types (\*required):** [connector\*](#list_appflow-resource-connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appflow-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a flow or a connector
  - **Resource types (\*required):** [connector](#list_appflow-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Resource types (\*required):** [flow](#list_appflow-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appflow-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpdateConnectorProfile.html)  **
  - **Description:** Grants permission to update a login profile configured in Amazon AppFlow
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnectorRegistration](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpdateConnectorRegistration.html)  **
  - **Description:** Grants permission to update a registered connector configured in Amazon AppFlow
  - **Resource types (\*required):** [connector\*](#list_appflow-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpdateFlow.html)  **
  - **Description:** Grants permission to update a flow configured in Amazon AppFlow
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon AppFlow
<a name="list_appflow-permission-only-actions"></a>

The following actions are defined by Amazon AppFlow but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DescribeConnectorFields](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#appflow-api-actions)  **
  - **Description:** Grants permission to describe all fields for an object in a login profile configured in Amazon AppFlow (Console Only)
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFlowExecution](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#appflow-api-actions)  **
  - **Description:** Grants permission to describe all flow executions for a flow configured in Amazon AppFlow (Console Only)
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlows](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#appflow-api-actions)  **
  - **Description:** Grants permission to describe all flows configured in Amazon AppFlow (Console Only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnectorFields](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#appflow-api-actions)  **
  - **Description:** Grants permission to list all objects for a login profile configured in Amazon AppFlow (Console Only)
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [RunFlow](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#appflow-api-actions)  **
  - **Description:** Grants permission to run a flow configured in Amazon AppFlow (Console Only)
  - **Resource types (\*required):** [flow\*](#list_appflow-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UseConnectorProfile](API_CreateFlow.html)  **
  - **Description:** Grants permission to use a connector profile while creating a flow in Amazon AppFlow
  - **Resource types (\*required):** [connectorprofile\*](#list_appflow-resource-connectorprofile)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon AppFlow
<a name="list_appflow-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [connector](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorDetail.html)  | arn:${Partition}:appflow:${Region}:${Account}:connector/${ConnectorLabel} | [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_) | 
|  [connectorprofile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorProfile.html)  | arn:${Partition}:appflow:${Region}:${Account}:connectorprofile/${ProfileName} |   | 
|  [flow](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_FlowDefinition.html)  | arn:${Partition}:appflow:${Region}:${Account}:flow/${FlowName} | [aws:ResourceTag/${TagKey}](#list_appflow-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon AppFlow
<a name="list_appflow-policy-keys"></a>

Amazon AppFlow defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by presence of mandatory tags in the request | ArrayOfString | 