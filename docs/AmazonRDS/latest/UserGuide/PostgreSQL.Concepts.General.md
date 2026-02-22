# Upgrading and using the PLV8

extension

PLV8 is a trusted Javascript language extension for PostgreSQL. You can use it for stored
procedures, triggers, and other procedural code that's callable from SQL. This language
extension is supported by all current releases of PostgreSQL.

If you use [PLV8](https://plv8.github.io/ "https://plv8.github.io/") and upgrade PostgreSQL to a
new PLV8 version, you immediately take advantage of the new extension. Take the following
steps to synchronize your catalog metadata with the new version of PLV8. These steps are
optional, but we highly recommend that you complete them to avoid metadata mismatch
warnings.

The upgrade process drops all your existing PLV8 functions. Thus, we recommend that you
create a snapshot of your RDS for PostgreSQL DB instance before upgrading. For more information,
see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").

###### Important

Starting with PostgreSQL version 18, Amazon RDS for PostgreSQL will deprecate the
`plcoffee` and `plls` PostgreSQL extensions. We recommend that you
stop using CoffeeScript and LiveScript in your applications to ensure you have an upgrade
path for future engine version upgrades.

###### To synchronize your catalog metadata with a new version of PLV8

1. Verify that you need to update. To do this, run the following command while connected
   to your instance.

```
SELECT * FROM pg_available_extensions WHERE name IN ('plv8','plls','plcoffee');
```

If your results contain values for an installed version that is a lower number than
the default version, continue with this procedure to update your extensions. For example,
the following result set indicates that you should update.

```
name    | default_version | installed_version |                     comment
--------+-----------------+-------------------+--------------------------------------------------
plls    | 2.1.0           | 1.5.3             | PL/LiveScript (v8) trusted procedural language
plcoffee| 2.1.0           | 1.5.3             | PL/CoffeeScript (v8) trusted procedural language
plv8    | 2.1.0           | 1.5.3             | PL/JavaScript (v8) trusted procedural language
(3 rows)
```

2. Create a snapshot of your RDS for PostgreSQL DB instance if you haven't done so yet.
   You can continue with the following steps while the snapshot is being created.
3. Get a count of the number of PLV8 functions in your DB instance so you can validate
   that they are all in place after the upgrade. For example, the following SQL query returns
   the number of functions written in plv8, plcoffee, and plls.

```
SELECT proname, nspname, lanname
FROM pg_proc p, pg_language l, pg_namespace n
WHERE p.prolang = l.oid
AND n.oid = p.pronamespace
AND lanname IN ('plv8','plcoffee','plls');

```

4. Use pg_dump to create a schema-only dump file. For example, create a file on your
   client machine in the `/tmp` directory.

```
./pg_dump -Fc --schema-only -U master postgres >/tmp/test.dmp
```

This example uses the following options:

    * `-Fc` – Custom format
    * --schema-only – Dump only the commands necessary to create schema
     (functions in this case)
    * `-U` – The RDS master user name
    * `database` – The database name for our DB instance

For more information on pg_dump, see [pg_dump](https://www.postgresql.org/docs/current/static/app-pgdump.html "https://www.postgresql.org/docs/current/static/app-pgdump.html ") in
the PostgreSQL documentation. 5. Extract the "CREATE FUNCTION" DDL statement that is present in the dump file. The
following example uses the `grep` command to extract the DDL statement that
creates the functions and save them to a file. You use this in subsequent steps to
recreate the functions.

```
./pg_restore -l /tmp/test.dmp | grep FUNCTION > /tmp/function_list
```

For more information on pg_restore, see [pg_restore](https://www.postgresql.org/docs/current/static/app-pgrestore.html "https://www.postgresql.org/docs/current/static/app-pgrestore.html") in the PostgreSQL documentation. 6. Drop the functions and extensions. The following example drops any PLV8 based objects.
The cascade option ensures that any dependent are dropped.

```
DROP EXTENSION plv8 CASCADE;
```

If your PostgreSQL instance contains objects based on plcoffee or plls, repeat this
step for those extensions. 7. Create the extensions. The following example creates the plv8, plcoffee, and plls
extensions.

```
CREATE EXTENSION plv8;
CREATE EXTENSION plcoffee;
CREATE EXTENSION plls;
```

8. Create the functions using the dump file and "driver" file.

The following example recreates the functions that you extracted previously.

```
./pg_restore -U master -d postgres -Fc -L /tmp/function_list /tmp/test.dmp
```

9. Verify that all your functions have been recreated by using the following query.

```
SELECT * FROM pg_available_extensions WHERE name IN ('plv8','plls','plcoffee');
```

The PLV8 version 2 adds the following extra row to your result set:

```
    proname    |  nspname   | lanname
---------------+------------+----------
 plv8_version  | pg_catalog | plv8

```
