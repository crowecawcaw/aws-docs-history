

# Mapping templates and implicit object types in Customer Profiles
<a name="templates-and-implicit-types"></a>

With mapping templates, you can ingest data from well-known sources without writing field and key definitions yourself. With implicit object types, you can use a template by name without explicitly creating it first. This topic explains both and how they interact with explicit object types.

## Mapping templates
<a name="mapping-templates"></a>

A mapping template is a predefined object type mapping included with Connect Customer Customer Profiles. Templates exist for standard object types (such as `_asset`, `_case`, `_order`, `_communicationRecord`, `_loyalty`, and several travel records), for contact records (`CTR`, `CTR-NoInferred`, `CTR-AutoAssociateOnly`), and for third-party sources such as Salesforce, ServiceNow, Marketo, and Zendesk.

For the complete, current list, use the [ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html) API.

**Note**  
When you create an object type from a template, you can't also specify `Fields` or `Keys`—the template provides them. For non-standard object types, you can still set `ExpirationDays` and `EncryptionKey`.

## Implicit object types
<a name="implicit-object-types"></a>

You can use any object type whose name matches a template ID (as returned by [ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html)) without explicitly defining it. The object type uses the template's definition exactly. This is called an implicit object type.

## Replacing an implicit object type with an explicit one
<a name="replace-implicit-object-type"></a>

If you create an explicit object type whose name was previously implicit, your explicit definition replaces the template definition entirely—you can't partially override a template. Keep these behaviors in mind:
+ Subsequent ingestions follow the explicit definition.
+ The object type's `createdAt` timestamp is set to the time you created the explicit definition.
+ Already-ingested data is not reprocessed automatically. Existing objects retain the field values they were ingested with. For more information, see [Update and validate an object type mapping in Customer Profiles](update-and-validate-mapping.md).