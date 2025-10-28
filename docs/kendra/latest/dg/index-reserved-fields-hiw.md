# Using Amazon Kendra reserved or

common document fields

With the
[UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md") API operation, you can create reserved or common fields.
To
do this, you use
`DocumentMetadataConfigurationUpdates`, and specify the Amazon Kendra reserved index field name to map to your equivalent document
attribute/field name. You can also create custom fields.

If you use a data source connector, most include field mappings that map your data
source document fields to Amazon Kendra index fields. If you use the console,
you update fields by selecting your data source, selecting the edit action, and then
proceeding next to the field mappings section for configuring the data
source.

You can configure the `Search` object to set a field as either
displayable, facetable, searchable, and sortable. You can configure the
`Relevance` object to set a field's rank order, boost duration or
time period to apply to boosting, freshness, importance value, and importance values
mapped to specific field values.

If you use the console, you can configure the search settings for a field by
selecting the facet option in the navigation menu. To set relevance tuning, select
the option to search your index in the navigation menu, enter a query, and use the
side panel options to tune the search relevance. You can't change the field type
after
you
have created the field.

Amazon Kendra has the following reserved or common
document fields that you can use:

- `_authors` –
  A
  list of one or more authors responsible for the content of the
  document.
- `_category` – A category that places a document in a
  specific group.
- `_created_at` – The date and time in ISO 8601 format
  that the document was created. For example, 2012-03-25T12:30:10+01:00 is the
  ISO 8601 date-time format for March 25th, 2012 at 12:30 PM (plus 10 seconds)
  in Central European Time.
- `_data_source_id` – The identifier of the data source
  that contains the document.
- `_document_body` – The content of the document.
- `_document_id` – A unique identifier for the
  document.
- `_document_title` – The title of the document.
- `_excerpt_page_number` – The page number in a PDF file
  where the document excerpt appears. If your index was created before
  September 8, 2020, you must re-index your documents before you can use this
  attribute.
- `_faq_id` – If this is a question-answer type document
  (FAQ), a unique identifier for the FAQ.
- `_file_type` – The file type of the document, such as
  pdf or doc.
- `_last_updated_at` – The date and time in ISO 8601
  format that the document was last updated. For example,
  2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th,
  2012 at 12:30 PM (plus 10 seconds) in Central European Time.
- `_source_uri` – The URI where the document is
  available—for example, the URI of the document on a company
  website.
- `_version` – An identifier for the specific version of a
  document.
- `_view_count` – The number of times that the document
  has been viewed.
- `_language_code` (String) – The code for a language that
  applies to the document. This defaults to English if you don't specify a
  language. For more information on supported languages, including their
  codes, see [Adding documents in
  languages other than English](in-adding-languages.md "in-adding-languages.md").
  You create custom fields using `DocumentMetadataConfigurationUpdates`
  with the `UpdateIndex` API operation, just as you do when creating a
  reserved or common field. You must set the appropriate data type for your custom
  field.

If you use the console, you update fields by selecting your data source, selecting
the edit action, and then proceeding next to the field mappings section for
configuring the data source. Some data sources don't support adding new fields or
custom fields. You can't change the field type after you have created the
field.

The following are the types that you can set for custom fields:

- Date
- Number
- String
- String list
  If you added documents to an index using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API operation, `Attributes` lists the
  fields/attributes of your documents and you create fields using the
  `DocumentAttribute` object.

For documents indexed from an Amazon S3 data source, you create fields
using a [JSON
metadata file](s3-metadata.md "s3-metadata.md") that includes the fields information.

If you use a supported database as your data source, you can configure your fields
using the [field mappings option](data-source-database.md#data-source-procedure-database "data-source-database.md#data-source-procedure-database").
