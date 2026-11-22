

# Using the Registry MCP endpoint

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Overview
<a name="registry-mcp-overview"></a>

Each registry exposes an MCP-compatible endpoint following the [2025-11-25 specification](https://modelcontextprotocol.io/specification/2025-11-25) on the Model Context Protocol website. The endpoint supports tool listing and tool invocation for searching registry records.

**Important**  
The MCP endpoint returns record metadata as publishers provide it. Before your agent installs a package, downloads from a repository, connects to an endpoint that a returned record references, or loads a skill package, validate it. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).

**Example**  

```
https://agent-registry.<region>.api.aws/registry/<registryId>/mcp
```

```
https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp
```

In the `agent-registry` namespace, the MCP endpoint exposes all three discovery data-plane APIs as MCP tools:
+  `search_discoverable_registry_records_paginated` — Search for approved records with a choice of search type, and page through the results.
+  `search_discoverable_registry_records` — Natural language search for approved records that returns one page of results.
+  `list_discoverable_registry_records` — Paginated listing of approved records.
+  `batch_get_discoverable_registry_record` — Bulk retrieval of full record content by record ID.

In the `bedrock-agentcore` namespace, only the `search_registry_records` tool is exposed. The following tables show the tool definitions:

**Example**  

```
Tool name: search_discoverable_registry_records_paginated

Description:
Searches discoverable registry records and returns a JSON object: registryRecords (best match first), searchType (the
search type that ran, also when you omit searchType) and, when more results may be available, nextToken. Use this
instead of search_discoverable_registry_records, which returns one page as a bare array without the search type or
paging. For the next page, call again with the same arguments plus nextToken. A page can hold fewer records than
maxResults, even none, while nextToken is present, so keep paging until nextToken is absent. A search returns at most
20 results in total with HYBRID or SEMANTIC and at most 1000 with KEYWORD. For a relevance search the first page is
usually enough; refine searchQuery or filter rather than paging through many pages. To list the records that match a
filter, most recently updated first, leave searchQuery empty, set filter and set searchType to KEYWORD.

Parameters:
- searchQuery: string - Search query: exact words such as a name, or a natural language description. Leave empty and
  set filter to list the records that match the filter; with searchType KEYWORD that lists up to 1000.
- searchType: string - How records are ranked against searchQuery. KEYWORD matches exact words, such as a record or
  tool name. SEMANTIC matches meaning, for a natural language description of a task. HYBRID (the default) combines
  both. Valid values: HYBRID, SEMANTIC, KEYWORD.
- maxResults: integer - Maximum number of results per page (default 10): up to 50 with searchType KEYWORD, up to 20
  with HYBRID or SEMANTIC
- filter: object - Optional metadata filter, with the same operators and fields as the filter of
  search_discoverable_registry_records.
- nextToken: string - Pagination token from a prior response of this tool. Pass it with the same arguments to get the
  next page.

---

Tool name: search_discoverable_registry_records

Description:
Searches discoverable registry records using natural language queries. Returns metadata for matching records. Returns
one page (up to 20 records) as a JSON array, without the search type it used or a token for more results. To page
through results, choose the search type, or see which search type ran, use
search_discoverable_registry_records_paginated.

Parameters:
- searchQuery (required): string - Natural language search query
- maxResults: integer - Maximum number of results to return (1-20, default 10)
- filter: object - Optional metadata filter using structured JSON operators. Supports field-level operators ($eq, $ne,
  $in) and logical operators ($and, $or). Filterable fields: name, recordType, recordVersion, and customMetadata.{key}
  (for example, customMetadata.environment or customMetadata.team). Example:
  {"recordType": {"$eq": "MCP"}, "customMetadata.environment": {"$eq": "prod"}}

---

Tool name: list_discoverable_registry_records

Description:
Returns paginated summaries of approved records in the registry. Summaries include record metadata but not descriptor
content. Use batch_get_discoverable_registry_record to fetch full descriptors after identifying the records you need.

Parameters:
- maxResults: integer - Maximum number of results per page (1-100, default 20)
- nextToken: string - Pagination token from a previous response. Omit for the first page.
- filters: array - Optional list of filter entries in the form {"name": "<field>", "values": ["<value>"]}. Supported
  filter names: recordType (valid values: AGENT, MCP, SKILL, CUSTOM) and descriptorType (valid values: a2aAgentCard,
  mcpServer, agentSkillsDefinition, custom). Duplicate filter names are rejected. If you specify multiple values for
  a single filter, the values are joined by OR. If you specify multiple filters, the filters are joined by AND.

---

Tool name: batch_get_discoverable_registry_record

Description:
Retrieves the full descriptor content for up to 100 approved records in a single call. Common use case: after
identifying records with list_discoverable_registry_records or search_discoverable_registry_records, fetch their full
descriptors in one call rather than making one call per record.

Parameters:
- recordIds (required): array - List of 1-100 record ARNs or IDs to retrieve from the registry.

The response returns HTTP 200 even on partial failure. Records that could not be retrieved appear in an errors list
with an errorCode (RESOURCE_NOT_FOUND, ACCESS_DENIED, or INTERNAL_ERROR) rather than causing the whole call to fail.
```

