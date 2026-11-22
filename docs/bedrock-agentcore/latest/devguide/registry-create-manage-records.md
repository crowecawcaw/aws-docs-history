

# Create and manage records

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Create a registry record
<a name="registry-create-record"></a>

### Console
<a name="registry-create-record-console"></a>

**Example**  

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose a source type:

   1.  **Synchronize from source** — Provide an endpoint URL (for MCP and Agent records) or an Amazon S3 or GitHub location (for Skills records), with optional credentials, and the registry fetches the content from the source. To update the record after the source changes, you must manually trigger synchronization. For more information, see [Synchronize records from external sources](registry-sync-records.md).

   1.  **Define manually** — Manually configure the record details and protocol configuration.
 **Synchronize from source: MCP and Agent records**   

1. Under **Record details**, select the record type: **MCP** or **Agent**.
**Note**  
Synchronization is available for MCP, Agent, and Skills record types. For Skills records, see the next procedure. For Custom and Web bot record types, choose **Define manually**.

1. Enter the **Endpoint** URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose how the registry authorizes with the endpoint:

   1.  **IAM** — Provide a **Role ARN** for SigV4 signing and a **Service** name (for example, `agent-registry`, `execute-api`, `lambda`). Optionally specify a **Region** for signing.

   1.  **OAuth** — Select or enter a **Credential provider** ARN from AgentCore Identity. Optionally configure **Scopes** and **Custom parameters** under Additional configuration.

   1.  **None** — No authorization (for public endpoints).

1. Choose **Create record**.

   The record is created in CREATING status. The registry connects to the endpoint, extracts metadata, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field on the record detail page. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors). To update the record when the source changes, choose **Manage**, then choose **Synchronization** on the record detail page, or choose **Manage → Edit** and select **Trigger synchronization**.
For AWS CLI and SDK examples of creating records with synchronization, see [Synchronize records from external sources](registry-sync-records.md).  
 **Synchronize from source: Skills records**   

1. Under **Record details**, select **Skills** as the record type.

1. Under **Synchronize from source**, choose **Amazon S3** or **GitHub**.

1. Under **Content type**, choose what the source provides:

   1.  **Skill markdown** — A SKILL.md file. The registry copies only SKILL.md into the record.

   1.  **Skill package** — A skill package .zip archive in Amazon S3, or the whole GitHub folder as a skill package. The registry validates and stores the package.

1. Enter the location:

   1. For Amazon S3, enter the **S3 URI** of the SKILL.md file or the .zip archive, or browse to the object.

   1. For GitHub, enter the **GitHub folder** that contains SKILL.md, in the form `https://github.com/{owner}/{repo}/tree/{branch}/{path}`.

1. Under **Credential type**, choose how the registry reads the source:

   1. For Amazon S3, choose **IAM Role** and enter a role that the registry can assume and that can read the object. To synchronize a publicly readable object without a role, use the AWS CLI or an AWS SDK, as described in [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md).

   1. For GitHub, choose **OAuth client**, select the **Credential provider** for your GitHub OAuth App, and choose **Public repository** or **Private repository** under **Repository access**. Optionally, enter a **Return URL**.

