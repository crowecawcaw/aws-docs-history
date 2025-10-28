# Convert input data format in Amazon Data Firehose

Amazon Data Firehose can convert the format of your input data from JSON to [Apache Parquet](https://parquet.apache.org/ "https://parquet.apache.org/") or [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") before storing the data in Amazon S3.
Parquet and ORC are columnar data formats that save space and enable faster queries compared
to row-oriented formats like JSON. If you want to convert an input format other than JSON,
such as comma-separated values (CSV) or structured text, you can use AWS Lambda to transform
it to JSON first. For more information, see [Transform source data in Amazon Data Firehose](data-transformation.md "data-transformation.md").

You can convert the format of your data even if you aggregate your records before
sending them to Amazon Data Firehose.

Amazon Data Firehose requires the following three elements to convert the format of your record data:

## Deserializer

Amazon Data Firehose requires a deserializer to read the JSON of your input data. You can choose
one of the following two types of deserializer.

When combining multiple JSON documents into the same record, make sure
that your input is still presented in the supported JSON format. An array of
JSON documents is not a valid input.

For example, this is the correct input: `{"a": 1}{"b": 1}` and this is the incorrect input: `[{"a":1}, {"a":2}]`.

- [Apache Hive JSON SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON")
- [OpenX JSON
  SerDe](https://github.com/rcongiu/Hive-JSON-Serde "https://github.com/rcongiu/Hive-JSON-Serde")

Choose the [OpenX JSON
SerDe](https://github.com/rcongiu/Hive-JSON-Serde "https://github.com/rcongiu/Hive-JSON-Serde") if your input JSON contains time stamps in the following
formats:

- yyyy-MM-dd'T'HH:mm:ss[.S]'Z', where the fraction can have up to 9 digits
  – For example, `2017-02-07T15:13:01.39256Z`.
- yyyy-[M]M-[d]d HH:mm:ss[.S], where the fraction can have up to 9 digits
  – For example, `2017-02-07 15:13:01.14`.
- Epoch seconds – For example, `1518033528`.
- Epoch milliseconds – For example, `1518033528123`.
- Floating point epoch seconds – For example,
  `1518033528.123`.
  The OpenX JSON SerDe can convert periods (`.`) to underscores
  (`_`). It can also convert JSON keys to lowercase before deserializing
  them. For more information about the options that are available with this deserializer
  through Amazon Data Firehose, see [OpenXJsonSerDe](../APIReference/API_OpenXJsonSerDe.md "../APIReference/API_OpenXJsonSerDe.md").

If you're not sure which deserializer to choose, use the OpenX JSON SerDe, unless you
have time stamps that it doesn't support.

If you have time stamps in formats other than those listed previously, use the [Apache Hive JSON SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON"). When you choose this deserializer, you can specify
the time stamp formats to use. To do this, follow the pattern syntax of the Joda-Time
`DateTimeFormat` format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html "https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html").

You can also use the special value `millis` to parse time stamps in epoch
milliseconds. If you don't specify a format, Amazon Data Firehose uses
`java.sql.Timestamp::valueOf` by default.

The Hive JSON SerDe doesn't allow the following:

- Periods (`.`) in column names.
- Fields whose type is `uniontype`.
- Fields that have numerical types in the schema, but that are strings in the
  JSON. For example, if the schema is (an int), and the JSON is
  `{"a":"123"}`, the Hive SerDe gives an error.
  The Hive SerDe doesn't convert nested JSON into strings. For example, if you have
  `{"a":{"inner":1}}`, it doesn't treat `{"inner":1}` as a
  string.

## Schema

Amazon Data Firehose requires a schema to determine how to interpret that
data. Use [AWS
Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") to create a schema in the AWS Glue Data Catalog. Amazon Data Firehose then references
that schema and uses it to interpret your input data. You can use the same
schema to configure both Amazon Data Firehose and your analytics software. For more
information, see [Populating
the AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md") in the _AWS Glue Developer
Guide_.

###### Note

The schema created in AWS Glue Data Catalog should match the input data structure. Otherwise, the converted data will not contain attributes that are not specified in the schema. If you use nested JSON, use a STRUCT type in the schema that mirrors the structure of your JSON data. See [this example](../../../athena/latest/ug/openx-json-serde.md#nested-json-serde-example "../../../athena/latest/ug/openx-json-serde.md#nested-json-serde-example") for how to handle nested JSON with a STRUCT type.

###### Important

For data types that do not specify a size limit, there is a practical limit of 32 MBs
for all of the data in a single row.

If you specify length for `CHAR` or `VARCHAR`, Firehose
truncates the strings at the specified length when it reads the input data. If the
underlying data string is longer, it remains unchanged.

## Serializer

**Firehose requires a serializer to convert the data to the target columnar
storage format (Parquet or ORC)** – You can choose one of the following
two types of serializers.

- [ORC SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC")
- [Parquet
  SerDe](https://cwiki.apache.org/confluence/display/Hive/Parquet "https://cwiki.apache.org/confluence/display/Hive/Parquet")

The serializer that you choose depends on your business needs. To learn more about the
two serializer options, see [ORC
SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC") and [Parquet
SerDe](https://cwiki.apache.org/confluence/display/Hive/Parquet "https://cwiki.apache.org/confluence/display/Hive/Parquet").
