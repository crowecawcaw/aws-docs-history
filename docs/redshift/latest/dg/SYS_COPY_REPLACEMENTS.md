Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_COPY_REPLACEMENTS

Displays a log that records when invalid UTF-8 characters were replaced by the [COPY](r_COPY.md "r_COPY.md") command with the ACCEPTINVCHARS option. A
log entry is added to SYS_COPY_REPLACEMENTS for each of the first 100 rows on each node
slice that required at least one replacement.

You can use this view to see information about serverless workgroups and provisioned
clusters.

SYS_COPY_REPLACEMENTS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type       | Description                                                                                                                                                                           |
| ----------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------- | ----------- | ------------------------------------------------------------------------------------------------------------------ | --- | ----------------------------------------- | --- | ------- | --- | ----------------------------------------- | --- | ------- | --- | ----------------------------------------- | --- | ------- | --- | ----------------------------------------- | --- | ------- | --- | ----------------------------------------- | --- | ------------- |
| user_id     | integer         | ID of the user who generated the query.                                                                                                                                               |
| query_id    | bigint          | The query ID. The column used to join other system tables and views.                                                                                                                  |
| table_id    | integer         | The table ID.                                                                                                                                                                         |
| file_name   | character(256)  | The complete path to the input file for the COPY command.                                                                                                                             |
| column_name | character(127)  | The first field that contains an invalid UTF-8 character.                                                                                                                             |
| line_number | bigint          | The line number in the input data file that containes an invalid UTF-8 character. -1 indicates that the line number is not available, such as when copying from a columnar data file. |
| raw_line    | character(1024) | The raw load data that contains an invalid UTF-8 character.                                                                                                                           | ## Sample queries The following example returns replacements for the most recent COPY operation. ``` `select query_idp, table_id, file_name, line_number, colname from sys_copy_replacements where query = pg_last_copy_id();` `query_id | table_id | file_name | line_number | column_name ---------+----------+-------------------------------------------------------+-------------+-------- 96 | 26  | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt | 123 | city 96 | 26  | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt | 456 | city 96 | 26  | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt | 789 | city 96 | 26  | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt | 012 | city 96 | 26  | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt | 119 | city ...` ``` |
