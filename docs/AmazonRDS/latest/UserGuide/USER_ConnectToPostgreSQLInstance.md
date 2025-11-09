# Using psql to connect to your

RDS for PostgreSQL DB instance

You can use a local instance of the psql command line utility to connect to a
RDS for PostgreSQL DB instance. You need either PostgreSQL or the psql client installed on
your client computer.

You can download the PostgreSQL client from the [PostgreSQL](https://www.postgresql.org/download/ "https://www.postgresql.org/download/") website. Follow the
instructions specific to your operating system version to install psql.

To connect to your RDS for PostgreSQL DB instance using psql, you need to provide host
(DNS) information, access credentials, and the name of the database.

Use one of the following formats to connect to your RDS for PostgreSQL DB instance. When
you connect, you're prompted for a password. For batch jobs or scripts, use the
`--no-password` option. This option is set for the entire session.

###### Note

A connection attempt with `--no-password` fails when the server
requires password authentication and a password is not available from other sources.
For more information, see the [psql
documentation](https://www.postgresql.org/docs/13/app-psql.html "https://www.postgresql.org/docs/13/app-psql.html").

If this is the first time you are connecting to this DB instance, or if you
didn't yet create a database for this RDS for PostgreSQL instance, you can connect to
the **postgres** database using the 'master
username' and password.

For Unix, use the following format.

```
psql \
   --host=<DB instance endpoint> \
   --port=<port> \
   --username=<master username> \
   --password \
   --dbname=<database name>
```

For Windows, use the following format.

```
psql ^
   --host=<DB instance endpoint> ^
   --port=<port> ^
   --username=<master username> ^
   --password ^
   --dbname=<database name>
```

For example, the following command connects to a database called `mypgdb`
on a PostgreSQL DB instance called `mypostgresql` using fictitious
credentials.

```
psql --host=mypostgresql.c6c8mwvfdgv0.us-west-2.rds.amazonaws.com --port=5432 --username=awsuser --password --dbname=mypgdb
```
