# Using a PostgreSQL database as a target for homogeneous data migrations in AWS DMS

You can use a PostgreSQL database as a migration target for homogeneous data migrations in AWS DMS.

AWS DMS requires certain permissions to migrate data into your target Amazon RDS for PostgreSQL
or Amazon Aurora PostgreSQL database. Use the following script to create a database user with the
required permissions in your PostgreSQL target database.

```
CREATE USER `your_user` WITH LOGIN PASSWORD '`your_password`';
GRANT USAGE ON SCHEMA `schema_name` TO `your_user`;
GRANT CONNECT ON DATABASE `db_name` to `your_user`;
GRANT CREATE ON DATABASE `db_name` TO `your_user`;
GRANT CREATE ON SCHEMA `schema_name` TO `your_user`;
GRANT UPDATE, INSERT, SELECT, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA `schema_name` TO `your_user`;
            #For "Full load and change data capture (CDC)" and "Change data capture (CDC)" data migrations, setting up logical replication requires rds_superuser privileges
GRANT rds_superuser TO `your_user`;
```

In the preceding example, replace each `user input placeholder` with your own information.

To turn on logical replication for your RDS for PostgreSQL target, set the `rds.logical_replication`
parameter in your DB parameter group to 1. This static parameter requires a reboot of the DB instance or DB cluster
to take effect. Some parameters are static, and you can only set them at server start. AWS DMS ignores changes
to their entries in the DB parameter group until you restart the server.

PostgreSQL uses triggers to implement foreign key constraints. During the full load phase, AWS DMS loads
each table one at a time. We recommend that you turn off foreign key constraints on your target database
during the full load. To do so, use one of the following methods.

- Temporarily turn off all triggers for your instance, and finish the full load.
- Change the value of the `session_replication_role` parameter in PostgreSQL.

At any given time, a trigger can be in one of the following states: `origin`,
`replica`, `always`, or `disabled`. When you set the
`session_replication_role` parameter to `replica`, only triggers in the
`replica` state are active. Otherwise, the triggers remain inactive.

## Limitations for using a

PostgreSQL compatible database as a target for homogeneous data migrations

The following limitations apply when using a PostgreSQL compatible database as a target for homogeneous data migrations:

- The username you use to connect to your data source has the following limitations:
  - Can be 2 to 64 characters in length.
  - Can't have spaces.
  - Can include the following characters: a-z, A-Z, 0-9, underscore (\_).
  - Must start with a-z or A-Z.

- The password you use to connect to your data source has the following limitations:
  - Can be 1 to 128 characters in length.
  - Can't contain any of the following: single quote ('), double quote ("), semicolon (;) or space.
