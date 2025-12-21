# Using PostgreSQL extensions with

Amazon RDS for PostgreSQL

You can extend the functionality of PostgreSQL by installing a variety of extensions and
modules. For example, to work with spatial data you can install and use the PostGIS extension.
For more information, see [Managing spatial data with the
PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md"). As another example, if you want
to improve data entry for very large tables, you can consider partitioning your data by using
the `pg_partman` extension. To learn more, see [Managing PostgreSQL partitions with the pg_partman extension](PostgreSQL_Partitions.md "PostgreSQL_Partitions.md").

###### Note

RDS for PostgreSQL supports Trusted Language Extensions for PostgreSQL through the `pg_tle` extension, which you
can add to your DB instance. By using this extension, developers can create their own
PostgreSQL extensions in a safe environment that simplifies the setup and configuration
requirements. To learn about RDS for PostgreSQL versions supporting `pg_tle` extension
and for more information, see [Working with Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension.md "PostgreSQL_trusted_language_extension.md").

In some cases, rather than installing an extension, you might add a specific module to the
list of `shared_preload_libraries` in your RDS for PostgreSQL DB instance's custom DB
parameter group. Typically, the default DB cluster parameter group loads only the
`pg_stat_statements`, but several other modules are available to add to the list.
For example, you can add scheduling capability by adding the `pg_cron` module, as
detailed in [Scheduling maintenance with the PostgreSQL pg_cron
extension](PostgreSQL_pg_cron.md "PostgreSQL_pg_cron.md"). As another
example, you can log query execution plans by loading the `auto_explain` module. To
learn more, see [Logging execution plans of queries](https://aws.amazon.com/premiumsupport/knowledge-center/rds-postgresql-tune-query-performance/# "https://aws.amazon.com/premiumsupport/knowledge-center/rds-postgresql-tune-query-performance/#") in the AWS knowledge center.

Depending on your version of RDS for PostgreSQL, installing an extension might require
`rds_superuser` permissions, as follows:

- For RDS for PostgreSQL versions 12 and earlier versions, installing extensions requires
  `rds_superuser` privileges.
- For RDS for PostgreSQL version 13 and higher versions, users (roles) with create permissions
  on a given database instance can install and use any _trusted
  extensions_. For a list of trusted extensions, see [PostgreSQL trusted
  extensions](PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.Extensions.Trusted "PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.Extensions.Trusted").
  You can also specify precisely which extensions can be installed on your RDS for PostgreSQL DB
  instance, by listing them in the `rds.allowed_extensions` parameter. For more
  information, see [Restricting installation of PostgreSQL extensions](PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction "PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.FeatureSupport.Extensions.Restriction").

To learn more about the `rds_superuser` role, see [Understanding PostgreSQL roles and
permissions](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

###### Topics

- [Using functions from the orafce
  extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Using Amazon RDS delegated extension support for PostgreSQL](RDS_delegated_ext.md "RDS_delegated_ext.md")
- [Managing PostgreSQL partitions with the pg_partman extension](PostgreSQL_Partitions.md "PostgreSQL_Partitions.md")
- [Using pgAudit to log database activity](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Scheduling maintenance with the PostgreSQL pg_cron
  extension](PostgreSQL_pg_cron.md "PostgreSQL_pg_cron.md")
- [Using pglogical to synchronize
  data across instances](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Using pgactive to support
  active-active replication](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Reducing bloat in tables and
  indexes with the pg_repack extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
- [Upgrading and using the PLV8
  extension](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md")
- [Using PL/Rust to write PostgreSQL
  functions in the Rust language](PostgreSQL.Concepts.General.Using.md "PostgreSQL.Concepts.General.Using.md")
- [Managing spatial data with the
  PostGIS extension](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")
