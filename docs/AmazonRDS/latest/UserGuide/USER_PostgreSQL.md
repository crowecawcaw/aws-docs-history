# Importing data from Amazon S3 into an RDS for PostgreSQL DB instance

You can import data that's been stored using Amazon Simple Storage Service into a table on an RDS for PostgreSQL DB
instance. To do this, you first install the
RDS for PostgreSQL `aws_s3` extension. This extension provides
the functions that you use to import data from an Amazon S3 bucket. A _bucket_ is an Amazon S3 container for objects
and files.
The data can be in a comma-separate value (CSV) file, a text file,
or a compressed (gzip) file. Following, you can learn how to install the extension and how to import data
from Amazon S3 into a table.

Your database must be running PostgreSQL version 10.7 or higher to import from Amazon S3 into
RDS for PostgreSQL.

If you don't have data stored on Amazon S3, you need to first create a bucket and store the data.
For more information, see the following topics in the _Amazon Simple Storage Service User Guide_.

- [Create a bucket](../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket "../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket")
- [Add an object to a
  bucket](../../../AmazonS3/latest/userguide/GetStartedWithS3.md#uploading-an-object-bucket "../../../AmazonS3/latest/userguide/GetStartedWithS3.md#uploading-an-object-bucket")
  Cross-account import from Amazon S3 is supported. For more information, see [Granting cross-account permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in the _Amazon Simple Storage Service User Guide_.

You can use the customer managed key for encryption while importing data from S3. For more information, see [KMS keys stored in AWS KMS](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") in the _Amazon Simple Storage Service User Guide_.

###### Topics

- [Installing the aws_s3 extension](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md")
- [Overview of importing data from Amazon S3 data](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md")
- [Setting up access to an Amazon S3 bucket](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md")
- [Importing data from Amazon S3 to your RDS for PostgreSQL DB instance](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md")
- [Function reference](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md")