1. Choose **Create record**.

   The record is created in CREATING status. The registry reads the source, validates the content, and then moves the record to DRAFT, or to CREATE\_FAILED. To see the error details, choose the record’s **Status** in the **Record details** section of the record detail page. The record takes its name and description from the `name` and `description` in SKILL.md.

   For a GitHub source, if a GitHub user must approve access first, the console shows **Authorize on GitHub** and the record has the status **Create pending authorization** until the approval completes. For the setup and permissions that each source needs, see [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md) and [Synchronize a skill from GitHub](registry-skill-sync-github.md). For the authorization flow, see [Authorize GitHub access](registry-skill-sync-github.md#registry-skill-sync-github-authorization).
 **Define manually**   

1. In the **Record details** section, for **Name**, enter a unique name for the record. The name must be unique within the registry — the combination of `Name` and `Record version` must be unique. The name must start with an alphanumeric character. Valid characters are a–z, A–Z, 0–9, `_` (underscore), `-` (hyphen), `.` (period), and `/` (forward slash). The name can have up to 255 characters. For a Skills record, no part of the name between slashes can be a name that Windows reserves for a device, such as `CON` or `NUL`, with or without an extension, and no part can end with a dot.

1. (Optional) For **Display name**, enter a human-readable label for the record. This appears in the registry records table and search results alongside the record’s technical name.

1. (Optional) For **Description**, enter a description for the record. The description can be 1 to 4,096 characters.

1. For **Record version**, enter a version identifier for the record (for example, `1.0.0` or `v2.1`).

1. In the **Record type and descriptor** section:

   1. Under **Type**, select the semantic type of the record. The type determines which primary descriptor keys are valid.
      +  **MCP** – Protocol designed for AI tool and agent communications. Handles context management and structured message formats.
      +  **Agent** – Protocol designed for secure agent-to-agent interactions. Enables distributed workflows and information exchange.
      +  **Skills** – Register agent skills with markdown documentation and an optional structured definition.
      +  **Custom** – Custom protocol implementation for specialized communication patterns. Define your own interface specification and integration requirements.
      +  **Web bot** – Register a signed-request bot identity.

   1. Under **Descriptor**, choose the shape of the record’s descriptor data. Available options depend on the **Type** you selected:
      +  **MCP** → **MCP server** or **Custom** 
      +  **Agent** → **A2A Agent Card**, **MCP server**, or **Custom** 
      +  **Skills** → **Agent skills definition** or **Custom** 
      +  **Custom** → **Custom** 
      +  **Web bot** → **Signature Agent Card** 

1. A descriptor-specific editor appears based on your **Descriptor** selection. Enter your protocol configuration in JSON format. For **MCP server** and **A2A Agent Card** descriptors, toggle **Show official schema** to display the reference schema side-by-side. The console validates your JSON against the official schema and shows inline errors (for example, "Missing property 'name'") with a **Diagnose with Amazon Q** button. For per-descriptor configuration details, see [Supported record types](registry-supported-record-types.md).

   For the **Agent skills definition** descriptor, under **Skill content source**, choose one of the following options:

   1.  **Author inline** — Enter the **Skill markdown**, **Your skill definition**, or both.

   1.  **Upload a package** — Under **Skill package**, choose a single .zip file of up to 5 MiB that contains SKILL.md and any bundled files. Optionally, enter its **SHA-256 checksum**. AWS Agent Registry validates the package after you create the record. The record stays in CREATING status until validation finishes, and then moves to DRAFT, or to CREATE\_FAILED. To see the problems, choose the record’s **Status** on the record detail page. For the package format and the upload steps, see [Skill package format and validation](registry-skill-package-format.md) and [Upload a skill package](registry-skill-package-upload.md).

1. (Optional) In the **Tags** section, choose **Add new tag** to attach one or more tags to the record. Each tag has a key and an optional value.

1. Choose one of:

   1.  **Create as draft** — Creates the record in Draft status.

   1.  **Create and submit for approval** — Creates the record and immediately submits it for approval.

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. Choose a source type:

   1.  **Synchronize from endpoint** — Provide an endpoint URL and optional credentials to invoke the endpoint, and the registry fetches metadata from the source. Available for MCP and Agent record types only. To update the record after the source changes, you must manually trigger synchronization. See [Synchronize records from external sources](registry-sync-records.md) for details.

   1.  **Manual** — Manually configure the record details and protocol configuration.
 **Synchronize from endpoint** 

Synchronization is available for MCP and Agent record types. For Agent Skills, Custom, and Web bot record types, use the Manual source type.

**Example**  

1. Under **Record details**, select the record type: **MCP** or **Agent**.

1. Enter the **Endpoint** URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose how the registry authorizes with the endpoint:

   1.  **IAM** — Provide a **Role ARN** for SigV4 signing and a **Service** name (e.g., `bedrock-agentcore`, `execute-api`, `lambda`). Optionally specify a **Region** for signing.

   1.  **OAuth** — Select or enter a **Credential provider** ARN from AgentCore Identity. Optionally configure **Scopes** and **Custom parameters** under Additional configuration.

   1.  **None** — No authorization (for public endpoints).

1. Choose **Create record**.

   The record is created in CREATING status. The registry connects to the endpoint, extracts metadata, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field on the record detail page. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors). To update the record when the source changes, use the **Sync** button on the record detail page or select **Re-sync from endpoint** during editing.
