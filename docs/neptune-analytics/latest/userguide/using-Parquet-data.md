# Using Parquet data

Neptune Analytics supports importing data using the Parquet format. A Parquet file must contain a header row and the column values. The
remainder of the files are interpreted based on the corresponding header column. The header should contain predefined system
column names and/or user-defined column names. Aside from the header row and column values, a Parquet file also has metadata
which is stored in-line with the Parquet file, and is used in the reading and decoding of said data.

###### Note

Compression for Parquet format is not supported at this time.

## System column headers

The required and allowed system column headers are different for vertex files and edge files. Each system column can appear
only once in a header. All labels are case sensitive.

###### Note

The `~id` column in `edge` (`relationship`) files in
`Parquet` format are not supported. They are ignored if provided in any of the `edge`
(`relationship`) files.

###### Vertex headers

- `~id` - Required. An `id` for the vertex.
- `~label` - Optional. A label for the vertex, multiple label values are supported, separated by
  semicolons (`;`).

###### Edge headers

- `~from` - Required. The vertex `id` of the **from** vertex.
- `~to` - Required. The vertex `id` of the **to** vertex.
- `~label` - Optional. A label for the edge. Edges can only have a single label.

## Property column headers

Unlike the property column headers of the CSV format, the property column headers of the Parquet format only need to
have the property names, there is no need to have the type names nor the cardinality.

There are however, some special column types in the Parquet format that requires annotation in the metadata, including
`Any` type, `Date` type, and `dateTime` type. For more details of `Any` type,
`Date` type, and `dateTime` type, please refer to [using CSV data](using-CSV-data.md "using-CSV-data.md").
The following object is an example of the metadata that has `Any` type column, `Date` type column and
`dateTime` type column annotated:

```
"metadata": {
    "anyTypeColumns": ["UserCol1"],
    "dateTypeColumns": ["UserCol2"],
    "dateTimeTypeColumns": ["UserCol3"]
}
```

###### Note

Space, comma, carriage return and newline characters are not allowed in the column headers, so property names cannot
include these characters.
