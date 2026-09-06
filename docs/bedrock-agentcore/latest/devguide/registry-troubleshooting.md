

# Troubleshooting
<a name="registry-troubleshooting"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Schema validation errors
<a name="registry-troubleshooting-schema-validation"></a>

When creating different types of records, you may see validation exception for the descriptors. See [Supported record types](registry-supported-record-types.md) section for valid schemas.

Common errors:
+ "Schema version '0.3.0' is not supported for descriptor type 'a2a'." — The schemaVersion field value should be `0.3` instead of `0.3.0`. This aligns with the [official A2A protocol version description](https://a2a-protocol.org/latest/specification/#446-agentinterface) on the A2A Protocol website: "Use the latest supported minor version per major version".
+ "Schema validation failed: content is not in compliance with schema version '0.3' for descriptor type 'a2a'." — You can find the schema on [Supported record types](registry-supported-record-types.md). Note that the content will be validated against \#/definitions/AgentCard in the json schema.

## Record synchronization errors
<a name="registry-troubleshooting-sync-errors"></a>

When you create or update record using synchronization feature, the record may transition to CREATE\_FAILED or UPDATE\_FAILED status, with a `statusReason` explaining what happened.

At high level, errors can be categorized as: permission errors, connection errors, validation errors, and server side errors.

### Permission errors
<a name="registry-troubleshooting-sync-permission"></a>

Synchronization configuration is wrong or expired:
+ "Unable to connect to MCP server because caller credentials have expired." — Your credentials for the create or update API have expired. You can retry with the UpdateRegistryRecord API.
+ "Received exception from GetWorkloadAccessToken API: <detailed message>" — The registry calls the [GetWorkloadAccessToken](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessToken.html) API on your behalf. Refer to the detailed message for the specific error. See [Synchronize records from external sources](registry-sync-records.md) if you see an access denied error.
+ "Unable to parse credential provider ARN: <arn>" — The credential provider ARN is malformed. Provide a valid [credential provider](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html) ARN created from AgentCore Identity.
+ "Received exception from GetResourceOauth2Token API: <detailed message>" — The registry calls the [GetResourceOauth2Token](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceOauth2Token.html) API on your behalf. Refer to the detailed message for the specific error. See [Synchronize records from external sources](registry-sync-records.md) if you see an access denied error.
+ "Unable to assume the provided IAM role for MCP server authorization." — The registry calls the AssumeRole API on your behalf. See [Synchronize records from external sources](registry-sync-records.md) for the expected IAM permissions. For example, you must have the `iam:PassRole` permission.

### Connection errors
<a name="registry-troubleshooting-sync-connection"></a>

Can’t reach the server:
+ "Failed to fetch agent card from URL: %s" — A2A IOException
+ "MCP server returned HTTP <code>" — non-200/202 HTTP response from the MCP server. Please check if the URL is correct and the MCP server can be connected.
+ If the status code is 401 or 403, verify that you have configured the correct credential provider and that your credentials have permission to connect to the MCP server. To troubleshoot, acquire the credentials manually and connect directly to the MCP server.
+ "The provided URL resolves to a non-public IP address" — Registry only supports connecting to public IP address servers.
+ "Failed to connect to MCP server" — IOException/connection failure
+ "Invalid MCP server URL" — malformed URL
+ "Failed to initialize MCP connection" — initialize request exception
+ "Failed to send initialized notification" — notification exception
+ "Failed to list tools from MCP server" — tools/list exception
+ "MCP server tools/list pagination timed out" — registry only supports at most 30 seconds when paginating tools from MCP server. Contact AWS support if your MCP server needs more time for synchronization.

### Validation errors
<a name="registry-troubleshooting-sync-validation"></a>

Server responded but content is not supported:
+ "Failed to parse agent card JSON" — A2A content empty or malformed JSON
+ "Agent card exceeds maximum size limit" — A2A response too large
+ "Failed to parse MCP server response JSON" — MCP content empty or malformed
+ "MCP server returned invalid response: missing result" — MCP JSON-RPC missing result
+ "MCP server response exceeds maximum allowed size" — MCP response too large
+ "Descriptor type %s does not support URL synchronization" — unsupported descriptor type

### Server side errors
<a name="registry-troubleshooting-sync-server"></a>
+ "Unknown error" — This is a server side error. Please retry later or contact AWS support for help.

## Auto-detection errors
<a name="registry-troubleshooting-auto-detection"></a>

### "Creating an organization-scoped registry requires the caller to be part of an AWS Organization."
<a name="registry-troubleshooting-auto-detection-not-in-org"></a>

The account creating the registry isn’t a member of an AWS Organization (for example, it’s a standalone account). Create the registry from an account that belongs to your organization.

### "Auto-detection preconditions are not satisfied for this organization."
<a name="registry-troubleshooting-auto-detection-preconditions"></a>

The organization doesn’t yet meet the auto-detection preconditions, or they haven’t finished propagating. Confirm that trusted access is enabled for auto-detection and that you’re creating the registry from the management account or a registered delegated administrator, then retry after a short wait. See [Enabling auto-detection across your organization](registry-organizations.md#registry-organizations-enabling).

### "An organization-scoped registry already exists for this account."
<a name="registry-troubleshooting-auto-detection-already-exists-account"></a>

This account already owns an organization-scoped registry, and an account can have only one. Use the existing registry, or delete it before creating another. If you can’t find the registry in this account, see [Locating an existing organization-scoped registry](#registry-troubleshooting-auto-detection-find-existing).

### "Another organization-scoped registry with active auto-detection already exists for this organization."
<a name="registry-troubleshooting-auto-detection-already-exists-org"></a>

Another account in your organization already owns an organization-scoped registry with active auto-detection, and an organization can have only one at a time. For security reasons, the error message does not name the account that owns the existing registry. To find it and choose how to resolve the conflict, see [Locating an existing organization-scoped registry](#registry-troubleshooting-auto-detection-find-existing).

### Locating an existing organization-scoped registry
<a name="registry-troubleshooting-auto-detection-find-existing"></a>

When `CreateRegistry` reports that an organization-scoped registry already exists — either in your account or somewhere else in your organization — the error does not name the specific registry or the account that owns it. Find the existing registry first, then decide how to resolve the conflict.

An organization-scoped registry is normally owned by one of these accounts:
+ The organization’s **management account**.
+ The account currently registered as the **delegated administrator** for AWS Agent Registry.

Ask an administrator with access to those accounts to list registries in the same Region as the failing call, and look for one whose `autoDetectionConfiguration.scope` is `ORGANIZATION`:

```
aws agent-registry-control list-registries --region us-east-1
```

From the management account, confirm which account is currently the delegated administrator:

```
aws organizations list-delegated-administrators \
  --service-principal agent-registry.amazonaws.com
```

The conflict only applies within the same Region — a registry in `us-east-1` does not prevent creating one in `us-west-2`.

Once you locate the existing registry, choose one of the following paths:
+  **Share and reuse it.** Have the owning account grant your account access using AWS RAM, and manage records in the shared registry instead of creating a new one. See [Sharing a registry across accounts with AWS RAM](registry-cross-account-sharing.md).
+  **Free the slot without deleting.** The owning account sets `autoDetectionConfiguration.enabled` to `false` on the existing registry; after the update takes effect, retry `CreateRegistry`. See [Disable auto-detection on the registry](registry-organizations.md#registry-organizations-disable).
+  **Delete the existing registry.** If it’s no longer needed, the owning account deletes it. See [Turning off auto-detection](registry-organizations.md#registry-organizations-turning-off) for the teardown order.

### `CreateRegistry` fails even though trusted access is enabled and the delegated administrator is registered
<a name="registry-troubleshooting-auto-detection-slr-missing"></a>

Confirm the management account has the AWS Agent Registry service-linked role (`AWSServiceRoleForAgentRegistry`). It must exist in the management account before an organization-scoped registry can be created, even when the delegated administrator is the one creating it. See [Step 1: Enable trusted access and create the service-linked role](registry-organizations.md#registry-organizations-step1).

### The registry is `READY` but records aren’t appearing
<a name="registry-troubleshooting-auto-detection-no-records"></a>

Confirm the registry’s auto-detection status is `ACTIVE` (with `get-registry`) and that the member accounts contain supported resource types (AgentCore Runtimes or Gateways). Allow time for discovery to complete — on first setup, the initial discovery of preexisting resources can take up to 20 minutes.

### Auto-detection status still shows "The registry’s delegated administrator account was deregistered" after a delegated administrator is re-registered
<a name="registry-troubleshooting-auto-detection-da-deregistered-status"></a>

When the management account deregisters the delegated administrator that owns an organization-scoped registry, AWS Agent Registry turns auto-detection off on that registry and records the status reason `The registry’s delegated administrator account was deregistered.` This status reason describes *why* auto-detection was originally disabled — it is a historical record and is not refreshed when the organization state later changes.

If a delegated administrator is registered again, the registry’s auto-detection does not resume automatically and the status reason continues to display the deregistration message. This is expected in each of the following situations:
+ The same account is re-registered as the delegated administrator.
+ A different account is registered as the delegated administrator — including when that account already owns its own organization-scoped registry with auto-detection previously disabled.
+ No new delegated administrator is registered, and the management account owns an organization-scoped registry directly.

To resume auto-detection, the account that owns the affected registry must explicitly set `enabled` back to `true`. Only one organization-scoped registry per Region can have `autoDetection.status` set to `ACTIVE` in an organization, so if multiple registries are eligible, re-enable auto-detection only on the one you want to keep active.

```
aws agent-registry-control update-registry \
  --registry-id <registry-id-or-arn> \
  --auto-detection-configuration '{"optionalValue":{"scope":"ORGANIZATION","enabled":true}}' \
  --region us-east-1
```

For the full lifecycle, see [Turning off auto-detection](registry-organizations.md#registry-organizations-turning-off).

### "Registry cannot be deleted while auto-detection is enabled. Disable auto-detection first."
<a name="registry-troubleshooting-auto-detection-delete-blocked"></a>

You must disable auto-detection before you can delete an organization-scoped registry. To delete the registry, complete these steps in order:

1. Disable auto-detection on the registry (set `autoDetectionConfiguration.enabled` to `false`).

1. Delete all registry records.

1. Delete the registry.

For more information, see [Disable auto-detection on the registry](registry-organizations.md#registry-organizations-disable).