For AWS CLI and SDK examples of creating records with synchronization, see [Synchronize records from external sources](registry-sync-records.md).  
 **Manual**   

1. Under **Record details**, enter:

   1.  **Name** — Must start with a letter or digit. Valid characters are a-z, A-Z, 0-9, \_ (underscore), - (hyphen), . (dot), and / (forward slash). The name can have up to 255 characters.

   1.  **Description** (optional) — 1 to 4,096 characters.

   1.  **Record version** — Specify the version of this record (e.g., 1.0.0, v2.1).

1. In the **Record type** section, select one of: **MCP**, **Agent**, **Agent Skills**, **Custom**, or **Web bot**.

1. A type-specific editor appears. Enter your protocol configuration in JSON format.

   1. For **Agent** and **MCP** types, toggle **Show official schema** to display the reference schema side-by-side for guidance.

   1. The console validates your JSON against the official schema and shows inline errors (e.g., "Missing property 'name'") with a **Diagnose with Amazon Q** button.

1. Choose one of:

   1.  **Create as draft** — Creates the record in Draft status.

   1.  **Create and submit for approval** — Creates the record and immediately submits it for approval.

### AWS CLI
<a name="registry-create-record-cli"></a>

**Example**  

```bash
aws agent-registry-control create-registry-record \
  --registry-id <registryId> \
  --name "my-mcp-server" \
  --display-name "MyMCPServer" \
  --record-type MCP \
  --descriptors '{"mcpServer": {"data": "{\"name\": \"my/mcp-server\", \"description\": \"My MCP server\", \"version\": \"1.0.0\"}", "dataSchemaVersion": "2025-12-11"}}' \
  --record-version "1.0" \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control create-registry-record \
  --registry-id <registryId> \
  --name "MyMCPServer" \
  --descriptor-type MCP \
  --descriptors '{"mcp": {"server": {"inlineContent": "{\"name\": \"my/mcp-server\", \"description\": \"My MCP server\", \"version\": \"1.0.0\"}"}}}' \
  --record-version "1.0" \
  --region us-east-1
```

### AWS SDK
<a name="registry-create-record-sdk"></a>

**Example**  

```python
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

```python
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

**Note**  
In the `agent-registry` namespace, `name` is the unique key within a registry (`name` \+ `recordVersion` combined must be unique). Use `displayName` for the human-readable label. The `descriptors` structure is flat and keyed by primary descriptor type (`mcpServer`, `a2aAgentCard`, `agentSkillsDefinition`, `custom`); the previous `inlineContent`/`schemaVersion` fields are renamed to `data`/`dataSchemaVersion`.

To create a skill record with a skill package or with a source in Amazon S3 or GitHub, see [Upload a skill package](registry-skill-package-upload.md), [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md), and [Synchronize a skill from GitHub](registry-skill-sync-github.md).

## List registry records
<a name="registry-list-records"></a>

### Console
<a name="registry-list-records-console"></a>

**Example**  

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. The **Registry records** section displays:

   1.  **Status summary counters** — Total submitted, Pending approval, Approved, Deprecated, Rejected.

   1.  **Records table** with columns: Name, Display name, Description, Status, Record type, Record ARN, Last updated.

1. Use the **Search records** bar to filter by name.

1. Open the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#).

1. The **Registry records** section displays:

   1.  **Status summary counters** — Total submitted, Pending approval, Approved, Deprecated, Rejected.

   1.  **Records table** with columns: Name, Description, Status, Record type, Record ARN, Last updated.

1. Use the **Search records** bar to filter by name.

1. Use the **Update status** dropdown to perform bulk status changes on selected records.

### AWS CLI
<a name="registry-list-records-cli"></a>

**Example**  

```bash
aws agent-registry-control list-registry-records \
  --registry-id "<registryId>" \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control list-registry-records \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-list-records-sdk"></a>

**Example**  

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.list_registry_records(
    registryId='<registryId>'
)
for record in response['registryRecords']:
    print(f"{record['displayName']} ({record['name']}) - {record['status']} - {record['recordType']}")
```

```python
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registry_records(
    registryId='<registryId>'
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['status']} - {record['descriptorType']}")
```

