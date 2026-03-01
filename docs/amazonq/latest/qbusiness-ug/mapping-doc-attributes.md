# Configuring metadata controls in Amazon Q Business

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

###### Important

This section assumes that you understand [document attributes](doc-attributes.md "doc-attributes.md") in Amazon Q Business.

###### Note

Before you configure relevance tuning, you must [create a Amazon Q Business retriever and index](select-retriever.md "select-retriever.md") for your
application.

An Amazon Q Business index has fields you can map your document attributes to.
Once mapped to document attributes and search enabled, these index fields can be used by
admin to boost results from specific sources, or by end users to filter and scope their
chat results to specific data.

Mapping document attributes from your documents to index fields is a multi-step
process that depends on the document upload method you use.

###### Note

You can filter using document attributes in chat only through the API.
You can boost search results using document attributes on both the console
and the API.

###### Topics

- [Mapping document attributes directly to index fields](#mapping-doc-attributes-directly "#mapping-doc-attributes-directly")
- [Mapping data source document attributes to index fields](#mapping-data-source-doc-attributes "#mapping-data-source-doc-attributes")
- [Ingesting attributes using the BatchPutDocument API operation](#custom-attributes-batch "#custom-attributes-batch")
- [Using aggregations and dynamic filtering in chat](#using-aggregations-in-chat "#using-aggregations-in-chat")

## Mapping document attributes directly to index fields

When you use the console or the API to directly add documents to your application,
you must first create and map your document attributes to index fields before you
can use them for filtering in chat or boosting responses. You use the following
processes to map document attributes to your index field and mark them
searchable.

###### Important

You can map up to 50 document attributes to index fields. You can mark up to
30 index fields searchable.

###### Topics

- [Using the console](#mapping-doc-attributes-directly-console "#mapping-doc-attributes-directly-console")
- [Using the API](#mapping-doc-attributes-directly-api "#mapping-doc-attributes-directly-api")

### Using the console

To map document attributes to index fields using the Amazon Q Business
console, complete the following steps:

**To create and map document attributes to index
fields**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation pane, from **Enhancements**,
   choose **Metadata controls**.
3. From **Metadata**, choose **Add metadata
   field**.
4. From the **Add metadata field** dialog box that opens
   up, do the following:
   1. For **Metadata field name** – Add a
      name for the metadata field you're adding to the index.
   2. For **Data type** – Select the data
      type you want to assign to the metadata field. Supported data
      types include **String**, **String
      list**, **Long (numeric)**, and
      **Date**.
   3. For **Usage type** – Select
      **Searchable** to mark your field
      searchable to end users.
   4. Select **Add** to finish adding the metadata
      field to your index.Repeat the previous step to add create and map more metadata fields.
      Once you add a metadata field, you can't delete it.

5. To save all the metadata fields you added, select
   **Save**.

###### Note

If you leave the page without saving your changes, any metadata
fields you added won't be saved.

Any metadata you add and mark searchable can be viewed from the
**Metadata** summary. You can update the searchability of a
metadata field at any time.

### Using the API

To map document attributes to index fields using the Amazon Q Business
API, complete the following steps:

1. You create an index by calling the [CreateIndex](../api-reference/API_CreateIndex.md "../api-reference/API_CreateIndex.md") API
   operation.
2. Then, you create index fields using the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") operation.
   You use this method to map both reserved and custom document attributes
   to index fields.
3. Optionally, you can test and view the index fields that you’ve added
   by using the [GetIndex](../api-reference/API_GetIndex.md "../api-reference/API_GetIndex.md")
   operation.
4. Then, when you use the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md")
   operation to ingest documents into your index, Amazon Q Business
   extracts your reserved or custom document attributes and maps them to
   the index fields that you have already created.
5. To mark mapped attributes searchable, follow the steps outlined in
   [enabling attributes for search using
   APIs](boosting-searchable-attributes.md#enable-attribute-search-api "boosting-searchable-attributes.md#enable-attribute-search-api").

After you map document attributes directly to index fields using the API, you
can select specific attributes for your end user to use for filtering chat
responses. With the `UpdateIndex` API operation, you add custom
fields or attributes using the `documentAttributeConfigurations`
parameter.

The following JSON example uses `documentAttributeConfigurations`
to add a field called "Department" to the index.

```
"DocumentmetadataConfigurationUpdates": [
   {
       "Name": "Department",
       "Type": "STRING_VALUE"
   }
]
```

## Mapping data source document attributes to index fields

If you use an Amazon Q Business data source connector, you can map default
document attributes attached to documents in your data source to fields in your
Amazon Q Business index during data source configuration. You can use
these document attributes to help your end user filter and scope chat
responses.

###### Important

Filtering using data source document attributes in chat is only supported
through the API.

Each data source connector is designed to automatically crawl and map specific
document attributes as default from your data source. For example, if you have a
field in your data source named `dept` that contains department
information for a document, your data source may automatically map it to an index
field named `Department`. You can't change or customize default data
source attributes that are mapped to an index.

If you use the console, you select and map default field mappings or create and
map custom mappings when you configure your connector. On the console, if a default
field or a default field property can’t be edited, it will appear grayed out. If you
use the API, you use the `configuration` parameter of the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation to
map default document attributes in your data source to index fields.

You can also map any custom document attributes in your data source connector to
Amazon Q Business reserved fields. For example, if your data source has a
custom attribute named `creation_date`, you can map this field to the
equivalent Amazon Q reserved field named `_created_at`. You
can also choose to add custom document attributes and map them to custom fields that
you create in your index. You do this when you configure and update your data
source, using both the console and the API.

If you want to map custom document attributes in your data source to Amazon Q index fields, use the `DocumentAttribute` parameter of
the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") operation to first
create the custom field matching the custom document attribute. By doing so, you can
specify and map your reserved or custom data source document attribute to a reserved
or custom index field.

Any metadata you add can be viewed and marked searchable using **Metadata
controls** or using the API. You can update the searchability of a
metadata field at any time.

###### Note

Document attributes mapped to index fields during the data source
configuration process must be [enabled for search](boosting-searchable-attributes.md "boosting-searchable-attributes.md") before they can be used for
search accuracy improvements, filtering search results, and metadata
boosting.

Most data sources support custom field mappings and follow a specific
configuration format, except Amazon S3 and database data sources. The
following outlines how Amazon S3 and database data sources configure mappings:

- If you store your documents in an Amazon S3 bucket or Amazon S3 data source, you can either use the console to specify field
  mappings or specify fields [using a JSON metadata file](s3-metadata.md "s3-metadata.md").

When you use an Amazon S3 bucket as a data source for your index,
you use companion metadata files to add metadata to the documents. You place
the metadata JSON files in a directory structure that is parallel to your
documents. For more information, see [S3 document
metadata](s3-metadata.md "s3-metadata.md").

You specify custom fields or attributes in the `Attributes`
JSON structure. You can create up to 50 custom fields or attributes. The
following example uses `Attributes` to define three custom fields
or attributes and one reserved field.

```
"Attributes": {
        "brand": "Amazon Basics",
        "price": 1595,
        "_category": "sports",
        "subcategories": ["outdoors", "electronics"]
    }
```

- For database data sources, if the name of the database column matches the
  name of a reserved field, the field and column are mapped
  automatically.

## Ingesting attributes using the BatchPutDocument API operation

When you use the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation to add a document to
your index, you can specify document attributes—both reserved and
custom—as part of `Attributes`. You can add multiple fields or
attributes when you call the API operation. You can create up to 50 custom fields or
attributes. The following example is a custom field or attribute that adds
"Department" to a document.

```
"Attributes":
    {
        "Department": "HR",
        "_category": "Vacation policy"
    }
```

## Using aggregations and dynamic filtering in chat

###### Note

Using aggregations and dynamic filtering in chat is only supported in [**Advanced search**](agentic-rag.md "agentic-rag.md").

###### Warning

To ensure optimal performance and accuracy, perform a `FORCED_FULL_CRAWL` on your data source first before using
the features.

### Supported aggregations

The Amazon Q API supports the following aggregations:

1. `SUM`: Logic to perform a summation upon any numeric data
   field. For example, "What is the total sum of tickets in status Open?"
2. `AVERAGE`: Logic to perform an average upon any numeric data
   field. For example, "What is my average watcher amount for the last
   week?"
3. `COUNT`: Logic to perform a distinct count of unique values
   across any type of data field. For example, "Give me the count of unique
   customer names in the sales database."
4. `LIST_ALL`: Logic to gather a subset of available values for
   any field. For example, "List all reports on Sunday Sales ticket
   repository."

Using the mathematical aggregations, users can quickly gather statistical and
analytical queries on any data in their data source.

### Filtering and Sorting

Amazon Q also offers the ability to intelligently ascertain user intent and
apply filtering or sorting across any number of fields. For example, users can
query against specific time ranges, values, or string matches by text alone.
Sorting can also be inferred through text, for example, "Show me the top 5
accounts sorted by sales data from the last month."
