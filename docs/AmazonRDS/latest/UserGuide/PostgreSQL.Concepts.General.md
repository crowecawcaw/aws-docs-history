# Working with PostgreSQL

features supported by Amazon RDS for PostgreSQL

Amazon RDS for PostgreSQL supports many of the most common PostgreSQL features. For example,
PostgreSQL has an autovacuum feature that performs routine maintenance on the database.
The autovacuum feature is active by default. Although you can turn off this feature, we
highly recommend that you keep it on. Understanding this feature and what you can do to
make sure it works as it should is a basic task of any DBA. For more information about
the autovacuum, see [Working with PostgreSQL
autovacuum on Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md"). To learn more about
other common DBA tasks, [Common DBA tasks for
Amazon RDS for PostgreSQL](Appendix.PostgreSQL.md "Appendix.PostgreSQL.md").

RDS for PostgreSQL also supports extensions that add important functionality to the DB
instance. For example, you can use the PostGIS extension to work with spatial data, or
use the pg_cron extension to schedule maintenance from within the instance. For more
information about PostgreSQL extensions, see [Using PostgreSQL extensions with
Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

Foreign data wrappers are a specific type of extension designed to let your
RDS for PostgreSQL DB instance work with other commercial databases or data types. For more
information about foreign data wrappers supported by RDS for PostgreSQL, see [Working
with the supported foreign data wrappers for Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Extensions.md "Appendix.PostgreSQL.CommonDBATasks.Extensions.md").

Following, you can find information about some other features supported by
RDS for PostgreSQL.

###### Topics

- [Custom data
  types and enumerations with RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [Event
  triggers for RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [Huge pages
  for RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [Performing
  logical replication for Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [Configuring IAM authentication for logical replication connections](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [RAM disk for
  the stats_temp_directory](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [Tablespaces for RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md")
- [RDS for PostgreSQL collations
  for EBCDIC and other mainframe migrations](PostgreSQL.Collations.mainframe.md "PostgreSQL.Collations.mainframe.md")
- [Managing logical slot synchronization for RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.pglogical.slot.md "Appendix.PostgreSQL.CommonDBATasks.pglogical.slot.md")
