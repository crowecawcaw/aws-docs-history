

# Actions, resources, and condition keys for Amazon Timestream InfluxDB
<a name="list_timestream-influxdb"></a>

Amazon Timestream InfluxDB (service prefix: `timestream-influxdb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/timestream/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/timestream/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/timestream-influxdb/timestream-influxdb.json) for this service.

**Topics**
+ [API operations defined by Amazon Timestream InfluxDB](#list_timestream-influxdb-operations)
+ [Actions defined by Amazon Timestream InfluxDB](#list_timestream-influxdb-actions-as-permissions)
+ [Resource types defined by Amazon Timestream InfluxDB](#list_timestream-influxdb-resources-for-iam-policies)
+ [Condition keys for Amazon Timestream InfluxDB](#list_timestream-influxdb-policy-keys)

## API operations defined by Amazon Timestream InfluxDB
<a name="list_timestream-influxdb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_timestream-influxdb-actions-as-permissions).




- **   CreateDbBackup  **
  - **IAM action:**  [timestream-influxdb:CreateDbBackup](#list_timestream-influxdb-action-CreateDbBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:TagResource](#list_timestream-influxdb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDbCluster  **
  - **IAM action:**  [timestream-influxdb:CreateDbCluster](#list_timestream-influxdb-action-CreateDbCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:CreateDbInstance](#list_timestream-influxdb-action-CreateDbInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:CreateDbParameterGroup](#list_timestream-influxdb-action-CreateDbParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:TagResource](#list_timestream-influxdb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDbInstance  **
  - **IAM action:**  [timestream-influxdb:CreateDbInstance](#list_timestream-influxdb-action-CreateDbInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:TagResource](#list_timestream-influxdb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDbParameterGroup  **
  - **IAM action:**  [timestream-influxdb:CreateDbParameterGroup](#list_timestream-influxdb-action-CreateDbParameterGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:TagResource](#list_timestream-influxdb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDbBackup  **
  - **IAM action:**  [timestream-influxdb:DeleteDbBackup](#list_timestream-influxdb-action-DeleteDbBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDbCluster  **
  - **IAM action:**  [timestream-influxdb:DeleteDbCluster](#list_timestream-influxdb-action-DeleteDbCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:DeleteDbInstance](#list_timestream-influxdb-action-DeleteDbInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteDbInstance  **
  - **IAM action:**  [timestream-influxdb:DeleteDbInstance](#list_timestream-influxdb-action-DeleteDbInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDbBackup  **
  - **IAM action:**  [timestream-influxdb:GetDbBackup](#list_timestream-influxdb-action-GetDbBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDbCluster  **
  - **IAM action:**  [timestream-influxdb:GetDbCluster](#list_timestream-influxdb-action-GetDbCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDbInstance  **
  - **IAM action:**  [timestream-influxdb:GetDbInstance](#list_timestream-influxdb-action-GetDbInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDbParameterGroup  **
  - **IAM action:**  [timestream-influxdb:GetDbParameterGroup](#list_timestream-influxdb-action-GetDbParameterGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDbBackups  **
  - **IAM action:**  [timestream-influxdb:ListDbBackups](#list_timestream-influxdb-action-ListDbBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDbClusters  **
  - **IAM action:**  [timestream-influxdb:ListDbClusters](#list_timestream-influxdb-action-ListDbClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDbInstances  **
  - **IAM action:**  [timestream-influxdb:ListDbInstances](#list_timestream-influxdb-action-ListDbInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDbInstancesForCluster  **
  - **IAM action:**  [timestream-influxdb:ListDbInstancesForCluster](#list_timestream-influxdb-action-ListDbInstancesForCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDbParameterGroups  **
  - **IAM action:**  [timestream-influxdb:ListDbParameterGroups](#list_timestream-influxdb-action-ListDbParameterGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [timestream-influxdb:ListTagsForResource](#list_timestream-influxdb-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RebootDbCluster  **
  - **IAM action:**  [timestream-influxdb:RebootDbCluster](#list_timestream-influxdb-action-RebootDbCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:RebootDbInstance](#list_timestream-influxdb-action-RebootDbInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RebootDbInstance  **
  - **IAM action:**  [timestream-influxdb:RebootDbInstance](#list_timestream-influxdb-action-RebootDbInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreFromDbBackup  **
  - **IAM action:**  [timestream-influxdb:RestoreFromDbBackup](#list_timestream-influxdb-action-RestoreFromDbBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [timestream-influxdb:TagResource](#list_timestream-influxdb-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [timestream-influxdb:UntagResource](#list_timestream-influxdb-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDbCluster  **
  - **IAM action:**  [timestream-influxdb:UpdateDbCluster](#list_timestream-influxdb-action-UpdateDbCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream-influxdb:UpdateDbInstance](#list_timestream-influxdb-action-UpdateDbInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateDbInstance  **
  - **IAM action:**  [timestream-influxdb:UpdateDbInstance](#list_timestream-influxdb-action-UpdateDbInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Timestream InfluxDB
<a name="list_timestream-influxdb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDbBackup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbBackup.html)  **
  - **Description:** Grants permission to create a Timestream InfluxDB Backup for a DbInstance or DbCluster
  - **Resource types (\*required):** [db-backup\*](#list_timestream-influxdb-resource-db-backup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbCluster.html)  **
  - **Description:** Grants permission to create a new Timestream InfluxDB Cluster
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbInstance.html)  **
  - **Description:** Grants permission to create a new Timestream InfluxDB instance
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDbParameterGroup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbParameterGroup.html)  **
  - **Description:** Grants permission to create a new Timestream InfluxDB parameter group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDbBackup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DeleteDbBackup.html)  **
  - **Description:** Grants permission to delete a Timestream InfluxDB backup
  - **Resource types (\*required):** [db-backup\*](#list_timestream-influxdb-resource-db-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DeleteDbCluster.html)  **
  - **Description:** Grants permission to delete a Timestream InfluxDB Cluster
  - **Resource types (\*required):** [db-cluster\*](#list_timestream-influxdb-resource-db-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DeleteDbInstance.html)  **
  - **Description:** Grants permission to delete a Timestream InfluxDB instance
  - **Resource types (\*required):** [db-instance\*](#list_timestream-influxdb-resource-db-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDbBackup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbBackup.html)  **
  - **Description:** Grants permission to get information about a Timestream InfluxDB Backup
  - **Resource types (\*required):** [db-backup\*](#list_timestream-influxdb-resource-db-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbCluster.html)  **
  - **Description:** Grants permission to get information about a Timestream InfluxDB Cluster
  - **Resource types (\*required):** [db-cluster\*](#list_timestream-influxdb-resource-db-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbInstance.html)  **
  - **Description:** Grants permission to get information about a Timestream InfluxDB instance
  - **Resource types (\*required):** [db-instance\*](#list_timestream-influxdb-resource-db-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDbParameterGroup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbParameterGroup.html)  **
  - **Description:** Grants permission to get information about a Timestream InfluxDB parameter group
  - **Resource types (\*required):** [db-parameter-group\*](#list_timestream-influxdb-resource-db-parameter-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDbBackups](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbBackups.html)  **
  - **Description:** Grants permission to list information about all Timestream InfluxDB backups in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDbClusters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbClusters.html)  **
  - **Description:** Grants permission to list information about all Timestream InfluxDB clusters in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDbInstances](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbInstances.html)  **
  - **Description:** Grants permission to list information about all Timestream InfluxDB instances in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDbInstancesForCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbInstancesForCluster.html)  **
  - **Description:** Grants permission to list information about all Timestream InfluxDB Instances belonging to a cluster
  - **Resource types (\*required):** [db-cluster\*](#list_timestream-influxdb-resource-db-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDbParameterGroups](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbParameterGroups.html)  **
  - **Description:** Grants permission to list information about all Timestream InfluxDB parameter groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Timestream InfluxDB resource
  - **Resource types (\*required):** [db-backup](#list_timestream-influxdb-resource-db-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-cluster](#list_timestream-influxdb-resource-db-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-instance](#list_timestream-influxdb-resource-db-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RebootDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RebootDbCluster.html)  **
  - **Description:** Grants permission to reboot a Timestream InfluxDB Cluster
  - **Resource types (\*required):** [db-cluster\*](#list_timestream-influxdb-resource-db-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-instance](#list_timestream-influxdb-resource-db-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RebootDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RebootDbInstance.html)  **
  - **Description:** Grants permission to reboot a Timestream InfluxDB instance
  - **Resource types (\*required):** [db-instance\*](#list_timestream-influxdb-resource-db-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreFromDbBackup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RestoreFromDbBackup.html)  **
  - **Description:** Grants permission to restore from a Timestream InfluxDB backup
  - **Resource types (\*required):** [db-backup\*](#list_timestream-influxdb-resource-db-backup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)<br />[timestream-influxdb:RestoreMode](#list_timestream-influxdb-timestream-influxdb_RestoreMode)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_TagResource.html)  **
  - **Description:** Grants permission to tag a Timestream InfluxDB resource
  - **Resource types (\*required):** [db-backup](#list_timestream-influxdb-resource-db-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Resource types (\*required):** [db-cluster](#list_timestream-influxdb-resource-db-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Resource types (\*required):** [db-instance](#list_timestream-influxdb-resource-db-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-influxdb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a Timestream InfluxDB resource
  - **Resource types (\*required):** [db-backup](#list_timestream-influxdb-resource-db-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Resource types (\*required):** [db-cluster](#list_timestream-influxdb-resource-db-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Resource types (\*required):** [db-instance](#list_timestream-influxdb-resource-db-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-influxdb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_UpdateDbCluster.html)  **
  - **Description:** Grants permission to update a Timestream InfluxDB Cluster
  - **Resource types (\*required):** [db-cluster\*](#list_timestream-influxdb-resource-db-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_UpdateDbInstance.html)  **
  - **Description:** Grants permission to update a Timestream InfluxDB instance
  - **Resource types (\*required):** [db-instance\*](#list_timestream-influxdb-resource-db-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-parameter-group](#list_timestream-influxdb-resource-db-parameter-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Timestream InfluxDB
<a name="list_timestream-influxdb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [db-backup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbBackupSummary.html)  | arn:${Partition}:timestream-influxdb:${Region}:${Account}:db-backup/${DbBackupId} | [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_) | 
|  [db-cluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbClusterSummary.html)  | arn:${Partition}:timestream-influxdb:${Region}:${Account}:db-cluster/${DbClusterId} | [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_) | 
|  [db-instance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceSummary.html)  | arn:${Partition}:timestream-influxdb:${Region}:${Account}:db-instance/${DbInstanceIdentifier} | [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_) | 
|  [db-parameter-group](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbParameterGroupSummary.html)  | arn:${Partition}:timestream-influxdb:${Region}:${Account}:db-parameter-group/${DbParameterGroupIdentifier} | [aws:ResourceTag/${TagKey}](#list_timestream-influxdb-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Timestream InfluxDB
<a name="list_timestream-influxdb-policy-keys"></a>

Amazon Timestream InfluxDB defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [timestream-influxdb:RestoreMode](https://docs.aws.amazon.com/timestream/latest/developerguide/security-iam.html)  | Filters access by the restore mode specified in the request | String | 