Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_STORED_PROC_MESSAGES

You can query the system view SVL_STORED_PROC_MESSAGES to get information about stored procedure messages. Raised messages are logged even if the stored procedure call is canceled. Each stored procedure call receives a query ID. For more information about how to set the minimum level for logged messages, see stored_proc_log_min_messages.

SVL_STORED_PROC_MESSAGES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_PROCEDURE_MESSAGES](SYS_PROCEDURE_MESSAGES.md "SYS_PROCEDURE_MESSAGES.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name    | Data type       | Description                                                                                                                                                                                               |
| -------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid         | integer         | The ID of the user whose privileges were used to run the statement.<br>If this call was nested within a SECURITY DEFINER stored procedure, then this is the userid of the owner of that stored procedure. |
| session_userid | integer         | The ID of the user that created the session and is the invoker of the top-level stored procedure call.                                                                                                    |
| pid            | integer         | The process ID.                                                                                                                                                                                           |
| xid            | bigint          | The transaction ID of the procedure call query.                                                                                                                                                           |
| query          | integer         | The query ID of the procedure call.                                                                                                                                                                       |
| recordtime     | timestamp       | The time in UTC that the message was raised.                                                                                                                                                              |
| loglevel       | integer         | The numeric value of the log level of the raised message. Possible values:<br>20 – for LOG<br>30 – for INFO<br>40 – for NOTICE<br>50 – for WARNING<br>60 – for EXCEPTION                                  |
| loglevel_text  | character(10)   | The log level that corresponds to the numeric value in loglevel. Possible values: LOG, INFO, NOTICE, WARNING, and EXCEPTION.                                                                              |
| message        | character(1024) | The text of the raised message.                                                                                                                                                                           |
| linenum        | integer         | The line number of the raised statement.                                                                                                                                                                  |
| querytext      | character(500)  | The actual text of the procedure call query.                                                                                                                                                              |
| label          | character(320)  | Either the name of the file used to run the query or a label defined with a SET QUERY_GROUP command. If the query is not file-based or the QUERY_GROUP parameter isn't set, this field value is default.  |
| aborted        | integer         | If a stored procedure was stopped by the system or canceled by the user, this column contains 1. If the call runs to completion, this column contains 0.                                                  |
| message_xid    | bigint          | The transaction ID of the raised message.                                                                                                                                                                 |

## Sample query

The following SQL statements show how to use SVL_STORED_PROC_MESSAGES to review raised messages.

```
-- Create and run a stored procedure
CREATE OR REPLACE PROCEDURE test_proc1(f1 int) AS
$$
BEGIN
    RAISE INFO 'Log Level: Input f1 is %',f1;
    RAISE NOTICE 'Notice Level: Input f1 is %',f1;
    EXECUTE 'select invalid';
    RAISE NOTICE 'Should not print this';

EXCEPTION WHEN OTHERS THEN
     raise exception 'EXCEPTION level: Exception Handling';
END;
$$ LANGUAGE plpgsql;

-- Call this stored procedure
CALL test_proc1(2);

-- Show raised messages with level higher than INFO
SELECT query, recordtime, loglevel, loglevel_text, trim(message) as message, aborted FROM svl_stored_proc_messages
  WHERE loglevel > 30 AND query = 193 ORDER BY recordtime;

 query |         recordtime         | loglevel | loglevel_text |               message               | aborted
-------+----------------------------+----------+---------------+-------------------------------------+---------
   193 | 2020-03-17 23:57:18.277196 |       40 | NOTICE        | Notice Level: Input f1 is 2         |       1
   193 | 2020-03-17 23:57:18.277987 |       60 | EXCEPTION     | EXCEPTION level: Exception Handling |       1
(2 rows)

-- Show raised messages at EXCEPTION level
SELECT query, recordtime, loglevel, loglevel_text, trim(message) as message, aborted FROM svl_stored_proc_messages
  WHERE loglevel_text = 'EXCEPTION' AND query = 193 ORDER BY recordtime;

 query |         recordtime         | loglevel | loglevel_text |               message               | aborted
-------+----------------------------+----------+---------------+-------------------------------------+---------
   193 | 2020-03-17 23:57:18.277987 |       60 | EXCEPTION     | EXCEPTION level: Exception Handling |       1

```

The following SQL statements show how to use SVL_STORED_PROC_MESSAGES to review raised messages with the SET option when creating a stored procedure. Because test_proc() has a minimum log level of NOTICE, only NOTICE, WARNING, and EXCEPTION level messages are logged in SVL_STORED_PROC_MESSAGES.

```
-- Create a stored procedure with minimum log level of NOTICE
CREATE OR REPLACE PROCEDURE test_proc() AS
$$
BEGIN
    RAISE LOG 'Raise LOG messages';
    RAISE INFO 'Raise INFO messages';
    RAISE NOTICE 'Raise NOTICE messages';
    RAISE WARNING 'Raise WARNING messages';
    RAISE EXCEPTION 'Raise EXCEPTION messages';
    RAISE WARNING 'Raise WARNING messages again'; -- not reachable
END;
$$ LANGUAGE plpgsql SET stored_proc_log_min_messages = NOTICE;

-- Call this stored procedure
CALL test_proc();

-- Show the raised messages
SELECT query, recordtime, loglevel_text, trim(message) as message, aborted FROM svl_stored_proc_messages
  WHERE query = 149 ORDER BY recordtime;

 query |         recordtime         | loglevel_text |          message         | aborted
-------+----------------------------+---------------+--------------------------+---------
   149 | 2020-03-16 21:51:54.847627 | NOTICE        | Raise NOTICE messages    |       1
   149 | 2020-03-16 21:51:54.84766  | WARNING       | Raise WARNING messages   |       1
   149 | 2020-03-16 21:51:54.847668 | EXCEPTION     | Raise EXCEPTION messages |       1
(3 rows)

```
