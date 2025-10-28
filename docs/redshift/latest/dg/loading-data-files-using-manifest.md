Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using a manifest to specify

data files

You can use a manifest to make sure that the COPY command loads all of the
required files, and only the required files, for a data load. You can use a
manifest to load files from different buckets or files that do not share the same
prefix. Instead of supplying an object path for the COPY command, you supply the
name of a JSON-formatted text file that explicitly lists the files to be loaded.
The URL in the manifest must specify the bucket name and full object path for the
file, not just a prefix.

For more information about manifest files, see the COPY example [Using a manifest to specify data files](r_COPY_command_examples.md#copy-command-examples-manifest "r_COPY_command_examples.md#copy-command-examples-manifest").

The following example shows the JSON to load files from different
buckets and with file names that begin with date stamps.

```
{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket1/2013-10-04-custdata", "mandatory":true},
    {"url":"s3://amzn-s3-demo-bucket1/2013-10-05-custdata", "mandatory":true},
    {"url":"s3://amzn-s3-demo-bucket2/2013-10-04-custdata", "mandatory":true},
    {"url":"s3://amzn-s3-demo-bucket2/2013-10-05-custdata", "mandatory":true}
  ]
}
```

The optional `mandatory` flag specifies whether COPY should return
an error if the file is not found. The default of `mandatory` is
`false`. Regardless of any mandatory settings, COPY will terminate
if no files are found.

The following example runs the COPY command with the manifest in the previous
example, which is named `cust.manifest`.

```
COPY customer
FROM 's3://amzn-s3-demo-bucket/cust.manifest'
IAM_ROLE 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
MANIFEST;
```

## Using a manifest

created by UNLOAD

A manifest created by an [UNLOAD](r_UNLOAD.md "r_UNLOAD.md")
operation using the MANIFEST parameter might have keys that are not required
for the COPY operation. For example, the following `UNLOAD` manifest
includes a `meta` key that is required for an Amazon Redshift Spectrum external
table and for loading data files in an `ORC` or `Parquet`
file format. The `meta` key contains a `content_length`
key with a value that is the actual size of the file in bytes. The COPY
operation requires only the `url` key and an optional
`mandatory` key.

```
{
  "entries": [
    {"url":"s3://amzn-s3-demo-bucket/unload/manifest_0000_part_00", "meta": { "content_length": 5956875 }},
    {"url":"s3://amzn-s3-demo-bucket/unload/unload/manifest_0001_part_00", "meta": { "content_length": 5997091 }}
 ]
}
```

For more information about manifest files, see [Example: COPY from Amazon S3 using a manifest](r_COPY_command_examples.md#copy-command-examples-manifest "r_COPY_command_examples.md#copy-command-examples-manifest").
