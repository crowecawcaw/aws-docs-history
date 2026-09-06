

# Browse approved records
<a name="registry-browse-records"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

As a consumer, you can browse the catalog of approved records in a registry using two data-plane APIs — `ListDiscoverableRegistryRecords` for paginated listing, and `BatchGetDiscoverableRegistryRecord` for bulk retrieval of full record content by record ID. Both APIs are only available under the `agent-registry` namespace and return only records whose latest revision has status **Approved**. Records in **Draft**, **Pending approval**, **Rejected**, or **Deprecated** status are not returned. To search records with a natural-language query, use `SearchDiscoverableRegistryRecords` instead. See [Search for registry records](registry-search-records.md).

**Note**  
 `ListDiscoverableRegistryRecords` and `BatchGetDiscoverableRegistryRecord` are only available under the `agent-registry` namespace. Registries created under the `bedrock-agentcore` namespace do not expose these APIs; use `SearchDiscoverableRegistryRecords`.

## List approved records
<a name="registry-browse-list"></a>

Use `ListDiscoverableRegistryRecords` to return paginated summaries of every approved record in a registry. Summaries do not include the record’s descriptors — use `BatchGetDiscoverableRegistryRecord` to fetch full descriptor content after identifying the records you need.

### Request parameters
<a name="registry-browse-list-parameters"></a>
+  **registryId** (required, path): ARN or ID of the registry to list from.
+  **maxResults** (optional): Maximum number of results per page. Valid range is 1–100.
+  **nextToken** (optional): Pagination token from a previous response. Omit for the first page.
+  **filters** (optional): A list of filter entries in the form `{"name": "<field>", "values": ["<value>"]}`. Supported filter names:
  +  `recordType` — Semantic type of the record. Valid values: `AGENT`, `MCP`, `SKILL`, `CUSTOM`.
  +  `descriptorType` — Primary descriptor key used by the record. Valid values: `a2aAgentCard`, `mcpServer`, `agentSkillsDefinition`, `custom`.

    Duplicate filter names are rejected. If you specify multiple values for a single filter, the values are joined by **OR**. If you specify multiple filters, the filters are joined by **AND**.

Each summary in the response contains: `registryArn`, `recordArn`, `recordId`, `name`, `displayName`, `description`, `recordType`, `recordVersion`, `status`, `createdAt`, `updatedAt`.

### Response ordering and pagination
<a name="registry-browse-list-ordering"></a>

Results are sorted alphabetically by record name.

 `ListDiscoverableRegistryRecords` does not guarantee dense pages. Any individual response can contain fewer than `maxResults` records, or zero records, even when more matching records exist. Continue calling the API with the returned `nextToken` on each subsequent request until the response contains no `nextToken` (or `nextToken` is `null`) to retrieve every matching record.

### Console
<a name="registry-browse-list-console"></a>

**Example**  

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Record directory**.

1. Choose the registry you want to browse. The page automatically calls `ListDiscoverableRegistryRecords` and displays the approved records in a paginated table.

1. (Optional) Use the **Properties** menu next to the search bar to filter by **Record type**.

1. Choose a record’s name to view its full descriptor content.
Browsing the approved-record catalog with `ListDiscoverableRegistryRecords` is only available in the `agent-registry` namespace. The older Bedrock-AgentCore console does not have a **Record directory** page or a browse feature. To find records in a registry created under the `bedrock-agentcore` namespace, use the **Search records** tab on the registry detail page — see [Search for registry records](registry-search-records.md).

**Note**  
The **Record directory** page requires IAM-based inbound authorization on the selected registry. For JWT-authorized registries, call `ListDiscoverableRegistryRecords` directly with an HTTP client and a valid JWT bearer token.

### AWS CLI
<a name="registry-browse-list-cli"></a>

```
aws agent-registry list-discoverable-registry-records \
  --registry-id "<registryARN>" \
  --filters '[{"name": "recordType", "values": ["MCP"]}]' \
  --max-results 50 \
  --region us-east-1
```

To page through results, pass the `nextToken` value from the previous response:

