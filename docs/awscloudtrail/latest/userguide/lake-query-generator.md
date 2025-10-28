# Create CloudTrail Lake queries from natural language

prompts

You can use the CloudTrail Lake query generator to produce a query from an English language
prompt that you provide. The query generator uses generative artificial intelligence
(generative AI) to produce a ready-to-use SQL query from your prompt, which you can
then choose to run in Lake's query editor, or further fine tune. You don't need to have extensive knowledge of
SQL or CloudTrail event fields to use the query generator.

The prompt can be a question or a statement about the event data
in your CloudTrail Lake event data store. For example, you can enter prompts like "What are my
top errors in the past month?" and “Give me a list of users that used SNS.”

A prompt can have a minimum of 3 characters and a maximum of 500 characters.

There are no charges for generating queries; however, when you run queries, you incur
charges based on the amount of optimized and compressed data scanned. To help control
costs, we recommend that you constrain queries by adding starting and ending
`eventTime` timestamps to queries.

###### Note

You can provide feedback about a generated query by choosing the thumbs up or thumbs down
button that appears below the generated query. When you provide feedback, CloudTrail saves your
prompt and the generated query.

Do not include any personally identifying, confidential, or sensitive information
in your prompts.

This feature uses generative AI large language models (LLMs); we recommend double-checking the
LLM response.

You can access the query generator using the CloudTrail console and AWS CLI.

CloudTrail console

###### To use the query generator on the CloudTrail console

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose
   **Query**.
3. On the **Query** page, choose the
   **Editor** tab.
