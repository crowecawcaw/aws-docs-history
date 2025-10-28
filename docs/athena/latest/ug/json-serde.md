# JSON SerDe libraries

In Athena, you can use SerDe libraries to deserialize JSON data. Deserialization converts
the JSON data so that it can be serialized (written out) into a different format like
Parquet or ORC.

- [Hive JSON SerDe](hive-json-serde.md "hive-json-serde.md")
- [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md")
- [Amazon Ion Hive SerDe](ion-serde.md "ion-serde.md")

###### Note

The Hive and OpenX libraries expect JSON data to be on a single line (not formatted),
with records separated by a new line character.

Because Amazon Ion is a superset of JSON, you can use the Amazon Ion Hive SerDe to query
non-Amazon Ion JSON datasets. Unlike the Hive and OpenX JSON SerDe libraries, the Amazon Ion
SerDe does not expect each row of data to be on a single line. This feature is useful if you
want to query JSON datasets that are in "pretty print" format or otherwise break up the
fields in a row with newline characters.

## Library names

Use one of the following:

[org.apache.hive.hcatalog.data.JsonSerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON")

[org.openx.data.jsonserde.JsonSerDe](https://github.com/rcongiu/Hive-JSON-Serde "https://github.com/rcongiu/Hive-JSON-Serde")

[com.amazon.ionhiveserde.IonHiveSerDe](https://github.com/amzn/ion-hive-serde "https://github.com/amzn/ion-hive-serde")

## Additional resources

For more information about working with JSON and nested JSON in Athena, see the
following resources:

- [Create tables in Amazon Athena from nested JSON and mappings using
  JSONSerDe](https://aws.amazon.com/blogs/big-data/create-tables-in-amazon-athena-from-nested-json-and-mappings-using-jsonserde/ "https://aws.amazon.com/blogs/big-data/create-tables-in-amazon-athena-from-nested-json-and-mappings-using-jsonserde/") (AWS Big Data Blog)
- [I get errors when I
  try to read JSON data in Amazon Athena](https://aws.amazon.com/premiumsupport/knowledge-center/error-json-athena/ "https://aws.amazon.com/premiumsupport/knowledge-center/error-json-athena/") (AWS Knowledge Center
  article)
- [hive-json-schema](https://github.com/quux00/hive-json-schema "https://github.com/quux00/hive-json-schema") (GitHub) – Tool written in Java that
  generates `CREATE TABLE` statements from example JSON documents. The
  `CREATE TABLE` statements that are generated use the OpenX JSON
  Serde.
