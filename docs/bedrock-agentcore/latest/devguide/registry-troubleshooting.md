# Troubleshooting

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Schema validation errors

When creating different types of records, you may see validation exception for the descriptors. See [Supported record types](registry-supported-record-types.md "registry-supported-record-types.md") section for valid schemas.

Common errors:

- "Schema version '0.3.0' is not supported for descriptor type 'a2a'." — The schemaVersion field value should be `0.3` instead of `0.3.0`. This aligns with the [official A2A protocol version description](https://a2a-protocol.org/latest/specification/#446-agentinterface "https://a2a-protocol.org/latest/specification/#446-agentinterface") on the A2A Protocol website: "Use the latest supported minor version per major version".
- "Schema validation failed: content is not in compliance with schema version '0.3' for descriptor type 'a2a'." — You can find the schema on [Supported record types](registry-supported-record-types.md "registry-supported-record-types.md"). Note that the content will be validated against #/definitions/AgentCard in the json schema.

## Record synchronization errors

When you create or update record using synchronization feature, the record may transition to CREATE\_FAILED or UPDATE\_FAILED status, with a `statusReason` explaining what happened.

At high level, errors can be categorized as: permission errors, connection errors, validation errors, and server side errors.

### Permission errors

Synchronization configuration is wrong or expired:

- "Unable to connect to MCP server because caller credentials have expired." — Your credentials for the create or update API have expired. You can retry with the UpdateRegistryRecord API.
- "Received exception from GetWorkloadAccessToken API: <detailed message>" — The registry calls the [GetWorkloadAccessToken](../APIReference/API_GetWorkloadAccessToken.md "../APIReference/API_GetWorkloadAccessToken.md") API on your behalf. Refer to the detailed message for the specific error. See [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md") if you see an access denied error.
- "Unable to parse credential provider ARN: <arn>" — The credential provider ARN is malformed. Provide a valid [credential provider](identity-outbound-credential-provider.md "identity-outbound-credential-provider.md") ARN created from AgentCore Identity.
- "Received exception from GetResourceOauth2Token API: <detailed message>" — The registry calls the [GetResourceOauth2Token](../APIReference/API_GetResourceOauth2Token.md "../APIReference/API_GetResourceOauth2Token.md") API on your behalf. Refer to the detailed message for the specific error. See [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md") if you see an access denied error.
- "Unable to assume the provided IAM role for MCP server authorization." — The registry calls the AssumeRole API on your behalf. See [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md") for the expected IAM permissions. For example, you must have the `iam:PassRole` permission.

### Connection errors

Can’t reach the server:

- "Failed to fetch agent card from URL: %s" — A2A IOException
- "MCP server returned HTTP <code>" — non-200/202 HTTP response from the MCP server. Please check if the URL is correct and the MCP server can be connected.
- "The provided URL resolves to a non-public IP address" — Registry only supports connecting to public IP address servers.
- "Failed to connect to MCP server" — IOException/connection failure
- "Invalid MCP server URL" — malformed URL
- "Failed to initialize MCP connection" — initialize request exception
- "Failed to send initialized notification" — notification exception
- "Failed to list tools from MCP server" — tools/list exception
- "MCP server tools/list pagination timed out" — registry only supports at most 30 seconds when paginating tools from MCP server. Contact AWS support if your MCP server needs more time for synchronization.

### Validation errors

Server responded but content is not supported:

- "Failed to parse agent card JSON" — A2A content empty or malformed JSON
- "Agent card exceeds maximum size limit" — A2A response too large
- "Failed to parse MCP server response JSON" — MCP content empty or malformed
- "MCP server returned invalid response: missing result" — MCP JSON-RPC missing result
- "MCP server response exceeds maximum allowed size" — MCP response too large
- "Descriptor type %s does not support URL synchronization" — unsupported descriptor type

### Server side errors

- "Unknown error" — This is a server side error. Please retry later or contact AWS support for help.
