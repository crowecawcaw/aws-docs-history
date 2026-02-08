# Controlling user access to the

PostgreSQL database

New databases in PostgreSQL are always created with a default set of privileges in the
database's `public` schema that allow all database users and roles to create
objects. These privileges allow database users to connect to the database, for example, and
create temporary tables while connected.

To better control user access to the databases instances that you create
on your RDS for PostgreSQL DB instance, we recommend that
you revoke these default `public` privileges. After doing so, you then grant
specific privileges for database users on a more granular basis, as shown in the following
procedure.

###### To set up roles and privileges for a new database instance

Suppose you're setting up a database on a newly created RDS for PostgreSQL DB
instance for use by several researchers, all of whom need read-write access to
the database.

1. Use `psql` (or pgAdmin) to connect to
   your RDS for PostgreSQL DB instance:

```
psql --host=`your-db-instance.666666666666`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password
```

When prompted, enter your password. The `psql` client connects and displays
the default administrative connection database, `postgres=>`, as the
prompt. 2. To prevent database users from creating objects in the `public` schema, do
the following:

```
`postgres=>` `REVOKE CREATE ON SCHEMA public FROM PUBLIC;`
`REVOKE`
```

3. Next, you create a new database instance:

```
`postgres=>` `CREATE DATABASE `lab_db`;`
`CREATE DATABASE`
```

4. Revoke all privileges from the `PUBLIC` schema on this new database.

```
`postgres=>` `REVOKE ALL ON DATABASE `lab_db` FROM public;`
`REVOKE`
```

5. Create a role for database users.

```
`postgres=>` `CREATE ROLE `lab_tech`;`
`CREATE ROLE`
```

6. Give database users that have this role the ability to connect to the database.

```
`postgres=>` `GRANT CONNECT ON DATABASE `lab_db` TO `lab_tech`;`
`GRANT`

```

7. Grant all users with the `lab_tech` role all privileges on this
   database.

```
`postgres=>` `GRANT ALL PRIVILEGES ON DATABASE `lab_db` TO `lab_tech`;`
`GRANT`

```

8. Create database users, as follows:

```
`postgres=>` `CREATE ROLE lab_user1 LOGIN PASSWORD 'change_me';`
`CREATE ROLE`
`postgres=>` `CREATE ROLE lab_user2 LOGIN PASSWORD 'change_me';`
`CREATE ROLE`
```

9. Grant these two users the privileges associated with the lab_tech role:

```
`postgres=>` `GRANT lab_tech TO lab_user1;`
`GRANT ROLE`
`postgres=>` `GRANT lab_tech TO lab_user2;`
`GRANT ROLE`

```

At this point, `lab_user1` and `lab_user2` can connect to the
`lab_db` database. This example doesn't follow best practices for enterprise
usage, which might include creating multiple database instances, different schemas, and
granting limited permissions. For more complete information and additional scenarios, see
[Managing PostgreSQL
Users and Roles](https://aws.amazon.com/blogs//database/managing-postgresql-users-and-roles/ "https://aws.amazon.com/blogs//database/managing-postgresql-users-and-roles/").

For more information about privileges in PostgreSQL databases, see the [GRANT](https://www.postgresql.org/docs/current/static/sql-grant.html "https://www.postgresql.org/docs/current/static/sql-grant.html") command in
the PostgreSQL documentation.
