

# Actions, resources, and condition keys for Amazon DocumentDB Elastic Clusters
<a name="list_docdb-elastic"></a>

Amazon DocumentDB Elastic Clusters (service prefix: `docdb-elastic`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_Operations_Amazon_DocumentDB_Elastic_Clusters.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/documentdb/latest/developerguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/docdb-elastic/docdb-elastic.json) for this service.

**Topics**
+ [API operations defined by Amazon DocumentDB Elastic Clusters](#list_docdb-elastic-operations)
+ [Actions defined by Amazon DocumentDB Elastic Clusters](#list_docdb-elastic-actions-as-permissions)
+ [Resource types defined by Amazon DocumentDB Elastic Clusters](#list_docdb-elastic-resources-for-iam-policies)
+ [Condition keys for Amazon DocumentDB Elastic Clusters](#list_docdb-elastic-policy-keys)

## API operations defined by Amazon DocumentDB Elastic Clusters
<a name="list_docdb-elastic-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_docdb-elastic-actions-as-permissions).




- **   ApplyPendingMaintenanceAction  **
  - **IAM action:**  [docdb-elastic:ApplyPendingMaintenanceAction](#list_docdb-elastic-action-ApplyPendingMaintenanceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyClusterSnapshot  **
  - **IAM action:**  [docdb-elastic:CopyClusterSnapshot](#list_docdb-elastic-action-CopyClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [docdb-elastic:CreateClusterSnapshot](#list_docdb-elastic-action-CreateClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [docdb-elastic:TagResource](#list_docdb-elastic-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCluster  **
  - **IAM action:**  [docdb-elastic:CreateCluster](#list_docdb-elastic-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [docdb-elastic:TagResource](#list_docdb-elastic-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateClusterSnapshot  **
  - **IAM action:**  [docdb-elastic:CreateClusterSnapshot](#list_docdb-elastic-action-CreateClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [docdb-elastic:TagResource](#list_docdb-elastic-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCluster  **
  - **IAM action:**  [docdb-elastic:DeleteCluster](#list_docdb-elastic-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterSnapshot  **
  - **IAM action:**  [docdb-elastic:DeleteClusterSnapshot](#list_docdb-elastic-action-DeleteClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCluster  **
  - **IAM action:**  [docdb-elastic:GetCluster](#list_docdb-elastic-action-GetCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClusterSnapshot  **
  - **IAM action:**  [docdb-elastic:GetClusterSnapshot](#list_docdb-elastic-action-GetClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPendingMaintenanceAction  **
  - **IAM action:**  [docdb-elastic:GetPendingMaintenanceAction](#list_docdb-elastic-action-GetPendingMaintenanceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListClusterSnapshots  **
  - **IAM action:**  [docdb-elastic:ListClusterSnapshots](#list_docdb-elastic-action-ListClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [docdb-elastic:ListClusters](#list_docdb-elastic-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPendingMaintenanceActions  **
  - **IAM action:**  [docdb-elastic:ListPendingMaintenanceActions](#list_docdb-elastic-action-ListPendingMaintenanceActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [docdb-elastic:ListTagsForResource](#list_docdb-elastic-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RestoreClusterFromSnapshot  **
  - **IAM action:**  [docdb-elastic:CreateCluster](#list_docdb-elastic-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [docdb-elastic:RestoreClusterFromSnapshot](#list_docdb-elastic-action-RestoreClusterFromSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [docdb-elastic:TagResource](#list_docdb-elastic-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartCluster  **
  - **IAM action:**  [docdb-elastic:StartCluster](#list_docdb-elastic-action-StartCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCluster  **
  - **IAM action:**  [docdb-elastic:StopCluster](#list_docdb-elastic-action-StopCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [docdb-elastic:TagResource](#list_docdb-elastic-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [docdb-elastic:UntagResource](#list_docdb-elastic-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCluster  **
  - **IAM action:**  [docdb-elastic:UpdateCluster](#list_docdb-elastic-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon DocumentDB Elastic Clusters
<a name="list_docdb-elastic-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ApplyPendingMaintenanceAction.html)  **
  - **Description:** Grants permission to apply pending maintenance actions on Amazon DocDB-Elastic cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_CopyClusterSnapshot.html)  **
  - **Description:** Grants permission to copy a new Amazon DocDB-Elastic cluster snapshot
  - **Resource types (\*required):** [cluster-snapshot\*](#list_docdb-elastic-resource-cluster-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_CreateCluster.html)  **
  - **Description:** Grants permission to create a new Amazon DocDB-Elastic cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_CreateClusterSnapshot.html)  **
  - **Description:** Grants permission to create a new Amazon DocDB-Elastic cluster snapshot
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Resource types (\*required):** [cluster-snapshot\*](#list_docdb-elastic-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_DeleteCluster.html)  **
  - **Description:** Grants permission to delete a cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_DeleteClusterSnapshot.html)  **
  - **Description:** Grants permission to delete a cluster snapshot
  - **Resource types (\*required):** [cluster-snapshot\*](#list_docdb-elastic-resource-cluster-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_GetCluster.html)  **
  - **Description:** Grants permission to view details about a cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_GetClusterSnapshot.html)  **
  - **Description:** Grants permission to view details about a cluster snapshot
  - **Resource types (\*required):** [cluster-snapshot\*](#list_docdb-elastic-resource-cluster-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_GetPendingMaintenanceAction.html)  **
  - **Description:** Grants permission to view details about pending maintenance actions on Amazon DocDB-Elastic cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListClusterSnapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListClusterSnapshots.html)  **
  - **Description:** Grants permission to list the cluster snapshots in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListClusters.html)  **
  - **Description:** Grants permission to list the clusters in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPendingMaintenanceActions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListPendingMaintenanceActions.html)  **
  - **Description:** Grants permission to list details about pending maintenance actions on any Amazon DocDB-Elastic cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tag for an DocumentDB Elastic resource
  - **Resource types (\*required):** [cluster](#list_docdb-elastic-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot](#list_docdb-elastic-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RestoreClusterFromSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_RestoreClusterFromSnapshot.html)  **
  - **Description:** Grants permission to restore cluster from a Amazon DocDB-Elastic cluster snapshot
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Resource types (\*required):** [cluster-snapshot\*](#list_docdb-elastic-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Access level:** Write

- **   [StartCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_StartCluster.html)  **
  - **Description:** Grants permission to start a stopped Amazon DocDB-Elastic cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_StopCluster.html)  **
  - **Description:** Grants permission to stop an existing Amazon DocDB-Elastic cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_TagResource.html)  **
  - **Description:** Grants permission to tag an DocumentDB Elastic resource
  - **Resource types (\*required):** [cluster](#list_docdb-elastic-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Resource types (\*required):** [cluster-snapshot](#list_docdb-elastic-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_docdb-elastic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_UntagResource.html)  **
  - **Description:** Grants permission to untag a DocumentDB Elastic resource
  - **Resource types (\*required):** [cluster](#list_docdb-elastic-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Resource types (\*required):** [cluster-snapshot](#list_docdb-elastic-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_docdb-elastic-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_elastic_UpdateCluster.html)  **
  - **Description:** Grants permission to modify a cluster
  - **Resource types (\*required):** [cluster\*](#list_docdb-elastic-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon DocumentDB Elastic Clusters
<a name="list_docdb-elastic-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html)  | arn:${Partition}:docdb-elastic:${Region}:${Account}:cluster/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_) | 
|  [cluster-snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/elastic-managing.html#elastic-manage-snapshots)  | arn:${Partition}:docdb-elastic:${Region}:${Account}:cluster-snapshot/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_docdb-elastic-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon DocumentDB Elastic Clusters
<a name="list_docdb-elastic-policy-keys"></a>

Amazon DocumentDB Elastic Clusters defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the set of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the set of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the set of tag keys in the request | ArrayOfString | 