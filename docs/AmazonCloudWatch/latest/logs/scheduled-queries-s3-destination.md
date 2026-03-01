# Configuring S3 destinations for scheduled queries

Configure Amazon S3 as a destination to store your scheduled query results as JSON
files for long-term retention and analysis.

When using Amazon S3 as a destination, query results are stored as JSON files in the
specified bucket and prefix. This option is ideal for archiving results, performing
batch analysis, or integrating with other AWS services that process S3 data.

The Amazon S3 destination configuration includes the following options:

**Amazon S3 URI**

The bucket and optional prefix where results will be stored (for example,
`s3://my-bucket/query-results/`). Enter the full Amazon S3 URI in
the box.

**View Amazon S3**

Choose this option to open the Amazon S3 console in a new tab, allowing you to
verify the bucket exists and check its configuration.

**Browse Amazon S3**

Choose this option to open the Amazon S3 browser, where you can navigate and
select an existing Amazon S3 location without manually typing the URI.

Required IAM permissions for Amazon S3 destinations:

- `s3:PutObject` - Permission to write query result files to the
  specified Amazon S3 bucket
  The IAM role for posting query results to Amazon S3 must be configured separately from
  the IAM role for scheduled query execution. This separation allows for fine-grained
  access control, where the execution role can run queries while the Amazon S3 role
  specifically handles result delivery.
