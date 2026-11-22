

# Search publicly discoverable records

With public search, AWS-authenticated callers can discover records that organizations have promoted to the public discovery plane. This topic introduces the public search surface, contrasts it with the enterprise search you already use, and explains what public search does and does not return.

**Important**  
Public search is ** AWS-authenticated**. Any AWS-authenticated caller can query it, but a caller must still present valid AWS credentials. Public search is not anonymous and does not allow unauthenticated access.

## Enterprise search and public search
<a name="registry-public-search-surfaces"></a>

 AWS Agent Registry has two search surfaces. They answer different questions and return different sets of records.

The following table compares enterprise search and public search.


|  | Enterprise search (existing) | Public search (new) | 
| --- | --- | --- | 
| Scope | Records within one organization’s registry. | Records promoted to the public discovery plane, across organizational boundaries. | 
| Returns | Records whose status is `APPROVED` for internal use. | Records that are `APPROVED` *and* whose Publisher association is `PUBLIC_ASSOCIATION_APPROVED`. | 
| Authorization | The registry’s IAM or JWT authorization configuration. |  AWS-authenticated. Any caller with valid AWS credentials can query it. | 
| API |  `SearchDiscoverableRegistryRecords`  |  `SearchPublicRecords`  | 

Enterprise search is documented in [Search for registry records](registry-search-records.md). The rest of this topic covers public search.

## What public search returns
<a name="registry-public-search-returned"></a>

Public search returns only records that are published under a verified Publisher — that is, records that are `APPROVED` and whose Publisher association is `PUBLIC_ASSOCIATION_APPROVED`. Records that are approved for internal use only never appear in public search. Promoting a record to public discovery is the only way to make it visible to callers outside your organization. For more information, see [Promote a record to public discovery](registry-promote-to-public.md).

## Query modes
<a name="registry-public-search-modes"></a>

Public search uses the same hybrid approach as enterprise search. It runs a semantic search and a lexical (keyword) search against the indexed public records and merges the results into a single ranked list.
+  **Semantic search** finds conceptually related records even when the query words do not appear in the record.
+  **Lexical search** matches exact names and specific technical terms.

For guidance on writing effective queries and discoverable records, see [How record attributes affect search relevance](registry-search-records.md#registry-search-relevance).

## Where you can run public search
<a name="registry-public-search-access"></a>

Because public search is available to any AWS-authenticated caller, you can run it from a range of clients:
+ Agents at runtime, to find verified agents and tools published by other organizations.
+ Integrated development environments and coding assistants.
+ API clients that call `SearchPublicRecords` directly.

## Regional endpoints
<a name="registry-public-search-endpoints"></a>

The public discovery data-plane endpoint, `agent-discovery.<region>.api.aws`, serves public search. This endpoint is distinct from the enterprise registry data-plane endpoint, `agent-registry.<region>.api.aws`. At general availability, public search is available through the following Regional endpoints:
+  `agent-discovery.us-east-1.api.aws` 
+  `agent-discovery.eu-west-1.api.aws` 
+  `agent-discovery.ap-northeast-1.api.aws` 

## Run a public search
<a name="registry-public-search-run"></a>

The public search API is available only in the `agent-registry` namespace.

### Console
<a name="registry-public-search-console"></a>

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the navigation pane, choose **Public discovery**.

1. In the search bar, enter your query. The console calls `SearchPublicRecords` and displays ranked results.

1. Choose a record to view its public details and the Publisher that it is published under.

### AWS CLI
<a name="registry-public-search-cli"></a>

The following AWS CLI command runs a public search.

```bash
aws agent-registry search-public-records \
  --search-query "travel booking agent" \
  --max-results 10 \
  --region us-east-1
```

### AWS SDK
<a name="registry-public-search-sdk"></a>

The following example runs a public search by using the AWS SDK for Python.

```python
import boto3

client = boto3.client('agent-registry')

response = client.search_public_records(
    searchQuery='travel booking agent',
    maxResults=10
)
for record in response['records']:
    print(f"{record['name']} - {record['publisherIdentifier']}")
```