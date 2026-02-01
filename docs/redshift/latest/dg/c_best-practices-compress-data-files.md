Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Compressing your data files

When you want to compress large load files, we recommend that you use gzip, lzop,
bzip2, or Zstandard to compress them and split the data into multiple smaller
files.

Specify the GZIP, LZOP, BZIP2, or ZSTD option with the COPY command. This example loads the
TIME table from a pipe-delimited lzop file.

```
copy time
from 's3://amzn-s3-demo-bucket/data/timerows.lzo'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
lzop
delimiter '|';
```

There are instances when you don't have to split uncompressed data files. For more information about splitting your data and examples of
using COPY to load data, see [Loading data from Amazon S3](t_Loading-data-from-S3.md "t_Loading-data-from-S3.md").
