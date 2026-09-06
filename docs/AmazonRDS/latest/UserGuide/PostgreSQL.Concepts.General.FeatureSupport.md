

# Working with PostgreSQL features supported by Amazon RDS for PostgreSQL
<a name="PostgreSQL.Concepts.General.FeatureSupport"></a>

Amazon RDS for PostgreSQL supports many of the most common PostgreSQL features. For example, PostgreSQL has an autovacuum feature that performs routine maintenance on the database. The autovacuum feature is active by default. Although you can turn off this feature, we highly recommend that you keep it on. Understanding this feature and what you can do to make sure it works as it should is a basic task of any DBA. For more information about the autovacuum, see [Working with PostgreSQL autovacuum on Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md). To learn more about other common DBA tasks, [Common DBA tasks for Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md). 

RDS for PostgreSQL also supports extensions that add important functionality to the DB instance. For example, you can use the PostGIS extension to work with spatial data, or use the pg\_cron extension to schedule maintenance from within the instance. For more information about PostgreSQL extensions, see [Using PostgreSQL extensions with Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Extensions.md). 

Foreign data wrappers are a specific type of extension designed to let your RDS for PostgreSQL DB instance work with other commercial databases or data types. For more information about foreign data wrappers supported by RDS for PostgreSQL, see [Working with the supported foreign data wrappers for Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Extensions.foreign-data-wrappers.md). 

Following, you can find information about some other features supported by RDS for PostgreSQL. 

**Topics**
+ [Custom data types and enumerations with RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.AlterEnum.md)
+ [Event triggers for RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.EventTriggers.md)
+ [Huge pages for RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.HugePages.md)
+ [Performing logical replication for Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication.md)
+ [Configuring IAM authentication for logical replication connections](PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.md)
+ [RAM disk for the stats\_temp\_directory](PostgreSQL.Concepts.General.FeatureSupport.RamDisk.md)
+ [Tablespaces for RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.Tablespaces.md)
+ [RDS for PostgreSQL collations for EBCDIC and other mainframe migrations](PostgreSQL.Collations.mainframe.migration.md)
+ [Managing logical slot synchronization for RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.pglogical.slot.synchronization.md)