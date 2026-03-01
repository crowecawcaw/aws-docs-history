# Create the table for resolver query logs

You can use the Query Editor in the Athena console to create and query a table for your
Route 53 Resolver query logs.

###### To create and query an Athena table for Route 53 resolver query logs

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the Athena Query Editor, enter the following `CREATE TABLE`
   statement. Replace the `LOCATION` clause values with those
   corresponding to the location of your Resolver logs in Amazon S3.

```
CREATE EXTERNAL TABLE r53_rlogs (
  version string,
  account_id string,
  region string,
  vpc_id string,
  query_timestamp string,
  query_name string,
  query_type string,
  query_class
    string,
  rcode string,
  answers array<
    struct<
      Rdata: string,
      Type: string,
      Class: string>
    >,
  srcaddr string,
  srcport int,
  transport string,
  srcids struct<
    instance: string,
    resolver_endpoint: string
    >,
  firewall_rule_action string,
  firewall_rule_group_id string,
  firewall_domain_list_id string
 )

ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`aws_account_id`/vpcdnsquerylogs/`{vpc-id}`/'
```

Because Resolver query log data is in JSON format, the CREATE TABLE statement
uses a [JSON SerDe
library](json-serde.md "json-serde.md") to analyze the data.

###### Note

The SerDe expects each JSON document to be on a single line of text with
no line termination characters separating the fields in the record. If the
JSON text is in pretty print format, you may receive an error message like
**`HIVE_CURSOR_ERROR: Row is not a valid JSON Object`** or **`HIVE_CURSOR_ERROR: JsonParseException: Unexpected end-of-input: expected close marker for OBJECT`** when you attempt to query the table after you create it. For more
information, see [JSON Data Files](https://github.com/rcongiu/Hive-JSON-Serde#json-data-files "https://github.com/rcongiu/Hive-JSON-Serde#json-data-files") in the OpenX SerDe documentation on GitHub. 3. Choose **Run query**. The statement creates an Athena table
named `r53_rlogs` whose columns represent each of the fields in your
Resolver log data. 4. In the Athena console Query Editor, run the following query to verify that your
table has been created.

```
SELECT * FROM "r53_rlogs" LIMIT 10
```