```
Tool name: search_registry_records

Description:
Searches for registry records using natural language queries. Returns metadata for matching records.

Parameters:
- searchQuery (required): string - Natural language search query
- maxResults: integer - Maximum number of results to return (1-20, default 10)
- filter: object - Optional metadata filter using structured JSON operators. Supports field-level operators ($eq, $ne,
  $in) and logical operators ($and, $or) on filterable fields (name, descriptorType, version). Example:
  {"descriptorType": {"$eq": "MCP"}}
```

For a SKILL record whose approved revision has a skill package, each record in the `registryRecords` list of the `batch_get_discoverable_registry_record` result also contains `artifact`, with `downloadUrl` (a presigned URL that is valid for up to 5 minutes) and `sha256` (the package checksum to verify the download against). The `search_discoverable_registry_records_paginated`, `search_discoverable_registry_records`, and `list_discoverable_registry_records` tools don’t return `artifact`. For more information, see [Download a skill package](registry-skill-package-download.md).

The `filter` parameter of `search_discoverable_registry_records_paginated` and `search_discoverable_registry_records` follows the same rules and limits as the `SearchDiscoverableRegistryRecords` API. See [Filter rules and limits](registry-search-records.md#registry-search-filter-rules). When a filter breaks these rules, the tool returns a result with `isError` set to `true` and the generic text `Error: Invalid request parameters` in its content. This text doesn’t name the rule that the filter broke.

You can connect to registry from an existing MCP client, such as Kiro, Claude, etc.

## Search with a search type and page through results
<a name="registry-mcp-search-paginated"></a>

The `search_discoverable_registry_records_paginated` tool runs the same search as the `SearchDiscoverableRegistryRecords` API, with the same search types, page sizes, and result limits. For more information, see [Choose a search type](registry-search-records.md#registry-search-types) and [Page through search results](registry-search-records.md#registry-search-pagination). Unlike `search_discoverable_registry_records`, it doesn’t require `searchQuery`: leave the query empty and set `filter` to list the records that match the filter.

The tool returns its result as a JSON object in the text content of the tool result:

```json
{
  "registryRecords": [ ... ],
  "searchType": "HYBRID",
  "nextToken": "<token>"
}
```
+  `registryRecords` — The matching records, best match first, with the same fields as the `search_discoverable_registry_records` result.
+  `searchType` — The search type that ran, including the default when you omit `searchType`.
+  `nextToken` — Present when more results might be available. To get the next page, call the tool again with the same arguments and add `nextToken`. A page can hold fewer records than `maxResults`, even none, while `nextToken` is present.

A `nextToken` works only with the tool that returned it, and only with the same `searchQuery`, `searchType`, and `filter`. It expires 15 minutes after the first page. The tool doesn’t accept a `nextToken` from the `SearchDiscoverableRegistryRecords` API, and the API doesn’t accept one from the tool.

If AWS Agent Registry becomes available in an AWS Region where semantic search isn’t available, the tool’s `searchType` parameter in that Region lists only `KEYWORD`, which is also the default there.

When the tool can’t run the search with the arguments you passed, it returns a result with `isError` set to `true` and a message that explains how to correct the call:
+  `nextToken is invalid or expired. Repeat the search without nextToken.` — The token has expired, or the arguments differ from the ones that returned it.
+  `searchType must be one of HYBRID, SEMANTIC, KEYWORD` — The `searchType` value isn’t valid.
+  `maxResults must be between 1 and 20 for searchType HYBRID` (or `SEMANTIC`) — The page size is above 20 for a `HYBRID` or `SEMANTIC` search.

A `maxResults` that isn’t an integer from 1 to 50, for any search type, is refused before the search runs: the tool returns a JSON-RPC error with code `-32602` (invalid params) instead of a tool result.

The following request lists the MCP records in a registry, 50 at a time, most recently updated first:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_discoverable_registry_records_paginated",
    "arguments": {
      "searchQuery": "",
      "searchType": "KEYWORD",
      "maxResults": 50,
      "filter": { "recordType": { "$eq": "MCP" } }
    }
  }
}
```

## Connect to OAuth-based registry MCP endpoint from an existing MCP client
<a name="registry-mcp-connect-oauth"></a>

### Permissions
<a name="registry-mcp-permissions-oauth"></a>

The MCP endpoint will use the same **CustomJWTAuthorizerConfiguration** to authorize the incoming requests.

The `.well-known/oauth-protected-resource` path is: `https://agent-registry.<region>.api.aws/.well-known/oauth-protected-resource/registry/<registryId>/mcp` (`https://bedrock-agentcore.<region>.amazonaws.com/.well-known/oauth-protected-resource/registry/<registryId>/mcp` for registries still on the `bedrock-agentcore` namespace).

