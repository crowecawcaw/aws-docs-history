# Validating the view generation status

When you run the `CreateTable` or `UpdateTable` operations, the
`Status` field for the `GetTable` API output shows the details of
the view creation status. For `create` requests where the table does not already
exist, AWS Glue creates an empty table for the duration of the asynchronous process.
When calling `GetTable`, you can pass an optional boolean flag
`IncludeStatusDetails`, which shows diagnostic information about the
request. In the case of a failure, this flag shows an error message with individual
statuses of each dialect.

Errors during view create, read, update, and delete (CRUD) operations can occur either during processing in the AWS Glue/Lake Formation service or during view SQL validation in Amazon Redshift or Athena.
When an error occurs during validation in an engine, the AWS Glue service provides the error message that the engine returns.

###### Status fields

The following are the status fields:

- Status: a generic status, which is agnostic to different types of jobs:
  - QUEUED
  - IN_PROGRESS
  - SUCCESS
  - FAILED

- Action – Indicates which action was called on the table, currently only
  `CREATE` or `UPDATE` operations are
  available.

Distinguishing between `UPDATE` and
`CREATE` operations is important when
working with views. The operation type determines how you should proceed
with querying the tables.

An `UPDATE` operation signifies that the
table already exists in the Data Catalog. In this case, you can continue
querying the previously created table without any issues. On the other hand,
a `CREATE` operation indicates that the table
has never been successfully created before. If a table is marked for `CREATE`,
attempting to query it will fail because the table does not yet exist in the
system. Therefore, it is essential to identify the operation type (UPDATE or
CREATE) before attempting to query a table.

- RequestedBy – The ARN of the user who requested the asynchronous change.
- UpdatedBy – The ARN of the user who last manually alter the asynchronous change process, such
  as requesting a cancellation or modification.
- Error – This field only appears when the state is **FAILED**. This
  is a parent level exception message. There may be different errors for each
  dialect.
  - ErrorCode – The type of exception.
  - ErrorMessage – a brief description of the exception.

- RequestTime – an ISO 8601-formatted date string indicating the time that the change was initiated.
- UpdateTime – an ISO 8601-formatted date string indicating the time that the state was last updated.