**Note**  
In the `agent-registry` namespace, `ListRegistryRecords` accepts a structured `filters` parameter (a list of `{"name": "<dotted.path>", "values": […​]}` entries) instead of discrete per-field query parameters. Supported filter names: `name`, `status`, and `recordType`.

## View record details
<a name="registry-view-record"></a>

### Console
<a name="registry-view-record-console"></a>

**Example**  

1. From the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#), choose a record name from the records table.

1. The record detail page displays:

   1.  **Record details** section — Name, Display name, Description, Record ARN, Status (shown as a badge next to the record name), Version, Last updated date, Record type, Record ID, Created date.

   1.  **Source** section (if configured) — Source type, URL, and credential provider details (credential provider type, role ARN, service, region or provider ARN, grant type, scopes, custom parameters, and, for a GitHub skill source, the return URL, which shows **Registry console (default)** when the record doesn’t set one).

   1.  **Protocol configuration** section — The descriptor content displayed as formatted JSON (e.g., "Agent card" for A2A records, "Server" and "Tools" for MCP records).

   1.  **Skill package** section (Skills records that have a skill package):
      +  **Download** — Downloads the package.
      +  **View checksum** — Shows the package’s SHA-256 checksum. Use it to verify the downloaded package.

   1.  **Skill content** section (Skills records) — The **Skill markdown** and **Skill definition**. When the record has a skill package, **Skill package files** takes the place of the skill markdown and lists the files in the package. You can view or download each file. For more information, see [Download a skill package](registry-skill-package-download.md).

   1.  **Tags** section — Shows the tags associated with the record as a key-value table. To add, remove, or modify tags, choose **Edit** in this section to open the **Edit tags** page.

1. Actions available:

   1.  **Update status** dropdown — Submit for approval, Approve, Reject, or Deprecate.

   1.  **Manage** button — Choose **Edit** to modify the record, **Delete** to permanently remove it, or **Synchronization** to trigger a fresh sync from the configured source (MCP, Agent, and Skills records). Synchronization opens a confirmation dialog; the record transitions to UPDATING status during synchronization.

1. From the registry detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#), choose a record name from the records table.

1. The record detail page displays:

   1.  **Record details** section — Name, Description, Record ARN, Status (shown as a badge next to the record name), Version, Last updated date, Record type, Record ID, Created date.

   1.  **Synchronization configuration** section (if configured) — Synchronization type, Source URL, and credential provider details (IAM role ARN, service, region or OAuth provider ARN, grant type, scopes, custom parameters).

   1.  **Protocol configuration** section — The descriptor content displayed as formatted JSON (e.g., "Agent card" for A2A records, "Server" and "Tools" for MCP records).

1. Actions available:

   1.  **Sync** button (MCP and Agent records only) — Triggers a fresh synchronization from the configured endpoint. Opens a confirmation dialog before proceeding. The record transitions to UPDATING status during synchronization.

   1.  **Update status** dropdown — Submit for approval, Approve, Reject, or Deprecate.

   1.  **Three-dot menu (⋮)** — Edit or Delete.

### AWS CLI
<a name="registry-view-record-cli"></a>

**Example**  

```bash
aws agent-registry-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-view-record-sdk"></a>

**Example**  

```python
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

