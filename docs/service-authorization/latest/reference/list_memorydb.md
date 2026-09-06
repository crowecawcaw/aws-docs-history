

# Actions, resources, and condition keys for Amazon MemoryDB
<a name="list_memorydb"></a>

Amazon MemoryDB (service prefix: `memorydb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/memorydb/index.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/memorydb/latest/devguide/iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/memorydb/memorydb.json) for this service.

**Topics**
+ [API operations defined by Amazon MemoryDB](#list_memorydb-operations)
+ [Actions defined by Amazon MemoryDB](#list_memorydb-actions-as-permissions)
+ [Permission-only actions for Amazon MemoryDB](#list_memorydb-permission-only-actions)
+ [Resource types defined by Amazon MemoryDB](#list_memorydb-resources-for-iam-policies)
+ [Condition keys for Amazon MemoryDB](#list_memorydb-policy-keys)

## API operations defined by Amazon MemoryDB
<a name="list_memorydb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_memorydb-actions-as-permissions).




- **   BatchUpdateCluster  **
  - **IAM action:**  [memorydb:BatchUpdateCluster](#list_memorydb-action-BatchUpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopySnapshot  **
  - **IAM action:**  [memorydb:CopySnapshot](#list_memorydb-action-CopySnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateACL  **
  - **IAM action:**  [memorydb:CreateAcl](#list_memorydb-action-CreateAcl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCluster  **
  - **IAM action:**  [memorydb:CreateCluster](#list_memorydb-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMultiRegionCluster  **
  - **IAM action:**  [memorydb:CreateMultiRegionCluster](#list_memorydb-action-CreateMultiRegionCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateParameterGroup  **
  - **IAM action:**  [memorydb:CreateParameterGroup](#list_memorydb-action-CreateParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSnapshot  **
  - **IAM action:**  [memorydb:CreateSnapshot](#list_memorydb-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSubnetGroup  **
  - **IAM action:**  [memorydb:CreateSubnetGroup](#list_memorydb-action-CreateSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUser  **
  - **IAM action:**  [memorydb:CreateUser](#list_memorydb-action-CreateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteACL  **
  - **IAM action:**  [memorydb:DeleteAcl](#list_memorydb-action-DeleteAcl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [memorydb:CreateSnapshot](#list_memorydb-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:DeleteCluster](#list_memorydb-action-DeleteCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteMultiRegionCluster  **
  - **IAM action:**  [memorydb:DeleteMultiRegionCluster](#list_memorydb-action-DeleteMultiRegionCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteParameterGroup  **
  - **IAM action:**  [memorydb:DeleteParameterGroup](#list_memorydb-action-DeleteParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshot  **
  - **IAM action:**  [memorydb:DeleteSnapshot](#list_memorydb-action-DeleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubnetGroup  **
  - **IAM action:**  [memorydb:DeleteSubnetGroup](#list_memorydb-action-DeleteSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [memorydb:DeleteUser](#list_memorydb-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeACLs  **
  - **IAM action:**  [memorydb:DescribeAcls](#list_memorydb-action-DescribeAcls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusters  **
  - **IAM action:**  [memorydb:DescribeClusters](#list_memorydb-action-DescribeClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEngineVersions  **
  - **IAM action:**  [memorydb:DescribeEngineVersions](#list_memorydb-action-DescribeEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEvents  **
  - **IAM action:**  [memorydb:DescribeEvents](#list_memorydb-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMultiRegionClusters  **
  - **IAM action:**  [memorydb:DescribeMultiRegionClusters](#list_memorydb-action-DescribeMultiRegionClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMultiRegionParameterGroups  **
  - **IAM action:**  [memorydb:DescribeMultiRegionParameterGroups](#list_memorydb-action-DescribeMultiRegionParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMultiRegionParameters  **
  - **IAM action:**  [memorydb:DescribeMultiRegionParameters](#list_memorydb-action-DescribeMultiRegionParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeParameterGroups  **
  - **IAM action:**  [memorydb:DescribeParameterGroups](#list_memorydb-action-DescribeParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeParameters  **
  - **IAM action:**  [memorydb:DescribeParameters](#list_memorydb-action-DescribeParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedNodes  **
  - **IAM action:**  [memorydb:DescribeReservedNodes](#list_memorydb-action-DescribeReservedNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedNodesOfferings  **
  - **IAM action:**  [memorydb:DescribeReservedNodesOfferings](#list_memorydb-action-DescribeReservedNodesOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceUpdates  **
  - **IAM action:**  [memorydb:DescribeServiceUpdates](#list_memorydb-action-DescribeServiceUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshots  **
  - **IAM action:**  [memorydb:DescribeSnapshots](#list_memorydb-action-DescribeSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSubnetGroups  **
  - **IAM action:**  [memorydb:DescribeSubnetGroups](#list_memorydb-action-DescribeSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUsers  **
  - **IAM action:**  [memorydb:DescribeUsers](#list_memorydb-action-DescribeUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   FailoverShard  **
  - **IAM action:**  [memorydb:FailoverShard](#list_memorydb-action-FailoverShard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAllowedMultiRegionClusterUpdates  **
  - **IAM action:**  [memorydb:ListAllowedMultiRegionClusterUpdates](#list_memorydb-action-ListAllowedMultiRegionClusterUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAllowedNodeTypeUpdates  **
  - **IAM action:**  [memorydb:ListAllowedNodeTypeUpdates](#list_memorydb-action-ListAllowedNodeTypeUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTags  **
  - **IAM action:**  [memorydb:ListTags](#list_memorydb-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PurchaseReservedNodesOffering  **
  - **IAM action:**  [memorydb:PurchaseReservedNodesOffering](#list_memorydb-action-PurchaseReservedNodesOffering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ResetParameterGroup  **
  - **IAM action:**  [memorydb:ResetParameterGroup](#list_memorydb-action-ResetParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [memorydb:TagResource](#list_memorydb-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [memorydb:UntagResource](#list_memorydb-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateACL  **
  - **IAM action:**  [memorydb:UpdateAcl](#list_memorydb-action-UpdateAcl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCluster  **
  - **IAM action:**  [memorydb:UpdateCluster](#list_memorydb-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMultiRegionCluster  **
  - **IAM action:**  [memorydb:UpdateMultiRegionCluster](#list_memorydb-action-UpdateMultiRegionCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateParameterGroup  **
  - **IAM action:**  [memorydb:UpdateParameterGroup](#list_memorydb-action-UpdateParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubnetGroup  **
  - **IAM action:**  [memorydb:UpdateSubnetGroup](#list_memorydb-action-UpdateSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [memorydb:UpdateUser](#list_memorydb-action-UpdateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon MemoryDB
<a name="list_memorydb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchUpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_BatchUpdateCluster.html)  **
  - **Description:** Grants permissions to apply service updates
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Connect](https://docs.aws.amazon.com/memorydb/latest/devguide/auth-iam.html)  **
  - **Description:** Allows an IAM user or role to connect as a specified MemoryDB user to a node in a cluster
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_memorydb-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopySnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CopySnapshot.html)  **
  - **Description:** Grants permissions to make a copy of an existing snapshot
  - **Resource types (\*required):** [snapshot\*](#list_memorydb-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAcl](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateAcl.html)  **
  - **Description:** Grants permissions to create a new access control list
  - **Resource types (\*required):** [user\*](#list_memorydb-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permissions to create a cluster
  - **Resource types (\*required):** [acl\*](#list_memorydb-resource-acl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [multiregioncluster](#list_memorydb-resource-multiregioncluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [parametergroup\*](#list_memorydb-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [snapshot](#list_memorydb-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [subnetgroup\*](#list_memorydb-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Access level:** Write

- **   [CreateMultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateMultiRegionCluster.html)  **
  - **Description:** Grants permissions to create a Multi-Region cluster
  - **Resource types (\*required):** [multiregionparametergroup\*](#list_memorydb-resource-multiregionparametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Access level:** Write

- **   [CreateParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateParameterGroup.html)  **
  - **Description:** Grants permissions to create a new parameter group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSnapshot.html)  **
  - **Description:** Grants permissions to create a backup of a cluster at the current point in time
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSubnetGroup.html)  **
  - **Description:** Grants permissions to create a new subnet group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateUser.html)  **
  - **Description:** Grants permissions to create a new user
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:UserAuthenticationMode](#list_memorydb-memorydb_UserAuthenticationMode)
  - **Access level:** Write

- **   [DeleteAcl](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteAcl.html)  **
  - **Description:** Grants permissions to delete an access control list
  - **Resource types (\*required):** [acl\*](#list_memorydb-resource-acl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permissions to delete a previously provisioned cluster
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [multiregioncluster](#list_memorydb-resource-multiregioncluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [snapshot](#list_memorydb-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteMultiRegionCluster.html)  **
  - **Description:** Grants permissions to delete a Multi-Region cluster
  - **Resource types (\*required):** [multiregioncluster\*](#list_memorydb-resource-multiregioncluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Access level:** Write

- **   [DeleteParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteParameterGroup.html)  **
  - **Description:** Grants permissions to delete a parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_memorydb-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSnapshot.html)  **
  - **Description:** Grants permissions to delete a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_memorydb-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSubnetGroup.html)  **
  - **Description:** Grants permissions to delete a subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_memorydb-resource-subnetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permissions to delete a user
  - **Resource types (\*required):** [user\*](#list_memorydb-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAcls](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeAcls.html)  **
  - **Description:** Grants permissions to retrieve information about access control lists
  - **Resource types (\*required):** [acl\*](#list_memorydb-resource-acl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html)  **
  - **Description:** Grants permissions to retrieve information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster identifier is supplied
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEngineVersions](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEngineVersions.html)  **
  - **Description:** Grants permissions to list of the available engines and their versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEvents](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permissions to retrieve events related to clusters, subnet groups, and parameter groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMultiRegionClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeMultiRegionClusters.html)  **
  - **Description:** Grants permissions to retrieve information about all Multi-Region clusters if no cluster identifier is specified, or about a specific Multi-Region cluster if a cluster identifier is supplied
  - **Resource types (\*required):** [multiregioncluster\*](#list_memorydb-resource-multiregioncluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Access level:** Read

- **   [DescribeMultiRegionParameterGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeMultiRegionParameterGroups.html)  **
  - **Description:** Grants permissions to retrieve information about Multi-Region parameter groups
  - **Resource types (\*required):** [multiregionparametergroup\*](#list_memorydb-resource-multiregionparametergroup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMultiRegionParameters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeMultiRegionParameters.html)  **
  - **Description:** Grants permissions to retrieve a detailed parameter list for a particular Multi-Region parameter group
  - **Resource types (\*required):** [multiregionparametergroup\*](#list_memorydb-resource-multiregionparametergroup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeParameterGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameterGroups.html)  **
  - **Description:** Grants permissions to retrieve information about parameter groups
  - **Resource types (\*required):** [parametergroup\*](#list_memorydb-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeParameters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameters.html)  **
  - **Description:** Grants permissions to retrieve a detailed parameter list for a particular parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_memorydb-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeReservedNodes](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeReservedNodes.html)  **
  - **Description:** Grants permissions to retrieve reserved nodes
  - **Resource types (\*required):** [reservednode\*](#list_memorydb-resource-reservednode)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeReservedNodesOfferings](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeReservedNodesOfferings.html)  **
  - **Description:** Grants permissions to retrieve reserved nodes offerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeServiceUpdates.html)  **
  - **Description:** Grants permissions to retrieve details of the service updates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSnapshots](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSnapshots.html)  **
  - **Description:** Grants permissions to retrieve information about cluster snapshots
  - **Resource types (\*required):** [snapshot\*](#list_memorydb-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSubnetGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSubnetGroups.html)  **
  - **Description:** Grants permissions to retrieve a list of subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_memorydb-resource-subnetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUsers](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeUsers.html)  **
  - **Description:** Grants permissions to retrieve information about users
  - **Resource types (\*required):** [user\*](#list_memorydb-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [FailoverShard](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_FailoverShard.html)  **
  - **Description:** Grants permissions to test automatic failover on a specified shard in a cluster
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAllowedMultiRegionClusterUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedMultiRegionClusterUpdates.html)  **
  - **Description:** Grants permissions to list available Multi-Region cluster updates
  - **Resource types (\*required):** [multiregioncluster\*](#list_memorydb-resource-multiregioncluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Access level:** Read

- **   [ListAllowedNodeTypeUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedNodeTypeUpdates.html)  **
  - **Description:** Grants permissions to list available node type updates
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTags](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permissions to list cost allocation tags
  - **Resource types (\*required):** [acl](#list_memorydb-resource-acl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_memorydb-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [multiregioncluster](#list_memorydb-resource-multiregioncluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [parametergroup](#list_memorydb-resource-parametergroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_memorydb-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subnetgroup](#list_memorydb-resource-subnetgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_memorydb-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PurchaseReservedNodesOffering](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_PurchaseReservedNodesOffering.html)  **
  - **Description:** Grants permissions to purchase a new reserved node
  - **Resource types (\*required):** [reservednode\*](#list_memorydb-resource-reservednode)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Write

- **   [ResetParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ResetParameterGroup.html)  **
  - **Description:** Grants permissions to modify the parameters of a parameter group to the engine or system default value
  - **Resource types (\*required):** [parametergroup\*](#list_memorydb-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permissions to add up to 10 cost allocation tags to the named resource
  - **Resource types (\*required):** [acl](#list_memorydb-resource-acl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_memorydb-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [multiregioncluster](#list_memorydb-resource-multiregioncluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [parametergroup](#list_memorydb-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [reservednode](#list_memorydb-resource-reservednode) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_memorydb-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [subnetgroup](#list_memorydb-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_memorydb-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_memorydb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permissions to remove the tags identified by the TagKeys list from a resource
  - **Resource types (\*required):** [acl](#list_memorydb-resource-acl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [cluster](#list_memorydb-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [multiregioncluster](#list_memorydb-resource-multiregioncluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [parametergroup](#list_memorydb-resource-parametergroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_memorydb-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [subnetgroup](#list_memorydb-resource-subnetgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_memorydb-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_memorydb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAcl](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateAcl.html)  **
  - **Description:** Grants permissions to update an access control list
  - **Resource types (\*required):** [acl\*](#list_memorydb-resource-acl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_memorydb-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html)  **
  - **Description:** Grants permissions to update the settings for a cluster
  - **Resource types (\*required):** [acl](#list_memorydb-resource-acl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster\*](#list_memorydb-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [parametergroup](#list_memorydb-resource-parametergroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMultiRegionCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateMultiRegionCluster.html)  **
  - **Description:** Grants permissions to update the settings for a Multi-Region cluster
  - **Resource types (\*required):** [multiregioncluster\*](#list_memorydb-resource-multiregioncluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Resource types (\*required):** [multiregionparametergroup](#list_memorydb-resource-multiregionparametergroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateParameterGroup.html)  **
  - **Description:** Grants permissions to update parameters in a parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_memorydb-resource-parametergroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateSubnetGroup.html)  **
  - **Description:** Grants permissions to update a subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_memorydb-resource-subnetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateUser.html)  **
  - **Description:** Grants permissions to update a user
  - **Resource types (\*required):** [user\*](#list_memorydb-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:UserAuthenticationMode](#list_memorydb-memorydb_UserAuthenticationMode)
  - **Access level:** Write



## Permission-only actions for Amazon MemoryDB
<a name="list_memorydb-permission-only-actions"></a>

The following actions are defined by Amazon MemoryDB but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [PauseMultiRegionClusterReplication](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#memorydb-actions-reference)  **
  - **Description:** Grants permission to pause replication for a Multi-Region cluster
  - **Resource types (\*required):** [multiregioncluster\*](#list_memorydb-resource-multiregioncluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled)
  - **Access level:** Write



## Resource types defined by Amazon MemoryDB
<a name="list_memorydb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [acl](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:acl/${AclName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:cluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 
|  [multiregioncluster](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb::${Account}:multiregioncluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_)<br />[memorydb:TLSEnabled](#list_memorydb-memorydb_TLSEnabled) | 
|  [multiregionparametergroup](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb::${Account}:multiregionparametergroup/${MultiRegionParameterGroupName} |   | 
|  [parametergroup](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:parametergroup/${ParameterGroupName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 
|  [reservednode](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:reservednode/${ReservationID} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 
|  [snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:snapshot/${SnapshotName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 
|  [subnetgroup](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:subnetgroup/${SubnetGroupName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 
|  [user](https://docs.aws.amazon.com/memorydb/latest/devguide/WhatIs.Components.html)  | arn:${Partition}:memorydb:${Region}:${Account}:user/${UserName} | [aws:ResourceTag/${TagKey}](#list_memorydb-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon MemoryDB
<a name="list_memorydb-policy-keys"></a>

Amazon MemoryDB defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the tag keys that are passed in the request | ArrayOfString | 
|   [memorydb:TLSEnabled](https://docs.aws.amazon.com/memorydb/latest/devguide/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the TLSEnabled parameter present in the request or defaults to true value if parameter is not present | Bool | 
|   [memorydb:UserAuthenticationMode](https://docs.aws.amazon.com/memorydb/latest/devguide/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the UserAuthenticationMode.Type parameter in the request | String | 