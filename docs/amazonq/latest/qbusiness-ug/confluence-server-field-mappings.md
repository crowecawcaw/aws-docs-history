# Amazon Q Business Confluence (Server/Data Center) data source connector field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to
fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use
  reserved attributes to map commonly occurring document attributes in your data
  source to Amazon Q index fields.
- **Custom** – You can create custom attributes to
  map document attributes that are unique to your data to Amazon Q
  index fields.
  When you connect Amazon Q to a data source, Amazon Q
  automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a
  attribute mapping already available, or if you want to map additional document
  attributes to index fields, use the custom field mappings to specify how a data source
  attribute maps to an Amazon Q index field. You create field mappings by
  editing your data source after your application environment and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes-types.md "doc-attributes-types.md").

###### Important

Filtering using document attributes in chat is only supported through the
API.

The Amazon Q Confluence connector supports the following entities and the
associated reserved and custom attributes.

###### Important

If you map any Confluence (Server/Data Center) field to Amazon Q document title and document body fields,
Amazon Q will generate responses from data in the document title and body.

###### Supported entities and field mappings

- [Space](#confluence-field-mappings-space "#confluence-field-mappings-space")
- [Page](#confluence-field-mappings-page "#confluence-field-mappings-page")
- [Blog](#confluence-field-mappings-blog "#confluence-field-mappings-blog")
- [Comment](#confluence-field-mappings-comment "#confluence-field-mappings-comment")
- [Attachment](#confluence-field-mappings-attachment "#confluence-field-mappings-attachment")

## Space

| Confluence field name | Index field name     | Description | Data type |
| --------------------- | -------------------- | ----------- | --------- |
| spaceName             | cf_sp_document_title | Custom      | String    |
| itemType              | \_category           | Default     | String    |
| url                   | \_source_uri         | Default     | String    |
| spaceKey              | cf_space_key         | Custom      | String    |
| description           | cf_description       | Custom      | String    |
| spaceType             | cf_type              | Custom      | String    |

## Page

| Confluence field name | Index field name         | Description | Data type      |
| --------------------- | ------------------------ | ----------- | -------------- |
| title                 | \_cf_page_document_title | Custom      | String         |
| authors               | \_authors                | Default     | String list    |
| createdDate           | \_created_at             | Default     | Date           |
| modifiedDate          | \_last_updated_at        | Default     | Date           |
| labels                | cf_labels                | Custom      | String list    |
| version               | cf_version               | Custom      | Long (numeric) |
| itemType              | \_category               | Default     | String         |
| spaceKey              | cf_space_key             | Custom      | String         |
| spaceName             | cf_space_name            | Custom      | String         |
| url                   | \_source_uri             | Default     | String         |
| status                | cf_status                | Custom      | String         |
| parentId              | cf_parent_id             | Custom      | String         |

## Blog

| Confluence field name | Index field name     | Description | Data type      |
| --------------------- | -------------------- | ----------- | -------------- |
| title                 | cf_bg_document_title | Custom      | String         |
| author                | \_authors            | Default     | String list    |
| publishedDate         | \_created_at         | Default     | Date           |
| labels                | \_source_uri         | Default     | String         |
| version               | cf_version           | Custom      | Long (numeric) |
| itemType              | \_category           | Custom      | String         |
| spaceKey              | cf_space_key         | Custom      | String         |
| modifiedDate          | \_last_updated_at    | Default     | Date           |
| spaceName             | cf_space_name        | Custom      | String         |
| status                | cf_status            | Custom      | String         |
| url                   | \_source_uri         | Default     | String         |
| parentId              | cf_parent_id         | Custom      | String         |

## Comment

| Confluence field name | Index field name      | Description | Data type      |
| --------------------- | --------------------- | ----------- | -------------- |
| title                 | cf_cmt_document_title | Custom      | String         |
| author                | \_authors             | Default     | String list    |
| createdDate           | \_created_at          | Default     | Date           |
| version               | cf_version            | Custom      | Long (numeric) |
| itemType              | \_category            | Default     | String         |
| spaceKey              | cf_space_key          | Custom      | String         |
| spaceName             | cf_space_name         | Custom      | String         |
| contentType           | cf_content_type       | Custom      | String         |
| url                   | \_source_uri          | Default     | String         |
| parentId              | cf_parent_id          | Custom      | String         |
| status                | cf_status             | Custom      | String         |

## Attachment

| Confluence field name | Index field name             | Description | Data type      |
| --------------------- | ---------------------------- | ----------- | -------------- |
| fileName              | cf_attachment_document_title | Custom      | String         |
| author                | \_authors                    | Default     | String list    |
| createdDate           | \_created_at                 | Default     | Date           |
| labels                | cf_labels                    | Custom      | String list    |
| version               | cf_version                   | Custom      | Long (numeric) |
| itemType              | \_category                   | Default     | String         |
| spaceKey              | cf_space_key                 | Custom      | String         |
| contentType           | cf_content_type              | Custom      | String         |
| modifiedDate          | \_last_updated_at            | Default     | Date           |
| fileSize              | cf_file_size                 | Custom      | Long (numeric) |
| fileType              | cf_attachment_file_type      | Custom      | String         |
| spaceName             | cf_space_name                | Custom      | String         |
| documentId            | \_document_id                | Default     | String list    |
| url                   | \_source_uri                 | Default     | String         |
| parentId              | cf_parent_id                 | Custom      | String         |
| attachmentComment     | cf_attachment_comment        | Custom      | String         |
| status                | cf_status                    | Custom      | String         |
