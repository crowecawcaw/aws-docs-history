

# Define a custom metadata schema
<a name="registry-custom-metadata-schema"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

Custom metadata lets you define a structured schema for a registry and collect typed, validated information on every record. Use custom metadata to capture information that isn’t covered by a record’s standard fields — for example, an owning team, an internal review status, or a compliance tag.

A custom metadata schema has two parts:
+ An optional **default schema** that applies to any record type that does not have its own override. If a record type has neither a default schema nor an override, records of that type cannot include custom metadata.
+ Optional **record-type overrides** that apply only to a specific record type (for example, Model Context Protocol (MCP) or Agent) and take precedence over the default schema.

Each field in a schema has a **name**, a **data type** (text, enum, URL, or boolean), and whether it’s **required**. After the record’s type resolves to a schema — either its own override or the default schema — record authors enter matching values. They do this when they create or edit the record. For more information, see [Set custom metadata values on a record](registry-custom-metadata-values.md).

**Note**  
A saved field can’t be removed, retyped, or have a saved Enum value deleted — the schema only grows. You can still add new fields, add new Enum values to an existing field, and change whether a field is required at any time (required-ness is not locked by the additive-only rule). Plan your schema with this in mind.

Changing the schema does not modify existing records. Records whose custom metadata no longer satisfies the updated schema are reported as `NON_COMPLIANT` via the `customMetadataSchemaComplianceStatus` field on `GetRegistryRecord`, `ListRegistryRecords`, and `UpdateRegistryRecord` responses. Two permitted schema changes can make existing records non-compliant: making a field required (records without that field become non-compliant, including records with no metadata at all), and adding a record-type override (records of that type that were previously validated against the default schema may no longer match). Approval status is not affected — an approved record remains approved even if its metadata becomes non-compliant. Update the record’s custom metadata to restore compliance.

## Define the schema
<a name="registry-custom-metadata-schema-define"></a>

### Console
<a name="registry-custom-metadata-schema-define-console"></a>

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Custom metadata schema** section, choose **Manage schema**.

1. Choose **Default schema**, or select a specific record type to define an override.

1. Switch between **Form** and **JSON** to build the schema — both modes edit the same underlying schema.

1. In **Form** mode, choose **Add field** and for each field enter:

   1.  **Name** — Must start with a letter. Valid characters are a–z, A–Z, 0–9, `_` (underscore), and `-` (hyphen). Up to 64 characters.

   1.  **Type** — **Text**, **Enum**, **URL**, or **Boolean**. For **Enum**, add one or more allowed values (each up to 64 characters, no duplicates).

   1.  **Required** — Toggle on so that, when a record author provides custom metadata, this field must be included.

      If a field with the same name appears in more than one record type, it must use the same **Type** in every occurrence.

1. In **JSON** mode, enter a JSON Schema (draft-07, restricted subset) directly. The editor validates additive-only changes and shows inline errors if you try to remove a saved field, change its type, or remove a saved Enum value.

   If a field with the same name appears in more than one record type, it must use the same **Type** in every occurrence.

1. Choose **Save changes**.

### AWS CLI
<a name="registry-custom-metadata-schema-define-cli"></a>

