# Use natural language to generate and update CloudWatch Metrics Insights queries

CloudWatch supports a natural language query capability to help you generate and update
queries for [CloudWatch
Metrics Insights](query_with_cloudwatch-metrics-insights.md "query_with_cloudwatch-metrics-insights.md") and [CloudWatch Logs Insights](../logs/AnalyzingLogData.md "../logs/AnalyzingLogData.md").

With this capability, you can ask questions about or describe the CloudWatch data you're
looking for in plain English. The natural language capability generates a query based on a
prompt that you enter and provides a line-by-line explanation of how the query works. You
can also update your query to further investigate your data.

Depending on your environment, you can enter prompts like "Which Amazon Elastic Compute Cloud instance has
the highest network out?" and "Show me the top 10 Amazon DynamoDB Tables by consumed reads."

###### Note

The natural-language query feature is generally available in 10 Regions. For some
Regions, the feature makes cross-Region calls to Regions in the United States to process
the query prompts. The following table lists the supported Regions, and shows where each
Region processes its prompts.

| Supported Region         | Region where prompt is processed |
| ------------------------ | -------------------------------- |
| US East (N. Virginia)    | US East (N. Virginia)            |
| US East (Ohio)           | US East (N. Virginia)            |
| US West (Oregon)         | US West (Oregon)                 |
| Asia Pacific (Hong Kong) | US West (Oregon)                 |
| Asia Pacific (Singapore) | US West (Oregon)                 |
| Asia Pacific (Sydney)    | US West (Oregon)                 |
| Asia Pacific (Tokyo)     | Asia Pacific (Tokyo)             |
| Europe (Frankfurt)       | Europe (Frankfurt)               |
| Europe (Ireland)         | US East (N. Virginia)            |
| Europe (Stockholm)       | US East (N. Virginia)            |

To generate a CloudWatch Metrics Insights query with this capability, open the CloudWatch Metrics Insights query editor in the
_builder_ or _editor_
view and choose **Generate query**.

###### Important

To use the natural language query capability, you must use the [CloudWatchFullAccess](../../../aws-managed-policy/latest/reference/CloudWatchFullAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchFullAccess.md"), [CloudWatchReadOnlyAccess](../../../aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.md"), [CloudWatchFullAccessV2](../../../aws-managed-policy/latest/reference/CloudWatchFullAccessV2.md "../../../aws-managed-policy/latest/reference/CloudWatchFullAccessV2.md"), [AdministratorAccess](../../../aws-managed-policy/latest/reference/AdministratorAccess.md "../../../aws-managed-policy/latest/reference/AdministratorAccess.md"), or [ReadOnlyAccess](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md")
policy.

You can also include the `cloudwatch:GenerateQuery` action in a new or
existing customer managed or inline policy.

## Example queries

The examples in this section describe how to generate and update queries using the
natural language capability.

###### Note

For more information on the CloudWatch Metrics Insights query editor and syntax, see [CloudWatch Metrics Insights query components and syntax](cloudwatch-metrics-insights-querylanguage.md "cloudwatch-metrics-insights-querylanguage.md").

### Example: Generate a natural language query

To generate a query using natural language, enter a prompt and choose
**Generate new query**. This example shows a query that performs a
basic search.

###### Prompt

The following is an example of a prompt that directs the capability to search for
the top 10 DynamoDB Tables that consume the most read capacity.

```
Show top 10 DynamoDB Tables by consumed reads
```

###### Query

The following is an example of a query that the natural language capability
generates based on the prompt. Notice how the prompt appears in a comment before the
query. After the query, you can read an explanation that describes how the query
works.

```
# Show top 10 DynamoDB Tables by consumed reads
SELECT SUM("ConsumedReadCapacityUnits")
FROM "AWS/DynamoDB"
GROUP BY TableName
ORDER BY SUM() DESC
LIMIT 10
# This query selects the sum of consumed read capacity units for each DynamoDB table, groups the results by table name, orders the results from highest to lowest read capacity consumption, and limits the results to the top 10 tables.
```

###### Note

To turn off the appearance of your prompt and the explanation of how the query
works, use the gear icon in your editor.

### Example: Update a natural language query

You can update a query by editing the initial prompt and then choosing
**Update query**.

###### Updated prompt

The following example shows an updated version of the previous prompt. Instead of
a prompt that searches for the top 10 DynamoDB Tables that consume the most read
capacity, this prompt now directs the capability to sort the results by the number of
bytes returned.

```
Sort by bytes returned instead
```

###### Updated query

The following is an example of the updated query. Notice how the updated prompt
appears in a comment before the updated query. After the query, you can read an
explanation that describes how the original query has been updated.

```
# Sort by bytes returned instead
SELECT SUM("ReturnedBytes")
FROM "AWS/DynamoDB"
GROUP BY TableName
ORDER BY SUM() DESC
LIMIT 10
# This query modifies the original query to select the sum of returned bytes instead of consumed read capacity units, and orders the results from highest to lowest sum of returned bytes, limiting the results to the top 10 tables.
```

## Opting out of using your data for service improvement

The natural language prompt data you provide to train the AI model and generate
relevant queries is used solely to provide and maintain your service. This data might be
used to improve the quality of CloudWatch Metrics Insights. Your trust and privacy, as well as the security of
your content, is our highest priority. For more information, see [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") and [AWS responsible AI policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/ "https://aws.amazon.com/machine-learning/responsible-ai/policy/").

You can opt out of having your content used to develop or improve the quality of
natural language queries by creating an AI service opt-out policy. To opt-out of data
collection for all CloudWatch AI features, including the query generation capability, you must
create an opt-out policy for CloudWatch. For more information, see [AI services
opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User Guide_.
