

# Actions, resources, and condition keys for Amazon QLDB
<a name="list_qldb"></a>

Amazon QLDB (service prefix: `qldb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/qldb/latest/developerguide/index.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/qldb/latest/developerguide/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/qldb/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/qldb/qldb.json) for this service.

**Topics**
+ [Actions defined by Amazon QLDB](#list_qldb-actions-as-permissions)
+ [Permission-only actions for Amazon QLDB](#list_qldb-permission-only-actions)
+ [Resource types defined by Amazon QLDB](#list_qldb-resources-for-iam-policies)
+ [Condition keys for Amazon QLDB](#list_qldb-policy-keys)

## Actions defined by Amazon QLDB
<a name="list_qldb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelJournalKinesisStream](https://docs.aws.amazon.com/qldb/latest/developerguide/API_CancelJournalKinesisStream.html)  **
  - **Description:** Grants permission to cancel a journal kinesis stream
  - **Resource types (\*required):** [stream\*](#list_qldb-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_CreateLedger.html)  **
  - **Description:** Grants permission to create a ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DeleteLedger.html)  **
  - **Description:** Grants permission to delete a ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeJournalKinesisStream](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalKinesisStream.html)  **
  - **Description:** Grants permission to describe information about a journal kinesis stream
  - **Resource types (\*required):** [stream\*](#list_qldb-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJournalS3Export](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalS3Export.html)  **
  - **Description:** Grants permission to describe information about a journal export job
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeLedger.html)  **
  - **Description:** Grants permission to describe a ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExportJournalToS3](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ExportJournalToS3.html)  **
  - **Description:** Grants permission to export journal contents to an Amazon S3 bucket
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBlock](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetBlock.html)  **
  - **Description:** Grants permission to retrieve a block from a ledger for a given BlockAddress
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDigest](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetDigest.html)  **
  - **Description:** Grants permission to retrieve a digest from a ledger for a given BlockAddress
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRevision](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetRevision.html)  **
  - **Description:** Grants permission to retrieve a revision for a given document ID and a given BlockAddress
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListJournalKinesisStreamsForLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalKinesisStreamsForLedger.html)  **
  - **Description:** Grants permission to list journal kinesis streams for a specified ledger
  - **Resource types (\*required):** [stream\*](#list_qldb-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJournalS3Exports](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3Exports.html)  **
  - **Description:** Grants permission to list journal export jobs for all ledgers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJournalS3ExportsForLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3ExportsForLedger.html)  **
  - **Description:** Grants permission to list journal export jobs for a specified ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLedgers](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListLedgers.html)  **
  - **Description:** Grants permission to list existing ledgers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [catalog](#list_qldb-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ledger](#list_qldb-resource-ledger) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream](#list_qldb-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table](#list_qldb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PartiQLCreateIndex](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.create-index.html)  **
  - **Description:** Grants permission to create an index on a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PartiQLCreateTable](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.create-table.html)  **
  - **Description:** Grants permission to create a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Access level:** Write

- **   [PartiQLDelete](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.delete.html)  **
  - **Description:** Grants permission to delete documents from a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PartiQLDropIndex](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.drop-index.html)  **
  - **Description:** Grants permission to drop an index from a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[qldb:Purge](#list_qldb-qldb_Purge)
  - **Access level:** Write

- **   [PartiQLDropTable](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.drop-table.html)  **
  - **Description:** Grants permission to drop a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[qldb:Purge](#list_qldb-qldb_Purge)
  - **Access level:** Write

- **   [PartiQLHistoryFunction](https://docs.aws.amazon.com/qldb/latest/developerguide/working.history.html)  **
  - **Description:** Grants permission to use the history function on a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PartiQLInsert](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.insert.html)  **
  - **Description:** Grants permission to insert documents into a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PartiQLRedact](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-stored-procedures.redact_revision.html)  **
  - **Description:** Grants permission to redact historic revisions
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PartiQLSelect](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.select.html)  **
  - **Description:** Grants permission to select documents from a table
  - **Resource types (\*required):** [catalog](#list_qldb-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table](#list_qldb-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PartiQLUndropTable](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.undrop-table.html)  **
  - **Description:** Grants permission to undrop a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PartiQLUpdate](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.update.html)  **
  - **Description:** Grants permission to update existing documents in a table
  - **Resource types (\*required):** [table\*](#list_qldb-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendCommand](https://docs.aws.amazon.com/qldb/latest/developerguide/API_QLDB-Session_SendCommand.html)  **
  - **Description:** Grants permission to send commands to a ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StreamJournalToKinesis](https://docs.aws.amazon.com/qldb/latest/developerguide/API_StreamJournalToKinesis.html)  **
  - **Description:** Grants permission to stream journal contents to a Kinesis Data Stream
  - **Resource types (\*required):** [stream\*](#list_qldb-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/qldb/latest/developerguide/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a resource
  - **Resource types (\*required):** [catalog](#list_qldb-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Resource types (\*required):** [ledger](#list_qldb-resource-ledger) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_qldb-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_qldb-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/qldb/latest/developerguide/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a resource
  - **Resource types (\*required):** [catalog](#list_qldb-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Resource types (\*required):** [ledger](#list_qldb-resource-ledger) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_qldb-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_qldb-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_qldb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_qldb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateLedger](https://docs.aws.amazon.com/qldb/latest/developerguide/API_UpdateLedger.html)  **
  - **Description:** Grants permission to update properties on a ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLedgerPermissionsMode](https://docs.aws.amazon.com/qldb/latest/developerguide/API_UpdateLedgerPermissionsMode.html)  **
  - **Description:** Grants permission to update the permissions mode on a ledger
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon QLDB
<a name="list_qldb-permission-only-actions"></a>

The following actions are defined by Amazon QLDB but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ExecuteStatement](https://docs.aws.amazon.com/qldb/latest/developerguide/console_QLDB.html)  **
  - **Description:** Grants permission to send commands to a ledger via the console
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InsertSampleData](https://docs.aws.amazon.com/qldb/latest/developerguide/console_QLDB.html)  **
  - **Description:** Grants permission to insert sample application data via the console
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ShowCatalog](https://docs.aws.amazon.com/qldb/latest/developerguide/console_QLDB.html)  **
  - **Description:** Grants permission to view a ledger's catalog via the console
  - **Resource types (\*required):** [ledger\*](#list_qldb-resource-ledger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon QLDB
<a name="list_qldb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [catalog](https://docs.aws.amazon.com/qldb/latest/developerguide/working.catalog.html)  | arn:${Partition}:qldb:${Region}:${Account}:ledger/${LedgerName}/information\_schema/user\_tables | [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_) | 
|  [ledger](https://docs.aws.amazon.com/qldb/latest/developerguide/ledger-structure.html)  | arn:${Partition}:qldb:${Region}:${Account}:ledger/${LedgerName} | [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_) | 
|  [stream](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html)  | arn:${Partition}:qldb:${Region}:${Account}:stream/${LedgerName}/${StreamId} | [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_) | 
|  [table](https://docs.aws.amazon.com/qldb/latest/developerguide/working.manage-tables.html)  | arn:${Partition}:qldb:${Region}:${Account}:ledger/${LedgerName}/table/${TableId} | [aws:ResourceTag/${TagKey}](#list_qldb-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon QLDB
<a name="list_qldb-policy-keys"></a>

Amazon QLDB defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [qldb:Purge](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-purge)  | Filters access by the value of purge that is specified in a PartiQL DROP statement | String | 