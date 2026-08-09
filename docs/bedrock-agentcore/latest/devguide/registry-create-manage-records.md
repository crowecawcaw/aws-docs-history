# Create and manage records

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Create a registry record

### Console

###### Example

AWS Agent Registry namespace

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1# "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#").
2. In the **Registry records** section, choose **Create record**.
3. Choose a source type:

   1. **Synchronize from endpoint** — Provide an endpoint URL and optional credentials to invoke the endpoint, and the registry fetches metadata from the source. Available for MCP and Agent record types only. To update the record after the source changes, you must manually trigger synchronization. See [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md") for details.
   2. **Manual** — Manually configure the record details and protocol configuration.

**Synchronize from endpoint**

1. Under **Record details**, select the record type: **MCP** or **Agent**.

###### Note

Synchronization is only supported for MCP and Agent record types. Agent Skills and Custom record types do not support synchronization — use the Manual source type instead. 2. Enter the **Endpoint** URL. Must be a valid HTTPS URL. 3. Under **Credential type**, choose how the registry authorizes with the endpoint:

    1. **IAM** — Provide a **Role ARN** for SigV4 signing and a **Service** name (for example, `agent-registry`, `execute-api`, `lambda`). Optionally specify a **Region** for signing.
    2. **OAuth** — Select or enter a **Credential provider** ARN from AgentCore Identity. Optionally configure **Scopes** and **Custom parameters** under Additional configuration.
    3. **None** — No authorization (for public endpoints).

4. Choose **Create record**.

The record is created in CREATING status. The registry connects to the endpoint, extracts metadata, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field on the record detail page. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors "registry-troubleshooting.md#registry-troubleshooting-sync-errors"). To update the record when the source changes, choose **Manage**, then choose **Synchronization** on the record detail page, or choose **Manage → Edit** and select **Re-sync from endpoint**.

