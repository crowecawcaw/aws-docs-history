

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Index types in Amazon Kendra
<a name="hiw-index-types"></a>

Amazon Kendra has three index types: GenAI Enterprise Edition index, Enterprise Edition index, and Developer Edition index. The following sections describe the features of each index.

**Topics**
+ [Amazon Kendra GenAI Enterprise Edition index](#kendra-gen-ai-index)
+ [Amazon Kendra Enterprise Edition index](#kendra-enterprise-index)
+ [Amazon Kendra Developer Edition index](#kendra-developer-index)

## Amazon Kendra GenAI Enterprise Edition index
<a name="kendra-gen-ai-index"></a>

An Amazon Kendra GenAI Enterprise Edition index offers the highest accuracy for the Retrieve API operation and for Retrieval Augmented Generation (RAG) use cases. It's powered by the latest information retrieval technologies—like hybrid search (keyword and vector), semantic embedding, and re-ranker models—and has been tested across a variety of datasets. The Query API operation offers similar accuracy for an Amazon Kendra GenAI Enterprise Edition index when compared with Amazon Kendra Developer Edition and Amazon Kendra Enterprise Edition indexes.

An Amazon Kendra GenAI Enterprise Edition index enables mobility of your indexed data across AWS generative AI services. With this functionality, you can seamlessly reuse your investments without having to rebuild indexes. You can use it in an [Amazon Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) as a managed retriever, and integrate it with Amazon Bedrock tools like agents and prompt flows to build advanced AI assistants. You can also use it with [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) for a fully managed digital assistant.

An Amazon Kendra GenAI Enterprise Edition index offers smaller, more granular capacity units and a lower starting price compared to the other two index types. This helps you to be more efficient with your capacity utilization.

**Note**  
For the best experience and accuracy, we recommend that you choose an Amazon Kendra GenAI Enterprise Edition index.

**Topics**
+ [Supported features](#kendra-gen-ai-index-features)
+ [Limitations](#genai-index-limitations)

### Supported features
<a name="kendra-gen-ai-index-features"></a>

The following features are supported for an Amazon Kendra GenAI Enterprise Edition index if you're using the [Retrieve](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) API operation for RAG use cases:
+ **Full support** – [Confidence score buckets](https://docs.aws.amazon.com/kendra/latest/APIReference/API_QueryResultItem.html#Kendra-Type-QueryResultItem-ScoreAttributes), [filtering](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html), [faceting](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-facets), [relevance tuning](https://docs.aws.amazon.com/kendra/latest/dg/tuning.html), [custom document enrichment](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html), [custom metadata](https://docs.aws.amazon.com/kendra/latest/dg/custom-attributes.html), and [adjusting query capacity and document capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html).
+ **Partial support** – [Data source connectors](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html) and [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html). For more information on partially supported features, see [Limitations](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-types.html#genai-index-limitations).

The following features are supported for an Amazon Kendra GenAI Enterprise Edition index if you're using the [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) API operation for search use cases:
+ **Full support** – [Document ranking](https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html), [extractive question answering](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html), [confidence score buckets](https://docs.aws.amazon.com/kendra/latest/APIReference/API_QueryResultItem.html#Kendra-Type-QueryResultItem-ScoreAttributes), [filtering](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html), [faceting](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-facets), [sorting](https://docs.aws.amazon.com/kendra/latest/dg/tuning-sorting-responses.html#sorting-responses), [collapsing and expanding query results](https://docs.aws.amazon.com/kendra/latest/dg/expand-collapse-query-results.html), [index browsing](https://docs.aws.amazon.com/kendra/latest/dg/browsing.html), [Boolean queries](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax), [exact match](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax), [wildcard queries](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax), [query suggestions](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html), [query spell checker](https://docs.aws.amazon.com/kendra/latest/dg/query-spell-check.html), [relevance tuning](https://docs.aws.amazon.com/kendra/latest/dg/tuning.html), [incremental learning](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html), [custom document enrichment](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html), [custom metadata](https://docs.aws.amazon.com/kendra/latest/dg/custom-attributes.html), [adjusting query capacity and document capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html), and [search experience](https://docs.aws.amazon.com/kendra/latest/dg/deploying.html).
+ **Partial support** – [Data source connectors](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html) and [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html). For more information on partially supported features, see [Limitations](https://docs.aws.amazon.com/kendra/latest/dg/hiw-index-types.html#kendra-gen-ai-index).

### Limitations
<a name="genai-index-limitations"></a>

The following outlines the known limitations of an Amazon Kendra GenAI Enterprise Edition index:
+ Amazon Kendra GenAI Enterprise Edition indexes are only available in US East (N. Virginia) and US West (Oregon).
+ Amazon Kendra GenAI Enterprise Edition indexes only support English language content.
+ Amazon Kendra GenAI Enterprise Edition indexes support only v2.0 Amazon Kendra data source connectors.
+ In an Amazon Kendra GenAI Enterprise Edition index, you can only use [user attributes](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html#context-filter-attribute) to filter search results by user context.
+ Amazon Kendra GenAI Enterprise Edition indexes don't support [token-based user access control](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control.html) or [user ID and group –based user access control](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html#context-filter-user-incl-datasources) to documents.
+ The [CreateAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateAccessControlConfiguration.html) API operation is disabled for Amazon Kendra GenAI Enterprise Edition indexes.
+ If you're using an Amazon Kendra GenAI Enterprise Edition index with Amazon Q Business, note the following about controlling end-user access to documents:

  Amazon Q Business uses user email ID to determine end-user access to documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to enable document filtering for end users. If data sources connected to your Amazon Kendra index don’t use email ID–based document filtering, or the email ID is not present, Amazon Q Business generates responses only from public documents.

## Amazon Kendra Enterprise Edition index
<a name="kendra-enterprise-index"></a>

An Amazon Kendra Enterprise Edition index provides semantic search capabilities, and offers a high-availability service that is suitable for production workloads.

**Topics**
+ [Supported features](#kendra-ent-index-features)
+ [Limitations](#ent-index-limitations)

### Supported features
<a name="kendra-ent-index-features"></a>

The following features are supported for an Amazon Kendra Enterprise Edition index if you're using the [Retrieve](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) API operation for RAG use cases: querying using [advance query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax), [suggested spell corrections](https://docs.aws.amazon.com/kendra/latest/dg/query-spell-check.html) for queries, [faceting](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-facets), [query suggestions](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html) to autocomplete search queries, and [incremental learning](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html).

All features are supported for an Amazon Kendra Enterprise Edition index if you're using the [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) API operation for search use cases.

### Limitations
<a name="ent-index-limitations"></a>

The following outlines the known limitations of an Amazon Kendra Enterprise Edition index:
+ If you're using an Amazon Kendra Enterprise Edition index with Amazon Q Business, note the following about controlling end-user access to documents:

  Amazon Q Business uses user email ID to determine end-user access to documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to enable document filtering for end users. If data sources connected to your Amazon Kendra index don’t use email ID–based document filtering, or the email ID is not present, Amazon Q Business generates responses only from public documents.

## Amazon Kendra Developer Edition index
<a name="kendra-developer-index"></a>

An Amazon Kendra Developer Edition index also provides semantic search capabilities for you to test your use cases. However, we don't recommend it for production use cases.

**Topics**
+ [Supported features](#kendra-dev-index-features)
+ [Limitations](#dev-index-limitations)

### Supported features
<a name="kendra-dev-index-features"></a>

The following features are supported for an Amazon Kendra Developer Edition index if you're using the [Retrieve](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) API operation for RAG use cases: querying using [advance query syntax](https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax), [suggested spell corrections](https://docs.aws.amazon.com/kendra/latest/dg/query-spell-check.html) for queries, [faceting](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-facets), [query suggestions](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html) to autocomplete search queries, and [incremental learning](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html).

All features are supported for an Amazon Kendra Developer Edition index if you're using the [Query](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) API operation for search use cases.

### Limitations
<a name="dev-index-limitations"></a>

The following outlines the known limitations of an Amazon Kendra Developer Edition index:
+ If you're using an Amazon Kendra Developer Edition index with Amazon Q Business, note the following about controlling end-user access to documents:

  Amazon Q Business uses user email ID to determine end-user access to documents in an index. When you connect an Amazon Kendra index to Amazon Q Business, Amazon Q Business relays the user’s identifying email ID to Amazon Kendra to enable document filtering for end users. If data sources connected to your Amazon Kendra index don’t use email ID–based document filtering, or the email ID is not present, Amazon Q Business generates responses only from public documents.