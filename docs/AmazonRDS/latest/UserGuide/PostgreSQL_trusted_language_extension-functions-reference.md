# Function reference for Trusted Language Extensions for PostgreSQL

View the following reference documentation about functions available in Trusted Language Extensions for PostgreSQL. Use
these functions to install, register, update, and manage your _TLE
extensions_, that is, the PostgreSQL extensions that you develop using the
Trusted Language Extensions development kit.

###### Functions

- [pgtle.available_extensions](#pgtle.available_extensions "#pgtle.available_extensions")
- [pgtle.available_extension_versions](#pgtle.available_extension_versions "#pgtle.available_extension_versions")
- [pgtle.extension_update_paths](#pgtle.extension_update_paths "#pgtle.extension_update_paths")
- [pgtle.install_extension](#pgtle.install_extension "#pgtle.install_extension")
- [pgtle.install_update_path](#pgtle.install_update_path "#pgtle.install_update_path")
- [pgtle.register_feature](#pgtle.register_feature "#pgtle.register_feature")
- [pgtle.register_feature_if_not_exists](#pgtle.register_feature_if_not_exists "#pgtle.register_feature_if_not_exists")
- [pgtle.set_default_version](#pgtle.set_default_version "#pgtle.set_default_version")
- [pgtle.uninstall_extension(name)](#pgtle.uninstall_extension-name "#pgtle.uninstall_extension-name")
- [pgtle.uninstall_extension(name, version)](#pgtle.uninstall_extension-name-version "#pgtle.uninstall_extension-name-version")
- [pgtle.uninstall_extension_if_exists](#pgtle.uninstall_extension_if_exists "#pgtle.uninstall_extension_if_exists")
- [pgtle.uninstall_update_path](#pgtle.uninstall_update_path "#pgtle.uninstall_update_path")
- [pgtle.uninstall_update_path_if_exists](#pgtle.uninstall_update_path_if_exists "#pgtle.uninstall_update_path_if_exists")
- [pgtle.unregister_feature](#pgtle.unregister_feature "#pgtle.unregister_feature")
- [pgtle.unregister_feature_if_exists](#pgtle.unregister_feature_if_exists "#pgtle.unregister_feature_if_exists")

## pgtle.available_extensions

The `pgtle.available_extensions` function is a set-returning function. It
returns all available TLE extensions in the database. Each returned row contains information
about a single TLE extension.

### Function prototype

```
pgtle.available_extensions()
```

### Role

None.

### Arguments

None.

### Output

- `name` – The name of the TLE extension.
- `default_version` – The version of the TLE extension to use when `CREATE EXTENSION` is
  called without a version specified.
- `description` – A more detailed description about the TLE extension.

### Usage example

```
SELECT * FROM pgtle.available_extensions();
```

## pgtle.available_extension_versions

The `available_extension_versions` function is a set-returning function. It
returns a list of all available TLE extensions and their versions. Each row contains
information about a specific version of the given TLE extension, including whether it
requires a specific role.

### Function prototype

```
pgtle.available_extension_versions()
```

### Role

None.

### Arguments

None.

### Output

- `name` – The name of the TLE extension.
- `version` – The version of the TLE extension.
- `superuser` – This value is always `false` for your TLE
  extensions. The permissions needed to create the TLE extension or update it
  are the same as for creating other objects in the given database.
- `trusted` – This value is always `false` for a TLE
  extension.
- `relocatable` – This value is always `false` for a TLE
  extension.
- `schema` – Specifies the name of the schema in which the TLE extension is
  installed.
- `requires` – An array containing the names of other extensions needed by this TLE extension.
- `description` – A detailed description of the TLE extension.

For more information about output values, see [Packaging Related Objects into an Extension > Extension Files](https://www.postgresql.org/docs/current/extend-extensions.html#id-1.8.3.20.11 "https://www.postgresql.org/docs/current/extend-extensions.html#id-1.8.3.20.11") in the
PostgreSQL documentation.

### Usage example

```
SELECT * FROM pgtle.available_extension_versions();
```

## pgtle.extension_update_paths

The `extension_update_paths` function is a set-returning function. It returns a
list of all the possible update paths for a TLE extension. Each row includes the
available upgrades or downgrades for that TLE extension.

### Function prototype

```
pgtle.extension_update_paths(name)
```

### Role

None.

### Arguments

`name` – The name of the TLE extension from which to get upgrade paths.

### Output

- `source` – The source version for an update.
- `target` – The target version for an update.
- `path` – The upgrade path used to update a TLE extension from
  `source` version to `target` version, for example, `0.1--0.2`.

### Usage example

```
SELECT * FROM pgtle.extension_update_paths('`your-TLE`');
```

## pgtle.install_extension

The `install_extension` function lets you install the artifacts that make up
your TLE extension in the database, after which it can be created using the `CREATE
 EXTENSION` command.

### Function prototype

```
pgtle.install_extension(name text, version text, description text, ext text, requires text[] DEFAULT NULL::text[])
```

### Role

None.

### Arguments

- `name` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.
- `version` – The version of the TLE extension.
- `description` – A detailed description about the TLE extension. This
  description is displayed in the `comment` field in
  `pgtle.available_extensions()`.
- `ext` – The contents of the TLE extension. This value contains objects such
  as functions.
- `requires` – An optional parameter that specifies dependencies for this TLE extension.
  The `pg_tle` extension is automatically added as a dependency.

Many of these arguments are the same as those that are included in an
extension control file for installing a PostgreSQL extension on the file system of a
PostgreSQL instance. For more information, see the [Extension Files](http://www.postgresql.org/docs/current/extend-extensions.html#id-1.8.3.20.11 "http://www.postgresql.org/docs/current/extend-extensions.html#id-1.8.3.20.11") in [Packaging
Related Objects into an Extension](https://www.postgresql.org/docs/current/extend-extensions.html "https://www.postgresql.org/docs/current/extend-extensions.html") in the PostgreSQL
documentation.

### Output

This functions returns `OK` on success and `NULL` on error.

- `OK` – The TLE extension has been successfully installed in the database.
- `NULL` – The TLE extension hasn't been successfully installed in the database.

### Usage example

```
SELECT pgtle.install_extension(
 'pg_tle_test',
 '0.1',
 'My first pg_tle extension',
$_pgtle_$
  CREATE FUNCTION my_test()
  RETURNS INT
  AS $$
    SELECT 42;
  $$ LANGUAGE SQL IMMUTABLE;
$_pgtle_$
);
```

## pgtle.install_update_path

The `install_update_path` function provides an update path between two
different versions of a TLE extension. This function allows users of your TLE extension
to update its version by using the `ALTER EXTENSION ... UPDATE`
syntax.

### Function prototype

```
pgtle.install_update_path(name text, fromvers text, tovers text, ext text)
```

### Role

`pgtle_admin`

### Arguments

- `name` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.
- `fromvers` – The source version of the TLE extension for the upgrade.
- `tovers` – The destination version of the TLE extension for the upgrade.
- `ext` – The contents of the update. This value contains objects such as
  functions.

### Output

None.

### Usage example

```
SELECT pgtle.install_update_path('pg_tle_test', '0.1', '0.2',
  $_pgtle_$
    CREATE OR REPLACE FUNCTION my_test()
    RETURNS INT
    AS $$
      SELECT 21;
    $$ LANGUAGE SQL IMMUTABLE;
  $_pgtle_$
);
```

## pgtle.register_feature

The `register_feature` function adds the specified internal PostgreSQL feature
to the `pgtle.feature_info` table. PostgreSQL hooks are an example of an internal PostgreSQL feature.
The Trusted Language Extensions development kit supports the use of PostgreSQL hooks. Currently, this function
supports the following feature.

- `passcheck` – Registers the password-check hook with your procedure
  or function that customizes PostgreSQL's password-check behavior.

### Function prototype

```
pgtle.register_feature(proc regproc, feature pg_tle_feature)
```

### Role

`pgtle_admin`

### Arguments

- `proc` – The name of a stored procedure or function to
  use for the feature.
- `feature` – The name of the `pg_tle`
  feature (such as `passcheck`) to register with the function.

### Output

None.

### Usage example

```
SELECT pgtle.register_feature('pw_hook', 'passcheck');
```

## pgtle.register_feature_if_not_exists

The `pgtle.register_feature_if_not_exists` function adds the specified PostgreSQL feature
to the `pgtle.feature_info` table and identifies the TLE extension or other procedure or function
that uses the feature. For more information about hooks and Trusted Language Extensions, see
[Using PostgreSQL hooks with your TLE extensions](PostgreSQL_trusted_language_extension.overview.md "PostgreSQL_trusted_language_extension.overview.md").

### Function prototype

```
pgtle.register_feature_if_not_exists(proc regproc, feature pg_tle_feature)
```

### Role

`pgtle_admin`

### Arguments

- `proc` – The name of a stored procedure or function that contains the logic
  (code) to use as a feature for your TLE extension. For example, the
  `pw_hook` code.
- `feature` – The name of the PostgreSQL feature to register for the TLE function. Currently, the
  only available feature is the `passcheck` hook. For more information, see [Password-check hook (passcheck)](PostgreSQL_trusted_language_extension-hooks-reference.md#passcheck_hook "PostgreSQL_trusted_language_extension-hooks-reference.md#passcheck_hook").

### Output

Returns `true` after registering the feature for the specified
extension. Returns `false` if the feature is already registered.

### Usage example

```
SELECT pgtle.register_feature_if_not_exists('pw_hook', 'passcheck');
```

## pgtle.set_default_version

The `set_default_version` function lets you specify a `default_version` for your TLE extension.
You can use this function to define an upgrade path and designate the version as the default for your
TLE extension. When database users specify your TLE extension in the `CREATE EXTENSION`
and `ALTER EXTENSION ... UPDATE` commands, that version of your TLE extension is created in the
database for that user.

This function returns `true` on success. If the TLE extension specified in the
`name` argument doesn't exist, the function returns an error.
Similarly, if the `version` of the TLE extension doesn't exist, it
returns an error.

### Function prototype

```
pgtle.set_default_version(name text, version text)
```

### Role

`pgtle_admin`

### Arguments

- `name` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.
- `version` – The version of the TLE extension to set the default.

### Output

- `true` – When setting default version succeeds, the function returns `true`.
- `ERROR` – Returns an error message if a TLE extension with the specified name or version doesn't
  exist.

### Usage example

```
SELECT * FROM pgtle.set_default_version('my-extension', '1.1');
```

## pgtle.uninstall_extension(name)

The `uninstall_extension` function removes all versions of a TLE extension
from a database. This function prevents future calls of `CREATE EXTENSION`
from installing the TLE extension. If the TLE extension doesn't exist in the
database, an error is raised.

The `uninstall_extension` function won't drop a TLE extension that's currently
active in the database. To remove a TLE extension that's currently active, you need to explicitly call
`DROP EXTENSION` to remove it.

### Function prototype

```
pgtle.uninstall_extension(extname text)
```

### Role

`pgtle_admin`

### Arguments

- `extname` – The name of the TLE extension to uninstall. This name is the
  same as the one used with `CREATE EXTENSION` to load the TLE
  extension for use in a given database.

### Output

None.

### Usage example

```
SELECT * FROM pgtle.uninstall_extension('pg_tle_test');
```

## pgtle.uninstall_extension(name, version)

The `uninstall_extension(name, version)` function removes the specified
version of the TLE extension from the database. This function prevents `CREATE
 EXTENSION` and `ALTER EXTENSION` from installing or updating a TLE
extension to the specified version. This function also removes all update paths for the
specified version of the TLE extension. This function won't uninstall the TLE
extension if it's currently active in the database. You must explicitly call
`DROP EXTENSION` to remove the TLE extension. To uninstall all versions
of a TLE extension, see [pgtle.uninstall_extension(name)](#pgtle.uninstall_extension-name "#pgtle.uninstall_extension-name").

### Function prototype

```
pgtle.uninstall_extension(extname text, version text)
```

### Role

`pgtle_admin`

### Arguments

- `extname` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.
- `version` – The version of the TLE extension to uninstall from the database.

### Output

None.

### Usage example

```
SELECT * FROM pgtle.uninstall_extension('pg_tle_test', '0.2');
```

## pgtle.uninstall_extension_if_exists

The `uninstall_extension_if_exists` function removes all versions of a TLE extension
from a given database. If the TLE extension doesn't exist, the function returns
silently (no error message is raised). If the specified extension is currently active
within a database, this function doesn't drop it. You must explicitly call
`DROP EXTENSION` to remove the TLE extension before using this function
to uninstall its artifacts.

### Function prototype

```
pgtle.uninstall_extension_if_exists(extname text)
```

### Role

`pgtle_admin`

### Arguments

- `extname` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.

### Output

The `uninstall_extension_if_exists` function returns `true`
after uninstalling the specified extension. If the specified extension doesn't
exist, the function returns `false`.

- `true` – Returns `true` after uninstalling the TLE extension.
- `false` – Returns `false` when the TLE extension doesn't
  exist in the database.

### Usage example

```
SELECT * FROM pgtle.uninstall_extension_if_exists('pg_tle_test');
```

## pgtle.uninstall_update_path

The `uninstall_update_path` function removes the specific update path from a TLE extension. This prevents `ALTER EXTENSION ... UPDATE TO` from using this as an update path.

If the TLE extension is currently being used by one of the versions on this update path, it remains in the database.

If the update path specified doesn't exist, this function raises an error.

### Function prototype

```
pgtle.uninstall_update_path(extname text, fromvers text, tovers text)
```

### Role

`pgtle_admin`

### Arguments

- `extname` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.
- `fromvers` – The source version of the TLE extension used on the update path.
- `tovers` – The destination version of the TLE extension used on the update path.

### Output

None.

### Usage example

```
SELECT * FROM pgtle.uninstall_update_path('pg_tle_test', '0.1', '0.2');
```

## pgtle.uninstall_update_path_if_exists

The `uninstall_update_path_if_exists` function is similar to
`uninstall_update_path` in that it removes the specified update path from
a TLE extension. However, if the update path doesn't exist, this function
doesn't raise an error message. Instead, the function returns
`false`.

### Function prototype

```
pgtle.uninstall_update_path_if_exists(extname text, fromvers text, tovers text)
```

### Role

`pgtle_admin`

### Arguments

- `extname` – The name of the TLE extension. This value is used when calling
  `CREATE EXTENSION`.
- `fromvers` – The source version of the TLE extension used on the update path.
- `tovers` – The destination version of the TLE extension used on the update path.

### Output

- `true` – The function has successfully updated the path for the TLE
  extension.
- `false` – The function wasn't able to update the path for the TLE
  extension.

### Usage example

```
SELECT * FROM pgtle.uninstall_update_path_if_exists('pg_tle_test', '0.1', '0.2');
```

## pgtle.unregister_feature

The `unregister_feature` function provides a way to remove functions that were
registered to use `pg_tle` features, such as hooks. For information about registering a feature,
see [pgtle.register_feature](#pgtle.register_feature "#pgtle.register_feature").

### Function prototype

```
pgtle.unregister_feature(proc regproc, feature pg_tle_features)
```

### Role

`pgtle_admin`

### Arguments

- `proc` – The name of a stored function to register with a `pg_tle` feature.
- `feature` – The name of the `pg_tle` feature to register with the function.
  For example, `passcheck` is a feature that can be registered for use by the trusted language
  extensions that you develop. For more information, see [Password-check hook (passcheck)](PostgreSQL_trusted_language_extension-hooks-reference.md#passcheck_hook "PostgreSQL_trusted_language_extension-hooks-reference.md#passcheck_hook").

### Output

None.

### Usage example

```
SELECT * FROM pgtle.unregister_feature('pw_hook', 'passcheck');
```

## pgtle.unregister_feature_if_exists

The `unregister_feature` function provides a way to remove functions that
were registered to use `pg_tle` features, such as hooks. For more
information, see [Using PostgreSQL hooks with your TLE extensions](PostgreSQL_trusted_language_extension.overview.md "PostgreSQL_trusted_language_extension.overview.md").
Returns `true` after successfully unregistering the feature. Returns
`false` if the feature wasn't registered.

For information about registering `pg_tle` features for your TLE extensions, see
[pgtle.register_feature](#pgtle.register_feature "#pgtle.register_feature").

### Function prototype

```
pgtle.unregister_feature_if_exists('proc regproc', 'feature pg_tle_features')
```

### Role

`pgtle_admin`

### Arguments

- `proc` – The name of the stored function that was registered to
  include a `pg_tle` feature.
- `feature` – The name of the `pg_tle` feature that was registered
  with the trusted language extension.

### Output

Returns `true` or `false`, as follows.

- `true` – The function has successfully unregistered the feature from
  extension.
- `false` – The function wasn't able to unregister the feature from the
  TLE extension.

### Usage example

```
SELECT * FROM pgtle.unregister_feature_if_exists('pw_hook', 'passcheck');
```
