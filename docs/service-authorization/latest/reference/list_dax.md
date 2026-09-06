

# Actions, resources, and condition keys for Amazon DynamoDB Accelerator (DAX)
<a name="list_dax"></a>

Amazon DynamoDB Accelerator (DAX) (service prefix: `dax`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access_permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dax/dax.json) for this service.

**Topics**
+ [API operations defined by Amazon DynamoDB Accelerator (DAX)](#list_dax-operations)
+ [Actions defined by Amazon DynamoDB Accelerator (DAX)](#list_dax-actions-as-permissions)
+ [Resource types defined by Amazon DynamoDB Accelerator (DAX)](#list_dax-resources-for-iam-policies)
+ [Condition keys for Amazon DynamoDB Accelerator (DAX)](#list_dax-policy-keys)

## API operations defined by Amazon DynamoDB Accelerator (DAX)
<a name="list_dax-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_dax-actions-as-permissions).




- **   CreateCluster  **
  - **IAM action:**  [dax:CreateCluster](#list_dax-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dax:TagResource](#list_dax-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dax.amazonaws.com / **Access level:** Write

- **   CreateParameterGroup  **
  - **IAM action:**  [dax:CreateParameterGroup](#list_dax-action-CreateParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSubnetGroup  **
  - **IAM action:**  [dax:CreateSubnetGroup](#list_dax-action-CreateSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DecreaseReplicationFactor  **
  - **IAM action:**  [dax:DecreaseReplicationFactor](#list_dax-action-DecreaseReplicationFactor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [dax:DeleteCluster](#list_dax-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteParameterGroup  **
  - **IAM action:**  [dax:DeleteParameterGroup](#list_dax-action-DeleteParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubnetGroup  **
  - **IAM action:**  [dax:DeleteSubnetGroup](#list_dax-action-DeleteSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeClusters  **
  - **IAM action:**  [dax:DescribeClusters](#list_dax-action-DescribeClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDefaultParameters  **
  - **IAM action:**  [dax:DescribeDefaultParameters](#list_dax-action-DescribeDefaultParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEvents  **
  - **IAM action:**  [dax:DescribeEvents](#list_dax-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeParameterGroups  **
  - **IAM action:**  [dax:DescribeParameterGroups](#list_dax-action-DescribeParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeParameters  **
  - **IAM action:**  [dax:DescribeParameters](#list_dax-action-DescribeParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSubnetGroups  **
  - **IAM action:**  [dax:DescribeSubnetGroups](#list_dax-action-DescribeSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   IncreaseReplicationFactor  **
  - **IAM action:**  [dax:IncreaseReplicationFactor](#list_dax-action-IncreaseReplicationFactor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTags  **
  - **IAM action:**  [dax:ListTags](#list_dax-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RebootNode  **
  - **IAM action:**  [dax:RebootNode](#list_dax-action-RebootNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [dax:TagResource](#list_dax-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [dax:UntagResource](#list_dax-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCluster  **
  - **IAM action:**  [dax:UpdateCluster](#list_dax-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateParameterGroup  **
  - **IAM action:**  [dax:UpdateParameterGroup](#list_dax-action-UpdateParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubnetGroup  **
  - **IAM action:**  [dax:UpdateSubnetGroup](#list_dax-action-UpdateSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon DynamoDB Accelerator (DAX)
<a name="list_dax-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html)  **
  - **Description:** Grants permission to return the attributes of one or more items from one or more tables
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html)  **
  - **Description:** Grants permission to put or delete multiple items in one or more tables
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ConditionCheckItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConditionCheckItem.html)  **
  - **Description:** Grants permission to the ConditionCheckItem operation that checks the existence of a set of attributes for the item with the given primary key
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateCluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateCluster.html)  **
  - **Description:** Grants permission to create a DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateParameterGroup.html)  **
  - **Description:** Grants permission to create a parameter group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateSubnetGroup.html)  **
  - **Description:** Grants permission to create a subnet group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DecreaseReplicationFactor](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DecreaseReplicationFactor.html)  **
  - **Description:** Grants permission to remove one or more nodes from a DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteCluster.html)  **
  - **Description:** Grants permission to delete a previously provisioned DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html)  **
  - **Description:** Grants permission to delete a single item in a table by primary key
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:** [dax:EnclosingOperation](#list_dax-dax_EnclosingOperation)
  - **Access level:** Write

- **   [DeleteParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteParameterGroup.html)  **
  - **Description:** Grants permission to delete the specified parameter group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteSubnetGroup.html)  **
  - **Description:** Grants permission to delete a subnet group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeClusters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeClusters.html)  **
  - **Description:** Grants permission to return information about all provisioned DAX clusters
  - **Resource types (\*required):** [application](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDefaultParameters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeDefaultParameters.html)  **
  - **Description:** Grants permission to return the default system parameter information for DAX
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEvents](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeEvents.html)  **
  - **Description:** Grants permission to return events related to DAX clusters and parameter groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeParameterGroups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameterGroups.html)  **
  - **Description:** Grants permission to return a list of parameter group descriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeParameters](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameters.html)  **
  - **Description:** Grants permission to return the detailed parameter list for a particular parameter group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSubnetGroups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeSubnetGroups.html)  **
  - **Description:** Grants permission to return a list of subnet group descriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html)  **
  - **Description:** Grants permission to the GetItem operation that returns a set of attributes for the item with the given primary key
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:** [dax:EnclosingOperation](#list_dax-dax_EnclosingOperation)
  - **Access level:** Read

- **   [IncreaseReplicationFactor](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_IncreaseReplicationFactor.html)  **
  - **Description:** Grants permission to add one or more nodes to a DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListTags](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_ListTags.html)  **
  - **Description:** Grants permission to return a list all of the tags for a DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html)  **
  - **Description:** Grants permission to create a new item, or replace an old item with a new item
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:** [dax:EnclosingOperation](#list_dax-dax_EnclosingOperation)
  - **Access level:** Write

- **   [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html)  **
  - **Description:** Grants permission to use the primary key of a table or a secondary index to directly access items from that table or index
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Read

- **   [RebootNode](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_RebootNode.html)  **
  - **Description:** Grants permission to reboot a single node of a DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html)  **
  - **Description:** Grants permission to return one or more items and item attributes by accessing every item in a table or a secondary index
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_TagResource.html)  **
  - **Description:** Grants permission to associate a set of tags with a DAX resource
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UntagResource.html)  **
  - **Description:** Grants permission to remove the association of tags from a DAX resource
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UpdateCluster](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateCluster.html)  **
  - **Description:** Grants permission to modify the settings for a DAX cluster
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html)  **
  - **Description:** Grants permission to edit an existing item's attributes, or adds a new item to the table if it does not already exist
  - **Resource types (\*required):** [application\*](#list_dax-resource-application)
  - **Condition keys:** [dax:EnclosingOperation](#list_dax-dax_EnclosingOperation)
  - **Access level:** Write

- **   [UpdateParameterGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateParameterGroup.html)  **
  - **Description:** Grants permission to modify the parameters of a parameter group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSubnetGroup](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateSubnetGroup.html)  **
  - **Description:** Grants permission to modify an existing subnet group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon DynamoDB Accelerator (DAX)
<a name="list_dax-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.access-control.html)  | arn:${Partition}:dax:${Region}:${Account}:cache/${ClusterName} |   | 

## Condition keys for Amazon DynamoDB Accelerator (DAX)
<a name="list_dax-policy-keys"></a>

Amazon DynamoDB Accelerator (DAX) defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [dax:EnclosingOperation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.access-control.htmlspecifying-conditions.html#FGAC_DDB.ConditionKeys)  | Used to block Transactions APIs calls and allow the non-Transaction APIs calls and vice-versa | String | 