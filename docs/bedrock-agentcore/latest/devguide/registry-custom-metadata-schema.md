

# Define a custom metadata schema
<a name="registry-custom-metadata-schema"></a>

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

Use custom metadata to add your own fields to records in a registry, such as an owning team, a review status, or a data classification. You define the fields once on the registry. Then, when you create or edit a record, you fill them in.

You define two kinds of fields:
+  **Common attributes** — fields available to records of every record type, defined in the default schema (`defaultSchema` in the API). Whether a record must have a value depends on the field’s **Required** setting.
+  **Record type fields** — extra fields for one record type, such as Model Context Protocol (MCP) servers or agents. For the list of record types, see [Supported record types and descriptors](registry-supported-record-types.md).

A record can carry the common attributes plus the fields for its record type. Use common attributes for anything you want to filter or report on across all records.

## Example
<a name="registry-custom-metadata-schema-example"></a>

Every record in this registry needs an owner and can have a data classification. Agent records also need a model family and a classification, and can be classified as `restricted`.

Common attributes:

```
{
  "type": "object",
  "properties": {
    "owner": {"type": "string"},
    "dataClassification": {"type": "string", "enum": ["public", "internal", "confidential"]}
  },
  "required": ["owner"]
}
```

Fields for `AGENT`:

```
{
  "type": "object",
  "properties": {
    "modelFamily": {"type": "string"},
    "dataClassification": {"type": "string", "enum": ["public", "internal", "confidential", "restricted"]}
  },
  "required": ["modelFamily", "dataClassification"]
}
```

Records can then carry:


| Record type | Fields | Required | Allowed values for `dataClassification`  | 
| --- | --- | --- | --- | 
| Agent |  `owner`, `modelFamily`, `dataClassification`  | All three |  `public`, `internal`, `confidential`, `restricted`  | 
| All other types |  `owner`, `dataClassification`  |  `owner`  |  `public`, `internal`, `confidential`  | 

The Agent fields don’t repeat `owner`, because every record type already gets the common attributes. They do repeat `dataClassification`. This makes the field required for agents and allows the additional value `restricted`. To change a common attribute for one record type like this, include it in that record type’s fields with the same type and all of its allowed values. You can add allowed values and make it required.

## Define the schema
<a name="registry-custom-metadata-schema-define"></a>

### Console
<a name="registry-custom-metadata-schema-define-console"></a>

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Custom metadata schema** section, choose **Manage schema**.

1. Under **Common attributes**, choose **Add field** for each field every record should have, and enter:

   1.  **Name** — Starts with a letter. Letters, numbers, `_`, and `-`. Up to 64 characters.

   1.  **Type** — **Text**, **Enum** (a list of allowed values), **URL**, or **Boolean**.

   1.  **Allowed values** — For an **Enum** field, enter each value records can use: 1 to 25 values, each up to 64 characters.

   1.  **Required** — Whether a value must be provided.

1. To add fields for one record type, select the record type and choose **Add field**. The common attributes are listed for reference. To make one required or allow more values for this record type, edit it in place.

1. Choose **Save changes**.

