# Use a SerDe to create a table

To use a SerDe when creating a table in Athena, use one of the following
methods:

- Specify `ROW FORMAT DELIMITED` and then use DDL statements to
  specify field delimiters, as in the following example. When you specify
  `ROW FORMAT DELIMITED`, Athena uses the LazySimpleSerDe by
  default.

```
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
ESCAPED BY '\\'
COLLECTION ITEMS TERMINATED BY '|'
MAP KEYS TERMINATED BY ':'
```

For examples of `ROW FORMAT DELIMITED`, see the following
topics:

[Lazy Simple SerDe for CSV, TSV, and custom-delimited
files](lazy-simple-serde.md "lazy-simple-serde.md")

[Query Amazon CloudFront logs](cloudfront-logs.md "cloudfront-logs.md")

[Query Amazon EMR logs](emr-logs.md "emr-logs.md")

[Query Amazon VPC flow logs](vpc-flow-logs.md "vpc-flow-logs.md")

[Use CTAS and INSERT INTO for ETL and data
analysis](ctas-insert-into-etl.md "ctas-insert-into-etl.md")

- Use `ROW FORMAT SERDE` to explicitly specify the type of SerDe that
  Athena should use when it reads and writes data to the table. The following
  example specifies the LazySimpleSerDe. To specify the delimiters, use `WITH
SERDEPROPERTIES`. The properties specified by `WITH
SERDEPROPERTIES` correspond to the separate statements (like
  `FIELDS TERMINATED BY`) in the `ROW FORMAT DELIMITED`
  example.

```
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
'serialization.format' = ',',
'field.delim' = ',',
'collection.delim' = '|',
'mapkey.delim' = ':',
'escape.delim' = '\\'
)
```

For examples of `ROW FORMAT SERDE`, see the following
topics:

[Avro SerDe](avro-serde.md "avro-serde.md")

[Grok SerDe](grok-serde.md "grok-serde.md")

[JSON SerDe libraries](json-serde.md "json-serde.md")

[Open CSV SerDe for processing CSV](csv-serde.md "csv-serde.md")

[Regex SerDe](regex-serde.md "regex-serde.md")
