

# Retrieve memory records
<a name="long-term-retrieve-records"></a>

You can retrieve extracted memories using the [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html) API. This operation lets you search extracted memory records based on semantic queries, making it easy to find relevant information from your agent’s memory.

## Required parameters
<a name="retrieve-records-parameters"></a>

The `RetrieveMemoryRecords` operation requires the following key parameters:

 **memoryId**   
The identifier of the memory resource containing the records you want to retrieve.

 **namespace**   
The exact namespace where the memory records are stored. The operation returns paginated memory records in namespaces that match with the provided namespace.

 **namespacePath**   
The namespace path of where the memory records are stored. The operation returns paginated memory records under the provided namespaces hierarchy that start with the provided path.

 **searchCriteria**   
A structure containing search parameters:  
+  *searchQuery* - The semantic query text used to find relevant memories (up to 10,000 characters).
+  *memoryStrategyId* (optional) - Limits the search to memories created by a specific strategy.
+  *topK* - The maximum number of most relevant results to return (default: 10, maximum: 100).

## Response format
<a name="retrieve-records-response"></a>

The operation returns a list of memory record summaries that match your search criteria. Each summary includes a *relevance score* , which is derived from the cosine similarity of embedding vectors. This score does **not** represent a percentage match, but instead measures how closely two vectors align in a high-dimensional space. Higher scores indicate greater relevance of the memory record to the search query. The results are paginated, with a default maximum of 100 results per page. You can use the `nextToken` parameter to retrieve additional pages of results.

## Best practices
<a name="retrieve-records-best-practices"></a>

When retrieving memories, consider the following best practices:
+ Craft specific search queries that clearly describe the information you’re looking for.
+ Use the `topK` parameter to control the number of results based on your application’s needs.
+ When working with large memories, implement pagination to efficiently process all relevant results.
+ Consider filtering by `memoryStrategyId` when you need memories from a specific extraction strategy.

Once retrieved, these memory records can be incorporated into your agent’s context, enabling more personalized and contextually aware responses.