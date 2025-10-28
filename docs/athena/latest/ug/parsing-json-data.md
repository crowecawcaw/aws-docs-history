# Best practices for reading JSON data

JavaScript Object Notation (JSON) is a common method for encoding data structures as text.
Many applications and tools output data that is JSON-encoded.

In Amazon Athena, you can create tables from external data and include the JSON-encoded data
in them. For such types of source data, use Athena together with [JSON SerDe libraries](json-serde.md "json-serde.md").

Use the following tips to read JSON-encoded data:

- Choose the right SerDe, a native JSON SerDe,
  `org.apache.hive.hcatalog.data.JsonSerDe`, or an OpenX SerDe,
  `org.openx.data.jsonserde.JsonSerDe`. For more information, see [JSON SerDe libraries](json-serde.md "json-serde.md").
- Make sure that each JSON-encoded record is represented on a separate line, not
  pretty-printed.

###### Note

The SerDe expects each JSON document to be on a single line of text with
no line termination characters separating the fields in the record. If the
JSON text is in pretty print format, you may receive an error message like
**`HIVE_CURSOR_ERROR: Row is not a valid JSON Object`** or **`HIVE_CURSOR_ERROR: JsonParseException: Unexpected end-of-input: expected close marker for OBJECT`** when you attempt to query the table after you create it. For more
information, see [JSON Data Files](https://github.com/rcongiu/Hive-JSON-Serde#json-data-files "https://github.com/rcongiu/Hive-JSON-Serde#json-data-files") in the OpenX SerDe documentation on GitHub.

- Generate your JSON-encoded data in case-insensitive columns.
- Provide an option to ignore malformed records, as in this example.

```
CREATE EXTERNAL TABLE json_table (
  column_a string,
  column_b int
 )
 ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 `WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')`
 LOCATION 's3://amzn-s3-demo-bucket/path/';

```

- Convert fields in source data that have an undetermined schema to JSON-encoded
  strings in Athena.
  When Athena creates tables backed by JSON data, it parses the data based on the existing
  and predefined schema. However, not all of your data may have a predefined schema. To
  simplify schema management in such cases, it is often useful to convert fields in source
  data that have an undetermined schema to JSON strings in Athena, and then use [JSON SerDe libraries](json-serde.md "json-serde.md").

For example, consider an IoT application that publishes events with common fields from
different sensors. One of those fields must store a custom payload that is unique to the
sensor sending the event. In this case, since you don't know the schema, we recommend that
you store the information as a JSON-encoded string. To do this, convert data in your Athena
table to JSON, as in the following example. You can also convert JSON-encoded data to Athena
data types.

###### Topics

- [Convert Athena data types to
  JSON](converting-native-data-types-to-json.md "converting-native-data-types-to-json.md")
- [Convert JSON to Athena data
  types](converting-json-to-native-data-types.md "converting-json-to-native-data-types.md")
