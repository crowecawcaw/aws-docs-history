# Example CloudTrail log queries

The following example shows a portion of a query that returns all anonymous (unsigned)
requests from the table created for CloudTrail event logs. This query selects those requests
where `useridentity.accountid` is anonymous, and
`useridentity.arn` is not specified:

```
SELECT *
FROM `cloudtrail_logs`
WHERE
    eventsource = 's3.amazonaws.com' AND
    eventname in ('GetObject') AND
    useridentity.accountid = 'anonymous' AND
    useridentity.arn IS NULL AND
    requestparameters LIKE '%[your bucket name ]%';
```

For more information, see the AWS Big Data blog post [Analyze security, compliance, and operational activity using AWS CloudTrail and
Amazon Athena](https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/ "https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/").

## Query nested fields in CloudTrail

logs

Because the `userIdentity` and `resources` fields are nested
data types, querying them requires special treatment.

The `userIdentity` object consists of nested `STRUCT` types.
These can be queried using a dot to separate the fields, as in the following
example:

```
SELECT
    eventsource,
    eventname,
    useridentity.sessioncontext.attributes.creationdate,
    useridentity.sessioncontext.sessionissuer.arn
FROM cloudtrail_logs
WHERE useridentity.sessioncontext.sessionissuer.arn IS NOT NULL
ORDER BY eventsource, eventname
LIMIT 10
```

The `resources` field is an array of `STRUCT` objects. For
these arrays, use `CROSS JOIN UNNEST` to unnest the array so that you can
query its objects.

The following example returns all rows where the resource ARN ends in
`example/datafile.txt`. For readability, the [replace](https://prestodb.io/docs/current/functions/string.html#replace "https://prestodb.io/docs/current/functions/string.html#replace") function removes the initial `arn:aws:s3:::`
substring from the ARN.

```
SELECT
    awsregion,
    replace(unnested.resources_entry.ARN,'arn:aws:s3:::') as s3_resource,
    eventname,
    eventtime,
    useragent
FROM cloudtrail_logs t
CROSS JOIN UNNEST(t.resources) unnested (resources_entry)
WHERE unnested.resources_entry.ARN LIKE '%example/datafile.txt'
ORDER BY eventtime
```

The following example queries for `DeleteBucket` events. The query
extracts the name of the bucket and the account ID to which the bucket belongs from
the `resources` object.

```
SELECT
    awsregion,
    replace(unnested.resources_entry.ARN,'arn:aws:s3:::') as deleted_bucket,
    eventtime AS time_deleted,
    useridentity.username,
    unnested.resources_entry.accountid as bucket_acct_id
FROM cloudtrail_logs t
CROSS JOIN UNNEST(t.resources) unnested (resources_entry)
WHERE eventname = 'DeleteBucket'
ORDER BY eventtime
```

For more information about unnesting, see [Filter arrays](filtering-arrays.md "filtering-arrays.md").

## Tips for querying CloudTrail

logs

Consider the following when exploring CloudTrail log data:

- Before querying the logs, verify that your logs table looks the same as
  the one in [Create a table for CloudTrail logs in Athena using
  manual partitioning](create-cloudtrail-table.md "create-cloudtrail-table.md"). If it is not the first
  table, delete the existing table using the following command: `DROP
TABLE cloudtrail_logs`.
- After you drop the existing table, re-create it. For more information, see
  [Create a table for CloudTrail logs in Athena using
  manual partitioning](create-cloudtrail-table.md "create-cloudtrail-table.md").

Verify that fields in your Athena query are listed correctly. For
information about the full list of fields in a CloudTrail record, see [CloudTrail record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md").

If your query includes fields in JSON formats, such as
`STRUCT`, extract data from JSON. For more information, see [Extract JSON data from strings](extracting-data-from-JSON.md "extracting-data-from-JSON.md").

Some suggestions for issuing queries against your CloudTrail table:

- Start by looking at which users called which API operations and from which
  source IP addresses.
- Use the following basic SQL query as your template. Paste the query to the
  Athena console and run it.

```
SELECT
 useridentity.arn,
 eventname,
 sourceipaddress,
 eventtime
FROM cloudtrail_logs
LIMIT 100;
```

- Modify the query to further explore your data.
- To improve performance, include the `LIMIT` clause to return a
  specified subset of rows.
