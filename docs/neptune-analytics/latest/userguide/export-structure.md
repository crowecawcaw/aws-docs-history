# Structure of exported files

## CSV

When the export format is CSV, the generated vertex and edge files will be consistent with the Gremlin CSV format used by the
loader (for more information, see [Using CSV data](using-CSV-data.md "using-CSV-data.md")). The CSV files generated will,
with [one exception](export-filter-samples.md#export-filter-samples-2 "export-filter-samples.md#export-filter-samples-2"), be separated
by label to provide a label-driven schema design. This allows for the efficient export of only the properties that exist or
are specified for a particular vertex or edge label. Typically, multiple files will be created for each label (this allows
for increased export speed by writing in parallel using multiple threads), and each set of files sharing a label will have
the same schema and header.

The exception to this label-based separation occurs if you specify to export
[all labels together in the provided filter](export-filter-samples.md#export-filter-samples-2 "export-filter-samples.md#export-filter-samples-2"). In this case, the label column will indicate the
potentially different labels for each vertex and edge (when a vertex or edge has multiple labels, they will both be specified,
separated by semi-colons `‘;’`), and all files for vertices and/or edges will share the same schema. It is important
to note that vertices and edges will always be output to separate file sets.

## Parquet

Exported Parquet files have a columnar structure similar to CSV files, though an explicit header column is not required. Unlike
CSV files, property columns of fixed types will, where possible, be represented as named typed columns rather than with strings.
For instance, if a property column contains floating point numeric values, such a column might be a explicitly represented with
32-bit float values rather than the string representation of the value. This allows for less space to be used to store these
values. Like with CSV data, the Parquet files exported are structured to be compatible with the Neptune Analytics loader. For more
information on the columnar Parquet format used by Neptune Analytics, please see the corresponding documentation for the loader.
For more information, see [Using CSV data](using-CSV-data.md "using-CSV-data.md").

As listed in the loader, [metadata](using-Parquet-data.md#using-Parquet-data-property-column-headers "using-Parquet-data.md#using-Parquet-data-property-column-headers")
is used to indicate some special circumstances, such as special
types and multiple types being present for a given property. In addition, the exported parquet files (due to standard
restrictions in permitted column names in parquet data) may indicate in metadata if a column corresponding to a property has
been necessarily renamed (for example, if the property name has a character disallowed by the parquet standard), such as in
the following:

```
"metadata": {
  "anyTypeColumns": [
   "col2"
  ],
  "invalidVertexPropertyNames": {
   "http://www.company.com/id": "col2",
   "http://www.w3.org/2000/01/rdf-schema#label": "col3"
  },
  "renamedVertexProperties": {
   "http://www.company.com/id": "col2",
   "http://www.w3.org/2000/01/rdf-schema#label": "col3"
  }
 }
```
