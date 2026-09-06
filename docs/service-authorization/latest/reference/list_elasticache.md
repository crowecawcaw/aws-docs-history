

# Actions, resources, and condition keys for Amazon ElastiCache
<a name="list_elasticache"></a>

Amazon ElastiCache (service prefix: `elasticache`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elasticache/index.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elasticache/elasticache.json) for this service.

**Topics**
+ [API operations defined by Amazon ElastiCache](#list_elasticache-operations)
+ [Actions defined by Amazon ElastiCache](#list_elasticache-actions-as-permissions)
+ [Permission-only actions for Amazon ElastiCache](#list_elasticache-permission-only-actions)
+ [Resource types defined by Amazon ElastiCache](#list_elasticache-resources-for-iam-policies)
+ [Condition keys for Amazon ElastiCache](#list_elasticache-policy-keys)

## API operations defined by Amazon ElastiCache
<a name="list_elasticache-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_elasticache-actions-as-permissions).




- **   AddTagsToResource  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AuthorizeCacheSecurityGroupIngress  **
  - **IAM action:**  [elasticache:AuthorizeCacheSecurityGroupIngress](#list_elasticache-action-AuthorizeCacheSecurityGroupIngress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchApplyUpdateAction  **
  - **IAM action:**  [elasticache:BatchApplyUpdateAction](#list_elasticache-action-BatchApplyUpdateAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchStopUpdateAction  **
  - **IAM action:**  [elasticache:BatchStopUpdateAction](#list_elasticache-action-BatchStopUpdateAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteMigration  **
  - **IAM action:**  [elasticache:CompleteMigration](#list_elasticache-action-CompleteMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyServerlessCacheSnapshot  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CopyServerlessCacheSnapshot](#list_elasticache-action-CopyServerlessCacheSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopySnapshot  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CopySnapshot](#list_elasticache-action-CopySnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCacheCluster  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateCacheCluster](#list_elasticache-action-CreateCacheCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCacheParameterGroup  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateCacheParameterGroup](#list_elasticache-action-CreateCacheParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCacheSecurityGroup  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateCacheSecurityGroup](#list_elasticache-action-CreateCacheSecurityGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCacheSubnetGroup  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateCacheSubnetGroup](#list_elasticache-action-CreateCacheSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:CreateGlobalReplicationGroup](#list_elasticache-action-CreateGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReplicationGroup  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateReplicationGroup](#list_elasticache-action-CreateReplicationGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateServerlessCache  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateServerlessCache](#list_elasticache-action-CreateServerlessCache)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateServerlessCacheSnapshot  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateServerlessCacheSnapshot](#list_elasticache-action-CreateServerlessCacheSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSnapshot  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateSnapshot](#list_elasticache-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUser  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateUser](#list_elasticache-action-CreateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUserGroup  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:CreateUserGroup](#list_elasticache-action-CreateUserGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DecreaseNodeGroupsInGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:DecreaseNodeGroupsInGlobalReplicationGroup](#list_elasticache-action-DecreaseNodeGroupsInGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DecreaseReplicaCount  **
  - **IAM action:**  [elasticache:DecreaseReplicaCount](#list_elasticache-action-DecreaseReplicaCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCacheCluster  **
  - **IAM action:**  [elasticache:CreateSnapshot](#list_elasticache-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticache:DeleteCacheCluster](#list_elasticache-action-DeleteCacheCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteCacheParameterGroup  **
  - **IAM action:**  [elasticache:DeleteCacheParameterGroup](#list_elasticache-action-DeleteCacheParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCacheSecurityGroup  **
  - **IAM action:**  [elasticache:DeleteCacheSecurityGroup](#list_elasticache-action-DeleteCacheSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCacheSubnetGroup  **
  - **IAM action:**  [elasticache:DeleteCacheSubnetGroup](#list_elasticache-action-DeleteCacheSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:DeleteGlobalReplicationGroup](#list_elasticache-action-DeleteGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationGroup  **
  - **IAM action:**  [elasticache:CreateSnapshot](#list_elasticache-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticache:DeleteReplicationGroup](#list_elasticache-action-DeleteReplicationGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteServerlessCache  **
  - **IAM action:**  [elasticache:CreateServerlessCacheSnapshot](#list_elasticache-action-CreateServerlessCacheSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticache:DeleteServerlessCache](#list_elasticache-action-DeleteServerlessCache)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteServerlessCacheSnapshot  **
  - **IAM action:**  [elasticache:DeleteServerlessCacheSnapshot](#list_elasticache-action-DeleteServerlessCacheSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshot  **
  - **IAM action:**  [elasticache:DeleteSnapshot](#list_elasticache-action-DeleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [elasticache:DeleteUser](#list_elasticache-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserGroup  **
  - **IAM action:**  [elasticache:DeleteUserGroup](#list_elasticache-action-DeleteUserGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCacheClusters  **
  - **IAM action:**  [elasticache:DescribeCacheClusters](#list_elasticache-action-DescribeCacheClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCacheEngineVersions  **
  - **IAM action:**  [elasticache:DescribeCacheEngineVersions](#list_elasticache-action-DescribeCacheEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCacheParameterGroups  **
  - **IAM action:**  [elasticache:DescribeCacheParameterGroups](#list_elasticache-action-DescribeCacheParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCacheParameters  **
  - **IAM action:**  [elasticache:DescribeCacheParameters](#list_elasticache-action-DescribeCacheParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCacheSecurityGroups  **
  - **IAM action:**  [elasticache:DescribeCacheSecurityGroups](#list_elasticache-action-DescribeCacheSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCacheSubnetGroups  **
  - **IAM action:**  [elasticache:DescribeCacheSubnetGroups](#list_elasticache-action-DescribeCacheSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEngineDefaultParameters  **
  - **IAM action:**  [elasticache:DescribeEngineDefaultParameters](#list_elasticache-action-DescribeEngineDefaultParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEvents  **
  - **IAM action:**  [elasticache:DescribeEvents](#list_elasticache-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeGlobalReplicationGroups  **
  - **IAM action:**  [elasticache:DescribeGlobalReplicationGroups](#list_elasticache-action-DescribeGlobalReplicationGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReplicationGroups  **
  - **IAM action:**  [elasticache:DescribeReplicationGroups](#list_elasticache-action-DescribeReplicationGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReservedCacheNodes  **
  - **IAM action:**  [elasticache:DescribeReservedCacheNodes](#list_elasticache-action-DescribeReservedCacheNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReservedCacheNodesOfferings  **
  - **IAM action:**  [elasticache:DescribeReservedCacheNodesOfferings](#list_elasticache-action-DescribeReservedCacheNodesOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeServerlessCacheSnapshots  **
  - **IAM action:**  [elasticache:DescribeServerlessCacheSnapshots](#list_elasticache-action-DescribeServerlessCacheSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeServerlessCaches  **
  - **IAM action:**  [elasticache:DescribeServerlessCaches](#list_elasticache-action-DescribeServerlessCaches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeServiceUpdates  **
  - **IAM action:**  [elasticache:DescribeServiceUpdates](#list_elasticache-action-DescribeServiceUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeSnapshots  **
  - **IAM action:**  [elasticache:DescribeSnapshots](#list_elasticache-action-DescribeSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeUpdateActions  **
  - **IAM action:**  [elasticache:DescribeUpdateActions](#list_elasticache-action-DescribeUpdateActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeUserGroups  **
  - **IAM action:**  [elasticache:DescribeUserGroups](#list_elasticache-action-DescribeUserGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeUsers  **
  - **IAM action:**  [elasticache:DescribeUsers](#list_elasticache-action-DescribeUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:DisassociateGlobalReplicationGroup](#list_elasticache-action-DisassociateGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportServerlessCacheSnapshot  **
  - **IAM action:**  [elasticache:ExportServerlessCacheSnapshot](#list_elasticache-action-ExportServerlessCacheSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:FailoverGlobalReplicationGroup](#list_elasticache-action-FailoverGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   IncreaseNodeGroupsInGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:IncreaseNodeGroupsInGlobalReplicationGroup](#list_elasticache-action-IncreaseNodeGroupsInGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   IncreaseReplicaCount  **
  - **IAM action:**  [elasticache:IncreaseReplicaCount](#list_elasticache-action-IncreaseReplicaCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAllowedNodeTypeModifications  **
  - **IAM action:**  [elasticache:ListAllowedNodeTypeModifications](#list_elasticache-action-ListAllowedNodeTypeModifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [elasticache:ListTagsForResource](#list_elasticache-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyCacheCluster  **
  - **IAM action:**  [elasticache:ModifyCacheCluster](#list_elasticache-action-ModifyCacheCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCacheParameterGroup  **
  - **IAM action:**  [elasticache:ModifyCacheParameterGroup](#list_elasticache-action-ModifyCacheParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCacheSubnetGroup  **
  - **IAM action:**  [elasticache:ModifyCacheSubnetGroup](#list_elasticache-action-ModifyCacheSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:ModifyGlobalReplicationGroup](#list_elasticache-action-ModifyGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyReplicationGroup  **
  - **IAM action:**  [elasticache:ModifyReplicationGroup](#list_elasticache-action-ModifyReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyReplicationGroupShardConfiguration  **
  - **IAM action:**  [elasticache:ModifyReplicationGroupShardConfiguration](#list_elasticache-action-ModifyReplicationGroupShardConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyServerlessCache  **
  - **IAM action:**  [elasticache:ModifyServerlessCache](#list_elasticache-action-ModifyServerlessCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyUser  **
  - **IAM action:**  [elasticache:ModifyUser](#list_elasticache-action-ModifyUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyUserGroup  **
  - **IAM action:**  [elasticache:ModifyUserGroup](#list_elasticache-action-ModifyUserGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PurchaseReservedCacheNodesOffering  **
  - **IAM action:**  [elasticache:AddTagsToResource](#list_elasticache-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticache:PurchaseReservedCacheNodesOffering](#list_elasticache-action-PurchaseReservedCacheNodesOffering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RebalanceSlotsInGlobalReplicationGroup  **
  - **IAM action:**  [elasticache:RebalanceSlotsInGlobalReplicationGroup](#list_elasticache-action-RebalanceSlotsInGlobalReplicationGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootCacheCluster  **
  - **IAM action:**  [elasticache:RebootCacheCluster](#list_elasticache-action-RebootCacheCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **IAM action:**  [elasticache:RemoveTagsFromResource](#list_elasticache-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetCacheParameterGroup  **
  - **IAM action:**  [elasticache:ResetCacheParameterGroup](#list_elasticache-action-ResetCacheParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeCacheSecurityGroupIngress  **
  - **IAM action:**  [elasticache:RevokeCacheSecurityGroupIngress](#list_elasticache-action-RevokeCacheSecurityGroupIngress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMigration  **
  - **IAM action:**  [elasticache:StartMigration](#list_elasticache-action-StartMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestFailover  **
  - **IAM action:**  [elasticache:TestFailover](#list_elasticache-action-TestFailover) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestMigration  **
  - **IAM action:**  [elasticache:TestMigration](#list_elasticache-action-TestMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon ElastiCache
<a name="list_elasticache-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTagsToResource](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_AddTagsToResource.html)  **
  - **Description:** Grants permission to add tags to an ElastiCache resource
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [parametergroup](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [reserved-instance](#list_elasticache-resource-reserved-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [serverlesscache](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [subnetgroup](#list_elasticache-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_elasticache-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [AuthorizeCacheSecurityGroupIngress](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_AuthorizeCacheSecurityGroupIngress.html)  **
  - **Description:** Grants permission to authorize an EC2 security group on a ElastiCache security group
  - **Resource types (\*required):** [securitygroup\*](#list_elasticache-resource-securitygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [BatchApplyUpdateAction](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_BatchApplyUpdateAction.html)  **
  - **Description:** Grants permission to apply ElastiCache service updates to sets of clusters and replication groups
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [BatchStopUpdateAction](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_BatchStopUpdateAction.html)  **
  - **Description:** Grants permission to stop ElastiCache service updates from being executed on a set of clusters
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [CompleteMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CompleteMigration.html)  **
  - **Description:** Grants permission to complete an online migration of data from hosted Redis on Amazon EC2 to ElastiCache
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [Connect](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth-iam.html)  **
  - **Description:** Grants permission to connect as a specified ElastiCache user to an ElastiCache Replication Group or ElastiCache serverless cache
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [serverlesscache](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Access level:** Write

- **   [CopyServerlessCacheSnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CopyServerlessCacheSnapshot.html)  **
  - **Description:** Grants permission to make a copy of an existing serverless cache snapshot
  - **Resource types (\*required):** [serverlesscachesnapshot\*](#list_elasticache-resource-serverlesscachesnapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [CopySnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CopySnapshot.html)  **
  - **Description:** Grants permission to make a copy of an existing snapshot
  - **Resource types (\*required):** [snapshot\*](#list_elasticache-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [CreateCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheCluster.html)  **
  - **Description:** Grants permission to create a cache cluster
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [subnetgroup](#list_elasticache-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheParameterGroup.html)  **
  - **Description:** Grants permission to create a parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Access level:** Write

- **   [CreateCacheSecurityGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSecurityGroup.html)  **
  - **Description:** Grants permission to create a cache security group
  - **Resource types (\*required):** [securitygroup\*](#list_elasticache-resource-securitygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCacheSubnetGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html)  **
  - **Description:** Grants permission to create a cache subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_elasticache-resource-subnetgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to create a global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [CreateReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateReplicationGroup.html)  **
  - **Description:** Grants permission to create a replication group
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [globalreplicationgroup](#list_elasticache-resource-globalreplicationgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [subnetgroup](#list_elasticache-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServerlessCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateServerlessCache.html)  **
  - **Description:** Grants permission to create a serverless cache
  - **Resource types (\*required):** [serverlesscache\*](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServerlessCacheSnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateServerlessCacheSnapshot.html)  **
  - **Description:** Grants permission to create a copy of a serverless cache at a specific moment in time
  - **Resource types (\*required):** [serverlesscache\*](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot\*](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to create a copy of an entire Redis cluster at a specific moment in time
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [snapshot\*](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a user for Redis. Users are supported from Redis 6.0 onwards
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Access level:** Write

- **   [CreateUserGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateUserGroup.html)  **
  - **Description:** Grants permission to create a user group for Redis. Groups are supported from Redis 6.0 onwards
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Resource types (\*required):** [usergroup\*](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [DecreaseNodeGroupsInGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DecreaseNodeGroupsInGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to decrease the number of node groups in global replication groups
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [DecreaseReplicaCount](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DecreaseReplicaCount.html)  **
  - **Description:** Grants permission to decrease the number of replicas in a Redis (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Redis (cluster mode enabled) replication group
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [DeleteCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteCacheCluster.html)  **
  - **Description:** Grants permission to delete a previously provisioned cluster
  - **Resource types (\*required):** [cluster\*](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [DeleteCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteCacheParameterGroup.html)  **
  - **Description:** Grants permission to delete the specified cache parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Access level:** Write

- **   [DeleteCacheSecurityGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteCacheSecurityGroup.html)  **
  - **Description:** Grants permission to delete a cache security group
  - **Resource types (\*required):** [securitygroup\*](#list_elasticache-resource-securitygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCacheSubnetGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteCacheSubnetGroup.html)  **
  - **Description:** Grants permission to delete a cache subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_elasticache-resource-subnetgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to delete an existing global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [DeleteReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteReplicationGroup.html)  **
  - **Description:** Grants permission to delete an existing replication group
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [DeleteServerlessCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteServerlessCache.html)  **
  - **Description:** Grants permission to delete a serverless cache
  - **Resource types (\*required):** [serverlesscache\*](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [DeleteServerlessCacheSnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteServerlessCacheSnapshot.html)  **
  - **Description:** Grants permission to delete a serverless cache snapshot
  - **Resource types (\*required):** [serverlesscachesnapshot\*](#list_elasticache-resource-serverlesscachesnapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [DeleteSnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteSnapshot.html)  **
  - **Description:** Grants permission to delete an existing snapshot
  - **Resource types (\*required):** [snapshot\*](#list_elasticache-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete an existing user and thus remove it from all user groups and replication groups where it was assigned
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Access level:** Write

- **   [DeleteUserGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteUserGroup.html)  **
  - **Description:** Grants permission to delete an existing user group
  - **Resource types (\*required):** [usergroup\*](#list_elasticache-resource-usergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeCacheClusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheClusters.html)  **
  - **Description:** Grants permission to list information about provisioned cache clusters
  - **Resource types (\*required):** [cluster\*](#list_elasticache-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Access level:** List

- **   [DescribeCacheEngineVersions](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheEngineVersions.html)  **
  - **Description:** Grants permission to list available cache engines and their versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeCacheParameterGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheParameterGroups.html)  **
  - **Description:** Grants permission to list cache parameter group descriptions
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Access level:** List

- **   [DescribeCacheParameters](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheParameters.html)  **
  - **Description:** Grants permission to retrieve the detailed parameter list for a particular cache parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Access level:** List

- **   [DescribeCacheSecurityGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheSecurityGroups.html)  **
  - **Description:** Grants permission to list cache security group descriptions
  - **Resource types (\*required):** [securitygroup\*](#list_elasticache-resource-securitygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** List

- **   [DescribeCacheSubnetGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheSubnetGroups.html)  **
  - **Description:** Grants permission to list cache subnet group descriptions
  - **Resource types (\*required):** [subnetgroup\*](#list_elasticache-resource-subnetgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** List

- **   [DescribeEngineDefaultParameters](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEngineDefaultParameters.html)  **
  - **Description:** Grants permission to retrieve the default engine and system parameter information for the specified cache engine
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEvents](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permission to list events related to clusters, cache security groups, and cache parameter groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeGlobalReplicationGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeGlobalReplicationGroups.html)  **
  - **Description:** Grants permission to list information about global replication groups
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** List

- **   [DescribeReplicationGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.html)  **
  - **Description:** Grants permission to list information about provisioned replication groups
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** List

- **   [DescribeReservedCacheNodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReservedCacheNodes.html)  **
  - **Description:** Grants permission to list information about purchased reserved cache nodes
  - **Resource types (\*required):** [reserved-instance\*](#list_elasticache-resource-reserved-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** List

- **   [DescribeReservedCacheNodesOfferings](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReservedCacheNodesOfferings.html)  **
  - **Description:** Grants permission to list available reserved cache node offerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeServerlessCacheSnapshots](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeServerlessCacheSnapshots.html)  **
  - **Description:** Grants permission to list information about serverless cache snapshots
  - **Resource types (\*required):** [serverlesscache](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot\*](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** List

- **   [DescribeServerlessCaches](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeServerlessCaches.html)  **
  - **Description:** Grants permission to list serverless caches
  - **Resource types (\*required):** [serverlesscache\*](#list_elasticache-resource-serverlesscache)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Access level:** List

- **   [DescribeServiceUpdates](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeServiceUpdates.html)  **
  - **Description:** Grants permission to list details of the service updates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeSnapshots](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeSnapshots.html)  **
  - **Description:** Grants permission to list information about cluster or replication group snapshots
  - **Resource types (\*required):** [snapshot\*](#list_elasticache-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** List

- **   [DescribeUpdateActions](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeUpdateActions.html)  **
  - **Description:** Grants permission to list details of the update actions for a set of clusters or replication groups
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** List

- **   [DescribeUserGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeUserGroups.html)  **
  - **Description:** Grants permission to list information about Redis user groups
  - **Resource types (\*required):** [usergroup\*](#list_elasticache-resource-usergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** List

- **   [DescribeUsers](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeUsers.html)  **
  - **Description:** Grants permission to list information about Redis users
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Access level:** List

- **   [DisassociateGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DisassociateGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to remove a secondary replication group from the global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [ExportServerlessCacheSnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ExportServerlessCacheSnapshot.html)  **
  - **Description:** Grants permission to export a copy of a serverless cache at a specific moment in time to s3 bucket
  - **Resource types (\*required):** [serverlesscachesnapshot\*](#list_elasticache-resource-serverlesscachesnapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Access level:** Write

- **   [FailoverGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_FailoverGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to failover the primary region to a selected secondary region of a global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [IncreaseNodeGroupsInGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_IncreaseNodeGroupsInGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to increase the number of node groups in a global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [IncreaseReplicaCount](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_IncreaseReplicaCount.html)  **
  - **Description:** Grants permission to increase the number of replicas in a Redis (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Redis (cluster mode enabled) replication group
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [ListAllowedNodeTypeModifications](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ListAllowedNodeTypeModifications.html)  **
  - **Description:** Grants permission to list available node type that can be used to scale a particular Redis cluster or replication group
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an ElastiCache resource
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [parametergroup](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [reserved-instance](#list_elasticache-resource-reserved-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [serverlesscache](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [subnetgroup](#list_elasticache-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_elasticache-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Read

- **   [ModifyCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html)  **
  - **Description:** Grants permission to modify settings for a cluster
  - **Resource types (\*required):** [cluster\*](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [parametergroup](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [ModifyCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html)  **
  - **Description:** Grants permission to modify parameters of a cache parameter group
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Access level:** Write

- **   [ModifyCacheSubnetGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheSubnetGroup.html)  **
  - **Description:** Grants permission to modify an existing cache subnet group
  - **Resource types (\*required):** [subnetgroup\*](#list_elasticache-resource-subnetgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [ModifyGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to modify settings for a global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [ModifyReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroup.html)  **
  - **Description:** Grants permission to modify the settings for a replication group
  - **Resource types (\*required):** [parametergroup](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [ModifyReplicationGroupShardConfiguration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroupShardConfiguration.html)  **
  - **Description:** Grants permission to add shards, remove shards, or rebalance the keyspaces among existing shards of a replication group
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [ModifyServerlessCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyServerlessCache.html)  **
  - **Description:** Grants permission to modify parameters for a serverless cache
  - **Resource types (\*required):** [serverlesscache\*](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [ModifyUser](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyUser.html)  **
  - **Description:** Grants permission to change Redis user password(s) and/or access string
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Access level:** Write

- **   [ModifyUserGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyUserGroup.html)  **
  - **Description:** Grants permission to change list of users that belong to the user group
  - **Resource types (\*required):** [user\*](#list_elasticache-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Resource types (\*required):** [usergroup\*](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [PurchaseReservedCacheNodesOffering](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_PurchaseReservedCacheNodesOffering.html)  **
  - **Description:** Grants permission to purchase a reserved cache node offering
  - **Resource types (\*required):** [reserved-instance\*](#list_elasticache-resource-reserved-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [RebalanceSlotsInGlobalReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RebalanceSlotsInGlobalReplicationGroup.html)  **
  - **Description:** Grants permission to perform a key space rebalance operation to redistribute slots and ensure uniform key distribution across existing shards in a global replication group
  - **Resource types (\*required):** [globalreplicationgroup\*](#list_elasticache-resource-globalreplicationgroup)
  - **Condition keys:** [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [RebootCacheCluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RebootCacheCluster.html)  **
  - **Description:** Grants permission to reboot some, or all, of the cache nodes within a provisioned cache cluster or replication group (cluster mode disabled)
  - **Resource types (\*required):** [cluster\*](#list_elasticache-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Access level:** Write

- **   [RemoveTagsFromResource](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RemoveTagsFromResource.html)  **
  - **Description:** Grants permission to remove tags from a ElastiCache resource
  - **Resource types (\*required):** [cluster](#list_elasticache-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [parametergroup](#list_elasticache-resource-parametergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Resource types (\*required):** [replicationgroup](#list_elasticache-resource-replicationgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Resource types (\*required):** [reserved-instance](#list_elasticache-resource-reserved-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [securitygroup](#list_elasticache-resource-securitygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [serverlesscache](#list_elasticache-resource-serverlesscache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)
  - **Resource types (\*required):** [serverlesscachesnapshot](#list_elasticache-resource-serverlesscachesnapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [snapshot](#list_elasticache-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)
  - **Resource types (\*required):** [subnetgroup](#list_elasticache-resource-subnetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_elasticache-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode)
  - **Resource types (\*required):** [usergroup](#list_elasticache-resource-usergroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ResetCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ResetCacheParameterGroup.html)  **
  - **Description:** Grants permission to modify parameters of a cache parameter group back to their default values
  - **Resource types (\*required):** [parametergroup\*](#list_elasticache-resource-parametergroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)
  - **Access level:** Write

- **   [RevokeCacheSecurityGroupIngress](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RevokeCacheSecurityGroupIngress.html)  **
  - **Description:** Grants permission to remove an EC2 security group ingress from a ElastiCache security group
  - **Resource types (\*required):** [securitygroup\*](#list_elasticache-resource-securitygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)
  - **Access level:** Write

- **   [StartMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StartMigration.html)  **
  - **Description:** Grants permission to start a migration of data from hosted Redis on Amazon EC2 to ElastiCache for Redis
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [TestFailover](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_TestFailover.html)  **
  - **Description:** Grants permission to test automatic failover on a specified node group in a replication group
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write

- **   [TestMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_TestMigration.html)  **
  - **Description:** Grants permission to test a migration of data from hosted Redis on Amazon EC2 to ElastiCache for Redis
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write



## Permission-only actions for Amazon ElastiCache
<a name="list_elasticache-permission-only-actions"></a>

The following actions are defined by Amazon ElastiCache but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [InterruptClusterAzPower](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#elasticache-actions-reference)  **
  - **Description:** Grants permission to test an AZ power interruption for an ElastiCache resource
  - **Resource types (\*required):** [replicationgroup\*](#list_elasticache-resource-replicationgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled)
  - **Access level:** Write



## Resource types defined by Amazon ElastiCache
<a name="list_elasticache-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.Clusters)  | arn:${Partition}:elasticache:${Region}:${Account}:cluster:${CacheClusterId} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit) | 
|  [globalreplicationgroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Redis-Global-Datastore.html)  | arn:${Partition}:elasticache::${Account}:globalreplicationgroup:${GlobalReplicationGroupId} | [elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled) | 
|  [parametergroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.ParameterGroups)  | arn:${Partition}:elasticache:${Region}:${Account}:parametergroup:${CacheParameterGroupName} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName) | 
|  [replicationgroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.ReplicationGroups)  | arn:${Partition}:elasticache:${Region}:${Account}:replicationgroup:${ReplicationGroupId} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:AtRestEncryptionEnabled](#list_elasticache-elasticache_AtRestEncryptionEnabled)<br />[elasticache:AuthTokenEnabled](#list_elasticache-elasticache_AuthTokenEnabled)<br />[elasticache:AutomaticFailoverEnabled](#list_elasticache-elasticache_AutomaticFailoverEnabled)<br />[elasticache:CacheNodeType](#list_elasticache-elasticache_CacheNodeType)<br />[elasticache:CacheParameterGroupName](#list_elasticache-elasticache_CacheParameterGroupName)<br />[elasticache:ClusterModeEnabled](#list_elasticache-elasticache_ClusterModeEnabled)<br />[elasticache:Durability](#list_elasticache-elasticache_Durability)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MultiAZEnabled](#list_elasticache-elasticache_MultiAZEnabled)<br />[elasticache:NumNodeGroups](#list_elasticache-elasticache_NumNodeGroups)<br />[elasticache:ReplicasPerNodeGroup](#list_elasticache-elasticache_ReplicasPerNodeGroup)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit)<br />[elasticache:TransitEncryptionEnabled](#list_elasticache-elasticache_TransitEncryptionEnabled) | 
|  [reserved-instance](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/reserved-nodes.html)  | arn:${Partition}:elasticache:${Region}:${Account}:reserved-instance:${ReservedCacheNodeId} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys) | 
|  [securitygroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.SecurityGroups)  | arn:${Partition}:elasticache:${Region}:${Account}:securitygroup:${CacheSecurityGroupName} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys) | 
|  [serverlesscache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html)  | arn:${Partition}:elasticache:${Region}:${Account}:serverlesscache:${ServerlessCacheName} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:DataStorageUnit](#list_elasticache-elasticache_DataStorageUnit)<br />[elasticache:EngineType](#list_elasticache-elasticache_EngineType)<br />[elasticache:EngineVersion](#list_elasticache-elasticache_EngineVersion)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId)<br />[elasticache:MaximumDataStorage](#list_elasticache-elasticache_MaximumDataStorage)<br />[elasticache:MaximumECPUPerSecond](#list_elasticache-elasticache_MaximumECPUPerSecond)<br />[elasticache:MinimumDataStorage](#list_elasticache-elasticache_MinimumDataStorage)<br />[elasticache:MinimumECPUPerSecond](#list_elasticache-elasticache_MinimumECPUPerSecond)<br />[elasticache:SnapshotRetentionLimit](#list_elasticache-elasticache_SnapshotRetentionLimit) | 
|  [serverlesscachesnapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html)  | arn:${Partition}:elasticache:${Region}:${Account}:serverlesscachesnapshot:${ServerlessCacheSnapshotName} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId) | 
|  [snapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.Snapshots)  | arn:${Partition}:elasticache:${Region}:${Account}:snapshot:${SnapshotName} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:KmsKeyId](#list_elasticache-elasticache_KmsKeyId) | 
|  [subnetgroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.Components.html#WhatIs.Components.SubnetGroups)  | arn:${Partition}:elasticache:${Region}:${Account}:subnetgroup:${CacheSubnetGroupName} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys) | 
|  [user](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html)  | arn:${Partition}:elasticache:${Region}:${Account}:user:${UserId} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys)<br />[elasticache:UserAuthenticationMode](#list_elasticache-elasticache_UserAuthenticationMode) | 
|  [usergroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html)  | arn:${Partition}:elasticache:${Region}:${Account}:usergroup:${UserGroupId} | [aws:RequestTag/${TagKey}](#list_elasticache-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticache-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticache-aws_TagKeys) | 

## Condition keys for Amazon ElastiCache
<a name="list_elasticache-policy-keys"></a>

Amazon ElastiCache defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the tag keys that are passed in the request | ArrayOfString | 
|   [elasticache:AtRestEncryptionEnabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the AtRestEncryptionEnabled parameter present in the request or default false value if parameter is not present | Bool | 
|   [elasticache:AuthTokenEnabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the presence of non empty AuthToken parameter in the request | Bool | 
|   [elasticache:AutomaticFailoverEnabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the AutomaticFailoverEnabled parameter in the request | Bool | 
|   [elasticache:CacheNodeType](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the cacheNodeType parameter present in the request. This key can be used to restrict which cache node types can be used on cluster creation or scaling operations | String | 
|   [elasticache:CacheParameterGroupName](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the CacheParameterGroupName parameter in the request | String | 
|   [elasticache:ClusterModeEnabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the cluster mode parameter present in the request. Default value for single node group (shard) creations is false | Bool | 
|   [elasticache:DataStorageUnit](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the CacheUsageLimits.DataStorage.Unit parameter in the CreateServerlessCache and ModifyServerlessCache request | String | 
|   [elasticache:Durability](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the Durability parameter in the request. Valid values are default, async, sync, or disabled | String | 
|   [elasticache:EngineType](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the engine type present in creation requests. For replication group creations, default engine 'redis' is used as key if parameter is not present | String | 
|   [elasticache:EngineVersion](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the engineVersion parameter present in creation or cluster modification requests | String | 
|   [elasticache:KmsKeyId](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the Key ID of the KMS key | String | 
|   [elasticache:MaximumDataStorage](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the CacheUsageLimits.DataStorage.Maximum parameter in the CreateServerlessCache and ModifyServerlessCache request | Numeric | 
|   [elasticache:MaximumECPUPerSecond](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the CacheUsageLimits.ECPUPerSecond.Maximum parameter in the CreateServerlessCache and ModifyServerlessCache request | Numeric | 
|   [elasticache:MinimumDataStorage](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the CacheUsageLimits.DataStorage.Minimum parameter in the CreateServerlessCache and ModifyServerlessCache request | Numeric | 
|   [elasticache:MinimumECPUPerSecond](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the CacheUsageLimits.ECPUPerSecond.Minimum parameter in the CreateServerlessCache and ModifyServerlessCache request | Numeric | 
|   [elasticache:MultiAZEnabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the AZMode parameter, MultiAZEnabled parameter or the number of availability zones that the cluster or replication group can be placed in | Bool | 
|   [elasticache:NumNodeGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the NumNodeGroups or NodeGroupCount parameter specified in the request. This key can be used to restrict the number of node groups (shards) clusters can have after creation or scaling operations | Numeric | 
|   [elasticache:ReplicasPerNodeGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the number of replicas per node group (shards) specified in creations or scaling requests | Numeric | 
|   [elasticache:SnapshotRetentionLimit](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the SnapshotRetentionLimit parameter in the request | Numeric | 
|   [elasticache:TransitEncryptionEnabled](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the TransitEncryptionEnabled parameter present in the request. For replication group creations, default value 'false' is used as key if parameter is not present | Bool | 
|   [elasticache:UserAuthenticationMode](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/IAM.ConditionKeys.html#IAM.SpecifyingConditions)  | Filters access by the UserAuthenticationMode parameter in the request | String | 