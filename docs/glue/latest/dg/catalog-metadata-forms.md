

# Attaching forms
<a name="catalog-metadata-forms"></a>

**Note**  
Business context and semantic search is in preview for AWS Glue and is subject to change.

You can standardize metadata by defining form types, which are reusable, structured schema templates. The schema can then be populated by attaching instances of these forms to assets.

## Defining form types
<a name="catalog-metadata-forms-defining"></a>

A form type defines the schema using Smithy IDL syntax. Names must start with an uppercase letter.

```
structure DataResidency {
    region: String
    complianceFramework: String
    retentionDays: Integer
}
```

### To create a form type
<a name="catalog-metadata-forms-put-form-type"></a>

Use `PutFormType` to create or update a form type.

```
aws glue put-form-type \
    --name DataResidency \
    --schema 'structure DataResidency {
    region: String
    complianceFramework: String
    retentionDays: Integer
}'
```

Example output:

```
{
    "Id": "DataResidency",
    "Name": "DataResidency"
}
```

### To retrieve a form type
<a name="catalog-metadata-forms-get-form-type"></a>

```
aws glue get-form-type --identifier DataResidency
```

## Attaching forms to assets
<a name="catalog-metadata-forms-attaching"></a>

### To attach a form to an asset
<a name="catalog-metadata-forms-put-attachment"></a>

Use `PutAttachment` with the asset identifier, attachment name, form type ID, and JSON content conforming to the schema.

```
aws glue put-attachment \
    --asset-identifier {{asset-id}} \
    --attachment-name residencyInfo \
    --form-type-id DataResidency \
    --content '{"region":"us-east-1","complianceFramework":"SOC2","retentionDays":730}'
```

### To view an asset's forms and attachments
<a name="catalog-metadata-forms-get-asset-attachments"></a>

Use `GetAsset` to retrieve an asset along with its forms and attachments.

The following command retrieves an asset:

```
aws glue get-asset --asset-identifier {{asset-id}}
```

### To attach a form to a column
<a name="catalog-metadata-forms-put-attachment-item"></a>

You can attach a form to a single column of an asset.

Each column is a single item of the `columns` iterable form with column name as the item identifier.

The following command attaches a form to a specific column:

```
aws glue put-attachment \
    --asset-identifier {{asset-id}} \
    --iterable-form-name columns \
    --item-identifier region \
    --attachment-name sensitivity \
    --form-type-id DataClassification \
    --content '{"classification":"PII","sensitivity":"HIGH"}'
```

After you attach the form, use `SearchAssets` to discover the asset by any searchable fields on the form.

## Retrieving column metadata
<a name="catalog-metadata-forms-retrieving-columns"></a>

### To list columns for an asset
<a name="catalog-metadata-forms-list-iterable"></a>

```
aws glue list-iterable-forms \
    --asset-identifier {{asset-id}} \
    --iterable-form-name columns \
    --max-results 20
```

### To retrieve specific columns with their forms
<a name="catalog-metadata-forms-batch-get"></a>

Use `BatchGetIterableForms` to retrieve columns and attached forms in a single request.

```
aws glue batch-get-iterable-forms \
    --asset-identifier {{asset-id}} \
    --iterable-form-name columns \
    --item-identifiers region email
```

Example output:

```
{
    "Items": [
        {
            "ItemId": "{{asset-id}}#region",
            "ItemName": "region",
            "GlossaryTerms": ["{{term-id}}"],
            "Forms": {},
            "Attachments": {
                "sensitivity": {"FormTypeId": "DataClassification", "Content": "{\"classification\":\"PII\",\"sensitivity\":\"HIGH\"}"}
            }
        },
        {
            "ItemId": "{{asset-id}}#email",
            "ItemName": "email",
            "Forms": {},
            "Attachments": {}
        }
    ],
    "Errors": []
}
```

## Deleting attachments and form types
<a name="catalog-metadata-forms-deleting"></a>

### To delete an attachment
<a name="catalog-metadata-forms-delete-attachment"></a>

```
aws glue delete-attachment \
    --asset-identifier {{asset-id}} \
    --attachment-name residencyInfo
```

### To delete an attachment from a specific column
<a name="catalog-metadata-forms-delete-attachment-item"></a>

To remove a form attached to a single column, run the following command. Pass the iterable form name, item identifier, and attachment name:

```
aws glue delete-attachment \
    --asset-identifier {{asset-id}} \
    --iterable-form-name columns \
    --item-identifier region \
    --attachment-name sensitivity
```

### To delete a form type
<a name="catalog-metadata-forms-delete-form-type"></a>

You cannot delete a form type that is still referenced by an asset type.

```
aws glue delete-form-type --identifier DataResidency
```

## Listing form types
<a name="catalog-metadata-forms-listing"></a>

```
aws glue list-form-types --max-results 20
```

Example output:

```
{
    "Items": [
        {"Id": "DataResidency", "Name": "DataResidency"},
        {"Id": "DataClassification", "Name": "DataClassification"}
    ]
}
```