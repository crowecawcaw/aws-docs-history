Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Supported data types with Apache Iceberg tables

This topic describes the supported data types that Redshift Spectrum can read from tables in Apache Iceberg format.

Amazon Redshift can query Iceberg tables that contain the following data types:

```
binary
boolean
date
decimal
double
float
int
list
long
map
string
struct
timestamp without time zone
```

For more information about Iceberg data types, see the [Schemas for
Iceberg](https://iceberg.apache.org/docs/latest/schemas/ "https://iceberg.apache.org/docs/latest/schemas/") in the Apache Iceberg documentation.

The following table shows the relationship between Amazon Redshift data types and Iceberg table
data types.

| Iceberg type     | Amazon Redshift type | Notes                                                               |
| ---------------- | -------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `boolean`        | `boolean`            |                                                                     |
| -                | `tinyint`            | Not supported for Iceberg tables.                                   |
| -                | `smallint`           |                                                                     |
| `int`            | `int`                |                                                                     |
| `long`           | `bigint`             |                                                                     |
| `double`         | `double precision`   |                                                                     |
| `float`          | `real`               |                                                                     |
| `decimal(P, S)`  | `decimal(P, S)`      | `P` is precision, `S` is scale.                                     |
| -                | `char`               |                                                                     |
| `string`         | `varchar(16384)`     | Strings larger than `16384` are truncated to `16384`.               |
| `binary`         | `varbyte(64000)`     |                                                                     |
| `date`           | `date`               |                                                                     |
| `time`           | -                    |                                                                     |
| `timestamp`      | `timestamp`          |                                                                     |
| `timestamptz`    | `timestamp`          |                                                                     |
| `list<E>`        | `SUPER`              |                                                                     |
| `map<K,V>`       | `SUPER`              |                                                                     |
| `struct<...>`    | `SUPER`              |                                                                     |
| `fixed(L)`       | -                    | The `fixed(L)` type isn't currently supported in Redshift Spectrum. |
| `uuid`           | -                    | The `uuid` type isn't currently supported in Redshift Spectrum.     |
| `variant`        | -                    | Amazon Redshift doesn't support Iceberg V3.                         |
| `geometry`       | -                    | Amazon Redshift doesn't support Iceberg V3.                         |
| `geography`      | -                    | Amazon Redshift doesn't support Iceberg V3.                         |
| `timestamp_ns`   | -                    | Amazon Redshift doesn't support Iceberg V3.                         |
| `timestamptz_ns` | -                    | Amazon Redshift doesn't support Iceberg V3.                         |
| `Unknown`        | -                    | Amazon Redshift doesn't support Iceberg V3.                         | For more information about data types in Amazon Redshift, see [Data types](c_Supported_data_types.md "c_Supported_data_types.md"). |
