# neptune.read()

Neptune supports a `CALL` procedure `neptune.read` to read data from Amazon S3 and then run an openCypher
query (read, insert, update) using the data. The procedure yields each row in the file as a declared result variable row. It
uses the IAM credentials of the caller to access the data in Amazon S3. See [Create your IAM role for Amazon S3 access](bulk-import-create-from-s3.md#create-iam-role-for-s3-access "bulk-import-create-from-s3.md#create-iam-role-for-s3-access") to set up the permissions. The AWS region of the Amazon S3 bucket must be in
the same region where Neptune Analytics instance is located. Currently, cross-region reads are not supported.

**Syntax**

```
CALL neptune.read(
  {
    source: "string",
    format: "parquet/csv",
    concurrency: 10
  }
)
YIELD row
...
```

###### Inputs

- **source** (required) - Amazon S3 URI to a **single** object.
  Amazon S3 prefix to multiple objects is not supported.
- **format** (required) - `parquet` and `csv` are supported.
  - More details on the supported Parquet format can be found in
    [Supported Parquet column types](parquet-column-types.md "parquet-column-types.md").
  - For more information on the supported csv format, see [Gremlin load data format](../../../neptune/latest/userguide/bulk-load-tutorial-format-gremlin.md "../../../neptune/latest/userguide/bulk-load-tutorial-format-gremlin.md").

- **concurrency** (optional) - Type: 0 or greater integer. Default: 0. Specifies the number of
  threads to be used for reading the file. If the value is 0, the maximum number of threads allowed by the resource will be used.
  For Parquet, it is recommended to be set to a number of row groups.

###### Outputs

The neptune.read returns:

- **row** - type:Map
  - Each row in the file, where the keys are the columns and the values are the data found in each column.
  - You can access each column's data like a property access (`row.col`).
