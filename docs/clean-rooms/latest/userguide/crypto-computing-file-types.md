# Supported file and data types in Cryptographic Computing for Clean Rooms

The C3R encryption client recognizes the following file types:

- CSV files
- Parquet files
  You can use the `--fileFormat` flag in the C3R encryption client to specify a file format
  explicitly. When explicitly specified, file format is not determined by file extension.

###### Topics

- [CSV files](#csv-file-type "#csv-file-type")
- [Parquet files](#parquet-file-type "#parquet-file-type")
- [Encrypting non-string values](#encrypt-non-string-values "#encrypt-non-string-values")

## CSV files

A file with a .csv extension is assumed to be CSV formatted and contain UTF-8 encoded
text. The C3R encryption client
treats all values as strings.

### Supported properties in .csv files

The C3R encryption client requires that .csv files have the following properties:

- Might or might not contain an initial header row that uniquely names each column.
- Comma-delimited. (Currently, custom delimiters are not supported.)
- UTF-8 encoded text.

#### White space trimming from .csv entries

Both leading and trailing white space is trimmed from .csv entries.

#### Custom NULL encoding for a .csv

file

A .csv file can use custom NULL encoding.

With the C3R encryption client, you can specify custom encodings for NULL entries
in the input data by using the `--csvInputNULLValue=<csv-input-null>` flag. The
C3R encryption client can use custom encodings in the generated output file for NULL entries by using
the `--csvOutputNULLValue=<csv-output-null>` flag.

###### Note

A NULL entry is considered to be _lacking_ content, specifically in the context of a richer tabular format like an
SQL table. Although .csv doesn't explicitly support this characterization for historical
reasons, it's a common convention to consider an empty entry that contains only white space to
be NULL. Therefore, that's the default behavior of the C3R encryption client and it
can be customized as needed.

### How .csv entries are interpreted by

C3R

The following table provides examples of how .csv entries are marshalled
(cleartext to cleartext for clarity) based on the values (if any)
that are provided for the `--csvInputNULLValue=<csv-input-null>` and
`--csvOutputNULLValue=<csv-output-null>` flags. Leading and trailing white
space outside of quotes is trimmed before C3R interprets any value's meaning.

| `<csv-input-null>` | `<csv-output-null>` | Input entry        | Output entry   |
| ------------------ | ------------------- | ------------------ | -------------- |
| None               | None                | `,AnyProduct,`     | `,AnyProduct,` |
| None               | None                | `, AnyProduct ,`   | `,AnyProduct,` |
| None               | None                | `,"AnyProduct",`   | `,AnyProduct,` |
| None               | None                | `, "AnyProduct" ,` | `,AnyProduct,` |
| None               | None                | `,,`               | `,,`           |
| None               | None                | `, ,`              | `,,`           |
| None               | None                | `,"",`             | `,,`           |
| None               | None                | `," ",`            | `," ",`        |
| None               | None                | `, " " ,`          | `," ",`        |
| `"AnyProduct"`     | `"NULL"`            | `,AnyProduct,`     | `,NULL,`       |
| `"AnyProduct"`     | `"NULL"`            | `, AnyProduct ,`   | `,NULL,`       |
| `"AnyProduct"`     | `"NULL"`            | `,"AnyProduct",`   | `,NULL,`       |
| `"AnyProduct"`     | `"NULL"`            | `, "AnyProduct" ,` | `,NULL,`       |
| None               | `"NULL"`            | `,,`               | `,NULL,`       |
| None               | `"NULL"`            | `, ,`              | `,NULL,`       |
| None               | `"NULL"`            | `,"",`             | `,NULL,`       |
| None               | `"NULL"`            | `," ",`            | `," ",`        |
| None               | `"NULL"`            | `, " " ,`          | `," ",`        |
| `""`               | `"NULL"`            | `,,`               | `,NULL,`       |
| `""`               | `"NULL"`            | `, ,`              | `,NULL,`       |
| `""`               | `"NULL"`            | `,"",`             | `,"",`         |
| `""`               | `"NULL"`            | `," ",`            | `," ",`        |
| `""`               | `"NULL"`            | `, " " ,`          | `," ",`        |
| `"\"\""`           | `"NULL"`            | `,,`               | `,,`           |
| `"\"\""`           | `"NULL"`            | `, ,`              | `,,`           |
| `"\"\""`           | `"NULL"`            | `,"",`             | `,NULL,`       |
| `"\"\""`           | `"NULL"`            | `," ",`            | `," ",`        |
| `"\"\""`           | `"NULL"`            | `, " " ,`          | `," ",`        |

### CSV file without headers

The source .csv file doesn't need to have headers in the first row that uniquely name each
column. However, a .csv file without a header row requires a positional encryption schema. The
positional encryption schema is required instead of the typical mapped schema that's used for
both .csv files with a header row and Parquet files.

A positional encryption schema specifies output columns by position instead of by name. A
mapped encryption schema maps source column names to target column names. For more information,
including a detailed discussion and examples of both schema formats, see [Mapped and positional table schemas](create-schema.md#mapped-and-positional-schemas "create-schema.md#mapped-and-positional-schemas").

## Parquet files

A
file with a .parquet extension is assumed to be in the
Apache Parquet format.

### Supported Parquet data

types

The C3R encryption client can process any non-complex (that is, primitive type) data in a
Parquet
file that represents a
data type supported by AWS Clean Rooms.

However, only string columns can be used for sealed
columns.

The following Parquet data types are supported:

- `Binary` primitive type with the following logical annotations:
  - None if the `--parquetBinaryAsString` is set (`STRING` data
    type)
  - `Decimal(scale, precision)` (`DECIMAL` data type)
  - `String` (`STRING` data type)

- `Boolean` primitive data type with no logical annotation (`BOOLEAN`
  data type)
- `Double` primitive data type with no logical annotation (`DOUBLE`
  data type)
- `Fixed_Len_Binary_Array` primitive type with the `Decimal(scale,
precision)` logical annotation (`DECIMAL` data type)
- `Float` primitive data type with no logical annotation (`FLOAT`
  data type)
- `Int32` primitive type with the following logical annotations:
  - None (`INT` data type)
  - `Date` (`DATE` data type)
  - `Decimal(scale, precision)` (`DECIMAL` data type)
  - `Int(16, true)` (`SMALLINT` data type)
  - `Int(32, true)` (`INT` data type)

- `Int64` primitive data type with the following logical annotations:
  - None (`BIGINT` data type)
  - `Decimal(scale, precision)` (`DECIMAL` data type)
  - `Int(64, true)` (`BIGINT` data type)
  - `Timestamp(isUTCAdjusted, TimeUnit.MILLIS)` (`TIMESTAMP` data
    type)
  - `Timestamp(isUTCAdjusted, TimeUnit.MICROS)` (`TIMESTAMP` data
    type)
  - `Timestamp(isUTCAdjusted, TimeUnit.NANOS)` (`TIMESTAMP` data
    type)

## Encrypting non-string values

Currently, only string values are supported for sealed
columns.

For .csv files, the C3R encryption client treats all values as UTF-8 encoded text and makes no
attempt to interpret them differently before encryption.

For fingerprint columns, types are grouped into equivalence classes. An equivalence class is
a set of data types that can be unambiguously compared for equality via a representative data
type.

Equivalence classes allow identical fingerprints to be assigned to the same semantic value
regardless of the original representation. However, the same value in two equivalence classes
will not result in the same fingerprint column.

For example, the `INTEGRAL` value `42` will be assigned the same
fingerprint regardless of whether it was originally an `SMALLINT`, `INT`,
or `BIGINT`. Also, the `INTEGRAL` value `0` will never match the
`BOOLEAN` value `FALSE` (which is represented by the value
`0`).

The following equivalence classes and corresponding AWS Clean Rooms data types are supported by
fingerprint columns:

| Equivalence<br>class | Supported AWS Clean Rooms<br>data type |
| -------------------- | -------------------------------------- |
| `BOOLEAN`            | `BOOLEAN`                              |
| `DATE`               | `DATE`                                 |
| `INTEGRAL`           | `BIGINT`, `INT`, `SMALLINT`            |
| `STRING`             | `CHAR`, `STRING`, `VARCHAR`            |
