# Create a table for AWS WAF logs without partitioning

This section describes how to create a table for AWS WAF logs without partitioning
or partition projection.

###### Note

For performance and cost reasons, we do not recommend using non-partitioned schema
for queries. For more information, see [Top 10
Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/") in the AWS Big Data Blog.

###### To create the AWS WAF table

1. Copy and paste the following DDL statement into the Athena console. Modify
   the fields as necessary to match your log output. Modify the
   `LOCATION` for the Amazon S3 bucket to correspond to the one that
   stores your logs.

This query uses the [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md").

###### Note

The SerDe expects each JSON document to be on a single line of text with
no line termination characters separating the fields in the record. If the
JSON text is in pretty print format, you may receive an error message like
**`HIVE_CURSOR_ERROR: Row is not a valid JSON Object`** or **`HIVE_CURSOR_ERROR: JsonParseException: Unexpected end-of-input: expected close marker for OBJECT`** when you attempt to query the table after you create it. For more
information, see [JSON Data Files](https://github.com/rcongiu/Hive-JSON-Serde#json-data-files "https://github.com/rcongiu/Hive-JSON-Serde#json-data-files") in the OpenX SerDe documentation on GitHub.

```
CREATE EXTERNAL TABLE `waf_logs`(
  `timestamp` bigint,
  `formatversion` int,
  `webaclid` string,
  `terminatingruleid` string,
  `terminatingruletype` string,
  `action` string,
  `terminatingrulematchdetails` array <
                                    struct <
                                        conditiontype: string,
                                        sensitivitylevel: string,
                                        location: string,
                                        matcheddata: array < string >
                                          >
                                     >,
  `httpsourcename` string,
  `httpsourceid` string,
  `rulegrouplist` array <
                      struct <
                          rulegroupid: string,
                          terminatingrule: struct <
                                              ruleid: string,
                                              action: string,
                                              rulematchdetails: array <
                                                                   struct <
                                                                       conditiontype: string,
                                                                       sensitivitylevel: string,
                                                                       location: string,
                                                                       matcheddata: array < string >
                                                                          >
                                                                    >
                                                >,
                          nonterminatingmatchingrules: array <
                                                              struct <
                                                                  ruleid: string,
                                                                  action: string,
                                                                  overriddenaction: string,
                                                                  rulematchdetails: array <
                                                                                       struct <
                                                                                           conditiontype: string,
                                                                                           sensitivitylevel: string,
                                                                                           location: string,
                                                                                           matcheddata: array < string >
                                                                                              >
                                                                   >,
                                                                  challengeresponse: struct <
                                                                            responsecode: string,
                                                                            solvetimestamp: string
                                                                              >,
                                                                  captcharesponse: struct <
                                                                            responsecode: string,
                                                                            solvetimestamp: string
                                                                              >
                                                                    >
                                                             >,
                          excludedrules: string
                            >
                       >,
`ratebasedrulelist` array <
                         struct <
                             ratebasedruleid: string,
                             limitkey: string,
                             maxrateallowed: int
                               >
                          >,
  `nonterminatingmatchingrules` array <
                                    struct <
                                        ruleid: string,
                                        action: string,
                                        rulematchdetails: array <
                                                             struct <
                                                                 conditiontype: string,
                                                                 sensitivitylevel: string,
                                                                 location: string,
                                                                 matcheddata: array < string >
                                                                    >
                                                             >,
                                        challengeresponse: struct <
                                                            responsecode: string,
                                                            solvetimestamp: string
                                                             >,
                                        captcharesponse: struct <
                                                            responsecode: string,
                                                            solvetimestamp: string
                                                             >
                                          >
                                     >,
  `requestheadersinserted` array <
                                struct <
                                    name: string,
                                    value: string
                                      >
                                 >,
  `responsecodesent` string,
  `httprequest` struct <
                    clientip: string,
                    country: string,
                    headers: array <
                                struct <
                                    name: string,
                                    value: string
                                      >
                                 >,
                    uri: string,
                    args: string,
                    httpversion: string,
                    httpmethod: string,
                    requestid: string
                      >,
  `labels` array <
               struct <
                   name: string
                     >
                >,
  `captcharesponse` struct <
                        responsecode: string,
                        solvetimestamp: string,
                        failureReason: string
                          >,
  `challengeresponse` struct <
                        responsecode: string,
                        solvetimestamp: string,
                        failureReason: string
                        >,
  `ja3Fingerprint` string,
  `oversizefields` string,
  `requestbodysize` int,
  `requestbodysizeinspectedbywaf` int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://`amzn-s3-demo-bucket`/`prefix`/'
```

2. Run the `CREATE EXTERNAL TABLE` statement in the Athena console
   query editor. This registers the `waf_logs` table and makes the
   data in it available for queries from Athena.
