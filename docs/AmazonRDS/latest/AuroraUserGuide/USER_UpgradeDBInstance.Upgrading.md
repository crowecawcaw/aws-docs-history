# Upgrading

PostgreSQL extensions

Upgrading your Aurora PostgreSQL DB cluster to a new major or minor version doesn't
upgrade the PostgreSQL extensions at the same time. For most extensions, you upgrade the
extension after the major or minor version upgrade completes. However, in some cases,
you upgrade the extension before you upgrade the Aurora PostgreSQL DB engine. For more
information, see the [list of extensions to update](USER_UpgradeDBInstance.PostgreSQL.md#upgrade-extensions "USER_UpgradeDBInstance.PostgreSQL.md#upgrade-extensions") in
[Testing an upgrade of your production DB cluster to a new major version](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary").

Installing PostgreSQL extensions requires `rds_superuser` privileges.
Typically, an `rds_superuser` delegates permissions over specific extensions
to relevant users (roles), to facilitate the management of a given extension. That means
that the task of upgrading all the extensions in your Aurora PostgreSQL DB cluster might involve
many different users (roles). Keep this in mind especially if you want to automate the
upgrade process by using scripts. For more information about PostgreSQL privileges and
roles, see [Security with Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

###### Note

For information about updating the PostGIS extension, see [Managing spatial data with the
PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md") ([Step 6: Upgrade the
PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update "Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.PostGIS.Update")).

To update the `pg_repack` extension, drop the extension and then create
the new version in the upgraded DB instance. For more information, see [pg_repack installation](https://reorg.github.io/pg_repack/ "https://reorg.github.io/pg_repack/") in the
`pg_repack` documentation.

To update an extension after an engine upgrade, use the `ALTER EXTENSION
 UPDATE` command.

```
ALTER EXTENSION `extension_name` UPDATE TO '`new_version`';
```

To list your currently installed extensions, use the PostgreSQL [pg_extension](https://www.postgresql.org/docs/current/catalog-pg-extension.html "https://www.postgresql.org/docs/current/catalog-pg-extension.html") catalog in the following command.

```
SELECT * FROM pg_extension;
```

To view a list of the specific extension versions that are available for your
installation, use the PostgreSQL [pg_available_extension_versions](https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html "https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html") view in the following command.

```
SELECT * FROM pg_available_extension_versions;
```
