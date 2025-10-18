# Run and manage CloudTrail Lake queries with the AWS CLI

You can use the AWS CLI to run and manage your CloudTrail Lake queries. When using the AWS CLI,
 remember that your commands run in the AWS Region configured for your profile. If
 you want to run the commands in a different Region, either change the default Region for
 your profile, or use the **--region** parameter with the command.


## Available commands for CloudTrail Lake queries


Commands for running and managing queries in CloudTrail Lake include:



* `start-query` to run a query.
* `describe-query` to return metadata about a query.
* `generate-query` to produce a query from an English language prompt. For more information, 
 see [Create CloudTrail Lake queries from natural language
 prompts](lake-query-generator.md "lake-query-generator.md").
* `get-query-results` to return query results for the specified query ID.
* `list-queries` to get a list queries for the specified event data store.
* `cancel-query` to cancel a running query.

For a list of available commands for CloudTrail Lake event data stores, see [Available commands for event data stores](lake-eds-cli.md#lake-eds-cli-commands "lake-eds-cli.md#lake-eds-cli-commands").


For a list of available commands for CloudTrail Lake dashboards, see 
 [Available commands for dashboards](lake-dashboard-cli.md#lake-dashboard-cli-commands "lake-dashboard-cli.md#lake-dashboard-cli-commands").


For a list of available commands for CloudTrail Lake integrations, see [Available commands for CloudTrail Lake integrations](lake-integrations-cli.md#lake-integrations-cli-commands "lake-integrations-cli.md#lake-integrations-cli-commands").


## Produce a query from a natural language prompt with the AWS CLI


Run the `generate-query` command to generate a query
 from an English prompt. For `--event-data-stores`,
 provide the ARN (or ID suffix of the ARN) of the event data store
 you want to query. You can only specify one event data store. For `--prompt`, provide the prompt in
 English.



```
aws cloudtrail generate-query 
--event-data-stores arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE \
--prompt "Show me all console login events for the past week?"
```

If successful, the command outputs a SQL statement and provides a
 `QueryAlias` that you will use with the
 `start-query` command to run the query against your
 event data store.



```
{
  "QueryStatement": "SELECT * FROM $EDS_ID WHERE eventname = 'ConsoleLogin' AND eventtime >= timestamp '2024-09-16 00:00:00' AND eventtime <= timestamp '2024-09-23 00:00:00' AND eventSource = 'signin.amazonaws.com'",
  "QueryAlias": "AWSCloudTrail-UUID"
}
```

## Start a query with the AWS CLI


The following example AWS CLI **start-query** command runs a query on the event data store specified as an ID in
 the query statement and delivers the query results to a specified S3 bucket. The
 `--query-statement` parameter provides a SQL query, enclosed in
 single quotation marks. Optional parameters include `--delivery-s3-uri`,
 to deliver the query results to a specified S3 bucket. For more information about the
 query language you can use in CloudTrail Lake, see [CloudTrail Lake SQL constraints](query-limitations.md "query-limitations.md").



```
aws cloudtrail start-query
--query-statement 'SELECT eventID, eventTime FROM EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE LIMIT 10'
--delivery-s3-uri "s3://aws-cloudtrail-lake-query-results-123456789012-us-east-1"
```

The response is a `QueryId` string. To get the status of a query, run
 **describe-query** using the `QueryId` value returned
 by **start-query**. If the query is successful, you can run
 **get-query-results** to get results.


**Output**



```
{
    "QueryId": "EXAMPLE2-0add-4207-8135-2d8a4EXAMPLE"
}
```

###### Note

Queries that run for longer than one hour might time out. You can still get
 partial results that were processed before the query timed out.

If you are delivering the query results to an S3 bucket using the optional
 `--delivery-s3-uri` parameter, the bucket policy must grant CloudTrail
 permission to delivery query results to the bucket. For information about
 manually editing the bucket policy, see [Amazon S3 bucket policy for CloudTrail Lake query results](s3-bucket-policy-lake-query-results.md "s3-bucket-policy-lake-query-results.md").


## Get metadata about a query with the AWS CLI


The following example AWS CLI **describe-query** command gets
 metadata about a query, including query run time in milliseconds, number of events
 scanned and matched, total number of bytes scanned, and query status. The
 `BytesScanned` value matches the number of bytes for which your
 account is billed for the query, unless the query is still running. If the query results were delivered to an S3 bucket, 
 the response also provides the S3 URI and the delivery status.


You must specify a value for either the `--query-id` or the `--query-alias` parameter. 
 Specifying the `--query-alias` parameter returns information about the last query run for the alias. 



```
aws cloudtrail describe-query --query-id EXAMPLEd-17a7-47c3-a9a1-eccf7EXAMPLE
```

The following is an example response.



```
{
    "QueryId": "EXAMPLE2-0add-4207-8135-2d8a4EXAMPLE", 
    "QueryString": "SELECT eventID, eventTime FROM EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE LIMIT 10", 
    "QueryStatus": "RUNNING",
    "QueryStatistics": {
        "EventsMatched": 10,
        "EventsScanned": 1000,
        "BytesScanned": 35059,
        "ExecutionTimeInMillis": 3821,
        "CreationTime": "1598911142"
    }
}
```

## Get query results with the AWS CLI


The following example AWS CLI **get-query-results** command gets event data results of a query. You must
 specify the `--query-id` returned by the **start-query** command. The
 `BytesScanned` value matches the number of bytes for which your
 account is billed for the query, unless the query is still running. Optional
 parameters include `--max-query-results`, to specify a maximum number of
 results that you want the command to return on a single page. If there are more
 results than your specified `--max-query-results` value, run the command
 again adding the returned `NextToken` value to get the next page of
 results.



```
aws cloudtrail get-query-results
--query-id EXAMPLEd-17a7-47c3-a9a1-eccf7EXAMPLE
```

**Output**



```
{
    "QueryStatus": "RUNNING",
    "QueryStatistics": {
        "ResultsCount": 244,
        "TotalResultsCount": 1582,
        "BytesScanned":27044
    },
    "QueryResults": [
      {
        "key": "eventName",
        "value": "StartQuery",
      }
   ],
    "QueryId": "EXAMPLE2-0add-4207-8135-2d8a4EXAMPLE", 
    "QueryString": "SELECT eventID, eventTime FROM EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE LIMIT 10",
    "NextToken": "20add42078135EXAMPLE"
}
```

## List all queries on an event data
 store with the AWS CLI


The following example AWS CLI **list-queries** command returns a list of queries and query statuses
 on a specified event data store for the past seven days. You must specify an ARN or
 the ID suffix of an ARN value for `--event-data-store`. Optionally, to
 shorten the list of results, you can specify a time range, formatted as timestamps,
 by adding `--start-time` and `--end-time` parameters, and a
 `--query-status` value. Valid values for `QueryStatus`
 include `QUEUED`, `RUNNING`, `FINISHED`,
 `FAILED`, or `CANCELLED`.


**list-queries** also has optional pagination parameters. Use
 `--max-results` to specify a maximum number of results that you want
 the command to return on a single page. If there are more results than your
 specified `--max-results` value, run the command again adding the
 returned `NextToken` value to get the next page of results.



```
aws cloudtrail list-queries
--event-data-store EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
--query-status CANCELLED
--start-time 1598384589
--end-time 1598384602
--max-results 10
```

**Output**



```
{
    "Queries": [
        {
          "QueryId": "EXAMPLE2-0add-4207-8135-2d8a4EXAMPLE", 
          "QueryStatus": "CANCELLED",
          "CreationTime": 1598911142
        },
        {
          "QueryId": "EXAMPLE2-4e89-9230-2127-5dr3aEXAMPLE", 
          "QueryStatus": "CANCELLED",
          "CreationTime": 1598296624
        }
     ],
    "NextToken": "20add42078135EXAMPLE"
}
```

## Cancel a running query with the AWS CLI


The following example AWS CLI **cancel-query** command cancels a
 query with a status of `RUNNING`. You must specify a value for
 `--query-id`. When you run **cancel-query**, the query
 status might show as `CANCELLED` even if the
 **cancel-query** operation is not yet finished.


###### Note

A canceled query can incur charges. Your account is still charged for the
 amount of data that was scanned before you canceled the query.


The following is a CLI example.



```
aws cloudtrail cancel-query
--query-id EXAMPLEd-17a7-47c3-a9a1-eccf7EXAMPLE
```

**Output**



```
QueryId -> (string)
QueryStatus -> (string)
```
