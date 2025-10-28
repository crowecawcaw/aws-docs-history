Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query the system tables and views

In addition to the tables that you create, your data warehouse contains a number of system
tables and views. These tables and views contain information about your installation and the
various queries and processes that are running on the system. You can query these system
tables and views to collect information about your database. For more information, see
[System tables and views reference](../dg/cm_chap_system-tables.md "../dg/cm_chap_system-tables.md")
in the _Amazon Redshift Database Developer Guide_. The description for each table or view indicates whether a table is
visible to all users or only to superusers. Log in as a superuser to query tables
that are visible only to superusers.

## View a

list of table names

To view a list of all tables in a schema, you
can query the PG_TABLE_DEF system catalog table. You can first examine the setting for `search_path`.

```
SHOW search_path;
```

The result should look similar to the following,

```
  search_path
---------------
 $user, public
```

The following example adds the `SALES` schema to the search path and shows all the tables in the `SALES` schema.

```
`set search_path to '$user', 'public', 'sales';`

`SHOW search_path;`
`search_path
------------------------
 "$user", public, sales`


`select * from pg_table_def where schemaname = 'sales';`
`schemaname | tablename | column | type | encoding | distkey | sortkey | notnull
------------+-----------+----------+------------------------+----------+---------+---------+---------
 sales | demo | personid | integer | az64 | f | 0 | f
 sales | demo | city | character varying(255) | lzo | f | 0 | f`
```

The following example shows a list of all tables called `DEMO` in all schemas on the current database.

```
`set search_path to '$user', 'public', 'sales';`
`select * from pg_table_def where tablename = 'demo';`
`schemaname | tablename | column | type | encoding | distkey | sortkey | notnull
------------+-----------+----------+------------------------+----------+---------+---------+---------
 public | demo | personid | integer | az64 | f | 0 | f
 public | demo | city | character varying(255) | lzo | f | 0 | f
 sales | demo | personid | integer | az64 | f | 0 | f
 sales | demo | city | character varying(255) | lzo | f | 0 | f`
```

For more information, see [PG_TABLE_DEF](../dg/r_PG_TABLE_DEF.md "../dg/r_PG_TABLE_DEF.md").

You can also use the Amazon Redshift query editor v2 to view all the tables in a specified
schema by first choosing a database that you want to connect to.

## View users

You can query the PG_USER catalog to view a list of all users, along with the user
ID (USESYSID) and user privileges.

```
`SELECT * FROM pg_user;`
`usename | usesysid | usecreatedb | usesuper | usecatupd | passwd | valuntil | useconfig
------------+----------+-------------+----------+-----------+----------+----------+-----------
 rdsdb | 1 | true | true | true | ******** | infinity |
 awsuser | 100 | true | true | false | ******** | |
 guest | 104 | true | false | false | ******** | |`
```

The user name `rdsdb` is used internally by Amazon Redshift to perform routine
administrative and maintenance tasks. You can filter your query to show only
user-defined user names by adding `where usesysid > 1` to your SELECT
statement.

```
`SELECT * FROM pg_user WHERE usesysid > 1;`
`usename | usesysid | usecreatedb | usesuper | usecatupd | passwd | valuntil | useconfig
------------+----------+-------------+----------+-----------+----------+----------+-----------
 awsuser | 100 | true | true | false | ******** | |
 guest | 104 | true | false | false | ******** | |`
```

## View recent queries

In the previous example, the user ID (user_id) for `adminuser` is 100.
To list the four most recent queries run by `adminuser`, you can query
the SYS_QUERY_HISTORY view.

You can use this view to find the query ID (query_id) or process ID (session_id) for a
recently run query. You can also use this view to check how long it took a query to
complete. SYS_QUERY_HISTORY includes the first 4,000 characters of the query string (query_text)
to help you locate a specific query. Use the LIMIT clause with your SELECT statement
to limit the results.

```
`SELECT query_id, session_id, elapsed_time, query_text
FROM sys_query_history
WHERE user_id = 100
ORDER BY start_time desc
LIMIT 4;`
```

The result look something like the following.

```
 query_id |  session_id  |  elapsed_time |   query_text
----------+--------------+---------------+----------------------------------------------------------------
 892      |    21046     |       55868   | SELECT query, pid, elapsed, substring from ...
 620      |    17635     |     1296265   | SELECT query, pid, elapsed, substring from ...
 610      |    17607     |       82555   | SELECT * from DEMO;
 596      |    16762     |      226372   | INSERT INTO DEMO VALUES (100);
```

## Determine the session ID of a running query

To retrieve system table information about a query, you might need to specify the
session ID (process ID) associated with that query. Or, you might need to find the session ID for a query that is still running.
For example, you
need the session ID if you need to cancel a query that is taking too long to run on a provisioned cluster. You can
query the STV_RECENTS system table to obtain a list of session IDs for running
queries, along with the corresponding query string. If your query returns multiple
session, you can look at the query text to determine which session ID you need.

To determine the session ID of a running query, run the following SELECT
statement.

```
SELECT session_id, user_id, start_time, query_text
FROM sys_query_history
WHERE status='running';
```
