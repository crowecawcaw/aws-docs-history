Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Amazon Q Business Confluence (Cloud) data source connector field mappings

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

The Amazon Q
Confluence connector supports the following entities and the associated
reserved and custom attributes.

###### Important

If you map any Confluence (Cloud) field to Amazon Q document title and document body fields,
Amazon Q will generate responses from data in the document title and body.

###### Supported entities and field mappings

- [Space](#confluence-field-mappings-space "#confluence-field-mappings-space")
- [Page](#confluence-field-mappings-page "#confluence-field-mappings-page")
- [Blog](#confluence-field-mappings-blog "#confluence-field-mappings-blog")
- [Comment](#confluence-field-mappings-comment "#confluence-field-mappings-comment")
- [Attachment](#confluence-field-mappings-attachment "#confluence-field-mappings-attachment")

## Space

| Confluence field name | Index field name        | Description | Data type |
| --------------------- | ----------------------- | ----------- | --------- |
| spaceName             | cf\_sp\_document\_title | Custom      | String    |
| itemType              | \_category              | Default     | String    |
| url                   | \_source\_uri           | Default     | String    |
| spaceKey              | cf\_space\_key          | Custom      | String    |
| description           | cf\_description         | Custom      | String    |
| spaceType             | cf\_type                | Custom      | String    |

## Page

| Confluence field name | Index field name            | Description | Data type      |
| --------------------- | --------------------------- | ----------- | -------------- |
| title                 | \_cf\_page\_document\_title | Custom      | String         |
| authors               | \_authors                   | Default     | String list    |
| createdDate           | \_created\_at               | Default     | Date           |
| modifiedDate          | \_last\_updated\_at         | Default     | Date           |
| labels                | cf\_labels                  | Custom      | String list    |
| version               | cf\_version                 | Custom      | Long (numeric) |
| itemType              | \_category                  | Default     | String         |
| spaceKey              | cf\_space\_key              | Custom      | String         |
| spaceName             | cf\_space\_name             | Custom      | String         |
| url                   | \_source\_uri               | Default     | String         |
| status                | cf\_status                  | Custom      | String         |
| parentId              | cf\_parent\_id              | Custom      | String         |

## Blog

| Confluence field name | Index field name        | Description | Data type      |
| --------------------- | ----------------------- | ----------- | -------------- |
| title                 | cf\_bg\_document\_title | Custom      | String         |
| author                | \_authors               | Default     | String list    |
| publishedDate         | \_created\_at           | Default     | Date           |
| labels                | \_source\_uri           | Default     | String         |
| version               | cf\_version             | Custom      | Long (numeric) |
| itemType              | \_category              | Custom      | String         |
| spaceKey              | cf\_space\_key          | Custom      | String         |
| modifiedDate          | \_last\_updated\_at     | Default     | Date           |
| spaceName             | cf\_space\_name         | Custom      | String         |
| status                | cf\_status              | Custom      | String         |
| url                   | \_source\_uri           | Default     | String         |
| parentId              | cf\_parent\_id          | Custom      | String         |

## Comment

| Confluence field name | Index field name         | Description | Data type      |
| --------------------- | ------------------------ | ----------- | -------------- |
| title                 | cf\_cmt\_document\_title | Custom      | String         |
| author                | \_authors                | Default     | String list    |
| createdDate           | \_created\_at            | Default     | Date           |
| version               | cf\_version              | Custom      | Long (numeric) |
| itemType              | \_category               | Default     | String         |
| spaceKey              | cf\_space\_key           | Custom      | String         |
| spaceName             | cf\_space\_name          | Custom      | String         |
| contentType           | cf\_content\_type        | Custom      | String         |
| url                   | \_source\_uri            | Default     | String         |
| parentId              | cf\_parent\_id           | Custom      | String         |
| status                | cf\_status               | Custom      | String         |

## Attachment

| Confluence field name | Index field name                | Description | Data type      |
| --------------------- | ------------------------------- | ----------- | -------------- |
| fileName              | cf\_attachment\_document\_title | Custom      | String         |
| author                | \_authors                       | Default     | String list    |
| createdDate           | \_created\_at                   | Default     | Date           |
| labels                | cf\_labels                      | Custom      | String list    |
| version               | cf\_version                     | Custom      | Long (numeric) |
| itemType              | \_category                      | Default     | String         |
| spaceKey              | cf\_space\_key                  | Custom      | String         |
| contentType           | cf\_content\_type               | Custom      | String         |
| modifiedDate          | \_last\_updated\_at             | Default     | Date           |
| fileSize              | cf\_file\_size                  | Custom      | Long (numeric) |
| fileType              | cf\_attachment\_file\_type      | Custom      | String         |
| spaceName             | cf\_space\_name                 | Custom      | String         |
| documentId            | \_document\_id                  | Default     | String list    |
| url                   | \_source\_uri                   | Default     | String         |
| parentId              | cf\_parent\_id                  | Custom      | String         |
| attachmentComment     | cf\_attachment\_comment         | Custom      | String         |
| status                | cf\_status                      | Custom      | String         |
