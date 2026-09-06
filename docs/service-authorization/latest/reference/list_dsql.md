

# Actions, resources, and condition keys for Amazon Aurora DSQL
<a name="list_dsql"></a>

Amazon Aurora DSQL (service prefix: `dsql`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dsql/dsql.json) for this service.

**Topics**
+ [API operations defined by Amazon Aurora DSQL](#list_dsql-operations)
+ [Actions defined by Amazon Aurora DSQL](#list_dsql-actions-as-permissions)
+ [Permission-only actions for Amazon Aurora DSQL](#list_dsql-permission-only-actions)
+ [Resource types defined by Amazon Aurora DSQL](#list_dsql-resources-for-iam-policies)
+ [Condition keys for Amazon Aurora DSQL](#list_dsql-policy-keys)

## API operations defined by Amazon Aurora DSQL
<a name="list_dsql-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_dsql-actions-as-permissions).




- **   CreateCluster  **
  - **IAM action:**  [dsql:AddPeerCluster](#list_dsql-action-AddPeerCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:CreateCluster](#list_dsql-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:DeleteClusterPolicy](#list_dsql-action-DeleteClusterPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:PutClusterPolicy](#list_dsql-action-PutClusterPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:PutMultiRegionProperties](#list_dsql-action-PutMultiRegionProperties)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:PutWitnessRegion](#list_dsql-action-PutWitnessRegion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:TagResource](#list_dsql-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStream  **
  - **IAM action:**  [dsql:CreateStream](#list_dsql-action-CreateStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:TagResource](#list_dsql-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dsql.amazonaws.com / **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [dsql:DeleteCluster](#list_dsql-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterPolicy  **
  - **IAM action:**  [dsql:DeleteClusterPolicy](#list_dsql-action-DeleteClusterPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStream  **
  - **IAM action:**  [dsql:DeleteStream](#list_dsql-action-DeleteStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCluster  **
  - **IAM action:**  [dsql:GetCluster](#list_dsql-action-GetCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClusterPolicy  **
  - **IAM action:**  [dsql:GetClusterPolicy](#list_dsql-action-GetClusterPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStream  **
  - **IAM action:**  [dsql:GetStream](#list_dsql-action-GetStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcEndpointServiceName  **
  - **IAM action:**  [dsql:GetVpcEndpointServiceName](#list_dsql-action-GetVpcEndpointServiceName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListClusters  **
  - **IAM action:**  [dsql:ListClusters](#list_dsql-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreams  **
  - **IAM action:**  [dsql:ListStreams](#list_dsql-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [dsql:ListTagsForResource](#list_dsql-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutClusterPolicy  **
  - **IAM action:**  [dsql:DeleteClusterPolicy](#list_dsql-action-DeleteClusterPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:PutClusterPolicy](#list_dsql-action-PutClusterPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [dsql:TagResource](#list_dsql-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [dsql:UntagResource](#list_dsql-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCluster  **
  - **IAM action:**  [dsql:AddPeerCluster](#list_dsql-action-AddPeerCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:GetCluster](#list_dsql-action-GetCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [dsql:PutMultiRegionProperties](#list_dsql-action-PutMultiRegionProperties)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:PutWitnessRegion](#list_dsql-action-PutWitnessRegion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:RemovePeerCluster](#list_dsql-action-RemovePeerCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dsql:UpdateCluster](#list_dsql-action-UpdateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by Amazon Aurora DSQL
<a name="list_dsql-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create new clusters
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dsql-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dsql-aws_TagKeys)<br />[dsql:WitnessRegion](#list_dsql-dsql_WitnessRegion)
  - **Access level:** Write

- **   [CreateStream](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)  **
  - **Description:** Grants permission to create a Change Stream for a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dsql-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dsql-aws_TagKeys)
  - **Access level:** Write

- **   [DbConnect](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing-sql-clients.html)  **
  - **Description:** Grants permission to connect to the database
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DbConnectAdmin](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/accessing-sql-clients.html)  **
  - **Description:** Grants permission to connect to the database with admin role. Connecting with any other role requires DbConnect permission
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete a cluster and all of its data
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/rbp-api-operations.html)  **
  - **Description:** Grants permission to remove the inline resource-based policy attached to a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStream](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)  **
  - **Description:** Grants permission to delete a Change Stream
  - **Resource types (\*required):** [Stream\*](#list_dsql-resource-Stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBackupJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)  **
  - **Description:** Grants permission to get the status of an Aurora DSQL cluster backup job
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetCluster.html)  **
  - **Description:** Grants permission to get information about a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/rbp-api-operations.html)  **
  - **Description:** Grants permission to retrieve the inline resource-based policy attached to a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRestoreJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)  **
  - **Description:** Grants permission to get the status of an Aurora DSQL cluster restore job
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStream](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)  **
  - **Description:** Grants permission to get information about a Change Stream
  - **Resource types (\*required):** [Stream\*](#list_dsql-resource-Stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVpcEndpointServiceName](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetVpcEndpointServiceName.html)  **
  - **Description:** Grants permission to retrieve the VPC endpoint service name for a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListClusters](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListClusters.html)  **
  - **Description:** Grants permission to retrieve a list of clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreams](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)  **
  - **Description:** Grants permission to retrieve a list of Change Streams for a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags on an Aurora DSQL resource
  - **Resource types (\*required):** [Cluster](#list_dsql-resource-Cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stream](#list_dsql-resource-Stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/rbp-api-operations.html)  **
  - **Description:** Grants permission to attach or update the inline resource-based policy attached to a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBackupJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)  **
  - **Description:** Grants permission to start a backup job for an Aurora DSQL cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRestoreJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)  **
  - **Description:** Grants permission to start a restore job for an Aurora DSQL cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBackupJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)  **
  - **Description:** Grants permission to stop a backup job for an Aurora DSQL cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRestoreJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html)  **
  - **Description:** Grants permission to stop a restore job for an Aurora DSQL Cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to Aurora DSQL resources
  - **Resource types (\*required):** [Cluster](#list_dsql-resource-Cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dsql-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dsql-aws_TagKeys)
  - **Resource types (\*required):** [Stream](#list_dsql-resource-Stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dsql-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dsql-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from Aurora DSQL resources
  - **Resource types (\*required):** [Cluster](#list_dsql-resource-Cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dsql-aws_TagKeys)
  - **Resource types (\*required):** [Stream](#list_dsql-resource-Stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dsql-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UpdateCluster.html)  **
  - **Description:** Grants permission to modify cluster attributes
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[dsql:WitnessRegion](#list_dsql-dsql_WitnessRegion)
  - **Access level:** Write

- **   [UpdateStream](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)  **
  - **Description:** Grants permission to modify Change Stream attributes
  - **Resource types (\*required):** [Stream\*](#list_dsql-resource-Stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Aurora DSQL
<a name="list_dsql-permission-only-actions"></a>

The following actions are defined by Amazon Aurora DSQL but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AddPeerCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to add a peer cluster to a multi-Region cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InjectError](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  **
  - **Description:** Grants permission to inject errors in targeted clusters
  - **Resource types (\*required):** 
  - **Condition keys:** [dsql:FisActionId](#list_dsql-dsql_FisActionId)<br />[dsql:FisTargetArns](#list_dsql-dsql_FisTargetArns)
  - **Access level:** Write

- **   [PutMultiRegionProperties](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to update multi-Region properties of a cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutWitnessRegion](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to configure and update the witness Region of a multi-Region cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)<br />[dsql:WitnessRegion](#list_dsql-dsql_WitnessRegion)
  - **Access level:** Write

- **   [RemovePeerCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UpdateCluster.html)  **
  - **Description:** Grants permission to remove a peer cluster from a multi-Region cluster
  - **Resource types (\*required):** [Cluster\*](#list_dsql-resource-Cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Aurora DSQL
<a name="list_dsql-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Cluster](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html)  | arn:${Partition}:dsql:${Region}:${Account}:cluster/${Identifier} | [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_) | 
|  [Stream](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)  | arn:${Partition}:dsql:${Region}:${Account}:cluster/${ClusterId}/stream/${StreamId} | [aws:ResourceTag/${TagKey}](#list_dsql-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Aurora DSQL
<a name="list_dsql-policy-keys"></a>

Amazon Aurora DSQL defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [dsql:FisActionId](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  | Filters access by the ID of an AWS FIS action | String | 
|   [dsql:FisTargetArns](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html)  | Filters access by the ARN of an AWS FIS target | ArrayOfARN | 
|   [dsql:WitnessRegion](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/using-iam-condition-keys.html#using-iam-condition-keys-create-mr-cluster-witness)  | Filters access by the witness region of multi-Region clusters | String | 