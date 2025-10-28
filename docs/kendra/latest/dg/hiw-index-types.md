# Index types in Amazon Kendra

Amazon Kendra has three index types: GenAI Enterprise Edition index,
Enterprise Edition index, and Developer Edition index. The following sections
describe the features of each index.

###### Topics

- [Amazon Kendra GenAI Enterprise Edition
  index](#kendra-gen-ai-index "#kendra-gen-ai-index")
- [Amazon Kendra Enterprise Edition index](#kendra-enterprise-index "#kendra-enterprise-index")
- [Amazon Kendra Developer Edition index](#kendra-developer-index "#kendra-developer-index")

## Amazon Kendra GenAI Enterprise Edition

index

An
Amazon Kendra
GenAI Enterprise Edition index offers the highest accuracy
for the Retrieve
API
operation and for
Retrieval
Augmented Generation (RAG) use cases. It's powered by the latest information
retrieval technologies—like hybrid search (keyword and vector), semantic
embedding, and re-ranker models—and has been tested across a variety of
datasets.
The Query API operation offers similar accuracy for an Amazon Kendra GenAI Enterprise
Edition index when compared with Amazon Kendra Developer Edition and Amazon Kendra Enterprise
Edition indexes.

An Amazon Kendra GenAI Enterprise Edition index enables mobility of your indexed data
across AWS generative AI services. With this functionality, you can seamlessly
reuse your investments without having to rebuild indexes. You can use it in an
[Amazon Bedrock knowledge base](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") as a managed retriever, and
integrate it with Amazon Bedrock tools like agents and prompt flows to build advanced AI
assistants. You can also use it with [Amazon Q Business](../../../amazonq/latest/qbusiness-ug/what-is.md "../../../amazonq/latest/qbusiness-ug/what-is.md") for a fully managed digital assistant.

An Amazon Kendra GenAI Enterprise Edition index offers smaller, more granular capacity
units and a lower starting price compared to the
other
two index types. This helps you to be more efficient with
your capacity utilization.

###### Note

For the best experience and accuracy, we recommend that you choose an
Amazon Kendra GenAI Enterprise Edition index.

###### Topics

- [Supported
  features](#kendra-gen-ai-index-features "#kendra-gen-ai-index-features")
- [Limitations](#genai-index-limitations "#genai-index-limitations")

### Supported

features

The following features are supported for an Amazon Kendra GenAI Enterprise Edition
index if you're using the [Retrieve](../APIReference/API_Retrieve.md "../APIReference/API_Retrieve.md") API
operation for RAG use cases:

- **Full support** – [Confidence score buckets](../APIReference/API_QueryResultItem.md#Kendra-Type-QueryResultItem-ScoreAttributes "../APIReference/API_QueryResultItem.md#Kendra-Type-QueryResultItem-ScoreAttributes"), [filtering](filtering.md "filtering.md"), [faceting](filtering.md#search-facets "filtering.md#search-facets"), [relevance tuning](tuning.md "tuning.md"), [custom document enrichment](custom-document-enrichment.md "custom-document-enrichment.md"), [custom metadata](custom-attributes.md "custom-attributes.md"), and [adjusting query capacity and document
  capacity](adjusting-capacity.md "adjusting-capacity.md").
- **Partial support** – [Data source connectors](data-source.md "data-source.md") and [user context filtering](user-context-filter.md "user-context-filter.md"). For more
  information on partially supported features, see [Limitations](hiw-index-types.md#genai-index-limitations "hiw-index-types.md#genai-index-limitations").

The following features are supported for an Amazon Kendra GenAI Enterprise Edition
index if you're using the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API
operation for search use cases:

- **Full support** – [Document ranking](search-service-rerank.md "search-service-rerank.md"), [extractive question answering](searching-example.md "searching-example.md"),
  [confidence score buckets](../APIReference/API_QueryResultItem.md#Kendra-Type-QueryResultItem-ScoreAttributes "../APIReference/API_QueryResultItem.md#Kendra-Type-QueryResultItem-ScoreAttributes"), [filtering](filtering.md "filtering.md"), [faceting](filtering.md#search-facets "filtering.md#search-facets"), [sorting](tuning-sorting-responses.md#sorting-responses "tuning-sorting-responses.md#sorting-responses"), [collapsing and expanding query
  results](expand-collapse-query-results.md "expand-collapse-query-results.md"), [index browsing](browsing.md "browsing.md"), [Boolean queries](searching-example.md#searching-index-query-syntax "searching-example.md#searching-index-query-syntax"), [exact match](searching-example.md#searching-index-query-syntax "searching-example.md#searching-index-query-syntax"), [wildcard queries](searching-example.md#searching-index-query-syntax "searching-example.md#searching-index-query-syntax"), [query
  suggestions](query-suggestions.md "query-suggestions.md"), [query spell checker](query-spell-check.md "query-spell-check.md"), [relevance tuning](tuning.md "tuning.md"), [incremental learning](submitting-feedback.md "submitting-feedback.md"), [custom document enrichment](custom-document-enrichment.md "custom-document-enrichment.md"), [custom metadata](custom-attributes.md "custom-attributes.md"), [adjusting query capacity and document
  capacity](adjusting-capacity.md "adjusting-capacity.md"), and [search experience](deploying.md "deploying.md").
- **Partial support** – [Data source connectors](data-source.md "data-source.md") and [user context filtering](user-context-filter.md "user-context-filter.md"). For more
  information on partially supported features, see [Limitations](hiw-index-types.md#kendra-gen-ai-index "hiw-index-types.md#kendra-gen-ai-index").

### Limitations

The following outlines the known limitations of an Amazon Kendra GenAI Enterprise
Edition index:

- Amazon Kendra GenAI Enterprise Edition indexes are only available in
  US East (N. Virginia) and US West (Oregon).
- Amazon Kendra GenAI Enterprise Edition indexes only support English
  language content.
- Amazon Kendra GenAI Enterprise Edition indexes support only v2.0 Amazon Kendra
  data source connectors.
- In an Amazon Kendra GenAI Enterprise Edition index, you can only use
  [user attributes](user-context-filter.md#context-filter-attribute "user-context-filter.md#context-filter-attribute") to filter search results by user
  context.
- Amazon Kendra GenAI Enterprise Edition indexes don't support [token-based user access control](create-index-access-control.md "create-index-access-control.md") or
  [user ID and group –based user access control](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") to
  documents.
- The [CreateAccessControlConfiguration](../APIReference/API_CreateAccessControlConfiguration.md "../APIReference/API_CreateAccessControlConfiguration.md")
  API operation is disabled for Amazon Kendra GenAI Enterprise Edition
  indexes.
- If you're using an Amazon Kendra GenAI Enterprise Edition index with
  Amazon Q Business, note the following about controlling
  end-user access to documents:

Amazon Q Business uses user email ID to determine end-user
access to documents in an index. When you connect an Amazon Kendra index to
Amazon Q Business, Amazon Q Business relays the
user’s identifying email ID to Amazon Kendra to enable document filtering
for end users. If data sources connected to your Amazon Kendra index don’t
use
email
ID–based document filtering, or the email
ID is not present, Amazon Q Business generates responses only
from public documents.

## Amazon Kendra Enterprise Edition index

An Amazon Kendra Enterprise Edition index provides semantic search capabilities, and
offers a high-availability service that is suitable for production
workloads.

###### Topics

- [Supported features](#kendra-ent-index-features "#kendra-ent-index-features")
- [Limitations](#ent-index-limitations "#ent-index-limitations")

### Supported features

The following features are supported for an Amazon Kendra Enterprise Edition index
if you're using the [Retrieve](../APIReference/API_Retrieve.md "../APIReference/API_Retrieve.md") API
operation for RAG use cases: querying using [advance query syntax](searching-example.md#searching-index-query-syntax "searching-example.md#searching-index-query-syntax"), [suggested spell
corrections](query-spell-check.md "query-spell-check.md") for queries, [faceting](filtering.md#search-facets "filtering.md#search-facets"),
[query suggestions](query-suggestions.md "query-suggestions.md")
to autocomplete search queries, and [incremental
learning](submitting-feedback.md "submitting-feedback.md").

All features are supported for an Amazon Kendra Enterprise Edition index if you're
using the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API
operation for search use cases.

### Limitations

The following outlines the known limitations of an Amazon Kendra Enterprise
Edition index:

- If you're using an Amazon Kendra
  Enterprise
  Edition index with Amazon Q Business, note
  the following about controlling end-user access to documents:

Amazon Q Business uses user email ID to determine end-user
access to documents in an index. When you connect an Amazon Kendra index to
Amazon Q Business, Amazon Q Business relays the
user’s identifying email ID to Amazon Kendra to enable document filtering
for end users. If data sources connected to your Amazon Kendra index don’t
use email ID–based document filtering, or the email ID is not
present, Amazon Q Business generates responses only from
public documents.

## Amazon Kendra Developer Edition index

An Amazon Kendra Developer Edition index also provides semantic search capabilities
for you to test your use cases. However, we don't recommend it for production
use cases.

###### Topics

- [Supported features](#kendra-dev-index-features "#kendra-dev-index-features")
- [Limitations](#dev-index-limitations "#dev-index-limitations")

### Supported features

The following features are supported for an Amazon Kendra Developer Edition index
if you're using the [Retrieve](../APIReference/API_Retrieve.md "../APIReference/API_Retrieve.md") API
operation for RAG use cases: querying using [advance query syntax](searching-example.md#searching-index-query-syntax "searching-example.md#searching-index-query-syntax"), [suggested spell
corrections](query-spell-check.md "query-spell-check.md") for queries, [faceting](filtering.md#search-facets "filtering.md#search-facets"),
[query suggestions](query-suggestions.md "query-suggestions.md")
to autocomplete search queries, and [incremental
learning](submitting-feedback.md "submitting-feedback.md").

All features are supported for an Amazon Kendra Developer Edition index if you're
using the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API
operation for search use cases.

### Limitations

The following outlines the known limitations of an Amazon Kendra Developer Edition
index:

- If you're using an Amazon Kendra Developer Edition index with Amazon Q Business, note the following about controlling end-user
  access to documents:

Amazon Q Business uses user email ID to determine end-user
access to documents in an index. When you connect an Amazon Kendra index to
Amazon Q Business, Amazon Q Business relays the
user’s identifying email ID to Amazon Kendra to enable document filtering
for end users. If data sources connected to your Amazon Kendra index don’t
use email ID–based document filtering, or the email ID is not
present, Amazon Q Business generates responses only from
public documents.
