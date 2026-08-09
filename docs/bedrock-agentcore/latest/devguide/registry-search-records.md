# Search for registry records

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

As a consumer, you can search a registry’s approved records using the `SearchDiscoverableRegistryRecords` data-plane API. The API accepts a natural language query, applies hybrid search that combines semantic understanding with keyword matching, and returns ranked results limited to records whose latest revision has status **Approved**. Records in **Draft**, **Pending approval**, **Rejected**, or **Deprecated** status are not returned. To browse the catalog without a query, use `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` instead — see [Browse approved records](registry-browse-records.md "registry-browse-records.md").

You can also invoke the discovery data-plane APIs through the registry’s MCP endpoint (`InvokeRegistryMcp`) using any MCP-compatible client. The endpoint exposes `SearchDiscoverableRegistryRecords`, `ListDiscoverableRegistryRecords`, and `BatchGetDiscoverableRegistryRecord` as MCP tools that you can call directly.

## Request Parameters

- **searchQuery** (required): Can be any natural language query from 1–256 characters
- **registryIds** (required): Which Registry to conduct the Search in. Supports exactly one registry ARN or ID
- **maxResults** (optional): How many records are returned in the Search response. Can take any value between 1–20 and defaults to 10
- **filters** (optional) — Metadata filter expression

## Metadata filters

Operators: `$eq`, `$ne`, `$in`. Logical: `$and`, `$or`. Fields: `name`, `recordType`, `recordVersion`.

Example: `{"recordType": {"$eq": "MCP"}}`

Combined: `{"$and": [{"recordType": {"$eq": "MCP"}}, {"recordVersion": {"$eq": "1.0"}}]}`

## Console

###### Example

AWS Agent Registry namespace

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1# "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#").
2. In the navigation pane, choose **Record directory**.
3. Choose the registry you want to search. The page automatically calls `ListDiscoverableRegistryRecords` and displays the approved records in the registry.
4. In the search bar, enter your search query. This triggers `SearchDiscoverableRegistryRecords` and displays ranked results.
5. (Optional) To filter results by a specific property, choose the search field to expand the **Properties** menu, and then choose a filter: **Name**, **Record type**, or **Version**.
6. Choose a record from the results to view its full descriptor content.

Amazon Bedrock AgentCore namespace (to be deprecated)

1. Open the AWS Agent Registry page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1# "https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#").
2. In the navigation pane, choose **Registry**, and then choose the registry name.
3. Choose the **Search records** tab.
4. Enter your search query and view results.

###### Note

Console search is available only for registries that use IAM-based inbound authorization. For JWT-authorized registries, use the search API directly with an HTTP client (such as `curl`) and a valid JWT bearer token, or use the MCP endpoint for the registry via an MCP client.

## AWS CLI (Registry with IAM based Inbound Authorization)

###### Example

AWS Agent Registry namespace

```
aws agent-registry search-discoverable-registry-records \
  --search-query "weather" \
  --registry-ids "<registryARN>" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore search-registry-records \
  --search-query "weather" \
  --registry-ids "<registryARN>" \
  --region us-east-1
```

## AWS SDK (Registry with IAM based Inbound Authorization)

###### Example

AWS Agent Registry namespace

```
import boto3

client = boto3.client('agent-registry')

response = client.search_discoverable_registry_records(
    registryIds=['<registryARN>'],
    searchQuery='weather',
    maxResults=10
)
for record in response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['recordType']} - {record['status']}")
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
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

First obtain a bearer token:

```
SECRET_HASH=$(echo -n "<username><appClientId>" | openssl dgst -sha256 -hmac "<appClientSecret>" -binary | base64)

aws cognito-idp initiate-auth \
  --client-id "<appClientId>" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME="<username>",PASSWORD='<password>',SECRET_HASH="$SECRET_HASH" \
  --region us-east-1 | jq -r '.AuthenticationResult.AccessToken'
