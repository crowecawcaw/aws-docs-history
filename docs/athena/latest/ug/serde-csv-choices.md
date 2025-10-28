# CSV SerDe libraries

When you create a table for CSV data in Athena, you can use either the Open CSV SerDe or
the Lazy Simple SerDe library. To help you decide which to use, consider the following
guidelines.

- If your data contains values enclosed in double quotes (`"`), you can
  use the [Open
  CSV SerDe](https://cwiki.apache.org/confluence/display/Hive/CSV+Serde "https://cwiki.apache.org/confluence/display/Hive/CSV+Serde") library to deserialize the values in Athena. If your data does
  not contain values enclosed in double quotes (`"`), you can omit
  specifying any SerDe. In this case, Athena uses the default Lazy Simple SerDe. For
  information, see [Lazy Simple SerDe for CSV, TSV, and custom-delimited
  files](lazy-simple-serde.md "lazy-simple-serde.md").
- If your data has UNIX numeric `TIMESTAMP` values (for example,
  `1579059880000`), use the Open CSV SerDe. If your data uses the
  `java.sql.Timestamp` format, use the Lazy Simple SerDe.

###### Topics

- [Lazy Simple SerDe for CSV, TSV, and custom-delimited
  files](lazy-simple-serde.md "lazy-simple-serde.md")
- [Open CSV SerDe for processing CSV](csv-serde.md "csv-serde.md")
