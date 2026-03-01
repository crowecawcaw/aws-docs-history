# Enabling document attributes for search in Amazon Q Business

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

For `STRING` and `STRING_LIST` type attributes to be
eligible for boosting, they must first be enabled for search in your Amazon Q index.

The following sections outline how to do so using both the console and the
API.

###### Topics

- [Using the console](#enable-attribute-search-console "#enable-attribute-search-console")
- [Using the API](#enable-attribute-search-api "#enable-attribute-search-api")

## Using the console

To enable document attributes using the console, use the
**Metadata** functionality. The following procedure
outlines how.

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
      type you want to assign to the metadata field.
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

You can update the searchability of a metadata field at any time.

## Using the API

To enable these attributes for search using the API, use the [DocumentAttributeConfiguration](../api-reference/API_DocumentAttributeConfiguration.md "../api-reference/API_DocumentAttributeConfiguration.md")
object of the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API
operation.

The following sections provide AWS CLI examples of how to enable document
attributes for search.

###### Topics

- [Making reserved document attributes searchable](#enable-reserved-attribute-search "#enable-reserved-attribute-search")
- [Making custom document attributes searchable](#enable-custom-attribute-search "#enable-custom-attribute-search")
- [Checking document attribute search activation](#check-attribute-search "#check-attribute-search")

### Making reserved document attributes searchable

The following is an example of how to use the AWS CLI to enable for search
the `STRING` type reserved document attribute
`_category` and the `STRING_LIST` type reserved
document attribute `_authors` by using the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API operation.

```
aws qbusiness update-index \
--application-id `APPLICATION_ID` \
--index-id `INDEX_ID` \
--document-attribute-configurations '
          [
            {
              "name": "_category",
              "type": "STRING",
              "search": "ENABLED"
            },
            {
              "name": "_authors",
              "type": "STRING_LIST",
              "search": "ENABLED"
            }
          ]'
```

### Making custom document attributes searchable

You can also enable custom document attributes for search using the [DocumentAttributeConfiguration](../api-reference/API_DocumentAttributeConfiguration.md "../api-reference/API_DocumentAttributeConfiguration.md") object of the
[UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API
operation.

The following is an example of how to use the AWS CLI to enable for search
the custom `STRING` and `STRING_LIST` type document
attributes using the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API
operation.

```
aws qbusiness update-index \
--application-id `APPLICATION_ID` \
--index-id `INDEX_ID` \
--document-attribute-configurations '
          [
            {
              "name": "`custom_string`",
              "type": "STRING",
              "search": "ENABLED"
            },
            {
              "name": "`custom_string_list`",
              "type": "STRING_LIST",
              "search": "ENABLED"
            }
            ]'
```

### Checking document attribute search activation

To check if a `STRING` or `STRING_LIST` type
document attribute has been enabled for search successfully, use the [GetIndex](../api-reference/API_GetIndex.md "../api-reference/API_GetIndex.md") API
operation.

```

aws qbusiness get-index \
--application-id `APPLICATION_ID` \
--index-id `INDEX_ID`
```

The AWS CLI returns the following type of response:

```
{
...
    "documentAttributeConfigurations": [
        {
            "name": "_authors",
            "search": "ENABLED",
            "type": "STRING_LIST"
        },
        {
            "name": "_category",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_created_at",
            "search": "DISABLED",
            "type": "DATE"
        },
        {
            "name": "_data_source_id",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_document_title",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_file_type",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_language_code",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_last_updated_at",
            "search": "DISABLED",
            "type": "DATE"
        },
        {
            "name": "_source_uri",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_version",
            "search": "ENABLED",
            "type": "STRING"
        },
        {
            "name": "_view_count",
            "search": "DISABLED",
            "type": "NUMBER"
        }
    ],
...
}
```
