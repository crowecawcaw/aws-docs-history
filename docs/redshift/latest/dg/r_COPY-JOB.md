Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# COPY JOB

For information about using this command, see
[Create an S3 event integration to automatically copy files from Amazon S3 buckets](loading-data-copy-job.md "loading-data-copy-job.md").

Manages COPY commands that
load data into a table. The COPY JOB command is an extension of the COPY command and automates
data loading from Amazon S3 buckets. When you create a COPY job, Amazon Redshift detects when new Amazon S3 files
are created in a specified path,
and then loads them automatically without your intervention. The same
parameters that are
used in the original COPY command are used when loading the data. Amazon Redshift keeps track of the
loaded files (based on filename) to verify that they
are loaded only one time.

###### Note

For information about the COPY command, including usage, parameters, and permissions, see
[COPY](r_COPY.md "r_COPY.md").

## Required permission

To use the COPY JOB command, you must have one of the following
permissions in addition to all of the required permissions to use COPY:

- Superuser
- All of the following:
  - The relevant CREATE, ALTER, or DROP scoped permission
    for COPY JOBS in the database you want to COPY to.
  - USAGE permission for the schema you want to COPY to,
    or USAGE scoped permission for schemas in the database
    you want to COPY to.
  - INSERT permission for the table you want to COPY to,
    or INSERT scoped permission for tables in the schema
    or database you want to COPY to.

The IAM role specified with the COPY command must have permission to access the data to load.
For more information, see [IAM permissions for COPY, UNLOAD,
and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions "copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions").

## Syntax

Create a copy job. The parameters of the COPY command are saved with the copy job.

You can't run COPY JOB CREATE within the scope of a transaction block.

```
COPY *copy-command* JOB CREATE *job-name*
[AUTO ON | OFF]

```

Change the configuration of a copy job.

```
COPY JOB ALTER *job-name*
[AUTO ON | OFF]

```

Run a copy job. The stored COPY command parameters are used.

```
COPY JOB RUN *job-name*

```

List all copy jobs.

```
COPY JOB LIST

```

Show the details of a copy job.

```
COPY JOB SHOW *job-name*

```

Delete a copy job.

You can't run COPY JOB DROP within the scope of a transaction block.

```
COPY JOB DROP *job-name*

```

## Parameters

_copy-command_

A COPY command that loads data from Amazon S3 to Amazon Redshift. The clause contains COPY parameters that define the
Amazon S3 bucket, target table, IAM role, and other parameters used when loading data.
All COPY command parameters for an Amazon S3 data load are supported except:

- The COPY JOB does not ingest preexisting files in the folder pointed to by the COPY command. Only files created after the COPY JOB creation timestamp are ingested.
- You cannot specify a COPY command with the MAXERROR or IGNOREALLERRORS options.
- You cannot specify a
  manifest file. COPY JOB requires a designated Amazon S3 location to monitor for newly
  created files.
- You cannot specify a COPY command with authorization types like Access and Secret keys. Only COPY commands that use the `IAM_ROLE` parameter for authorization are supported. For more information, see
  [Authorization parameters](copy-parameters-authorization.md "copy-parameters-authorization.md").
- The COPY JOB doesn't support the default IAM role associated with the cluster. You must specify the `IAM_ROLE` in the COPY command.

For more information, see
[COPY from Amazon S3](copy-parameters-data-source-s3.md "copy-parameters-data-source-s3.md").

_job-name_

The name of the job used to reference the COPY job.
The _job-name_ can't contain a hyphen (‐).

[AUTO ON | OFF]

Clause that indicates whether Amazon S3 data is automatically loaded into Amazon Redshift tables.

- When `ON`, Amazon Redshift monitors the source Amazon S3 path for newly created files, and if found, a
  COPY command is run with the COPY parameters in the job definition. This is the default.
- When `OFF`, Amazon Redshift does not run the COPY JOB automatically.

## Usage notes

The options of the COPY command aren't validated until run time. For example, an invalid `IAM_ROLE` or an Amazon S3 data source results in runtime errors when the COPY JOB starts.

If the cluster is paused, COPY JOBS are not run.

To query COPY command files loaded and load errors, see [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md"),
[STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md"),
[STL_LOADERROR_DETAIL](r_STL_LOADERROR_DETAIL.md "r_STL_LOADERROR_DETAIL.md").
For more information, see [Verifying that the data loaded
correctly](verifying-that-data-loaded-correctly.md "verifying-that-data-loaded-correctly.md").

## Examples

The following example shows creating a COPY JOB to load data from an Amazon S3 bucket.

```
COPY public.target_table
FROM 's3://amzn-s3-demo-bucket/staging-folder'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyLoadRoleName'
JOB CREATE my_copy_job_name
AUTO ON;

```
