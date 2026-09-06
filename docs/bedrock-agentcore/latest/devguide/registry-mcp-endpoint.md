

# Using the Registry MCP endpoint
<a name="registry-mcp-endpoint"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Overview
<a name="registry-mcp-overview"></a>

Each registry exposes an MCP-compatible endpoint following the [2025-11-25 specification](https://modelcontextprotocol.io/specification/2025-11-25) on the Model Context Protocol website. The endpoint supports tool listing and tool invocation for searching registry records.

**Example**  

```
https://agent-registry.<region>.api.aws/registry/<registryId>/mcp
```

```
https://bedrock-agentcore.<region>.amazonaws.com/registry/<registryId>/mcp
```

In the `agent-registry` namespace, the MCP endpoint exposes all three discovery data-plane APIs as MCP tools:
+  `search_discoverable_registry_records` — Natural language search for approved records.
+  `list_discoverable_registry_records` — Paginated listing of approved records.
+  `batch_get_discoverable_registry_record` — Bulk retrieval of full record content by record ID.

In the `bedrock-agentcore` namespace, only the `search_registry_records` tool is exposed. The following tables show the tool definitions:

**Example**  

```
Tool name: search_discoverable_registry_records

Description:
Searches for approved registry records using natural language queries. Returns metadata for matching records.

Parameters:
- searchQuery (required): string - Natural language search query
- maxResults: integer - Maximum number of results to return (1-20, default 10)
- filter: object - Optional metadata filter using structured JSON operators. Supports field-level operators ($eq, $ne,
  $in) and logical operators ($and, $or) on filterable fields (name, recordType, recordVersion). Example:
  {"recordType": {"$eq": "MCP"}}

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

You can connect to registry from an existing MCP client, such as Kiro, Claude, etc.

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

```
curl -s -X POST "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_discoverable_registry_records","arguments":{"searchQuery":"weather"}}}'
```

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
{
  "mcpServers": {
    "dcr-registry": {
      "type": "http",
      "url": "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp"
    }
  }
}
```

```
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
+ Currently registry does not return scope challenge in www-authenticate header. Some MCP clients support explicitly defining `oauthScopes` in configuration, such as [Kiro](https://kiro.dev/docs/cli/custom-agents/configuration-reference/#oauth-configuration).

## Connect to IAM-based registry MCP endpoint from an existing MCP client
<a name="registry-mcp-connect-iam"></a>

### Permissions
<a name="registry-mcp-permissions-iam"></a>

For MCP initialization and tool listing:

**Example**  

```
{
    "Effect": "Allow",
    "Action": "agent-registry:InvokeRegistryMcp",
    "Resource": "arn:aws:agent-registry:*:<account>:registry/*"
}
```

```
{
    "Effect": "Allow",
    "Action": "bedrock-agentcore:InvokeRegistryMcp",
    "Resource": "arn:aws:bedrock-agentcore:*:<account>:registry/*"
}
```

For searching via MCP tool invocation, you also need:

**Example**  

```
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

```
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

```
curl -s -X POST "https://agent-registry.<region>.api.aws/registry/<registryId>/mcp" \
  -H "Content-Type: application/json" \
  -H "X-Amz-Security-Token: ${AWS_SESSION_TOKEN}" \
  --aws-sigv4 "aws:amz:<region>:agent-registry" \
  --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_discoverable_registry_records","arguments":{"searchQuery":"weather"}}}'
```

```
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

```
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

```
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