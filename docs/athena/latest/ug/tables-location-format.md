# Specify a table location in Amazon S3

When you run a `CREATE TABLE` query in Athena, Athena registers your table with
the AWS Glue Data Catalog, which is where Athena stores your metadata.

To specify the path to your data in Amazon S3, use the `LOCATION` property in your
`CREATE TABLE` statement, as in the following example:

```
CREATE EXTERNAL TABLE `test_table`(
...
)
ROW FORMAT ...
STORED AS INPUTFORMAT ...
OUTPUTFORMAT ...
LOCATION s3://amzn-s3-demo-bucket/`folder`/
```

- For information about naming buckets, see [Bucket restrictions and
  limitations](../../../AmazonS3/latest/dev/BucketRestrictions.md "../../../AmazonS3/latest/dev/BucketRestrictions.md") in the _Amazon Simple Storage Service User Guide_.
- For information about using folders in Amazon S3, see [Using folders](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the
  _Amazon Simple Storage Service User Guide._
  The `LOCATION` in Amazon S3 specifies _all_ of the files
  representing your table.

###### Important

Athena reads _all_ data stored in the Amazon S3 folder that you specify.
If you have data that you do _not_ want Athena to read, do not store
that data in the same Amazon S3 folder as the data that you do want Athena to read.

When you specify the `LOCATION` in the `CREATE TABLE` statement, use
the following guidelines:

- Use a trailing slash.
- You can use a path to an Amazon S3 folder or an Amazon S3 access point alias. For
  information about Amazon S3 access point aliases, see [Using a bucket-style
  alias for your access point](../../../AmazonS3/latest/userguide/access-points-alias.md "../../../AmazonS3/latest/userguide/access-points-alias.md") in the _Amazon S3 User Guide_.

**Use**:

```
s3://amzn-s3-demo-bucket/`folder`/
```

```
s3://amzn-s3-demo-bucket-`metadata`-s3alias/`folder`/
```

Do not use any of the following items for specifying the `LOCATION` for your
data.

- Do not use filenames, underscores, wildcards, or glob patterns for specifying file
  locations.
- Do not add the full HTTP notation, such as `s3.amazon.com` to the Amazon S3
  bucket path.
- Do not use empty folders like `//` in the path, as follows:
  `S3://amzn-s3-demo-bucket/`folder`//`folder`/`.
- Do not use paths like the following:

```
s3://amzn-s3-demo-bucket
s3://amzn-s3-demo-bucket/*
s3://amzn-s3-demo-bucket/mySpecialFile.dat
s3://amzn-s3-demo-bucket/prefix/filename.csv
s3://amzn-s3-demo-bucket.s3.amazon.com
S3://amzn-s3-demo-bucket/prefix//prefix/
arn:aws:s3:::amzn-s3-demo-bucket/prefix
s3://arn:aws:s3:`<region>`:`<account_id>`:accesspoint/`<accesspointname>`
https://`<accesspointname>`-`<number>`.s3-accesspoint.`<region>`.amazonaws.com
```
