# Searching an index

###### Note

Feature support varies by index type and search API being used. To see if this feature
is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

To search an Amazon Kendra index, you use the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API. The
`Query` API returns information about the indexed documents that you use in
your application. This section shows you how to make a query, perform filters, and interpret
the response that you get from the `Query` API.

To search documents that you have indexed with Amazon Kendra for Amazon Lex,
use [AMAZON.KendraSearchIntent](../../../lexv2/latest/APIReference/API_KendraConfiguration.md "../../../lexv2/latest/APIReference/API_KendraConfiguration.md"). For an example of configuring Amazon Kendra
with Amazon Lex, see [Creating a FAQ Bot for an Amazon Kendra Index](../../../lexv2/latest/dg/faq-bot-kendra-search.md "../../../lexv2/latest/dg/faq-bot-kendra-search.md").

###### Topics

- [Querying an index](searching-example.md "searching-example.md")
- [Retrieving passages](searching-retrieve.md "searching-retrieve.md")
- [Browsing an index](browsing.md "browsing.md")
- [Featuring search results](featured-results.md "featured-results.md")
- [Tabular search for HTML](searching-tables.md "searching-tables.md")
- [Query suggestions](query-suggestions.md "query-suggestions.md")
- [Query spell checker](query-spell-check.md "query-spell-check.md")
- [Filtering and facet search](filtering.md "filtering.md")
- [Filtering on user context](user-context-filter.md "user-context-filter.md")
- [Query responses and response types](query-responses-types.md "query-responses-types.md")
- [Tuning and sorting responses](tuning-sorting-responses.md "tuning-sorting-responses.md")
- [Collapsing/expanding query
  results](expand-collapse-query-results.md "expand-collapse-query-results.md")
