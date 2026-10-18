

# Set custom metadata values on a record
<a name="registry-custom-metadata-values"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

When a registry has a custom metadata schema, you fill in its fields when you create or edit a record. A record can carry the registry’s common attributes, defined in its default schema, plus any fields defined for its record type. To set up the fields, see [Define a custom metadata schema](registry-custom-metadata-schema.md).

**Note**  
You can create or update a record without custom metadata. If you enter any, fill in every required field. Before a record can be submitted for approval, all required fields must have a value.

## Set values
<a name="registry-custom-metadata-values-set"></a>

### Console
<a name="registry-custom-metadata-values-set-console"></a>

1. On the **Create record** or **Edit record** page in the [AWS Agent](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#), select a **Record type**. If the registry has common attributes or fields for that record type, the **Custom metadata** section appears.

1. Choose how to enter values:

   1.  **Form** — Enter a value for each field using a control that matches its type: a text box, a dropdown for **Enum** fields, or a toggle for **Boolean** fields.

   1.  **JSON** — Enter values directly as JSON. The editor validates your input against the schema and shows the schema alongside your content for reference.

1. If you provide any custom metadata, enter a value for every field marked required. Text and URL values can have up to 128 characters.

1. Choose **Create record** or **Save changes**.

### AWS CLI
<a name="registry-custom-metadata-values-set-cli"></a>

These examples use the schema from the [example](registry-custom-metadata-schema.md#registry-custom-metadata-schema-example) in Define a custom metadata schema.

```
aws agent-registry-control create-registry-record \
  --registry-id "<registryId>" \
  --name "my-mcp-server" \
  --record-type MCP \
  --descriptors '{"mcpServer": {"data": "{\"name\":\"my/mcp-server\",\"description\":\"My MCP server\",\"version\":\"1.0.0\"}", "dataSchemaVersion": "2025-12-11"}}' \
  --record-version "1.0" \
  --custom-metadata '{"owner": "search-team", "dataClassification": "internal"}' \
  --region us-east-1
```

To change the values on an existing record, use `update-registry-record`. The `--custom-metadata` parameter works as follows:
+ Omit it to keep the existing values.
+ Pass `{"optionalValue": {…​}}` with the complete set of values. They replace all existing values, rather than merging with them.
+ Pass `{"optionalValue": {}}` to remove all custom metadata values from the record. The registry’s schema doesn’t change.

This example replaces the record’s values:

```
aws agent-registry-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --custom-metadata '{"optionalValue": {"owner": "search-team", "dataClassification": "confidential"}}' \
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
    customMetadata={'owner': 'search-team', 'dataClassification': 'internal'}
)
print(f"Record ARN: {response['recordArn']}")
```

To change the values later, pass `customMetadata` wrapped in `optionalValue`, as with the CLI. Omit `customMetadata` to keep the existing values, or pass `{'optionalValue': {}}` to remove the record’s values.

```
client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    customMetadata={'optionalValue': {'owner': 'search-team', 'dataClassification': 'confidential'}}
)
```

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
+ Values must be strings or native booleans (`true` / `false`). Numbers, arrays, objects, and null are rejected.
+ Text and URL values can be up to 128 characters. An Enum value must be one of the field’s allowed values, each of which is up to 64 characters.
+ A Boolean field requires a native JSON boolean. The string `"true"` is rejected — there is no type conversion.
+ Every key must be a field the record can carry: a common attribute or one of its record type’s fields. Other keys are rejected. Keys are case-sensitive, so `Owner` doesn’t match a field named `owner`.
+ An Enum value must be one of the field’s allowed values. If the record type redefines the field, its own list of allowed values applies.

For limits on the schema itself, see [Schema rules and limits](registry-custom-metadata-schema.md#registry-custom-metadata-schema-constraints).

## Related information
<a name="registry-custom-metadata-values-related"></a>
+  [Define a custom metadata schema](registry-custom-metadata-schema.md) 
+  [Create and manage records](registry-create-manage-records.md) 
+  [Supported record types and descriptors](registry-supported-record-types.md) 