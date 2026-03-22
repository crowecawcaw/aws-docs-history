# Dropping your TLE extensions from a database

You can drop your TLE extensions by using the `DROP EXTENSION` command
in the same way that you do for other PostgreSQL extensions. Dropping the extension
doesn't remove the installation files that make up the extension, which allows
users to re-create the extension. To remove the extension and its installation files, do
the following two-step process.

###### To drop the TLE extension and remove its installation files

1. Use `psql` or another client
   tool to connect to the writer instance of your
   Aurora PostgreSQL DB cluster.

```
psql --host=`cluster-instance-1.111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=`dbname`
```

2. Drop the extension as you would any PostgreSQL extension.

```
DROP EXTENSION `your-TLE-extension`
```

For example, if you create the `pg_distance` extension as detailed in
[Example: Creating a trusted language extension using SQL](PostgreSQL_trusted_language_extension-creating-TLE-extensions.md#PostgreSQL_trusted_language_extension-simple-example "PostgreSQL_trusted_language_extension-creating-TLE-extensions.md#PostgreSQL_trusted_language_extension-simple-example"), you can drop the extension as follows.

```
DROP EXTENSION pg_distance;
```

You see output confirming that the extension has been dropped, as follows.

```
DROP EXTENSION
```

At this point, the extension is no longer active in the database. However, its installation
files and control file are still available in the database, so database users
can create the extension again if they like.

    * If you want to leave the extension files intact so that database users can create your TLE
     extension, you can stop here.
    * If you want to remove all files that make up the extension,
     continue to the next step.

3. To remove all installation files for your extension, use the
   `pgtle.uninstall_extension` function. This function removes all
   the code and control files for your extension.

```
SELECT pgtle.uninstall_extension('`your-tle-extension-name`');
```

For example, to remove all `pg_distance` installation files, use the following
command.

```
SELECT pgtle.uninstall_extension('pg_distance');
 `uninstall_extension
---------------------
 t
(1 row)`
```
