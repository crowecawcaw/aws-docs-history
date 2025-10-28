# Use path extractors

Amazon Ion is a document style file format, but Apache Hive is a flat columnar format. You
can use special Amazon Ion SerDe properties called `path extractors` to map
between the two formats. Path extractors flatten the hierarchical Amazon Ion format, map
Amazon Ion values to Hive columns, and can be used to rename fields.

Athena can generate the extractors for you, but you can also define your own extractors if
necessary.

###### Topics

- [Use Athena generated path
  extractors](ion-serde-generated-path-extractors.md "ion-serde-generated-path-extractors.md")
- [Specify your own path
  extractors](ion-serde-specifying-your-own-path-extractors.md "ion-serde-specifying-your-own-path-extractors.md")
- [Use search paths in
  path extractors](ion-serde-using-search-paths-in-path-extractors.md "ion-serde-using-search-paths-in-path-extractors.md")
- [Path extractor examples](ion-serde-examples.md "ion-serde-examples.md")
