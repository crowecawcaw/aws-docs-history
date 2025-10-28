# Work with CSV data in AWS Glue

This page describes how to use AWS Glue to create schema from CSV files that have quotes
around the data values for each column or from CSV files that include header values.

## Handling CSV data enclosed in quotes

Suppose a CSV file has data fields enclosed in double quotes, as in the following
example.

```
"John","Doe","123-555-1231","John said \"hello\""
"Jane","Doe","123-555-9876","Jane said \"hello\""
```

To run a query in Athena on a table created from a CSV file that has quoted values, you
must modify the table properties in AWS Glue to use the OpenCSVSerDe. For more information
about the OpenCSV SerDe, see [Open CSV SerDe for processing CSV](csv-serde.md "csv-serde.md").

###### To edit table properties in the AWS Glue console

1. In the AWS Glue console navigation pane, choose
   **Tables**.
2. Choose the link for the table that you want to edit, and then choose
   **Actions**, **Edit table**.
3. On the **Edit table** page, make the following
   changes:
   - For **Serialization lib**, enter
     `org.apache.hadoop.hive.serde2.OpenCSVSerde`.
   - For **Serde parameters**, enter the following values
     for the keys `escapeChar`, `quoteChar`, and
     `separatorChar`:
     - For `escapeChar`, enter a backslash
       (`\`).
     - For `quoteChar`, enter a double quote
       (`"`).
     - For `separatorChar`, enter a comma
       (`,`).

4. Choose **Save**.

For more information, see [Viewing and editing table details](../../../glue/latest/dg/console-tables.md#console-tables-details "../../../glue/latest/dg/console-tables.md#console-tables-details") in the _AWS Glue Developer
Guide_.

You can also update AWS Glue table properties programmatically. Use the AWS Glue [UpdateTable](../../../glue/latest/webapi/API_UpdateTable.md "../../../glue/latest/webapi/API_UpdateTable.md") API operation or the [update-table](../../../cli/latest/reference/glue/update-table.md "../../../cli/latest/reference/glue/update-table.md") AWS CLI command
to modify the `SerDeInfo` block in the table definition, as in the following
JSON example.

```
"SerDeInfo": {
   "name": "",
   "serializationLib": "org.apache.hadoop.hive.serde2.OpenCSVSerde",
   "parameters": {
      "separatorChar": ","
      "quoteChar": "\""
      "escapeChar": "\\"
      }
},
```

## Handling CSV files with headers

When you define a table in Athena with a `CREATE TABLE` statement, you can
use the `skip.header.line.count` table property to ignore headers in your CSV
data, as in the following example.

```
...
STORED AS TEXTFILE
LOCATION 's3://amzn-s3-demo-bucket/`csvdata_folder`/';
TBLPROPERTIES ("skip.header.line.count"="1")
```

Alternatively, you can remove the CSV headers beforehand so that the header
information is not included in Athena query results. One way to achieve this is to use
AWS Glue jobs, which perform extract, transform, and load (ETL) work. You can write
scripts in AWS Glue using a language that is an extension of the PySpark Python
dialect. For more information, see [Authoring Jobs in AWS Glue](../../../glue/latest/dg/author-job-glue.md "../../../glue/latest/dg/author-job-glue.md") in
the _AWS Glue Developer Guide_.

The following example shows a function in an AWS Glue script that writes out a dynamic
frame using `from_options`, and sets the `writeHeader` format
option to false, which removes the header information:

```
glueContext.write_dynamic_frame.from_options(frame = applymapping1, connection_type = "s3", connection_options = {"path": "s3://amzn-s3-demo-bucket/MYTABLEDATA/"}, format = "csv", format_options = {"writeHeader": False}, transformation_ctx = "datasink2")
```
