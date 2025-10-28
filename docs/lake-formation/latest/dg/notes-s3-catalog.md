#

S3 tables catalog integration limitations

You can integrate Amazon S3 table buckets and tables with AWS Glue Data Catalog (Data Catalog), and register the
catalog as a Lake Formation data location from the Lake Formation console or using service APIs.

The following limitations apply to integrating S3 tables catalog with Data Catalog and Lake Formation:

- AWS Glue and Lake Formation don't support mixed-case column names, and convert all column names to
  lowercase. You must verify that table column names are unique when converted to lowercase.
  Use `customer_id` instead of `customerId`. The use of mixed-case
  column names was supported only during the preview release.
- The CreateCatalog API cannot create table buckets in Amazon S3.
- The SearchTables API cannot search S3 tables.
