# Schema for reporting the location of sensitive

data

Amazon Macie uses standardized JSON structures to store information about where it finds
sensitive data in Amazon Simple Storage Service (Amazon S3) objects. The structures are used by sensitive data
findings and sensitive data discovery results. For sensitive data findings, the structures are part of the JSON
schema for findings. To review the complete JSON schema for findings, see [Findings](../APIReference/findings-describe.md "../APIReference/findings-describe.md") in the _Amazon Macie API Reference_. To
learn more about sensitive data discovery results, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

###### Topics

- [Schema overview](#findings-locate-sd-schema-overview "#findings-locate-sd-schema-overview")
- [Schema details and examples](#findings-locate-sd-schema-examples "#findings-locate-sd-schema-examples")

## Schema overview

To report the location of sensitive data that Amazon Macie found in an affected S3 object, the
JSON schema for sensitive data findings and sensitive data discovery results includes one
`customDataIdentifiers` object and one `sensitiveData` object.
The `customDataIdentifiers` object provides details about data that Macie
detected using [custom data identifiers](custom-data-identifiers.md "custom-data-identifiers.md").
The `sensitiveData` object provides details about data that Macie detected
using [managed data identifiers](managed-data-identifiers.md "managed-data-identifiers.md").

Each `customDataIdentifiers` and `sensitiveData` object contains one
or more `detections` arrays:

- In a `customDataIdentifiers` object, the `detections` array
  indicates which custom data identifiers detected the data and produced the finding.
  For each custom data identifier, the array also indicates the number of occurrences
  of the data that the identifier detected. It can also indicate the location of the
  data that the identifier detected.
- In a `sensitiveData` object, a `detections` array indicates
  the types of sensitive data that Macie detected using managed data identifiers. For
  each type of sensitive data, the array also indicates the number of occurrences of
  the data, and it can indicate the location of the data.

For a sensitive data finding, a `detections` array can include 1–15
`occurrences` objects. Each `occurrences` object specifies
where Macie detected individual occurrences of a specific type of sensitive data.

For example, the following `detections` array indicates the location of three
occurrences of sensitive data (US Social Security numbers) that Macie found in a CSV
file.

```
"sensitiveData": [
     {
       "category": "PERSONAL_INFORMATION",
       "detections": [
          {
             "count": 30,
             "occurrences": {
                "cells": [
                   {
                      "cellReference": null,
                      "column": 1,
                      "columnName": "SSN",
                      "row": 2
                   },
                   {
                      "cellReference": null,
                      "column": 1,
                      "columnName": "SSN",
                      "row": 3
                   },
                   {
                      "cellReference": null,
                      "column": 1,
                      "columnName": "SSN",
                      "row": 4
                   }
                ]
             },
             "type": "USA_SOCIAL_SECURITY_NUMBER"
           }
```

The location and number of `occurrences` objects in a `detections`
array varies based on the categories, types, and number of occurrences of sensitive data
that Macie detects during an automated sensitive data discovery analysis cycle or a run of a sensitive data
discovery job. For each analysis cycle or job run, Macie uses a _depth-first search_ algorithm to populate the resulting findings with
location data for 1–15 occurrences of sensitive data that Macie detects in S3
objects. These occurrences are indicative of the categories and types of sensitive data
that an affected S3 bucket and object might contain.

An `occurrences` object can contain any the following structures, depending on an
affected S3 object's file type or storage format:

- `cells` array – This array applies to Microsoft Excel workbooks, CSV
  files, and TSV files. An object in this array specifies a cell or field that Macie
  detected an occurrence of sensitive data in.
- `lineRanges` array – This array applies to email message (EML) files, and
  non-binary text files other than CSV, JSON, JSON Lines, and TSV files—for
  example, HTML, TXT, and XML files. An object in this array specifies a line or
  an inclusive range of lines that Macie detected an occurrence of sensitive data
  in, and the position of the data on the specified line or lines.

In certain cases, an object in a `lineRanges` array specifies the location of a
sensitive data detection in a file type or storage format that's supported by
another type of array. Those cases are: a detection in an unstructured section of an
otherwise structured file, such as a comment in a file; a detection in a malformed
file that Macie analyzes as plaintext; and, a CSV or TSV file that has one or more
column names that Macie detected sensitive data in.

- `offsetRanges` array – This array is reserved for future use. If this
  array is present, the value for it is
  null.
- `pages` array – This array applies to Adobe Portable Document Format
  (PDF) files. An object in this array specifies a page that Macie detected an
  occurrence of sensitive data
  in.
- `records` array – This array applies to Apache Avro object containers,
  Apache Parquet files, JSON files, and JSON Lines files. For Avro object containers
  and Parquet files, an object in this array specifies a record index and the path to
  a field in a record that Macie detected an occurrence of sensitive data in. For JSON
  and JSON Lines files, an object in this array specifies the path to a field or array
  that Macie detected an occurrence of sensitive data in. For JSON Lines files, it
  also specifies the index of the line that contains the data.

The contents of these arrays vary based on an affected S3 object's file type or storage
format and its contents.

## Schema details and examples

Amazon Macie tailors the contents of the JSON structures that it uses to indicate where it
detected sensitive data in specific types of files and content. The following topics
explain and provide examples of these structures.

###### Topics

- [Cells array](#findings-locate-sd-schema-examples-cell "#findings-locate-sd-schema-examples-cell")
- [LineRanges
  array](#findings-locate-sd-schema-examples-linerange "#findings-locate-sd-schema-examples-linerange")
- [Pages array](#findings-locate-sd-schema-examples-page "#findings-locate-sd-schema-examples-page")
- [Records array](#findings-locate-sd-schema-examples-record "#findings-locate-sd-schema-examples-record")

For a complete list of JSON structures that can be included in a sensitive data
finding, see [Findings](../APIReference/findings-describe.md "../APIReference/findings-describe.md") in the
_Amazon Macie API Reference_.

### Cells array

**Applies to:** Microsoft Excel workbooks, CSV files,
and TSV files

In a `cells` array, a `Cell` object specifies a cell or field that
Macie detected an occurrence of sensitive data in. The following table describes the
purpose of each field in a `Cell` object.

| Field           | Type    | Description                                                                                                                                                                                                                              |
| --------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cellReference` | String  | The location of the cell, as an absolute cell reference, that contains the occurrence.<br>This field applies only to Excel workbooks. This value is null for<br>CSV and TSV files.                                                       |
| `column`        | Integer | The column number of the column that contains the occurrence. For an Excel workbook,<br>this value correlates to the alphabetical character(s) for a column<br>identifier—for example, `1` for column A,<br>`2` for column B, and so on. |
| `columnName`    | String  | The name of the column that contains the occurrence, if available.                                                                                                                                                                       |
| `row`           | Integer | The row number of the row that contains the occurrence.                                                                                                                                                                                  |

The following example shows the structure of a `Cell` object that specifies the
location of an occurrence of sensitive data that Macie detected in a CSV
file.

```
"cells": [
   {
      "cellReference": null,
      "column": 3,
      "columnName": "SSN",
      "row": 5
   }
]
```

In the preceding example, the finding indicates that Macie detected sensitive data in the
field in the fifth row of the third column (named _SSN_) of the file.

The following example shows the structure of a `Cell` object that specifies the
location of an occurrence of sensitive data that Macie detected in an Excel
workbook.

```
"cells": [
   {
      "cellReference": "Sheet2!C5",
      "column": 3,
      "columnName": "SSN",
      "row": 5
   }
]
```

In the preceding example, the finding indicates that Macie detected sensitive data in the
worksheet named _Sheet2_ in the workbook. In that
worksheet, Macie detected sensitive data in the cell in the fifth row of the third
column (column C, named _SSN_).

### LineRanges

array

**Applies to:** Email message (EML) files, and non-binary text
files other than CSV, JSON, JSON Lines, and TSV files—for example, HTML, TXT,
and XML files

In a `lineRanges` array, a `Range` object specifies a line or an
inclusive range of lines that Macie detected an occurrence of sensitive data in, and
the position of the data on the specified line or lines.

This object is often empty for file types that are supported by other types of
arrays in `occurrences` objects. Exceptions are:

- Data in unstructured sections of an otherwise structured file, such as a
  comment in a file.
- Data in a malformed file that Macie analyzes as plaintext.
- A CSV or TSV file that has one or more column names that Macie detected sensitive data
  in.

The following table describes the purpose of each field in a `Range`
object of a `lineRanges` array.

| Field         | Type    | Description                                                                                                                                                                      |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `end`         | Integer | The number of lines from the beginning of the file to the end of the<br>occurrence.                                                                                              |
| `start`       | Integer | The number of lines from the beginning of the file to the beginning of the<br>occurrence.                                                                                        |
| `startColumn` | Integer | The number of characters, with spaces and starting from 1, from the beginning of the<br>first line that contains the occurrence (`start`) to the<br>beginning of the occurrence. |

The following example shows the structure of a `Range` object that specifies the
location of an occurrence of sensitive data that Macie detected on a single line in
a TXT file.

```
"lineRanges": [
   {
      "end": 1,
      "start": 1,
      "startColumn": 119
   }
]
```

In the preceding example, the finding indicates that Macie detected a complete occurrence
of sensitive data (a mailing address) in the first line of the file. The first
character in the occurrence is 119 characters (with spaces) from the beginning of
that line.

The following example shows the structure of a `Range` object that specifies the
location of an occurrence of sensitive data that spans multiple lines in a TXT
file.

```
"lineRanges": [
   {
      "end": 54,
      "start": 51,
      "startColumn": 1
   }
]
```

In the preceding example, the finding indicates that Macie detected an occurrence of
sensitive data (a mailing address) spanning lines 51 through 54 of the file. The
first character in the occurrence is the first character on line 51 of the
file.

### Pages array

**Applies to:** Adobe Portable Document Format (PDF)
files

In a `pages` array, a `Page` object specifies a page that Macie
detected an occurrence of sensitive data
in. The object contains a
`pageNumber` field. The `pageNumber` field stores an
integer that specifies the page number of the page that contains the
occurrence.

The following example shows the structure of a `Page` object that specifies the
location of an occurrence of sensitive data that Macie detected in a PDF
file.

```
"pages": [
   {
      "pageNumber": 10
   }
]
```

In the preceding example, the finding indicates that page 10 of the file contains the
occurrence.

### Records array

**Applies to:** Apache Avro object containers, Apache
Parquet files, JSON files, and JSON Lines files

For an Avro object container or a Parquet file, a `Record` object in a
`records` array specifies a record index and the path to a field in a
record that Macie detected an occurrence of sensitive data in. For JSON and JSON
Lines files, a `Record` object specifies the path to a field or array
that Macie detected an occurrence of sensitive data in. For JSON Lines files, it
also specifies the index of the line that contains the occurrence.

The following table describes the purpose of each field in a `Record`
object.

| Field         | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `jsonPath`    | String  | The path, as a JSONPath expression, to the occurrence.<br>For an Avro object container or a Parquet file, this is the<br>path to the field in the record (`recordIndex`) that<br>contains the occurrence. For a JSON or JSON Lines file, this is<br>the path to the field or array that contains the occurrence. If<br>the data is a value in an array, the path also indicates which<br>value contains the occurrence.<br>If Macie detects sensitive data in the name of any element in<br>the path, Macie omits the `jsonPath` field from a<br>`Record` object. If the name of a path element<br>exceeds 240 characters, Macie truncates the name by removing<br>characters from the beginning of the name. If the resulting full<br>path exceeds 250 characters, Macie also truncates the path,<br>starting with the first element in the path, until the path<br>contains 250 or fewer characters. |
| `recordIndex` | Integer | For an Avro object container or a Parquet file, the record index,<br>starting from 0, for the record that contains the occurrence. For a<br>JSON Lines file, the line index, starting from 0, for the line that<br>contains the occurrence. This value is always `0` for<br>JSON files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

The following example shows the structure of a `Record` object that
specifies the location of an occurrence of sensitive data that Macie detected in a
Parquet file.

```
"records": [
   {
      "jsonPath": "$['abcdefghijklmnopqrstuvwxyz']",
      "recordIndex": 7663
   }
]
```

In the preceding example, the finding indicates that Macie detected sensitive data
in the record of index 7663 (record number 7664). In that record, Macie detected
sensitive data in the field named `abcdefghijklmnopqrstuvwxyz`. The full
JSON path to the field in the record is `$.abcdefghijklmnopqrstuvwxyz`.
The field is a direct descendant of the root (outer-level) object.

The following example also shows the structure of a `Record` object for
an occurrence of sensitive data that Macie detected in a Parquet file. However, in
this example, Macie truncated the name of the field that contains the occurrence
because the name exceeds the character limit.

```
"records": [
   {
      "jsonPath": "$['...uvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']",
      "recordIndex": 7663
   }
]
```

In the preceding example, the field is a direct descendant of the root
(outer-level) object.

In the following example, also for an occurrence of sensitive data that Macie
detected in a Parquet file, Macie truncated the full path to the field that contains
the occurrence. The full path exceeds the character limit.

```
"records": [
   {
      "jsonPath": "$..usssn2.usssn3.usssn4.usssn5.usssn6.usssn7.usssn8.usssn9.usssn10.usssn11.usssn12.usssn13.usssn14.usssn15.usssn16.usssn17.usssn18.usssn19.usssn20.usssn21.usssn22.usssn23.usssn24.usssn25.usssn26.usssn27.usssn28.usssn29['abcdefghijklmnopqrstuvwxyz']",
      "recordIndex": 2335
   }
]
```

In the preceding example, the finding indicates that Macie detected sensitive data
in the record of index 2335 (record number 2336). In that record, Macie detected
sensitive data in the field named `abcdefghijklmnopqrstuvwxyz`. The full
JSON path to the field in the record is:

`$['1234567890']usssn1.usssn2.usssn3.usssn4.usssn5.usssn6.usssn7.usssn8.usssn9.usssn10.usssn11.usssn12.usssn13.usssn14.usssn15.usssn16.usssn17.usssn18.usssn19.usssn20.usssn21.usssn22.usssn23.usssn24.usssn25.usssn26.usssn27.usssn28.usssn29['abcdefghijklmnopqrstuvwxyz']`

The following example shows the structure of a `Record` object that
specifies the location of an occurrence of sensitive data that Macie detected in a
JSON file. In this example, the occurrence is a specific value in an array.

```
"records": [
   {
      "jsonPath": "$.access.key[2]",
      "recordIndex": 0
   }
]
```

In the preceding example, the finding indicates that Macie detected sensitive data
in the second value of an array named `key`. The array is a child of an
object named `access`.

The following example shows the structure of a `Record` object that
specifies the location of an occurrence of sensitive data that Macie detected in a
JSON Lines file.

```
"records": [
   {
      "jsonPath": "$.access.key",
      "recordIndex": 3
   }
]
```

In the preceding example, the finding indicates that Macie detected sensitive data
in the third value (line) in the file. In that line, the occurrence is in a field
named `key`, which is a child of an object named
`access`.
