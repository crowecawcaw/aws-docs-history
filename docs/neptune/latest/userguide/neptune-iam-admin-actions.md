# IAM actions for administering Amazon Neptune

You can use the administrative actions listed below in the `Action`
element of an IAM policy statement to control access to the [Neptune
management APIs](api.md "api.md"). When you use an action in a policy, you usually allow or deny
access to the API operation or CLI command with the same name. However, in some cases,
a single action controls access to more than one operation. Alternatively, some
operations require several different actions.

The `Resource type` field in the list below indicates whether
each action supports resource-level permissions. If there is no value in this field,
you must specify all resources ("\*") in the `Resource` element of your policy
statement. If the column includes a resource type, then you can specify a resource ARN
of that type in a statement with that action. Neptune administrative resource
types are listed on [this page](iam-admin-resources.md "iam-admin-resources.md").

Required resources are indicated in the list below with an asterisk (\*).
If you specify a resource-level permission ARN in a statement using this action,
then it must be of this type. Some actions support multiple resource types.
If a resource types is optional (in other words, is not marked with an asterisk),
then you do not have to include it.

For more information about the fields listed here, see [action table](../../../IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.md#actions_table "../../../IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.md#actions_table") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## rds:AddRoleToDBCluster

`AddRoleToDBCluster`
associates an IAM role with a Neptune DB cluster.

_Access level:_ `Write`.

_Dependent actions:_ `iam:PassRole`.

_Resource type:_ [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).

## rds:AddSourceIdentifierToSubscription

`AddSourceIdentifierToSubscription`
adds a source identifier to an existing Neptune event notification subscription.

_Access level:_ `Write`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:AddTagsToResource

`AddTagsToResource`
associates an IAM role with a Neptune DB cluster.

_Access level:_ `Write`.

_Resource types:_

- [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource")
- [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource")
- [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource")
- [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource")
- [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource")

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:ApplyPendingMaintenanceAction

`ApplyPendingMaintenanceAction`
applies a pending maintenance action to a resource.

_Access level:_ `Write`.

_Resource type:_ [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).

## rds:CopyDBClusterParameterGroup

`CopyDBClusterParameterGroup`
copies the specified DB cluster parameter group.

_Access level:_ `Write`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:CopyDBClusterSnapshot

`CopyDBClusterSnapshot`
copies a snapshot of a DB cluster.

_Access level:_ `Write`.

_Resource type:_ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

## rds:CopyDBParameterGroup

`CopyDBParameterGroup`
copies the specified DB parameter group.

_Access level:_ `Write`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:CreateDBCluster

`CreateDBCluster`
creates a new Neptune DB cluster.

_Access level:_ `Tagging`.

_Dependent actions:_ `iam:PassRole`.

_Resource types:_

- [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
- [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).
- [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")
- [neptune-rds_DatabaseEngine](iam-admin-condition-keys.md#admin-rds_DatabaseEngine "iam-admin-condition-keys.md#admin-rds_DatabaseEngine")

## rds:CreateDBClusterParameterGroup

`CreateDBClusterParameterGroup`
creates a new DB cluster parameter group.

_Access level:_ `Tagging`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:CreateDBClusterSnapshot

`CreateDBClusterSnapshot`
creates a snapshot of a DB cluster.

_Access level:_ `Tagging`.

_Resource types:_

- [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
- [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:CreateDBInstance

`CreateDBInstance`
creates a new DB instance.

_Access level:_ `Tagging`.

_Dependent actions:_ `iam:PassRole`.

_Resource types:_

- [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).
- [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).
- [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:CreateDBParameterGroup

`CreateDBParameterGroup`
creates a new DB parameter group.

_Access level:_ `Tagging`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:CreateDBSubnetGroup

`CreateDBSubnetGroup`
creates a new DB subnet group.

_Access level:_ `Tagging`.

_Resource type:_ [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:CreateEventSubscription

`CreateEventSubscription`
creates a Neptune event notification subscription.

_Access level:_ `Tagging`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:DeleteDBCluster

`DeleteDBCluster`
deletes an existing Neptune DB cluster.

_Access level:_ `Write`.

_Resource types:_

- [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
- [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

## rds:DeleteDBClusterParameterGroup

`DeleteDBClusterParameterGroup`
deletes a specified DB cluster parameter group.

_Access level:_ `Write`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:DeleteDBClusterSnapshot

`DeleteDBClusterSnapshot`
deletes a DB cluster snapshot.

_Access level:_ `Write`.

_Resource type:_ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

## rds:DeleteDBInstance

`DeleteDBInstance`
deletes a specified DB instance.

_Access level:_ `Write`.

_Resource type:_ [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).

## rds:DeleteDBParameterGroup

`DeleteDBParameterGroup`
deletes a specified DBParameterGroup.

_Access level:_ `Write`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:DeleteDBSubnetGroup

`DeleteDBSubnetGroup`
deletes a DB subnet group.

_Access level:_ `Write`.

_Resource type:_ [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

## rds:DeleteEventSubscription

`DeleteEventSubscription`
deletes an event notification subscription.

_Access level:_ `Write`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:DescribeDBClusterParameterGroups

`DescribeDBClusterParameterGroups`
returns a list of DBClusterParameterGroup descriptions.

_Access level:_ `List`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:DescribeDBClusterParameters

`DescribeDBClusterParameters`
returns the detailed parameter list for a particular DB cluster parameter group.

_Access level:_ `List`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:DescribeDBClusterSnapshotAttributes

`DescribeDBClusterSnapshotAttributes`
returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.

_Access level:_ `List`.

_Resource type:_ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

## rds:DescribeDBClusterSnapshots

`DescribeDBClusterSnapshots`
returns information about DB cluster snapshots.

_Access level:_ `Read`.

## rds:DescribeDBClusters

`DescribeDBClusters`
returns information about a provisioned Neptune DB cluster.

_Access level:_ `List`.

_Resource type:_ [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).

## rds:DescribeDBEngineVersions

`DescribeDBEngineVersions`
returns a list of the available DB engines.

_Access level:_ `List`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:DescribeDBInstances

`DescribeDBInstances`
returns information about DB instances.

_Access level:_ `List`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:DescribeDBParameterGroups

`DescribeDBParameterGroups`
returns a list of DBParameterGroup descriptions.

_Access level:_ `List`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:DescribeDBParameters

`DescribeDBParameters`
returns a detailed parameter list for a particular DB parameter group.

_Access level:_ `List`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:DescribeDBSubnetGroups

`DescribeDBSubnetGroups`
returns a list of DBSubnetGroup descriptions.

_Access level:_ `List`.

_Resource type:_ [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

## rds:DescribeEventCategories

`DescribeEventCategories`
returns a list of categories for all event source types, or, if specified, for a specified source type.

_Access level:_ `List`.

## rds:DescribeEventSubscriptions

`DescribeEventSubscriptions`
lists all the subscription descriptions for a customer account.

_Access level:_ `List`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:DescribeEvents

`DescribeEvents`
returns events related to DB instances, DB security groups, and DB
parameter groups for the past 14 days.

_Access level:_ `List`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:DescribeOrderableDBInstanceOptions

`DescribeOrderableDBInstanceOptions`
returns a list of orderable DB instance options for the specified engine.

_Access level:_ `List`.

## rds:DescribePendingMaintenanceActions

`DescribePendingMaintenanceActions`
returns a list of resources (for example, DB instances) that have at least one pending maintenance action.

_Access level:_ `List`.

_Resource type:_ [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).

## rds:DescribeValidDBInstanceModifications

`DescribeValidDBInstanceModifications`
lists available modifications you can make to your DB instance.

_Access level:_ `List`.

_Resource type:_ [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).

## rds:FailoverDBCluster

`FailoverDBCluster`
forces a failover for a DB cluster.

_Access level:_ `Write`.

_Resource type:_ [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).

## rds:ListTagsForResource

`ListTagsForResource`
lists all tags on a Neptune resource.

_Access level:_ `Read`.

_Resource types:_

- [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource")
- [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource")
- [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource")
- [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource")
- [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource")

## rds:ModifyDBCluster

`ModifyDBCluster`

Modifies a setting for a Neptune DB cluster.

_Access level:_ `Write`.

_Dependent actions:_ `iam:PassRole`.

_Resource types:_

- [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
- [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:ModifyDBClusterParameterGroup

`ModifyDBClusterParameterGroup`
modifies the parameters of a DB cluster parameter group.

_Access level:_ `Write`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:ModifyDBClusterSnapshotAttribute

`ModifyDBClusterSnapshotAttribute`
adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.

_Access level:_ `Write`.

_Resource type:_ [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

## rds:ModifyDBInstance

`ModifyDBInstance`
modifies settings for a DB instance.

_Access level:_ `Write`.

_Dependent actions:_ `iam:PassRole`.

_Resource types:_

- [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).
- [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:ModifyDBParameterGroup

`ModifyDBParameterGroup`
modifies the parameters of a DB parameter group.

_Access level:_ `Write`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:ModifyDBSubnetGroup

`ModifyDBSubnetGroup`
modifies an existing DB subnet group.

_Access level:_ `Write`.

_Resource type:_ [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

## rds:ModifyEventSubscription

`ModifyEventSubscription`
modifies an existing Neptune event notification subscription.

_Access level:_ `Write`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:RebootDBInstance

`RebootDBInstance`
restarts the database engine service for the instance.

_Access level:_ `Write`.

_Resource type:_ [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource") (required).

## rds:RemoveRoleFromDBCluster

`RemoveRoleFromDBCluster`
disassociates an AWS Identity and Access Management (IAM) role from an Amazon Neptune DB cluster.

_Access level:_ `Write`.

_Dependent actions:_ `iam:PassRole`.

_Resource type:_ [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).

## rds:RemoveSourceIdentifierFromSubscription

`RemoveSourceIdentifierFromSubscription`
removes a source identifier from an existing Neptune event notification subscription.

_Access level:_ `Write`.

_Resource type:_ [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource") (required).

## rds:RemoveTagsFromResource

`RemoveTagsFromResource`
removes metadata tags from a Neptune resource.

_Access level:_ `Tagging`.

_Resource types:_

- [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource")
- [db](iam-admin-resources.md#neptune-db-resource "iam-admin-resources.md#neptune-db-resource")
- [es](iam-admin-resources.md#neptune-es-resource "iam-admin-resources.md#neptune-es-resource")
- [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource")
- [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource")

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:ResetDBClusterParameterGroup

`ResetDBClusterParameterGroup`
modifies the parameters of a DB cluster parameter group to the default value.

_Access level:_ `Write`.

_Resource type:_ [cluster-pg](iam-admin-resources.md#neptune-cluster-pg-resource "iam-admin-resources.md#neptune-cluster-pg-resource") (required).

## rds:ResetDBParameterGroup

`ResetDBParameterGroup`
modifies the parameters of a DB parameter group to the engine/system default value.

_Access level:_ `Write`.

_Resource type:_ [pg](iam-admin-resources.md#neptune-pg-resource "iam-admin-resources.md#neptune-pg-resource") (required).

## rds:RestoreDBClusterFromSnapshot

`RestoreDBClusterFromSnapshot`
creates a new DB cluster from a DB cluster snapshot.

_Access level:_ `Write`.

_Dependent actions:_ `iam:PassRole`.

_Resource types:_

- [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
- [cluster-snapshot](iam-admin-resources.md#neptune-cluster-snapshot-resource "iam-admin-resources.md#neptune-cluster-snapshot-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:RestoreDBClusterToPointInTime

`RestoreDBClusterToPointInTime`
restores a DB cluster to an arbitrary point in time.

_Access level:_ `Write`.

_Dependent actions:_ `iam:PassRole`.

_Resource types:_

- [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
- [subgrp](iam-admin-resources.md#neptune-subgrp-resource "iam-admin-resources.md#neptune-subgrp-resource") (required).

_Condition Keys:_

- [aws:RequestTag/tag-key](iam-admin-condition-keys.md#admin-aws_RequestTag "iam-admin-condition-keys.md#admin-aws_RequestTag")
- [aws:TagKeys](iam-admin-condition-keys.md#admin-aws_TagKeys "iam-admin-condition-keys.md#admin-aws_TagKeys")

## rds:StartDBCluster

`StartDBCluster`
starts the specified DB cluster.

_Access level:_ `Write`.

_Resource type:_ [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).

## rds:StopDBCluster

`StopDBCluster`
stops the specified DB cluster.

_Access level:_ `Write`.

_Resource type:_ [cluster](iam-admin-resources.md#neptune-cluster-resource "iam-admin-resources.md#neptune-cluster-resource") (required).
