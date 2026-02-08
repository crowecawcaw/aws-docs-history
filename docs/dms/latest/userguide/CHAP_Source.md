# Using Amazon S3 as a source for AWS DMS

You can migrate data from an Amazon S3 bucket using AWS DMS. To do this, provide access to an
Amazon S3 bucket containing one or more data files. In that S3 bucket, include a JSON file
that describes the mapping between the data and the database tables of the data in those
files.

The source data files must be present in the Amazon S3 bucket before the full load starts.
You specify the bucket name using the `bucketName` parameter.

The source data files can be in the following formats:

- Comma-separated value (.csv)
- Parquet (DMS version 3.5.3 and later). For information about using Parquet-format files,
  see [Using Parquet-format files in Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.Parquet "#CHAP_Source.S3.Parquet").
  For source data files in comma-separated value (.csv) format, name them using
  the following naming convention. In this convention,
  `schemaName` is the source schema and
  `tableName` is the name of a table within
  that schema.

```
/`schemaName`/`tableName`/LOAD001.csv
/`schemaName`/`tableName`/LOAD002.csv
/`schemaName`/`tableName`/LOAD003.csv
...
```

For example, suppose that your data files are in `amzn-s3-demo-bucket`, at the
following Amazon S3 path.

```
s3://amzn-s3-demo-bucket/hr/employee
```

At load time, AWS DMS assumes that the source schema name is `hr`, and that
the source table name is `employee`.

In addition to `bucketName` (which is required), you can optionally provide
a `bucketFolder` parameter to specify where AWS DMS should look for data files
in the Amazon S3 bucket. Continuing the previous example, if you set
`bucketFolder` to `sourcedata`, then AWS DMS reads the data
files at the following path.

```
s3://amzn-s3-demo-bucket/sourcedata/hr/employee
```

