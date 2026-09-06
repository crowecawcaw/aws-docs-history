

# IAM actions for administering Amazon Neptune
<a name="neptune-iam-admin-actions"></a>

You can use the administrative actions listed below in the `Action` element of an IAM policy statement to control access to the [Neptune management APIs](api.md). When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

The `Resource type` field in the list below indicates whether each action supports resource-level permissions. If there is no value in this field, you must specify all resources ("\*") in the `Resource` element of your policy statement. If the column includes a resource type, then you can specify a resource ARN of that type in a statement with that action. Neptune administrative resource types are listed on [this page](iam-admin-resources.md).

Required resources are indicated in the list below with an asterisk (\*). If you specify a resource-level permission ARN in a statement using this action, then it must be of this type. Some actions support multiple resource types. If a resource types is optional (in other words, is not marked with an asterisk), then you do not have to include it.

For more information about the fields listed here, see [action table](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html#actions_table) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

## rds:AddRoleToDBCluster
<a name="neptune-iam-admin-actions-AddRoleToDBCluster"></a>

`AddRoleToDBCluster` associates an IAM role with a Neptune DB cluster.

*Access level:* `Write`.

*Dependent actions:* `iam:PassRole`.

*Resource type:* [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).

## rds:AddSourceIdentifierToSubscription
<a name="neptune-iam-admin-actions-AddSourceIdentifierToSubscription"></a>

`AddSourceIdentifierToSubscription` adds a source identifier to an existing Neptune event notification subscription.

*Access level:* `Write`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:AddTagsToResource
<a name="neptune-iam-admin-actions-AddTagsToResource"></a>

`AddTagsToResource` associates an IAM role with a Neptune DB cluster.

*Access level:* `Write`.

*Resource types:*
+ [db](iam-admin-resources.md#neptune-db-resource)
+ [es](iam-admin-resources.md#neptune-es-resource)
+ [pg](iam-admin-resources.md#neptune-pg-resource)
+ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource)
+ [subgrp](iam-admin-resources.md#neptune-subgrp-resource)

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:ApplyPendingMaintenanceAction
<a name="neptune-iam-admin-actions-ApplyPendingMaintenanceAction"></a>

`ApplyPendingMaintenanceAction` applies a pending maintenance action to a resource.

*Access level:* `Write`.

*Resource type:* [db](iam-admin-resources.md#neptune-db-resource) (required).

## rds:CopyDBClusterParameterGroup
<a name="neptune-iam-admin-actions-CopyDBClusterParameterGroup"></a>

`CopyDBClusterParameterGroup` copies the specified DB cluster parameter group.

*Access level:* `Write`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:CopyDBClusterSnapshot
<a name="neptune-iam-admin-actions-CopyDBClusterSnapshot"></a>

`CopyDBClusterSnapshot` copies a snapshot of a DB cluster.

*Access level:* `Write`.

*Resource type:* [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

## rds:CopyDBParameterGroup
<a name="neptune-iam-admin-actions-CopyDBParameterGroup"></a>

`CopyDBParameterGroup` copies the specified DB parameter group.

*Access level:* `Write`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:CreateDBCluster
<a name="neptune-iam-admin-actions-CreateDBCluster"></a>

`CreateDBCluster` creates a new Neptune DB cluster.

*Access level:* `Tagging`.

*Dependent actions:* `iam:PassRole`.

*Resource types:*
+ [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).
+ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).
+ [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)
+ [neptune-rds\_DatabaseEngine](iam-admin-condition-keys.md#admin-rds_DatabaseEngine)

## rds:CreateDBClusterParameterGroup
<a name="neptune-iam-admin-actions-CreateDBClusterParameterGroup"></a>

`CreateDBClusterParameterGroup` creates a new DB cluster parameter group.

*Access level:* `Tagging`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:CreateDBClusterSnapshot
<a name="neptune-iam-admin-actions-CreateDBClusterSnapshot"></a>

`CreateDBClusterSnapshot` creates a snapshot of a DB cluster.

*Access level:* `Tagging`.

*Resource types:*
+ [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).
+ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:CreateDBInstance
<a name="neptune-iam-admin-actions-CreateDBInstance"></a>

`CreateDBInstance` creates a new DB instance.

*Access level:* `Tagging`.

*Dependent actions:* `iam:PassRole`.

*Resource types:*
+ [db](iam-admin-resources.md#neptune-db-resource) (required).
+ [pg](iam-admin-resources.md#neptune-pg-resource) (required).
+ [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:CreateDBParameterGroup
<a name="neptune-iam-admin-actions-CreateDBParameterGroup"></a>

`CreateDBParameterGroup` creates a new DB parameter group.

*Access level:* `Tagging`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:CreateDBSubnetGroup
<a name="neptune-iam-admin-actions-CreateDBSubnetGroup"></a>

`CreateDBSubnetGroup` creates a new DB subnet group.

*Access level:* `Tagging`.

*Resource type:* [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:CreateEventSubscription
<a name="neptune-iam-admin-actions-CreateEventSubscription"></a>

`CreateEventSubscription` creates a Neptune event notification subscription.

*Access level:* `Tagging`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:DeleteDBCluster
<a name="neptune-iam-admin-actions-DeleteDBCluster"></a>

`DeleteDBCluster` deletes an existing Neptune DB cluster.

*Access level:* `Write`.

*Resource types:*
+ [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).
+ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

## rds:DeleteDBClusterParameterGroup
<a name="neptune-iam-admin-actions-DeleteDBClusterParameterGroup"></a>

`DeleteDBClusterParameterGroup` deletes a specified DB cluster parameter group.

*Access level:* `Write`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:DeleteDBClusterSnapshot
<a name="neptune-iam-admin-actions-DeleteDBClusterSnapshot"></a>

`DeleteDBClusterSnapshot` deletes a DB cluster snapshot.

*Access level:* `Write`.

*Resource type:* [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

## rds:DeleteDBInstance
<a name="neptune-iam-admin-actions-DeleteDBInstance"></a>

`DeleteDBInstance` deletes a specified DB instance.

*Access level:* `Write`.

*Resource type:* [db](iam-admin-resources.md#neptune-db-resource) (required).

## rds:DeleteDBParameterGroup
<a name="neptune-iam-admin-actions-DeleteDBParameterGroup"></a>

`DeleteDBParameterGroup` deletes a specified DBParameterGroup.

*Access level:* `Write`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:DeleteDBSubnetGroup
<a name="neptune-iam-admin-actions-DeleteDBSubnetGroup"></a>

`DeleteDBSubnetGroup` deletes a DB subnet group.

*Access level:* `Write`.

*Resource type:* [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

## rds:DeleteEventSubscription
<a name="neptune-iam-admin-actions-DeleteEventSubscription"></a>

`DeleteEventSubscription` deletes an event notification subscription.

*Access level:* `Write`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:DescribeDBClusterParameterGroups
<a name="neptune-iam-admin-actions-DescribeDBClusterParameterGroups"></a>

`DescribeDBClusterParameterGroups` returns a list of DBClusterParameterGroup descriptions.

*Access level:* `List`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:DescribeDBClusterParameters
<a name="neptune-iam-admin-actions-DescribeDBClusterParameters"></a>

`DescribeDBClusterParameters` returns the detailed parameter list for a particular DB cluster parameter group.

*Access level:* `List`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:DescribeDBClusterSnapshotAttributes
<a name="neptune-iam-admin-actions-DescribeDBClusterSnapshotAttributes"></a>

`DescribeDBClusterSnapshotAttributes` returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.

*Access level:* `List`.

*Resource type:* [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

## rds:DescribeDBClusterSnapshots
<a name="neptune-iam-admin-actions-DescribeDBClusterSnapshots"></a>

`DescribeDBClusterSnapshots` returns information about DB cluster snapshots.

*Access level:* `Read`.

## rds:DescribeDBClusters
<a name="neptune-iam-admin-actions-DescribeDBClusters"></a>

`DescribeDBClusters` returns information about a provisioned Neptune DB cluster.

*Access level:* `List`.

*Resource type:* [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).

## rds:DescribeDBEngineVersions
<a name="neptune-iam-admin-actions-DescribeDBEngineVersions"></a>

`DescribeDBEngineVersions` returns a list of the available DB engines.

*Access level:* `List`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:DescribeDBInstances
<a name="neptune-iam-admin-actions-DescribeDBInstances"></a>

`DescribeDBInstances` returns information about DB instances.

*Access level:* `List`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:DescribeDBParameterGroups
<a name="neptune-iam-admin-actions-DescribeDBParameterGroups"></a>

`DescribeDBParameterGroups` returns a list of DBParameterGroup descriptions.

*Access level:* `List`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:DescribeDBParameters
<a name="neptune-iam-admin-actions-DescribeDBParameters"></a>

`DescribeDBParameters` returns a detailed parameter list for a particular DB parameter group.

*Access level:* `List`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:DescribeDBSubnetGroups
<a name="neptune-iam-admin-actions-DescribeDBSubnetGroups"></a>

`DescribeDBSubnetGroups` returns a list of DBSubnetGroup descriptions.

*Access level:* `List`.

*Resource type:* [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

## rds:DescribeEventCategories
<a name="neptune-iam-admin-actions-DescribeEventCategories"></a>

`DescribeEventCategories` returns a list of categories for all event source types, or, if specified, for a specified source type.

*Access level:* `List`.

## rds:DescribeEventSubscriptions
<a name="neptune-iam-admin-actions-DescribeEventSubscriptions"></a>

`DescribeEventSubscriptions` lists all the subscription descriptions for a customer account.

*Access level:* `List`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:DescribeEvents
<a name="neptune-iam-admin-actions-DescribeEvents"></a>

`DescribeEvents` returns events related to DB instances, DB security groups, and DB parameter groups for the past 14 days.

*Access level:* `List`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:DescribeOrderableDBInstanceOptions
<a name="neptune-iam-admin-actions-DescribeOrderableDBInstanceOptions"></a>

`DescribeOrderableDBInstanceOptions` returns a list of orderable DB instance options for the specified engine.

*Access level:* `List`.

## rds:DescribePendingMaintenanceActions
<a name="neptune-iam-admin-actions-DescribePendingMaintenanceActions"></a>

`DescribePendingMaintenanceActions` returns a list of resources (for example, DB instances) that have at least one pending maintenance action.

*Access level:* `List`.

*Resource type:* [db](iam-admin-resources.md#neptune-db-resource) (required).

## rds:DescribeValidDBInstanceModifications
<a name="neptune-iam-admin-actions-DescribeValidDBInstanceModifications"></a>

`DescribeValidDBInstanceModifications` lists available modifications you can make to your DB instance.

*Access level:* `List`.

*Resource type:* [db](iam-admin-resources.md#neptune-db-resource) (required).

## rds:FailoverDBCluster
<a name="neptune-iam-admin-actions-FailoverDBCluster"></a>

`FailoverDBCluster` forces a failover for a DB cluster.

*Access level:* `Write`.

*Resource type:* [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).

## rds:ListTagsForResource
<a name="neptune-iam-admin-actions-ListTagsForResource"></a>

`ListTagsForResource` lists all tags on a Neptune resource.

*Access level:* `Read`.

*Resource types:*
+ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource)
+ [db](iam-admin-resources.md#neptune-db-resource)
+ [es](iam-admin-resources.md#neptune-es-resource)
+ [pg](iam-admin-resources.md#neptune-pg-resource)
+ [subgrp](iam-admin-resources.md#neptune-subgrp-resource)

## rds:ModifyDBCluster
<a name="neptune-iam-admin-actions-ModifyDBCluster"></a>

`ModifyDBCluster`

Modifies a setting for a Neptune DB cluster.

*Access level:* `Write`.

*Dependent actions:* `iam:PassRole`.

*Resource types:*
+ [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).
+ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:ModifyDBClusterParameterGroup
<a name="neptune-iam-admin-actions-ModifyDBClusterParameterGroup"></a>

`ModifyDBClusterParameterGroup` modifies the parameters of a DB cluster parameter group.

*Access level:* `Write`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:ModifyDBClusterSnapshotAttribute
<a name="neptune-iam-admin-actions-ModifyDBClusterSnapshotAttribute"></a>

`ModifyDBClusterSnapshotAttribute` adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.

*Access level:* `Write`.

*Resource type:* [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

## rds:ModifyDBInstance
<a name="neptune-iam-admin-actions-ModifyDBInstance"></a>

`ModifyDBInstance` modifies settings for a DB instance.

*Access level:* `Write`.

*Dependent actions:* `iam:PassRole`.

*Resource types:*
+ [db](iam-admin-resources.md#neptune-db-resource) (required).
+ [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:ModifyDBParameterGroup
<a name="neptune-iam-admin-actions-ModifyDBParameterGroup"></a>

`ModifyDBParameterGroup` modifies the parameters of a DB parameter group.

*Access level:* `Write`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:ModifyDBSubnetGroup
<a name="neptune-iam-admin-actions-ModifyDBSubnetGroup"></a>

`ModifyDBSubnetGroup` modifies an existing DB subnet group.

*Access level:* `Write`.

*Resource type:* [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

## rds:ModifyEventSubscription
<a name="neptune-iam-admin-actions-ModifyEventSubscription"></a>

`ModifyEventSubscription` modifies an existing Neptune event notification subscription.

*Access level:* `Write`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:RebootDBInstance
<a name="neptune-iam-admin-actions-RebootDBInstance"></a>

`RebootDBInstance` restarts the database engine service for the instance.

*Access level:* `Write`.

*Resource type:* [db](iam-admin-resources.md#neptune-db-resource) (required).

## rds:RemoveRoleFromDBCluster
<a name="neptune-iam-admin-actions-RemoveRoleFromDBCluster"></a>

`RemoveRoleFromDBCluster` disassociates an AWS Identity and Access Management (IAM) role from an Amazon Neptune DB cluster.

*Access level:* `Write`.

*Dependent actions:* `iam:PassRole`.

*Resource type:* [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).

## rds:RemoveSourceIdentifierFromSubscription
<a name="neptune-iam-admin-actions-RemoveSourceIdentifierFromSubscription"></a>

`RemoveSourceIdentifierFromSubscription` removes a source identifier from an existing Neptune event notification subscription.

*Access level:* `Write`.

*Resource type:* [es](iam-admin-resources.md#neptune-es-resource) (required).

## rds:RemoveTagsFromResource
<a name="neptune-iam-admin-actions-RemoveTagsFromResource"></a>

`RemoveTagsFromResource` removes metadata tags from a Neptune resource.

*Access level:* `Tagging`.

*Resource types:*
+ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource)
+ [db](iam-admin-resources.md#neptune-db-resource)
+ [es](iam-admin-resources.md#neptune-es-resource)
+ [pg](iam-admin-resources.md#neptune-pg-resource)
+ [subgrp](iam-admin-resources.md#neptune-subgrp-resource)

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:ResetDBClusterParameterGroup
<a name="neptune-iam-admin-actions-ResetDBClusterParameterGroup"></a>

`ResetDBClusterParameterGroup` modifies the parameters of a DB cluster parameter group to the default value.

*Access level:* `Write`.

*Resource type:* [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource) (required).

## rds:ResetDBParameterGroup
<a name="neptune-iam-admin-actions-ResetDBParameterGroup"></a>

`ResetDBParameterGroup` modifies the parameters of a DB parameter group to the engine/system default value.

*Access level:* `Write`.

*Resource type:* [pg](iam-admin-resources.md#neptune-pg-resource) (required).

## rds:RestoreDBClusterFromSnapshot
<a name="neptune-iam-admin-actions-RestoreDBClusterFromSnapshot"></a>

`RestoreDBClusterFromSnapshot` creates a new DB cluster from a DB cluster snapshot.

*Access level:* `Write`.

*Dependent actions:* `iam:PassRole`.

*Resource types:*
+ [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).
+ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:RestoreDBClusterToPointInTime
<a name="neptune-iam-admin-actions-RestoreDBClusterToPointInTime"></a>

`RestoreDBClusterToPointInTime` restores a DB cluster to an arbitrary point in time.

*Access level:* `Write`.

*Dependent actions:* `iam:PassRole`.

*Resource types:*
+ [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).
+ [subgrp](iam-admin-resources.md#neptune-subgrp-resource) (required).

*Condition Keys:*
+ [aws:RequestTag/{{tag-key}}](iam-admin-condition-keys.md#admin-aws_RequestTag)
+ [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys)

## rds:StartDBCluster
<a name="neptune-iam-admin-actions-StartDBCluster"></a>

`StartDBCluster` starts the specified DB cluster.

*Access level:* `Write`.

*Resource type:* [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).

## rds:StopDBCluster
<a name="neptune-iam-admin-actions-StopDBCluster"></a>

`StopDBCluster` stops the specified DB cluster.

*Access level:* `Write`.

*Resource type:* [cluster](iam-admin-resources.md#neptune-cluster-resource) (required).