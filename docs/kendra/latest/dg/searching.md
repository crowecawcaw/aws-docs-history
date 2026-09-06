

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Searching an index
<a name="searching"></a>

**Note**  
Feature support varies by index type and search API being used. To see if this feature is supported for the index type and search API you’re using, see [Index types](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-types.html).

To search an Amazon Kendra index, you use the [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) API. The `Query` API returns information about the indexed documents that you use in your application. This section shows you how to make a query, perform filters, and interpret the response that you get from the `Query` API.

To search documents that you have indexed with Amazon Kendra for Amazon Lex, use [AMAZON.KendraSearchIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_KendraConfiguration.html). For an example of configuring Amazon Kendra with Amazon Lex, see [Creating a FAQ Bot for an Amazon Kendra Index](https://docs.aws.amazon.com/lexv2/latest/dg/faq-bot-kendra-search.html).

**Topics**
+ [Querying an index](searching-example.md)
+ [Retrieving passages](searching-retrieve.md)
+ [Browsing an index](browsing.md)
+ [Featuring search results](featured-results.md)
+ [Tabular search for HTML](searching-tables.md)
+ [Query suggestions](query-suggestions.md)
+ [Query spell checker](query-spell-check.md)
+ [Filtering and facet search](filtering.md)
+ [Filtering on user context](user-context-filter.md)
+ [Query responses and response types](query-responses-types.md)
+ [Tuning and sorting responses](tuning-sorting-responses.md)
+ [Collapsing/expanding query results](expand-collapse-query-results.md)