```
aws agent-registry list-discoverable-registry-records \
  --registry-id "<registryARN>" \
  --next-token "<tokenFromPreviousResponse>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-browse-list-sdk"></a>

```
import boto3

client = boto3.client('agent-registry')

paginator = client.get_paginator('list_discoverable_registry_records')

for page in paginator.paginate(
    registryId='<registryARN>',
    filters=[{'name': 'recordType', 'values': ['MCP']}]
):
    for record in page['registryRecords']:
        print(f"{record['displayName']} ({record['name']}) - {record['recordType']} v{record['recordVersion']}")
```

### HTTP client
<a name="registry-browse-list-http"></a>

```
curl -X POST "https://agent-registry.<region>.api.aws/registries/<registryARN>/discoverable-records-list" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <accessToken>" \
  -d '{
    "filters": [{"name": "recordType", "values": ["MCP"]}],
    "maxResults": 50
  }'
```

## Batch retrieve approved records
<a name="registry-browse-batch-get"></a>

Use `BatchGetDiscoverableRegistryRecord` to retrieve the full descriptor content for up to 100 record IDs in a single call. Common use case: after browsing with `ListDiscoverableRegistryRecords` and identifying the records you want, fetch their descriptors in one call rather than making one `SearchDiscoverableRegistryRecords` call per record.

### Request parameters
<a name="registry-browse-batch-get-parameters"></a>
+  **entries** (required): A list of registry-scoped record groups. At launch, exactly one entry is accepted (single registry per request); this is forward-compatible for cross-registry batching in the future.

  Each entry contains:
  +  **registryId** (required): ARN or ID of the registry.
  +  **recordIds** (required): List of 1–100 record ARNs or IDs to retrieve from the registry.

### Response
<a name="registry-browse-batch-get-response"></a>
+  **registryRecords**: Full record objects (with descriptors) for records that were successfully retrieved.
+  **errors**: A per-record error list. Empty when every requested record was returned successfully.

The call returns HTTP 200 even on partial failure — records that could not be retrieved appear in the `errors` list rather than causing the whole call to fail. Each error entry echoes `registryId` and `recordId` from the request, plus an `errorCode`:
+  **RESOURCE\_NOT\_FOUND** — The record does not exist, is deleted, or its latest revision is not **Approved**. Non-approved records are collapsed into this code so their existence is not disclosed to callers who lack visibility.
+  **ACCESS\_DENIED** — The caller is not authorized to read this specific record.
+  **INTERNAL\_ERROR** — A transient retrieval failure. Safe to retry the failed subset with exponential backoff.

Batch-level failures (the registry doesn’t exist, the caller has no access to the registry, unrecoverable service error) return through standard operation errors, not the per-record `errors` list.

### AWS CLI
<a name="registry-browse-batch-get-cli"></a>

```
aws agent-registry batch-get-discoverable-registry-record \
  --entries '[{"registryId": "<registryARN>", "recordIds": ["<recordId1>", "<recordId2>", "<recordId3>"]}]' \
  --region us-east-1
```

### AWS SDK
<a name="registry-browse-batch-get-sdk"></a>

```
import boto3

client = boto3.client('agent-registry')

response = client.batch_get_discoverable_registry_record(
    entries=[
        {
            'registryId': '<registryARN>',
            'recordIds': ['<recordId1>', '<recordId2>', '<recordId3>']
        }
    ]
)

for record in response['registryRecords']:
    print(f"Retrieved: {record['displayName']} ({record['recordId']})")

for error in response['errors']:
    print(f"Failed: {error['recordId']} ({error['errorCode']}): {error.get('message', '')}")
```

### HTTP client
<a name="registry-browse-batch-get-http"></a>

```
curl -X POST "https://agent-registry.<region>.api.aws/discoverable-records-batch" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <accessToken>" \
  -d '{
    "entries": [
      {
        "registryId": "<registryARN>",
        "recordIds": ["<recordId1>", "<recordId2>", "<recordId3>"]
      }
    ]
  }'
```