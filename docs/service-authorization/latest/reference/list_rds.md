

# Actions, resources, and condition keys for Amazon RDS
<a name="list_rds"></a>

Amazon RDS (service prefix: `rds`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rds/rds.json) for this service.

**Topics**
+ [API operations defined by Amazon RDS](#list_rds-operations)
+ [Actions defined by Amazon RDS](#list_rds-actions-as-permissions)
+ [Permission-only actions for Amazon RDS](#list_rds-permission-only-actions)
+ [Resource types defined by Amazon RDS](#list_rds-resources-for-iam-policies)
+ [Condition keys for Amazon RDS](#list_rds-policy-keys)

## API operations defined by Amazon RDS
<a name="list_rds-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rds-actions-as-permissions).




- **   AddSourceIdentifierToSubscription  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddSourceIdentifierToSubscription](#list_rds-action-AddSourceIdentifierToSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTagsToResource  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ApplyPendingMaintenanceAction  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ApplyPendingMaintenanceAction](#list_rds-action-ApplyPendingMaintenanceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyDBClusterParameterGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBClusterParameterGroup](#list_rds-action-CopyDBClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyDBClusterSnapshot  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBClusterSnapshot](#list_rds-action-CopyDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBCluster](#list_rds-action-CreateDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBClusterParameterGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterParameterGroup](#list_rds-action-CreateDBClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBClusterSnapshot  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterSnapshot](#list_rds-action-CreateDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBInstance  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBSubnetGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSubnetGroup](#list_rds-action-CreateDBSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateEventSubscription  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateEventSubscription](#list_rds-action-CreateEventSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGlobalCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateGlobalCluster](#list_rds-action-CreateGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterSnapshot](#list_rds-action-CreateDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBCluster](#list_rds-action-DeleteDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBClusterParameterGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DeleteDBClusterParameterGroup](#list_rds-action-DeleteDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBClusterSnapshot  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DeleteDBClusterSnapshot](#list_rds-action-DeleteDBClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBInstance  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSnapshot](#list_rds-action-CreateDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteTenantDatabase](#list_rds-action-DeleteTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBSubnetGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DeleteDBSubnetGroup](#list_rds-action-DeleteDBSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSubscription  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DeleteEventSubscription](#list_rds-action-DeleteEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlobalCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DeleteGlobalCluster](#list_rds-action-DeleteGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCertificates  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeCertificates](#list_rds-action-DescribeCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterParameterGroups  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBClusterParameterGroups](#list_rds-action-DescribeDBClusterParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterParameters  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBClusterParameters](#list_rds-action-DescribeDBClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterSnapshotAttributes  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBClusterSnapshotAttributes](#list_rds-action-DescribeDBClusterSnapshotAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterSnapshots  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBClusterSnapshots](#list_rds-action-DescribeDBClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusters  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBClusters](#list_rds-action-DescribeDBClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBEngineVersions  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBEngineVersions](#list_rds-action-DescribeDBEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBInstances  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBInstances](#list_rds-action-DescribeDBInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSubnetGroups  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeDBSubnetGroups](#list_rds-action-DescribeDBSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEngineDefaultClusterParameters  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeEngineDefaultClusterParameters](#list_rds-action-DescribeEngineDefaultClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventCategories  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeEventCategories](#list_rds-action-DescribeEventCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventSubscriptions  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeEventSubscriptions](#list_rds-action-DescribeEventSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEvents  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeEvents](#list_rds-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeGlobalClusters  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeGlobalClusters](#list_rds-action-DescribeGlobalClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOrderableDBInstanceOptions  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribeOrderableDBInstanceOptions](#list_rds-action-DescribeOrderableDBInstanceOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePendingMaintenanceActions  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:DescribePendingMaintenanceActions](#list_rds-action-DescribePendingMaintenanceActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   FailoverDBCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:FailoverDBCluster](#list_rds-action-FailoverDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverGlobalCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:FailoverGlobalCluster](#list_rds-action-FailoverGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTagsForResource  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ListTagsForResource](#list_rds-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyDBCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ModifyDBCluster](#list_rds-action-ModifyDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   ModifyDBClusterParameterGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ModifyDBClusterParameterGroup](#list_rds-action-ModifyDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBClusterSnapshotAttribute  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ModifyDBClusterSnapshotAttribute](#list_rds-action-ModifyDBClusterSnapshotAttribute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBInstance  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   ModifyDBSubnetGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ModifyDBSubnetGroup](#list_rds-action-ModifyDBSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyEventSubscription  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ModifyEventSubscription](#list_rds-action-ModifyEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyGlobalCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ModifyGlobalCluster](#list_rds-action-ModifyGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootDBInstance  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:RebootDBInstance](#list_rds-action-RebootDBInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFromGlobalCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:RemoveFromGlobalCluster](#list_rds-action-RemoveFromGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveSourceIdentifierFromSubscription  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:RemoveSourceIdentifierFromSubscription](#list_rds-action-RemoveSourceIdentifierFromSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:RemoveTagsFromResource](#list_rds-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetDBClusterParameterGroup  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:ResetDBClusterParameterGroup](#list_rds-action-ResetDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreDBClusterFromSnapshot  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBClusterFromSnapshot](#list_rds-action-RestoreDBClusterFromSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RestoreDBClusterToPointInTime  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBClusterToPointInTime](#list_rds-action-RestoreDBClusterToPointInTime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   StartDBCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:StartDBCluster](#list_rds-action-StartDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDBCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:StopDBCluster](#list_rds-action-StopDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SwitchoverGlobalCluster  **
  - **SDK client:** docdb
  - **IAM action:**  [rds:SwitchoverGlobalCluster](#list_rds-action-SwitchoverGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddRoleToDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   AddSourceIdentifierToSubscription  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddSourceIdentifierToSubscription](#list_rds-action-AddSourceIdentifierToSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTagsToResource  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ApplyPendingMaintenanceAction  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ApplyPendingMaintenanceAction](#list_rds-action-ApplyPendingMaintenanceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyDBClusterParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBClusterParameterGroup](#list_rds-action-CopyDBClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyDBClusterSnapshot  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBClusterSnapshot](#list_rds-action-CopyDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyDBParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBParameterGroup](#list_rds-action-CopyDBParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBCluster](#list_rds-action-CreateDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBClusterEndpoint  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterEndpoint](#list_rds-action-CreateDBClusterEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBClusterParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterParameterGroup](#list_rds-action-CreateDBClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBClusterSnapshot  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterSnapshot](#list_rds-action-CreateDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBInstance  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBParameterGroup](#list_rds-action-CreateDBParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBSubnetGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSubnetGroup](#list_rds-action-CreateDBSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateEventSubscription  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateEventSubscription](#list_rds-action-CreateEventSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGlobalCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateGlobalCluster](#list_rds-action-CreateGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterSnapshot](#list_rds-action-CreateDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBCluster](#list_rds-action-DeleteDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBClusterEndpoint  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteDBClusterEndpoint](#list_rds-action-DeleteDBClusterEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBClusterParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteDBClusterParameterGroup](#list_rds-action-DeleteDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBClusterSnapshot  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteDBClusterSnapshot](#list_rds-action-DeleteDBClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBInstance  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSnapshot](#list_rds-action-CreateDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteTenantDatabase](#list_rds-action-DeleteTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteDBParameterGroup](#list_rds-action-DeleteDBParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBSubnetGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteDBSubnetGroup](#list_rds-action-DeleteDBSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSubscription  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteEventSubscription](#list_rds-action-DeleteEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlobalCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DeleteGlobalCluster](#list_rds-action-DeleteGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDBClusterEndpoints  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBClusterEndpoints](#list_rds-action-DescribeDBClusterEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterParameterGroups  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBClusterParameterGroups](#list_rds-action-DescribeDBClusterParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterParameters  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBClusterParameters](#list_rds-action-DescribeDBClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterSnapshotAttributes  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBClusterSnapshotAttributes](#list_rds-action-DescribeDBClusterSnapshotAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterSnapshots  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBClusterSnapshots](#list_rds-action-DescribeDBClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusters  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBClusters](#list_rds-action-DescribeDBClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBEngineVersions  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBEngineVersions](#list_rds-action-DescribeDBEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBInstances  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBInstances](#list_rds-action-DescribeDBInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBParameterGroups  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBParameterGroups](#list_rds-action-DescribeDBParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBParameters  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBParameters](#list_rds-action-DescribeDBParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSubnetGroups  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeDBSubnetGroups](#list_rds-action-DescribeDBSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEngineDefaultClusterParameters  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeEngineDefaultClusterParameters](#list_rds-action-DescribeEngineDefaultClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEngineDefaultParameters  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeEngineDefaultParameters](#list_rds-action-DescribeEngineDefaultParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventCategories  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeEventCategories](#list_rds-action-DescribeEventCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventSubscriptions  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeEventSubscriptions](#list_rds-action-DescribeEventSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEvents  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeEvents](#list_rds-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeGlobalClusters  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeGlobalClusters](#list_rds-action-DescribeGlobalClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOrderableDBInstanceOptions  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeOrderableDBInstanceOptions](#list_rds-action-DescribeOrderableDBInstanceOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePendingMaintenanceActions  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribePendingMaintenanceActions](#list_rds-action-DescribePendingMaintenanceActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeValidDBInstanceModifications  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:DescribeValidDBInstanceModifications](#list_rds-action-DescribeValidDBInstanceModifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   FailoverDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:FailoverDBCluster](#list_rds-action-FailoverDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverGlobalCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:FailoverGlobalCluster](#list_rds-action-FailoverGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTagsForResource  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ListTagsForResource](#list_rds-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyDBCluster](#list_rds-action-ModifyDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   ModifyDBClusterEndpoint  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyDBClusterEndpoint](#list_rds-action-ModifyDBClusterEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBClusterParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyDBClusterParameterGroup](#list_rds-action-ModifyDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBClusterSnapshotAttribute  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyDBClusterSnapshotAttribute](#list_rds-action-ModifyDBClusterSnapshotAttribute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBInstance  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   ModifyDBParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyDBParameterGroup](#list_rds-action-ModifyDBParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBSubnetGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyDBSubnetGroup](#list_rds-action-ModifyDBSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyEventSubscription  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyEventSubscription](#list_rds-action-ModifyEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyGlobalCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ModifyGlobalCluster](#list_rds-action-ModifyGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PromoteReadReplicaDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:PromoteReadReplicaDBCluster](#list_rds-action-PromoteReadReplicaDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootDBInstance  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:RebootDBInstance](#list_rds-action-RebootDBInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFromGlobalCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:RemoveFromGlobalCluster](#list_rds-action-RemoveFromGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveRoleFromDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:RemoveRoleFromDBCluster](#list_rds-action-RemoveRoleFromDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RemoveSourceIdentifierFromSubscription  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:RemoveSourceIdentifierFromSubscription](#list_rds-action-RemoveSourceIdentifierFromSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:RemoveTagsFromResource](#list_rds-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetDBClusterParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ResetDBClusterParameterGroup](#list_rds-action-ResetDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetDBParameterGroup  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:ResetDBParameterGroup](#list_rds-action-ResetDBParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreDBClusterFromSnapshot  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBClusterFromSnapshot](#list_rds-action-RestoreDBClusterFromSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RestoreDBClusterToPointInTime  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBClusterToPointInTime](#list_rds-action-RestoreDBClusterToPointInTime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   StartDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:StartDBCluster](#list_rds-action-StartDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDBCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:StopDBCluster](#list_rds-action-StopDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SwitchoverGlobalCluster  **
  - **SDK client:** neptune
  - **IAM action:**  [rds:SwitchoverGlobalCluster](#list_rds-action-SwitchoverGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddRoleToDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   AddRoleToDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddRoleToDBInstance](#list_rds-action-AddRoleToDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   AddSourceIdentifierToSubscription  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddSourceIdentifierToSubscription](#list_rds-action-AddSourceIdentifierToSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTagsToResource  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ApplyPendingMaintenanceAction  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ApplyPendingMaintenanceAction](#list_rds-action-ApplyPendingMaintenanceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AuthorizeDBSecurityGroupIngress  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AuthorizeDBSecurityGroupIngress](#list_rds-action-AuthorizeDBSecurityGroupIngress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   BacktrackDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:BacktrackDBCluster](#list_rds-action-BacktrackDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelExportTask  **
  - **SDK client:** rds
  - **IAM action:**  [rds:CancelExportTask](#list_rds-action-CancelExportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyDBClusterParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBClusterParameterGroup](#list_rds-action-CopyDBClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyDBClusterSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBClusterSnapshot](#list_rds-action-CopyDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyDBParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyDBParameterGroup](#list_rds-action-CopyDBParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyDBSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyCustomDBEngineVersion](#list_rds-action-CopyCustomDBEngineVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CopyDBSnapshot](#list_rds-action-CopyDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyOptionGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CopyOptionGroup](#list_rds-action-CopyOptionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateBlueGreenDeployment  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateBlueGreenDeployment](#list_rds-action-CreateBlueGreenDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBCluster](#list_rds-action-CreateDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBClusterEndpoint](#list_rds-action-CreateDBClusterEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBInstanceReadReplica](#list_rds-action-CreateDBInstanceReadReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateGlobalCluster](#list_rds-action-CreateGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   CreateCustomDBEngineVersion  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateCustomDBEngineVersion](#list_rds-action-CreateCustomDBEngineVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBCluster](#list_rds-action-CreateDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBClusterEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterEndpoint](#list_rds-action-CreateDBClusterEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBClusterParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterParameterGroup](#list_rds-action-CreateDBClusterParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBClusterSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterSnapshot](#list_rds-action-CreateDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBInstanceReadReplica  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstanceReadReplica](#list_rds-action-CreateDBInstanceReadReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   CreateDBParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBParameterGroup](#list_rds-action-CreateDBParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBProxy  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBProxy](#list_rds-action-CreateDBProxy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   CreateDBProxyEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBProxyEndpoint](#list_rds-action-CreateDBProxyEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBSecurityGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSecurityGroup](#list_rds-action-CreateDBSecurityGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBShardGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBShardGroup](#list_rds-action-CreateDBShardGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSnapshot](#list_rds-action-CreateDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDBSubnetGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSubnetGroup](#list_rds-action-CreateDBSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateEventSubscription  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateEventSubscription](#list_rds-action-CreateEventSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGlobalCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateGlobalCluster](#list_rds-action-CreateGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateIntegration  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateIntegration](#list_rds-action-CreateIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateOptionGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateOptionGroup](#list_rds-action-CreateOptionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTenantDatabase  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBlueGreenDeployment  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteBlueGreenDeployment](#list_rds-action-DeleteBlueGreenDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBCluster](#list_rds-action-DeleteDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBClusterEndpoint](#list_rds-action-DeleteDBClusterEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteGlobalCluster](#list_rds-action-DeleteGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:PromoteReadReplica](#list_rds-action-PromoteReadReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:PromoteReadReplicaDBCluster](#list_rds-action-PromoteReadReplicaDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RemoveFromGlobalCluster](#list_rds-action-RemoveFromGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteCustomDBEngineVersion  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteCustomDBEngineVersion](#list_rds-action-DeleteCustomDBEngineVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBClusterSnapshot](#list_rds-action-CreateDBClusterSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBCluster](#list_rds-action-DeleteDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBClusterAutomatedBackup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBClusterAutomatedBackup](#list_rds-action-DeleteDBClusterAutomatedBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBClusterEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBClusterEndpoint](#list_rds-action-DeleteDBClusterEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBClusterParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBClusterParameterGroup](#list_rds-action-DeleteDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBClusterSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBClusterSnapshot](#list_rds-action-DeleteDBClusterSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSnapshot](#list_rds-action-CreateDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteDBInstance](#list_rds-action-DeleteDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteTenantDatabase](#list_rds-action-DeleteTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDBInstanceAutomatedBackup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBInstanceAutomatedBackup](#list_rds-action-DeleteDBInstanceAutomatedBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBParameterGroup](#list_rds-action-DeleteDBParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBProxy  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBProxy](#list_rds-action-DeleteDBProxy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBProxyEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBProxyEndpoint](#list_rds-action-DeleteDBProxyEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBSecurityGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBSecurityGroup](#list_rds-action-DeleteDBSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBShardGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBShardGroup](#list_rds-action-DeleteDBShardGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBSnapshot](#list_rds-action-DeleteDBSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDBSubnetGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteDBSubnetGroup](#list_rds-action-DeleteDBSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSubscription  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteEventSubscription](#list_rds-action-DeleteEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlobalCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteGlobalCluster](#list_rds-action-DeleteGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteIntegration](#list_rds-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOptionGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeleteOptionGroup](#list_rds-action-DeleteOptionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTenantDatabase  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSnapshot](#list_rds-action-CreateDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:DeleteTenantDatabase](#list_rds-action-DeleteTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeregisterDBProxyTargets  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DeregisterDBProxyTargets](#list_rds-action-DeregisterDBProxyTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountAttributes  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeAccountAttributes](#list_rds-action-DescribeAccountAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeBlueGreenDeployments  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeBlueGreenDeployments](#list_rds-action-DescribeBlueGreenDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeCertificates  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeCertificates](#list_rds-action-DescribeCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterAutomatedBackups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterAutomatedBackups](#list_rds-action-DescribeDBClusterAutomatedBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterBacktracks  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterBacktracks](#list_rds-action-DescribeDBClusterBacktracks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterEndpoints  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterEndpoints](#list_rds-action-DescribeDBClusterEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterParameterGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterParameterGroups](#list_rds-action-DescribeDBClusterParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterParameters  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterParameters](#list_rds-action-DescribeDBClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterSnapshotAttributes  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterSnapshotAttributes](#list_rds-action-DescribeDBClusterSnapshotAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusterSnapshots  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusterSnapshots](#list_rds-action-DescribeDBClusterSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBClusters  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBClusters](#list_rds-action-DescribeDBClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBEngineVersions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBEngineVersions](#list_rds-action-DescribeDBEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBInstanceAutomatedBackups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBInstanceAutomatedBackups](#list_rds-action-DescribeDBInstanceAutomatedBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBInstances  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBInstances](#list_rds-action-DescribeDBInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBLogFiles  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBLogFiles](#list_rds-action-DescribeDBLogFiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBMajorEngineVersions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBMajorEngineVersions](#list_rds-action-DescribeDBMajorEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBParameterGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBParameterGroups](#list_rds-action-DescribeDBParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBParameters  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBParameters](#list_rds-action-DescribeDBParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBProxies  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBProxies](#list_rds-action-DescribeDBProxies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBProxyEndpoints  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBProxyEndpoints](#list_rds-action-DescribeDBProxyEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBProxyTargetGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBProxyTargetGroups](#list_rds-action-DescribeDBProxyTargetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBProxyTargets  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBProxyTargets](#list_rds-action-DescribeDBProxyTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBRecommendations  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBRecommendations](#list_rds-action-DescribeDBRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSecurityGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBSecurityGroups](#list_rds-action-DescribeDBSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBShardGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBShardGroups](#list_rds-action-DescribeDBShardGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSnapshotAttributes  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBSnapshotAttributes](#list_rds-action-DescribeDBSnapshotAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSnapshotTenantDatabases  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBSnapshotTenantDatabases](#list_rds-action-DescribeDBSnapshotTenantDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSnapshots  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBSnapshots](#list_rds-action-DescribeDBSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDBSubnetGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeDBSubnetGroups](#list_rds-action-DescribeDBSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEngineDefaultClusterParameters  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeEngineDefaultClusterParameters](#list_rds-action-DescribeEngineDefaultClusterParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEngineDefaultParameters  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeEngineDefaultParameters](#list_rds-action-DescribeEngineDefaultParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventCategories  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeEventCategories](#list_rds-action-DescribeEventCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEventSubscriptions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeEventSubscriptions](#list_rds-action-DescribeEventSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEvents  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeEvents](#list_rds-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeExportTasks  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeExportTasks](#list_rds-action-DescribeExportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeGlobalClusters  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeGlobalClusters](#list_rds-action-DescribeGlobalClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeIntegrations  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeIntegrations](#list_rds-action-DescribeIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOptionGroupOptions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeOptionGroupOptions](#list_rds-action-DescribeOptionGroupOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOptionGroups  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeOptionGroups](#list_rds-action-DescribeOptionGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOrderableDBInstanceOptions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeOrderableDBInstanceOptions](#list_rds-action-DescribeOrderableDBInstanceOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePendingMaintenanceActions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribePendingMaintenanceActions](#list_rds-action-DescribePendingMaintenanceActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReservedDBInstances  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeReservedDBInstances](#list_rds-action-DescribeReservedDBInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReservedDBInstancesOfferings  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeReservedDBInstancesOfferings](#list_rds-action-DescribeReservedDBInstancesOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeSourceRegions  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeSourceRegions](#list_rds-action-DescribeSourceRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTenantDatabases  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeTenantDatabases](#list_rds-action-DescribeTenantDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeValidDBInstanceModifications  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DescribeValidDBInstanceModifications](#list_rds-action-DescribeValidDBInstanceModifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisableHttpEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DisableHttpEndpoint](#list_rds-action-DisableHttpEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DownloadDBLogFilePortion  **
  - **SDK client:** rds
  - **IAM action:**  [rds:DownloadDBLogFilePortion](#list_rds-action-DownloadDBLogFilePortion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   EnableHttpEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:EnableHttpEndpoint](#list_rds-action-EnableHttpEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:FailoverDBCluster](#list_rds-action-FailoverDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverGlobalCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:FailoverGlobalCluster](#list_rds-action-FailoverGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTagsForResource  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ListTagsForResource](#list_rds-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyActivityStream  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyActivityStream](#list_rds-action-ModifyActivityStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCertificates  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyCertificates](#list_rds-action-ModifyCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCurrentDBClusterCapacity  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyCurrentDBClusterCapacity](#list_rds-action-ModifyCurrentDBClusterCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCustomDBEngineVersion  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyCustomDBEngineVersion](#list_rds-action-ModifyCustomDBEngineVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBCluster](#list_rds-action-ModifyDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   ModifyDBClusterEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBClusterEndpoint](#list_rds-action-ModifyDBClusterEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBClusterParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBClusterParameterGroup](#list_rds-action-ModifyDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBClusterSnapshotAttribute  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBClusterSnapshotAttribute](#list_rds-action-ModifyDBClusterSnapshotAttribute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   ModifyDBParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBParameterGroup](#list_rds-action-ModifyDBParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBProxy  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBProxy](#list_rds-action-ModifyDBProxy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   ModifyDBProxyEndpoint  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBProxyEndpoint](#list_rds-action-ModifyDBProxyEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBProxyTargetGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBProxyTargetGroup](#list_rds-action-ModifyDBProxyTargetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBRecommendation  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBRecommendation](#list_rds-action-ModifyDBRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBShardGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBShardGroup](#list_rds-action-ModifyDBShardGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBSnapshot](#list_rds-action-ModifyDBSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBSnapshotAttribute  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBSnapshotAttribute](#list_rds-action-ModifyDBSnapshotAttribute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDBSubnetGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBSubnetGroup](#list_rds-action-ModifyDBSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyEventSubscription  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyEventSubscription](#list_rds-action-ModifyEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyGlobalCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyGlobalCluster](#list_rds-action-ModifyGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyIntegration  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyIntegration](#list_rds-action-ModifyIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyOptionGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyOptionGroup](#list_rds-action-ModifyOptionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   ModifyTenantDatabase  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyTenantDatabase](#list_rds-action-ModifyTenantDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PromoteReadReplica  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:PromoteReadReplica](#list_rds-action-PromoteReadReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PromoteReadReplicaDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:PromoteReadReplicaDBCluster](#list_rds-action-PromoteReadReplicaDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PurchaseReservedDBInstancesOffering  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:PurchaseReservedDBInstancesOffering](#list_rds-action-PurchaseReservedDBInstancesOffering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RebootDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RebootDBCluster](#list_rds-action-RebootDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RebootDBInstance](#list_rds-action-RebootDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RebootDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RebootDBInstance](#list_rds-action-RebootDBInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootDBShardGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RebootDBShardGroup](#list_rds-action-RebootDBShardGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterDBProxyTargets  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RegisterDBProxyTargets](#list_rds-action-RegisterDBProxyTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFromGlobalCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RemoveFromGlobalCluster](#list_rds-action-RemoveFromGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveRoleFromDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RemoveRoleFromDBCluster](#list_rds-action-RemoveRoleFromDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RemoveRoleFromDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RemoveRoleFromDBInstance](#list_rds-action-RemoveRoleFromDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RemoveSourceIdentifierFromSubscription  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RemoveSourceIdentifierFromSubscription](#list_rds-action-RemoveSourceIdentifierFromSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RemoveTagsFromResource](#list_rds-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetDBClusterParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ResetDBClusterParameterGroup](#list_rds-action-ResetDBClusterParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetDBParameterGroup  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ResetDBParameterGroup](#list_rds-action-ResetDBParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreDBClusterFromS3  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:RestoreDBClusterFromS3](#list_rds-action-RestoreDBClusterFromS3)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   RestoreDBClusterFromSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBClusterFromSnapshot](#list_rds-action-RestoreDBClusterFromSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RestoreDBClusterToPointInTime  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddRoleToDBCluster](#list_rds-action-AddRoleToDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBInstance](#list_rds-action-CreateDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBClusterToPointInTime](#list_rds-action-RestoreDBClusterToPointInTime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RestoreDBInstanceFromDBSnapshot  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBInstanceFromDBSnapshot](#list_rds-action-RestoreDBInstanceFromDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   RestoreDBInstanceFromS3  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:RestoreDBInstanceFromS3](#list_rds-action-RestoreDBInstanceFromS3)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   RestoreDBInstanceToPointInTime  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateTenantDatabase](#list_rds-action-CreateTenantDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:RestoreDBInstanceToPointInTime](#list_rds-action-RestoreDBInstanceToPointInTime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds-preview.amazonaws.com, rds.amazonaws.com / **Access level:** Write

- **   RevokeDBSecurityGroupIngress  **
  - **SDK client:** rds
  - **IAM action:**  [rds:RevokeDBSecurityGroupIngress](#list_rds-action-RevokeDBSecurityGroupIngress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartActivityStream  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StartActivityStream](#list_rds-action-StartActivityStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StartDBCluster](#list_rds-action-StartDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StartDBInstance](#list_rds-action-StartDBInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDBInstanceAutomatedBackupsReplication  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:StartDBInstanceAutomatedBackupsReplication](#list_rds-action-StartDBInstanceAutomatedBackupsReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartExportTask  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StartExportTask](#list_rds-action-StartExportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rds.amazonaws.com / **Access level:** Write

- **   StopActivityStream  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StopActivityStream](#list_rds-action-StopActivityStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDBCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StopDBCluster](#list_rds-action-StopDBCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDBInstance  **
  - **SDK client:** rds
  - **IAM action:**  [rds:AddTagsToResource](#list_rds-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [rds:CreateDBSnapshot](#list_rds-action-CreateDBSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:StopDBInstance](#list_rds-action-StopDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StopDBInstanceAutomatedBackupsReplication  **
  - **SDK client:** rds
  - **IAM action:**  [rds:StopDBInstanceAutomatedBackupsReplication](#list_rds-action-StopDBInstanceAutomatedBackupsReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SwitchoverBlueGreenDeployment  **
  - **SDK client:** rds
  - **IAM action:**  [rds:ModifyDBCluster](#list_rds-action-ModifyDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:ModifyDBInstance](#list_rds-action-ModifyDBInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:ModifyGlobalCluster](#list_rds-action-ModifyGlobalCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:PromoteReadReplica](#list_rds-action-PromoteReadReplica)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:PromoteReadReplicaDBCluster](#list_rds-action-PromoteReadReplicaDBCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rds:SwitchoverBlueGreenDeployment](#list_rds-action-SwitchoverBlueGreenDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SwitchoverGlobalCluster  **
  - **SDK client:** rds
  - **IAM action:**  [rds:SwitchoverGlobalCluster](#list_rds-action-SwitchoverGlobalCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SwitchoverReadReplica  **
  - **SDK client:** rds
  - **IAM action:**  [rds:SwitchoverReadReplica](#list_rds-action-SwitchoverReadReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon RDS
<a name="list_rds-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddRoleToDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddRoleToDBCluster.html)  **
  - **Description:** Grants permission to associate an Identity and Access Management (IAM) role from an Aurora DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [AddRoleToDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddRoleToDBInstance.html)  **
  - **Description:** Grants permission to associate an AWS Identity and Access Management (IAM) role with a DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [AddSourceIdentifierToSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddSourceIdentifierToSubscription.html)  **
  - **Description:** Grants permission to add a source identifier to an existing RDS event notification subscription
  - **Resource types (\*required):** [es\*](#list_rds-resource-es)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)
  - **Access level:** Write

- **   [AddTagsToResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddTagsToResource.html)  **
  - **Description:** Grants permission to add metadata tags to an Amazon RDS resource
  - **Resource types (\*required):** [auto-backup](#list_rds-resource-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [cev](#list_rds-resource-cev) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [cluster-auto-backup](#list_rds-resource-cluster-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [cluster-endpoint](#list_rds-resource-cluster-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [cluster-pg](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [deployment](#list_rds-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [es](#list_rds-resource-es) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [global-cluster](#list_rds-resource-global-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [integration](#list_rds-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [proxy](#list_rds-resource-proxy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [proxy-endpoint](#list_rds-resource-proxy-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [ri](#list_rds-resource-ri) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:ri-tag/${TagKey}](#list_rds-rds_ri-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [shardgrp](#list_rds-resource-shardgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [snapshot-tenant-database](#list_rds-resource-snapshot-tenant-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [subgrp](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [target-group](#list_rds-resource-target-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Resource types (\*required):** [tenant-database](#list_rds-resource-tenant-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TagsFromRequest](#list_rds-rds_TagsFromRequest)
  - **Access level:** Tagging, Write

- **   [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ApplyPendingMaintenanceAction.html)  **
  - **Description:** Grants permission to apply a pending maintenance action to a resource
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [AuthorizeDBSecurityGroupIngress](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AuthorizeDBSecurityGroupIngress.html)  **
  - **Description:** Grants permission to enable ingress to a DBSecurityGroup using one of two forms of authorization
  - **Resource types (\*required):** [secgrp\*](#list_rds-resource-secgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [BacktrackDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_BacktrackDBCluster.html)  **
  - **Description:** Grants permission to backtrack a DB cluster to a specific time, without creating a new DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [CancelExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CancelExportTask.html)  **
  - **Description:** Grants permission to cancel an export task in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CopyDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBClusterParameterGroup.html)  **
  - **Description:** Grants permission to copy the specified DB cluster parameter group
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CopyDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBClusterSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot of a DB cluster
  - **Resource types (\*required):** [cluster-snapshot\*](#list_rds-resource-cluster-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CopyDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBParameterGroup.html)  **
  - **Description:** Grants permission to copy the specified DB parameter group
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CopyDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBSnapshot.html)  **
  - **Description:** Grants permission to copy the specified DB snapshot
  - **Resource types (\*required):** [snapshot\*](#list_rds-resource-snapshot)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:CopyOptionGroup](#list_rds-rds_CopyOptionGroup)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [CopyOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyOptionGroup.html)  **
  - **Description:** Grants permission to copy the specified option group
  - **Resource types (\*required):** [og\*](#list_rds-resource-og)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateBlueGreenDeployment](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateBlueGreenDeployment.html)  **
  - **Description:** Grants permission to create a blue-green deployment for a given source cluster or instance
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [cluster-pg](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [deployment\*](#list_rds-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [CreateCustomDBEngineVersion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateCustomDBEngineVersion.html)  **
  - **Description:** Grants permission to create a custom engine version
  - **Resource types (\*required):** [cev\*](#list_rds-resource-cev)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html)  **
  - **Description:** Grants permission to create a new DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [global-cluster](#list_rds-resource-global-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterEndpoint.html)  **
  - **Description:** Grants permission to create a new custom endpoint and associates it with an Amazon Aurora DB cluster or Amazon DocumentDB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:EndpointType](#list_rds-rds_EndpointType)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster-endpoint\*](#list_rds-resource-cluster-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:EndpointType](#list_rds-rds_EndpointType)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterParameterGroup.html)  **
  - **Description:** Grants permission to create a new DB cluster parameter group
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot of a DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot\*](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html)  **
  - **Description:** Grants permission to create a new DB instance
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Resource types (\*required):** [subgrp](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html)  **
  - **Description:** Grants permission to create a DB instance that acts as a Read Replica of a source DB instance
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBParameterGroup.html)  **
  - **Description:** Grants permission to create a new DB parameter group
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBProxy.html)  **
  - **Description:** Grants permission to create a database proxy
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBProxyEndpoint.html)  **
  - **Description:** Grants permission to create a database proxy endpoint
  - **Resource types (\*required):** [proxy\*](#list_rds-resource-proxy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)
  - **Resource types (\*required):** [proxy-endpoint\*](#list_rds-resource-proxy-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDBSecurityGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSecurityGroup.html)  **
  - **Description:** Grants permission to create a new DB security group. DB security groups control access to a DB instance
  - **Resource types (\*required):** [secgrp\*](#list_rds-resource-secgrp)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBShardGroup.html)  **
  - **Description:** Grants permission to create a new Aurora Limitless Database DB shard group
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [shardgrp\*](#list_rds-resource-shardgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSnapshot.html)  **
  - **Description:** Grants permission to create a DBSnapshot
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [snapshot\*](#list_rds-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDBSubnetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSubnetGroup.html)  **
  - **Description:** Grants permission to create a new DB subnet group
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateEventSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateEventSubscription.html)  **
  - **Description:** Grants permission to create an RDS event notification subscription
  - **Resource types (\*required):** [es\*](#list_rds-resource-es)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateGlobalCluster.html)  **
  - **Description:** Grants permission to create an Aurora global database or DocumentDB global database spread across multiple regions
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [global-cluster\*](#list_rds-resource-global-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateIntegration.html)  **
  - **Description:** Grants permission to create an Aurora zero-ETL integration with Redshift
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [integration\*](#list_rds-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateOptionGroup.html)  **
  - **Description:** Grants permission to create a new option group
  - **Resource types (\*required):** [og\*](#list_rds-resource-og)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateTenantDatabase](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateTenantDatabase.html)  **
  - **Description:** Grants permission to create a new tenant database
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:TenantDatabaseName](#list_rds-rds_TenantDatabaseName)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [tenant-database\*](#list_rds-resource-tenant-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:TenantDatabaseName](#list_rds-rds_TenantDatabaseName)
  - **Access level:** Write

- **   [DeleteBlueGreenDeployment](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteBlueGreenDeployment.html)  **
  - **Description:** Grants permission to delete blue green deployments
  - **Resource types (\*required):** [deployment\*](#list_rds-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomDBEngineVersion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteCustomDBEngineVersion.html)  **
  - **Description:** Grants permission to delete an existing custom engine version
  - **Resource types (\*required):** [cev\*](#list_rds-resource-cev)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBCluster.html)  **
  - **Description:** Grants permission to delete a previously provisioned DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot\*](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBClusterAutomatedBackup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterAutomatedBackup.html)  **
  - **Description:** Grants permission to delete cluster automated backups based on the source cluster's DbClusterResourceId value or the restorable cluster's resource ID
  - **Resource types (\*required):** [cluster-auto-backup\*](#list_rds-resource-cluster-auto-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterEndpoint.html)  **
  - **Description:** Grants permission to delete a custom endpoint and removes it from an Amazon Aurora DB cluster or Amazon DocumentDB cluster
  - **Resource types (\*required):** [cluster-endpoint\*](#list_rds-resource-cluster-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterParameterGroup.html)  **
  - **Description:** Grants permission to delete a specified DB cluster parameter group
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterSnapshot.html)  **
  - **Description:** Grants permission to delete a DB cluster snapshot
  - **Resource types (\*required):** [cluster-snapshot\*](#list_rds-resource-cluster-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBInstance.html)  **
  - **Description:** Grants permission to delete a previously provisioned DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [DeleteDBInstanceAutomatedBackup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBInstanceAutomatedBackup.html)  **
  - **Description:** Grants permission to delete automated backups based on the source instance's DbiResourceId value or the restorable instance's resource ID
  - **Resource types (\*required):** [auto-backup\*](#list_rds-resource-auto-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBParameterGroup.html)  **
  - **Description:** Grants permission to delete a specified DBParameterGroup
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBProxy.html)  **
  - **Description:** Grants permission to delete a database proxy
  - **Resource types (\*required):** [proxy\*](#list_rds-resource-proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBProxyEndpoint.html)  **
  - **Description:** Grants permission to delete a database proxy endpoint
  - **Resource types (\*required):** [proxy-endpoint\*](#list_rds-resource-proxy-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBSecurityGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBSecurityGroup.html)  **
  - **Description:** Grants permission to delete a DB security group
  - **Resource types (\*required):** [secgrp\*](#list_rds-resource-secgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBShardGroup.html)  **
  - **Description:** Grants permission to delete an Aurora Limitless Database DB shard group
  - **Resource types (\*required):** [shardgrp\*](#list_rds-resource-shardgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBSnapshot.html)  **
  - **Description:** Grants permission to delete a DBSnapshot
  - **Resource types (\*required):** [snapshot\*](#list_rds-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDBSubnetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBSubnetGroup.html)  **
  - **Description:** Grants permission to delete a DB subnet group
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteEventSubscription.html)  **
  - **Description:** Grants permission to delete an RDS event notification subscription
  - **Resource types (\*required):** [es\*](#list_rds-resource-es)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteGlobalCluster.html)  **
  - **Description:** Grants permission to delete a global database cluster
  - **Resource types (\*required):** [global-cluster\*](#list_rds-resource-global-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete an Aurora zero-ETL integration with Redshift
  - **Resource types (\*required):** [integration\*](#list_rds-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteOptionGroup.html)  **
  - **Description:** Grants permission to delete an existing option group
  - **Resource types (\*required):** [og\*](#list_rds-resource-og)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteTenantDatabase](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteTenantDatabase.html)  **
  - **Description:** Grants permission to delete a tenant database
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [tenant-database\*](#list_rds-resource-tenant-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeregisterDBProxyTargets.html)  **
  - **Description:** Grants permission to remove targets from a database proxy target group
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [proxy\*](#list_rds-resource-proxy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [target-group\*](#list_rds-resource-target-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeAccountAttributes.html)  **
  - **Description:** Grants permission to list all of the attributes for a customer account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeBlueGreenDeployments](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeBlueGreenDeployments.html)  **
  - **Description:** Grants permission to describe blue green deployments
  - **Resource types (\*required):** [deployment](#list_rds-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeCertificates.html)  **
  - **Description:** Grants permission to list the set of CA certificates provided by Amazon RDS for this AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDBClusterAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterAutomatedBackups.html)  **
  - **Description:** Grants permission to return a list of cluster automated backups for both current and deleted clusters
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-auto-backup](#list_rds-resource-cluster-auto-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusterBacktracks](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterBacktracks.html)  **
  - **Description:** Grants permission to return information about backtracks for a DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusterEndpoints](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterEndpoints.html)  **
  - **Description:** Grants permission to return information about endpoints for an Amazon Aurora DB cluster
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-endpoint](#list_rds-resource-cluster-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterParameterGroups.html)  **
  - **Description:** Grants permission to return a list of DBClusterParameterGroup descriptions
  - **Resource types (\*required):** [cluster-pg](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusterParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterParameters.html)  **
  - **Description:** Grants permission to return the detailed parameter list for a particular DB cluster parameter group
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusterSnapshotAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterSnapshotAttributes.html)  **
  - **Description:** Grants permission to return a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot
  - **Resource types (\*required):** [cluster-snapshot\*](#list_rds-resource-cluster-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusterSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterSnapshots.html)  **
  - **Description:** Grants permission to return information about DB cluster snapshots
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html)  **
  - **Description:** Grants permission to return information about provisioned Aurora DB clusters or DocumentDB clusters
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBEngineVersions.html)  **
  - **Description:** Grants permission to return a list of the available DB engines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDBInstanceAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstanceAutomatedBackups.html)  **
  - **Description:** Grants permission to return a list of automated backups for both current and deleted instances
  - **Resource types (\*required):** [auto-backup](#list_rds-resource-auto-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** List

- **   [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)  **
  - **Description:** Grants permission to return information about provisioned RDS instances
  - **Resource types (\*required):** [db](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** List

- **   [DescribeDBLogFiles](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBLogFiles.html)  **
  - **Description:** Grants permission to return a list of DB log files for the DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** List

- **   [DescribeDBMajorEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBMajorEngineVersions.html)  **
  - **Description:** Grants permission to return information specific for each DB major engine versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDBParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameterGroups.html)  **
  - **Description:** Grants permission to return a list of DBParameterGroup descriptions
  - **Resource types (\*required):** [pg](#list_rds-resource-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameters.html)  **
  - **Description:** Grants permission to return the detailed parameter list for a particular DB parameter group
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBProxies](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxies.html)  **
  - **Description:** Grants permission to view proxies
  - **Resource types (\*required):** [proxy](#list_rds-resource-proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBProxyEndpoints](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyEndpoints.html)  **
  - **Description:** Grants permission to view proxy endpoints
  - **Resource types (\*required):** [proxy](#list_rds-resource-proxy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [proxy-endpoint](#list_rds-resource-proxy-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBProxyTargetGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyTargetGroups.html)  **
  - **Description:** Grants permission to view database proxy target group details
  - **Resource types (\*required):** [proxy\*](#list_rds-resource-proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyTargets.html)  **
  - **Description:** Grants permission to view database proxy target details
  - **Resource types (\*required):** [proxy\*](#list_rds-resource-proxy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [target-group\*](#list_rds-resource-target-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBRecommendations](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBRecommendations.html)  **
  - **Description:** Grants permission to list recommendation details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDBSecurityGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSecurityGroups.html)  **
  - **Description:** Grants permission to return a list of DBSecurityGroup descriptions
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBShardGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBShardGroups.html)  **
  - **Description:** Grants permission to return information about all Aurora Limitless Database DB shard groups for this account. You can filter by shard group(s)
  - **Resource types (\*required):** [shardgrp](#list_rds-resource-shardgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBSnapshotAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshotAttributes.html)  **
  - **Description:** Grants permission to return a list of DB snapshot attribute names and values for a manual DB snapshot
  - **Resource types (\*required):** [snapshot\*](#list_rds-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBSnapshotTenantDatabases](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshotTenantDatabases.html)  **
  - **Description:** Grants permission to return information about tenant databases in DB snapshots. You can filter by Region or snapshot
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Resource types (\*required):** [snapshot-tenant-database](#list_rds-resource-snapshot-tenant-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDBSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshots.html)  **
  - **Description:** Grants permission to return information about DB snapshots
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** List

- **   [DescribeDBSubnetGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSubnetGroups.html)  **
  - **Description:** Grants permission to return a list of DBSubnetGroup descriptions
  - **Resource types (\*required):** [subgrp](#list_rds-resource-subgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** List

- **   [DescribeEngineDefaultClusterParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEngineDefaultClusterParameters.html)  **
  - **Description:** Grants permission to return the default engine and system parameter information for the cluster database engine
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEngineDefaultParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEngineDefaultParameters.html)  **
  - **Description:** Grants permission to return the default engine and system parameter information for the specified database engine
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEventCategories](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventCategories.html)  **
  - **Description:** Grants permission to display a list of categories for all event source types, or, if specified, for a specified source type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEventSubscriptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventSubscriptions.html)  **
  - **Description:** Grants permission to list all the subscription descriptions for a customer account
  - **Resource types (\*required):** [es](#list_rds-resource-es)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)
  - **Access level:** List

- **   [DescribeEvents](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permission to return events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeExportTasks](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeExportTasks.html)  **
  - **Description:** Grants permission to return information about the export tasks
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** List

- **   [DescribeGlobalClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeGlobalClusters.html)  **
  - **Description:** Grants permission to return information about Aurora global database clusters or DocumentDB global database clusters
  - **Resource types (\*required):** [global-cluster](#list_rds-resource-global-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeIntegrations](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeIntegrations.html)  **
  - **Description:** Grants permission to describe an Aurora zero-ETL integration with Redshift
  - **Resource types (\*required):** [integration](#list_rds-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeOptionGroupOptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOptionGroupOptions.html)  **
  - **Description:** Grants permission to describe all available options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOptionGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOptionGroups.html)  **
  - **Description:** Grants permission to describe the available option groups
  - **Resource types (\*required):** [og](#list_rds-resource-og)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)
  - **Access level:** List

- **   [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOrderableDBInstanceOptions.html)  **
  - **Description:** Grants permission to return a list of orderable DB instance options for the specified engine
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePendingMaintenanceActions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribePendingMaintenanceActions.html)  **
  - **Description:** Grants permission to return a list of resources (for example, DB instances) that have at least one pending maintenance action
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** List

- **   [DescribeReservedDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstances.html)  **
  - **Description:** Grants permission to return information about reserved DB instances for this account, or about a specified reserved DB instance
  - **Resource types (\*required):** [ri](#list_rds-resource-ri)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ri-tag/${TagKey}](#list_rds-rds_ri-tag___TagKey_)
  - **Access level:** List

- **   [DescribeReservedDBInstancesOfferings](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstancesOfferings.html)  **
  - **Description:** Grants permission to list available reserved DB instance offerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeSourceRegions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeSourceRegions.html)  **
  - **Description:** Grants permission to return a list of the source AWS Regions where the current AWS Region can create a Read Replica or copy a DB snapshot from
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTenantDatabases](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeTenantDatabases.html)  **
  - **Description:** Grants permission to return information about provisioned tenant databases. You can filter by Region or snapshot
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [tenant-database](#list_rds-resource-tenant-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeValidDBInstanceModifications](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeValidDBInstanceModifications.html)  **
  - **Description:** Grants permission to list available modifications you can make to your DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** List

- **   [DisableHttpEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DisableHttpEndpoint.html)  **
  - **Description:** Grants permission to disable http endpoint for a DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [DownloadCompleteDBLogFile](https://docs.aws.amazon.com/AmazonRDS/latest/USER_LogAccess.html)  **
  - **Description:** Grants permission to download specified log file
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Read

- **   [DownloadDBLogFilePortion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DownloadDBLogFilePortion.html)  **
  - **Description:** Grants permission to download all or a portion of the specified log file, up to 1 MB in size
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Read

- **   [EnableHttpEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_EnableHttpEndpoint.html)  **
  - **Description:** Grants permission to enable http endpoint for a DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [FailoverDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_FailoverDBCluster.html)  **
  - **Description:** Grants permission to force a failover for a DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [FailoverGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_FailoverGlobalCluster.html)  **
  - **Description:** Grants permission to failover a global cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [global-cluster\*](#list_rds-resource-global-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags on an Amazon RDS resource
  - **Resource types (\*required):** [auto-backup](#list_rds-resource-auto-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cev](#list_rds-resource-cev) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-auto-backup](#list_rds-resource-cluster-auto-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster-endpoint](#list_rds-resource-cluster-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster-pg](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [es](#list_rds-resource-es) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)
  - **Resource types (\*required):** [global-cluster](#list_rds-resource-global-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integration](#list_rds-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Resource types (\*required):** [proxy](#list_rds-resource-proxy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [proxy-endpoint](#list_rds-resource-proxy-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ri](#list_rds-resource-ri) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ri-tag/${TagKey}](#list_rds-rds_ri-tag___TagKey_)
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Resource types (\*required):** [shardgrp](#list_rds-resource-shardgrp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Resource types (\*required):** [snapshot-tenant-database](#list_rds-resource-snapshot-tenant-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subgrp](#list_rds-resource-subgrp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Resource types (\*required):** [target-group](#list_rds-resource-target-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tenant-database](#list_rds-resource-tenant-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ModifyActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyActivityStream.html)  **
  - **Description:** Grants permission to modify a database activity stream
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [ModifyCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyCertificates.html)  **
  - **Description:** Grants permission to modify the system-default Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificate for Amazon RDS for new DB instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyCurrentDBClusterCapacity](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyCurrentDBClusterCapacity.html)  **
  - **Description:** Grants permission to modify current cluster capacity for an Amazon Aurora Serverless DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyCustomDBEngineVersion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyCustomDBEngineVersion.html)  **
  - **Description:** Grants permission to modify an existing custom engine version
  - **Resource types (\*required):** [cev\*](#list_rds-resource-cev)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html)  **
  - **Description:** Grants permission to modify a setting for an Amazon Aurora DB cluster or Amazon DocumentDB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [cluster-pg](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Access level:** Write

- **   [ModifyDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterEndpoint.html)  **
  - **Description:** Grants permission to modify the properties of an endpoint in an Amazon Aurora DB cluster or Amazon DocumentDB cluster
  - **Resource types (\*required):** [cluster-endpoint\*](#list_rds-resource-cluster-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterParameterGroup.html)  **
  - **Description:** Grants permission to modify the parameters of a DB cluster parameter group
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBClusterSnapshotAttribute](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterSnapshotAttribute.html)  **
  - **Description:** Grants permission to add an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot
  - **Resource types (\*required):** [cluster-snapshot\*](#list_rds-resource-cluster-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html)  **
  - **Description:** Grants permission to modify settings for a DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Resource types (\*required):** [subgrp](#list_rds-resource-subgrp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBParameterGroup.html)  **
  - **Description:** Grants permission to modify the parameters of a DB parameter group
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxy.html)  **
  - **Description:** Grants permission to modify database proxy
  - **Resource types (\*required):** [proxy\*](#list_rds-resource-proxy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxyEndpoint.html)  **
  - **Description:** Grants permission to modify database proxy endpoint
  - **Resource types (\*required):** [proxy-endpoint\*](#list_rds-resource-proxy-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBProxyTargetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxyTargetGroup.html)  **
  - **Description:** Grants permission to modify target group for a database proxy
  - **Resource types (\*required):** [target-group\*](#list_rds-resource-target-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBRecommendation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBRecommendation.html)  **
  - **Description:** Grants permission to modify recommendation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBShardGroup.html)  **
  - **Description:** Grants permission to modify properties of an Aurora Limitless Database DB shard group
  - **Resource types (\*required):** [shardgrp\*](#list_rds-resource-shardgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshot.html)  **
  - **Description:** Grants permission to update a manual DB snapshot, which can be encrypted or not encrypted, with a new engine version
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)
  - **Resource types (\*required):** [snapshot\*](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBSnapshotAttribute](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshotAttribute.html)  **
  - **Description:** Grants permission to add an attribute and values to, or removes an attribute and values from, a manual DB snapshot
  - **Resource types (\*required):** [snapshot\*](#list_rds-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyDBSubnetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSubnetGroup.html)  **
  - **Description:** Grants permission to modify an existing DB subnet group
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyEventSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyEventSubscription.html)  **
  - **Description:** Grants permission to modify an existing RDS event notification subscription
  - **Resource types (\*required):** [es\*](#list_rds-resource-es)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyGlobalCluster.html)  **
  - **Description:** Grants permission to modify a setting for an Amazon Aurora global cluster or Amazon DocumentDB global cluster
  - **Resource types (\*required):** [global-cluster\*](#list_rds-resource-global-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyIntegration.html)  **
  - **Description:** Grants permission to modify an Aurora zero-ETL integration with Redshift
  - **Resource types (\*required):** [integration\*](#list_rds-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyOptionGroup.html)  **
  - **Description:** Grants permission to modify an existing option group
  - **Resource types (\*required):** [og\*](#list_rds-resource-og)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyTenantDatabase](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyTenantDatabase.html)  **
  - **Description:** Grants permission to modify a tenant database
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:TenantDatabaseName](#list_rds-rds_TenantDatabaseName)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [tenant-database\*](#list_rds-resource-tenant-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:TenantDatabaseName](#list_rds-rds_TenantDatabaseName)
  - **Access level:** Write

- **   [PromoteReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PromoteReadReplica.html)  **
  - **Description:** Grants permission to promote a Read Replica DB instance to a standalone DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [PromoteReadReplicaDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PromoteReadReplicaDBCluster.html)  **
  - **Description:** Grants permission to promote a Read Replica DB cluster to a standalone DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [PurchaseReservedDBInstancesOffering](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PurchaseReservedDBInstancesOffering.html)  **
  - **Description:** Grants permission to purchase a reserved DB instance offering
  - **Resource types (\*required):** [ri\*](#list_rds-resource-ri)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:ri-tag/${TagKey}](#list_rds-rds_ri-tag___TagKey_)
  - **Access level:** Write

- **   [RebootDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBCluster.html)  **
  - **Description:** Grants permission to reboot a previously provisioned DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [RebootDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBInstance.html)  **
  - **Description:** Grants permission to restart the database engine service
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [RebootDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBShardGroup.html)  **
  - **Description:** Grants permission to reboot an Aurora Limitless Database DB shard group
  - **Resource types (\*required):** [shardgrp\*](#list_rds-resource-shardgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RegisterDBProxyTargets.html)  **
  - **Description:** Grants permission to add targets to a database proxy target group
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [target-group\*](#list_rds-resource-target-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveFromGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveFromGlobalCluster.html)  **
  - **Description:** Grants permission to detach an Aurora secondary cluster from an Aurora global database cluster or DocumentDB global cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [global-cluster\*](#list_rds-resource-global-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveRoleFromDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveRoleFromDBCluster.html)  **
  - **Description:** Grants permission to disassociate an AWS Identity and Access Management (IAM) role from an Amazon Aurora DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [RemoveRoleFromDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveRoleFromDBInstance.html)  **
  - **Description:** Grants permission to disassociate an AWS Identity and Access Management (IAM) role from a DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [RemoveSourceIdentifierFromSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveSourceIdentifierFromSubscription.html)  **
  - **Description:** Grants permission to remove a source identifier from an existing RDS event notification subscription
  - **Resource types (\*required):** [es\*](#list_rds-resource-es)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)
  - **Access level:** Write

- **   [RemoveTagsFromResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveTagsFromResource.html)  **
  - **Description:** Grants permission to remove metadata tags from an Amazon RDS resource
  - **Resource types (\*required):** [auto-backup](#list_rds-resource-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cev](#list_rds-resource-cev) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster-auto-backup](#list_rds-resource-cluster-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster-endpoint](#list_rds-resource-cluster-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster-pg](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [deployment](#list_rds-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [es](#list_rds-resource-es) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [global-cluster](#list_rds-resource-global-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [integration](#list_rds-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [og](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [pg](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [proxy](#list_rds-resource-proxy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [proxy-endpoint](#list_rds-resource-proxy-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [ri](#list_rds-resource-ri) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:ri-tag/${TagKey}](#list_rds-rds_ri-tag___TagKey_)
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Resource types (\*required):** [shardgrp](#list_rds-resource-shardgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Resource types (\*required):** [snapshot-tenant-database](#list_rds-resource-snapshot-tenant-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [subgrp](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Resource types (\*required):** [target-group](#list_rds-resource-target-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [tenant-database](#list_rds-resource-tenant-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Access level:** Tagging, Write

- **   [ResetDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBClusterParameterGroup.html)  **
  - **Description:** Grants permission to modify the parameters of a DB cluster parameter group to the default value
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)
  - **Access level:** Write

- **   [ResetDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBParameterGroup.html)  **
  - **Description:** Grants permission to modify the parameters of a DB parameter group to the engine/system default value
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)
  - **Access level:** Write

- **   [RestoreDBClusterFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromS3.html)  **
  - **Description:** Grants permission to create an Amazon Aurora DB cluster from data stored in an Amazon S3 bucket
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [RestoreDBClusterFromSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.html)  **
  - **Description:** Grants permission to create a new DB cluster from a DB cluster snapshot
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.html)  **
  - **Description:** Grants permission to restore a DB cluster to an arbitrary point in time
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [cluster-auto-backup](#list_rds-resource-cluster-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [cluster-pg\*](#list_rds-resource-cluster-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [RestoreDBInstanceFromDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html)  **
  - **Description:** Grants permission to create a new DB instance from a DB snapshot
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [RestoreDBInstanceFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html)  **
  - **Description:** Grants permission to create a new DB instance from an Amazon S3 bucket
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [secgrp](#list_rds-resource-secgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [RestoreDBInstanceToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html)  **
  - **Description:** Grants permission to restore a DB instance to an arbitrary point in time
  - **Resource types (\*required):** [auto-backup](#list_rds-resource-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [og\*](#list_rds-resource-og) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [pg\*](#list_rds-resource-pg) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [subgrp\*](#list_rds-resource-subgrp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:BackupTarget](#list_rds-rds_BackupTarget)<br />[rds:ManageMasterUserPassword](#list_rds-rds_ManageMasterUserPassword)<br />[rds:PubliclyAccessible](#list_rds-rds_PubliclyAccessible)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [RevokeDBSecurityGroupIngress](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RevokeDBSecurityGroupIngress.html)  **
  - **Description:** Grants permission to revoke ingress from a DBSecurityGroup for previously authorized IP ranges or EC2 or VPC Security Groups
  - **Resource types (\*required):** [secgrp\*](#list_rds-resource-secgrp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_)
  - **Access level:** Write

- **   [StartActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartActivityStream.html)  **
  - **Description:** Grants permission to start Activity Stream
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [StartDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBCluster.html)  **
  - **Description:** Grants permission to start the DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [StartDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstance.html)  **
  - **Description:** Grants permission to start the DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [StartDBInstanceAutomatedBackupsReplication](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstanceAutomatedBackupsReplication.html)  **
  - **Description:** Grants permission to start replication of automated backups to a different AWS Region
  - **Resource types (\*required):** [auto-backup\*](#list_rds-resource-auto-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rds-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-aws_TagKeys)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:req-tag/${TagKey}](#list_rds-rds_req-tag___TagKey_)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [StartExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartExportTask.html)  **
  - **Description:** Grants permission to start a new Export task for a DB snapshot
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [StopActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopActivityStream.html)  **
  - **Description:** Grants permission to stop Activity Stream
  - **Resource types (\*required):** [cluster](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [StopDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBCluster.html)  **
  - **Description:** Grants permission to stop the DB cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Access level:** Write

- **   [StopDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstance.html)  **
  - **Description:** Grants permission to stop the DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [StopDBInstanceAutomatedBackupsReplication](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstanceAutomatedBackupsReplication.html)  **
  - **Description:** Grants permission to stop automated backup replication for a DB instance
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write

- **   [SwitchoverBlueGreenDeployment](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverBlueGreenDeployment.html)  **
  - **Description:** Grants permission to switch a blue-green deployment from source instance or cluster to target
  - **Resource types (\*required):** [deployment\*](#list_rds-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SwitchoverGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverGlobalCluster.html)  **
  - **Description:** Grants permission to switchover a global cluster
  - **Resource types (\*required):** [cluster\*](#list_rds-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_)
  - **Resource types (\*required):** [global-cluster\*](#list_rds-resource-global-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SwitchoverReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverReadReplica.html)  **
  - **Description:** Grants permission to switch over a read replica, making it the new primary database
  - **Resource types (\*required):** [db\*](#list_rds-resource-db)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Access level:** Write



## Permission-only actions for Amazon RDS
<a name="list_rds-permission-only-actions"></a>

The following actions are defined by Amazon RDS but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CopyCustomDBEngineVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html)  **
  - **Description:** Grants permission to copy a custom engine version
  - **Resource types (\*required):** [cev\*](#list_rds-resource-cev)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CrossRegionCommunication](https://docs.aws.amazon.com/AmazonRDS/latest/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  **
  - **Description:** Grants permission to access a resource in the remote Region when executing cross-Region operations, such as cross-Region snapshot copy or cross-Region read replica creation
  - **Resource types (\*required):** [cluster-snapshot](#list_rds-resource-cluster-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_)
  - **Resource types (\*required):** [db](#list_rds-resource-db) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)
  - **Resource types (\*required):** [snapshot](#list_rds-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_)
  - **Access level:** Write

- **   [DescribeRecommendationGroups](https://docs.aws.amazon.com/AmazonRDS/latest/USER_Recommendations.html)  **
  - **Description:** Grants permission to return information about recommendation groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecommendations](https://docs.aws.amazon.com/AmazonRDS/latest/USER_Recommendations.html)  **
  - **Description:** Grants permission to return information about recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ModifyRecommendation](https://docs.aws.amazon.com/AmazonRDS/latest/USER_Recommendations.html)  **
  - **Description:** Grants permission to modify recommendation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon RDS
<a name="list_rds-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [auto-backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)  | arn:${Partition}:rds:${Region}:${Account}:auto-backup:${DbInstanceAutomatedBackupId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [cev](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html)  | arn:${Partition}:rds:${Region}:${Account}:cev:${Engine}/${EngineVersion}/${CustomDbEngineVersionId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Aurora.html)  | arn:${Partition}:rds:${Region}:${Account}:cluster:${DbClusterInstanceName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-tag/${TagKey}](#list_rds-rds_cluster-tag___TagKey_) | 
|  [cluster-auto-backup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html)  | arn:${Partition}:rds:${Region}:${Account}:cluster-auto-backup:${DbClusterAutomatedBackupId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [cluster-endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html)  | arn:${Partition}:rds:${Region}:${Account}:cluster-endpoint:${DbClusterEndpoint} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [cluster-pg](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)  | arn:${Partition}:rds:${Region}:${Account}:cluster-pg:${ClusterParameterGroupName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-pg-tag/${TagKey}](#list_rds-rds_cluster-pg-tag___TagKey_) | 
|  [cluster-snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html)  | arn:${Partition}:rds:${Region}:${Account}:cluster-snapshot:${ClusterSnapshotName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:cluster-snapshot-tag/${TagKey}](#list_rds-rds_cluster-snapshot-tag___TagKey_) | 
|  [db](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html)  | arn:${Partition}:rds:${Region}:${Account}:db:${DbInstanceName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:DatabaseClass](#list_rds-rds_DatabaseClass)<br />[rds:DatabaseEngine](#list_rds-rds_DatabaseEngine)<br />[rds:DatabaseName](#list_rds-rds_DatabaseName)<br />[rds:MultiAz](#list_rds-rds_MultiAz)<br />[rds:Piops](#list_rds-rds_Piops)<br />[rds:StorageEncrypted](#list_rds-rds_StorageEncrypted)<br />[rds:StorageSize](#list_rds-rds_StorageSize)<br />[rds:Vpc](#list_rds-rds_Vpc)<br />[rds:db-tag/${TagKey}](#list_rds-rds_db-tag___TagKey_) | 
|  [deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)  | arn:${Partition}:rds:${Region}:${Account}:deployment:${BlueGreenDeploymentIdentifier} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [es](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)  | arn:${Partition}:rds:${Region}:${Account}:es:${SubscriptionName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:es-tag/${TagKey}](#list_rds-rds_es-tag___TagKey_) | 
|  [global-cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)  | arn:${Partition}:rds::${Account}:global-cluster:${GlobalCluster} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [integration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html)  | arn:${Partition}:rds:${Region}:${Account}:integration:${IntegrationIdentifier} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [og](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html)  | arn:${Partition}:rds:${Region}:${Account}:og:${OptionGroupName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:og-tag/${TagKey}](#list_rds-rds_og-tag___TagKey_) | 
|  [pg](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)  | arn:${Partition}:rds:${Region}:${Account}:pg:${ParameterGroupName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:pg-tag/${TagKey}](#list_rds-rds_pg-tag___TagKey_) | 
|  [proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)  | arn:${Partition}:rds:${Region}:${Account}:db-proxy:${DbProxyId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [proxy-endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)  | arn:${Partition}:rds:${Region}:${Account}:db-proxy-endpoint:${DbProxyEndpointId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [ri](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)  | arn:${Partition}:rds:${Region}:${Account}:ri:${ReservedDbInstanceName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:ri-tag/${TagKey}](#list_rds-rds_ri-tag___TagKey_) | 
|  [secgrp](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html)  | arn:${Partition}:rds:${Region}:${Account}:secgrp:${SecurityGroupName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:secgrp-tag/${TagKey}](#list_rds-rds_secgrp-tag___TagKey_) | 
|  [shardgrp](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-architecture.html)  | arn:${Partition}:rds:${Region}:${Account}:shard-group:${DbShardGroupResourceId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)  | arn:${Partition}:rds:${Region}:${Account}:snapshot:${SnapshotName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:snapshot-tag/${TagKey}](#list_rds-rds_snapshot-tag___TagKey_) | 
|  [snapshot-tenant-database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.single-tenant.snapshots.html#br-cdb.db-snapshots)  | arn:${Partition}:rds:${Region}:${Account}:snapshot-tenant-database:${SnapshotName}:${TenantResourceId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [subgrp](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1)  | arn:${Partition}:rds:${Region}:${Account}:subgrp:${SubnetGroupName} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_)<br />[rds:subgrp-tag/${TagKey}](#list_rds-rds_subgrp-tag___TagKey_) | 
|  [target-group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)  | arn:${Partition}:rds:${Region}:${Account}:target-group:${TargetGroupId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 
|  [tenant-database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.CDBs.html#multi-tenant-configuration)  | arn:${Partition}:rds:${Region}:${Account}:tenant-database:${TenantResourceId} | [aws:ResourceTag/${TagKey}](#list_rds-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon RDS
<a name="list_rds-policy-keys"></a>

Amazon RDS defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the set of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the set of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the set of tag keys in the request | ArrayOfString | 
|   [rds:BackupTarget](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the type of backup target. One of: region, outposts | String | 
|   [rds:CopyOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that specifies whether the CopyDBSnapshot action requires copying the DB option group | Bool | 
|   [rds:DatabaseClass](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the type of DB instance class | String | 
|   [rds:DatabaseEngine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the database engine. For possible values refer to the engine parameter in CreateDBInstance API | String | 
|   [rds:DatabaseName](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the user-defined name of the database on the DB instance | String | 
|   [rds:EndpointType](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the type of the endpoint. One of: READER, WRITER, CUSTOM | String | 
|   [rds:ManageMasterUserPassword](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that specifies whether RDS manages master user password in AWS Secrets Manager for the DB instance or cluster | Bool | 
|   [rds:MultiAz](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that specifies whether the DB instance runs in multiple Availability Zones. To indicate that the DB instance is using Multi-AZ, specify true | Bool | 
|   [rds:Piops](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that contains the number of Provisioned IOPS (PIOPS) that the instance supports. To indicate a DB instance that does not have PIOPS enabled, specify 0 | Numeric | 
|   [rds:PubliclyAccessible](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that specifies whether the DB Instance or DB ShardGroup is publicly accessible | Bool | 
|   [rds:StorageEncrypted](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that specifies whether the DB instance storage should be encrypted. To enforce storage encryption, specify true | Bool | 
|   [rds:StorageSize](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the storage volume size (in GB) | Numeric | 
|   [rds:TagsFromRequest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access for rds:AddTagsToResource based on whether tags are explicitly specified in the Tags or TagSpecification request parameters. Evaluates to true when tags are provided in these parameters. Evaluates as false when tags are implicitly inherited from source resources | Bool | 
|   [rds:TenantDatabaseName](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tenant database name in CreateTenantDatabase and by the new tenant database name in ModifyTenantDatabase | String | 
|   [rds:Vpc](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the value that specifies whether the DB instance runs in an Amazon Virtual Private Cloud (Amazon VPC). To indicate that the DB instance runs in an Amazon VPC, specify true | Bool | 
|   [rds:cluster-pg-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB cluster parameter group | String | 
|   [rds:cluster-snapshot-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB cluster snapshot | String | 
|   [rds:cluster-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB cluster | String | 
|   [rds:db-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB instance | String | 
|   [rds:es-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to an event subscription | String | 
|   [rds:og-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB option group | String | 
|   [rds:pg-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB parameter group | String | 
|   [rds:req-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the set of tag keys and values that can be used to tag a resource | String | 
|   [rds:ri-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a reserved DB instance | String | 
|   [rds:secgrp-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB security group | String | 
|   [rds:snapshot-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB snapshot | String | 
|   [rds:subgrp-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions)  | Filters access by the tag attached to a DB subnet group | String | 