The client can discover the metadata from `WWW-Authenticate` header as well:

**Example**  

```
www-authenticate: Bearer resource_metadata="https://agent-registry.<region>.api.aws/.well-known/oauth-protected-resource/registry/<registryId>/mcp"
```

```
www-authenticate: Bearer resource_metadata="https://bedrock-agentcore.<region>.amazonaws.com/.well-known/oauth-protected-resource/registry/<registryId>/mcp"
```

Once you obtained the access token, you can validate it:

**Example**  

```bash
curl -s -X POST "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_discoverable_registry_records","arguments":{"searchQuery":"weather"}}}'
```

```bash
curl -s -X POST "https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_registry_records","arguments":{"searchQuery":"weather"}}}'
```

Depending on your authorization server and organization’s security requirements, you may choose one of the following approaches to configure your MCP client:

1. Bearer token: use a separate process to fetch bearer token and configure it in MCP client header

1. Pre-registered client: create a client in your authorization server, and allowlist the client on registry’s configuration.

1. Dynamic client registration: if your authorization server supports dynamic client registration (DCR), you can allowlist the audience in registry’s configuration.

### OAuth-based MCP client setup
<a name="registry-mcp-connect-oauth-setup"></a>

#### Use bearer token
<a name="registry-mcp-connect-oauth-bearer"></a>

