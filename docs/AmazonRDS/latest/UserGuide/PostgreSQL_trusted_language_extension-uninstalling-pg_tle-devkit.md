# Uninstalling Trusted Language Extensions for PostgreSQL

If you no longer want to create your own TLE extensions using TLE, you
can drop the `pg_tle` extension and remove all artifacts. This action
includes dropping any TLE extensions in the database and dropping the `pgtle`
schema.

###### To drop the `pg_tle` extension and its schema from a database

1. Use `psql` or another client
   tool to connect to the RDS for PostgreSQL DB instance.

```
psql --host=`.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=`dbname`
```

2. Drop the `pg_tle` extension from the database. If the database has your own TLE extensions still running in the database, you
   need to also drop those extensions. To do so, you can use the `CASCADE` keyword, as shown in the following.

```
DROP EXTENSION pg_tle CASCADE;
```

If the `pg_tle` extension isn't still active in the database,
you don't need to use the `CASCADE` keyword. 3. Drop the `pgtle` schema. This action removes all the management functions from the
database.

```
DROP SCHEMA pgtle CASCADE;
```

The command returns the following when the process completes.

```
DROP SCHEMA
```

The `pg_tle` extension, its schema and functions, and all artifacts are removed. To
create new extensions using TLE, go through the setup
process again. For more information, see [Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").