You can specify the column delimiter, row delimiter, null value indicator, and other
parameters using extra connection attributes. For more information, see [Endpoint settings for Amazon S3 as
a source for AWS DMS](#CHAP_Source.S3.Configuring "#CHAP_Source.S3.Configuring").

You can specify a bucket owner and prevent sniping by using the
`ExpectedBucketOwner` Amazon S3 endpoint setting, as shown following. Then, when you
make a request to test a connection or perform a migration, S3 checks the account
ID of the bucket owner against the specified parameter.

```
--s3-settings='{"ExpectedBucketOwner": "*AWS\_Account\_ID*"}'
```

###### Topics

- [Defining external tables for Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.ExternalTableDef "#CHAP_Source.S3.ExternalTableDef")
- [Using CDC with Amazon S3 as a source for
  AWS DMS](#CHAP_Source.S3.CDC "#CHAP_Source.S3.CDC")
- [Prerequisites when using Amazon S3 as a
  source for AWS DMS](#CHAP_Source.S3.Prerequisites "#CHAP_Source.S3.Prerequisites")
- [Limitations when using Amazon S3 as
  a source for AWS DMS](#CHAP_Source.S3.Limitations "#CHAP_Source.S3.Limitations")
- [Endpoint settings for Amazon S3 as
  a source for AWS DMS](#CHAP_Source.S3.Configuring "#CHAP_Source.S3.Configuring")
- [Source data types for Amazon S3](#CHAP_Source.S3.DataTypes "#CHAP_Source.S3.DataTypes")
- [Using Parquet-format files in Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.Parquet "#CHAP_Source.S3.Parquet")

## Defining external tables for Amazon S3

as a source for AWS DMS

In addition to the data files, you must also provide an external table definition.
An _external table definition_ is a JSON document that describes
how AWS DMS should interpret the data from Amazon S3. The maximum size of this document is
2 MB. If you create a source endpoint using the AWS DMS Management Console, you can
enter the JSON directly into the table-mapping box. If you use the AWS Command Line Interface (AWS CLI)
or AWS DMS API to perform migrations, you can create a JSON file to specify the
external table definition.

Suppose that you have a data file that includes the following.

```
101,Smith,Bob,2014-06-04,New York
102,Smith,Bob,2015-10-08,Los Angeles
103,Smith,Bob,2017-03-13,Dallas
104,Smith,Bob,2017-03-13,Dallas
```

Following is an example external table definition for this data.

```
{
    "TableCount": "1",
    "Tables": [
        {
            "TableName": "employee",
            "TablePath": "hr/employee/",
            "TableOwner": "hr",
            "TableColumns": [
                {
                    "ColumnName": "Id",
                    "ColumnType": "INT8",
                    "ColumnNullable": "false",
                    "ColumnIsPk": "true"
                },
                {
                    "ColumnName": "LastName",
                    "ColumnType": "STRING",
                    "ColumnLength": "20"
                },
                {
                    "ColumnName": "FirstName",
                    "ColumnType": "STRING",
                    "ColumnLength": "30"
                },
                {
                    "ColumnName": "HireDate",
                    "ColumnType": "DATETIME"
                },
                {
                    "ColumnName": "OfficeLocation",
                    "ColumnType": "STRING",
                    "ColumnLength": "20"
                }
            ],
            "TableColumnsTotal": "5"
        }
    ]
}
```

The elements in this JSON document are as follows:

`TableCount` – the number of source tables. In this example,
there is only one table.

`Tables` – an array consisting of one JSON map per source table.
In this example, there is only one map. Each map consists of the following
elements:

- `TableName` – the name of the source table.
- `TablePath` – the path in your Amazon S3 bucket where AWS DMS
  can find the full data load file. If a `bucketFolder` value is
  specified, its value is prepended to the path.
- `TableOwner` – the schema name for this table.
- `TableColumns` – an array of one or more maps, each of
  which describes a column in the source table:
  - `ColumnName` – the name of a column in the
    source table.
  - `ColumnType` – the data type for the column. For
    valid data types, see [Source data types for Amazon S3](#CHAP_Source.S3.DataTypes "#CHAP_Source.S3.DataTypes").
  - `ColumnLength` – the number of bytes in this
    column. Maximum column length is limited to2147483647 Bytes (2,047
    MegaBytes) since an S3 source doesn't support FULL LOB

  mode. `ColumnLength` is valid for the following data types:

      - BYTE
      - STRING

  - `ColumnNullable` – a Boolean value that is
    `true` if this column can contain NULL values
    (default=`false`).
  - `ColumnIsPk` – a Boolean value that is
    `true` if this column is part of the primary key
    (default=`false`).
  - `ColumnDateFormat` – the input date format for a column with
    DATE, TIME, and DATETIME types, and used to parse a data string into a date object.
    Possible values include:

  ```
  - YYYY-MM-dd HH:mm:ss
  - YYYY-MM-dd HH:mm:ss.F
  - YYYY/MM/dd HH:mm:ss
  - YYYY/MM/dd HH:mm:ss.F
  - MM/dd/YYYY HH:mm:ss
  - MM/dd/YYYY HH:mm:ss.F
  - YYYYMMdd HH:mm:ss
  - YYYYMMdd HH:mm:ss.F
  ```

- `TableColumnsTotal` – the total number of columns. This
  number must match the number of elements in the `TableColumns`
  array.

If you don't specify otherwise, AWS DMS assumes that `ColumnLength`
is zero.

###### Note

In supported versions of AWS DMS, the S3 source data can also contain an
optional operation column as the first column before the `TableName`
column value. This operation column identifies the operation
(`INSERT`) used to migrate the data to an S3 target endpoint
during a full load.

If present, the value of this column is the initial character of the
`INSERT` operation keyword (`I`). If specified, this
column generally indicates that the S3 source was created by DMS as an S3 target
during a previous migration.

In DMS versions prior to 3.4.2, this column wasn't present in S3 source data
created from a previous DMS full load. Adding this column to S3 target data
allows the format of all rows written to the S3 target to be consistent whether
they are written during a full load or during a CDC load. For more information
on the options for formatting S3 target data, see [Indicating source DB
operations in migrated S3 data](CHAP_Target.md#CHAP_Target.S3.Configuring.InsertOps "CHAP_Target.md#CHAP_Target.S3.Configuring.InsertOps").

For a column of the NUMERIC type, specify the precision and scale.
_Precision_ is the total number of digits in a number, and
_scale_ is the number of digits to the right of the decimal
point. You use the `ColumnPrecision` and `ColumnScale`
elements for this, as shown following.

```
...
    {
        "ColumnName": "HourlyRate",
        "ColumnType": "NUMERIC",
        "ColumnPrecision": "5"
        "ColumnScale": "2"
    }
...
```

For a column of the DATETIME type with data that contains fractional seconds,
specify the scale. _Scale_ is the number of digits for the
fractional seconds, and can range from 0 to 9. You use the `ColumnScale`
element for this, as shown following.

```
...
{
      "ColumnName": "HireDate",
      "ColumnType": "DATETIME",
      "ColumnScale": "3"
}
...
```

If you don't specify otherwise, AWS DMS assumes `ColumnScale` is zero and
truncates the fractional seconds.

## Using CDC with Amazon S3 as a source for

AWS DMS

After AWS DMS performs a full data load, it can optionally replicate data changes to
the target endpoint. To do this, you upload change data capture files (CDC files) to
your Amazon S3 bucket. AWS DMS reads these CDC files when you upload them, and then applies
the changes at the target endpoint.

The CDC files are named as follows:

```
CDC00001.csv
CDC00002.csv
CDC00003.csv
...
```

###### Note

To replicate CDC files in the change data folder successfully upload them in a
lexical (sequential) order. For example, upload the file CDC00002.csv before the
file CDC00003.csv. Otherwise, CDC00002.csv is skipped and isn't replicated
if you load it after CDC00003.csv. But the file CDC00004.csv replicates
successfully if loaded after CDC00003.csv.

To indicate where AWS DMS can find the files, specify the
`cdcPath` parameter. Continuing the previous example, if you set
`cdcPath` to `changedata`, then
AWS DMS reads the CDC files at the following path.

```
s3://`amzn-s3-demo-bucket`/`changedata`
```

If you set
`cdcPath` to `changedata` and `bucketFolder`
to `myFolder`, then
AWS DMS reads the CDC files at the following path.

```
s3://`amzn-s3-demo-bucket`/`myFolder`/`changedata`
```

The records in a CDC file are formatted as follows:

- Operation – the change operation to be performed:
  `INSERT` or `I`, `UPDATE` or
  `U`, or `DELETE` or `D`. These keyword
  and character values are case-insensitive.

###### Note

In supported AWS DMS versions, AWS DMS can identify the operation to
perform for each load record in two ways. AWS DMS can do this from the
record's keyword value (for example, `INSERT`) or from
its keyword initial character (for example, `I`). In prior
versions, AWS DMS recognized the load operation only from the full keyword
value.

In prior versions of AWS DMS, the full keyword value was written to log
the CDC data. Also, prior versions wrote the operation value to any S3
target using only the keyword initial.

Recognizing both formats allows AWS DMS to handle the operation
regardless of how the operation column is written to create the S3
source data. This approach supports using S3 target data as the source
for a later migration. With this approach, you don't need to change
the format of any keyword initial value that appears in the operation
column of the later S3 source.

- Table name – the name of the source table.
- Schema name – the name of the source schema.
- Data – one or more columns that represent the data to be
  changed.

Following is an example CDC file for a table named `employee`.

```
INSERT,employee,hr,101,Smith,Bob,2014-06-04,New York
UPDATE,employee,hr,101,Smith,Bob,2015-10-08,Los Angeles
UPDATE,employee,hr,101,Smith,Bob,2017-03-13,Dallas
DELETE,employee,hr,101,Smith,Bob,2017-03-13,Dallas
```

## Prerequisites when using Amazon S3 as a

source for AWS DMS

To use Amazon S3 as a source for AWS DMS, your source S3 bucket must be in the same AWS
Region as the DMS replication instance that migrates your data. In addition, the
AWS account you use for the migration must have read access to the source bucket.
For AWS DMS version 3.4.7 and higher, DMS must access the source bucket through a VPC endpoint or a public route. For
information about VPC endpoints, see [Configuring VPC endpoints for AWS DMS](CHAP_VPC_Endpoints.md "CHAP_VPC_Endpoints.md").

The AWS Identity and Access Management (IAM) role assigned to the user account used to create the migration
task must have the following set of permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket*/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket*"
 ]
 }
 ]
}`

```

The AWS Identity and Access Management (IAM) role assigned to the user account used to create the migration
task must have the following set of permissions if versioning is enabled on the Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket*/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket*"
 ]
 }
 ]
}`

```