For AWS CLI and SDK examples of creating records with synchronization, see [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md").

**Manual**

1. In the **Record details** section, for **Name**, enter a unique name for the record. The name must be unique within the registry — the combination of `Name` and `Record version` must be unique. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 255 characters.
2. (Optional) For **Display name**, enter a human-readable label for the record. This appears in the registry records table and search results alongside the record’s technical name.
3. (Optional) For **Description**, enter a description for the record. The description can be 1 to 4,096 characters.
4. For **Record version**, enter a version identifier for the record (for example, `1.0.0` or `v2.1`).
5. In the **Record type and descriptor** section:

   1. Under **Type**, select the semantic type of the record. The type determines which primary descriptor keys are valid.

      - **MCP** – Protocol designed for AI tool and agent communications. Handles context management and structured message formats.
      - **Agent** – Protocol designed for secure agent-to-agent interactions. Enables distributed workflows and information exchange.
      - **Skills** – Register agent skills with markdown documentation and an optional structured definition.
      - **Custom** – Custom protocol implementation for specialized communication patterns. Define your own interface specification and integration requirements.

   2. Under **Descriptor**, choose the shape of the record’s descriptor data. Available options depend on the **Type** you selected:

      - **MCP** → **MCP server** or **Custom**
      - **Agent** → **A2A Agent Card**, **MCP server**, or **Custom**
      - **Skills** → **Agent skills definition** or **Custom**
      - **Custom** → **Custom**

6. A descriptor-specific editor appears based on your **Descriptor** selection. Enter your protocol configuration in JSON format. For **MCP server** and **A2A Agent Card** descriptors, toggle **Show official schema** to display the reference schema side-by-side. The console validates your JSON against the official schema and shows inline errors (for example, "Missing property 'name'") with a **Diagnose with Amazon Q** button. For per-descriptor configuration details, see [Supported record types](registry-supported-record-types.md "registry-supported-record-types.md").
7. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.
8. Choose one of:

   1. **Create as draft** — Creates the record in Draft status.
   2. **Create and submit for approval** — Creates the record and immediately submits it for approval.

Amazon Bedrock AgentCore namespace (to be deprecated)

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1# "https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#").
2. In the **Registry records** section, choose **Create record**.
3. Choose a source type:

   1. **Synchronize from endpoint** — Provide an endpoint URL and optional credentials to invoke the endpoint, and the registry fetches metadata from the source. Available for MCP and Agent record types only. To update the record after the source changes, you must manually trigger synchronization. See [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md") for details.
   2. **Manual** — Manually configure the record details and protocol configuration.

**Synchronize from endpoint**

1. Under **Record details**, select the record type: **MCP** or **Agent**.

###### Note

Synchronization is only supported for MCP and Agent record types. Agent Skills and Custom record types do not support synchronization — use the Manual source type instead. 2. Enter the **Endpoint** URL. Must be a valid HTTPS URL. 3. Under **Credential type**, choose how the registry authorizes with the endpoint:

    1. **IAM** — Provide a **Role ARN** for SigV4 signing and a **Service** name (e.g., `bedrock-agentcore`, `execute-api`, `lambda`). Optionally specify a **Region** for signing.
    2. **OAuth** — Select or enter a **Credential provider** ARN from AgentCore Identity. Optionally configure **Scopes** and **Custom parameters** under Additional configuration.
    3. **None** — No authorization (for public endpoints).

4. Choose **Create record**.

The record is created in CREATING status. The registry connects to the endpoint, extracts metadata, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field on the record detail page. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors "registry-troubleshooting.md#registry-troubleshooting-sync-errors"). To update the record when the source changes, use the **Sync** button on the record detail page or select **Re-sync from endpoint** during editing.

For AWS CLI and SDK examples of creating records with synchronization, see [Synchronize records from external sources](registry-sync-records.md "registry-sync-records.md").

**Manual**

1. Under **Record details**, enter:

   1. **Name** — Must start with a letter or digit. Valid characters are a-z, A-Z, 0-9, \_ (underscore), - (hyphen), . (dot), and / (forward slash). The name can have up to 255 characters.
   2. **Description** (optional) — 1 to 4,096 characters.
   3. **Record version** — Specify the version of this record (e.g., 1.0.0, v2.1).

2. Under **Record type**, select one of: **MCP**, **Agent**, **Agent Skills**, or **Custom**.
3. A type-specific editor appears. Enter your protocol configuration in JSON format.

   1. For **Agent** and **MCP** types, toggle **Show official schema** to display the reference schema side-by-side for guidance.
   2. The console validates your JSON against the official schema and shows inline errors (e.g., "Missing property 'name'") with a **Diagnose with Amazon Q** button.

4. Choose one of:

   1. **Create as draft** — Creates the record in Draft status.
   2. **Create and submit for approval** — Creates the record and immediately submits it for approval.

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control create-registry-record \
  --registry-id <registryId> \
  --name "my-mcp-server" \
  --display-name "MyMCPServer" \
  --record-type MCP \
  --descriptors '{"mcpServer": {"data": "{\"name\": \"my/mcp-server\", \"description\": \"My MCP server\", \"version\": \"1.0.0\"}", "dataSchemaVersion": "2025-12-11"}}' \
  --record-version "1.0" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id <registryId> \
  --name "MyMCPServer" \
  --descriptor-type MCP \
  --descriptors '{"mcp": {"server": {"inlineContent": "{\"name\": \"my/mcp-server\", \"description\": \"My MCP server\", \"version\": \"1.0.0\"}"}}}' \
  --record-version "1.0" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

```
import boto3
import json

client = boto3.client('agent-registry-control')

server_content = json.dumps({
    "name": "my/mcp-server",
    "description": "My MCP server",
    "version": "1.0.0"
})

response = client.create_registry_record(
    registryId='<registryId>',
    name='my-mcp-server',
    displayName='MyMCPServer',
    recordType='MCP',
    descriptors={
        'mcpServer': {
            'data': server_content,
            'dataSchemaVersion': '2025-12-11'
        }
    },
    recordVersion='1.0'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
import boto3
import json

client = boto3.client('bedrock-agentcore-control')

server_content = json.dumps({
    "name": "my/mcp-server",
    "description": "My MCP server",
    "version": "1.0.0"
})

response = client.create_registry_record(
    registryId='<registryId>',
    name='MyMCPServer',
    descriptorType='MCP',
    descriptors={
        'mcp': {
            'server': {
                'inlineContent': server_content
            }
        }
    },
    recordVersion='1.0'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

###### Note

In the `agent-registry` namespace, `name` is the unique key within a registry (`name` + `recordVersion` combined must be unique). Use `displayName` for the human-readable label. The `descriptors` structure is flat and keyed by primary descriptor type (`mcpServer`, `a2aAgentCard`, `agentSkillsDefinition`, `custom`); the previous `inlineContent`/`schemaVersion` fields are renamed to `data`/`dataSchemaVersion`.

## List registry records

### Console

###### Example

AWS Agent Registry namespace

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1# "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#").
2. The **Registry records** section displays:

   1. **Status summary counters** — Total submitted, Pending approval, Approved, Deprecated, Rejected.
   2. **Records table** with columns: Name, Display name, Description, Status, Record type, Record ARN, Last updated.

3. Use the **Search records** bar to filter by name.

Amazon Bedrock AgentCore namespace (to be deprecated)

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1# "https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#").
2. The **Registry records** section displays:

   1. **Status summary counters** — Total submitted, Pending approval, Approved, Deprecated, Rejected.
   2. **Records table** with columns: Name, Description, Status, Record type, Record ARN, Last updated.

3. Use the **Search records** bar to filter by name.
4. Use the **Update status** dropdown to perform bulk status changes on selected records.

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control list-registry-records \
  --registry-id "<registryId>" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control list-registry-records \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

```
import boto3

client = boto3.client('agent-registry-control')

response = client.list_registry_records(
    registryId='<registryId>'
)
for record in response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['status']} - {record['recordType']}")
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registry_records(
    registryId='<registryId>'
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['status']} - {record['descriptorType']}")
```

###### Note

In the `agent-registry` namespace, `ListRegistryRecords` accepts a structured `filters` parameter (a list of `{"name": "<dotted.path>", "values": […​]}` entries) instead of discrete per-field query parameters. Supported filter names: `name`, `status`, and `recordType`.

## View record details

### Console

###### Example

AWS Agent Registry namespace

1. From the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1# "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#"), choose a record name from the records table.
2. The record detail page displays:

   1. **Record details** section — Name, Display name, Description, Record ARN, Status (shown as a badge next to the record name), Version, Last updated date, Record type, Record ID, Created date.
   2. **Synchronization configuration** section (if configured) — Synchronization type, Source URL, and credential provider details (IAM role ARN, service, region or OAuth provider ARN, grant type, scopes, custom parameters).
   3. **Protocol configuration** section — The descriptor content displayed as formatted JSON (e.g., "Agent card" for A2A records, "Server" and "Tools" for MCP records).
   4. **Tags** section — Shows the tags associated with the record as a key-value table. To add, remove, or modify tags, choose **Edit** in this section to open the **Edit tags** page.

3. Actions available:

   1. **Update status** dropdown — Submit for approval, Approve, Reject, or Deprecate.
   2. **Manage** button — Choose **Edit** to modify the record, **Delete** to permanently remove it, or **Synchronization** to trigger a fresh sync from the configured endpoint (MCP and Agent records only). Synchronization opens a confirmation dialog; the record transitions to UPDATING status during synchronization.

Amazon Bedrock AgentCore namespace (to be deprecated)

1. From the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1# "https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#"), choose a record name from the records table.
2. The record detail page displays:

   1. **Record details** section — Name, Description, Record ARN, Status (shown as a badge next to the record name), Version, Last updated date, Record type, Record ID, Created date.
   2. **Synchronization configuration** section (if configured) — Synchronization type, Source URL, and credential provider details (IAM role ARN, service, region or OAuth provider ARN, grant type, scopes, custom parameters).
   3. **Protocol configuration** section — The descriptor content displayed as formatted JSON (e.g., "Agent card" for A2A records, "Server" and "Tools" for MCP records).

3. Actions available:

   1. **Sync** button (MCP and Agent records only) — Triggers a fresh synchronization from the configured endpoint. Opens a confirmation dialog before proceeding. The record transitions to UPDATING status during synchronization.
   2. **Update status** dropdown — Submit for approval, Approve, Reject, or Deprecate.
   3. **Three-dot menu (⋮)** — Edit or Delete.

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

```
import boto3

