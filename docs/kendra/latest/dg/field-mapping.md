# Mapping data source fields

Amazon Kendra data source connectors can map document or content fields from your
data source to fields in your Amazon Kendra index. By default, each connector is
designed to crawl specific data source fields. Default data source fields and their
properties cannot be changed or customized. On the Amazon Kendra console, default
fields and default field properties that cannnot be edited are grayed out.

Amazon Kendra connectors also allow you to map custom document or content fields
from your data source to custom fields in your index. For example, if you have a field
in your data source called "dept" that contains department information for a document,
you can map it to an index field called "Department". That way, you can use the field
when querying documents.

You can also map Amazon Kendra reserved or common fields such as
`_created_at`. If your data source has a field called "creation_date",
you can map this to the equivalent Amazon Kendra reserved field called
`_created_at`. For more information on Amazon Kendra reserved
fields, see [Document attributes or
fields](hiw-document-attributes.md "hiw-document-attributes.md").

You can map fields for most data sources. You can create field mappings for the
following data sources:

- Adobe Experience Manager
- Alfresco
- Aurora (MySQL)
- Aurora (PostgreSQL)
- Amazon FSx (Windows)
- Amazon FSx (NetApp ONTAP)
- Amazon RDS/Aurora
- Amazon RDS (Microsoft SQL Server)
- Amazon RDS (MySQL)
- Amazon RDS (Oracle)
- Amazon RDS (PostgreSQL)
- Amazon Kendra Web Crawler
- WorkDocs
- Box
- Confluence
- Dropbox
- Drupal
- GitHub
- Google Workspace Drives
- Gmail
- IBM DB2
- Jira
- Microsoft Exchange
- Microsoft OneDrive
- Microsoft SharePoint
- Microsoft Teams
- Microsoft SQL Server
- Microsoft Yammer
- MySQL
- Oracle Database
- PostgreSQL
- Quip
- Salesforce
- ServiceNow
- Slack
- Zendesk
  If you store your documents in an S3 bucket, or S3 data source, you specify your
  fields using a JSON metadata file. For more information, see [S3 data source connector](data-source-s3.md "data-source-s3.md").

Mapping your data source fields to an index field is a three-step process:

1. Create an index. For more information, see [Creating an index](create-index.md "create-index.md").
2. Update the index to add fields.
3. Create a data source and include field mappings to map reserved fields and any
   custom fields to Amazon Kendra index fields.
   To update the index to add custom fields, use the console to edit the data source
   field mappings and add a custom field or use the [UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md") API. You
   can add a total of 500 custom fields to your index.

For database data sources, if the name of the database column matches the name of a
reserved field, the field and column are automatically mapped.

With the [UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md") API, you
add reserved and custom fields using
`DocumentMetadataConfigurationUpdates`.

The following JSON example uses `DocumentMetadataConfigurationUpdates` to
add a field called "Department" to the index.

```
"DocumentmetadataConfigurationUpdates": [
   {
       "Name": "Department",
       "Type": "STRING_VALUE"
   }
]

```

When you create the field, you have the option of setting how the field is used for
search. You can choose from the following:

- **Displayable**—Determines whether the
  field is returned in the query response. The default is
  `true`.
- **Facetable**—Indicates that the field can
  be used to create facets. The default is `false`.
- **Searchable**—Determines whether the
  field is used in the search. The default is `true` for string fields
  and `false` for number and date fields.
- **Sortable**—Indicates that the field can
  be used to sort the response from a query. Can only be set for date, number, and
  string fields. Can't be set for string list fields.
  The following JSON example uses `DocumentMetadataConfigurationUpdates` to
  add a field called "Department" to the index and marks it as facetable.

```
"DocumentMetadataConfigurationUpdates": [
   {
       "Name": "Department",
       "Type": "STRING_VALUE",
       "Search": {
           "Facetable": true
       }
   }
]

```

## Using Amazon Kendra reserved or common document

fields

With the [UpdateIndex API](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md"), you can create reserved or common fields using
`DocumentMetadataConfigurationUpdates` and specifying the Amazon Kendra
reserved index field name to map to your equivalent document attribute/field name. You can
also create custom fields. If you use a data source connector, most include field mappings
that map your data source document fields to Amazon Kendra index fields. If you use the
console, you update fields by selecting your data source, selecting the edit action, and
then proceeding next to the field mappings section for configuring the data source.

You can configure the `Search` object to set a field as either displayable,
facetable, searchable, and sortable. You can configure the `Relevance` object to
set a field's rank order, boost duration or time period to apply to boosting, freshness,
importance value, and importance values mapped to specific field values. If you use the
console, you can set the search settings for a field by selecting the facet option in the
navigation menu. To set relevance tuning, select the option to search your index in the
navigation menu, enter a query, and use the side panel options to tune the search relevance.
You cannot change the field type once you have created the field.

Amazon Kendra has the following reserved or common document fields that you can
use:

- `_authors`—A list of one or more authors responsible for the
  content of the document.
- `_category`—A category that places a document in a specific
  group.
- `_created_at`—The date and time in ISO 8601 format that the
  document was created. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601
  date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central
  European Time.
- `_data_source_id`—The identifier of the data source that
  contains the document.
- `_document_body`—The content of the document.
- `_document_id`—A unique identifier for the document.
- `_document_title`—The title of the document.
- `_excerpt_page_number`—The page number in a PDF file where the
  document excerpt appears. If your index was created before September 8, 2020, you
  must re-index your documents before you can use this attribute.
- `_faq_id`—If this is a question-answer type document (FAQ), a
  unique identifier for the FAQ.
- `_file_type`—The file type of the document, such as pdf or
  doc.
- `_last_updated_at`—The date and time in ISO 8601 format that the
  document was last updated. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601
  date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central
  European Time.
- `_source_uri`—The URI where the document is available. For
  example, the URI of the document on a company website.
- `_version`—An identifier for the specific version of a
  document.
- `_view_count`—The number of times that the document has been
  viewed.
- `_language_code` (String)—The code for a language that applies
  to the document. This defaults to English if you do not specify a language. For more
  information on supported languages, including their codes, see [Adding
  documents in languages other than English](in-adding-languages.md "in-adding-languages.md").

For custom fields, you create these fields using
`DocumentMetadataConfigurationUpdates` with the `UpdateIndex` API,
just as you do when creating a reserved or common field. You must set the appropriate data
type for your custom field. If you use the console, you update fields by selecting your data
source, selecting the edit action, and then proceeding next to the field mappings section
for configuring the data source. Some data sources don't support adding new fields or custom
fields. You cannot change the field type once you have created the field.

The following are the types you can set for custom fields:

- Date
- Number
- String
- String list

If you added documents to the index using [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API,
`Attributes` lists the fields/attributes of your documents and you create
fields using the `DocumentAttribute` object.

For documents indexed from an Amazon S3 data source, you create fields using a
[JSON metadata
file](s3-metadata.md "s3-metadata.md") that includes the fields information.

If you use a supported database as your data source, you can configure your fields using
the [field
mappings option](data-source-database.md#data-source-procedure-database "data-source-database.md#data-source-procedure-database").
