# Managing large objects with the lo module

The lo module (extension) is for database users and developers working with
PostgreSQL databases through JDBC or ODBC drivers. Both JDBC and ODBC expect the database to
handle deletion of large objects when references to them change. However, PostgreSQL
doesn't work that way. PostgreSQL doesn't assume that an object should be deleted
when its reference changes. The result is that objects remain on disk, unreferenced. The
lo extension includes a function that you use to
trigger on reference changes to delete objects if needed.

###### Tip

To determine if your database can benefit from the lo extension, use the
`vacuumlo` utility to check for orphaned large objects. To get counts of
orphaned large objects without taking any action, run the utility with the
`-n` option (no-op). To learn how, see [vacuumlo utility](#vacuumlo-utility "#vacuumlo-utility") following.

The lo module is available for Aurora PostgreSQL 13.7, 12.11, 11.16, 10.21 and
higher minor versions.

To install the module (extension), you need `rds_superuser` privileges.
Installing the lo extension adds the following to your database:

- `lo` – This is a large object (lo) data type that you can use for binary
  large objects (BLOBs) and other large objects. The `lo` data type is a
  domain of the `oid` data type. In other words, it's an object
  identifier with optional constraints. For more information, see [Object
  identifiers](https://www.postgresql.org/docs/14/datatype-oid.html "https://www.postgresql.org/docs/14/datatype-oid.html") in the PostgreSQL documentation. In simple terms, you can
  use the `lo` data type to distinguish your database columns that hold
  large object references from other object identifiers (OIDs).
- `lo_manage` – This is a function that you can use in triggers on
  table columns that contain large object references. Whenever you delete or modify a
  value that references a large object, the trigger unlinks the object
  (`lo_unlink`) from its reference. Use the trigger on a column only if
  the column is the sole database reference to the large object.
  For more information about the large objects module, see [lo](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") in the
  PostgreSQL documentation.

## Installing the lo extension

Before installing the lo extension, make sure that you have `rds_superuser`
privileges.

###### To install the lo extension

1. Use `psql` to connect to the primary DB instance of your Aurora PostgreSQL DB
   cluster.

```
psql --host=`your-cluster-instance-1.666666666666`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password
```

When prompted, enter your password. The `psql` client connects and displays the
default administrative connection database, `postgres=>`, as the
prompt. 2. Install the extension as follows.

```
`postgres=>` `CREATE EXTENSION lo;`
`CREATE EXTENSION`
```

You can now use the `lo` data type to define columns in your tables. For
example, you can create a table (`images`) that contains raster image data.
You can use the `lo` data type for a column `raster`, as shown in
the following example, which creates a table.

```
`postgres=>` CREATE TABLE images (image_name text, raster lo);
```

## Using the lo_manage trigger function to delete objects

You can use the `lo_manage` function in a trigger on a `lo` or other
large object columns to clean up (and prevent orphaned objects) when the `lo`
is updated or deleted.

###### To set up triggers on columns that reference large objects

- Do one of the following:
  - Create a BEFORE UPDATE OR DELETE trigger on each column to contain unique
    references to large objects, using the column name for the
    argument.

  ```
  `postgres=>` CREATE TRIGGER t_raster BEFORE UPDATE OR DELETE ON images
      FOR EACH ROW EXECUTE FUNCTION lo_manage(raster);
  ```

  - Apply a trigger only when the column is being updated.

  ```
  `postgres=>` CREATE TRIGGER t_raster BEFORE UPDATE OF images
      FOR EACH ROW EXECUTE FUNCTION lo_manage(raster);
  ```

The `lo_manage` trigger function works only in the context of inserting or deleting
column data, depending on how you define the trigger. It has no effect when you perform
a `DROP` or `TRUNCATE` operation on a database. That means that
you should delete object columns from any tables before dropping, to prevent creating
orphaned objects.

For example, suppose that you want to drop the database containing the `images`
table. You delete the column as follows.

```
`postgres=>` DELETE FROM images COLUMN raster
```

Assuming that the `lo_manage` function is defined on that column to handle deletes, you can now safely
drop the table.

## Removing orphaned large objects using `vacuumlo`

The `vacuumlo` utility identifies
and removes orphaned large objects from databases. This utility has been available since
PostgreSQL 9.1.24. If your database users routinely work with
large objects, we recommend that you run `vacuumlo` occasionally to clean up
orphaned large objects.

Before installing the lo extension, you can use `vacuumlo` to assess whether your
Aurora PostgreSQL DB cluster can benefit. To do so, run `vacuumlo` with the `-n` option
(no-op) to show what would be removed, as shown in the following:

```
`$` `vacuumlo -v -n -h `your-cluster-instance-1.666666666666`.`aws-region`.rds.amazonaws.com -p 5433 -U postgres `docs-lab-spatial-db``
`Password:``*****``Connected to database "docs-lab-spatial-db"
Test run: no large objects will be removed!
Would remove 0 large objects from database "docs-lab-spatial-db".`
```

As the output shows, orphaned large objects aren't a problem for this particular database.

For more information about this utility, see
[`vacuumlo`](https://www.postgresql.org/docs/current/vacuumlo.html "https://www.postgresql.org/docs/current/vacuumlo.html") in the
PostgreSQL documentation.

## Understanding how `vacuumlo` works

The `vacuumlo` command removes orphaned large objects (LOs) from your PostgreSQL database without affecting or conflicting with your user tables.

The command works as follows:

1. `vacuumlo` starts by creating a temporary table containing all the Object IDs (OIDs) of the large objects in your database.
2. `vacuumlo` then scans through every column in the database that uses the data types `oid` or `lo`. If `vacuumlo` finds a matching OID in these columns,
   it removes the OID from the temporary table. `vacuumlo` checks only columns specifically named `oid` or `lo`, not domains based on these types.
3. The remaining entries in the temporary table represent orphaned LOs, which `vacuumlo` then safely removes.

## Improving `vacuumlo` performance

You can potentially improve the performance of `vacuumlo` by increasing the batch size using the `-l` option. This allows `vacuumlo` to
process more LOs at once.

If your system has sufficient memory and you can accommodate the temporary table completely in memory, increasing the `temp_buffers` setting at the database level may improve performance.
This allows the table to reside entirely in memory, which can enhance the overall performance.

Following query estimates the size of the temporary table:

```
SELECT
    pg_size_pretty(SUM(pg_column_size(oid))) estimated_lo_temp_table_size
FROM
    pg_largeobject_metadata;

```

## Considerations for large objects

Following you can find some important considerations to note when working with large objects:

- `Vacuumlo` is the only solution as there is currently no other method to remove orphaned LOs.
- Tools like pglogical, native logical replication, and AWS DMS that use replication technologies do not support replicating large objects.
- When designing your database schema, avoid using large objects when possible and consider using alternative data types like `bytea` instead.
- Run `vacuumlo` regularly, at least weekly, to prevent issues with orphaned LOs.
- Use a trigger with the `lo_manage` function on tables that store large objects to help prevent orphaned LOs from being created.
