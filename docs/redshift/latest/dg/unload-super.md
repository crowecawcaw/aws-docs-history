Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Unloading semi-structured data

With Amazon Redshift, you can export semi-structured data from your Amazon Redshift cluster to Amazon S3 in a variety of formats,
including text, Apache Parquet, Apache ORC, and Avro. The following sections will guide you through the
process of configuring and executing unload operations for your semi-structured data in Amazon Redshift.

CSV or text formats
You can unload tables with SUPER data columns to Amazon S3 in a comma-separated value (CSV)
or text format. Using a combination of navigation and unnest clauses, Amazon Redshift unloads
hierarchical data in SUPER data format to Amazon S3 in CSV or text formats. Subsequently, you
can create external tables against unloaded data and query them using Redshift Spectrum. For
information on using UNLOAD and the required IAM permissions, see [UNLOAD](r_UNLOAD.md "r_UNLOAD.md").

The following example unloads all of the data from an Amazon Redshift table into an Amazon S3 bucket.

```
UNLOAD ('SELECT * FROM <`redshift_table`>')
TO '<`S3_bucket`>'
IAM_ROLE '<`iam_role`>'
DELIMITER AS '|'
GZIP
ALLOWOVERWRITE;
```

Unlike other data types where a user-defined string represents a null value, Amazon Redshift
exports the SUPER data columns using the JSON format and represents it as
_null_ as determined by the JSON format. As a result, SUPER data
columns ignore the NULL [AS] option used in UNLOAD commands.

Parquet format
You can unload tables with SUPER data columns to Amazon S3 in the Parquet format. Amazon Redshift represents SUPER columns in Parquet as the JSON data type.
This enables semi-structured data to be represented in Parquet. You can query these columns using Redshift Spectrum or ingest them back to Amazon Redshift using the COPY command. For
information on using UNLOAD and the required IAM permissions, see [UNLOAD](r_UNLOAD.md "r_UNLOAD.md").

The following example unloads all of the data from an Amazon Redshift table into an Amazon S3 bucket in the Parquet format.

```
UNLOAD ('SELECT * FROM <`Amazon Redshift_table`>')
TO '<`S3_bucket`>'
IAM_ROLE '<`iam_role`>'
FORMAT PARQUET;
```
