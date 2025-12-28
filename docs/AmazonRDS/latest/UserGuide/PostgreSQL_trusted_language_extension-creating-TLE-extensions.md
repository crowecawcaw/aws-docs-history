# Creating TLE extensions for

RDS for PostgreSQL

You can install any extensions that you create with TLE
in any
RDS for PostgreSQL DB instance that has the
`pg_tle` extension installed. The `pg_tle` extension is scoped
to the PostgreSQL database in which it's installed. The extensions that you create using TLE are scoped to the
same database.

Use the various `pgtle` functions to install the code that makes up your TLE
extension. The following Trusted Language Extensions functions all require the `pgtle_admin`
role.

- [pgtle.install_extension](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.install_extension "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.install_extension")
- [pgtle.install_update_path](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.install_update_path "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.install_update_path")
- [pgtle.register_feature](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature")
- [pgtle.register_feature_if_not_exists](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature_if_not_exists "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature_if_not_exists")
- [pgtle.set_default_version](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.set_default_version "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.set_default_version")
- [pgtle.uninstall_extension(name)](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_extension-name "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_extension-name")
- [pgtle.uninstall_extension(name, version)](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_extension-name-version "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_extension-name-version")
- [pgtle.uninstall_extension_if_exists](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_extension_if_exists "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_extension_if_exists")
- [pgtle.uninstall_update_path](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_update_path "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_update_path")
- [pgtle.uninstall_update_path_if_exists](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_update_path_if_exists "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.uninstall_update_path_if_exists")
- [pgtle.unregister_feature](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature")
- [pgtle.unregister_feature_if_exists](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature_if_exists "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature_if_exists")

## Example: Creating a trusted language extension using SQL

The following example shows you how to create a TLE extension named `pg_distance` that
contains a few SQL functions for calculating distances using different formulas.
In the listing, you can find the function for calculating the Manhattan distance and the function
for calculating the Euclidean distance. For more information about the difference between these formulas, see
[Taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry "https://en.wikipedia.org/wiki/Taxicab_geometry") and
[Euclidean geometry](https://en.wikipedia.org/wiki/Euclidean_geometry "https://en.wikipedia.org/wiki/Euclidean_geometry") in Wikipedia.

You can use this example in your own

RDS for PostgreSQL DB instance
if you have the `pg_tle` extension set up as detailed in
[Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

###### Note

You need to have the privileges of the `pgtle_admin` role to follow this procedure.

###### To create the example TLE extension

The following steps use an example database named `labdb`. This
database is owned by the `postgres` primary user. The
`postgres` role also has the permissions of the
`pgtle_admin` role.

1. Use `psql` to connect to
   RDS for PostgreSQL DB instance.

```
psql --host=`db-instance-123456789012`.`aws-region`.rds.amazonaws.com
--port=`5432` --username=`postgres` --password --dbname=labdb
```

2. Create a TLE extension named `pg_distance` by copying the following code and
   pasting it into your `psql` session console.

```
SELECT pgtle.install_extension
(
 'pg_distance',
 '0.1',
  'Distance functions for two points',
$_pg_tle_$
    CREATE FUNCTION dist(x1 float8, y1 float8, x2 float8, y2 float8, norm int)
    RETURNS float8
    AS $$
      SELECT (abs(x2 - x1) ^ norm + abs(y2 - y1) ^ norm) ^ (1::float8 / norm);
    $$ LANGUAGE SQL;

    CREATE FUNCTION manhattan_dist(x1 float8, y1 float8, x2 float8, y2 float8)
    RETURNS float8
    AS $$
      SELECT dist(x1, y1, x2, y2, 1);
    $$ LANGUAGE SQL;

    CREATE FUNCTION euclidean_dist(x1 float8, y1 float8, x2 float8, y2 float8)
    RETURNS float8
    AS $$
      SELECT dist(x1, y1, x2, y2, 2);
    $$ LANGUAGE SQL;
$_pg_tle_$
);
```

You see the output, such as the following.

```
install_extension
---------------
 t
(1 row)
```

The artifacts that make up the `pg_distance` extension are now
installed in your database. These artifacts include the control file and the
code for the extension, which are items that need to be present so that the
extension can be created using the `CREATE EXTENSION` command. In
other words, you still need to create the extension to make its functions
available to database users. 3. To create the extension, use the `CREATE EXTENSION` command as you do for any other
extension. As with other extensions, the database user needs to have the
`CREATE` permissions in the database.

```
CREATE EXTENSION pg_distance;
```

4. To test the `pg_distance` TLE extension, you can use it to calculate the
   [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry "https://en.wikipedia.org/wiki/Taxicab_geometry") between four points.

```
`labdb=>` `SELECT manhattan_dist(1, 1, 5, 5);`
`8`
```

To calculate the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_geometry "https://en.wikipedia.org/wiki/Euclidean_geometry")
between the same set of points, you can use the following.

```
`labdb=>` `SELECT euclidean_dist(1, 1, 5, 5);`
`5.656854249492381`
```

The `pg_distance` extension loads the functions in the database and makes
them available to any users with permissions on the database.

## Modifying your TLE extension

To improve query performance for the functions packaged in this TLE extension, add
the following two PostgreSQL attributes to their specifications.

- `IMMUTABLE` – The `IMMUTABLE` attribute ensures that the
  query optimizer can use optimizations to improve query response times. For more information,
  see [Function
  Volatility Categories](https://www.postgresql.org/docs/current/xfunc-volatility.html "https://www.postgresql.org/docs/current/xfunc-volatility.html") in the PostgreSQL documentation.
- `PARALLEL SAFE` – The `PARALLEL SAFE` attribute is another
  attribute that allows PostgreSQL to run the function in parallel mode. For
  more information, see [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "https://www.postgresql.org/docs/current/sql-createfunction.html") in the PostgreSQL documentation.

In the following example, you can see how the
`pgtle.install_update_path` function is used to add these attributes
to each function to create a version `0.2` of the
`pg_distance` TLE extension. For more information about this
function, see [pgtle.install_update_path](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.install_update_path "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.install_update_path"). You need to have the `pgtle_admin` role to
perform this task.

###### To update an existing TLE extension and specify the default version

1. Connect to
   RDS for PostgreSQL DB instance using `psql` or another client tool, such as pgAdmin.

```
psql --host=`db-instance-123456789012`.`aws-region`.rds.amazonaws.com
--port=`5432` --username=`postgres` --password --dbname=labdb
```

2. Modify the existing TLE extension by copying the following code and pasting it into your
   `psql` session console.

```
SELECT pgtle.install_update_path
(
 'pg_distance',
 '0.1',
 '0.2',
$_pg_tle_$
    CREATE OR REPLACE FUNCTION dist(x1 float8, y1 float8, x2 float8, y2 float8, norm int)
    RETURNS float8
    AS $$
      SELECT (abs(x2 - x1) ^ norm + abs(y2 - y1) ^ norm) ^ (1::float8 / norm);
    $$ LANGUAGE SQL IMMUTABLE PARALLEL SAFE;

    CREATE OR REPLACE FUNCTION manhattan_dist(x1 float8, y1 float8, x2 float8, y2 float8)
    RETURNS float8
    AS $$
      SELECT dist(x1, y1, x2, y2, 1);
    $$ LANGUAGE SQL IMMUTABLE PARALLEL SAFE;

    CREATE OR REPLACE FUNCTION euclidean_dist(x1 float8, y1 float8, x2 float8, y2 float8)
    RETURNS float8
    AS $$
      SELECT dist(x1, y1, x2, y2, 2);
    $$ LANGUAGE SQL IMMUTABLE PARALLEL SAFE;
$_pg_tle_$
);
```

You see a response similar to the following.

```
install_update_path
---------------------
 t
(1 row)
```

You can make this version of the extension the default version, so that
database users don't have to specify a version when they create or
update the extension in their database. 3. To specify that the modified version (version 0.2) of your TLE extension is the default
version, use the `pgtle.set_default_version` function as shown
in the following example.

```
SELECT pgtle.set_default_version('pg_distance', '0.2');
```

For more information about this function, see [pgtle.set_default_version](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.set_default_version "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.set_default_version"). 4. With the code in place, you can update the installed TLE extension in the usual way, by using
`ALTER EXTENSION ... UPDATE` command, as shown here:

```
ALTER EXTENSION pg_distance UPDATE;
```
