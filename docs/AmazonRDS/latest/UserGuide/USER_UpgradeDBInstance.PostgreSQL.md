# Upgrading PostgreSQL extensions in RDS for PostgreSQL databases

A PostgreSQL engine upgrade doesn't upgrade most PostgreSQL extensions.
To update an extension after a version upgrade, use the `ALTER
 EXTENSION UPDATE` command.

###### Note

For information about updating the PostGIS extension, see [Managing spatial data with the
PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
([Step 6: Upgrade the
PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update "Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update")).

To update the `pg_repack` extension, drop the extension and
then create the new version in the upgraded database. For more
information, see [pg_repack installation](https://reorg.github.io/pg_repack/ "https://reorg.github.io/pg_repack/") in the
`pg_repack` documentation.

To upgrade an extension, use the following command.

```
ALTER EXTENSION `extension_name` UPDATE TO '`new_version`';
```

For the list of supported versions of PostgreSQL extensions, see [Supported
PostgreSQL extension versions](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md").

To list your currently installed extensions, use the PostgreSQL [pg_extension](https://www.postgresql.org/docs/current/catalog-pg-extension.html "https://www.postgresql.org/docs/current/catalog-pg-extension.html") catalog in the following command.

```
SELECT * FROM pg_extension;
```

To view a list of the specific extension versions that are available for your
installation, use the PostgreSQL [pg_available_extension_versions](https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html "https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html") view in the following
command.

```
SELECT * FROM pg_available_extension_versions;
```