4. Choose the event data store you want to create a query for.
5. In the **Query generator** area, enter a prompt
   in plain English. For examples, see [Example prompts](#lake-query-generator-examples "#lake-query-generator-examples").
6. Choose **Generate query**. The query generator will attempt to generate
   a query from your prompt. If successful, the query generator provides the SQL query in the editor.
   If the prompt is unsuccessful, rephrase your prompt and try again.
7. (Optional) You can provide feedback about the generated
   query. To provide feedback, choose the thumbs up or thumbs down button that appears below
   the prompt. When you provide feedback, CloudTrail saves your prompt and the generated query.
8. (Optional) Choose **Run** to run the query.

###### Note

When you run queries, you incur charges
based on the amount of optimized and compressed data scanned. To help control costs, we recommend that you
constrain queries by adding starting and ending `eventTime` timestamps to queries. 9. (Optional) If you run the query and there are results, you can choose **Summarize results** to generate a natural language summary in English of the query results. This option uses
generative artificial intelligence (generative AI) to produce the summary. For more information about this option, see [Summarize query results in natural language](query-results-summary.md "query-results-summary.md").

You can provide feedback about the summary by choosing the thumbs up or thumbs down
button that appears below the generated summary.

###### Note

The query summarization feature is in preview release for
CloudTrail Lake and is subject to change. This feature is available in the following regions: Asia Pacific (Tokyo), US East (N. Virginia), and US West (Oregon).

AWS CLI
**To generate a query with the AWS CLI**

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

**To run a query with the AWS CLI**

Run the `start-query` command with the `QueryAlias`
outputted by the `generate-query` command in the previous
example. You also have the option of running the `start-query` command by providing the `QueryStatement`.

```
aws cloudtrail start-query --query-alias `AWSCloudTrail-UUID`
```

The response is a `QueryId` string. To get the status
of a query, run `describe-query` using the
`QueryId` value returned by `start-query`.
If the query is successful, you can run
`get-query-results` to get results.

```
{
    "QueryId": "EXAMPLE2-0add-4207-8135-2d8a4EXAMPLE"
}
```

###### Note

Queries that run for longer than one hour might time out. You
can still get partial results that were processed before the
query timed out.

If you are delivering the query results to an S3 bucket using
the optional `--delivery-s3uri` parameter, the bucket
policy must grant CloudTrail permission to delivery query results to
the bucket. For information about manually editing the bucket
policy, see [Amazon S3 bucket policy for CloudTrail Lake query results](s3-bucket-policy-lake-query-results.md "s3-bucket-policy-lake-query-results.md").

## Required permissions

The [`AWSCloudTrail_FullAccess`](../../../aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.md "../../../aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.md")
and [`AdministratorAccess`](../../../aws-managed-policy/latest/reference/AdministratorAccess.md "../../../aws-managed-policy/latest/reference/AdministratorAccess.md") managed policies both provide the
necessary permissions to use this feature.

You can also include the `cloudtrail:GenerateQuery` action in a new or existing customer managed or inline policy.

## Region support

This feature is supported in the following AWS Regions:

- Asia Pacific (Mumbai) Region (ap-south-1)
- Asia Pacific (Sydney) Region (ap-southeast-2)
- Asia Pacific (Tokyo) Region (ap-northeast-1)
- Canada (Central) Region (ca-central-1)
- Europe (London) Region (eu-west-2)
- US East (N. Virginia) Region (us-east-1)
- US West (Oregon) Region (us-west-2)

## Limitations

The following are limitations of the query generator:

- The query generator can only accept prompts in English.
- The query generator can only generate queries for event data stores that
  collect CloudTrail events (management events, data events, network activity
  events).
- The query generator cannot generate queries for prompts that do not
  pertain to CloudTrail Lake event data.

## Example prompts

This section provides example prompts and the resulting SQL queries generated from
the prompts.

If you choose to run
the example queries in this section, replace `eds-id` with the ID of the
event data store that you want to query and replace the timestamps with the
appropriate timestamps for your use case. Timestamps have the following format:
`YYYY-MM-DD HH:MM:SS`.

**Prompt:** What are my top errors in the past
month?

**SQL query:**

```
SELECT
    errorMessage,
    COUNT(*) as eventCount
FROM
    `eds-id`
WHERE
    errorMessage IS NOT NULL
AND eventTime >= timestamp '`2024-05-01 00:00:00`'
AND eventTime <= timestamp '`2024-05-31 23:59:59`'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 2;
```

**Prompt:**
Give me a list of users that used Amazon SNS.

**SQL query:**

```
SELECT
    DISTINCT userIdentity.arn AS user
FROM
    `eds-id`
WHERE
    eventSource = 'sns.amazonaws.com'
```

**Prompt:** What are my API counts each day for read
and write events in the past month?

**SQL query:**

```
SELECT date(eventTime) AS event_date,
    SUM(
        CASE
            WHEN readonly = true THEN 1
            ELSE 0
        END
    ) AS read_events,
    SUM(
        CASE
            WHEN readonly = false THEN 1
            ELSE 0
        END
    ) AS write_events
FROM
    `eds-id`
WHERE
    eventTime >= timestamp '`2024-05-04 00:00:00`'
AND eventTime <= timestamp '`2024-06-04 23:59:59`'
GROUP BY 1
ORDER BY 1 ASC;
```

**Prompt:** Show any events with access denied errors for the past three weeks.

**SQL query:**

```
SELECT *
FROM
  `eds-id`
WHERE
  WHERE (errorCode = 'AccessDenied' OR errorMessage = 'Access Denied')
AND eventTime >= timestamp '`2024-05-16 01:00:00`'
AND eventTime <= timestamp '`2024-06-06 01:00:00`'
```

**Prompt:**
Query the number of calls each operator performed on the date
2024-05-01. The operator is a principal tag.

**SQL query:**

```
SELECT element_at(
        eventContext.tagContext.principalTags,
        'operator'
    ) AS operator,
    COUNT(*) AS eventCount
FROM
    `eds-id`
WHERE eventtime >= '2024-05-01 00:00:00'
    AND eventtime < '2024-05-01 23:59:59'
GROUP BY 1
ORDER BY 2 DESC;
```

**Prompt:**
Give me all event IDs that touched resources within the AWS CloudFormation stack with name
myStack on the date 2024-05-01.

**SQL query:**

```
SELECT eventID
FROM
    `eds-id`
WHERE any_match(
        eventContext.tagcontext.resourcetags,
        rt->element_at(rt.tags, 'aws:cloudformation:stack-name') = 'myStack'
    )
    AND eventtime >= '2024-05-01 00:00:00'
    AND eventtime < '2024-05-01 23:59:59'
```

**Prompt:**
Count the number of events grouped by resource tag
'solution' values, listing them in descending order of
count.

**SQL query:**

```
SELECT element_at(rt.tags, 'solution'),
    count(*) as event_count
FROM
    `eds-id`,
    unnest(eventContext.tagContext.resourceTags) as rt
WHERE eventtime < '2025-05-14 19:00:00'
GROUP BY 1
ORDER BY 2 DESC;
```

**Prompt:**
Find all Amazon S3 data events where resource tag Environment has value
prod.

**SQL query:**

```
SELECT *
FROM
    `eds-id`
WHERE eventCategory = 'Data'
    AND eventSource = 's3.amazonaws.com'
    AND eventtime >= '2025-05-14 00:00:00'
    AND eventtime < '2025-05-14 20:00:00'
    AND any_match(
        eventContext.tagContext.resourceTags,
        rt->element_at(rt.tags, 'Environment') = 'prod'
    )
```
