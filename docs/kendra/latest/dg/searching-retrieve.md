# Retrieving passages

You can use the [Retrieve](../APIReference/API_Retrieve.md "../APIReference/API_Retrieve.md")
API as a retriever for retrieval augmented generation (RAG) systems.

RAG systems use generative artificial intelligence to build question-answering
applications. RAG systems consist of a retriever and large language models (LLM). Given
a query, the retriever identifies the most relevant chunks of text from a corpus of
documents and feeds it to the LLM to provide the most useful answer. Then, the LLM
analyzes the relevant text chunks or passages and generates a comprehensive response for
the query.

The `Retrieve` API looks at chunks of text or excerpts that
are referred to as _passages_ and returns the top
passages that are most relevant to the query.

Like the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API, the `Retrieve` API also searches
for relevant information. Retrieve API's information retrieval takes into account the
query's context, and all the available information from the indexed documents. However,
by default, the `Query` API only returns excerpt passages of
up to 100 token words. With the `Retrieve` API, you can
retrieve longer passages of up to 200 token words and up to 100 semantically relevant
passages. This doesn't include question-answer or FAQ type responses from your index.
The passages, also called chunks, are text excerpts that can be semantically extracted
from multiple documents and multiple parts of the same document. Kendra's GenAI
Enterprise Edition index offers high accuracy results for retrieve, using a hybrid
search over vector and keyword indices along with ranking by deep learning
models.

You can also do the following with the `Retrieve` API:

- Override boosting at the index level
- Filter based on document fields or attributes
- Filter based on the user or their group access to documents
- View the confidence score bucket for a retrieved passage result. The
  confidence bucket provides a relative ranking that indicates how confident
  Amazon Kendra is that the response is relevant to the query.

###### Note

Confidence score buckets are currently available only for English.
You can also include certain fields in the response that might provide useful
additional information.

The `Retrieve` API currently doesn't support the following
features: querying using [advance
query syntax](searching-example.md#searching-index-query-syntax "searching-example.md#searching-index-query-syntax"), [suggested spell corrections](query-spell-check.md "query-spell-check.md")
for queries, [faceting](filtering.md#search-facets "filtering.md#search-facets"), [query
suggestions](query-suggestions.md "query-suggestions.md") to autocomplete search queries, and [incremental learning](submitting-feedback.md "submitting-feedback.md"). Any
retrieve API queries will not surface in the analytics dashboard.

The `Retrieve` API shares the number of [query capacity
units](../APIReference/API_CapacityUnitsConfiguration.md "../APIReference/API_CapacityUnitsConfiguration.md") that you set for your index. For more information on what's included
in a single capacity unit and the default base capacity for an index, see [Adjusting
capacity](adjusting-capacity.md "adjusting-capacity.md").

###### Note

You can't add capacity if you are using the Amazon Kendra Developer Edition;
you can only add capacity when using Amazon Kendra Enterprise Edition. For more
information on what's included in the Developer and Enterprise Editions, see [Amazon Kendra Editions](what-is-kendra.md#kendra-editions "what-is-kendra.md#kendra-editions").

The following is an example of using the `Retrieve` API to
retrieve the top 100 most relevant passages from documents in an index for the query
"how does amazon kendra work?"

Python

```
import boto3
import pprint

kendra = boto3.client("kendra")

# Provide the index ID
index_id = "index-id"
# Provide the query text
query = "how does amazon kendra work?"
# You can retrieve up to 100 relevant passages
# You can paginate 100 passages across 10 pages, for example
page_size = 10
page_number = 10

result = kendra.retrieve(
        IndexId = index_id,
        QueryText = query,
        PageSize = page_size,
        PageNumber = page_number)

print("\nRetrieved passage results for query: " + query + "\n")

for retrieve_result in result["ResultItems"]:

    print("-------------------")
    print("Title: " + str(retrieve_result["DocumentTitle"]))
    print("URI: " + str(retrieve_result["DocumentURI"]))
    print("Passage content: " + str(retrieve_result["Content"]))
    print("------------------\n\n")
```

Java

```
package com.amazonaws.kendra;

import software.amazon.awssdk.services.kendra.KendraClient;
import software.amazon.awssdk.services.kendra.model.RetrieveRequest;
import software.amazon.awssdk.services.kendra.model.RetrieveResult;
import software.amazon.awssdk.services.kendra.model.RetrieveResultItem;

public class RetrievePassageExample {
    public static void main(String[] args) {
        KendraClient kendra = KendraClient.builder().build();

        String indxId = "index-id";
        String query = "how does amazon kendra work?";
        Integer pgSize = 10;
        Integer pgNumber = 10;

        RetrieveRequest retrieveRequest = retrieveRequest
            .builder()
            .indexId(indxId)
            .queryText(query)
            .pageSize(pgSize)
            .pageNumber(pgNumber)
            .build();

        RetrieveResult retrieveResult = kendra.retrieve(retrieveRequest);

        System.out.println(String.format("\nRetrieved passage results for query: %s", query));
        for(RetrieveResultItem item: retrieveResult.resultItems()) {
            System.out.println("----------------------");
            System.out.println(String.format("Title: %s", documentTitle));
            System.out.println(String.format("URI: %s", documentURI));
            System.out.println(String.format("Passage content: %s", content));
            System.out.println("-----------------------\n");
        }
    }
}
```