## Limitations when using Amazon S3 as

a source for AWS DMS

The following limitations apply when using Amazon S3 as a source:

- Don’t enable versioning for S3. If you need S3 versioning, use lifecycle policies to actively
  delete old versions. Otherwise, you might encounter endpoint test connection failures because of
  an S3 `list-object` call timeout. To create a lifecycle policy for an S3 bucket, see
  [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").
  To delete a version of an S3 object, see
  [Deleting object versions from a versioning-enabled bucket](../../../AmazonS3/latest/dev/DeletingObjectVersions.md "../../../AmazonS3/latest/dev/DeletingObjectVersions.md").
- A VPC-enabled (gateway VPC) S3 bucket is supported in versions 3.4.7 and higher.
- MySQL converts the `time` datatype to `string`. To see `time`
  data type values in MySQL, define the column in the target table as `string`, and set the task's
  **Target table preparation mode** setting to **Truncate**.
- AWS DMS uses the `BYTE` data type internally for data in both `BYTE` and
  `BYTES` data types.
- S3 source endpoints do not support the DMS table reload feature.
- AWS DMS doesn't support Full LOB mode with Amazon S3 as a Source.

The following limitations apply when using Parquet-format files in Amazon S3 as a source:

- Dates in `MMYYYYDD`, or `DDMMYYYY` are not supported for the S3 Parquet Source date-partitioning feature.

## Endpoint settings for Amazon S3 as

a source for AWS DMS

You can use endpoint settings to configure your Amazon S3 source database similar to using
extra connection attributes. You specify the settings when you create the source
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--s3-settings '{"`EndpointSetting"`:
 `"value"`, `...`}'` JSON syntax.

