

# Search for registry records

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

As a consumer, you can search a registry’s approved records using the `SearchDiscoverableRegistryRecords` data-plane API. The API accepts a natural language query or exact terms, ranks records with the search type that you choose (keyword, semantic, or hybrid search, which combines the two), and returns results limited to records whose latest revision has status **Approved**. You can page through the results with `nextToken`. Records in **Draft**, **Pending approval**, **Rejected**, or **Deprecated** status are not returned. To browse the catalog without a query, use `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` instead — see [Browse approved records](registry-browse-records.md).

You can also invoke the discovery data-plane APIs through the registry’s MCP endpoint (`InvokeRegistryMcp`) using any MCP-compatible client. You can call `SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, and `BatchGetDiscoverableRegistryRecord` directly as MCP tools. Its `search_discoverable_registry_records_paginated` tool takes the same search type and pagination options as the API. For more information, see [Search with a search type and page through results](registry-mcp-endpoint.md#registry-mcp-search-paginated).

## Request Parameters
<a name="registry-search-parameters"></a>
+  **searchQuery** (required): A natural language query or exact terms, from 0–256 characters. If you specify an empty string, the search returns the records that match `filters`, most recently updated first, up to the result limit for the search type.
+  **registryIds** (required): Which Registry to conduct the Search in. Supports exactly one registry ARN or ID
+  **searchType** (optional): How the service ranks records against the query: `HYBRID`, `SEMANTIC`, or `KEYWORD`. If you omit it, the service uses the default search type, `HYBRID`, and reports it in the response. For more information, see [Choose a search type](#registry-search-types).
+  **maxResults** (optional): How many records one page of results holds: 1–50 when `searchType` is `KEYWORD`, and 1–20 when it is `HYBRID` or `SEMANTIC`. Defaults to 10.
+  **nextToken** (optional): The pagination token from a previous response, to get the next page of results. For more information, see [Page through search results](#registry-search-pagination).
+  **filters** (optional) — Metadata filter expression

**Note**  
 `searchType` and `nextToken` are available in the AWS Agent Registry namespace (`agent-registry`).

## Response
<a name="registry-search-response"></a>
+  **registryRecords**: The matching records, most relevant first.
+  **searchType**: The search type that the service used, including the default when you omit `searchType` in the request.
+  **nextToken**: Present when more results might be available. It’s absent when there are no more results, or when the search has returned the maximum number of results for its search type.

## Choose a search type
<a name="registry-search-types"></a>

The `searchType` parameter sets how AWS Agent Registry ranks records against your query. The following table describes each search type.


| Search type | How it ranks records | Use it when | 
| --- | --- | --- | 
|  `KEYWORD`  | Matches the query terms against the record name, description, descriptors, and custom metadata text values. Returns up to 1,000 results, in pages of up to 50. | You know the name or exact terms, such as a record name or a tool name, or you want to list and filter records. | 
|  `SEMANTIC`  | Ranks records by semantic similarity to the query, and returns the most similar records, up to `maxResults`, even when none of them closely matches the query. Returns up to 20 results. | You describe a task in natural language, and the words in your query might not appear in the record. | 
|  `HYBRID` (default) | Combines keyword ranking and semantic ranking. Returns up to 20 results. | Your query combines names and intent, or you aren’t sure which search type works best. | 

To list and filter records with `KEYWORD`, leave `searchQuery` empty and set `filters` on any supported field, such as `name`, `recordType`, `recordVersion`, or a custom metadata field. The search returns every matching record, most recently updated first, up to 1,000 results. For an example, see [Page through search results](#registry-search-pagination).

The response reports the search type that ran in its `searchType` field, including the default when you omit `searchType`. Read the search type from the response rather than assume `HYBRID`. If AWS Agent Registry becomes available in an AWS Region where semantic search isn’t available, `KEYWORD` is the default search type in that Region, and a request that sets `HYBRID` or `SEMANTIC` there returns a `ValidationException`.

Searches with `KEYWORD` count toward their own request rate quota, which is higher than the quota for `HYBRID` and `SEMANTIC` searches. For the quotas, see [Throttling limits](bedrock-agentcore-limits.md#registry-throttling-limits).

## Page through search results
<a name="registry-search-pagination"></a>

When more results might be available, the response includes `nextToken`. To get the next page, send the request again with the same `searchQuery`, `registryIds`, `filters`, and `searchType`, and add `nextToken`. If you omitted `searchType` for the first page, omit it for the later pages too.

Follow these rules when you page through results:
+ If `searchQuery`, `registryIds`, `filters`, or `searchType` differ from the first page, the request fails with a `ValidationException` whose field list names `nextToken`. Repeat the search without `nextToken` to start again.
+ A pagination token expires 15 minutes after the service returns the first page.
+ A page can hold fewer records than `maxResults`, even none, while the response still includes `nextToken`. Keep requesting pages until the response doesn’t include `nextToken`.
+ A search returns at most 1,000 results across all pages when `searchType` is `KEYWORD`, and at most 20 results when it is `HYBRID` or `SEMANTIC`. For a relevance search, the first page usually holds the best matches. To retrieve more records, refine the query or the filters, or use `ListDiscoverableRegistryRecords` to list every record. For more information, see [Browse approved records](registry-browse-records.md).

To list the records that match a filter, most recently updated first, send an empty `searchQuery` with `filters` and set `searchType` to `KEYWORD`. You can filter on any supported field, including custom metadata fields. A listing like this returns up to 1,000 records across its pages. The following example lists every MCP record in a registry.

In the following example, replace `<registryARN>` with the ARN of your registry.

```json
{
  "registryIds": ["<registryARN>"],
  "searchQuery": "",
  "searchType": "KEYWORD",
  "maxResults": 50,
  "filters": {
    "recordType": { "$eq": "MCP" }
  }
}
```

The AWS SDKs provide a paginator for `SearchDiscoverableRegistryRecords`. The following Python example pages through a `KEYWORD` search, 50 records at a time. Replace `<registryARN>` with the ARN of your registry.

```python
import boto3