client = boto3.client('agent-registry-control')

response = client.get_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Name (dedup key): {response['name']}")
print(f"Display Name: {response['displayName']}")
print(f"Description: {response['description']}")
print(f"Status: {response['status']}")
print(f"Record Type: {response['recordType']}")
print(f"Version: {response['recordVersion']}")
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.get_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Name: {response['name']}")
print(f"Description: {response['description']}")
print(f"Status: {response['status']}")
print(f"Descriptor Type: {response['descriptorType']}")
print(f"Version: {response['recordVersion']}")
```

## Update a registry record

### Console

###### Example

AWS Agent Registry namespace

1. From the record detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1# "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#"), choose **Manage**, then choose **Edit**.
2. On the **Edit record** page, update any of the following:

   1. **Name**, **Display name**, **Description**, **Record version** under Record details.
   2. **Record type** and **Descriptor** — Change the semantic type and/or descriptor shape if needed. Changing the type might require you to select a new descriptor and re-enter the descriptor content.

3. (MCP and Agent records only) Under **Synchronize from endpoint**, optionally configure synchronization:

You can update records via synchronization regardless of whether they were originally created with synchronization. When synchronization is triggered during an update, the record transitions to UPDATING status. If it succeeds, a new record version is created in DRAFT status. If it fails, the record transitions to UPDATE\_FAILED status with error details in the Status Reason field. The synchronized data overwrites the record’s name, description, version, tool definitions, and server definitions with the values found at the source, but does not modify fields that the source does not provide. An admin or curator must review and approve the new draft for it to become visible in search. Until then, the previous approved revision (if any) remains searchable. For more information on dual-revision behavior, see [Record lifecycle](registry-record-lifecycle.md "registry-record-lifecycle.md").

    1. Enter an **Endpoint** URL to enable synchronization. Credential type fields appear when an endpoint is provided. If the record already has synchronization configured, the endpoint and credential provider fields are pre-populated with the existing configuration.
    2. Choose a **Credential type** (IAM, OAuth, or None) and fill in the required fields. If the record was previously configured with a credential provider, the existing values are pre-filled.
    3. Select **Re-sync from endpoint** to trigger a fresh synchronization when saving. The record transitions to UPDATING status during synchronization.
    4. To remove synchronization, choose the clear button next to the endpoint field. This resets the endpoint and all credential fields.

4. Under **Record configuration**, update the record’s definitions in the JSON editor.

    1. You can configure both the endpoint for synchronization and manually edit the record’s definitions. When synchronization is triggered, the registry fetches the latest metadata from the endpoint and updates the record’s name, description, version, tool definitions, and server definitions with the values found at the source, taking precedence over any manual edits to those fields. Fields that the source does not provide are not modified.

5. The console validates your JSON against the official schema and shows inline errors with a **Diagnose with Amazon Q** button. 6. Choose one of:

    1. **Save changes** — Saves the record as a draft.
    2. **Save and submit for approval** — Saves and submits in one step.

A success banner confirms: "[Name] is updated and submitted for approval successfully."

Amazon Bedrock AgentCore namespace (to be deprecated)

1. From the record detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1# "https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#"), choose the three-dot menu (⋮), then choose **Edit**.
2. On the **Edit record** page, update any of the following:

   1. **Name**, **Description**, **Record version** under Record details.
   2. **Record type** — Change the protocol type if needed.

3. (MCP and Agent records only) Under **Synchronize from endpoint**, optionally configure synchronization:

You can update records via synchronization regardless of whether they were originally created with synchronization. When synchronization is triggered during an update, the record transitions to UPDATING status. If it succeeds, a new record version is created in DRAFT status. If it fails, the record transitions to UPDATE\_FAILED status with error details in the Status Reason field. The synchronized data overwrites the record’s name, description, version, tool definitions, and server definitions with the values found at the source, but does not modify fields that the source does not provide. An admin or curator must review and approve the new draft for it to become visible in search. Until then, the previous approved revision (if any) remains searchable. For more information on dual-revision behavior, see [Record lifecycle](registry-record-lifecycle.md "registry-record-lifecycle.md").

    1. Enter an **Endpoint** URL to enable synchronization. Credential type fields appear when an endpoint is provided. If the record already has synchronization configured, the endpoint and credential provider fields are pre-populated with the existing configuration.
    2. Choose a **Credential type** (IAM, OAuth, or None) and fill in the required fields. If the record was previously configured with a credential provider, the existing values are pre-filled.
    3. Select **Re-sync from endpoint** to trigger a fresh synchronization when saving. The record transitions to UPDATING status during synchronization.
    4. To remove synchronization, choose the clear button next to the endpoint field. This resets the endpoint and all credential fields.

4. Under **Record configuration**, update the record’s definitions in the JSON editor.

    1. You can configure both the endpoint for synchronization and manually edit the record’s definitions. When synchronization is triggered, the registry fetches the latest metadata from the endpoint and updates the record’s name, description, version, tool definitions, and server definitions with the values found at the source, taking precedence over any manual edits to those fields. Fields that the source does not provide are not modified.

5. The console validates your JSON against the official schema and shows inline errors with a **Diagnose with Amazon Q** button. 6. Choose one of:

    1. **Save changes** — Saves the record as a draft.
    2. **Save and submit for approval** — Saves and submits in one step.

A success banner confirms: "[Name] is updated and submitted for approval successfully."

###### Note

Tags are not edited from the **Edit record** page in the AWS Agent Registry console. To modify tags, go to the record detail page, choose **Edit** in the **Tags** section, add or remove tags on the **Edit tags** page, and choose **Save changes**. (Tags are only supported in the AWS Agent Registry console.)

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --description "Updated description" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --description "Updated description" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

```
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    description='Updated description'
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    description='Updated description'
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