```python
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
<a name="registry-update-record"></a>

### Console
<a name="registry-update-record-console"></a>

**Example**  

1. From the record detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#), choose **Manage**, then choose **Edit**.

1. On the **Edit record** page, update any of the following:

   1.  **Name**, **Display name**, **Description**, **Record version** under Record details.

   1.  **Record type** and **Descriptor** — Change the semantic type and/or descriptor shape if needed. Changing the type might require you to select a new descriptor and re-enter the descriptor content.

1. (MCP and Agent records only) Under **Source**, optionally configure synchronization:

   You can update records via synchronization regardless of whether they were originally created with synchronization. When synchronization is triggered during an update, the record transitions to UPDATING status. If it succeeds, a new record version is created in DRAFT status. If it fails, the record transitions to UPDATE\_FAILED status with error details in the Status Reason field. The synchronized data overwrites the record’s name, description, version, tool definitions, and server definitions with the values found at the source, but does not modify fields that the source does not provide. An admin or curator must review and approve the new draft for it to become visible in search. Until then, the previous approved revision (if any) remains searchable. For more information on dual-revision behavior, see [Record lifecycle](registry-record-lifecycle.md).

   1. Enter an **Endpoint** URL to enable synchronization. Credential type fields appear when an endpoint is provided. If the record already has synchronization configured, the endpoint and credential provider fields are pre-populated with the existing configuration.

   1. Choose a **Credential type** (IAM, OAuth, or None) and fill in the required fields. If the record was previously configured with a credential provider, the existing values are pre-filled.

   1. Select **Trigger synchronization** to trigger a fresh synchronization when saving. The record transitions to UPDATING status during synchronization.

   1. To remove synchronization, choose the clear button next to the endpoint field. This resets the endpoint and all credential fields.

1. (Skills records) Under **Skill content source**, choose where the skill’s content comes from. Changing the content source replaces the skill’s content and removes the previous source, including any uploaded package.

   1.  **Author inline** — Edit the **Skill markdown** or **Your skill definition**. If the record has a package or a source, saving with **Author inline** removes it.

   1.  **Upload a package** — To replace the package, choose a new .zip file under **Skill package**. If you don’t choose a file, the record keeps its current package. To change SKILL.md, upload a new package.

   1.  **Synchronize from source** — Set or change the Amazon S3 or GitHub source, the same way as when you create a record. Saving a new or changed source starts a synchronization. To read an unchanged source again, select **Trigger synchronization**. For a GitHub source, select **Re-authorize GitHub access** to approve GitHub access again on save, even if the current approval still works. The new approval also replaces the one used by other records in this registry that use the same credential provider and repository access.

      A skill synchronization replaces the skill’s markdown and, for a package source, its package. It also sets the record’s name and description to the `name` and `description` in SKILL.md, so a name or description that you edit lasts only until the next synchronization. It doesn’t change the record’s display name or version. When a save starts a synchronization, **Save and submit for approval** isn’t available. Save your changes, and then submit the record for approval after synchronization finishes. While a record waits for GitHub authorization, you can’t edit it. For more information, see [Publish skill packages](registry-skill-packages.md).

1. Under **Record configuration**, update the record’s definitions in the JSON editor.

   1. You can configure both the endpoint for synchronization and manually edit the record’s definitions. When synchronization is triggered, the registry fetches the latest metadata from the endpoint and updates the record’s name, description, version, tool definitions, and server definitions with the values found at the source, taking precedence over any manual edits to those fields. Fields that the source does not provide are not modified.

1. The console validates your JSON against the official schema and shows inline errors with a **Diagnose with Amazon Q** button.

1. Choose one of:

   1.  **Save changes** — Saves the record as a draft.

   1.  **Save and submit for approval** — Saves and submits in one step.
A success banner confirms: "[Name] is updated and submitted for approval successfully."

1. From the record detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#), choose the three-dot menu (⋮), then choose **Edit**.

1. On the **Edit record** page, update any of the following:

   1.  **Name**, **Description**, **Record version** under Record details.

   1.  **Record type** — Change the protocol type if needed.

1. (MCP and Agent records only) Under **Synchronize from endpoint**, optionally configure synchronization:

   You can update records via synchronization regardless of whether they were originally created with synchronization. When synchronization is triggered during an update, the record transitions to UPDATING status. If it succeeds, a new record version is created in DRAFT status. If it fails, the record transitions to UPDATE\_FAILED status with error details in the Status Reason field. The synchronized data overwrites the record’s name, description, version, tool definitions, and server definitions with the values found at the source, but does not modify fields that the source does not provide. An admin or curator must review and approve the new draft for it to become visible in search. Until then, the previous approved revision (if any) remains searchable. For more information on dual-revision behavior, see [Record lifecycle](registry-record-lifecycle.md).

   1. Enter an **Endpoint** URL to enable synchronization. Credential type fields appear when an endpoint is provided. If the record already has synchronization configured, the endpoint and credential provider fields are pre-populated with the existing configuration.

   1. Choose a **Credential type** (IAM, OAuth, or None) and fill in the required fields. If the record was previously configured with a credential provider, the existing values are pre-filled.

   1. Select **Re-sync from endpoint** to trigger a fresh synchronization when saving. The record transitions to UPDATING status during synchronization.

   1. To remove synchronization, choose the clear button next to the endpoint field. This resets the endpoint and all credential fields.

1. Under **Record configuration**, update the record’s definitions in the JSON editor.

   1. You can configure both the endpoint for synchronization and manually edit the record’s definitions. When synchronization is triggered, the registry fetches the latest metadata from the endpoint and updates the record’s name, description, version, tool definitions, and server definitions with the values found at the source, taking precedence over any manual edits to those fields. Fields that the source does not provide are not modified.

1. The console validates your JSON against the official schema and shows inline errors with a **Diagnose with Amazon Q** button.

1. Choose one of:

   1.  **Save changes** — Saves the record as a draft.

   1.  **Save and submit for approval** — Saves and submits in one step.
A success banner confirms: "[Name] is updated and submitted for approval successfully."

**Note**  
Tags are not edited from the **Edit record** page in the AWS Agent Registry console. To modify tags, go to the record detail page, choose **Edit** in the **Tags** section, add or remove tags on the **Edit tags** page, and choose **Save changes**. (Tags are only supported in the AWS Agent Registry console.)

### AWS CLI
<a name="registry-update-record-cli"></a>

**Example**  

```bash
aws agent-registry-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --description "Updated description" \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --description "Updated description" \
  --region us-east-1