client = boto3.client('agent-registry')

paginator = client.get_paginator('search_discoverable_registry_records')
for page in paginator.paginate(
    registryIds=['<registryARN>'],
    searchQuery='weather',
    searchType='KEYWORD',
    PaginationConfig={'PageSize': 50}
):
    print(f"Search type: {page['searchType']}")
    for record in page['registryRecords']:
        print(f"{record['name']} - {record['recordType']}")
```

## Metadata filters
<a name="registry-search-metadata-filters"></a>

Operators: `$eq`, `$ne`, `$in`. Logical: `$and`, `$or`. Fields: `name`, `recordType`, `recordVersion`, and `customMetadata.{fieldName}` for any field defined in the registry’s custom metadata schema. For more information, see [Define a custom metadata schema](registry-custom-metadata-schema.md).

Example: `{"recordType": {"$eq": "MCP"}}` 

Combined: `{"$and": [{"recordType": {"$eq": "MCP"}}, {"recordVersion": {"$eq": "1.0"}}]}` 

Custom metadata example: `{"customMetadata.owner": {"$eq": "search-team"}}` 

### Filter rules and limits
<a name="registry-search-filter-rules"></a>

Filters must follow these rules and limits:
+ A filter contains at least one condition. To search without a filter, omit `filters`. An empty object (`{}`) returns a `ValidationException`.
+ A filter contains at most 10 conditions. A condition is one field with one operator, such as `{"recordType": {"$eq": "MCP"}}`. A `$in` condition counts as one condition.
+  `$in` accepts from 1 to 25 values.
+ Filter values are strings or booleans.
+ Each condition has exactly one operator. To apply two operators to the same field, use `$and` with one object per condition.
+ To combine conditions with AND, list several fields in one object, such as `{"recordType": {"$eq": "MCP"}, "recordVersion": {"$eq": "1.0"}}`, or use `$and`.
+  `$and` and `$or` take an array of 1–10 objects, and each object contains exactly one condition. An object with more than one field, or an empty object, returns a `ValidationException`. You can’t combine conditions with AND inside `$or`. To find records that match (A AND B) OR C, run separate searches.
+ A filter uses at most one logical operator. You can’t nest `$and` or `$or`, or mix a logical operator with field conditions at the top level.

## Console
<a name="registry-search-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Record directory**.

1. Choose the registry you want to search. The page automatically calls `ListDiscoverableRegistryRecords` and displays the approved records in the registry.

1. In the search bar, enter your search query. This triggers `SearchDiscoverableRegistryRecords` and displays ranked results.

1. (Optional) To filter results by a specific property, choose the search field to expand the **Properties** menu, and then choose a filter: **Name**, **Record type**, or **Version**. If the registry has a custom metadata schema, its fields appear grouped under **Custom metadata**.

1. Choose a record from the results to view its full descriptor content.

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the navigation pane, choose **Registry**, and then choose the registry name.

1. Choose the **Search records** tab.

1. Enter your search query and view results.

**Note**  
Console search is available only for registries that use IAM-based inbound authorization. For JWT-authorized registries, use the search API directly with an HTTP client (such as `curl`) and a valid JWT bearer token, or use the MCP endpoint for the registry via an MCP client.

## AWS CLI (Registry with IAM based Inbound Authorization)
<a name="registry-search-cli-iam"></a>

**Example**  

```bash
aws agent-registry search-discoverable-registry-records \
  --search-query "weather" \
  --search-type KEYWORD \
  --registry-ids "<registryARN>" \
  --region us-east-1
