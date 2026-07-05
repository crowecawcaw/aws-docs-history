Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_LUDF\_DETAIL

SYS\_LUDF\_DETAIL records information and metrics for Lambda User Defined Functions (LUDFs) that were used in a particular query.

SYS\_LUDF\_DETAIL is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name            | Data type | Description                                                                                                                                                                                          |
| ---------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user\_id               | integer   | The identifier of the user who submitted the query calling the function.                                                                                                                             |
| transaction\_id        | bigint    | The transaction identifier.                                                                                                                                                                          |
| query\_id              | bigint    | User query identifier.                                                                                                                                                                               |
| function\_oid          | bigint    | Object id of the function in the catalog.                                                                                                                                                            |
| function\_position     | integer   | Numerical position of this function in the step. For example, if there are multiple calls of the same function in the SELECT list of a query, they can be identified using these positional numbers. |
| stream\_id             | integer   | The stream identifier the function call was performed in.                                                                                                                                            |
| segment\_id            | integer   | The segment identifier the function call was performed in.                                                                                                                                           |
| step\_id               | integer   | The step identifier the function call performed in.                                                                                                                                                  |
| lambda\_function\_name | char(256) | Name of the lambda function.                                                                                                                                                                         |
| start\_time            | timestamp | The time the calls started at.                                                                                                                                                                       |
| end\_time              | timestamp | The time the calls ended at.                                                                                                                                                                         |
| total\_duration        | bigint    | The total duration of the calls in microseconds.                                                                                                                                                     |
| invocations            | integer   | The number of concurrent or external invocations.                                                                                                                                                    |
| total\_rows            | bigint    | The number of rows passed/returned to/from the call.                                                                                                                                                 |
| input\_bytes           | bigint    | The number of bytes passed to the call.                                                                                                                                                              |
| output\_bytes          | bigint    | The number of bytes the call produced.                                                                                                                                                               |

## Sample queries

The following example uses a Lambda UDF in a query, and then shows how to query the SYS\_LUDF\_DETAIL view to see the function execution details.

```
`SET SESSION AUTHORIZATION regular_user;

CREATE EXTERNAL FUNCTION exfunc_sum(INT,INT) RETURNS INT STABLE
LAMBDA 'lambda_sum'
IAM_ROLE 'arn:aws:iam::123456789012:role/Redshift-Exfunc-Test';

CREATE TABLE t_sum(c1 int, c2 int);
INSERT INTO t_sum VALUES (4,5), (6,7);
SELECT exfunc_sum(c1,c2) FROM t_sum;

-- Switch to super user in order to inspect records in the LUDF SYS view.
SET SESSION AUTHORIZATION super_user;
select * from sys_ludf_detail;`
```

Sample output:

```
 user_id | transaction_id | query_id | function_oid | function_position | stream_id | segment_id | step_id | lambda_function_name |         start_time         |          end_time          | total_duration | invocations | total_rows | input_bytes | output_bytes
---------+----------------+----------+--------------+-------------------+-----------+------------+---------+----------------------+----------------------------+----------------------------+----------------+-------------+------------+-------------+--------------
     100 |           1463 |     1544 |       111055 |                 0 |         0 |          0 |       2 | lambda_sum           | 2026-01-06 17:23:25.165898 | 2026-01-06 17:23:25.165898 |            414 |           1 |          2 |         277 |           18
(1 row)
```