The schema is defined as a [JSON Schema (draft-07)](https://json-schema.org/specification-links.html#draft-7) document, restricted to flat object types with `string`, `boolean`, `string` with `enum`, and `string` with `format: "uri"` (URL) properties. Nested objects, arrays, `$ref`, and other advanced JSON Schema features are not supported.

Set the schema when you create the registry:

```
aws agent-registry-control create-registry \
  --name "my-registry" \
  --custom-metadata-schema-configuration '{
    "defaultSchema": "{\"type\":\"object\",\"properties\":{\"owner\":{\"type\":\"string\"}},\"required\":[\"owner\"]}",
    "recordTypeSchemaOverrides": [
      {
        "recordType": "MCP",
        "schema": "{\"type\":\"object\",\"properties\":{\"tier\":{\"type\":\"string\",\"enum\":[\"internal\",\"partner\",\"public\"]}}}"
      }
    ]
  }' \
  --region us-east-1
```

Or update an existing registry’s schema (a full replace of the schema configuration). Wrap the configuration in `optionalValue` — this PATCH-style pattern distinguishes **omit the field** (leave the schema unchanged) from **set to this value** (replace it):

```
aws agent-registry-control update-registry \
  --registry-id "<registryId>" \
  --custom-metadata-schema-configuration '{
    "optionalValue": {
      "defaultSchema": "{\"type\":\"object\",\"properties\":{\"owner\":{\"type\":\"string\"}},\"required\":[\"owner\"]}"
    }
  }' \
  --region us-east-1
```

### AWS SDK
<a name="registry-custom-metadata-schema-define-sdk"></a>

```
import boto3
import json

client = boto3.client('agent-registry-control')

default_schema = json.dumps({
    "type": "object",
    "properties": {
        "owner": {"type": "string"}
    },
    "required": ["owner"]
})

mcp_override_schema = json.dumps({
    "type": "object",
    "properties": {
        "tier": {"type": "string", "enum": ["internal", "partner", "public"]}
    }
})

response = client.create_registry(
    name='my-registry',
    customMetadataSchemaConfiguration={
        'defaultSchema': default_schema,
        'recordTypeSchemaOverrides': [
            {'recordType': 'MCP', 'schema': mcp_override_schema}
        ]
    }
)
print(f"Registry ARN: {response['registryArn']}")
```

**Note**  
 `customMetadataSchemaConfiguration` on `UpdateRegistry` is a PATCH-style field. Omit it to leave the schema unchanged, or provide `{"optionalValue": {…​}}` with the full replacement schema configuration. Schema evolution is additive-only: you can add new fields, new enum values, and new record-type overrides, and you can change whether a field is required at any time. However, you cannot remove a saved field, change its type, remove a saved enum value, or drop an existing override. The update body must include every existing field and override — the service validates the new configuration against the current one and rejects any breaking change. The service doesn’t support clearing the schema once set.

## View the schema
<a name="registry-custom-metadata-schema-view"></a>

### Console
<a name="registry-custom-metadata-schema-view-console"></a>

On the registry detail page, the **Custom metadata schema** section shows a read-only table of the fields defined for each record type, with columns for field name, type, whether the field is required, and allowed values (for Enum fields). Use the search bar to filter by field name, type, or required status.

### AWS CLI
<a name="registry-custom-metadata-schema-view-cli"></a>

```
aws agent-registry-control get-registry \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-custom-metadata-schema-view-sdk"></a>

```
import boto3

client = boto3.client('agent-registry-control')

registry = client.get_registry(registryId='<registryId>')
print(registry['customMetadataSchemaConfiguration'])
```

## Constraints
<a name="registry-custom-metadata-schema-constraints"></a>

 **Schema structure:** 
+ The schema must be a valid JSON object. Do not include a `$schema` key — it is rejected.
+ Allowed top-level keys: `type` (must be `"object"`), `properties` (required, even if empty), `required`, `title`, and `description`.
+ Each field definition must be one of four forms: `{"type":"string"}` (Text), `{"type":"string","enum":[…​]}` (Enum), `{"type":"string","format":"uri"}` (URL), or `{"type":"boolean"}` (Boolean). No other keywords (`default`, `pattern`, `maxLength`, `description`) are allowed at the field level.
+ Each schema string can be at most 10,240 characters.
+ Every entry in `required` must name a property defined in `properties`.
+ URL field values must be valid absolute URIs (RFC 3986) with a scheme.

 **Naming and limits:** 
+ Field name: must start with a letter; valid characters are a–z, A–Z, 0–9, `_` (underscore), and `-` (hyphen); up to 64 characters.
+ Enum allowed values: up to 64 characters each, no duplicates within a field, at least one required.
+ Record-type overrides: at most 5, one per record type (`MCP`, `AGENT`, `SKILL`, `GATEWAY`, or `CUSTOM`).
+ A field with the same name used in more than one record type (default schema or an override) must use the same data type and format everywhere it appears — for example, a **Text** field and a **URL** field are not interchangeable even though both are strings. Enum allowed values may differ between record types for the same field name.

 **Additive-only evolution:** 
+ You can add new fields, add new Enum values to an existing Enum field, add new record-type overrides, add a default schema to a registry that has only overrides, and change whether a field is required.
+ You cannot remove a saved field, change its data type, remove a saved Enum value, add or remove the Enum constraint on an existing field (for example, a Text field cannot become an Enum field or vice versa), change a field’s format (for example, Text to URL or vice versa), remove an existing override, or remove the default schema.

For constraints on the values stored against a schema, see [Constraints](registry-custom-metadata-values.md#registry-custom-metadata-values-constraints) in [Set custom metadata values on a record](registry-custom-metadata-values.md).

## Related information
<a name="registry-custom-metadata-schema-related"></a>
+  [Set custom metadata values on a record](registry-custom-metadata-values.md) 
+  [Search for registry records](registry-search-records.md) — filter search results by custom metadata field values
+  [Supported record types and descriptors](registry-supported-record-types.md) 
+  [Create and manage registries](registry-create-manage.md) 