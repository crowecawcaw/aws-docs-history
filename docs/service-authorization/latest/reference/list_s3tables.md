

# Actions, resources, and condition keys for Amazon S3 Tables
<a name="list_s3tables"></a>

Amazon S3 Tables (service prefix: `s3tables`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3tables/s3tables.json) for this service.

**Topics**
+ [API operations defined by Amazon S3 Tables](#list_s3tables-operations)
+ [Actions defined by Amazon S3 Tables](#list_s3tables-actions-as-permissions)
+ [Permission-only actions for Amazon S3 Tables](#list_s3tables-permission-only-actions)
+ [Resource types defined by Amazon S3 Tables](#list_s3tables-resources-for-iam-policies)
+ [Condition keys for Amazon S3 Tables](#list_s3tables-policy-keys)

## API operations defined by Amazon S3 Tables
<a name="list_s3tables-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_s3tables-actions-as-permissions).




- **   CreateNamespace  **
  - **IAM action:**  [s3tables:CreateNamespace](#list_s3tables-action-CreateNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTable  **
  - **IAM action:**  [s3tables:CreateTable](#list_s3tables-action-CreateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:PutTableEncryption](#list_s3tables-action-PutTableEncryption)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:PutTableStorageClass](#list_s3tables-action-PutTableStorageClass)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:TagResource](#list_s3tables-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTableBucket  **
  - **IAM action:**  [s3tables:CreateTableBucket](#list_s3tables-action-CreateTableBucket)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:PutTableBucketEncryption](#list_s3tables-action-PutTableBucketEncryption)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:PutTableBucketPolicy](#list_s3tables-action-PutTableBucketPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [s3tables:PutTableBucketStorageClass](#list_s3tables-action-PutTableBucketStorageClass)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3tables:TagResource](#list_s3tables-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteNamespace  **
  - **IAM action:**  [s3tables:DeleteNamespace](#list_s3tables-action-DeleteNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTable  **
  - **IAM action:**  [s3tables:DeleteTable](#list_s3tables-action-DeleteTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTableBucket  **
  - **IAM action:**  [s3tables:DeleteTableBucket](#list_s3tables-action-DeleteTableBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTableBucketEncryption  **
  - **IAM action:**  [s3tables:DeleteTableBucketEncryption](#list_s3tables-action-DeleteTableBucketEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTableBucketMetricsConfiguration  **
  - **IAM action:**  [s3tables:DeleteTableBucketMetricsConfiguration](#list_s3tables-action-DeleteTableBucketMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTableBucketPolicy  **
  - **IAM action:**  [s3tables:DeleteTableBucketPolicy](#list_s3tables-action-DeleteTableBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteTableBucketReplication  **
  - **IAM action:**  [s3tables:DeleteTableBucketReplication](#list_s3tables-action-DeleteTableBucketReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTablePolicy  **
  - **IAM action:**  [s3tables:DeleteTablePolicy](#list_s3tables-action-DeleteTablePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteTableReplication  **
  - **IAM action:**  [s3tables:DeleteTableReplication](#list_s3tables-action-DeleteTableReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetNamespace  **
  - **IAM action:**  [s3tables:GetNamespace](#list_s3tables-action-GetNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTable  **
  - **IAM action:**  [s3tables:GetTable](#list_s3tables-action-GetTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucket  **
  - **IAM action:**  [s3tables:GetTableBucket](#list_s3tables-action-GetTableBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucketEncryption  **
  - **IAM action:**  [s3tables:GetTableBucketEncryption](#list_s3tables-action-GetTableBucketEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucketMaintenanceConfiguration  **
  - **IAM action:**  [s3tables:GetTableBucketMaintenanceConfiguration](#list_s3tables-action-GetTableBucketMaintenanceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucketMetricsConfiguration  **
  - **IAM action:**  [s3tables:GetTableBucketMetricsConfiguration](#list_s3tables-action-GetTableBucketMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucketPolicy  **
  - **IAM action:**  [s3tables:GetTableBucketPolicy](#list_s3tables-action-GetTableBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucketReplication  **
  - **IAM action:**  [s3tables:GetTableBucketReplication](#list_s3tables-action-GetTableBucketReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableBucketStorageClass  **
  - **IAM action:**  [s3tables:GetTableBucketStorageClass](#list_s3tables-action-GetTableBucketStorageClass) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableEncryption  **
  - **IAM action:**  [s3tables:GetTableEncryption](#list_s3tables-action-GetTableEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableMaintenanceConfiguration  **
  - **IAM action:**  [s3tables:GetTableMaintenanceConfiguration](#list_s3tables-action-GetTableMaintenanceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableMaintenanceJobStatus  **
  - **IAM action:**  [s3tables:GetTableMaintenanceJobStatus](#list_s3tables-action-GetTableMaintenanceJobStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableMetadataLocation  **
  - **IAM action:**  [s3tables:GetTableMetadataLocation](#list_s3tables-action-GetTableMetadataLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTablePolicy  **
  - **IAM action:**  [s3tables:GetTablePolicy](#list_s3tables-action-GetTablePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableRecordExpirationConfiguration  **
  - **IAM action:**  [s3tables:GetTableRecordExpirationConfiguration](#list_s3tables-action-GetTableRecordExpirationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableRecordExpirationJobStatus  **
  - **IAM action:**  [s3tables:GetTableRecordExpirationJobStatus](#list_s3tables-action-GetTableRecordExpirationJobStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableReplication  **
  - **IAM action:**  [s3tables:GetTableReplication](#list_s3tables-action-GetTableReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableReplicationStatus  **
  - **IAM action:**  [s3tables:GetTableReplicationStatus](#list_s3tables-action-GetTableReplicationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableStorageClass  **
  - **IAM action:**  [s3tables:GetTableStorageClass](#list_s3tables-action-GetTableStorageClass) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNamespaces  **
  - **IAM action:**  [s3tables:ListNamespaces](#list_s3tables-action-ListNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTableBuckets  **
  - **IAM action:**  [s3tables:ListTableBuckets](#list_s3tables-action-ListTableBuckets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTables  **
  - **IAM action:**  [s3tables:ListTables](#list_s3tables-action-ListTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [s3tables:ListTagsForResource](#list_s3tables-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutTableBucketEncryption  **
  - **IAM action:**  [s3tables:PutTableBucketEncryption](#list_s3tables-action-PutTableBucketEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTableBucketMaintenanceConfiguration  **
  - **IAM action:**  [s3tables:PutTableBucketMaintenanceConfiguration](#list_s3tables-action-PutTableBucketMaintenanceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTableBucketMetricsConfiguration  **
  - **IAM action:**  [s3tables:PutTableBucketMetricsConfiguration](#list_s3tables-action-PutTableBucketMetricsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTableBucketPolicy  **
  - **IAM action:**  [s3tables:PutTableBucketPolicy](#list_s3tables-action-PutTableBucketPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutTableBucketReplication  **
  - **IAM action:**  [s3tables:PutTableBucketReplication](#list_s3tables-action-PutTableBucketReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** replication.s3tables.amazonaws.com / **Access level:** Write

- **   PutTableBucketStorageClass  **
  - **IAM action:**  [s3tables:PutTableBucketStorageClass](#list_s3tables-action-PutTableBucketStorageClass) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTableMaintenanceConfiguration  **
  - **IAM action:**  [s3tables:PutTableMaintenanceConfiguration](#list_s3tables-action-PutTableMaintenanceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTablePolicy  **
  - **IAM action:**  [s3tables:PutTablePolicy](#list_s3tables-action-PutTablePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutTableRecordExpirationConfiguration  **
  - **IAM action:**  [s3tables:PutTableRecordExpirationConfiguration](#list_s3tables-action-PutTableRecordExpirationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTableReplication  **
  - **IAM action:**  [s3tables:PutTableReplication](#list_s3tables-action-PutTableReplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** replication.s3tables.amazonaws.com / **Access level:** Write

- **   RenameTable  **
  - **IAM action:**  [s3tables:RenameTable](#list_s3tables-action-RenameTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [s3tables:TagResource](#list_s3tables-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [s3tables:UntagResource](#list_s3tables-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateTableMetadataLocation  **
  - **IAM action:**  [s3tables:UpdateTableMetadataLocation](#list_s3tables-action-UpdateTableMetadataLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon S3 Tables
<a name="list_s3tables-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateNamespace.html)  **
  - **Description:** Grants permission to create a namespace
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [CreateTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTable.html)  **
  - **Description:** Grants permission to create a table
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3tables-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3tables-aws_TagKeys)<br />[s3tables:KMSKeyArn](#list_s3tables-s3tables_KMSKeyArn)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:SSEAlgorithm](#list_s3tables-s3tables_SSEAlgorithm)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [CreateTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_CreateTableBucket.html)  **
  - **Description:** Grants permission to create a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3tables-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3tables-aws_TagKeys)<br />[s3tables:KMSKeyArn](#list_s3tables-s3tables_KMSKeyArn)<br />[s3tables:SSEAlgorithm](#list_s3tables-s3tables_SSEAlgorithm)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteNamespace.html)  **
  - **Description:** Grants permission to delete a namespace
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTable.html)  **
  - **Description:** Grants permission to delete a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [DeleteTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucket.html)  **
  - **Description:** Grants permission to delete a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTableBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketEncryption.html)  **
  - **Description:** Grants permission to delete encryption configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTableBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to delete a metrics configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTableBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketPolicy.html)  **
  - **Description:** Grants permission to delete a policy on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteTableBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableBucketReplication.html)  **
  - **Description:** Grants permission to delete table bucket replication configuration on a bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTablePolicy.html)  **
  - **Description:** Grants permission to delete a policy on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Permissions management, Write

- **   [DeleteTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DeleteTableReplication.html)  **
  - **Description:** Grants permission to delete table replication configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [GetNamespace](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetNamespace.html)  **
  - **Description:** Grants permission to get a namespace
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTable.html)  **
  - **Description:** Grants permission to retrieve a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucket.html)  **
  - **Description:** Grants permission to retrieve a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketEncryption.html)  **
  - **Description:** Grants permission to retrieve encryption configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableBucketMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketMaintenanceConfiguration.html)  **
  - **Description:** Grants permission to retrieve a maintenance configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to retrieve a metrics configuration on a bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketPolicy.html)  **
  - **Description:** Grants permission to retrieve a policy on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketReplication.html)  **
  - **Description:** Grants permission to retrieve a table bucket replication configuration on a bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableBucketStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableBucketStorageClass.html)  **
  - **Description:** Grants permission to retrieve the storage class configuration for a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Read

- **   [GetTableEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableEncryption.html)  **
  - **Description:** Grants permission to retrieve encryption configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMaintenanceConfiguration.html)  **
  - **Description:** Grants permission to retrieve a maintenance configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableMaintenanceJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMaintenanceJobStatus.html)  **
  - **Description:** Grants permission to retrieve the status of maintenance jobs on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableMetadataLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableMetadataLocation.html)  **
  - **Description:** Grants permission to retrieve the metadata location of a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTablePolicy.html)  **
  - **Description:** Grants permission to retrieve a policy on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableRecordExpirationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableRecordExpirationConfiguration.html)  **
  - **Description:** Grants permission to retrieve a table maintenance configuration on a system table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableRecordExpirationJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableRecordExpirationJobStatus.html)  **
  - **Description:** Grants permission to retrieve the status of table record expiration jobs on a system table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableReplication.html)  **
  - **Description:** Grants permission to retrieve a table replication configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableReplicationStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableReplicationStatus.html)  **
  - **Description:** Grants permission to retrieve a table replication status on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [GetTableStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GetTableStorageClass.html)  **
  - **Description:** Grants permission to retrieve the storage class configuration for a specific table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [ListNamespaces](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListNamespaces.html)  **
  - **Description:** Grants permission to list namespaces
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** List

- **   [ListTableBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTableBuckets.html)  **
  - **Description:** Grants permission to list table buckets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTables](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ListTables.html)  **
  - **Description:** Grants permission to list tables
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables-tagging.html)  **
  - **Description:** Grants permission to list the tags for an S3 Tables resource
  - **Resource types (\*required):** [Table](#list_s3tables-resource-Table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Resource types (\*required):** [TableBucket](#list_s3tables-resource-TableBucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** List

- **   [PutTableBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketEncryption.html)  **
  - **Description:** Grants permission to put or overwrite encryption configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:KMSKeyArn](#list_s3tables-s3tables_KMSKeyArn)<br />[s3tables:SSEAlgorithm](#list_s3tables-s3tables_SSEAlgorithm)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [PutTableBucketMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketMaintenanceConfiguration.html)  **
  - **Description:** Grants permission to put a maintenance configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [PutTableBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketMetricsConfiguration.html)  **
  - **Description:** Grants permission to create or overwrite a metrics configuration on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [PutTableBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketPolicy.html)  **
  - **Description:** Grants permission to create or overwrite a policy on a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutTableBucketReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketReplication.html)  **
  - **Description:** Grants permission to put table bucket replication configuration on a bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [PutTableBucketStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableBucketStorageClass.html)  **
  - **Description:** Grants permission to set or update the storage class configuration for a table bucket
  - **Resource types (\*required):** [TableBucket\*](#list_s3tables-resource-TableBucket)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:StorageClass](#list_s3tables-s3tables_StorageClass)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Write

- **   [PutTableMaintenanceConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableMaintenanceConfiguration.html)  **
  - **Description:** Grants permission to put a maintenance configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [PutTablePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTablePolicy.html)  **
  - **Description:** Grants permission to create or overwrite a policy on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Permissions management, Write

- **   [PutTableRecordExpirationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableRecordExpirationConfiguration.html)  **
  - **Description:** Grants permission to put a table record expiration configuration on a system table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [PutTableReplication](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableReplication.html)  **
  - **Description:** Grants permission to put table replication configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [PutTableStorageClass](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_PutTableStorageClass.html)  **
  - **Description:** Grants permission to set or update the storage class configuration for a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:StorageClass](#list_s3tables-s3tables_StorageClass)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [RenameTable](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_RenameTable.html)  **
  - **Description:** Grants permission to rename a table or move a table across namespaces
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables-tagging.html)  **
  - **Description:** Grants permission to tag a S3 Tables resource
  - **Resource types (\*required):** [Table](#list_s3tables-resource-Table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3tables-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3tables-aws_TagKeys)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Resource types (\*required):** [TableBucket](#list_s3tables-resource-TableBucket) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3tables-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3tables-aws_TagKeys)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables-tagging.html)  **
  - **Description:** Grants permission to untag a S3 Tables resource
  - **Resource types (\*required):** [Table](#list_s3tables-resource-Table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3tables-aws_TagKeys)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Resource types (\*required):** [TableBucket](#list_s3tables-resource-TableBucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3tables-aws_TagKeys)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateTableMetadataLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_UpdateTableMetadataLocation.html)  **
  - **Description:** Grants permission to update the metadata location of a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write



## Permission-only actions for Amazon S3 Tables
<a name="list_s3tables-permission-only-actions"></a>

The following actions are defined by Amazon S3 Tables but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetTableData](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html#s3-tables-actions)  **
  - **Description:** Grants permission to read metadata and data objects from a table storage endpoint using S3 APIs
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Read

- **   [PutTableData](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html#s3-tables-actions)  **
  - **Description:** Grants permission to write metadata and data objects to a table storage endpoint using S3 APIs
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write

- **   [PutTableEncryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html#s3-tables-actions)  **
  - **Description:** Grants permission to put encryption configuration on a table
  - **Resource types (\*required):** [Table\*](#list_s3tables-resource-Table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:KMSKeyArn](#list_s3tables-s3tables_KMSKeyArn)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:SSEAlgorithm](#list_s3tables-s3tables_SSEAlgorithm)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName)
  - **Access level:** Write



## Resource types defined by Amazon S3 Tables
<a name="list_s3tables-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Table](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html)  | arn:${Partition}:s3tables:${Region}:${Account}:bucket/${TableBucketName}/table/${TableID} | [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_)<br />[s3tables:namespace](#list_s3tables-s3tables_namespace)<br />[s3tables:tableName](#list_s3tables-s3tables_tableName) | 
|  [TableBucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html)  | arn:${Partition}:s3tables:${Region}:${Account}:bucket/${TableBucketName} | [aws:ResourceTag/${TagKey}](#list_s3tables-aws_ResourceTag___TagKey_)<br />[s3tables:TableBucketTag/${TagKey}](#list_s3tables-s3tables_TableBucketTag___TagKey_) | 

## Condition keys for Amazon S3 Tables
<a name="list_s3tables-policy-keys"></a>

Amazon S3 Tables defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [s3tables:KMSKeyArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.htmls3-tables-setting-up.html)  | Filters access by the AWS KMS key ARN for the key used to encrypt a table | ARN | 
|   [s3tables:SSEAlgorithm](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.htmls3-tables-setting-up.html)  | Filters access by the server-side encryption algorithm used to encrypt a table | String | 
|   [s3tables:StorageClass](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.htmls3-tables-setting-up.html)  | Filters access by the storage class that can be set on tables under a table bucket | String | 
|   [s3tables:TableBucketTag/${TagKey}](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.htmls3-tables-setting-up.html)  | Filters access by the tags associated with the table bucket | String | 
|   [s3tables:namespace](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.htmls3-tables-setting-up.html)  | Filters access by the namespaces created in the table bucket | String | 
|   [s3tables:tableName](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.htmls3-tables-setting-up.html)  | Filters access by the name of the tables in the table bucket | String | 