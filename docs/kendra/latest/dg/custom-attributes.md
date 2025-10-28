# Creating custom document fields

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Searching indexes](hiw-index.md#index-searching "hiw-index.md#index-searching").

You can create custom attributes or fields for your documents in your Amazon Kendra index. For
example, you can create a custom field or attribute called "Department" with the values
of "HR", "Sales", and "Manufacturing". If you map these custom fields or attributes to
your Amazon Kendra index, you can use them to filter the search results to include documents by
the "HR" department attribute, for example.

Before you can use a custom field or attribute, you must first create the field in the
index. Use the console to edit the data source field mappings to add a custom field or
use the [UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md") API to
create the index field. You cannot change the field data type once you have created the
field.

For most data sources, you map fields in the external data source to the corresponding
fields in Amazon Kendra. For more information, see [Mapping data source fields](field-mapping.md "field-mapping.md"). For S3
data sources, you can create custom fields or attributes using a JSON metadata
file.

You can create up to 500 custom fields or attributes.

You can also use Amazon Kendra reserved or common fields. For more information,
see [Document attributes or fields](hiw-document-attributes.md "hiw-document-attributes.md").

###### Topics

- [Updating custom document fields](#update-attributes "#update-attributes")

## Updating custom document fields

With the `UpdateIndex` API, you add custom fields or attributes using
the `DocumentMetadataConfigurationUpdates` parameter.

The following JSON example uses `DocumentMetadataConfigurationUpdates`
to add a field called "Department" to the index.

```
"DocumentmetadataConfigurationUpdates": [
   {
       "Name": "Department",
       "Type": "STRING_VALUE"
   }
]
```

The following sections include examples for adding custom attributes or fields
using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") and for an Amazon S3 data source.

###### Topics

- [Adding custom attributes or fields
  with the BatchPutDocument API](#custom-attributes-batch "#custom-attributes-batch")
- [Adding custom attributes or fields to an
  Amazon S3 data source](#custom-attributes-s3 "#custom-attributes-s3")

### Adding custom attributes or fields

with the BatchPutDocument API

When you use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API to add a document to your index, you specify
custom fields or attributes as part of `Attributes`. You can add
multiple fields or attributes when you call the API. You can create up to 500
custom fields or attributes. The following example is a custom field or
attribute that adds "Department" to a document.

```
"Attributes":
    {
        "Department": "HR",
        "_category": "Vacation policy"
    }
```

### Adding custom attributes or fields to an

Amazon S3 data source

When you use an S3 bucket as a data source for your index, you add metadata to
the documents with companion metadata files. You place the metadata JSON files
in a directory structure that is parallel to your documents. For more
information, see [S3 document metadata](s3-metadata.md "s3-metadata.md").

You specify custom fields or attributes in the `Attributes` JSON
structure. You can create up to 500 custom fields or attributes. For example,
the following example uses `Attributes` to define three custom fields
or attributes and one reserved field.

```
"Attributes": {
        "brand": "Amazon Basics",
        "price": 1595,
        "_category": "sports",
        "subcategories": ["outdoors", "electronics"]
    }
```

The following steps walk you through adding custom attributes to an Amazon S3 data
source.

###### Topics

- [Step 1: Create a Amazon Kendra
  index](#custom-attributes-s3-1 "#custom-attributes-s3-1")
- [Step 2: Update index to add custom
  document fields](#custom-attributes-s3-2 "#custom-attributes-s3-2")
- [Step 3: Create an Amazon S3 data source
  and map data source fields to custom attributes](#custom-attributes-s3-3 "#custom-attributes-s3-3")

#### Step 1: Create a Amazon Kendra

index

Follow the steps in [Creating an index](create-index.md "create-index.md") to create your Amazon Kendra index.

#### Step 2: Update index to add custom

document fields

After creating an index, you add fields to it. The following procedure
shows how to add fields to an index using the console and the CLI.

Console

###### To create index fields

1.  Make sure you've [created an
    index](create-index.md "create-index.md").
2.  Then, from the left navigation menu, from
    **Data management**, choose
    **Facet definition**.
3.  In **Index field settings guide**,
    from **Index fields**, choose
    **Add field** to add custom
    fields.
4.  In the **Add index field** dialog
    box, do the following:

        * **Field name** – Add a
         field name.
        * **Data type** – Select
         data type, whether **String**,
         **String list**, or
         **Date**.
        * **Usage types** –
         Select usage types, whether
         **Facetable**,
         **Searchable**,
         **Displayable**, and
         **Sortable**.


        Then, select **Add**.

    Repeat the last step for any other fields you want to
    map.

CLI

```
aws kendra `update-index`  \
--region `$region` \
--endpoint-url `$endpoint` \
--application-id `$applicationId` \
--index-id `$indexId`  \
--document-metadata-configuration-updates \
"[
    {
        "Name": "`string`",
        "Type": "`STRING_VALUE`"|"`STRING_LIST_VALUE`"|"`LONG_VALUE`"|"DATE_VALUE",
        "Relevance": {
            "Freshness": `true`|`false`,
            "Importance": `integer`,
            "Duration": "`string`",
            "RankOrder": "`ASCENDING`"|"`DESCENDING`",
            "ValueImportanceMap": {"`string`": `integer`
            ...}
    },
    "Search": {
        "Facetable": `true`|`false`,
        "Searchable": `true`|`false`,
        "Displayable": `true`|`false`,
        "Sortable": `true`|`false`
        }
    }
...
]"
```

#### Step 3: Create an Amazon S3 data source

and map data source fields to custom attributes

To create an Amazon S3 data source and map fields to it, follow the
instructions in [Amazon S3](data-source-s3.md "data-source-s3.md").

If you're using the API, use the `fieldMappings` attribute
under `configuration` when you use the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API.

For an overview of how data source fields are mapped, see [Mapping data source fields](field-mapping.md "field-mapping.md").
