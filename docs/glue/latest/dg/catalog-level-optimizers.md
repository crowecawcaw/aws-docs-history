# Catalog-level table optimizers

With a one-time catalog configuration, you can set up automatic optimizers such as
compaction, snapshot retention, and orphan file deletion for all new and updated Apache Iceberg
tables in the AWS Glue Data Catalog. Catalog-level optimizer configurations allow you to apply consistent
optimizer settings across all tables within a catalog, eliminating the need to configure
optimizers individually for each table.

Data lake administrators can configure the table optimizers by selecting the default catalog
in the Lake Formation console and enabling optimizers using the `Table optimization`
option. When you create new tables or update existing tables in the Data Catalog, the Data Catalog
automatically runs the table optimizations to reduce operational burden.

If you have configured optimization at the table level or if you have previously deleted the
table optimization settings for a table, those table-specific settings take precedence over the
default catalog settings for table optimization. If a configuration parameter is not defined at
either the table or catalog level, the Iceberg table property value will be applied. This
setting is applicable to snapshot retention and orphan file deletion optimizer.

When enabling catalog-level optimizers, consider the following:

- When you configure optimization settings at the time of catalog creation and subsequently disable the optimizations through an Update Catalog request, the operation will cascade through all the tables within the catalog.
- If you have already configured optimizers for a given table, then the disable operation at the catalog level will not impact this table.
- When you disable optimizers at the catalog level, tables with existing optimizer
  configurations will maintain their specific settings and remain unaffected by the
  catalog-level change. However, tables without their own optimizer configurations will
  inherit the disabled state from the catalog level.
- Since snapshot retention and orphan file deletion optimizers can be schedule-based, updates will introduce a random delay to the start of their schedule. This will cause each optimizer to start at slightly different times, spreading out the load and reducing the likelihood of exceeding service limits.

###### Topics

- [Enabling catalog-level automatic table optimization](enable-auto-table-optimizers.md "enable-auto-table-optimizers.md")
- [Viewing catalog-level optimizations](view-catalog-optimizations.md "view-catalog-optimizations.md")
- [Disabling catalog-level table optimization](disable-auto-table-optimizers.md "disable-auto-table-optimizers.md")
