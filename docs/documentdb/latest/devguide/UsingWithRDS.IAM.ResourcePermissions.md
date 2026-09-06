

# Amazon DocumentDB API permissions: actions, resources, and conditions reference
<a name="UsingWithRDS.IAM.ResourcePermissions"></a>

Use the following sections as a reference when you set up [Using identity-based policies (IAM policies) for Amazon DocumentDB](UsingWithRDS.IAM.AccessControl.IdentityBased.md) and write permissions policies that you can attach to an IAM identity (identity-based policies). 

The following lists each Amazon DocumentDB API operation. Included in the list are the corresponding actions for which you can grant permissions to perform the action, the AWS resource that you can grant the permissions for, and condition keys that you can include for fine-grained access control. You specify the actions in the policy's `Action` field, the resource value in the policy's `Resource` field, and conditions in the policy's `Condition` field. For more information about conditions, see [Specifying conditions in a policy](UsingWithRDS.IAM.AccessControl.Overview.md#SpecifyingIAMPolicyConditions-RDS). 

You can use AWS-wide condition keys in your Amazon DocumentDB policies to express conditions. For a complete list of AWS-wide keys, see [Available Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*. 

You can test IAM policies with the IAM policy simulator. It automatically provides a list of resources and parameters required for each AWS action, including Amazon DocumentDB actions. The IAM policy simulator determines the permissions that are required for each of the actions that you specify. For information about the IAM policy simulator, see [ Testing IAM Policies with the IAM Policy Simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) in the *IAM User Guide*. 

**Note**  
To specify an action, use the `rds:` prefix followed by the API operation name (for example, `rds:CreateDBInstance`).

The following lists Amazon RDS API operations and their related actions, resources, and condition keys.

**Topics**
+ [Amazon DocumentDB actions that support resource-level permissions](#UsingWithRDS.IAM.ResourceLevelPermissions)
+ [Amazon DocumentDB actions that don't support resource-level permissions](#UsingWithRDS.IAM.UnsupportedResourceLevelPermissions)

## Amazon DocumentDB actions that support resource-level permissions
<a name="UsingWithRDS.IAM.ResourceLevelPermissions"></a>

Resource-level permissions provide the ability to specify the resources on which users are allowed to perform actions. Amazon DocumentDB has partial support for resource-level permissions. This means that for certain Amazon DocumentDB actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use. For example, you can grant users permission to modify only specific instances.

The following lists Amazon DocumentDB API operations and their related actions, resources, and condition keys.

**Note**  
For certain management features, Amazon DocumentDB uses operational technology that is shared with Amazon RDS. For more Amazon DocumentDB actions and permissions, refer to [Actions, resources, and condition keys for Amazon RDS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html) in the *Service Authorization Reference*.

<a name="actions-related-to-objects-table"></a>

- **  [AddTagsToResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_AddTagsToResource.html)  `rds:AddTagsToResource`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}` / **Condition Keys:** `rds:db-tag`
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}` / **Condition Keys:** `rds:subgrp-tag`

- **  [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ApplyPendingMaintenanceAction.html)  `rds:ApplyPendingMaintenanceAction`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}`
  - **Condition Keys:** `rds:db-tag`

- **  [CopyDBClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_CopyDBClusterSnapshot.html) `rds:CopyDBClusterSnapshot`**
  - **Resources:** Cluster snapshot<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:{{cluster-snapshot-name}}`
  - **Condition Keys:** `rds:cluster-snapshot-tag`

- **  [CreateDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_CreateDBCluster.html) `rds:CreateDBCluster`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-name}}` / **Condition Keys:** `rds:cluster-tag`
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}` / **Condition Keys:** `rds:cluster-pg-tag`
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}` / **Condition Keys:** `rds:subgrp-tag`

- **  [CreateDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_CreateDBClusterParameterGroup.html) `rds:CreateDBClusterParameterGroup`**
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}`
  - **Condition Keys:** `rds:cluster-pg-tag`

- **  [CreateDBClusterSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_CreateDBClusterSnapshot.html) `rds:CreateDBClusterSnapshot`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-name}}` / **Condition Keys:** `rds:cluster-tag`
  - **Resources:** Cluster snapshot<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:{{cluster-snapshot-name}}` / **Condition Keys:** `rds:cluster-snapshot-tag`

- **  [CreateDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_CreateDBInstance.html) `rds:CreateDBInstance` **
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}` / **Condition Keys:** `rds:DatabaseClass`<br />`rds:db-tag`
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-name}}` / **Condition Keys:** `rds:cluster-tag`

- **  [CreateDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_CreateDBSubnetGroup.html) `rds:CreateDBSubnetGroup`**
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}`
  - **Condition Keys:** `rds:subgrp-tag`

- **  [DeleteDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DeleteDBInstance.html)  `rds:DeleteDBInstance` **
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}`
  - **Condition Keys:** `rds:db-tag`

- **  [DeleteDBSubnetGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DeleteDBSubnetGroup.html) `rds:DeleteDBSubnetGroup`**
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}`
  - **Condition Keys:** `rds:subgrp-tag`

- **  [DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DescribeDBClusterParameterGroups.html) `rds:DescribeDBClusterParameterGroups`**
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}`
  - **Condition Keys:** `rds:cluster-pg-tag`

