Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_STORED_PROC_CALL

You can query the system view SVL_STORED_PROC_CALL to get information about stored
procedure calls, including start time, end time, and whether a call is canceled. Each
stored procedure call receives a query ID.

SVL_STORED_PROC_CALL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_PROCEDURE_CALL](SYS_PROCEDURE_CALL.md "SYS_PROCEDURE_CALL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name    | Data type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid         | integer         | The ID of the user whose privileges were used to run the statement.<br>If this call was nested within a SECURITY DEFINER stored procedure, then this is the userid of the owner of that stored procedure.                                                                                                                                                                                                                  |
| session_userid | integer         | The ID of the user that created the session and is the invoker of the top-level stored procedure call.                                                                                                                                                                                                                                                                                                                     |
| query          | integer         | The query ID of the procedure call.                                                                                                                                                                                                                                                                                                                                                                                        |
| label          | character(320)  | Either the name of the file used to run the query<br>or a label defined with a SET QUERY_GROUP command. If the query is<br>not file-based or the QUERY_GROUP parameter isn't set, this<br>field value is default.                                                                                                                                                                                                          |
| xid            | bigint          | The transaction ID.                                                                                                                                                                                                                                                                                                                                                                                                        |
| pid            | integer         | The process ID. Usually, all of the queries in a<br>session are run in the same process, so this value usually remains<br>constant if you run a series of queries in the same session.<br>Following certain internal events, Amazon Redshift might restart an active<br>session and assign a new pid value. For more information, see [STL_RESTARTED_SESSIONS](r_STL_RESTARTED_SESSIONS.md "r_STL_RESTARTED_SESSIONS.md"). |
| database       | character(32)   | The name of the database that the user was<br>connected to when the query was issued.                                                                                                                                                                                                                                                                                                                                      |
| querytxt       | character(4000) | The actual text of the procedure call<br>query.                                                                                                                                                                                                                                                                                                                                                                            |
| starttime      | timestamp       | The time in UTC that the query started running,<br>with six digits of precision for fractional seconds, for example:<br>`2009-06-12 11:29:19.131358.`                                                                                                                                                                                                                                                                      |
| endtime        | timestamp       | The time in UTC that the query finished running,<br>with six digits of precision for fractional seconds, for example:<br>`2009-06-12 11:29:19.131358.`                                                                                                                                                                                                                                                                     |
| aborted        | integer         | If a stored procedure was stopped by the system or canceled by the user, this column contains 1. If the call runs to completion, this column contains 0.                                                                                                                                                                                                                                                                   |
| from_sp_call   | integer         | If the procedure call was invoked by another<br>procedure call, this column contains the query ID of the outer call.<br>Otherwise, the field is NULL.                                                                                                                                                                                                                                                                      |

## Sample query

The following query returns the elapsed time in descending order and the
completion status for stored procedure calls in the past day.

```
select query, datediff(seconds, starttime, endtime) as elapsed_time, aborted, trim(querytxt) as call from svl_stored_proc_call where starttime >= getdate() - interval '1 day' order by 2 desc;

  query | elapsed_time | aborted |                                       call
--------+--------------+---------+-----------------------------------------------------------------------------------
   4166 |            7 |       0 | call search_batch_status(35,'succeeded');
   2433 |            3 |       0 | call test_batch (123456)
   1810 |            1 |       0 | call prod_benchmark (123456)
   1836 |            1 |       0 | call prod_testing (123456)
   1808 |            1 |       0 | call prod_portfolio ('N', 123456)
   1816 |            1 |       1 | call prod_portfolio ('Y', 123456)

```