###### Note

AWS DMS defaults to a secure connection to the Amazon S3 endpoint without requiring to
specify SSL mode or certificate.

The following table shows the endpoint settings that you can use with
Amazon S3 as a source.

| **Option**         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BucketFolder`     | (Optional) A folder name in the S3 bucket. If this attribute<br>is provided, source data files and CDC files are read from the<br>path<br>`s3://`amzn-s3-demo-bucket`/`bucketFolder`/`schemaName`/`tableName`/`<br>and<br>`s3://`amzn-s3-demo-bucket`/`bucketFolder`/` respectively.<br>If this attribute isn't specified, then the path used is<br>``schemaName`/`tableName`/`.<br>`'{"BucketFolder": "`sourceData`"}'`                                                                                                                                            |
| `BucketName`       | The name of the S3 bucket.<br>`'{"BucketName": "`amzn-s3-demo-bucket`"}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `CdcPath`          | The location of CDC files. This attribute is required if a task<br>captures change data; otherwise, it's optional. If<br>`CdcPath` is present, then AWS DMS reads CDC files from<br>this path and replicates the data changes to the target endpoint.<br>For more information, see [Using CDC with Amazon S3 as a source for<br>AWS DMS](#CHAP_Source.S3.CDC "#CHAP_Source.S3.CDC").<br>`'{"CdcPath": "`changeData`"}'`                                                                                                                                             |
| `CsvDelimiter`     | The delimiter used to separate columns in the source files.<br>The default is a comma. An example follows.<br>`'{"CsvDelimiter": ","}'`                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `CsvNullValue`     | A user-defined string that AWS DMS treats as null when reading from the source.<br>The default is an empty string. If you do not set this parameter, AWS DMS treats<br>an empty string as a null value. If you set this parameter to a string<br>such as "\N", AWS DMS treats this string as the null value, and treats empty strings<br>as an empty string value.                                                                                                                                                                                                  |
| `CsvRowDelimiter`  | The delimiter used to separate rows in the source files. The<br>default is a newline (`\n`).<br>`'{"CsvRowDelimiter": "\n"}'`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `DataFormat`       | Set this value to `Parquet` to read data in Parquet format.<br>`'{"DataFormat": "Parquet"}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `IgnoreHeaderRows` | When this value is set to 1, AWS DMS ignores the first row<br>header in a .csv file. A value of 1 enables the feature, a value<br>of 0 disables the feature.<br>The default is 0.<br>`'{"IgnoreHeaderRows": 1}'`                                                                                                                                                                                                                                                                                                                                                    |
| `Rfc4180`          | When this value is set to `true` or `y`,<br>each leading double quotation mark has to be followed by an<br>ending double quotation mark. This formatting complies with RFC<br>4180. When this value is set to `false` or<br>`n`, string literals are copied to the target as<br>is. In this case, a delimiter (row or column) signals the end of<br>the field. Thus, you can't use a delimiter as part of the<br>string, because it signals the end of the value.<br>The default is `true`.<br>Valid values: `true`, `false`,<br>`y`, `n`<br>`'{"Rfc4180": false}'` |