To edit the schema as JSON, switch from **Form** to **JSON**. Each schema, the common attributes or one record type’s fields, is a JSON Schema document like the ones in the [example](#registry-custom-metadata-schema-example).

### AWS CLI
<a name="registry-custom-metadata-schema-define-cli"></a>

In the API, the common attributes are `defaultSchema`, and each record type’s fields are an entry in `recordTypeSchemaOverrides`. Each schema is a JSON string.

Save the two schemas from the [example](#registry-custom-metadata-schema-example) as `common.json` and `agent.json`, then create the registry:

```
jq -n --rawfile common common.json --rawfile agent agent.json \
  '{defaultSchema: $common, recordTypeSchemaOverrides: [{recordType: "AGENT", schema: $agent}]}' \
  > schema-config.json

aws agent-registry-control create-registry \
  --name "my-registry" \
  --custom-metadata-schema-configuration file://schema-config.json \
  --region us-east-1
```

To change the schema later, edit the schema files, rebuild the configuration, and send it wrapped in `optionalValue`. This example adds a `team` field to the common attributes:

```
jq '.properties.team = {"type": "string"}' common.json > common.tmp && mv common.tmp common.json

jq -n --rawfile common common.json --rawfile agent agent.json \
  '{optionalValue: {defaultSchema: $common, recordTypeSchemaOverrides: [{recordType: "AGENT", schema: $agent}]}}' \
  > schema-update.json

aws agent-registry-control update-registry \
  --registry-id "<registryId>" \
  --custom-metadata-schema-configuration file://schema-update.json \
  --region us-east-1
```

### AWS SDK
<a name="registry-custom-metadata-schema-define-sdk"></a>

```
import boto3
import json

client = boto3.client('agent-registry-control')

common_attributes = {
    "type": "object",
    "properties": {
        "owner": {"type": "string"},
        "dataClassification": {"type": "string", "enum": ["public", "internal", "confidential"]}
    },
    "required": ["owner"]
}

agent_fields = {
    "type": "object",
    "properties": {
        "modelFamily": {"type": "string"},
        "dataClassification": {
            "type": "string",
            "enum": ["public", "internal", "confidential", "restricted"]
        }
    },
    "required": ["modelFamily", "dataClassification"]
}

response = client.create_registry(
    name='my-registry',
    customMetadataSchemaConfiguration={
        'defaultSchema': json.dumps(common_attributes),
        'recordTypeSchemaOverrides': [
            {'recordType': 'AGENT', 'schema': json.dumps(agent_fields)}
        ]
    }
)
print(f"Registry ARN: {response['registryArn']}")
```

To change the schema later, send the complete new configuration wrapped in `optionalValue`:

```
common_attributes["properties"]["team"] = {"type": "string"}

client.update_registry(
    registryId='<registryId>',
    customMetadataSchemaConfiguration={
        'optionalValue': {
            'defaultSchema': json.dumps(common_attributes),
            'recordTypeSchemaOverrides': [
                {'recordType': 'AGENT', 'schema': json.dumps(agent_fields)}
            ]
        }
    }
)
```

## Change the schema
<a name="registry-custom-metadata-schema-change"></a>

An update replaces the whole schema, so include every field and record type you want to keep.

You can make these changes at any time:
+ Add fields to the common attributes or to a record type.
+ Add allowed values to an Enum field. If you add one to a common attribute that a record type repeats, add it to that record type too, in the same update.
+ Make an optional field required.
+ Move a field from a record type into the common attributes, with the same type, at least the same allowed values, and the same required setting. The field then applies to every record type, and if it’s required, every record type must have a value for it. If the record type has no fields of its own left, you can remove it.

You can’t make these changes:
+ Rename a field.
+ Remove a field. The only exception is a record type’s field that you move into the common attributes.
+ Change a field’s type, for example from Text to Enum.
+ Remove an allowed value.
+ Make a required field optional.
+ Remove the common attributes.
+ Remove the custom metadata schema from the registry. Once a registry has a schema, it keeps one.

Existing records aren’t changed when you update the schema. A record that no longer matches it, for example because you made a field required, is reported as `NON_COMPLIANT` in `customMetadataSchemaComplianceStatus` and keeps its approval status. Update its custom metadata before you next submit it for approval.

## View the schema
<a name="registry-custom-metadata-schema-view"></a>

 **Console** — On the registry detail page, the **Custom metadata schema** section has a tab for each record type with the fields its records can carry.

 ** AWS CLI** 

```
aws agent-registry-control get-registry \
  --registry-id "<registryId>" \
  --region us-east-1 \
  --output json | jq '.customMetadataSchemaConfiguration'
```

 ** AWS SDK** 

```
import boto3

client = boto3.client('agent-registry-control')

registry = client.get_registry(registryId='<registryId>')
print(registry['customMetadataSchemaConfiguration'])
```

## Schema rules and limits
<a name="registry-custom-metadata-schema-constraints"></a>
+ Each field is Text (`{"type":"string"}`), Enum (`{"type":"string","enum":[…​]}`), URL (`{"type":"string","format":"uri"}`), or Boolean (`{"type":"boolean"}`). Fields can’t be nested or use other keywords, such as `default` or `pattern`.
+ A field has the same field type (Text, Enum, URL, or Boolean) everywhere in the schema. Its allowed values can differ by record type.
+ Field names can’t differ only in capitalization, such as `owner` and `Owner`.
+ Each schema is a JSON object with `"type": "object"` and at least one field in `properties`. It can also have `required`, `title`, and `description`, but not `$schema`.
+ A schema’s `required` list can only name fields in the same schema. To require a common attribute for one record type, repeat the field in that record type’s fields.

The following table lists the schema limits.


| Limit | Value | 
| --- | --- | 
| Fields a record type can carry, common attributes included (a repeated field counts once) | 30 | 
| Common attributes | 30 fields | 
| Number of allowed values per Enum field | 1–25 | 
| Allowed value length | 64 characters | 
| Field name length | 64 characters | 
| Schema `title`  | 64 characters | 
| Schema `description`  | 256 characters | 
| One schema (the common attributes, or one record type’s fields) | 16,384 characters | 
| Whole schema configuration | 128 KB | 
| Schemas per record type | 1 | 

For limits on values, see [Constraints](registry-custom-metadata-values.md#registry-custom-metadata-values-constraints) in [Set custom metadata values on a record](registry-custom-metadata-values.md).

## Related information
<a name="registry-custom-metadata-schema-related"></a>
+  [Set custom metadata values on a record](registry-custom-metadata-values.md) 
+  [Search for registry records](registry-search-records.md) — filter results by custom metadata values
+  [Supported record types and descriptors](registry-supported-record-types.md) 
+  [Create and manage registries](registry-create-manage.md) 