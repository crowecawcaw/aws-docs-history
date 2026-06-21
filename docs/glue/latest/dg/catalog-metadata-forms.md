# Attaching forms

###### Note

Business context and semantic search is in preview for AWS Glue and is subject to change.

You can standardize metadata by defining form types, which are reusable,
structured schema templates. The schema can then be populated by attaching instances of
these forms to assets.

## Defining form types

A form type defines the schema using Smithy IDL syntax. Names must start with an
uppercase letter.

```
structure DataResidency {
    region: String
    complianceFramework: String
    retentionDays: Integer
}
```

### To create a form type

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

```
aws glue get-form-type --identifier DataResidency
```

## Attaching forms to assets

### To attach a form to an asset

Use `PutAttachment` with the asset identifier, attachment name, form
type ID, and JSON content conforming to the schema.

```
aws glue put-attachment \
    --asset-identifier `asset-id` \
    --attachment-name residencyInfo \
    --form-type-id DataResidency \
    --content '{"region":"us-east-1","complianceFramework":"SOC2","retentionDays":730}'
```

## Retrieving column metadata

### To list columns for an asset

```
aws glue list-iterable-forms \
    --asset-identifier `asset-id` \
    --iterable-form-name columns \
    --max-results 20
```

### To retrieve specific columns with their forms

Use `BatchGetIterableForms` to retrieve columns and attached forms in
a single request.

```
aws glue batch-get-iterable-forms \
    --asset-identifier `asset-id` \
    --iterable-form-name columns \
    --item-identifiers region email
```

## Deleting attachments and form types

### To delete an attachment

```
aws glue delete-attachment \
    --asset-identifier `asset-id` \
    --attachment-name residencyInfo
```

### To delete a form type

You cannot delete a form type that is still referenced by an asset type.

```
aws glue delete-form-type --identifier DataResidency
```

## Listing form types

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