- **  [DescribeDBClusterParameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DescribeDBClusterParameters.html) `rds:DescribeDBClusterParameters`**
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}`
  - **Condition Keys:** `rds:cluster-pg-tag`

- **  [DescribeDBClusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DescribeDBClusters.html) `rds:DescribeDBClusters`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-instance-name}}`
  - **Condition Keys:** `rds:cluster-tag`

- **  [DescribeDBClusterSnapshotAttributes](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DescribeDBClusterSnapshotAttributes.html) `rds:DescribeDBClusterSnapshotAttributes`**
  - **Resources:** Cluster snapshot<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:{{cluster-snapshot-name}}`
  - **Condition Keys:** `rds:cluster-snapshot-tag`

- **  [DescribeDBSubnetGroups](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DescribeDBSubnetGroups.html) `rds:DescribeDBSubnetGroups`**
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}`
  - **Condition Keys:** `rds:subgrp-tag`

- **  [DescribePendingMaintenanceActions](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_DescribePendingMaintenanceActions.html) `rds:DescribePendingMaintenanceActions`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}`
  - **Condition Keys:** `rds:DatabaseClass`<br />`rds:db-tag`

- **  [FailoverDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_FailoverDBCluster.html) `rds:FailoverDBCluster`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-instance-name}}`
  - **Condition Keys:** `rds:cluster-tag`

- **  [ListTagsForResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ListTagsForResource.html) `rds:ListTagsForResource`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}` / **Condition Keys:** `rds:db-tag`
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}` / **Condition Keys:** `rds:subgrp-tag`

- **  [ModifyDBCluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ModifyDBCluster.html)  `rds:ModifyDBCluster`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-name}}` / **Condition Keys:** `rds:cluster-tag`
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}` / **Condition Keys:** `rds:cluster-pg-tag`

- **  [ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ModifyDBClusterParameterGroup.html) `rds:ModifyDBClusterParameterGroup`**
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}`
  - **Condition Keys:** `rds:cluster-pg-tag`

- **  [ModifyDBClusterSnapshotAttribute](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ModifyDBClusterSnapshotAttribute.html) `rds:ModifyDBClusterSnapshotAttribute`**
  - **Resources:** Cluster snapshot<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:{{cluster-snapshot-name}}`
  - **Condition Keys:** `rds:cluster-snapshot-tag`

- **  [ModifyDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ModifyDBInstance.html) `rds:ModifyDBInstance`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}`
  - **Condition Keys:** `rds:DatabaseClass`<br />`rds:db-tag`

- **  [RebootDBInstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_RebootDBInstance.html) `rds:RebootDBInstance`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}`
  - **Condition Keys:** `rds:db-tag`

- **  [RemoveTagsFromResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_RemoveTagsFromResource.html) `rds:RemoveTagsFromResource`**
  - **Resources:** Instance<br />`arn:aws:rds:{{region}}:{{account-id}}:db:{{db-instance-name}}` / **Condition Keys:** `rds:db-tag`
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}` / **Condition Keys:** `rds:subgrp-tag`

- **  [ResetDBClusterParameterGroup](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_ResetDBClusterParameterGroup.html) `rds:ResetDBClusterParameterGroup`**
  - **Resources:** Cluster parameter group<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-pg:{{cluster-parameter-group-name}}`
  - **Condition Keys:** `rds:cluster-pg-tag`

- **  [RestoreDBClusterFromSnapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_RestoreDBClusterFromSnapshot.html) `rds:RestoreDBClusterFromSnapshot`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-instance-name}}` / **Condition Keys:** `rds:cluster-tag`
  - **Resources:** Cluster snapshot<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:{{cluster-snapshot-name}}` / **Condition Keys:** `rds:cluster-snapshot-tag`

- **  [RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/documentdb/latest/developerguide/api-reference.htmlAPI_RestoreDBClusterToPointInTime.html) `rds:RestoreDBClusterToPointInTime`**
  - **Resources:** Cluster<br />`arn:aws:rds:{{region}}:{{account-id}}:cluster:{{db-cluster-instance-name}}` / **Condition Keys:** `rds:cluster-tag`
  - **Resources:** Subnet group<br />`arn:aws:rds:{{region}}:{{account-id}}:subgrp:{{subnet-group-name}}` / **Condition Keys:** `rds:subgrp-tag`



## Amazon DocumentDB actions that don't support resource-level permissions
<a name="UsingWithRDS.IAM.UnsupportedResourceLevelPermissions"></a>

You can use all Amazon DocumentDB actions in an IAM policy to either grant or deny users permission to use that action. However, not all Amazon DocumentDB actions support resource-level permissions, which enable you to specify the resources on which an action can be performed. The following Amazon DocumentDB API actions currently don't support resource-level permissions. Therefore, to use these actions in an IAM policy, you must grant users permission to use all resources for the action by using a `*` wildcard for the `Resource` element in your statement.
+ `rds:DescribeDBClusterSnapshots`
+ `rds:DescribeDBInstances`