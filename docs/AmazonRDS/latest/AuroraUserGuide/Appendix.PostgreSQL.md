# Working with extensions and foreign data wrappers

To extend the functionality to your Aurora PostgreSQL-Compatible Edition DB cluster, you can install
and use various PostgreSQL _extensions_. For example, if your use case calls for intensive
data entry across very large tables, you can install the `pg_partman`
extension to partition your data and thus spread the workload.

###### Note

As of Aurora PostgreSQL 14.5, Aurora PostgreSQL supports Trusted Language Extensions for PostgreSQL. This feature is implemented as
the extension `pg_tle`, which you can add to your Aurora PostgreSQL. By using
this extension, developers can create their own PostgreSQL extensions in a safe
environment that simplifies the setup and configuration requirements, as well as much of
the preliminary testing for new extensions. For more information, see [Working with Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension.md "PostgreSQL_trusted_language_extension.md").

In some cases, rather than installing an extension, you might add a specific _module_ to the list
of `shared_preload_libraries` in your Aurora PostgreSQL DB cluster's custom DB cluster parameter group.
Typically, the default DB cluster parameter group loads only the `pg_stat_statements`, but several
other modules are available to add to the list. For example, you can add scheduling capability by adding the
`pg_cron` module, as detailed in [Scheduling maintenance with the PostgreSQL pg_cron extension](PostgreSQL_pg_cron.md "PostgreSQL_pg_cron.md"). As another example, you can log query execution plans by
loading the `auto_explain` module. To learn more, see
[Logging execution plans
of queries](https://aws.amazon.com/premiumsupport/knowledge-center/rds-postgresql-tune-query-performance/# "https://aws.amazon.com/premiumsupport/knowledge-center/rds-postgresql-tune-query-performance/#") in the AWS knowledge center.

An extension that provides access to external data is
more specifically known as a _foreign data wrapper_
(FDW). As one example, the `oracle_fdw` extension allows your Aurora PostgreSQL DB
cluster to work with Oracle databases.

You can also specify precisely which extensions can be installed on your Aurora PostgreSQL DB instance, by
listing them in the `rds.allowed_extensions` parameter. For more information, see [Restricting installation of PostgreSQL extensions](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction.html "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction.html").

Following, you can find information about setting up and using some of the extensions, modules, and
FDWs available for Aurora PostgreSQL. For simplicity's sake, these are all referred to as "extensions." You can find
listings of extensions that you can use with the currently available Aurora PostgreSQL versions, see [Extension
versions for Amazon Aurora PostgreSQL](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md") in the _Release Notes for Aurora PostgreSQL_.

- [Managing large objects with the lo module](PostgreSQL_large_objects_lo_extension.md "PostgreSQL_large_objects_lo_extension.md")
- [Managing spatial data with the PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Managing PostgreSQL partitions with the pg_partman extension](PostgreSQL_Partitions.md "PostgreSQL_Partitions.md")
- [Scheduling maintenance with the PostgreSQL pg_cron extension](PostgreSQL_pg_cron.md "PostgreSQL_pg_cron.md")
- [Using pgAudit to log database activity](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Using pglogical to synchronize data across instances](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Working with Oracle databases by using the oracle_fdw extension](postgresql-oracle-fdw.md "postgresql-oracle-fdw.md")
- [Working with SQL Server databases by using the tds_fdw extension](postgresql-tds-fdw.md "postgresql-tds-fdw.md")
