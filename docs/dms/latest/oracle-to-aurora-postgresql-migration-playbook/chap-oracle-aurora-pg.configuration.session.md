

# Oracle and PostgreSQL session parameters
<a name="chap-oracle-aurora-pg.configuration.session"></a>

With AWS DMS, you can configure session parameters for Oracle and PostgreSQL databases to optimize performance and customize behavior during migration tasks. Session parameters are special configuration options that influence how the database engine operates and processes data.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-1.png)  | N/A | N/A | SET options are significantly different in PostgreSQL. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.configuration.session.ora"></a>

Certain Oracle database parameters and configuration options are modifiable at the session level using the `ALTER SESSION` command. However, not all Oracle configuration options and parameters can be modified on a per-session basis. To view a list of all configurable parameters that can be set for the scope of a specific session, query the `v$parameter` view as shown in the following example.

```
SELECT NAME, VALUE FROM V$PARAMETER WHERE ISSES_MODIFIABLE='TRUE';
```

 **Examples** 

Change the `NLS_LANAUGE` codepage parameter of the current session.

```
alter session set nls_language='SPANISH'

Sesi≤n modificada.

alter session set nls_language='ENGLISH';

Session altered.

alter session set nls_language='FRENCH';

Session modifiΘe.

alter session set nls_language='GERMAN';

Session wurde geΣndert.
```

Specify the format of date values returned from the database using the `NLS_DATE_FORMAT` session parameter.

```
select sysdate from dual;

SYSDATE
SEP-09-17

alter session set nls_date_format='DD-MON-RR';

Session altered.

select sysdate from dual;

SYSDATE
09-SEP-17

alter session set nls_date_format='MM-DD-YYYY';

Session altered.

select sysdate from dual;

SYSDATE
09-09-2017

alter session set nls_date_format='DAY-MON-RR';

Session altered.
```

For more information, see [Changing Parameter Values in a Parameter File](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html#GUID-4C578B21-DE2B-4210-8EB7-EF28D36CC1CB) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.configuration.session.pg"></a>

PostgreSQL provides session-modifiable parameters that are configured using the `SET SESSION` command. Configuration of parameters using `SET SESSION` will only be applicable in the current session. To view the list of parameters that can be set with `SET SESSION`, you can query `pg_settings`.

```
SELECT * FROM pg_settings where context = 'user';
```

Find the commonly used session parameters following:
+  `client_encoding` configures the connected client character set.
+  `force_parallel_mode` forces use of parallel query for the session.
+  `lock_timeout` sets the maximum allowed duration of time to wait for a database lock to release.
+  `search_path` sets the schema search order for object names that are not schema-qualified.
+  `transaction_isolation` sets the current Transaction Isolation Level for the session.

 **Examples** 

Change the Time zone of the connected session.

```
set session DateStyle to POSTGRES, DMY;
SET

select now();

now
Sat 09 Sep 11:03:43.597202 2017 UTC
(1 row)

set session DateStyle to ISO, MDY;
SET

select now();

now
2017-09-09 11:04:01.3859+00
(1 row)
```

## Summary
<a name="chap-oracle-aurora-pg.configuration.session.summary"></a>

The following table includes a partial list of parameters and is meant to highlight various session-level configuration parameters in both Oracle and PostgreSQL. Not all parameters are directly comparable.


| Parameter purpose | Oracle | PostgreSQL | 
| --- | --- | --- | 
| Configure time and date format |  <pre>ALTER SESSION<br />  SET nls_date_format =<br />    'dd/mm/yyyy hh24:mi:ss';</pre>  |  <pre>SET SESSION<br />  datestyle to 'SQL, DMY';</pre>  | 
| Configure the current default schema or database |  <pre>ALTER SESSION<br />  SET current schema='schema_name'</pre>  |  <pre>SET SESSION<br />  SEARCH_PATH TO schemaname;</pre>  | 
| Generate traces for specific errors |  <pre>ALTER SESSION SET<br />  events '10053 trace name<br />    context forever';</pre>  | N/A | 
| Run trace for a SQL statement |  <pre>ALTER SESSION<br />  SET sql_trace=TRUE;<br />ALTER SYSTEM<br />  SET EVENTS 'sql_trace<br />    [sql:&&sql_id]<br />    bindd=true, wait=true';</pre>  | N/A | 
| Modify query optimizer cost for index access |  <pre>ALTER SESSION<br />  SET optimizer_index_cost_adj = 50</pre>  |  <pre>SET SESSION random_page_cost TO 6;</pre>  | 
| Modify query optimizer row access strategy |  <pre>ALTER SESSION<br />  SET optimizer_mode=all_rows;</pre>  | N/A | 
| Memory allocated to sort operations |  <pre>ALTER SESSION<br />  SET sort_area_size=6321;</pre>  |  <pre>SET SESSION work_mem TO '6MB';</pre>  | 
| Memory allocated to hash joins |  <pre>ALTER SESSION<br />  SET hash_area_size=1048576000;</pre>  |  <pre>SET SESSION work_mem TO '6MB';</pre>  | 

For more information, see [SET](https://www.postgresql.org/docs/13/sql-set.html) in the *PostgreSQL documentation*.