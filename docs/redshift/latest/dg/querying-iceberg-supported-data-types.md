Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
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

When you create and define an Iceberg table, use the Amazon Redshift data type names in the
SQL statement. Redshift automatically maps them to the corresponding Iceberg types. For
more information about Iceberg data types, see the [Schemas for Iceberg](https://iceberg.apache.org/docs/latest/schemas/ "https://iceberg.apache.org/docs/latest/schemas/") in
the Apache Iceberg documentation.

When reading from Iceberg tables, Iceberg data-types are mapped into Redshift
data-types as shown in the below table:

| Iceberg type     | Amazon Redshift type | Notes                                                                  |
| ---------------- | -------------------- | ---------------------------------------------------------------------- |
| `boolean`        | `boolean`            | -                                                                      |
| -                | `tinyint`            | Not supported for Iceberg tables.                                      |
| -                | `smallint`           | Not supported for Iceberg tables.                                      |
| `int`            | `int`                | -                                                                      |
| `long`           | `bigint`             | -                                                                      |
| `double`         | `double precision`   | -                                                                      |
| `float`          | `real`               | -                                                                      |
| `decimal(P, S)`  | `decimal(P, S)`      | `P` is precision, `S` is scale.                                        |
| -                | `char`               | Not supported for Iceberg tables.                                      |
| `string`         | `varchar(16384)`     | Strings larger than `16384` are truncated to<br>`16384`.               |
| `binary`         | `varbyte(64000)`     | -                                                                      |
| `date`           | `date`               | -                                                                      |
| `time`           | -                    | -                                                                      |
| `timestamp`      | `timestamp`          | -                                                                      |
| `timestamptz`    | `timestampz`         | -                                                                      |
| `list<E>`        | `SUPER`              | -                                                                      |
| `map<K,V>`       | `SUPER`              | -                                                                      |
| `struct<...>`    | `SUPER`              | -                                                                      |
| `fixed(L)`       | -                    | The `fixed(L)` type isn't currently supported in<br>Redshift Spectrum. |
| `uuid`           | -                    | The `uuid` type isn't currently supported in<br>Redshift Spectrum.     |
| `variant`        | -                    | Amazon Redshift doesn't support Iceberg V3.                            |
| `geometry`       | -                    | Amazon Redshift doesn't support Iceberg V3.                            |
| `geography`      | -                    | Amazon Redshift doesn't support Iceberg V3.                            |
| `timestamp_ns`   | -                    | Amazon Redshift doesn't support Iceberg V3.                            |
| `timestamptz_ns` | -                    | Amazon Redshift doesn't support Iceberg V3.                            |
| `Unknown`        | -                    | Amazon Redshift doesn't support Iceberg V3.                            |

The following data-types are supported when creating Iceberg tables from Redshift.
Redshift data-types are mapped into Iceberg data-types as shown in the following table.

| Amazon Redshift type | Amazon Redshift alias               | Iceberg type   | Notes                                                                       |
| -------------------- | ----------------------------------- | -------------- | --------------------------------------------------------------------------- |
| `integer`            | `int, int4`                         | `int`          | -                                                                           |
| `bigint`             | `int8`                              | `long`         | -                                                                           |
| `decimal`            | `numeric`                           | `decimal(p,S)` | -                                                                           |
| `real`               | `float4`                            | `float`        | -                                                                           |
| `double precision`   | `float8, float`                     | `double`       | -                                                                           |
| `varchar`            | `charactter varying,nvarchar, text` | `string`       | The `varchar(n)` data type is not supported when creating an Iceberg table. |
| `date`               | -                                   | `date`         | -                                                                           |
| `timestamp`          | -                                   | `timestamp`    | -                                                                           |
| `timestamptz`        | -                                   | `timestamptz`  | -                                                                           |
| `boolean`            | -                                   | `boolean`      | -                                                                           |

When writing to Iceberg tables, in addition to the data-types mentioned in the
previous table, some source-data types are type promoted to their compatible Iceberg
types as shown in the following table.

| Amazon Redshift type | Iceberg type |
| -------------------- | ------------ |
| `tinyint`            | `int`        |
| `smallint`           | `int`        |
| `varchar(n)`         | `string`     |

Attempting to use data types that are not supported will result in syntax errors. When you
create an Iceberg table with `CREATE TABLE AS SELECT` clause, you can add
explicit cast to work around the type difference.

For example, suppose you have a Redshift RMS table with the following schema:

```
CREATE TABLE rms_t (c1 int, c2 char(20));
```

If you want to create an Iceberg table using `rms_t` as the source, you need an
explicit cast for the `c2` column, because the `varchar(n)` type is
not supported:

```
CREATE TABLE ext_schema.iceberg_t AS SELECT c1, c2::varchar FROM rms_t;
```

For more information about data types in Amazon Redshift, see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").
