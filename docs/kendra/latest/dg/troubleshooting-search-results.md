# Troubleshooting document search

results

This section can help you fix issues in your Amazon Kendra search results.

## My search

results are not relevant to my search query

If your search results seem irrelevant, it might be for the following
reasons:

- Results with `LOW` confidence are included in the results. You
  can filter out results with `LOW` confidence by using the [QueryResultItem](../APIReference/API_QueryResultItem.md "../APIReference/API_QueryResultItem.md")'s `ScoreAttributes` field to exclude
  any result with a value of `LOW`. Amazon Kendra assigns each
  result a confidence bucket value of either `VERY_HIGH`,
  `HIGH`, `MEDIUM` and `LOW`. These
  values indicate the level of confidence that a result is relevant to a
  query. Also, irrespective of confidence buckets, Amazon Kendra returns
  three types of results in the following order: `ANSWER`
  (suggested answer excerpt), `QUESTION_ANSWER` (FAQ) and
  `DOCUMENT` (document excerpt). Therefore, it is possible for
  a `LOW` confidence `QUESTION_ANSWER` result to be
  positioned above a `VERY_HIGH` confidence `DOCUMENT`
  result. However, it isn't always necessarily true that `LOW`
  confidence `QUESTION_ANSWER` is a better result than the
  `VERY_HIGH` confidence `DOCUMENT`.
- Certain metadata fields or attributes are boosted to a very high value,
  affecting the ranking of results. Amazon Kendra searches your index
  using multiple parameters such as document title, text, date, and custom
  text fields or attributes. You can experiment with different boosting values
  to get the best results across all queries. You can also use dynamic [relevance
  tuning](tuning.md "tuning.md") at the query level to use different boosting values for
  each query.
- Your users are using specialized terms when they query for information and
  there's no custom synonyms set up for your index to handle these specialized
  terms. For more details on how and when to use synonyms, see [Adding
  custom synonyms to an index](index-synonyms.md "index-synonyms.md").

## Why do I

only see 100 results?

Amazon Kendra returns the total count of relevant documents. The top 100 are
returned per query by default. The results are paginated. You can use
`PageNumber` to access different pages.

You can configure Amazon Kendra to return up to 1,000 documents or search
results per query, with up to 100 results per page. To return more than 100 results,
you can request this by contacting [Quotas
Support](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). Increasing the number of search results could impact
latency.

## Why

are documents that I expect to see missing?

Amazon Kendra supports access control lists (ACLs) based on user and groups.
Amazon Kendra ingests ACL policies via connectors. If an index does not
configure an ACL, only documents matching the attribute filter for user and group
will be shown. If a user or group attribute filter is provided, documents without an
ACL will not be shown.

If you are using token-based access control, documents without an ACL policy and
documents that match the user and groups will be shown.

## Why do I see

documents that have an ACL policy?

If an index does not configure an access control policy, then user and groups can
be provided by the filter. If no user and group filter is applied, then all related
documents will be returned. Any ACL policy will be ignored.