```

```bash
aws bedrock-agentcore search-registry-records \
  --search-query "weather" \
  --registry-ids "<registryARN>" \
  --region us-east-1
```

In the `agent-registry` namespace, the AWS CLI pages through the results for you and returns every result, up to the result limit for the search type. To get only the first page, add `--no-paginate`. To set the number of records in each page, add `--page-size`, and to cap the total number of records, add `--max-items`. For more information, see [Using the AWS CLI pagination options](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html) in the * AWS Command Line Interface User Guide*.

## AWS SDK (Registry with IAM based Inbound Authorization)
<a name="registry-search-sdk-iam"></a>

**Example**  

```python
import boto3

client = boto3.client('agent-registry')

response = client.search_discoverable_registry_records(
    registryIds=['<registryARN>'],
    searchQuery='weather',
    searchType='KEYWORD',
    maxResults=10
)
print(f"Search type: {response['searchType']}")
for record in response['registryRecords']:
    print(f"{record.get('displayName', record['name'])} ({record['name']}) - {record['recordType']} - {record['status']}")
```

```python
import boto3

client = boto3.client('bedrock-agentcore')

response = client.search_registry_records(
    registryIds=['<registryARN>'],
    searchQuery='weather',
    maxResults=10
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['descriptorType']} - {record['status']}")
```

## HTTP client (Registry with OAuth based Inbound Authorization)
<a name="registry-search-http-oauth"></a>

First obtain a bearer token:

```bash
SECRET_HASH=$(echo -n "<username><appClientId>" | openssl dgst -sha256 -hmac "<appClientSecret>" -binary | base64)

aws cognito-idp initiate-auth \
  --client-id "<appClientId>" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME="<username>",PASSWORD='<password>',SECRET_HASH="$SECRET_HASH" \
  --region us-east-1 | jq -r '.AuthenticationResult.AccessToken'
```

Then search with the bearer token:

**Example**  

```bash
curl -X POST "https://agent-registry.<region>.api.aws/discoverable-records-search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <accessToken>" \
  -d '{"registryIds": ["<registryARN>"], "searchQuery": "weather", "searchType": "KEYWORD", "maxResults": 10}'
```

```bash
curl -X POST "https://bedrock-agentcore.<region>.amazonaws.com/registry-records/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <accessToken>" \
  -d '{"registryIds": ["<registryARN>"], "searchQuery": "weather", "maxResults": 10}'
