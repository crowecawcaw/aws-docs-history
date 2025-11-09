# Excluding users or databases from audit logging

As discussed in [Aurora PostgreSQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md"), PostgreSQL logs consume
storage space. Using the pgAudit extension adds to the volume of data
gathered in your logs to varying degrees, depending on the changes that you track. You might not
need to audit every user or database in your Aurora PostgreSQL DB cluster.

To minimize impacts to your storage and to avoid needlessly capturing audit records, you
can exclude users and databases from being audited. You can also
change logging within a given session. The following examples show you how.

###### Note

Parameter settings at the session level take precedence over the settings
in the custom DB cluster parameter group for the Aurora PostgreSQL DB cluster's
writer instance. If you don't want database users to bypass your audit logging configuration
settings, be sure to change their permissions.

Suppose that your Aurora PostgreSQL DB cluster
is configured
to audit the same level of activity for all users and databases.
You then decide that you don't want to audit the user
`myuser`. You can turn off auditing for `myuser` with the following
SQL command.

```
ALTER USER myuser SET pgaudit.log TO 'NONE';
```

Then, you can use the following query to check the `user_specific_settings`
column for `pgaudit.log` to confirm that the parameter is set to `NONE`.

```
SELECT
    usename AS user_name,
    useconfig AS user_specific_settings
FROM
    pg_user
WHERE
    usename = 'myuser';
```

You see output such as the following.

```
 user_name | user_specific_settings
-----------+------------------------
 myuser    | {pgaudit.log=NONE}
(1 row)
```

You can turn off logging for a given user in the midst of their session with the database with
the following command.

```
ALTER USER myuser IN DATABASE mydatabase SET pgaudit.log TO 'none';
```

Use the following query to check the settings column for pgaudit.log for a specific user and database combination.

```
SELECT
    usename AS "user_name",
    datname AS "database_name",
    pg_catalog.array_to_string(setconfig, E'\n') AS "settings"
FROM
    pg_catalog.pg_db_role_setting s
    LEFT JOIN pg_catalog.pg_database d ON d.oid = setdatabase
    LEFT JOIN pg_catalog.pg_user r ON r.usesysid = setrole
WHERE
    usename = 'myuser'
    AND datname = 'mydatabase'
ORDER BY
    1,
    2;
```

You see output similar to the following.

```
  user_name | database_name |     settings
-----------+---------------+------------------
 myuser    | mydatabase    | pgaudit.log=none
(1 row)
```

After turning off auditing for `myuser`, you decide that
you don't want to track changes to `mydatabase`. You turn off auditing
for that specific database by using the following command.

```
ALTER DATABASE mydatabase SET pgaudit.log to 'NONE';
```

Then, use the following query to check the database_specific_settings column
to confirm that pgaudit.log is set to NONE.

```
SELECT
a.datname AS database_name,
b.setconfig AS database_specific_settings
FROM
pg_database a
FULL JOIN pg_db_role_setting b ON a.oid = b.setdatabase
WHERE
a.datname = 'mydatabase';
```

You see output such as the following.

```
 database_name | database_specific_settings
---------------+----------------------------
 mydatabase    | {pgaudit.log=NONE}
(1 row)
```

To return settings to the default setting for myuser, use the following command:

```
ALTER USER myuser RESET pgaudit.log;
```

To return settings to their default setting for a database, use the following command.

```
ALTER DATABASE mydatabase RESET pgaudit.log;
```

To reset user and database to the default setting,
use the following command.

```
ALTER USER myuser IN DATABASE mydatabase RESET pgaudit.log;
```

You can also capture specific events to the log by setting the `pgaudit.log` to one of the other
allowed values for the `pgaudit.log` parameter. For more information, see
[List of allowable settings for the pgaudit.log parameter](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.pgaudit-log-settings "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.pgaudit-log-settings").

```
ALTER USER myuser SET pgaudit.log TO 'read';
ALTER DATABASE mydatabase SET pgaudit.log TO 'function';
ALTER USER myuser IN DATABASE mydatabase SET pgaudit.log TO 'read,function'
```