```

Then search with the bearer token:

###### Example

AWS Agent Registry namespace

```
curl -X POST "https://agent-registry.<region>.api.aws/discoverable-records-search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <accessToken>" \
  -d '{"registryIds": ["<registryARN>"], "searchQuery": "weather", "maxResults": 10}'
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
curl -X POST "https://bedrock-agentcore.<region>.amazonaws.com/registry-records/search" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <accessToken>" \
  -d '{"registryIds": ["<registryARN>"], "searchQuery": "weather", "maxResults": 10}'
```

## Eventual consistency in AWS Agent Registry search

AWS Agent Registry uses an eventually consistent model for search indexing. When you approve a registry record by calling `UpdateRegistryRecordStatus` or through the console, the record does not appear in `SearchDiscoverableRegistryRecords` or `InvokeRegistryMcp` results immediately. It typically takes a few seconds for the approved record to be indexed and become discoverable, but in some cases it can take up to a few minutes.

During this time, you might observe the following behavior:

- A `SearchDiscoverableRegistryRecords` query does not return a record that was just approved.
- A `ListDiscoverableRegistryRecords` or `BatchGetDiscoverableRegistryRecord` call does not include the record.
- The registry MCP endpoint ( `InvokeRegistryMcp` ) does not include a recently approved record in tool results.
- In contrast, the control-plane APIs (`GetRegistryRecord` and `ListRegistryRecords`) return the newly approved record immediately after `UpdateRegistryRecordStatus` completes. Eventual consistency applies only to the discovery data-plane APIs and the registry MCP endpoint.

Only records in **Approved** status are included in discoverable results. Records in Draft, Pending Approval, Rejected, or Deprecated status are never returned by the discoverable data-plane APIs or by `InvokeRegistryMcp`. You can verify a record’s current status by calling `GetRegistryRecord`, which always returns the latest revision regardless of indexing state.

To handle eventual consistency in your application, we recommend the following:

- After approving a record, confirm it is discoverable by calling `SearchDiscoverableRegistryRecords` with a retry strategy that includes exponential backoff.
- Do not assume a record is missing from the registry if it does not appear in results immediately after approval. Call `GetRegistryRecord` to verify the record’s status.
- If you are integrating approval workflows through Amazon EventBridge and `UpdateRegistryRecordStatus`, add a brief delay before downstream systems query the discoverable APIs for the newly approved record.

###### Note

`SearchDiscoverableRegistryRecords` was named `SearchRegistryRecords` in the `bedrock-agentcore` namespace.

For general guidance on configuring retry behavior in AWS SDKs, see [Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md") in the _AWS SDKs and Tools Reference Guide_.

## How record attributes affect search relevance

AWS Agent Registry uses hybrid search that combines semantic understanding with keyword matching to return relevant results. If a record you expect to find does not appear in search results, understanding which record attributes influence search can help.

### Which record attributes are used for search

The following attributes from your registry record are used to determine search relevance:

- **Name** — Used for keyword matching. Clear, descriptive names that reflect what the resource does improve discoverability for exact and partial name lookups.
- **Description** — Used for both keyword and semantic matching. Descriptions written in natural language that explain the resource’s purpose and common use cases are more discoverable than terse technical labels.
- **Descriptors** — The full content of your protocol definition (MCP server definition, agent card, skill documentation, or custom JSON) is used for semantic matching. This includes tool names, tool descriptions, input parameter names, and capability summaries.
- **Record type and version** — Available as filterable fields. You can narrow results using metadata filters on `name`, `recordType`, and `recordVersion`.

### How search queries are processed

When you call `SearchDiscoverableRegistryRecords`, AWS Agent Registry runs two searches in parallel against the same set of indexed records and merges the results:

- **Semantic search** — Your query is converted into a vector representation and compared against the vector representations of indexed records. This finds conceptually related records even when the exact words in your query don’t appear in the record. For example, a query for "book a flight" can match a record named "travel-reservation-service."
- **Keyword search** — Your query is matched against the text content of record fields using traditional keyword relevance. This is effective for exact name lookups and specific technical terms. For example, a query for "weather-api-v2" matches records containing that exact text.

If you include metadata filters in your request, the filters are applied to both searches before results are scored and ranked. This means filters reduce the candidate set that both semantic and keyword search operate on, rather than filtering results after ranking.

### How results are ranked

Results from both semantic and keyword search are combined into a single ranked list and returned in order of relevance, with the most relevant record first. Each result’s final position is determined by its relevance across both searches — a record that ranks highly in both semantic and keyword results will appear higher than a record that ranks highly in only one. Within keyword search, the record name has the strongest influence on ranking, followed by the description and descriptor content, which contribute equally. Because both search modes always run and contribute to the final ranking, how you write your query affects which records surface. The following guidance can help you get better results depending on your intent.

### Writing effective search queries

**When you know the exact name or identifier** , use a short, specific query. Keyword search matches exact text against record names, descriptions, and descriptor content. Short queries like "weather-api-v2" or "pdf-processing" are effective for finding records by name.

**When you’re exploring by capability or use case** , use a natural language description of what you need. Semantic search understands conceptual intent, so queries like "find a tool that can book flights" or "extract structured data from PDF documents" can match relevant records even if those exact words don’t appear in the record metadata.

**Avoid mixing filter-like constraints with descriptive intent in the same query.** A query like "find all MCP servers for weather forecasts" sends the entire sentence through both semantic and keyword search. The semantic component interprets the full sentence as a conceptual intent, which can surface records that are conceptually related but don’t match the specific attribute you intended to constrain. Instead, use metadata filters for attribute-based constraints and keep the query focused on the topic. See [When to use metadata filters versus query text](#registry-search-filters-vs-query "#registry-search-filters-vs-query").

### Writing discoverable records

- Write descriptions that explain what the resource does and the problems it solves. Semantic search understands intent, so "helps customers track package deliveries" is more discoverable than "delivery-status-endpoint."
- Provide complete tool definitions for MCP servers. Tool descriptions and input parameter descriptions all contribute to search relevance.
- Include relevant keywords in your name and description. Keyword search matches exact text, so if consumers are likely to search for specific terms, make sure those terms appear in your record.

### When to use metadata filters versus query text

Use metadata filters when your intent is to constrain results by a known attribute such as record type, name, or version. Do not embed filter-like constraints in the query text itself. For example, if you want to find all MCP servers related to weather, use a metadata filter for the record type and a query for the topic:

```
{
  "searchQuery": "weather forecast",
  "filters": {
    "recordType": { "$eq": "MCP" }
  }
}
```

Avoid putting the constraint into the query text like "find all MCP servers for weather forecasts". Because longer queries lean toward semantic matching, the words "MCP servers" are interpreted as part of the conceptual intent rather than as an exact filter. This can cause the semantic component to return records that are conceptually related to the full sentence but don’t match the specific attribute you intended to filter on — for example, returning agent records about weather alongside MCP server records. The same applies to any attribute-based constraint. If you want records with a specific name, version, or type, use the corresponding metadata filter rather than including those terms in the query.

You can filter on the following fields:

- `name` — Match records by exact name.
- `recordType` — Match records by semantic type (`AGENT`, `MCP`, `SKILL`, `CUSTOM`).
- `recordVersion` — Match records by version string.

Filters support `$eq` (equals), `$ne` (not equals), and `$in` (matches any value in a list) operators, and can be combined using `$and` and `$or` logic.

For example, to search for weather-related MCP servers only:

```
{
  "searchQuery": "weather forecast",
  "filters": {
    "recordType": { "$eq": "MCP" }
  }
}
```

To exclude a specific resource type:

```
{
  "searchQuery": "<your query>",
  "filters": {
    "recordType": { "$ne": "CUSTOM" }
  }
}
```

To match any of several versions:

```
{
  "filters": {
    "recordVersion": { "$in": ["1.0", "1.1", "2.0"] }
  }
}
```

### Search returns only approved records

Only records in **Approved** status appear in search results and through the MCP endpoint. Records in Draft, Pending Approval, Rejected, or Deprecated status are not returned. If a recently approved record does not appear in results, see [Eventual consistency in AWS Agent Registry search](#registry-search-eventual-consistency "#registry-search-eventual-consistency").
