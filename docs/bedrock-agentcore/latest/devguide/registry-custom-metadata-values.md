

# Set custom metadata values on a record
<a name="registry-custom-metadata-values"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

After a registry has a custom metadata schema, record authors provide values for that schema’s fields when they create or edit a record. See [Define a custom metadata schema](registry-custom-metadata-schema.md) to set up the schema first.

**Note**  
Custom metadata is optional on create and update — you can create or update a record without providing any. However, `SubmitRegistryRecordForApproval` always validates the record’s metadata against the schema, so a record with no metadata is rejected at submit if the schema has any required field. When you do provide custom metadata, every field marked **Required** must have a value.

## Set values
<a name="registry-custom-metadata-values-set"></a>

### Console
<a name="registry-custom-metadata-values-set-console"></a>

1. On the **Create record** or **Edit record** page in the [AWS Agent](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#), select a **Record type**. If the resolved type (its own override, or the registry’s default schema) has fields defined, the **Custom metadata** section appears.

1. Choose how to enter values:

   1.  **Form** — Enter a value for each field using a control that matches its type: a text box, a dropdown for **Enum** fields, or a toggle for **Boolean** fields.

   1.  **JSON** — Enter values directly as JSON. The editor validates your input against the schema and shows the schema alongside your content for reference.

1. Provide a value for every field marked required. Text and URL values can have up to 128 characters.

1. Choose **Create record** or **Save changes**.

### AWS CLI
<a name="registry-custom-metadata-values-set-cli"></a>

```
aws agent-registry-control create-registry-record \
  --registry-id "<registryId>" \
  --name "my-mcp-server" \
  --record-type MCP \
  --descriptors '{"mcpServer": {"data": "{\"name\":\"my/mcp-server\",\"description\":\"My MCP server\",\"version\":\"1.0.0\"}", "dataSchemaVersion": "2025-12-11"}}' \
  --record-version "1.0" \
  --custom-metadata '{"tier": "internal", "humanInLoop": true}' \
  --region us-east-1
```

To update the values on an existing record (a full replace of the custom metadata map). Wrap the map in `optionalValue` — the same PATCH-style pattern used by the schema configuration — to distinguish **omit the field** (leave existing values unchanged) from **set to this value** (replace them):

```
aws agent-registry-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --custom-metadata '{"optionalValue": {"owner": "search-team", "tier": "partner"}}' \
  --region us-east-1
```

### AWS SDK
<a name="registry-custom-metadata-values-set-sdk"></a>

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
    recordType='MCP',
    descriptors={
        'mcpServer': {
            'data': server_content,
            'dataSchemaVersion': '2025-12-11'
        }
    },
    recordVersion='1.0',
    customMetadata={'tier': 'internal', 'humanInLoop': True}
)
print(f"Record ARN: {response['recordArn']}")
```

**Note**  
 `customMetadata` on `UpdateRegistryRecord` is a PATCH-style field, following the same `{"optionalValue": {…​}}` pattern as the schema configuration. Provide the full map you want stored — it replaces the existing map rather than merging with it. Omit the field to leave existing values unchanged. To remove all custom metadata from a record, pass an empty map: `{"optionalValue": {}}`.

## View values
<a name="registry-custom-metadata-values-view"></a>

### Console
<a name="registry-custom-metadata-values-view-console"></a>

On a record detail page, the **Custom metadata** section shows the record’s values. Boolean values display as Yes or No, and URL values display as clickable links.

### AWS CLI
<a name="registry-custom-metadata-values-view-cli"></a>

```
aws agent-registry-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-custom-metadata-values-view-sdk"></a>

```
import boto3

client = boto3.client('agent-registry-control')

record = client.get_registry_record(registryId='<registryId>', recordId='<recordId>')
print(record['customMetadata'])
```

## Constraints
<a name="registry-custom-metadata-values-constraints"></a>
+ Values must be strings (up to 128 characters) or native booleans (`true` / `false`). Numbers, arrays, objects, and null are rejected. The 128-character limit applies to all string types including Text, Enum, and URL values.
+ A Boolean field requires a native JSON boolean. The string `"true"` is rejected — there is no type conversion.
+ Unknown keys (fields not defined in the schema) are rejected.
+ Up to 15 fields per schema entry (the default schema or a single record-type override).

For constraints on the schema itself, see [Constraints](registry-custom-metadata-schema.md#registry-custom-metadata-schema-constraints) in [Define a custom metadata schema](registry-custom-metadata-schema.md).

## Related information
<a name="registry-custom-metadata-values-related"></a>
+  [Define a custom metadata schema](registry-custom-metadata-schema.md) 
+  [Create and manage records](registry-create-manage-records.md) 
+  [Supported record types and descriptors](registry-supported-record-types.md) 