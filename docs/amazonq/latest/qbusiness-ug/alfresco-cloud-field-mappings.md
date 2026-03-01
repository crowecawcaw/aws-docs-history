# Alfresco (Cloud) data source connector field mappings

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
Alfresco connector supports the following entities and the associated
reserved and custom attributes.

###### Important

If you map any Alfresco (Cloud) field to Amazon Q document title and document body fields,
Amazon Q will generate responses from data in the document title and body.

###### Supported entities and field mappings

- [Documents](#alfresco-field-mappings-documents "#alfresco-field-mappings-documents")
- [Comments](#alfresco-field-mappings-comments "#alfresco-field-mappings-comments")

## Documents

| Alfresco field name | Index field name  | Description | Data type      |
| ------------------- | ----------------- | ----------- | -------------- |
| creationTime        | \_created_at      | Default     | Date           |
| lastModified        | \_last_updated_at | Default     | Date           |
| author              | \_authors         | Default     | String list    |
| sourceUri           | \_source_uri      | Default     | String         |
| category            | \_category        | Default     | String         |
| fileType            | \_file_type       | Default     | String         |
| version             | \_version         | Default     | String         |
| siteName            | al_site_name      | Custom      | String         |
| size                | al_document_size  | Custom      | Long (numeric) |
| versionType         | al_version_type   | Custom      | String         |
| title               | al_document_title | Custom      | String         |
| repositoryId        | al_repository_id  | Custom      | String         |

## Comments

| Alfresco field name | Index field name  | Description | Data type      |
| ------------------- | ----------------- | ----------- | -------------- |
| creationTime        | \_created_at      | Default     | Date           |
| lastModified        | \_last_updated_at | Default     | Date           |
| author              | \_authors         | Default     | String list    |
| sourceUri           | \_source_uri      | Default     | String         |
| version             | \_version         | Default     | String         |
| category            | \_category        | Default     | String         |
| fileType            | \_file_type       | Default     | String         |
| siteName            | al_site_name      | Custom      | String         |
| size                | al_document_size  | Custom      | Long (numeric) |
| versionType         | \_al_version_type | Custom      | String         |
| title               | al_document_title | Custom      | String         |
| repositoryId        | al_repository_id  | Custom      | String         |
