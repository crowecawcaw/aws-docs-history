# Supported

PostgreSQL extension versions

RDS for PostgreSQL supports many PostgreSQL extensions. The PostgreSQL community sometimes
refers to these as modules. Extensions expand on the functionality provided by the
PostgreSQL engine. You can find a list of extensions supported by Amazon RDS in the default
DB parameter group for that PostgreSQL version. You can also see the current extensions
list using `psql` by showing the `rds.extensions` parameter as in
the following example.

```
SHOW rds.extensions;
```

###### Note

Parameters added in a minor version release might display inaccurately when using
the `rds.extensions` parameter in `psql`.

As of RDS for PostgreSQL 13, certain extensions can be installed by database users other
than the `rds_superuser`. These are known as _trusted
extensions_. To learn more, see [PostgreSQL trusted
extensions](#PostgreSQL.Concepts.General.Extensions.Trusted "#PostgreSQL.Concepts.General.Extensions.Trusted").

Certain versions of RDS for PostgreSQL support the `rds.allowed_extensions`
parameter. This parameter lets an `rds_superuser` limit the extensions that
can be installed in the RDS for PostgreSQL DB instance. For more information, see [Restricting installation of PostgreSQL extensions](#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction "#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction").

For lists of PostgreSQL extensions and versions that are supported by each available
RDS for PostgreSQL version, see [PostgreSQL
extensions supported on Amazon RDS](../PostgreSQLReleaseNotes/postgresql-extensions.md "../PostgreSQLReleaseNotes/postgresql-extensions.md") in _Amazon RDS for PostgreSQL Release Notes_.

## Restricting installation of PostgreSQL extensions

You can restrict which extensions can be installed on a PostgreSQL DB instance. By
default, this parameter isn't set, so any supported extension can be added if
the user has permissions to do so. To do so, set the
`rds.allowed_extensions` parameter to a string of comma-separated
extension names. By adding a list of extensions to this parameter, you explicitly
identify the extensions that your RDS for PostgreSQL DB instance can use. Only these
extensions can then be installed in the PostgreSQL DB instance.

The default string for the `rds.allowed_extensions` parameter is '\*',
which means that any extension available for the engine version can be installed.
Changing the `rds.allowed_extensions` parameter does not require a
database restart because it's a dynamic parameter.

The PostgreSQL DB instance engine must be one of the following versions for you to
use the `rds.allowed_extensions` parameter:

- All PostgreSQL 16 versions
- PostgreSQL 15 and all higher versions
- PostgreSQL 14 and all higher versions
- PostgreSQL 13.3 and higher minor versions
- PostgreSQL 12.7 and higher minor versions

To see which extension installations are allowed, use the following psql
command.

```
`postgres=>` `SHOW rds.allowed_extensions;`
 `rds.allowed_extensions
------------------------
 *`
```

If an extension was installed prior to it being left out of the list in the
`rds.allowed_extensions` parameter, the extension can still be used
normally, and commands such as `ALTER EXTENSION` and `DROP
 EXTENSION` will continue to work. However, after an extension is
restricted, `CREATE EXTENSION` commands for the restricted extension will
fail.

Installation of extension dependencies with `CREATE EXTENSION CASCADE`
are also restricted. The extension and its dependencies must be specified in
`rds.allowed_extensions`. If an extension dependency installation
fails, the entire `CREATE EXTENSION CASCADE` statement will fail.

If an extension is not included with the `rds.allowed_extensions`
parameter, you will see an error such as the following if you try to install
it.

```
ERROR: permission denied to create extension "`extension-name`"
HINT: This extension is not specified in "rds.allowed_extensions".
```

## PostgreSQL trusted

extensions

To install most PostgreSQL extensions requires `rds_superuser`
privileges. PostgreSQL 13 introduced trusted extensions, which reduce the need to
grant `rds_superuser` privileges to regular users. With this feature,
users can install many extensions if they have the `CREATE` privilege on
the current database instead of requiring the `rds_superuser` role. For
more information, see the SQL [CREATE
EXTENSION](https://www.postgresql.org/docs/current/sql-createextension.html "https://www.postgresql.org/docs/current/sql-createextension.html") command in the PostgreSQL documentation.

The following lists the extensions that can be installed by a user who has the
`CREATE` privilege on the current database and do not require the
`rds_superuser` role:

- bool_plperl
- [btree_gin](http://www.postgresql.org/docs/current/btree-gin.html "http://www.postgresql.org/docs/current/btree-gin.html")
- [btree_gist](http://www.postgresql.org/docs/current/btree-gist.html "http://www.postgresql.org/docs/current/btree-gist.html")
- [citext](http://www.postgresql.org/docs/current/citext.html "http://www.postgresql.org/docs/current/citext.html")
- [cube](http://www.postgresql.org/docs/current/cube.html "http://www.postgresql.org/docs/current/cube.html")
- [dict_int](http://www.postgresql.org/docs/current/dict-int.html "http://www.postgresql.org/docs/current/dict-int.html")
- [fuzzystrmatch](http://www.postgresql.org/docs/current/fuzzystrmatch.html "http://www.postgresql.org/docs/current/fuzzystrmatch.html")
- [hstore](http://www.postgresql.org/docs/current/hstore.html "http://www.postgresql.org/docs/current/hstore.html")
- [intarray](http://www.postgresql.org/docs/current/intarray.html "http://www.postgresql.org/docs/current/intarray.html")
- [isn](http://www.postgresql.org/docs/current/isn.html "http://www.postgresql.org/docs/current/isn.html")
- jsonb_plperl
- [ltree](http://www.postgresql.org/docs/current/ltree.html "http://www.postgresql.org/docs/current/ltree.html")
- [pg_trgm](http://www.postgresql.org/docs/current/pgtrgm.html "http://www.postgresql.org/docs/current/pgtrgm.html")
- [pgcrypto](http://www.postgresql.org/docs/current/pgcrypto.html "http://www.postgresql.org/docs/current/pgcrypto.html")
- [plperl](https://www.postgresql.org/docs/current/plperl.html "https://www.postgresql.org/docs/current/plperl.html")
- [plpgsql](https://www.postgresql.org/docs/current/plpgsql.html "https://www.postgresql.org/docs/current/plpgsql.html")
- [pltcl](https://www.postgresql.org/docs/current/pltcl-overview.html "https://www.postgresql.org/docs/current/pltcl-overview.html")
- [tablefunc](http://www.postgresql.org/docs/current/tablefunc.html "http://www.postgresql.org/docs/current/tablefunc.html")
- [tsm_system_rows](https://www.postgresql.org/docs/current/tsm-system-rows.html "https://www.postgresql.org/docs/current/tsm-system-rows.html")
- [tsm_system_time](https://www.postgresql.org/docs/current/tsm-system-time.html "https://www.postgresql.org/docs/current/tsm-system-time.html")
- [unaccent](http://www.postgresql.org/docs/current/unaccent.html "http://www.postgresql.org/docs/current/unaccent.html")
- [uuid-ossp](http://www.postgresql.org/docs/current/uuid-ossp.html "http://www.postgresql.org/docs/current/uuid-ossp.html")

For lists of PostgreSQL extensions and versions that are supported by each available
RDS for PostgreSQL version, see [PostgreSQL
extensions supported on Amazon RDS](../PostgreSQLReleaseNotes/postgresql-extensions.md "../PostgreSQLReleaseNotes/postgresql-extensions.md") in _Amazon RDS for PostgreSQL Release Notes_.
