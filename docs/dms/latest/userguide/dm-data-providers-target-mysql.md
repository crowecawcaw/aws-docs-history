# Using a MySQL compatible database as a target for homogeneous data migrations in AWS DMS

You can use a MySQL compatible database as a migration target for homogeneous data migrations in AWS DMS.

AWS DMS requires certain permissions to migrate data into your target Amazon RDS for MySQL or MariaDB
or Amazon Aurora MySQL database. Use the following script to create a database user with the
required permissions in your MySQL target database.

In this example, replace each `user input placeholder` with your own information.
If your target MariaDB database version is lower than 10.5, then you can skip the `GRANT SLAVE MONITOR` command.

```
CREATE USER '`your_user`'@'%' IDENTIFIED BY '`your_password`';

GRANT ALTER, CREATE, DROP, INDEX, INSERT, UPDATE, DELETE, SELECT, CREATE VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, EXECUTE, REFERENCES ON *.* TO '`your_user`'@'%';
GRANT REPLICATION SLAVE, REPLICATION CLIENT  ON *.* TO '`your_user`'@'%'; GRANT SLAVE MONITOR  ON *.* TO 'your_user'@'%';
```

In the preceding example, replace each `user input placeholder` with your own information.

Use the following script to create a database user with the required permissions in your MariaDB database. Run the GRANT queries
for all databases that you migrate to AWS.

```
CREATE USER '`your_user`'@'%' IDENTIFIED BY '`your_password`';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, EXECUTE,SLAVE MONITOR, REPLICATION SLAVE ON *.* TO 'your_user'@'%';
```

In the preceding example, replace each `user input placeholder` with your own information.

###### Note

In Amazon RDS, when you turn on automated backup for a MySQL/Maria database instance, you also turn on
binary logging. When these settings are enabled, your data migration task may fail with the following error
while creating secondary objects such as functions, procedures, and triggers on the target database. If
your target database has binary logging enabled, then set `log_bin_trust_function_creators` to
`true` in the database parameter group before starting the task.

```
ERROR 1419 (HY000): You don't have the SUPER privilege and binary logging is enabled (you might want to use the less safe log_bin_trust_function_creators variable)
```

## Limitations for using a

MySQL compatible database as a target for homogeneous data migrations

The following limitations apply when using a MySQL compatible database as a target for homogeneous data migrations:

- The username you use to connect to your data source has the following limitations:
  - Can be 2 to 64 characters in length.
  - Can't have spaces.
  - Can include the following characters: a-z, A-Z, 0-9, underscore (\_).
  - Can't include a hyphen (-).
  - Must start with a-z or A-Z.

- The password you use to connect to your data source has the following limitations:
  - Can be 1 to 128 characters in length.
  - Can't contain any of the following: single quote ('), double quote ("), semicolon (;) or space.
