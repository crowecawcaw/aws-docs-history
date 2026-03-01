# Hive JSON SerDe

The Hive JSON SerDe is commonly used to process JSON data like events. These events are
represented as single-line strings of JSON-encoded text separated by a new line. The Hive
JSON SerDe does not allow duplicate keys in `map` or `struct` key
names.

###### Note

The SerDe expects each JSON document to be on a single line of text with
no line termination characters separating the fields in the record. If the
JSON text is in pretty print format, you may receive an error message like
**`HIVE_CURSOR_ERROR: Row is not a valid JSON Object`** or **`HIVE_CURSOR_ERROR: JsonParseException: Unexpected end-of-input: expected close marker for OBJECT`** when you attempt to query the table after you create it. For more
information, see [JSON Data Files](https://github.com/rcongiu/Hive-JSON-Serde#json-data-files "https://github.com/rcongiu/Hive-JSON-Serde#json-data-files") in the OpenX SerDe documentation on GitHub.

The following example DDL statement uses the Hive JSON SerDe to create a table based on
sample online advertising data. In the `LOCATION` clause, replace the
`myregion` in
`s3://amzn-s3-demo-bucket.elasticmapreduce/samples/hive-ads/tables/impressions`
with the region identifier where you run Athena (for example,
`s3://us-west-2.elasticmapreduce/samples/hive-ads/tables/impressions`).

```
CREATE EXTERNAL TABLE impressions (
    requestbegintime string,
    adid string,
    impressionid string,
    referrer string,
    useragent string,
    usercookie string,
    ip string,
    number string,
    processid string,
    browsercookie string,
    requestendtime string,
    timers struct
                <
                 modellookup:string,
                 requesttime:string
                >,
    threadid string,
    hostname string,
    sessionid string
)
PARTITIONED BY (dt string)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION 's3://amzn-s3-demo-bucket.elasticmapreduce/samples/hive-ads/tables/impressions';
```

## Specify timestamp formats with the Hive JSON SerDe

To parse timestamp values from string, you can add the `WITH
 SERDEPROPERTIES` subfield to the `ROW FORMAT SERDE` clause and use
it to specify the `timestamp.formats` parameter. In the parameter, specify a
comma-separated list of one or more timestamp patterns, as in the following
example:

```
...
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
WITH SERDEPROPERTIES ("timestamp.formats"="yyyy-MM-dd'T'HH:mm:ss.SSS'Z',yyyy-MM-dd'T'HH:mm:ss")
...
```

For more information, see [Timestamps](https://cwiki.apache.org/confluence/display/hive/languagemanual+types#LanguageManualTypes-TimestampstimestampTimestamps "https://cwiki.apache.org/confluence/display/hive/languagemanual+types#LanguageManualTypes-TimestampstimestampTimestamps") in the Apache Hive documentation.

## Load the table for querying

After you create the table, run [MSCK REPAIR TABLE](msck-repair-table.md "msck-repair-table.md") to load the table and make it queryable from
Athena:

```
MSCK REPAIR TABLE impressions
```

## Query CloudTrail logs

You can use the Hive JSON SerDe to query CloudTrail logs. For more information and example
`CREATE TABLE` statements, see [Query AWS CloudTrail logs](cloudtrail-logs.md "cloudtrail-logs.md").
