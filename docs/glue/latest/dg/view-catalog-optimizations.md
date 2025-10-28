# Viewing catalog-level optimizations

When catalog-level table optimization is enabled, anytime an Apache Iceberg table is created or updated
via the `CreateTable` or `UpdateTable` APIs through AWS Management Console, SDK, or AWS Glue crawler,
an equivalent table level setting is created for that table.

After you create or update a table, you can verify the table details to confirm the table optimization.
The `Table optimization` shows the `Configuration source` property set as `Catalog`.

![An image of an Apache Iceberg table with catalog-level optimization configuration has
 been applied.](images/catalog-optimization-enabled.png)