```

## Eventual consistency in AWS Agent Registry search
<a name="registry-search-eventual-consistency"></a>

 AWS Agent Registry uses an eventually consistent model for search indexing. When you approve a registry record by calling `UpdateRegistryRecordStatus` or through the console, the record does not appear in `SearchDiscoverableRegistryRecords` or `InvokeRegistryMcp` results immediately. It typically takes a few seconds for the approved record to be indexed and become discoverable, but in some cases it can take up to a few minutes.

During this time, you might observe the following behavior:
+ A `SearchDiscoverableRegistryRecords` query does not return a record that was just approved.
+ A `ListDiscoverableRegistryRecords` or `BatchGetDiscoverableRegistryRecord` call does not include the record.
+ The registry MCP endpoint ( `InvokeRegistryMcp` ) does not include a recently approved record in tool results.
+ In contrast, the control-plane APIs (`GetRegistryRecord` and `ListRegistryRecords`) return the newly approved record immediately after `UpdateRegistryRecordStatus` completes. Eventual consistency applies only to the discovery data-plane APIs and the registry MCP endpoint.

Only records in **Approved** status are included in discoverable results. Records in Draft, Pending Approval, Rejected, or Deprecated status are never returned by the discoverable data-plane APIs or by `InvokeRegistryMcp`. You can verify a record’s current status by calling `GetRegistryRecord`, which always returns the latest revision regardless of indexing state.

To handle eventual consistency in your application, we recommend the following:
+ After approving a record, confirm it is discoverable by calling `SearchDiscoverableRegistryRecords` with a retry strategy that includes exponential backoff.
+ Do not assume a record is missing from the registry if it does not appear in results immediately after approval. Call `GetRegistryRecord` to verify the record’s status.
+ If you are integrating approval workflows through Amazon EventBridge and `UpdateRegistryRecordStatus`, add a brief delay before downstream systems query the discoverable APIs for the newly approved record.

**Note**  
 `SearchDiscoverableRegistryRecords` was named `SearchRegistryRecords` in the `bedrock-agentcore` namespace.

For general guidance on configuring retry behavior in AWS SDKs, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the * AWS SDKs and Tools Reference Guide*.

## How record attributes affect search relevance
<a name="registry-search-relevance"></a>

By default, AWS Agent Registry uses hybrid search, which combines semantic understanding with keyword matching to return relevant results. You can instead choose keyword or semantic search alone with `searchType`. For more information, see [Choose a search type](#registry-search-types). If a record you expect to find does not appear in search results, understanding which record attributes influence search can help.

### Which record attributes are used for search
<a name="registry-search-attributes"></a>

The following attributes from your registry record are used to determine search relevance:
+  **Name** — Used for keyword matching. Clear, descriptive names that reflect what the resource does improve discoverability for exact and partial name lookups.
+  **Description** — Used for both keyword and semantic matching. Descriptions written in natural language that explain the resource’s purpose and common use cases are more discoverable than terse technical labels.
+  **Descriptors** — The full content of your protocol definition (MCP server definition, agent card, skill documentation, or custom JSON) is used for semantic matching. This includes tool names, tool descriptions, input parameter names, and capability summaries.
+  **Record type and version** — Available as filterable fields. You can narrow results using metadata filters on `name`, `recordType`, and `recordVersion`.
+  **Custom metadata** — If the registry has a custom metadata schema, its fields are available as filterable fields under `customMetadata.{fieldName}`. Custom metadata values are included in the search index. The `customMetadata.{fieldName}` filter syntax provides exact-match filtering, while the values also contribute to keyword and semantic search ranking through the `searchQuery` parameter.

### How search queries are processed
<a name="registry-search-query-processing"></a>

When you call `SearchDiscoverableRegistryRecords` with `searchType` set to `HYBRID`, the default, AWS Agent Registry runs two searches in parallel against the same set of indexed records. It then merges the results. With `SEMANTIC`, it runs only the semantic search, and with `KEYWORD`, only the keyword search:
+  **Semantic search** — Your query is converted into a vector representation and compared against the vector representations of indexed records. This finds conceptually related records even when the exact words in your query don’t appear in the record. For example, a query for "book a flight" can match a record named "travel-reservation-service."
+  **Keyword search** — Your query is matched against the text content of record fields using traditional keyword relevance. This is effective for exact name lookups and specific technical terms. For example, a query for "weather-api-v2" matches records containing that exact text.

If you include metadata filters in your request, the filters are applied to each search that runs before results are scored and ranked. This means filters reduce the candidate set that the search operates on, rather than filtering results after ranking.

### How results are ranked
<a name="registry-search-ranking"></a>

Results are returned in order of relevance, with the most relevant record first. In a `HYBRID` search, the results from semantic and keyword search are combined into a single ranked list. Each result’s final position depends on its relevance across both searches. A record that ranks highly in both semantic and keyword results appears higher than one that ranks highly in only one. Within keyword search, the record name most strongly affects how results rank, followed equally by the description and descriptor content. Because both search modes run and contribute to the final ranking of a `HYBRID` search, how you write your query affects which records surface. The following guidance can help you get better results depending on your intent.

### Writing effective search queries
<a name="registry-search-effective-queries"></a>

 **When you know the exact name or identifier** , use a short, specific query, and consider setting `searchType` to `KEYWORD`. Keyword search matches exact text against record names, descriptions, and descriptor content. Short queries like "weather-api-v2" or "pdf-processing" are effective for finding records by name.

 **When you’re exploring by capability or use case** , use a natural language description of what you need, and consider setting `searchType` to `SEMANTIC`. Semantic search understands conceptual intent, so queries like "find a tool that can book flights" or "extract structured data from PDF documents" can match relevant records even if those exact words don’t appear in the record metadata.

 **Avoid mixing filter-like constraints with descriptive intent in the same query.** In a `HYBRID` search, a query like "find all MCP servers for weather forecasts" sends the entire sentence through both semantic and keyword search. The semantic component interprets the full sentence as a conceptual intent, which can surface records that are conceptually related but don’t match the specific attribute you intended to constrain. Instead, use metadata filters for attribute-based constraints and keep the query focused on the topic. See [When to use metadata filters versus query text](#registry-search-filters-vs-query).

### Writing discoverable records
<a name="registry-search-discoverable-records"></a>
+ Write descriptions that explain what the resource does and the problems it solves. Semantic search understands intent, so "helps customers track package deliveries" is more discoverable than "delivery-status-endpoint."
+ Provide complete tool definitions for MCP servers. Tool descriptions and input parameter descriptions all contribute to search relevance.
+ Include relevant keywords in your name and description. Keyword search matches exact text, so if consumers are likely to search for specific terms, make sure those terms appear in your record.

### When to use metadata filters versus query text
<a name="registry-search-filters-vs-query"></a>

Use metadata filters when your intent is to constrain results by a known attribute such as record type, name, or version. Do not embed filter-like constraints in the query text itself. For example, if you want to find all MCP servers related to weather, use a metadata filter for the record type and a query for the topic:

```json
{
  "searchQuery": "weather forecast",
  "filters": {
    "recordType": { "$eq": "MCP" }
  }
}
```

Avoid putting the constraint into the query text like "find all MCP servers for weather forecasts". Because longer queries lean toward semantic matching, the words "MCP servers" are interpreted as part of the conceptual intent rather than as an exact filter. This can cause the semantic component to return records that are conceptually related to the full sentence but don’t match the specific attribute you intended to filter on — for example, returning agent records about weather alongside MCP server records. The same applies to any attribute-based constraint. If you want records with a specific name, version, or type, use the corresponding metadata filter rather than including those terms in the query.

You can filter on the following fields:
+  `name` — Match records by exact name.
+  `recordType` — Match records by semantic type (`AGENT`, `MCP`, `SKILL`, `GATEWAY`, `CUSTOM`).
+  `recordVersion` — Match records by version string.
+  `customMetadata.{fieldName}` — Match records by a value in the registry’s custom metadata schema, where `{fieldName}` is the field name you defined (for example, `customMetadata.owner`). See [Define a custom metadata schema](registry-custom-metadata-schema.md).

Filters support `$eq` (equals), `$ne` (not equals), and `$in` (matches any value in a list) operators, and can be combined using `$and` and `$or` logic.

For example, to search for weather-related MCP servers only:

```json
{
  "searchQuery": "weather forecast",
  "filters": {
    "recordType": { "$eq": "MCP" }
  }
}
```

To exclude a specific resource type:

```json
{
  "searchQuery": "<your query>",
  "filters": {
    "recordType": { "$ne": "CUSTOM" }
  }
}
```

To match any of several versions:

```json
{
  "filters": {
    "recordVersion": { "$in": ["1.0", "1.1", "2.0"] }
  }
}
```

To match records by a custom metadata field:

```json
{
  "filters": {
    "customMetadata.humanInLoop": { "$eq": true }
  }
}
```

To combine a custom metadata filter with a base field filter:

```json
{
  "filters": {
    "$and": [
      { "recordType": { "$eq": "MCP" } },
      { "customMetadata.tier": { "$eq": "internal" } }
    ]
  }
}
```

To match records that meet either of two conditions, use `$or` with one condition in each object:

```json
{
  "filters": {
    "$or": [
      { "recordType": { "$eq": "MCP" } },
      { "customMetadata.owner": { "$eq": "search-team" } }
    ]
  }
}
```

To match several values of the same field, use `$in` instead of `$or`. For the full rules, see [Filter rules and limits](#registry-search-filter-rules).

**Note**  
Filter values for `customMetadata.{fieldName}` are strings or native booleans. For a **Boolean** field, use the string `"true"` or `"false"`, or a native JSON boolean (`true` / `false`). For an **Enum** field, use one of the schema’s allowed values. A filter on a field matches records of every record type that has that field.

### Search returns only approved records
<a name="registry-search-approved-only"></a>

Only records in **Approved** status appear in search results and through the MCP endpoint. Records in Draft, Pending Approval, Rejected, or Deprecated status are not returned. If a recently approved record does not appear in results, see [Eventual consistency in AWS Agent Registry search](#registry-search-eventual-consistency).