## Submit a record for approval

### Console

From the record detail page -

1. Choose the **Update status** dropdown
2. Then, choose **Submit for approval**.

   1. Alternatively, use **Create and submit for approval** or **Save and submit for approval** during creation or editing.

###### Note

If the Registry’s Auto-Approval configuration is set to TRUE, then submitting a record for approval automatically approves it. Otherwise, if the Auto-Approval configuration is set to FALSE, then the record moves to 'Pending Approval' status and waits for the Curator to either Approve it or Reject it. Additionally, an Amazon EventBridge notification is triggered indicating a new record has been requested for approval.

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control submit-registry-record-for-approval \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control submit-registry-record-for-approval \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

```
import boto3

client = boto3.client('agent-registry-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
```

## Delete a registry record

### Console

###### Example

AWS Agent Registry namespace

1. From the record detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1# "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#"), choose **Manage**, then choose **Delete**.
2. Confirm the deletion by typing `delete` when prompted.

Amazon Bedrock AgentCore namespace (to be deprecated)

1. From the record detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1# "https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#"), choose the three-dot menu (⋮), then choose **Delete**.
2. Confirm the deletion by typing `delete` when prompted.

Deletion is permanent and cannot be undone.

### AWS CLI

###### Example

AWS Agent Registry namespace

```
aws agent-registry-control delete-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
aws bedrock-agentcore-control delete-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK

###### Example

AWS Agent Registry namespace

```
import boto3

client = boto3.client('agent-registry-control')

response = client.delete_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print("Record deleted successfully")
```

Amazon Bedrock AgentCore namespace (to be deprecated)

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.delete_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print("Record deleted successfully")
```

## Schema validation

When you create or edit a record, the console and API validate your protocol configuration against the official schema for the selected record type. More details on validations can be found in [Supported record types](registry-supported-record-types.md "registry-supported-record-types.md").
