# Understanding export delivery

In the following sections, you'll find information about your export delivery.

- **Export S3 parent directory structure:** How export data
  is structured in the S3 directory to which your export is delivered to.
- **Export refreshing:** How often your export updates in
  your S3 directory.
- **Export overwriting and create new:** How your export
  delivery changes with overwriting and creates new delivery preferences.
- **Export data file names and chunks:** How the export
  files (gzip/csv or Parquet) are named.

## Export S3 parent directory

structure

Each export delivers the data from the query to S3 (as one or more gzip/csv or Parquet
files) and a `Manifest.json` metadata file containing information about the
export definition at the time the export was executed.

**Data**

The data resulting from the export query is stored in the following S3 file
path:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/`

The partition corresponds to the table that is being queried. For CUR 2.0, the
partition corresponds to the “billing period” of a given CUR 2.0 export.

`prefix`: The S3 file prefix that you assign to the export.

`export-name`: The name that you assign to the export.

`partition`: The partition describes how a single table is partitioned
into separate tables for delivery. For CUR 2.0, the partition corresponds to the
“billing period” in the format `BILLING_PERIOD=YYYY-MM`. For example, the
partition for November 2023 is 2023-11.

The following is an example of an S3 file path:

`s3://my-data-export-s3-bucket/my-cur-files/business_group_a_cur/data/BILLING_PERIOD=2023-11`

**Metadata**

The `Manifest.json` metadata file for the query is stored in the
following S3 file path:

`s3://<bucket-name>/<prefix>/<export-name>/metadata/<partition>/<export-name>-Manifest.json`

The `Manifest.json` file is updated each time the export is refreshed.
A new `Manifest.json` file is created for each new partition created by the
export. For CUR 2.0, this means a new `Manifest.json` file is generated
when a new billing period begins.

Manifest files contain the following information:

- All of the columns that are included in the export.
- A list of the export files and their file path. We recommend identifying which
  files to ingest by programmatically reading this list.
- The time period covered by the export.

The `Manifest.json` is only delivered once all of the export data files
have been delivered to S3.

## Export refreshing

Data Exports refreshes your exports each time the source data is updated. For CUR 2.0, this
occurs at least once a day. The current billing period (partition) is refreshed until the
billing period ends, at which point deliveries of the next billing period begin. Deliveries
of the next billing period only contain charges and billing data for that billing period.
After the billing period ends, AWS may update the export delivery for the previous billing
period within the first two weeks after it ended.

## Export overwriting and create new

When you create an export, you can choose to either create new export files or overwrite
the existing export files with each refresh.

**Create new**

Creating new export files uses more S3 storage because all export refreshes are
kept. Overwriting the previous export files uses less S3 storage because only the
latest version of each billing period refresh is kept.

When in “create new” mode, the export files are delivered to the following S3
path:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/<timestamp>-<execution-id>`

The `timestamp` is the date and time when the export was executed. The
`execution-id` is the unique ID assigned to the execution.

For "create new", two `Manifest.json` files are delivered with each
export execution. One is stored in the
`metadata/<partition>/<timestamp>-<execution-id>` directory, and
the other is overwritten in the `metadata/<partition>` directory. The
manifest in the `metadata/<partition>` directory always represents the
most recent refresh and its data is used to identify the location of the most recently
refreshed export files.

**Overwrite**

Overwriting only applies for refreshes of the same partition (that is, billing
period). Once a new billing period begins, the export creates a new S3 directory with
a name based on the latest partition or billing period, and begins delivering the new
export partition there. The export of the previous partition is not overwritten unless
the data for that specific partition is updated.

When in “overwrite” mode, the export files are delivered to the following S3
path:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/`

The export files in this file directory are overwritten with each delivery of the
same partition (that is, billing period).

Export files are delivered as multiple “chunks” (separate gzip/csv or Parquet
files) when the export becomes sufficiently big. If the export ever decreases in size
during the month (due to a changed query or correction to data), fewer chunks may be
needed to deliver the export refresh. In this case, Data Exports overwrites any extra chunks
from the last refresh with empty data.

For overwriting, one `Manifest.json` file is delivered with each export
execution. It is stored in the `metadata/<partition>` directory and is
overwritten with each refresh.

## Export data file names and chunks

Exports either deliver the results of one execution as one file (gzip/csv or Parquet) or
in multiple “chunks” (separate gzip/csv or Parquet files) when the export becomes
sufficiently big.

Exports are named as follows for the gzip/csv file format:

`<export-name>-<chunk-number>.csv.gz`

Exports are named as follows for the Parquet format:

`<export-name>-<chunk-number>.snappy.parquet`

Chunk numbers always have five digits. Chunk numbers are enumerated starting at
`00001`.

## Summary

**Export data file names with directory for create
new**

Parquet:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/<timestamp>-<execution-id>/<export-name>-<chunk-number>.snappy.parquet`

gzip/csv:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/<timestamp>-<execution-id>/<export-name>-<chunk-number>.csv.gz`

**Export data file names with directory for
overwrite**

Parquet:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/<export-name>-<chunk-number>.snappy.parquet`

gzip/csv:

`s3://<bucket-name>/<prefix>/<export-name>/data/<partition>/<export-name>-<chunk-number>.csv.gz`

**Manifest file names with directory for create
new**

The “create new” mode delivers `Manifest.json` to two locations.

The first location is in a folder representing a specific execution of an export
(named by `timestamp` and `execution-id`). This Manifest
corresponds to that specific execution. The file path is as follows:

`s3://<bucket-name>/<prefix>/<export-name>/metadata/<partition>/<timestamp>-<execution-id>`

The second location is in a partition folder containing all executions. This
Manifest is the same file from the most recent execution of the export. You can read
this Manifest to identify the exact file paths of all recent export files. The file
path is as follows:

`s3://<bucket-name>/<prefix>/<export-name>/metadata/<partition>/Manifest.json`

**Manifest file names with directory for
overwrite**

The “overwrite” mode delivers `Manifest.json` to one location.

`s3://<bucket-name>/<prefix>/<export-name>/metadata/<partition>`

The Manifest in this directory is overwritten with each refresh of a given
partition (that is, billing period).
