#

S3 Tables catalog integration limitations

Amazon S3 Tables integrates with AWS Glue Data Catalog (Data Catalog) and registers the catalog as a Lake Formation data location. You can set up this registration from the Lake Formation console or by using the service APIs.

###### Note

If you have an IAM or S3 Tables resource-based policy that restricts IAM users and
IAM roles based on principal tags, you must attach the same principal tags to the IAM role
that Lake Formation uses to access your S3 data (for example, LakeFormationDataAccessRole) and
grant this role the necessary permissions. This is required for your tag-based access control
policy to work correctly with your S3 Tables analytics integration.

The following limitations apply to integrating S3 Tables catalog with Data Catalog and Lake Formation:

- AWS Glue and Lake Formation don't support mixed-case column names, and convert all column names to
  lowercase. You must verify that table column names are unique when converted to lowercase.
  Use `customer_id` instead of `customerId`. The use of mixed-case
  column names was supported only during the preview release.
- The CreateCatalog API cannot create table buckets in Amazon S3.
- The SearchTables API cannot search S3 Tables.
