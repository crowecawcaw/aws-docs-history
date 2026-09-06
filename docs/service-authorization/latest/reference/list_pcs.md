

# Actions, resources, and condition keys for AWS Parallel Computing Service
<a name="list_pcs"></a>

AWS Parallel Computing Service (service prefix: `pcs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/pcs/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pcs/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/pcs/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pcs/pcs.json) for this service.

**Topics**
+ [API operations defined by AWS Parallel Computing Service](#list_pcs-operations)
+ [Actions defined by AWS Parallel Computing Service](#list_pcs-actions-as-permissions)
+ [Permission-only actions for AWS Parallel Computing Service](#list_pcs-permission-only-actions)
+ [Resource types defined by AWS Parallel Computing Service](#list_pcs-resources-for-iam-policies)
+ [Condition keys for AWS Parallel Computing Service](#list_pcs-policy-keys)

## API operations defined by AWS Parallel Computing Service
<a name="list_pcs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pcs-actions-as-permissions).




- **   CreateCluster  **
  - **IAM action:**  [pcs:CreateCluster](#list_pcs-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pcs:TagResource](#list_pcs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateComputeNodeGroup  **
  - **IAM action:**  [pcs:CreateComputeNodeGroup](#list_pcs-action-CreateComputeNodeGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pcs:TagResource](#list_pcs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   CreateQueue  **
  - **IAM action:**  [pcs:CreateQueue](#list_pcs-action-CreateQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pcs:TagResource](#list_pcs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCluster  **
  - **IAM action:**  [pcs:DeleteCluster](#list_pcs-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteComputeNodeGroup  **
  - **IAM action:**  [pcs:DeleteComputeNodeGroup](#list_pcs-action-DeleteComputeNodeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueue  **
  - **IAM action:**  [pcs:DeleteQueue](#list_pcs-action-DeleteQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCluster  **
  - **IAM action:**  [pcs:GetCluster](#list_pcs-action-GetCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComputeNodeGroup  **
  - **IAM action:**  [pcs:GetComputeNodeGroup](#list_pcs-action-GetComputeNodeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueue  **
  - **IAM action:**  [pcs:GetQueue](#list_pcs-action-GetQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListClusters  **
  - **IAM action:**  [pcs:ListClusters](#list_pcs-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComputeNodeGroups  **
  - **IAM action:**  [pcs:ListComputeNodeGroups](#list_pcs-action-ListComputeNodeGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueues  **
  - **IAM action:**  [pcs:ListQueues](#list_pcs-action-ListQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [pcs:ListTagsForResource](#list_pcs-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterComputeNodeGroupInstance  **
  - **IAM action:**  [pcs:RegisterComputeNodeGroupInstance](#list_pcs-action-RegisterComputeNodeGroupInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [pcs:TagResource](#list_pcs-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [pcs:UntagResource](#list_pcs-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCluster  **
  - **IAM action:**  [pcs:UpdateCluster](#list_pcs-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateComputeNodeGroup  **
  - **IAM action:**  [pcs:UpdateComputeNodeGroup](#list_pcs-action-UpdateComputeNodeGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   UpdateQueue  **
  - **IAM action:**  [pcs:UpdateQueue](#list_pcs-action-UpdateQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Parallel Computing Service
<a name="list_pcs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create clusters
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pcs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateComputeNodeGroup.html)  **
  - **Description:** Grants permission to create compute node groups
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pcs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateQueue.html)  **
  - **Description:** Grants permission to create queues
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pcs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete clusters
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeleteComputeNodeGroup.html)  **
  - **Description:** Grants permission to delete compute node groups
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computenodegroup\*](#list_pcs-resource-computenodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeleteQueue.html)  **
  - **Description:** Grants permission to delete queues
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [queue\*](#list_pcs-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetCluster.html)  **
  - **Description:** Grants permission to get cluster properties
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetComputeNodeGroup.html)  **
  - **Description:** Grants permission to get compute node group properties
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computenodegroup\*](#list_pcs-resource-computenodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetQueue.html)  **
  - **Description:** Grants permission to get queue properties
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [queue\*](#list_pcs-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListClusters](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListClusters.html)  **
  - **Description:** Grants permission to list clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComputeNodeGroups](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListComputeNodeGroups.html)  **
  - **Description:** Grants permission to list compute node groups
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQueues](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListQueues.html)  **
  - **Description:** Grants permission to list queues
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RegisterComputeNodeGroupInstance](https://docs.aws.amazon.com/pcs/latest/APIReference/API_RegisterComputeNodeGroupInstance.html)  **
  - **Description:** Grants permission to register a compute instance in a compute node group
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/pcs/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [cluster](#list_pcs-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pcs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Resource types (\*required):** [computenodegroup](#list_pcs-resource-computenodegroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pcs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Resource types (\*required):** [queue](#list_pcs-resource-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pcs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [cluster](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Resource types (\*required):** [computenodegroup](#list_pcs-resource-computenodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Resource types (\*required):** [queue](#list_pcs-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pcs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateCluster.html)  **
  - **Description:** Grants permission to update cluster properties
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateComputeNodeGroup.html)  **
  - **Description:** Grants permission to update compute node group properties
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computenodegroup\*](#list_pcs-resource-computenodegroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateQueue.html)  **
  - **Description:** Grants permission to update queue properties
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [queue\*](#list_pcs-resource-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Parallel Computing Service
<a name="list_pcs-permission-only-actions"></a>

The following actions are defined by AWS Parallel Computing Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring_scheduler-logs.html)  **
  - **Description:** Grants permission to configure vended log delivery for AWS PCS cluster logs
  - **Resource types (\*required):** [cluster\*](#list_pcs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Parallel Computing Service
<a name="list_pcs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Cluster.html)  | arn:${Partition}:pcs:${Region}:${Account}:cluster/${ClusterIdentifier} | [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_) | 
|  [computenodegroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroup.html)  | arn:${Partition}:pcs:${Region}:${Account}:cluster/${ClusterIdentifier}/computenodegroup/${ComputeNodeGroupIdentifier} | [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_) | 
|  [queue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Queue.html)  | arn:${Partition}:pcs:${Region}:${Account}:cluster/${ClusterIdentifier}/queue/${QueueIdentifier} | [aws:ResourceTag/${TagKey}](#list_pcs-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Parallel Computing Service
<a name="list_pcs-policy-keys"></a>

AWS Parallel Computing Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 