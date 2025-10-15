# Controlling access to metadata tables

To control access to your Amazon S3 metadata tables, you can use AWS Identity and Access Management (IAM) resource-based
 policies that are attached to your table bucket and to your metadata tables. In other words, you can
 control access to your metadata tables at both the table bucket level and the table level. 

For more information about controlling access to your table buckets and tables, see [Access
 management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").

###### Important

When you're creating or updating table bucket or table policies, make sure that you don't restrict
 the Amazon S3 service principals `metadata.s3.amazonaws.com` and
 `maintenance.s3tables.amazonaws.com` from writing to your table bucket or your metadata
 tables. 

If Amazon S3 is unable to write to your table bucket or your metadata tables, you must delete your
 metadata configuration, delete your metadata tables, and then create a new configuration. If you had
 an inventory table in your configuration, a new inventory table has to be created, and you will be
 charged again for backfilling the new inventory table.

You can also control access to the rows and columns in your metadata tables through AWS Lake Formation. For
 more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html "https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html") and [Data filtering and cell-level
 security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html "https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html") in the *AWS Lake Formation Developer Guide*.
