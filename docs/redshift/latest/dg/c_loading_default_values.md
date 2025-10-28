Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading default column values

You can optionally define a column list in your COPY command. If a column in the
table is omitted from the column list, COPY will load the column with either the value
supplied by the DEFAULT option that was specified in the CREATE TABLE command, or with
NULL if the DEFAULT option was not specified.

If COPY attempts to assign NULL to a column that is defined as NOT NULL, the COPY
command fails. For information about assigning the DEFAULT option, see [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md").

When loading from data files on Amazon S3, the columns in the column list must be in the
same order as the fields in the data file. If a field in the data file does not have a
corresponding column in the column list, the COPY command fails.

When loading from Amazon DynamoDB table, order does not matter. Any fields in the Amazon DynamoDB
attributes that do not match a column in the Amazon Redshift table are discarded.

The following restrictions apply when using the COPY command to load DEFAULT values
into a table:

- If an [IDENTITY](r_CREATE_TABLE_NEW.md#identity-clause "r_CREATE_TABLE_NEW.md#identity-clause") column is included in the column list,
  the EXPLICIT_IDS option must also be specified in the [COPY](r_COPY.md "r_COPY.md") command, or the COPY command will fail. Similarly, if
  an IDENTITY column is omitted from the column list, and the EXPLICIT_IDS option is
  specified, the COPY operation will fail.
- Because the evaluated DEFAULT expression for a given column is the same for all
  loaded rows, a DEFAULT expression that uses a RANDOM() function will assign to
  same value to all the rows.
- DEFAULT expressions that contain CURRENT_DATE or SYSDATE are set to the
  timestamp of the current transaction.
  For an example, see "Load data from a file with default values" in [COPY examples](r_COPY_command_examples.md "r_COPY_command_examples.md").