In most IDEs, you can configure authorization header bearer token in an mcp configuration. For example, Kiro IDE supports environment variables using the `${ENV_VAR}` syntax. For details, see [Securing MCP connections](https://kiro.dev/blog/introducing-remote-mcp/#securing-mcp-connections) on the Kiro website. You can use following example:

**Example**  

```json
{
  "mcpServers": {
    "my-registry": {
      "type": "http",
      "url": "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp",
      "headers": {
        "Authorization": "Bearer ${ACCESS_TOKEN}"
      }
    }
  }
}
```

```json
{
  "mcpServers": {
    "my-registry": {
      "type": "http",
      "url": "https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp",
      "headers": {
        "Authorization": "Bearer ${ACCESS_TOKEN}"
      }
    }
  }
}
```

#### Pre-registered client
<a name="registry-mcp-connect-oauth-preregistered"></a>

You can create a new client based on authorization code grant in your authorization server, and use the client to access registry. For example, [create a client in Cognito](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-cognito.html) user pool.

Once you have the client ID, make sure you allowlist it in registry:

**Example**  

```bash
aws agent-registry-control update-registry \
  --registry-id <registryId> \
  --discovery-configuration '{
    "authorizerConfiguration": {
      "optionalValue": {
        "customJWTAuthorizer": {
          "discoveryUrl": "https://<example-domain>/.well-known/openid-configuration",
          "allowedClients": ["<client-id>"]
        }
      }
    }
  }'
```

```bash
aws bedrock-agentcore-control update-registry \
  --registry-id <registryId> \
  --authorizer-configuration '{
    "optionalValue": {
      "customJWTAuthorizer": {
        "discoveryUrl": "https://<example-domain>/.well-known/openid-configuration",
        "allowedClients": ["<client-id>"]
      }
    }
  }'
```

Then you can configure your MCP client if it supports specifying clientId. An example in Claude code:

**Example**  

```json
{
  "mcpServers": {
    "pre-registered-registry": {
      "type": "http",
      "url": "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp",
      "oauth": {
        "clientId": "<client-id>",
        "callbackPort": "<port-number>"
      }
    }
  }
}
```

```json
{
  "mcpServers": {
    "pre-registered-registry": {
      "type": "http",
      "url": "https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp",
      "oauth": {
        "clientId": "<client-id>",
        "callbackPort": "<port-number>"
      }
    }
  }
}
```

**Note**  
Some authorization servers like Auth0 and Cognito don’t let you configure a range of ports as allowed redirect URIs, so you need to explicitly set one in the preregistered client’s allowed redirect/callback URL, as well as in the mcp.json.

#### Dynamic client registration
<a name="registry-mcp-connect-oauth-dcr"></a>

Most MCP client applications support dynamic client registration. In this case, you should NOT specify `allowedClients` value in registry. Instead, you can choose to set `allowedAudience`. The value can be the same as your MCP registry. You should configure your authorization server to issue JWT with `aud` field with the same value as in `allowedAudience`.

**Example**  

```bash
aws agent-registry-control update-registry \
  --registry-id <registryId> \
  --discovery-configuration '{
    "authorizerConfiguration": {
      "optionalValue": {
        "customJWTAuthorizer": {
          "discoveryUrl": "https://<example-domain>/.well-known/openid-configuration",
          "allowedAudience": ["https://agent-registry.<region>.api.aws/registry/<registryId>/mcp"]
        }
      }
    }
  }'
```

```bash
aws bedrock-agentcore-control update-registry \
  --registry-id <registryId> \
  --authorizer-configuration '{
    "optionalValue": {
      "customJWTAuthorizer": {
        "discoveryUrl": "https://<example-domain>/.well-known/openid-configuration",
        "allowedAudience": ["https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp"]
      }
    }
  }'
```

Then you can configure your MCP client simply using an url:

**Example**  

```json
{
  "mcpServers": {
    "dcr-registry": {
      "type": "http",
      "url": "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp"
    }
  }
}
```

```json
{
  "mcpServers": {
    "dcr-registry": {
      "type": "http",
      "url": "https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp"
    }
  }
}
```

Common errors when you setup dynamic client registration:
+ You must ensure the authorization server supports dynamic client registration.
+ The authorization server must issue JWT with `aud` field, which is allowed in your registry’s CustomJWTAuthorizerConfiguration.
+ Define the OAuth scopes in your MCP client configuration, because the registry doesn’t return a scope challenge in the `www-authenticate` header. Some MCP clients support explicitly defining `oauthScopes` in configuration, such as [Kiro](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#oauth-configuration).

## Connect to IAM-based registry MCP endpoint from an existing MCP client
<a name="registry-mcp-connect-iam"></a>

### Permissions
<a name="registry-mcp-permissions-iam"></a>

For MCP initialization and tool listing:

**Example**  

```json
{
    "Effect": "Allow",
    "Action": "agent-registry:InvokeRegistryMcp",
    "Resource": "arn:aws:agent-registry:*:<account>:registry/*"
}
```

```json
{
    "Effect": "Allow",
    "Action": "bedrock-agentcore:InvokeRegistryMcp",
    "Resource": "arn:aws:bedrock-agentcore:*:<account>:registry/*"
}
```

For searching via MCP tool invocation, with either `search_discoverable_registry_records_paginated` or `search_discoverable_registry_records`, you also need:

**Example**  

```json
{
    "Effect": "Allow",
    "Action":
    [
        "agent-registry:InvokeRegistryMcp",
        "agent-registry:SearchDiscoverableRegistryRecords"
    ],
    "Resource": "arn:aws:agent-registry:*:<account>:registry/*"
}
```

```json
{
    "Effect": "Allow",
    "Action":
    [
        "bedrock-agentcore:InvokeRegistryMcp",
        "bedrock-agentcore:SearchRegistryRecords"
    ],
    "Resource": "arn:aws:bedrock-agentcore:*:<account>:registry/*"
}
```

You can verify permission with command:

**Example**  

```bash
curl -s -X POST "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp" \
  -H "Content-Type: application/json" \
  -H "X-Amz-Security-Token: ${AWS_SESSION_TOKEN}" \
  --aws-sigv4 "aws:amz:<region>:agent-registry" \
  --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_discoverable_registry_records","arguments":{"searchQuery":"weather"}}}'
```

```bash
curl -s -X POST "https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp" \
  -H "Content-Type: application/json" \
  -H "X-Amz-Security-Token: ${AWS_SESSION_TOKEN}" \
  --aws-sigv4 "aws:amz:<region>:bedrock-agentcore" \
  --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_registry_records","arguments":{"searchQuery":"weather"}}}'
```

### IAM-based MCP client setup
<a name="registry-mcp-connect-iam-setup"></a>

You can use [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) on the GitHub website to connect to an IAM-based registry. For example, in Kiro mcp.json:

**Example**  

```json
{
  "mcpServers": {
    "iam-based-registry": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp",
        "--service",
        "agent-registry",
        "--region",
        "<region>",
        "--profile",
        "my-profile"
      ]
    }
  }
}
```

```json
{
  "mcpServers": {
    "iam-based-registry": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp",
        "--service",
        "bedrock-agentcore",
        "--region",
        "<region>",
        "--profile",
        "my-profile"
      ]
    }
  }
}
```

## Develop your own MCP client
<a name="registry-mcp-develop-client"></a>

For more code references of how to invoke the Registry MCP endpoint, including from popular IDEs like Kiro or Claude Code, please refer to sample code references in the public code repository.