Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CHANGE_SESSION_PRIORITY

CHANGE_SESSION_PRIORITY enables superusers to immediately change the priority of any session in the system.
Only one session, user, or query can run with the priority `CRITICAL`.

## Syntax

```
CHANGE_SESSION_PRIORITY(*pid*, *priority*)
```

## Arguments

_pid_

The process identifier of the session whose priority is changed. The
value `-1` refers to the current session. Requires an `INTEGER` value.

_priority_

The new priority to be assigned to the session. This argument must be a
string with the value `CRITICAL`, `HIGHEST`,
`HIGH`, `NORMAL`, `LOW`, or
`LOWEST`.

## Return type

None

## Examples

To return the process identifier of the server process
handling the current session, use the following example.

```
`SELECT pg_backend_pid();`

`+----------------+
| pg_backend_pid |
+----------------+
| 30311 |
+----------------+`
```

In this example, the priority is changed to
`LOWEST` for the current session.

```
`SELECT CHANGE_SESSION_PRIORITY(30311, 'Lowest');`

`+---------------------------------------------------------------------------------------+
| change_session_priority |
+---------------------------------------------------------------------------------------+
| Succeeded to change session priority. Changed session (pid:30311) priority to lowest. |
+---------------------------------------------------------------------------------------+`
```

In this example, the priority is changed to
`HIGH` for the current session.

```
`SELECT CHANGE_SESSION_PRIORITY(-1, 'High');`

`+-------------------------------------------------------------------------------------------------+
| change_session_priority |
+-------------------------------------------------------------------------------------------------+
| Succeeded to change session priority. Changed session (pid:30311) priority from lowest to high. |
+-------------------------------------------------------------------------------------------------+`
```

To create a stored procedure that changes a session priority, use the following example.
Permission to run this stored procedure is granted to the database user
`test_user`.

```
`CREATE OR REPLACE PROCEDURE sp_priority_low(pid IN int, result OUT varchar)
AS $$
BEGIN
 SELECT CHANGE_SESSION_PRIORITY(pid, 'low') into result;
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;
GRANT EXECUTE ON PROCEDURE sp_priority_low(int) TO test_user;`

```

Then the database user named `test_user` calls the procedure.

```
`CALL sp_priority_low(pg_backend_pid());`

`+------------------------------------------------------+
| result |
+------------------------------------------------------+
| Success. Change session (pid:13155) priority to low. |
+------------------------------------------------------+`
```
