# Oracle session parameters and MySQL session variables

With AWS DMS, you can configure Oracle session parameters and MySQL session variables to optimize performance, control resource usage, and customize database behavior during migration tasks. Oracle session parameters and MySQL session variables are special configuration settings that influence how the database engine operates and processes data. These settings can be crucial for ensuring efficient data transfer, minimizing resource contention, and adhering to organizational policies or regulatory requirements.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                            |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------------ |
| One star feature compatibility | N/A                                | N/A                       | `SET` options are significantly different. |

## Oracle usage

Certain Oracle database parameters and configuration options are modifiable at the session level using the `ALTER SESSION` command. However, not all Oracle configuration options and parameters can be modified on a per-session basis. To view a list of all configurable parameters that can be set for the scope of a specific session, query the v$parameter view as shown in the following example.

```
SELECT NAME, VALUE FROM V$PARAMETER WHERE ISSES_MODIFIABLE='TRUE';
```

### Examples

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

For more information, see [Changing Parameter Values in a Parameter File](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html#GUID-4C578B21-DE2B-4210-8EB7-EF28D36CC1CB "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html#GUID-4C578B21-DE2B-4210-8EB7-EF28D36CC1CB") in the _Oracle documentation_.

## MySQL usage

MySQL provides session-modifiable parameters configured using the `SET SESSION` command. Configuration of parameters using `SET SESSION` is only applicable in the current session. To view the list of parameters that you can set with `SET SESSION`, see [Dynamic System Variables](https://dev.mysql.com/doc/refman/5.7/en/dynamic-system-variables.html "https://dev.mysql.com/doc/refman/5.7/en/dynamic-system-variables.html") and search for variables with session scope.

Examples of commonly used session parameters:

- `autocommit` — Specify if changes take effect immediately or if an explicit COMMIT command is required.
- `character_set_client` — Set the character set for the client.
- `default_storage_engine` — Set the default storage engine.
- `foreign_key_checks` — Set whether or not to run FK checks.
- `innodb_lock_wait_timeout` — Set how much time the transaction should wait to acquire a row lock.

### Examples

Change the time zone of the connected session.

```
SELECT now();

now()
2018-02-26 12:13:25

SET SESSION TIME_ZONE = '+10:00';
SELECT now();

now()
2018-02-26 22:14:03
```

You can also use a time zone name such as `Europe/Helsinki` instead of `+10:00`.

## Oracle and MySQL session parameter examples

| Parameter purpose                                | Oracle                                                                                                                              | MySQL                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Configure time and date format                   | `<br>ALTER SESSION<br>SET nls_date_format = 'dd/mm/yyyy hh24:mi:ss';<br>`                                                           | N/A                                                                                                                                                                                                                                                                                                                      |
| Configure the current default schema or database | `<br>ALTER SESSION<br>SET current schema='schema_name'<br>`                                                                         | N/A                                                                                                                                                                                                                                                                                                                      |
| Generate traces for specific errors              | `<br>ALTER SESSION<br>SET events '10053 trace name context forever';<br>`                                                           | N/A                                                                                                                                                                                                                                                                                                                      |
| Run trace for a SQL statement                    | `<br>ALTER SESSION<br>SET sql_trace=TRUE;<br>ALTER SYSTEM<br>SET EVENTS 'sql_trace [sql:&&sql_id]<br>bind=true,<br>wait=true';<br>` | `<br>SET GLOBAL general_log = 'ON';<br>`                                                                                                                                                                                                                                                                                 |
| Modify query optimizer cost for index access     | `<br>ALTER SESSION<br>SET optimizer_index_cost_adj = 50<br>`                                                                        | `<br>SET SESSION optimizer_switch= ?<br>`<br>You can turn on and off other strategies. For more information, see [Switchable Optimizations](https://dev.mysql.com/doc/refman/5.7/en/switchable-optimizations.html "https://dev.mysql.com/doc/refman/5.7/en/switchable-optimizations.html") in the _MySQL documentation_. |
| Modify query optimizer row access strategy       | `<br>ALTER SESSION<br>SET optimizer_mode=all_rows;<br>`                                                                             | `<br>SET SESSION optimizer_switch= ?<br>`<br>You can turn on and off other strategies. For more information, see [Switchable Optimizations](https://dev.mysql.com/doc/refman/5.7/en/switchable-optimizations.html "https://dev.mysql.com/doc/refman/5.7/en/switchable-optimizations.html") in the _MySQL documentation_. |
| Memory allocated to sort operations              | `<br>ALTER SESSION<br>SET sort_area_size=6321;<br>`                                                                                 | `<br>SET SESSION sort_buffer_size=32768;<br>`                                                                                                                                                                                                                                                                            |
| Memory allocated to hash-joins                   | `<br>ALTER SESSION<br>SET hash_area_sizee= 1048576000;<br>`                                                                         | `<br>SET SESSION join_buffer_size=1048576000;<br>`                                                                                                                                                                                                                                                                       |

For more information, see [SET Syntax for Variable Assignment](https://dev.mysql.com/doc/refman/5.7/en/set-variable.html "https://dev.mysql.com/doc/refman/5.7/en/set-variable.html") in the _MySQL documentation_.
