# Use SerDes

Athena supports several SerDe (Serializer/Deserializer) libraries that parse data from a
variety of data formats. When you create a table in Athena, you can specify a SerDe that
corresponds to the format that your data is in. Athena does not support custom SerDes.

Athena can use SerDe libraries to create tables from CSV, TSV, custom-delimited, and JSON
formats; data from the Hadoop-related formats ORC, Avro, and Parquet; logs from Logstash,
AWS CloudTrail logs, and Apache WebServer logs. Each of these data formats has one or more
serializer-deserializer (SerDe) libraries that Athena can use to parse the data.

###### Note

The formats listed in this section are used by Athena for reading data. For information
about formats that Athena uses for writing data when it runs CTAS queries, see [Create a table from query results (CTAS)](ctas.md "ctas.md").

###### Topics

- [Choose a SerDe for your data](supported-serdes.md "supported-serdes.md")
- [Use a SerDe to create a table](serde-create-a-table.md "serde-create-a-table.md")
- [Amazon Ion Hive SerDe](ion-serde.md "ion-serde.md")
- [Avro SerDe](avro-serde.md "avro-serde.md")
- [Grok SerDe](grok-serde.md "grok-serde.md")
- [JSON SerDe libraries](json-serde.md "json-serde.md")
- [CSV SerDe libraries](serde-csv-choices.md "serde-csv-choices.md")
- [ORC SerDe](orc-serde.md "orc-serde.md")
- [Parquet SerDe](parquet-serde.md "parquet-serde.md")
- [Regex SerDe](regex-serde.md "regex-serde.md")
