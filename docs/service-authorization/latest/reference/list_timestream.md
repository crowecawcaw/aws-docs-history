

# Actions, resources, and condition keys for Amazon Timestream
<a name="list_timestream"></a>

Amazon Timestream (service prefix: `timestream`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/timestream/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/timestream/latest/developerguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/timestream/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/timestream/timestream.json) for this service.

**Topics**
+ [API operations defined by Amazon Timestream](#list_timestream-operations)
+ [Actions defined by Amazon Timestream](#list_timestream-actions-as-permissions)
+ [Resource types defined by Amazon Timestream](#list_timestream-resources-for-iam-policies)
+ [Condition keys for Amazon Timestream](#list_timestream-policy-keys)

## API operations defined by Amazon Timestream
<a name="list_timestream-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_timestream-actions-as-permissions).




- **   CancelQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:CancelQuery](#list_timestream-action-CancelQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateScheduledQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:CreateScheduledQuery](#list_timestream-action-CreateScheduledQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream:TagResource](#list_timestream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteScheduledQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:DeleteScheduledQuery](#list_timestream-action-DeleteScheduledQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountSettings  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:DescribeAccountSettings](#list_timestream-action-DescribeAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoints  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:DescribeEndpoints](#list_timestream-action-DescribeEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeScheduledQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:DescribeScheduledQuery](#list_timestream-action-DescribeScheduledQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ExecuteScheduledQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:ExecuteScheduledQuery](#list_timestream-action-ExecuteScheduledQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListScheduledQueries  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:ListScheduledQueries](#list_timestream-action-ListScheduledQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:ListTagsForResource](#list_timestream-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PrepareQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:Select](#list_timestream-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Query  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:DescribeTable](#list_timestream-action-DescribeTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [timestream:ListDatabases](#list_timestream-action-ListDatabases)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [timestream:ListMeasures](#list_timestream-action-ListMeasures)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [timestream:ListTables](#list_timestream-action-ListTables)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [timestream:Select](#list_timestream-action-Select)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [timestream:SelectValues](#list_timestream-action-SelectValues)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [timestream:Unload](#list_timestream-action-Unload)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:TagResource](#list_timestream-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:UntagResource](#list_timestream-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountSettings  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:UpdateAccountSettings](#list_timestream-action-UpdateAccountSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateScheduledQuery  **
  - **SDK client:** timestream-query
  - **IAM action:**  [timestream:UpdateScheduledQuery](#list_timestream-action-UpdateScheduledQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBatchLoadTask  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:CreateBatchLoadTask](#list_timestream-action-CreateBatchLoadTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream:WriteRecords](#list_timestream-action-WriteRecords)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDatabase  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:CreateDatabase](#list_timestream-action-CreateDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream:TagResource](#list_timestream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTable  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:CreateTable](#list_timestream-action-CreateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [timestream:TagResource](#list_timestream-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDatabase  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:DeleteDatabase](#list_timestream-action-DeleteDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTable  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:DeleteTable](#list_timestream-action-DeleteTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBatchLoadTask  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:DescribeBatchLoadTask](#list_timestream-action-DescribeBatchLoadTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatabase  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:DescribeDatabase](#list_timestream-action-DescribeDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoints  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:DescribeEndpoints](#list_timestream-action-DescribeEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTable  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:DescribeTable](#list_timestream-action-DescribeTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBatchLoadTasks  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:ListBatchLoadTasks](#list_timestream-action-ListBatchLoadTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatabases  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:ListDatabases](#list_timestream-action-ListDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTables  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:ListTables](#list_timestream-action-ListTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:ListTagsForResource](#list_timestream-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:TagResource](#list_timestream-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:UntagResource](#list_timestream-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDatabase  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:UpdateDatabase](#list_timestream-action-UpdateDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTable  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:UpdateTable](#list_timestream-action-UpdateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   WriteRecords  **
  - **SDK client:** timestream-write
  - **IAM action:**  [timestream:WriteRecords](#list_timestream-action-WriteRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Timestream
<a name="list_timestream-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_CancelQuery.html)  **
  - **Description:** Grants permission to cancel queries in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_CreateBatchLoadTask.html)  **
  - **Description:** Grants permission to create a batch load task in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDatabase](https://docs.aws.amazon.com/timestream/latest/developerguide/API_CreateDatabase.html)  **
  - **Description:** Grants permission to create a database in your account
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScheduledQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_CreateScheduledQuery.html)  **
  - **Description:** Grants permission to create a scheduled query in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTable](https://docs.aws.amazon.com/timestream/latest/developerguide/API_CreateTable.html)  **
  - **Description:** Grants permission to create a table in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDatabase](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DeleteDatabase.html)  **
  - **Description:** Grants permission to delete a database in your account
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScheduledQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DeleteScheduledQuery.html)  **
  - **Description:** Grants permission to delete a scheduled query in your account
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTable](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DeleteTable.html)  **
  - **Description:** Grants permission to delete a table in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountSettings](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_DescribeAccountSettings.html)  **
  - **Description:** Grants permission to describe your account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeBatchLoadTask.html)  **
  - **Description:** Grants permission to describe a batch load task in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDatabase](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeDatabase.html)  **
  - **Description:** Grants permission to describe a database in your account
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpoints](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeEndpoints.html)  **
  - **Description:** Grants permission to describe timestream endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeScheduledQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeScheduledQuery.html)  **
  - **Description:** Grants permission to describe a scheduled query in your account
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTable](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeTable.html)  **
  - **Description:** Grants permission to describe a table in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExecuteScheduledQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ExecuteScheduledQuery.html)  **
  - **Description:** Grants permission to execute a scheduled query in your account
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAwsBackupStatus](https://docs.aws.amazon.com/timestream/latest/developerguide/backups.html)  **
  - **Description:** Grants permission to get Status of a Timestream Table Backup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAwsRestoreStatus](https://docs.aws.amazon.com/timestream/latest/developerguide/backups.html)  **
  - **Description:** Grants permission to get Status of a Timestream Table Restore
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListBatchLoadTasks](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListBatchLoadTasks.html)  **
  - **Description:** Grants permission to list batch load tasks in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatabases](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListDatabases.html)  **
  - **Description:** Grants permission to list databases in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMeasures](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_Query.html)  **
  - **Description:** Grants permission to list measures of a table in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListScheduledQueries](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListScheduledQueries.html)  **
  - **Description:** Grants permission to list scheduled queries in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTables](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListTables.html)  **
  - **Description:** Grants permission to list tables in your account
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags of a resource in your account
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PrepareQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_PrepareQuery.html)  **
  - **Description:** Grants permission to issue prepare queries
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ResumeBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ResumeBatchLoadTask.html)  **
  - **Description:** Grants permission to resume a batch load task in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Select](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_Query.html)  **
  - **Description:** Grants permission to issue 'select from table' queries
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SelectValues](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_Query.html)  **
  - **Description:** Grants permission to issue 'select 1' queries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartAwsBackupJob](https://docs.aws.amazon.com/timestream/latest/developerguide/backups.html)  **
  - **Description:** Grants permission to start a Backup Job for a Timestream Table
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAwsRestoreJob](https://docs.aws.amazon.com/timestream/latest/developerguide/backups.html)  **
  - **Description:** Grants permission to start Restore Job for a Backup of Timestream Table
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/timestream/latest/developerguide/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_timestream-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [Unload](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_Query.html)  **
  - **Description:** Grants permission to issue Unload queries
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/timestream/latest/developerguide/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_timestream-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/timestream/latest/developerguide/API_query_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update your account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDatabase](https://docs.aws.amazon.com/timestream/latest/developerguide/API_UpdateDatabase.html)  **
  - **Description:** Grants permission to update a database in your account
  - **Resource types (\*required):** [database\*](#list_timestream-resource-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateScheduledQuery](https://docs.aws.amazon.com/timestream/latest/developerguide/API_UpdateScheduledQuery.html)  **
  - **Description:** Grants permission to update a scheduled query in your account
  - **Resource types (\*required):** [scheduled-query\*](#list_timestream-resource-scheduled-query)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTable](https://docs.aws.amazon.com/timestream/latest/developerguide/API_UpdateTable.html)  **
  - **Description:** Grants permission to update a table in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [WriteRecords](https://docs.aws.amazon.com/timestream/latest/developerguide/API_WriteRecords.html)  **
  - **Description:** Grants permission to ingest data to a table in your account
  - **Resource types (\*required):** [table\*](#list_timestream-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Timestream
<a name="list_timestream-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [database](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Database.html)  | arn:${Partition}:timestream:${Region}:${Account}:database/${DatabaseName} | [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_) | 
|  [scheduled-query](https://docs.aws.amazon.com/timestream/latest/developerguide/API_ScheduledQuery.html)  | arn:${Partition}:timestream:${Region}:${Account}:scheduled-query/${ScheduledQueryName} | [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_) | 
|  [table](https://docs.aws.amazon.com/timestream/latest/developerguide/API_Table.html)  | arn:${Partition}:timestream:${Region}:${Account}:database/${DatabaseName}/table/${TableName} | [aws:ResourceTag/${TagKey}](#list_timestream-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Timestream
<a name="list_timestream-policy-keys"></a>

Amazon Timestream defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/timestream/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/timestream/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/timestream/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the presence of tag keys in the request | ArrayOfString | 