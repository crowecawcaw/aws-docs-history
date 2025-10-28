# Using APIs for analytics

This section describes the API operations that you use to retrieve analytics for a
bot.

###### Note

To use the [ListUtteranceMetrics](../APIReference/API_ListUtteranceMetrics.md "../APIReference/API_ListUtteranceMetrics.md") and [ListUtteranceAnalyticsData](../APIReference/API_ListUtteranceAnalyticsData.md "../APIReference/API_ListUtteranceAnalyticsData.md"), your IAM role must have permissions to perform the [ListAggregatedUtterances](../APIReference/API_ListAggregatedUtterances.md "../APIReference/API_ListAggregatedUtterances.md") operation, which provides access to utterance-related analytics. See [Viewing utterance statistics from Lex V2 conversations](#monitoring-utterances "#monitoring-utterances") for details and the IAM policy to apply to the IAM role.

- The following API operations retrieve summary metrics for a bot:
  - [ListSessionMetrics](../APIReference/API_ListSessionMetrics.md "../APIReference/API_ListSessionMetrics.md")
  - [ListIntentMetrics](../APIReference/API_ListIntentMetrics.md "../APIReference/API_ListIntentMetrics.md")
  - [ListIntentStageMetrics](../APIReference/API_ListIntentStageMetrics.md "../APIReference/API_ListIntentStageMetrics.md")
  - [ListUtteranceMetrics](../APIReference/API_ListUtteranceMetrics.md "../APIReference/API_ListUtteranceMetrics.md")

- The following API operations retrieve a list of metadata for sessions and utterances:
  - [ListSessionAnalyticsData](../APIReference/API_ListSessionAnalyticsData.md "../APIReference/API_ListSessionAnalyticsData.md")
  - [ListUtteranceAnalyticsData](../APIReference/API_ListUtteranceAnalyticsData.md "../APIReference/API_ListUtteranceAnalyticsData.md")

- The [ListIntentPaths](../APIReference/API_ListIntentPaths.md "../APIReference/API_ListIntentPaths.md") operation retrieves metrics about an order of intents that customers take in conversations with a bot.

## Filtering results

The Analytics API requests require you to specify the `startTime` and
`endTime`. The API returns sessions, intents, intent stages, or
utterances that began _after_ the `startTime` and
ended _before_ the `endTime`.

`filters` is an optional field in the Analytics API requests. It maps
to a list of [AnalyticsSessionFilter](../APIReference/API_AnalyticsSessionFilter.md "../APIReference/API_AnalyticsSessionFilter.md"), [AnalyticsIntentFilter](../APIReference/API_AnalyticsIntentFilter.md "../APIReference/API_AnalyticsIntentFilter.md"), [AnalyticsIntentStageFilter](../APIReference/API_AnalyticsIntentStageFilter.md "../APIReference/API_AnalyticsIntentStageFilter.md"), or [AnalyticsUtteranceFilter](../APIReference/API_AnalyticsUtteranceFilter.md "../APIReference/API_AnalyticsUtteranceFilter.md") objects. In each object, use the fields to
create an expression to filter by. For example, if you add the following filter to
the list, the bot searches for conversations that are longer than 30
seconds.

```
{
    "name": "Duration",
    "operator": "GT",
    "value": "30 sec",
}
```

## Retrieving metrics for a bot

Use the `ListSessionMetrics`, `ListIntentMetrics`,
`ListIntentStageMetrics`, and `ListUtteranceMetrics`
operations to retrieve summary metrics for _sessions_,
_intents_, _intent stages_, and
_utterances_.

For these operations, fill in the following required fields:

- Provide a `startTime` and `endTime` to define a time range for which you want to retrieve results.
- Specify the metrics you want to calculate in `metrics`, a list
  of [AnalyticsSessionMetric](../APIReference/API_AnalyticsSessionMetric.md "../APIReference/API_AnalyticsSessionMetric.md"), [AnalyticsIntentMetric](../APIReference/API_AnalyticsIntentMetric.md "../APIReference/API_AnalyticsIntentMetric.md"), [AnalyticsIntentStageMetric](../APIReference/API_AnalyticsIntentStageMetric.md "../APIReference/API_AnalyticsIntentStageMetric.md"), or [AnalyticsUtteranceMetric](../APIReference/API_AnalyticsUtteranceMetric.md "../APIReference/API_AnalyticsUtteranceMetric.md") objects. In each object, use the
  `name` field to specify the metric to
  calculate
  the `statistic` field to specify whether to calculate the
  `Sum`, `Average`, or `Max` number, and
  the `order` field to specify whether to sort the results in
  `Ascending` or `Descending` order.

###### Note

Both the `metrics` and `binBy` objects contain an `order` field. You can specify the sorting `order` in only one of the two objects.

The remaining fields in the request are optional. You can filter and organize the results in the following ways:

- **Filtering results** – Use the `filters` field to filter the results. See [Filtering results](#analytics-api-filters "#analytics-api-filters") for more details.
- **Grouping results by category** – Specify the `groupBy` field, a list containing a single [AnalyticsSessionResult](../APIReference/API_AnalyticsSessionResult.md "../APIReference/API_AnalyticsSessionResult.md"), [AnalyticsIntentResult](../APIReference/API_AnalyticsIntentResult.md "../APIReference/API_AnalyticsIntentResult.md"), [AnalyticsIntentStageResult](../APIReference/API_AnalyticsIntentStageResult.md "../APIReference/API_AnalyticsIntentStageResult.md"), or [AnalyticsUtteranceResult](../APIReference/API_AnalyticsUtteranceResult.md "../APIReference/API_AnalyticsUtteranceResult.md") object. In the object, specify the `name` field with the category by which you want to group the results.

If you specify a `groupBy` field in the request, the `results` object in the response contains `groupByKeys`, a list of [AnalyticsSessionGroupByKey](../APIReference/API_AnalyticsSessionGroupByKey.md "../APIReference/API_AnalyticsSessionGroupByKey.md"), [AnalyticsIntentGroupByKey](../APIReference/API_AnalyticsIntentGroupByKey.md "../APIReference/API_AnalyticsIntentGroupByKey.md"), [AnalyticsIntentStageGroupByKey](../APIReference/API_AnalyticsIntentStageGroupByKey.md "../APIReference/API_AnalyticsIntentStageGroupByKey.md"), or [AnalyticsUtteranceGroupByKey](../APIReference/API_AnalyticsUtteranceGroupByKey.md "../APIReference/API_AnalyticsUtteranceGroupByKey.md") objects, each with the `name` that you specified in the request and a member of that category in the `value` field.

- **Binning results by time** – Specify the `binBy` field, a list containing a single [AnalyticsBinBySpecification](../APIReference/API_AnalyticsBinBySpecification.md "../APIReference/API_AnalyticsBinBySpecification.md") object. In the object, specify the `name` field with `ConversationStartTime` to bin the results by when the conversation began or `UtteranceTimestamp` to bin the results by when the utterance took place. Specify the interval of time by which you want to bin the results in the `interval` field, and whether to sort in `Ascending` or `Descending` order of time in the `order` field.

If you specify a `binBy` field in the request, the `results` object in the response contains `binKeys`, a list of [AnalyticsBinKey](../APIReference/API_AnalyticsBinKey.md "../APIReference/API_AnalyticsBinKey.md") objects, each with the `name` that you specified in the request and the interval of time that defines that bin in the `value` field.

###### Note

Both the `metrics` and `binBy` objects contain an `order` field. You can specify the sorting `order` in only one of the two objects.

Use the following fields to handle the display of the response:

- Specify a number between 1 and 1,000 in the `maxResults` field
  to limit the number of results to return in a single response.
- If the number of results is greater than the number you specify in the `maxResults` field, the response contains a `nextToken`. Make the request again, but use this value in the `nextToken` field to return the next batch of results.

If you are using `ListUtteranceMetrics`, you can specify attributes to return in the `attributes` field.
This field maps to a list containing a single [AnalyticsUtteranceAttribute](../APIReference/API_AnalyticsUtteranceAttribute.md "../APIReference/API_AnalyticsUtteranceAttribute.md")
object. Specify `LastUsedIntent` in the `name` field to return the intent that Amazon Lex V2 is using at the time of the utterance.

In the response, the `results` field maps to a list of [AnalyticsSessionResult](../APIReference/API_AnalyticsSessionResult.md "../APIReference/API_AnalyticsSessionResult.md"), [AnalyticsIntentResult](../APIReference/API_AnalyticsIntentResult.md "../APIReference/API_AnalyticsIntentResult.md"), [AnalyticsIntentStageResult](../APIReference/API_AnalyticsIntentStageResult.md "../APIReference/API_AnalyticsIntentStageResult.md"), or [AnalyticsUtteranceResult](../APIReference/API_AnalyticsUtteranceResult.md "../APIReference/API_AnalyticsUtteranceResult.md") objects. Each object contains a
`metrics` field which returns the value of a summary statistic for a
metric that you requested, in addition to any bins or groups created from the
methods you specified.

## Retrieving metadata for sessions and utterances in a bot

Use the [ListSessionAnalyticsData](../APIReference/API_ListSessionAnalyticsData.md "../APIReference/API_ListSessionAnalyticsData.md") and [ListUtteranceAnalyticsData](../APIReference/API_ListUtteranceAnalyticsData.md "../APIReference/API_ListUtteranceAnalyticsData.md") operations to retrieve metadata about individual sessions and utterances.

Fill in the required `startTime` and `endTime` fields to define a time range for which you want to retrieve results.

The remaining fields in the request are optional. To filter and sort results:

- **Filtering results** – Use the `filters` field to filter the results. See [Filtering results](#analytics-api-filters "#analytics-api-filters") for more details.
- **Sorting results** – Sort the results with the `sortBy` field, which contains a [SessionDataSortBy](../APIReference/API_SessionDataSortBy.md "../APIReference/API_SessionDataSortBy.md") or [UtteranceDataSortBy](../APIReference/API_UtteranceDataSortBy.md "../APIReference/API_UtteranceDataSortBy.md") object. Specify the value you want to sort by in the `name` field and whether to sort in `Ascending` or `Descending` order in the `order` field.

Use the following fields to handle the display of the response:

- Specify a number between 1 and 1,000 in the `maxResults` field to limit the number of results to return in a single response.
- If the number of results is greater than the number you specify in the `maxResults` field, the response contains a `nextToken`. Make the request again, but use this value in the `nextToken` field to return the next batch of results.

In the response, the `sessions` or `utterances` field maps to a list of [SessionSpecification](../APIReference/API_SessionSpecification.md "../APIReference/API_SessionSpecification.md") or [UtteranceSpecification](../APIReference/API_UtteranceSpecification.md "../APIReference/API_UtteranceSpecification.md") objects. Each object contains metadata for a single session or utterance.

## Retrieving intent path analytics data

Use the [ListIntentPaths](../APIReference/API_ListIntentPaths.md "../APIReference/API_ListIntentPaths.md") operation to retrieve metrics about an order of intents that customers take in conversation with a bot.

For this operation, fill in the following required fields:

- Provide a `startTime` and `endTime` to define a time range for which you want to retrieve results.
- Provide an `intentPath` to define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the `intentPath` field with `/BookCar/BookHotel` to see details about how many times users invoked the `BookCar` and `BookHotel` intents in that order.

Use the optional `filters` field to filter the results. For more
details, see [Filtering results](#analytics-api-filters "#analytics-api-filters").

## Viewing utterance statistics from Lex V2 conversations

You can use utterance statistics to determine the utterances that your users are sending to
your bot. You can see both the utterances that Amazon Lex V2 successfully detects and the utterances
that it doesn't. You can use this information to help tune your bot.

For example, if you find that your users are sending an utterance that
Amazon Lex V2 is missing, you can add the utterance to an intent. The Draft version
of the intent is updated with the new utterance and you can test it before
deploying it to your bot.

An utterance is detected when Amazon Lex V2 recognizes the utterance as an
attempt to invoke an intent configured for a bot. An utterance is missed
when Amazon Lex V2 doesn't recognize the utterance and invokes the
`AMAZON.FallbackIntent` instead.

Utterance statistics can be viewed using the `ListUtteranceMetrics`
API and the `ListAggregatedUtterance` API.

Utterance statistics are not generated using `ListUtteranceMetrics` API
under the following conditions:

- The Child Online Privacy Protection Act setting was set to
  **Yes** when the bot was created with the console, or
  the `childDirected` field was set to true when the bot was
  created withe the `CreateBot` operation.

The `ListUtteranceMetrics` API provides additonal features including:

- More information available, such as mapped intent for detected utterances.
- More filtering capability (including channel and mode).
- Longer retention date range (30 days).
- You can use the API even if you have opted out of data storage. The console
  functionality for missed and detected utterances will rely
  on `ListUtteranceMetrics` API.

Utterance statistics are not generated using `ListAggregatedUtterance` API
under the following conditions:

- The Child Online Privacy Protection Act setting was set to
  **Yes** when the bot was created with the console, or
  the `childDirected` field was set to true when the bot was
  created withe the `CreateBot` operation.
- You are using slot obfuscation with one or more slots.
- You opted out of participating in improving Amazon Lex.

The `ListAggregatedUtterance` API provides features including:

- Less detailed information available (no mapped intent for utterances).
- Limited filtering capability (not including channel and mode).
- Short retention date range (15 days).

Using utterance statistics, you can see whether a specific utterance was detected or missed,
alongside the last time that the utterance was used in a bot interaction.

Amazon Lex V2 stores utterances continuously while users interact with your bot. You can query the
statistics using the console or the `ListAggregatedUtterances` operation. It has a
data retention of 15 days and it is not available if the user has opted out of data storage. You
can delete utterances using the `DeleteUtterances` operation or by opting out of data
storage. All utterances are deleted if you close your AWS account. Stored utterances are
encrypted with a server-managed key.

When you delete a bot version, utterance statistics are available for the version for up to
30 days with `ListUtteranceMetrics`, and 15 days using `ListAggregatedUtterances`.
You can't see statistics for deleted version in the Amazon Lex V2 console. To see the
statistics for deleted versions, you can use both `ListAggregatedUtterances`
and `ListUtteranceMetrics`operations.

With both the `ListAggregatedUtterances`
and `ListUtteranceMetrics` APIs, utterances are aggregated by the text of the utterance. For example, all
instances where the customer used the phrase "I want to order a pizza" are
aggregated into the same line in a response. When you use the
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md") operation, the text used
is the input transcript.

To use the `ListAggregatedUtterances`
and `ListUtteranceMetrics` APIs, apply the following policy to a
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAggregatedUtterancesPolicy",
 "Effect": "Allow",
 "Action": "lex:ListAggregatedUtterances",
 "Resource": "*"
 }
 ]
}`

```
