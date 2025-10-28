# Amazon Ion Hive SerDe

You can use the Amazon Ion Hive SerDe to query data stored in [Amazon Ion](https://amzn.github.io/ion-docs/guides/cookbook.html "https://amzn.github.io/ion-docs/guides/cookbook.html") format.
Amazon Ion is a richly-typed, self-describing, open source data format. The Amazon Ion
format is used in the open source SQL query language [PartiQL](https://partiql.org/ "https://partiql.org/").

Amazon Ion has binary and text formats that are interchangeable. This feature combines the
ease of use of text with the efficiency of binary encoding.

To query Amazon Ion data from Athena, you can use the [Amazon Ion Hive SerDe](https://github.com/amzn/ion-hive-serde "https://github.com/amzn/ion-hive-serde"), which
serializes and deserializes Amazon Ion data. Deserialization allows you to run queries on
the Amazon Ion data or read it for writing out into a different format like Parquet or ORC.
Serialization lets you generate data in the Amazon Ion format by using `CREATE TABLE AS
 SELECT` (CTAS) or `INSERT INTO` queries to copy data from existing
tables.

###### Note

Because Amazon Ion is a superset of JSON, you can use the Amazon Ion Hive SerDe to
query non-Amazon Ion JSON datasets. Unlike other [JSON SerDe
libraries](json-serde.md "json-serde.md"), the Amazon Ion SerDe does not expect each row of data to be on a
single line. This feature is useful if you want to query JSON datasets that are in
"pretty print" format or otherwise break up the fields in a row with newline
characters.

For additional information and examples of querying Amazon Ion with Athena, see [Analyze
Amazon Ion datasets using Amazon Athena](https://aws.amazon.com/blogs/big-data/analyze-amazon-ion-datasets-using-amazon-athena/ "https://aws.amazon.com/blogs/big-data/analyze-amazon-ion-datasets-using-amazon-athena/").

## Serialization library name

The serialization library name for the Amazon Ion SerDe is
`com.amazon.ionhiveserde.IonHiveSerDe`. For source code information, see
[Amazon Ion Hive
SerDe](https://github.com/amazon-ion/ion-hive-serde "https://github.com/amazon-ion/ion-hive-serde") on GitHub.com.

## Considerations and

limitations

- Duplicated fields – Amazon Ion structs
  are ordered and support duplicated fields, while Hive's
  `STRUCT<>` and `MAP<>` do not. Thus, when
  you deserialize a duplicated field from an Amazon Ion struct, a single value is
  chosen non deterministically, and the others are ignored.
- External symbol tables unsupported –
  Currently, Athena does not support external symbol tables or the following Amazon
  Ion Hive SerDe properties:
  - `ion.catalog.class`
  - `ion.catalog.file`
  - `ion.catalog.url`
  - `ion.symbol_table_imports`

- File extensions – Amazon Ion uses file
  extensions to determine which compression codec to use for deserializing Amazon
  Ion files. As such, compressed files must have the file extension that
  corresponds to the compression algorithm used. For example, if ZSTD is used,
  corresponding files should have the extension `.zst`.
- Homogeneous data – Amazon Ion has no
  restrictions on the data types that can be used for values in particular fields.
  For example, two different Amazon Ion documents might have a field with the same
  name that have different data types. However, because Hive uses a schema, all
  values that you extract to a single Hive column must have the same data
  type.
- Map key type restrictions – When you
  serialize data from another format into Amazon Ion, ensure that the map key type
  is one of `STRING`, `VARCHAR`, or `CHAR`.
  Although Hive allows you to use any primitive data type as a map key, [Amazon Ion
  symbols](https://amzn.github.io/ion-docs/docs/symbols.html "https://amzn.github.io/ion-docs/docs/symbols.html") must be a string type.
- Union type – Athena does not currently
  support the Hive [union type](https://cwiki.apache.org/confluence/display/hive/languagemanual+types/#LanguageManualTypes-UnionTypesunionUnionTypes "https://cwiki.apache.org/confluence/display/hive/languagemanual+types/#LanguageManualTypes-UnionTypesunionUnionTypes").
- Double data type – Amazon Ion does not
  currently support the `double` data type.

###### Topics

- [Create Amazon Ion tables](ion-serde-using-create-table.md "ion-serde-using-create-table.md")
- [Use CTAS and
  INSERT INTO to create Amazon Ion tables](ion-serde-using-ctas-and-insert-into-to-create-ion-tables.md "ion-serde-using-ctas-and-insert-into-to-create-ion-tables.md")
- [Amazon Ion SerDe property
  reference](ion-serde-using-ion-serde-properties.md "ion-serde-using-ion-serde-properties.md")
- [Use path extractors](ion-serde-using-path-extractors.md "ion-serde-using-path-extractors.md")
