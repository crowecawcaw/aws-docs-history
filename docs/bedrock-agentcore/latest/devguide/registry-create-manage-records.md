# Create and manage records

## Create a registry record

### Console

1. Open the registry detail page.
2. In the **Registry records** section, choose **Create record**.
3. Under **Record details** , enter:
   1. **Name** — Must start with a letter or digit. Valid characters are a-z, A-Z, 0-9, \_ (underscore), - (hyphen), . (dot), and / (forward slash). The name can have up to 255 characters.
   2. **Description** (optional) — 1 to 4,096 characters.
   3. **Record version** — Specify the version of this record (e.g., 1.0.0, v2.1).

4. Under **Record type** , select one of: **MCP** , **Agent** , **Agent Skills** , or **Custom**.
5. A type-specific editor appears. Enter your protocol configuration in JSON format.
   1. For **Agent** and **MCP** types, toggle **Show official schema** to display the reference schema side-by-side for guidance.
   2. The console validates your JSON against the official schema and shows inline errors (e.g., "Missing property 'name'") with a **Diagnose with Amazon Q** button.

6. Choose one of:
   1. **Create as draft** — Creates the record in Draft status.
   2. **Create and submit for approval** — Creates the record and immediately submits it for approval.

### AWS CLI

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

## List registry records

### Console

1. Open the registry detail page.
2. The **Registry records** section displays:
   1. **Status summary counters** — Total submitted, Pending approval, Approved, Deprecated, Rejected.
   2. **Records table** with columns: Name, Description, Status, Record type, Record ARN, Last updated.

3. Use the **Search records** bar to filter by name.
4. Use the **Update status** dropdown to perform bulk status changes on selected records.

### AWS CLI

```
aws bedrock-agentcore-control list-registry-records \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registry_records(
    registryId='<registryId>'
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['status']} - {record['descriptorType']}")
```

## View record details

### Console

1. From the registry detail page, choose a record name from the records table.
2. The record detail page displays:
   1. **Record details** section — Name, Description, Record ARN, Status (shown as a badge next to the record name), Version, Last updated date, Record type, Record ID, Created date.
   2. **Protocol configuration** section — The descriptor content displayed as formatted JSON (e.g., "Agent card" for A2A records, "Server" and "Tools" for MCP records).

3. Actions available:
   1. **Update status** dropdown — Submit for approval, Approve, Reject, or Deprecate.
   2. **Three-dot menu (⋮)** — Edit or Delete.

### AWS CLI

```
aws bedrock-agentcore-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK

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

1. From the record detail page, choose the three-dot menu (⋮), then choose **Edit**.
2. On the **Edit record** page, update any of the following:
   1. **Name** , **Description** , **Record version** under Record details.
   2. **Protocol configuration** in the JSON editor.

3. The console validates your JSON against the official schema and shows inline errors with a **Diagnose with Amazon Q** button.
4. Choose one of:
   1. **Save changes** — Saves the record as a draft.
   2. **Save and submit for approval** — Saves and submits in one step.

A success banner confirms: "[Name] is updated and submitted for approval successfully."

### AWS CLI

```
aws bedrock-agentcore-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --description "Updated description" \
  --region us-east-1
```

### AWS SDK

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

```
aws bedrock-agentcore-control submit-registry-record-for-approval \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK

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

1. From the record detail page, choose the three-dot menu (⋮), then choose **Delete**.
2. Confirm the deletion by typing in 'delete' when prompted

Deletion is permanent and cannot be undone.

### AWS CLI

```
aws bedrock-agentcore-control delete-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK

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