```

### AWS SDK
<a name="registry-update-record-sdk"></a>

**Example**  

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    description='Updated description'
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

```python
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    description='Updated description'
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

To replace or remove a skill package, or to change or synchronize a skill’s source, see [Upload a skill package](registry-skill-package-upload.md), [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md), and [Synchronize a skill from GitHub](registry-skill-sync-github.md).

## Submit a record for approval
<a name="registry-submit-record"></a>

### Console
<a name="registry-submit-record-console"></a>

From the record detail page -

1. Choose the **Update status** dropdown

1. Then, choose **Submit for approval**.

   1. Alternatively, use **Create and submit for approval** or **Save and submit for approval** during creation or editing.

**Note**  
If the Registry’s Auto-Approval configuration is set to TRUE, then submitting a record for approval automatically approves it. Otherwise, if the Auto-Approval configuration is set to FALSE, then the record moves to 'Pending Approval' status and waits for the Curator to either Approve it or Reject it. Additionally, an Amazon EventBridge notification is triggered indicating a new record has been requested for approval.

### AWS CLI
<a name="registry-submit-record-cli"></a>

**Example**  

```bash
aws agent-registry-control submit-registry-record-for-approval \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control submit-registry-record-for-approval \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-submit-record-sdk"></a>

**Example**  

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
```

```python
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
```

## Delete a registry record
<a name="registry-delete-record"></a>

### Console
<a name="registry-delete-record-console"></a>

**Example**  

1. From the record detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#), choose **Manage**, then choose **Delete**.

1. Confirm the deletion by typing `delete` when prompted.

1. From the record detail page in the [Bedrock-AgentCore console](https://console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#), choose the three-dot menu (⋮), then choose **Delete**.

1. Confirm the deletion by typing `delete` when prompted.

**Deletion is permanent**  
You can’t undo a deletion. Deleting a skill record also deletes all of its stored skill packages.

### AWS CLI
<a name="registry-delete-record-cli"></a>

**Example**  

```bash
aws agent-registry-control delete-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

```bash
aws bedrock-agentcore-control delete-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-delete-record-sdk"></a>

**Example**  

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.delete_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print("Record deleted successfully")
```

```python
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.delete_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print("Record deleted successfully")
```

## Schema validation
<a name="registry-schema-validation"></a>

When you create or edit a record, the console and API validate your protocol configuration against the official schema for the selected record type. More details on validations can be found in [Supported record types](registry-supported-record-types.md).

The registry validates a skill package, and a SKILL.md that it synchronizes from a source, after the request returns, while the record is in CREATING or UPDATING status. If validation fails, the record moves to CREATE\_FAILED or UPDATE\_FAILED, and the record’s status reason lists the problems. In the console, choose the record’s **Status** to see it. For the rules, see [Skill package format and validation](registry-skill-package-format.md).