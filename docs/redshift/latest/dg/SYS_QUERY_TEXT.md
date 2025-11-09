Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_QUERY_TEXT

Use SYS_QUERY_TEXT to view the query text of all queries. Each row represents the
query text of queries up to 4000 characters starting with sequence number 0. When the
query statement contains more than 4000 characters, additional rows are logged for the
statement by incrementing the sequence number for each row. This view logs all user
query text such as DDL, utility, Amazon Redshift queries, and leader-node only queries.

SYS_QUERY_TEXT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type        | Description                                                                                                                                                                  |
| -------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id        | integer          | The identifier of the user who submitted the<br>query.                                                                                                                       |
| query_id       | bigint           | The query identifier.                                                                                                                                                        |
| transaction_id | bigint           | The identifier of the transaction associated with<br>the statement.                                                                                                          |
| session_id     | integer          | The process identifier of the session running the<br>query.                                                                                                                  |
| start_time     | timestamp        | The time when the query starts.                                                                                                                                              |
| sequence       | integer          | When a single statement contains more than 4000<br>characters, additional rows are logged for the statement. Sequence 0<br>is the first row, 1 is the second row, and so on. |
| text           | character (4000) | The text of the SQL query that is in<br>4000-character increments. This field might contain special<br>characters, such as backslash (\) and newline (\n).                   |

## Sample queries

The following query returns running and queued queries.

```
SELECT user_id,
 query_id,
 transaction_id,
 session_id, start_time,
 sequence, trim(text) as text from sys_query_text
 ORDER BY sequence;
```

Sample output.

```
 user_id | query_id | transaction_id | session_id |        start_time          | sequence |                                                        text
--------+----------+-----------------+------------+----------------------------+----------+----------------------------------------------------------------------------------------------------------------------
   100  |     4    |       1396      | 1073750220 | 2023-04-28 16:44:55.887184 |     0    | SELECT trim(text) as text, sequence FROM sys_query_text WHERE query_id = pg_last_query_id() AND user_id > 1 AND start
_time > '2023-04-28 16:44:55.922705+00:00'::timestamp order by sequence;
```

The following query returns the permissions that have been granted or revoked from
groups in your database.

```
`SELECT
 SPLIT_PART(text, ' ', 1) as grantrevoke,
 SPLIT_PART((SUBSTRING(text, STRPOS(UPPER(text), 'GROUP'))), ' ', 2) as group,
 SPLIT_PART((SUBSTRING(text, STRPOS(UPPER(text), ' '))), 'ON', 1) as type,
 SPLIT_PART((SUBSTRING(text, STRPOS(UPPER(text), 'ON'))), ' ', 2) || ' ' || SPLIT_PART((SUBSTRING(text, STRPOS(UPPER(text), 'ON'))), ' ', 3) as entity
FROM SYS_QUERY_TEXT
WHERE (text LIKE 'GRANT%' OR text LIKE 'REVOKE%') AND text LIKE '%GROUP%';`

`+-------------+----------+--------+----------+
| grantrevoke | group | type | entity |
+-------------+----------+--------+----------+
| GRANT | bi_group | SELECT | TABLE t1 |
| GRANT | bi_group | SELECT | TABLE t1 |
| GRANT | bi_group | SELECT | TABLE t1 |
| GRANT | bi_group | USAGE | TABLE t1 |
| GRANT | bi_group | SELECT | TABLE t1 |
| GRANT | bi_group | SELECT | TABLE t1 |
+-------------+----------+--------+----------+`
```
