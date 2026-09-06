

# Business context APIs
<a name="aws-glue-api-catalog-aws-glue-api-semantics"></a>

The business context API describes the data types and operations for managing assets, asset types, form types, glossaries, glossary terms, attachments, and search in the AWS Glue Data Catalog.

## Data types
<a name="aws-glue-api-catalog-aws-glue-api-semantics-objects"></a>
+ [AssetFormEntry structure](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry)
+ [AssetTypeFormReference structure](#aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeFormReference)
+ [IterableFormEntry structure](#aws-glue-api-catalog-aws-glue-api-semantics-IterableFormEntry)
+ [IterableFormItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-IterableFormItem)
+ [IterableFormListItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-IterableFormListItem)
+ [SearchResultItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchResultItem)
+ [SearchSort structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchSort)
+ [SearchFilterClause structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterClause)
+ [SearchAttributeFilter structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchAttributeFilter)
+ [SearchMapFilter structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchMapFilter)
+ [SearchMapFilterValue structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchMapFilterValue)
+ [SearchFilterValue structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterValue)
+ [ItemError structure](#aws-glue-api-catalog-aws-glue-api-semantics-ItemError)
+ [AssetTypeItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeItem)
+ [FormTypeItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-FormTypeItem)
+ [GlossaryItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-GlossaryItem)
+ [GlossaryTermItem structure](#aws-glue-api-catalog-aws-glue-api-semantics-GlossaryTermItem)
+ [GetAssetOutput structure](#aws-glue-api-catalog-aws-glue-api-semantics-GetAssetOutput)
+ [SearchAssetsOutput structure](#aws-glue-api-catalog-aws-glue-api-semantics-SearchAssetsOutput)
+ [ExportEncryptionConfiguration structure](#aws-glue-api-catalog-aws-glue-api-semantics-ExportEncryptionConfiguration)
+ [GetDataCatalogExportConfigurationOutput structure](#aws-glue-api-catalog-aws-glue-api-semantics-GetDataCatalogExportConfigurationOutput)
+ [PutDataCatalogExportConfigurationOutput structure](#aws-glue-api-catalog-aws-glue-api-semantics-PutDataCatalogExportConfigurationOutput)

## AssetFormEntry structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry"></a>

A form on an asset, consisting of the form type identifier and its JSON content.

**Fields**
+ `FormTypeId` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type that defines this form's schema.
+ `Content` – UTF-8 string.

  The JSON content of the form, conforming to the schema of the specified form type.

## AssetTypeFormReference structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeFormReference"></a>

A reference to a form type that is included in an asset type.

**Fields**
+ `FormTypeIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the referenced form type.

## IterableFormEntry structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-IterableFormEntry"></a>

An iterable form available on an asset, identified by its form type.

**Fields**
+ `FormTypeId` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The form type identifier of the iterable form (for example, `columns`), used to retrieve its items via `ListIterableForms` or `BatchGetIterableForms`.

## IterableFormItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-IterableFormItem"></a>

A full iterable form item with its forms.

**Fields**
+ `ItemId` – UTF-8 string.

  The unique identifier of the item.
+ `ItemName` – UTF-8 string.

  The name of the item.
+ `GlossaryTerms` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The identifiers of the glossary terms associated with the item.
+ `Forms` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [AssetFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry) object.

  The forms on the item, keyed by form name.
+ `Attachments` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [AssetFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry) object.

  Additional attachments on the item for more context, keyed by attachment name.

## IterableFormListItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-IterableFormListItem"></a>

A summary of an item in an iterable form.

**Fields**
+ `ItemId` – UTF-8 string.

  The unique identifier of the item.
+ `ItemName` – UTF-8 string.

  The name of the item.
+ `Description` – UTF-8 string.

  The description of the item.
+ `GlossaryTerms` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The identifiers of the glossary terms associated with the item.

## SearchResultItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchResultItem"></a>

A single search result item representing a matched asset.

**Fields**
+ `Id` – UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the matched asset.
+ `AssetName` – UTF-8 string.

  The name of the matched asset.
+ `AssetDescription` – UTF-8 string.

  The description of the matched asset.
+ `UpdatedAt` – Timestamp.

  The timestamp at which the matched asset was last updated.
+ `AssetTypeId` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type for the matched asset.

## SearchSort structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchSort"></a>

The sort criteria for search results.

**Fields**
+ `Attribute` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The attribute to sort by.
+ `Order` – UTF-8 string (valid values: `ASCENDING` \| `DESCENDING`).

  The sort order. Valid values are `ASCENDING` and `DESCENDING`.

## SearchFilterClause structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterClause"></a>

A filter clause that supports nested boolean logic. Exactly one of `andAllFilters`, `orAnyFilters`, `attributeFilter`, or `mapFilter` must be specified.

**Fields**
+ `AndAllFilters` – An array of [SearchFilterClause](#aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterClause) objects, not less than 1 or more than 10 structures.

  A list of filter clauses that must all match (logical AND).
+ `OrAnyFilters` – An array of [SearchFilterClause](#aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterClause) objects, not less than 1 or more than 10 structures.

  A list of filter clauses where at least one must match (logical OR).
+ `AttributeFilter` – A [SearchAttributeFilter](#aws-glue-api-catalog-aws-glue-api-semantics-SearchAttributeFilter) object.

  A filter on a single attribute value.
+ `MapFilter` – A [SearchMapFilter](#aws-glue-api-catalog-aws-glue-api-semantics-SearchMapFilter) object.

  A filter on a map attribute's key-value pair.

## SearchAttributeFilter structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchAttributeFilter"></a>

A filter that compares an attribute value using an operator.

**Fields**
+ `Attribute` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The attribute name to filter on.
+ `Operator` – *Required:* UTF-8 string (valid values: `equals` \| `greaterThan` \| `greaterThanOrEquals` \| `lessThan` \| `lessThanOrEquals` \| `notExists`).

  The comparison operator. Valid values are `equals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, and `notExists`.
+ `Value` – A [SearchFilterValue](#aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterValue) object.

  The value to compare against.

## SearchMapFilter structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchMapFilter"></a>

A filter on a map attribute's key-value pair.

**Fields**
+ `Attribute` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The map attribute name to filter on.
+ `Key` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long.

  The key within the map attribute to filter on.
+ `Value` – *Required:* A [SearchMapFilterValue](#aws-glue-api-catalog-aws-glue-api-semantics-SearchMapFilterValue) object.

  The value to compare against.

## SearchMapFilterValue structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchMapFilterValue"></a>

A map filter value. Currently supports string comparison only.

**Fields**
+ `StringValue` – UTF-8 string, not more than 256 bytes long.

  A string filter value.

## SearchFilterValue structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterValue"></a>

A filter value. Exactly one of `stringValue` or `longValue` must be specified.

**Fields**
+ `StringValue` – UTF-8 string, not more than 256 bytes long.

  A string filter value.
+ `LongValue` – Number (long).

  A long integer filter value.

## ItemError structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ItemError"></a>

An error that occurred when retrieving an iterable form item.

**Fields**
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item that caused the error.
+ `Code` – UTF-8 string.

  The error code.
+ `Message` – UTF-8 string.

  The error message.

## AssetTypeItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeItem"></a>

A summary of an asset type.

**Fields**
+ `Id` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type.
+ `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  The name of the asset type.

## FormTypeItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-FormTypeItem"></a>

A summary of a form type.

**Fields**
+ `Id` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type.
+ `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #77](aws-glue-api-common.md#regex_77).

  The name of the form type.

## GlossaryItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GlossaryItem"></a>

A summary of a business glossary.

**Fields**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary.
+ `Description` – UTF-8 string, not less than 1 or more than 2048 bytes long.

  The description of the glossary.

## GlossaryTermItem structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GlossaryTermItem"></a>

A summary of a glossary term.

**Fields**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary term.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary term.
+ `ShortDescription` – UTF-8 string, not less than 1 or more than 1024 bytes long.

  The short description of the glossary term.

## GetAssetOutput structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetAssetOutput"></a>

The asset metadata returned by the `GetAsset` operation.

**Fields**
+ `Id` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `Name` – UTF-8 string.

  The name of the asset.
+ `Description` – UTF-8 string.

  The description of the asset.
+ `CreatedAt` – Timestamp.

  The timestamp at which the asset was created.
+ `UpdatedAt` – Timestamp.

  The timestamp at which the asset was last updated.
+ `AssetTypeId` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type for this asset.
+ `GlossaryTerms` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The identifiers of the glossary terms associated with the asset.
+ `Forms` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [AssetFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry) object.

  The forms on the asset, keyed by form name.
+ `Attachments` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [AssetFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry) object.

  Additional attachments on the asset for more context, keyed by attachment name.
+ `IterableForms` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [IterableFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-IterableFormEntry) object.

  The iterable forms available on the asset, keyed by form name (for example, `columns`). Use the form name with `ListIterableForms` or `BatchGetIterableForms` to retrieve the form's items.

## SearchAssetsOutput structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchAssetsOutput"></a>

The search results returned by the `SearchAssets` operation.

**Fields**
+ `Items` – An array of [SearchResultItem](#aws-glue-api-catalog-aws-glue-api-semantics-SearchResultItem) objects.

  The list of assets matching the search criteria.
+ `NextToken` – UTF-8 string.

  A continuation token, present if the current segment is not the last.

## ExportEncryptionConfiguration structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ExportEncryptionConfiguration"></a>

The encryption configuration for exported data catalog metadata.

**Fields**
+ `SseAlgorithm` – UTF-8 string.

  The server-side encryption algorithm used for the exported data. Valid values are `AES256` and `aws:kms`.
+ `KmsKeyArn` – UTF-8 string, matching the [Custom string pattern #72](aws-glue-api-common.md#regex_72).

  The ARN of the KMS key used to encrypt the exported data.

## GetDataCatalogExportConfigurationOutput structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetDataCatalogExportConfigurationOutput"></a>

The export configuration returned by the `GetDataCatalogExportConfiguration` operation.

**Fields**
+ `ExportSetting` – UTF-8 string (valid values: `ENABLED` \| `DISABLED`).

  The export setting for the data catalog. Valid values are `ENABLED` and `DISABLED`.
+ `Status` – UTF-8 string (valid values: `ENABLING` \| `ENABLED` \| `DISABLING` \| `DISABLED` \| `FAILED`).

  The current status of the export. Valid values are `ENABLING`, `ENABLED`, `DISABLING`, `DISABLED`, and `FAILED`.
+ `EncryptionConfiguration` – An [ExportEncryptionConfiguration](#aws-glue-api-catalog-aws-glue-api-semantics-ExportEncryptionConfiguration) object.

  The encryption configuration for the exported data.
+ `S3TableBucketArn` – UTF-8 string.

  The ARN of the S3 Tables bucket where catalog metadata is exported.
+ `CreatedAt` – Timestamp.

  The timestamp at which the export configuration was created.
+ `UpdatedAt` – Timestamp.

  The timestamp at which the export configuration was last updated.

## PutDataCatalogExportConfigurationOutput structure
<a name="aws-glue-api-catalog-aws-glue-api-semantics-PutDataCatalogExportConfigurationOutput"></a>

The export configuration returned by the `PutDataCatalogExportConfiguration` operation.

**Fields**
+ `ExportSetting` – UTF-8 string (valid values: `ENABLED` \| `DISABLED`).

  The export setting for the data catalog.
+ `EncryptionConfiguration` – An [ExportEncryptionConfiguration](#aws-glue-api-catalog-aws-glue-api-semantics-ExportEncryptionConfiguration) object.

  The encryption configuration for the exported data.

## Operations
<a name="aws-glue-api-catalog-aws-glue-api-semantics-actions"></a>
+ [GetAsset action (Python: get\_asset)](#aws-glue-api-catalog-aws-glue-api-semantics-GetAsset)
+ [PutAsset action (Python: put\_asset)](#aws-glue-api-catalog-aws-glue-api-semantics-PutAsset)
+ [DeleteAsset action (Python: delete\_asset)](#aws-glue-api-catalog-aws-glue-api-semantics-DeleteAsset)
+ [PutAssetType action (Python: put\_asset\_type)](#aws-glue-api-catalog-aws-glue-api-semantics-PutAssetType)
+ [GetAssetType action (Python: get\_asset\_type)](#aws-glue-api-catalog-aws-glue-api-semantics-GetAssetType)
+ [DeleteAssetType action (Python: delete\_asset\_type)](#aws-glue-api-catalog-aws-glue-api-semantics-DeleteAssetType)
+ [ListAssetTypes action (Python: list\_asset\_types)](#aws-glue-api-catalog-aws-glue-api-semantics-ListAssetTypes)
+ [PutFormType action (Python: put\_form\_type)](#aws-glue-api-catalog-aws-glue-api-semantics-PutFormType)
+ [GetFormType action (Python: get\_form\_type)](#aws-glue-api-catalog-aws-glue-api-semantics-GetFormType)
+ [DeleteFormType action (Python: delete\_form\_type)](#aws-glue-api-catalog-aws-glue-api-semantics-DeleteFormType)
+ [ListFormTypes action (Python: list\_form\_types)](#aws-glue-api-catalog-aws-glue-api-semantics-ListFormTypes)
+ [PutAttachment action (Python: put\_attachment)](#aws-glue-api-catalog-aws-glue-api-semantics-PutAttachment)
+ [DeleteAttachment action (Python: delete\_attachment)](#aws-glue-api-catalog-aws-glue-api-semantics-DeleteAttachment)
+ [ListIterableForms action (Python: list\_iterable\_forms)](#aws-glue-api-catalog-aws-glue-api-semantics-ListIterableForms)
+ [BatchGetIterableForms action (Python: batch\_get\_iterable\_forms)](#aws-glue-api-catalog-aws-glue-api-semantics-BatchGetIterableForms)
+ [CreateGlossary action (Python: create\_glossary)](#aws-glue-api-catalog-aws-glue-api-semantics-CreateGlossary)
+ [GetGlossary action (Python: get\_glossary)](#aws-glue-api-catalog-aws-glue-api-semantics-GetGlossary)
+ [UpdateGlossary action (Python: update\_glossary)](#aws-glue-api-catalog-aws-glue-api-semantics-UpdateGlossary)
+ [DeleteGlossary action (Python: delete\_glossary)](#aws-glue-api-catalog-aws-glue-api-semantics-DeleteGlossary)
+ [ListGlossaries action (Python: list\_glossaries)](#aws-glue-api-catalog-aws-glue-api-semantics-ListGlossaries)
+ [CreateGlossaryTerm action (Python: create\_glossary\_term)](#aws-glue-api-catalog-aws-glue-api-semantics-CreateGlossaryTerm)
+ [GetGlossaryTerm action (Python: get\_glossary\_term)](#aws-glue-api-catalog-aws-glue-api-semantics-GetGlossaryTerm)
+ [UpdateGlossaryTerm action (Python: update\_glossary\_term)](#aws-glue-api-catalog-aws-glue-api-semantics-UpdateGlossaryTerm)
+ [DeleteGlossaryTerm action (Python: delete\_glossary\_term)](#aws-glue-api-catalog-aws-glue-api-semantics-DeleteGlossaryTerm)
+ [ListGlossaryTerms action (Python: list\_glossary\_terms)](#aws-glue-api-catalog-aws-glue-api-semantics-ListGlossaryTerms)
+ [AssociateGlossaryTerms action (Python: associate\_glossary\_terms)](#aws-glue-api-catalog-aws-glue-api-semantics-AssociateGlossaryTerms)
+ [DisassociateGlossaryTerms action (Python: disassociate\_glossary\_terms)](#aws-glue-api-catalog-aws-glue-api-semantics-DisassociateGlossaryTerms)
+ [SearchAssets action (Python: search\_assets)](#aws-glue-api-catalog-aws-glue-api-semantics-SearchAssets)
+ [GetDataCatalogExportConfiguration action (Python: get\_data\_catalog\_export\_configuration)](#aws-glue-api-catalog-aws-glue-api-semantics-GetDataCatalogExportConfiguration)
+ [PutDataCatalogExportConfiguration action (Python: put\_data\_catalog\_export\_configuration)](#aws-glue-api-catalog-aws-glue-api-semantics-PutDataCatalogExportConfiguration)

## GetAsset action (Python: get\_asset)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetAsset"></a>

Retrieves the metadata for an asset in AWS Glue Data Catalog, including its forms, additional attachments, and associated glossary terms.

**Example**  
The following example retrieves an asset by its identifier.  

```
aws glue get-asset --identifier quarterly-sales-2026q1
    
    {
        "Id": "quarterly-sales-2026q1",
        "Name": "Quarterly Sales 2026 Q1",
        "Description": "Aggregated quarterly sales metrics",
        "CreatedAt": "2026-06-16T06:42:00.442Z",
        "AssetTypeId": "DataSet",
        "GlossaryTerms": [],
        "Forms": {
            "DataClassification": {
                "FormTypeId": "DataClassification",
                "Content": "{\"classification\":\"internal\",\"owner\":\"data-platform-team\"}"
            }
        },
        "Attachments": {},
        "IterableForms": {}
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset to retrieve.

**Response**

The asset metadata returned by the `GetAsset` operation.
+ `GetAssetOutput` – A [GetAssetOutput](#aws-glue-api-catalog-aws-glue-api-semantics-GetAssetOutput) object.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `ThrottlingException`
+ `InvalidInputException`

## PutAsset action (Python: put\_asset)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-PutAsset"></a>

Creates or updates an asset in AWS Glue Data Catalog. If the asset already exists, this operation updates it; otherwise, a new asset is created.

**Example**  
The following example creates an asset with a form.  

```
aws glue put-asset \
        --asset-type-id DataSet \
        --identifier quarterly-sales-2026q1 \
        --name "Quarterly Sales 2026 Q1" \
        --description "Aggregated quarterly sales metrics" \
        --forms '{"DataClassification":{"FormTypeId":"DataClassification","Content":"{\"classification\":\"internal\",\"owner\":\"data-platform-team\"}"}}'
    
    {
        "Id": "quarterly-sales-2026q1",
        "Name": "Quarterly Sales 2026 Q1",
        "Description": "Aggregated quarterly sales metrics",
        "CreatedAt": "2026-06-16T06:42:00.442Z",
        "Forms": {
            "DataClassification": {
                "FormTypeId": "DataClassification",
                "Content": "{\"classification\":\"internal\",\"owner\":\"data-platform-team\"}"
            }
        }
    }
```

**Request**
+ `AssetTypeId` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type for the asset.
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset. If an asset with this identifier already exists, it is updated.
+ `Name` – *Required:* UTF-8 string.

  The name of the asset.
+ `Description` – UTF-8 string.

  The description of the asset.
+ `Forms` – *Required:* A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [AssetFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry) object.

  The forms to set on the asset, keyed by form name. Each entry specifies the form type and its JSON content.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `Name` – *Required:* UTF-8 string.

  The name of the asset.
+ `Description` – UTF-8 string.

  The description of the asset.
+ `CreatedAt` – Timestamp.

  The timestamp at which the asset was created.
+ `Forms` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a An [AssetFormEntry](#aws-glue-api-catalog-aws-glue-api-semantics-AssetFormEntry) object.

  The forms attached to the asset, keyed by form name.

**Errors**
+ `AccessDeniedException`
+ `ConcurrentModificationException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## DeleteAsset action (Python: delete\_asset)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DeleteAsset"></a>

Deletes an asset from AWS Glue Data Catalog.

**Example**  
The following example deletes an asset by its identifier.  

```
aws glue delete-asset --identifier quarterly-sales-2026q1
```

**Request**
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset to delete.

**Response**
+ *No Response parameters.*

**Errors**
+ `AccessDeniedException`
+ `ConcurrentModificationException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## PutAssetType action (Python: put\_asset\_type)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-PutAssetType"></a>

Creates or updates an asset type in AWS Glue Data Catalog. An asset type defines the structure of assets by specifying which forms they include. If an asset type with the given name already exists, it is updated.

**Example**  
The following example creates an asset type that references a form type.  

```
aws glue put-asset-type \
        --name DataSet \
        --forms '{"DataClassification":{"FormTypeIdentifier":"DataClassification"}}'
    
    {
        "Id": "DataSet",
        "Name": "DataSet",
        "Forms": {
            "DataClassification": {
                "FormTypeIdentifier": "DataClassification"
            }
        }
    }
```

**Request**
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  The name of the asset type.
+ `Forms` – *Required:* A map array of key-value pairs, not less than 1 or more than 100 pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  Each value is a An [AssetTypeFormReference](#aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeFormReference) object.

  The forms that make up the asset type, keyed by form name. Each entry references the form type that defines the form's schema.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type.
+ `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  The name of the asset type.
+ `Forms` – A map array of key-value pairs, not less than 1 or more than 100 pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  Each value is a An [AssetTypeFormReference](#aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeFormReference) object.

  The forms that make up the asset type, keyed by form name.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## GetAssetType action (Python: get\_asset\_type)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetAssetType"></a>

Retrieves an asset type in AWS Glue Data Catalog by its identifier.

**Example**  
The following example retrieves an asset type by its identifier.  

```
aws glue get-asset-type --identifier DataSet
    
    {
        "Id": "DataSet",
        "Name": "DataSet",
        "Forms": {
            "DataClassification": {
                "FormTypeIdentifier": "DataClassification"
            }
        }
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type to retrieve.

**Response**
+ `Id` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type.
+ `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  The name of the asset type.
+ `Forms` – A map array of key-value pairs, not less than 1 or more than 100 pairs.

  Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #75](aws-glue-api-common.md#regex_75).

  Each value is a An [AssetTypeFormReference](#aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeFormReference) object.

  The forms that make up the asset type, keyed by form name.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## DeleteAssetType action (Python: delete\_asset\_type)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DeleteAssetType"></a>

Deletes an asset type from AWS Glue Data Catalog.

**Example**  
The following example deletes an asset type by its identifier.  

```
aws glue delete-asset-type --identifier DataSet
```

**Request**
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the asset type to delete.

**Response**
+ *No Response parameters.*

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## ListAssetTypes action (Python: list\_asset\_types)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ListAssetTypes"></a>

Lists the asset types defined in AWS Glue Data Catalog.

**Example**  
The following example lists the asset types in the account.  

```
aws glue list-asset-types --max-results 20
    
    {
        "Items": [
            {
                "Id": "DataSet",
                "Name": "DataSet"
            }
        ]
    }
```

**Request**
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of results to return in the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.

**Response**
+ `Items` – An array of [AssetTypeItem](#aws-glue-api-catalog-aws-glue-api-semantics-AssetTypeItem) objects.

  The list of asset type items.
+ `NextToken` – UTF-8 string.

  A continuation token, present if the current segment is not the last.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## PutFormType action (Python: put\_form\_type)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-PutFormType"></a>

Creates or updates a form type in AWS Glue Data Catalog. A form type defines the schema for structured metadata that can be attached to assets.

**Example**  
The following example creates a form type with a Smithy schema.  

```
aws glue put-form-type \
        --name DataClassification \
        --schema 'structure DataClassification {
        classification: String
        owner: String
    }'
    
    {
        "Id": "DataClassification",
        "Name": "DataClassification",
        "Schema": "structure DataClassification {\n    classification: String\n    owner: String\n}"
    }
```

**Request**
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #77](aws-glue-api-common.md#regex_77).

  The name of the form type. Must start with an uppercase letter.
+ `Schema` – *Required:* UTF-8 string, not less than 1 or more than 100000 bytes long.

  The Smithy IDL schema definition for the form type.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type.
+ `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #77](aws-glue-api-common.md#regex_77).

  The name of the form type.
+ `Schema` – UTF-8 string, not less than 1 or more than 100000 bytes long.

  The Smithy IDL schema of the form type.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## GetFormType action (Python: get\_form\_type)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetFormType"></a>

Retrieves a form type in AWS Glue Data Catalog by its identifier.

**Example**  
The following example retrieves a form type by its identifier.  

```
aws glue get-form-type --identifier DataClassification
    
    {
        "Id": "DataClassification",
        "Name": "DataClassification",
        "Schema": "structure DataClassification {\n    classification: String\n    owner: String\n}"
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type to retrieve.

**Response**
+ `Id` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type.
+ `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #77](aws-glue-api-common.md#regex_77).

  The name of the form type.
+ `Schema` – UTF-8 string, not less than 1 or more than 100000 bytes long.

  The Smithy IDL schema of the form type.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## DeleteFormType action (Python: delete\_form\_type)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DeleteFormType"></a>

Deletes a form type from AWS Glue Data Catalog. A form type cannot be deleted if it is still referenced by an asset type.

**Example**  
The following example deletes a form type by its identifier.  

```
aws glue delete-form-type --identifier DataClassification
```

**Request**
+ `Identifier` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type to delete.

**Response**
+ *No Response parameters.*

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ConflictException`
+ `ThrottlingException`

## ListFormTypes action (Python: list\_form\_types)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ListFormTypes"></a>

Lists the form types defined in AWS Glue Data Catalog.

**Example**  
The following example lists the form types in the account.  

```
aws glue list-form-types --max-results 20
    
    {
        "Items": [
            {
                "Id": "DataClassification",
                "Name": "DataClassification"
            }
        ]
    }
```

**Request**
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of results to return in the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.

**Response**
+ `Items` – *Required:* An array of [FormTypeItem](#aws-glue-api-catalog-aws-glue-api-semantics-FormTypeItem) objects.

  The list of form type items.
+ `NextToken` – UTF-8 string.

  A continuation token, present if the current segment is not the last.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## PutAttachment action (Python: put\_attachment)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-PutAttachment"></a>

Attaches a form to an asset or an iterable form item in AWS Glue Data Catalog. If an attachment with the same name already exists, it is overwritten.

**Example**  
The following example attaches a form to an asset.  

```
aws glue put-attachment \
        --asset-identifier quarterly-sales-2026q1 \
        --attachment-name reviewNote \
        --form-type-id DataClassification \
        --content '{"classification":"internal","owner":"analytics-team"}'
    
    {
        "AssetIdentifier": "quarterly-sales-2026q1",
        "AttachmentName": "reviewNote",
        "FormTypeId": "DataClassification"
    }
```

**Request**
+ `AssetIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset to attach the form to.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form. When specified along with `itemIdentifier`, the attachment targets an item within the iterable form rather than the asset itself.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
+ `AttachmentName` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #76](aws-glue-api-common.md#regex_76).

  The name of the attachment.
+ `Content` – *Required:* UTF-8 string.

  The JSON content of the form, conforming to the schema of the specified form type.
+ `FormTypeId` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type for this attachment.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `AssetIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form, if the attachment targets an item.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form, if applicable.
+ `AttachmentName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #76](aws-glue-api-common.md#regex_76).

  The name of the attachment.
+ `FormTypeId` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The identifier of the form type for this attachment.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## DeleteAttachment action (Python: delete\_attachment)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DeleteAttachment"></a>

Deletes a form attachment from an asset in AWS Glue Data Catalog.

**Example**  
The following example deletes an attachment from an asset.  

```
aws glue delete-attachment \
        --asset-identifier quarterly-sales-2026q1 \
        --attachment-name reviewNote
    
    {
        "AssetIdentifier": "quarterly-sales-2026q1"
    }
```

**Request**
+ `AssetIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset from which to delete the attachment.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form. When specified along with `itemIdentifier`, the attachment is deleted from an item within the iterable form rather than from the asset itself.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
+ `AttachmentName` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #76](aws-glue-api-common.md#regex_76).

  The name of the attachment to delete.

**Response**
+ `AssetIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form, if the deletion targets an item.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form, if applicable.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## ListIterableForms action (Python: list\_iterable\_forms)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ListIterableForms"></a>

Lists the items in an iterable form on an asset in AWS Glue Data Catalog. For example, lists the columns of a table asset.

**Example**  
The following example lists the columns of an asset.  

```
aws glue list-iterable-forms \
        --asset-identifier quarterly-sales-2026q1 \
        --iterable-form-name columns \
        --max-results 20
    
    {
        "AssetId": "quarterly-sales-2026q1",
        "IterableFormName": "columns",
        "Items": [
            {
                "ItemId": "quarterly-sales-2026q1#region",
                "ItemName": "region",
                "Description": "AWS region of the sales record",
                "GlossaryTerms": []
            },
            {
                "ItemId": "quarterly-sales-2026q1#amount",
                "ItemName": "amount",
                "Description": "Sales amount in USD",
                "GlossaryTerms": []
            }
        ]
    }
```

**Request**
+ `AssetIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form to list items from.
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of results to return in the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.

**Response**
+ `AssetId` – UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form.
+ `Items` – An array of [IterableFormListItem](#aws-glue-api-catalog-aws-glue-api-semantics-IterableFormListItem) objects.

  The list of iterable form items.
+ `NextToken` – UTF-8 string.

  A continuation token, present if the current segment is not the last.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `ThrottlingException`
+ `InvalidInputException`

## BatchGetIterableForms action (Python: batch\_get\_iterable\_forms)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-BatchGetIterableForms"></a>

Retrieves multiple items from an iterable form on an asset in AWS Glue Data Catalog in a single request.

**Example**  
The following example retrieves specific columns by identifier.  

```
aws glue batch-get-iterable-forms \
        --asset-identifier quarterly-sales-2026q1 \
        --iterable-form-name columns \
        --item-identifiers region amount
    
    {
        "Items": [
            {
                "ItemId": "quarterly-sales-2026q1#region",
                "ItemName": "region",
                "GlossaryTerms": [],
                "Forms": {
                    "columns": {
                        "FormTypeId": "amazon.glue::Column",
                        "Content": "{\"type\":\"string\"}"
                    }
                },
                "Attachments": {}
            },
            {
                "ItemId": "quarterly-sales-2026q1#amount",
                "ItemName": "amount",
                "GlossaryTerms": [],
                "Forms": {
                    "columns": {
                        "FormTypeId": "amazon.glue::Column",
                        "Content": "{\"type\":\"double\"}"
                    }
                },
                "Attachments": {}
            }
        ],
        "Errors": []
    }
```

**Request**
+ `AssetIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form to retrieve items from.
+ `ItemIdentifiers` – *Required:* An array of UTF-8 strings, not less than 1 or more than 100 strings.

  The list of item identifiers to retrieve. Each identifier can be an item ID or item name.

**Response**
+ `Items` – An array of [IterableFormItem](#aws-glue-api-catalog-aws-glue-api-semantics-IterableFormItem) objects.

  The list of retrieved iterable form items.
+ `Errors` – An array of [ItemError](#aws-glue-api-catalog-aws-glue-api-semantics-ItemError) objects.

  The list of errors for items that could not be retrieved.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## CreateGlossary action (Python: create\_glossary)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-CreateGlossary"></a>

Creates a business glossary in AWS Glue Data Catalog. A glossary is a container for glossary terms that define business concepts.

**Example**  
The following example creates a business glossary.  

```
aws glue create-glossary \
        --name "Sales Terms" \
        --description "Glossary of sales-domain business terms"
    
    {
        "Id": "6n5f21s641nbjb",
        "Name": "Sales Terms",
        "Description": "Glossary of sales-domain business terms"
    }
```

**Request**
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary.
+ `Description` – UTF-8 string, not less than 1 or more than 2048 bytes long.

  The description of the glossary.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary.
+ `Description` – UTF-8 string, not less than 1 or more than 2048 bytes long.

  The description of the glossary.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`
+ `AlreadyExistsException`

## GetGlossary action (Python: get\_glossary)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetGlossary"></a>

Retrieves a business glossary in AWS Glue Data Catalog by its identifier.

**Example**  
The following example retrieves a glossary by its identifier.  

```
aws glue get-glossary --identifier 6n5f21s641nbjb
    
    {
        "Id": "6n5f21s641nbjb",
        "Name": "Sales Terms",
        "Description": "Glossary of sales-domain business terms"
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary to retrieve.

**Response**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary.
+ `Description` – UTF-8 string, not less than 1 or more than 2048 bytes long.

  The description of the glossary.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `ThrottlingException`

## UpdateGlossary action (Python: update\_glossary)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-UpdateGlossary"></a>

Updates a business glossary in AWS Glue Data Catalog.

**Example**  
The following example updates a glossary's description.  

```
aws glue update-glossary \
        --identifier 6n5f21s641nbjb \
        --name "Sales Terms" \
        --description "Glossary of sales and revenue business terms"
    
    {
        "Id": "6n5f21s641nbjb",
        "Name": "Sales Terms",
        "Description": "Glossary of sales and revenue business terms"
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary to update.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The updated name of the glossary.
+ `Description` – UTF-8 string, not less than 1 or more than 2048 bytes long.

  The updated description of the glossary.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary.
+ `Description` – UTF-8 string, not less than 1 or more than 2048 bytes long.

  The description of the glossary.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`
+ `AlreadyExistsException`

## DeleteGlossary action (Python: delete\_glossary)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DeleteGlossary"></a>

Deletes a business glossary from AWS Glue Data Catalog. A glossary cannot be deleted if it still contains glossary terms.

**Example**  
The following example deletes a glossary by its identifier.  

```
aws glue delete-glossary --identifier 6n5f21s641nbjb
```

**Request**
+ `Identifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary to delete.

**Response**
+ *No Response parameters.*

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConflictException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## ListGlossaries action (Python: list\_glossaries)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ListGlossaries"></a>

Lists business glossaries in AWS Glue Data Catalog.

**Example**  
The following example lists the glossaries in the account.  

```
aws glue list-glossaries --max-results 20
    
    {
        "Items": [
            {
                "Id": "6n5f21s641nbjb",
                "Name": "Sales Terms",
                "Description": "Glossary of sales and revenue business terms"
            }
        ]
    }
```

**Request**
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of results to return in the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.

**Response**
+ `Items` – An array of [GlossaryItem](#aws-glue-api-catalog-aws-glue-api-semantics-GlossaryItem) objects.

  The list of glossary items.
+ `NextToken` – UTF-8 string.

  A continuation token, present if the current segment is not the last.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## CreateGlossaryTerm action (Python: create\_glossary\_term)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-CreateGlossaryTerm"></a>

Creates a glossary term within a business glossary in AWS Glue Data Catalog.

**Example**  
The following example creates a glossary term.  

```
aws glue create-glossary-term \
        --glossary-identifier 6n5f21s641nbjb \
        --name "Net Revenue" \
        --short-description "Revenue after returns, allowances, and discounts." \
        --long-description "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
    
    {
        "Id": "avugvxvsul6izr",
        "GlossaryId": "6n5f21s641nbjb",
        "Name": "Net Revenue",
        "ShortDescription": "Revenue after returns, allowances, and discounts.",
        "LongDescription": "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
    }
```

**Request**
+ `GlossaryIdentifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary in which to create the term.
+ `Name` – *Required:* UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary term.
+ `ShortDescription` – UTF-8 string, not less than 1 or more than 1024 bytes long.

  A short description of the glossary term.
+ `LongDescription` – UTF-8 string, not less than 1 or more than 4096 bytes long.

  A long description of the glossary term.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary term.
+ `GlossaryId` – UTF-8 string.

  The unique identifier of the glossary containing this term.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary term.
+ `ShortDescription` – UTF-8 string, not less than 1 or more than 1024 bytes long.

  The short description of the glossary term.
+ `LongDescription` – UTF-8 string, not less than 1 or more than 4096 bytes long.

  The long description of the glossary term.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`
+ `AlreadyExistsException`

## GetGlossaryTerm action (Python: get\_glossary\_term)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetGlossaryTerm"></a>

Retrieves a glossary term in AWS Glue Data Catalog by its identifier.

**Example**  
The following example retrieves a glossary term by its identifier.  

```
aws glue get-glossary-term --identifier avugvxvsul6izr
    
    {
        "Id": "avugvxvsul6izr",
        "GlossaryId": "6n5f21s641nbjb",
        "Name": "Net Revenue",
        "ShortDescription": "Revenue after returns, allowances, and discounts.",
        "LongDescription": "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary term to retrieve.

**Response**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary term.
+ `GlossaryId` – UTF-8 string.

  The unique identifier of the glossary containing this term.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary term.
+ `ShortDescription` – UTF-8 string, not less than 1 or more than 1024 bytes long.

  The short description of the glossary term.
+ `LongDescription` – UTF-8 string, not less than 1 or more than 4096 bytes long.

  The long description of the glossary term.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `ThrottlingException`

## UpdateGlossaryTerm action (Python: update\_glossary\_term)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-UpdateGlossaryTerm"></a>

Updates a glossary term in AWS Glue Data Catalog.

**Example**  
The following example updates a glossary term's short description.  

```
aws glue update-glossary-term \
        --identifier avugvxvsul6izr \
        --name "Net Revenue" \
        --short-description "Gross revenue minus returns, allowances, and discounts." \
        --long-description "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
    
    {
        "Id": "avugvxvsul6izr",
        "GlossaryId": "6n5f21s641nbjb",
        "Name": "Net Revenue",
        "ShortDescription": "Gross revenue minus returns, allowances, and discounts.",
        "LongDescription": "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
    }
```

**Request**
+ `Identifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary term to update.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The updated name of the glossary term.
+ `ShortDescription` – UTF-8 string, not less than 1 or more than 1024 bytes long.

  The updated short description of the glossary term.
+ `LongDescription` – UTF-8 string, not less than 1 or more than 4096 bytes long.

  The updated long description of the glossary term.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `Id` – UTF-8 string.

  The unique identifier of the glossary term.
+ `GlossaryId` – UTF-8 string.

  The unique identifier of the glossary containing this term.
+ `Name` – UTF-8 string, not less than 1 or more than 256 bytes long.

  The name of the glossary term.
+ `ShortDescription` – UTF-8 string, not less than 1 or more than 1024 bytes long.

  The short description of the glossary term.
+ `LongDescription` – UTF-8 string, not less than 1 or more than 4096 bytes long.

  The long description of the glossary term.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`
+ `AlreadyExistsException`

## DeleteGlossaryTerm action (Python: delete\_glossary\_term)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DeleteGlossaryTerm"></a>

Deletes a glossary term from AWS Glue Data Catalog.

**Example**  
The following example deletes a glossary term by its identifier.  

```
aws glue delete-glossary-term --identifier avugvxvsul6izr
```

**Request**
+ `Identifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary term to delete.

**Response**
+ *No Response parameters.*

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## ListGlossaryTerms action (Python: list\_glossary\_terms)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-ListGlossaryTerms"></a>

Lists glossary terms within a business glossary in AWS Glue Data Catalog.

**Example**  
The following example lists the terms in a glossary.  

```
aws glue list-glossary-terms \
        --glossary-identifier 6n5f21s641nbjb \
        --max-results 20
    
    {
        "Items": [
            {
                "Id": "avugvxvsul6izr",
                "Name": "Net Revenue",
                "ShortDescription": "Gross revenue minus returns, allowances, and discounts."
            }
        ]
    }
```

**Request**
+ `GlossaryIdentifier` – *Required:* UTF-8 string.

  The unique identifier of the glossary whose terms to list.
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of results to return in the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.

**Response**
+ `GlossaryId` – UTF-8 string.

  The unique identifier of the glossary.
+ `Items` – An array of [GlossaryTermItem](#aws-glue-api-catalog-aws-glue-api-semantics-GlossaryTermItem) objects.

  The list of glossary term items.
+ `NextToken` – UTF-8 string.

  A continuation token, present if the current segment is not the last.

**Errors**
+ `AccessDeniedException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ThrottlingException`

## AssociateGlossaryTerms action (Python: associate\_glossary\_terms)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-AssociateGlossaryTerms"></a>

Associates one or more glossary terms with an asset in AWS Glue Data Catalog.

**Example**  
The following example associates a glossary term with an asset.  

```
aws glue associate-glossary-terms \
        --asset-identifier quarterly-sales-2026q1 \
        --glossary-term-identifiers avugvxvsul6izr
    
    {
        "AssetIdentifier": "quarterly-sales-2026q1",
        "GlossaryTerms": [
            "avugvxvsul6izr"
        ]
    }
```

**Request**
+ `AssetIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset to associate glossary terms with.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form. When specified along with `itemIdentifier`, the glossary terms are associated with an item within the iterable form rather than the asset itself.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
+ `GlossaryTermIdentifiers` – *Required:* An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The list of glossary term identifiers to associate with the asset.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `AssetIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form, if the association targets an item.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form, if applicable.
+ `GlossaryTerms` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The glossary terms now associated with the asset.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## DisassociateGlossaryTerms action (Python: disassociate\_glossary\_terms)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-DisassociateGlossaryTerms"></a>

Removes the association of one or more glossary terms from an asset in AWS Glue Data Catalog.

**Example**  
The following example removes a glossary term from an asset.  

```
aws glue disassociate-glossary-terms \
        --asset-identifier quarterly-sales-2026q1 \
        --glossary-term-identifiers avugvxvsul6izr
    
    {
        "AssetIdentifier": "quarterly-sales-2026q1",
        "GlossaryTerms": []
    }
```

**Request**
+ `AssetIdentifier` – *Required:* UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset to disassociate glossary terms from.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form. When specified along with `itemIdentifier`, the glossary terms are disassociated from an item within the iterable form rather than the asset itself.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
+ `GlossaryTermIdentifiers` – *Required:* An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The list of glossary term identifiers to disassociate from the asset.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**
+ `AssetIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long, matching the [Custom string pattern #69](aws-glue-api-common.md#regex_69).

  The unique identifier of the asset.
+ `IterableFormName` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #73](aws-glue-api-common.md#regex_73).

  The name of the iterable form, if the disassociation targets an item.
+ `ItemIdentifier` – UTF-8 string, not less than 1 or more than 1087 bytes long.

  The identifier of the item within the iterable form, if applicable.
+ `GlossaryTerms` – An array of UTF-8 strings, not less than 1 or more than 10 strings.

  The remaining glossary terms associated with the asset.

**Errors**
+ `AccessDeniedException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `InvalidInputException`
+ `ConcurrentModificationException`
+ `ThrottlingException`

## SearchAssets action (Python: search\_assets)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-SearchAssets"></a>

Searches for assets in AWS Glue Data Catalog using full-text search, filters, sorting, and aggregations. Returns matching assets with relevance-ranked results.

**Example**  
The following example runs a full-text search for assets.  

```
aws glue search-assets --search-text "sales" --max-results 10
    
    {
        "Items": [
            {
                "Id": "quarterly-sales-2026q1",
                "AssetName": "Quarterly Sales 2026 Q1",
                "AssetDescription": "Aggregated quarterly sales metrics",
                "UpdatedAt": "2026-06-16T06:42:00.442Z",
                "AssetTypeId": "DataSet"
            }
        ]
    }
```

**Example**  
The following example searches with a filter clause and sort order.  

```
aws glue search-assets \
        --search-text "sales" \
        --max-results 10 \
        --filter-clause '{"AttributeFilter":{"Attribute":"AssetTypeId","Operator":"equals","Value":{"StringValue":"DataSet"}}}' \
        --sort '{"Attribute":"name","Order":"ASCENDING"}'
    
    {
        "Items": [
            {
                "Id": "quarterly-sales-2026q1",
                "AssetName": "Quarterly Sales 2026 Q1",
                "AssetDescription": "Aggregated quarterly sales metrics",
                "UpdatedAt": "2026-06-16T06:42:00.442Z",
                "AssetTypeId": "DataSet"
            }
        ]
    }
```

**Request**
+ `SearchText` – UTF-8 string, not less than 1 or more than 1000 bytes long.

  The text to search for. At least one of `searchText` or `filterClause` must be provided.
+ `MaxResults` – Number (integer), not less than 1 or more than 100.

  The maximum number of results to return in the response.
+ `NextToken` – UTF-8 string.

  A continuation token, if this is a continuation call.
+ `Sort` – A [SearchSort](#aws-glue-api-catalog-aws-glue-api-semantics-SearchSort) object.

  The sort criteria for the search results.
+ `FilterClause` – A [SearchFilterClause](#aws-glue-api-catalog-aws-glue-api-semantics-SearchFilterClause) object.

  The filter clause to apply to the search. Supports nested AND/OR logic with attribute-level and map-level filters.

**Response**

The search results returned by the `SearchAssets` operation.
+ `SearchAssetsOutput` – A [SearchAssetsOutput](#aws-glue-api-catalog-aws-glue-api-semantics-SearchAssetsOutput) object.

**Errors**
+ `AccessDeniedException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `ThrottlingException`

## GetDataCatalogExportConfiguration action (Python: get\_data\_catalog\_export\_configuration)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-GetDataCatalogExportConfiguration"></a>

Retrieves the current export configuration for the AWS Glue Data Catalog. The export configuration controls whether catalog metadata is exported to S3 Tables.

**Request**
+ *No Request parameters.*

**Response**

The export configuration returned by the `GetDataCatalogExportConfiguration` operation.
+ `GetDataCatalogExportConfigurationOutput` – A [GetDataCatalogExportConfigurationOutput](#aws-glue-api-catalog-aws-glue-api-semantics-GetDataCatalogExportConfigurationOutput) object.

**Errors**
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `ThrottlingException`

## PutDataCatalogExportConfiguration action (Python: put\_data\_catalog\_export\_configuration)
<a name="aws-glue-api-catalog-aws-glue-api-semantics-PutDataCatalogExportConfiguration"></a>

Creates or updates the export configuration for the AWS Glue Data Catalog. Use this operation to enable or disable the export of catalog metadata to S3 Tables.

**Request**
+ `ExportSetting` – *Required:* UTF-8 string (valid values: `ENABLED` \| `DISABLED`).

  The export setting for the data catalog. Specify `ENABLED` to start exporting catalog metadata to S3 Tables, or `DISABLED` to stop exporting. This field is required.
+ `EncryptionConfiguration` – An [ExportEncryptionConfiguration](#aws-glue-api-catalog-aws-glue-api-semantics-ExportEncryptionConfiguration) object.

  The encryption configuration for the exported data. If not specified, the default encryption settings are used.
+ `ClientToken` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

**Response**

The export configuration returned by the `PutDataCatalogExportConfiguration` operation.
+ `PutDataCatalogExportConfigurationOutput` – A [PutDataCatalogExportConfigurationOutput](#aws-glue-api-catalog-aws-glue-api-semantics-PutDataCatalogExportConfigurationOutput) object.

**Errors**
+ `InvalidInputException`
+ `AccessDeniedException`
+ `InternalServiceException`
+ `ThrottlingException`
+ `ConflictException`