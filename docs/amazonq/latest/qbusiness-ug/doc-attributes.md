# Document attributes in Amazon Q Business

Every document has structural attributes—or metadata—attached to it.
Document attributes can include information such as document title, document author, time
created, time updated, and document type.

You can map document attributes to fields in your Amazon Q Business index. Once
mapped to document attributes, these index fields can be used by admin to boost results from
specific sources, or by end users to filter and scope their chat results to specific
data.

###### Note

Filtering using document attributes in chat is only supported through the API.
Boosting search results using document attributes is supported on both the console and
the API.

You can also use document attributes to prepare your data for—and customize and
control—end user chat. To learn more, see [Filtering
using metadata](metadata-filtering.md "metadata-filtering.md"), [Document enrichment in Amazon Q Business](custom-document-enrichment.md "custom-document-enrichment.md"), [Metadata controls](mapping-doc-attributes.md "mapping-doc-attributes.md"), and [Metadata
boosting](metadata-boosting.md "metadata-boosting.md").

###### Topics

- [Types of document attributes](#doc-attribute-types "#doc-attribute-types")
- [Mapped document attributes](#mapped-doc-attribute-types "#mapped-doc-attribute-types")
- [Document attribute data types](#doc-attribute-data-types "#doc-attribute-data-types")

## Types of document attributes

Amazon Q Business supports two types of document attributes: reserved or
default, and custom.

Reserved or default document attributes are provided by Amazon Q Business to map
commonly occurring document attributes to index fields. Custom attributes, on the other
hand, can be used to map document attributes unique to your content to index
fields.

Both reserved and custom document attributes can be used to customize end user chat
experience.

###### Important

You can create and map up to 50 document attributes to index fields. Once created,
you can't delete or rename any attributes.

The following section outlines the available document attributes.

###### Topics

- [Reserved document attributes](#reserved-doc-attributes "#reserved-doc-attributes")
- [Custom document attributes](#custom-doc-attributes "#custom-doc-attributes")

### Reserved document attributes

Amazon Q Business offers the following reserved document attributes or index
fields that you can map your metadata to:

- `_authors` – A list of one or more authors responsible
  for the content of the document.
- `_category` – A category that places a document in a
  specific group.
- `_created_at` – The date and time in ISO 8601 format
  that the document was created. For example, 2012-03-25T12:30:10+01:00 is the
  ISO 8601 date-time format for March 25, 2012 at 12:30 PM (plus 10 seconds)
  in Central European Time.
- `_data_source_id` – The identifier of the data source
  that contains the document.
- `_document_body` – The content of the document.
- `_document_id` – A unique identifier for the
  document.
- `_document_title` – The title of the document.
- `_file_type` – The file type of the document, such as
  .pdf or .docx.
- `_last_updated_at` – The date and time in ISO 8601
  format that the document was last updated. For example,
  2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25,
  2012 at 12:30 PM (plus 10 seconds) in Central European Time.
- `_source_uri` – The URI where the document is available.
  For example, the URI of the document on a company website.
- `_version` – An identifier for the specific version of a
  document.
- `_view_count` – The number of times that the document
  has been viewed.
- `_language_code (String)` – The code for a language that
  applies to the document. This defaults to English if you don't specify a
  language.
- `_data_source_type` – An **optional** type of data source that contains the document, specified as a text identifier (for example, "Amazon S3" or "WEBCRAWLERV2").

In addition to these default attributes, each Amazon Q Business data source
connector also automatically creates specific reserved or default attributes based
on commonly occurring metadata in the data source you're using. You can choose to
map these to Amazon Q Business index fields when you configure a data source.
You can't edit these default attributes.

### Custom document attributes

You can create custom attributes based on your own enterprise data. You can map
the custom attributes to index fields for a more tailored end user chat experience.
For example, you can create a custom attribute called "Department" with the values
of "HR", "Sales", and "Manufacturing" and map it an index field. Then, you can use
these fields or attributes to allow your end users to filter their chat results to
documents in the "HR" department, or restrict response generation to specific data
stores.

You can also create and map custom document attributes based on uniquely occurring
metadata in your data when you connect and configure a Amazon Q Business data
source connector. If a document attribute in your data source doesn't have a default
attribute mapping already available, or if you want to map additional document
attributes to index fields, you can use these custom field mappings to specify how a
data source attribute maps to an Amazon Q Business index field. You create and
map custom document attributes to index fields by editing your data source after
your application environment and retriever are created.

## Mapped document attributes

When a document attribute—reserved or custom—is mapped to an index
field, you can choose how the field will be used during chat. You can currently
configure index fields to perform the following action:

- **Searchable** – Allows end users the
  ability to search data with the specified attributes.

###### Important

You can mark up to 30 index fields searchable.

## Document attribute data types

Document attributes—reserved or custom—can only be the data types that
are shown in the following table. Additionally, document attributes can be used to
perform the operations outlined.

| Data type   | Searchable | Filterable | Boostable |
| ----------- | ---------- | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date        | Yes        | Yes        | Yes       |
| Number      | Yes        | Yes        | Yes       |
| String      | Yes        | Yes        | Yes       |
| String list | Yes        | Yes        | Yes       | ###### Note You can’t change an index field type after it has been created. For more information on filtering and boosting using document attributes, see [Filtering using document-attributes](metadata-filtering.md "metadata-filtering.md") and [Boosting using document attributes](metadata-boosting.md "metadata-boosting.md"). |