## Source data types for Amazon S3

Data migration that uses Amazon S3 as a source for AWS DMS needs to map data from Amazon S3 to
AWS DMS data types. For more information, see [Defining external tables for Amazon S3
as a source for AWS DMS](#CHAP_Source.S3.ExternalTableDef "#CHAP_Source.S3.ExternalTableDef").

For information on how to view the data type that is mapped in the target, see the
section for the target endpoint you are using.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.md "CHAP_Reference.md").

The following AWS DMS data types are used with Amazon S3 as a source:

- BYTE – Requires `ColumnLength`. For more information,
  see [Defining external tables for Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.ExternalTableDef "#CHAP_Source.S3.ExternalTableDef").
- DATE
- TIME
- DATETIME – For more information and an example, see the DATETIME
  type example in [Defining external tables for Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.ExternalTableDef "#CHAP_Source.S3.ExternalTableDef").
- INT1
- INT2
- INT4
- INT8
- NUMERIC – Requires `ColumnPrecision` and
  `ColumnScale`. AWS DMS supports the following maximum values:

      + **ColumnPrecision: 38**
      + **ColumnScale: 31**

  For more information and an example, see the
  NUMERIC type example in [Defining external tables for Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.ExternalTableDef "#CHAP_Source.S3.ExternalTableDef").

- REAL4
- REAL8
- STRING – Requires `ColumnLength`. For more information,
  see [Defining external tables for Amazon S3
  as a source for AWS DMS](#CHAP_Source.S3.ExternalTableDef "#CHAP_Source.S3.ExternalTableDef").
- UINT1
- UINT2
- UINT4
- UINT8
- BLOB
- CLOB
- BOOLEAN

## Using Parquet-format files in Amazon S3

as a source for AWS DMS

In AWS DMS version 3.5.3 and later, you can use Parquet-format files in an S3 bucket as a source for
both Full-Load or CDC replication.

DMS only supports Parquet format files as a source that DMS generates by migrating data to an S3 target endpoint.
File names must be in the supported format, or DMS won't include them in the migration.

For source data files in Parquet format, they must be in the following folder and naming convention.

```
schema/table1/LOAD00001.parquet
schema/table2/LOAD00002.parquet
schema/table2/LOAD00003.parquet
```

For source data files for CDC data in Parquet format, name and store them using the following folder
and naming convention.

```
schema/table/20230405-094615814.parquet
schema/table/20230405-094615853.parquet
schema/table/20230405-094615922.parquet
```

To access files in Parquet format, set the following endpoint settings:

- Set `DataFormat` to `Parquet`.
- Do not set the `cdcPath` setting. Make sure that you create your Parquet-format
  files in the specified schema/ table folders.

For
more information about settings for S3 endpoints, see
[S3Settings](../APIReference/API_S3Settings.md "../APIReference/API_S3Settings.md") in the
_AWS Database Migration Service API Reference_.

### Supported datatypes for Parquet-format files

AWS DMS supports the following source and target data types when migrating data from Parquet-format files.
Ensure that your target table has columns of the correct data types before migrating.

| Source data type | Target data type |
| ---------------- | ---------------- |
| `BYTE`           | `BINARY`         |
| `DATE`           | `DATE32`         |
| `TIME`           | `TIME32`         |
| `DATETIME`       | `TIMESTAMP`      |
| `INT1`           | `INT8`           |
| `INT2`           | `INT16`          |
| `INT4`           | `INT32`          |
| `INT8`           | `INT64`          |
| `NUMERIC`        | `DECIMAL`        |
| `REAL4`          | `FLOAT`          |
| `REAL8`          | `DOUBLE`         |
| `STRING`         | `STRING`         |
| `UINT1`          | `UINT8`          |
| `UINT2`          | `UINT16`         |
| `UINT4`          | `UINT32`         |
| `UINT8`          | `UINT`           |
| `WSTRING`        | `STRING`         |
| `BLOB`           | `BINARY`         |
| `NCLOB`          | `STRING`         |
| `CLOB`           | `STRING`         |
| `BOOLEAN`        | `BOOL`           |
