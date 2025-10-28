# Dropbox data source connector

field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields
in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use reserved
  attributes to map commonly occurring document attributes in your data source to
  Amazon Q index fields.
- **Custom** – You can create custom attributes to map
  document attributes that are unique to your data to Amazon Q index
  fields.
  When you connect Amazon Q to a data source, Amazon Q automatically
  maps specific data source document attributes to fields within an Amazon Q index.
  If a document attribute in your data source doesn't have a attribute mapping already
  available, or if you want to map additional document attributes to index fields, use the
  custom field mappings to specify how a data source attribute maps to an Amazon Q
  index field. You create field mappings by editing your data source after your application
  and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through the API.

The Amazon Q Dropbox connector supports the following entities and
the associated reserved and custom attributes.

###### Supported entities and field mappings

- [Files](#dropbox-field-mappings-files "#dropbox-field-mappings-files")
- [Dropbox Paper](#dropbox-field-mappings-paper "#dropbox-field-mappings-paper")
- [Dropbox Paper Templates](#dropbox-field-mappings-paper-templates "#dropbox-field-mappings-paper-templates")
- [Shortcuts](#dropbox-field-mappings-shortcuts "#dropbox-field-mappings-shortcuts")

## Files

| Dropbox field name | Index field name    | Description | Data type      |
| ------------------ | ------------------- | ----------- | -------------- | -------------------------- |
| sourceUrl          | \_source_uri        | Default     | String         |
| category           | \_category          | Default     | String         |
| fileName           | dbx_file_name       | Custom      | String         |
| fileId             | dbx_id1             | Custom      | String         |
| clientModifiedDate | dbx_client_modified | Custom      | Date           |
| serverModifiedDate | dbx_server_modified | Custom      | Date           |
| fileSize           | dbx_file_size       | Custom      | Long (numeric) |
| pathDisplay        | dbx_path_display    | Custom      | String         |
| tags               | dbx_tags            | Custom      | String         | ## Dropbox Paper           |
| Dropbox field name | Index field name    | Description | Data type      |
| ---                | ---                 | ---         | ---            |
| sourceUrl          | \_source_uri        | Default     | String         |
| category           | \_category          | Default     | String         |
| fileName           | dbx_file_name       | Custom      | String         |
| fileId             | dbx_id1             | Custom      | String         |
| clientModifiedDate | dbx_client_modified | Custom      | Date           |
| serverModifiedDate | dbx_server_modified | Custom      | Date           |
| fileSize           | dbx_file_size       | Custom      | Long (numeric) |
| pathDisplay        | dbx_path_display    | Custom      | String         |
| tags               | dbx_tags            | Custom      | String         | ## Dropbox Paper Templates |
| Dropbox field name | Index field name    | Description | Data type      |
| ---                | ---                 | ---         | ---            |
| sourceUrl          | \_source_uri        | Default     | String         |
| category           | \_category          | Default     | String         |
| fileName           | dbx_file_name       | Custom      | String         |
| fileId             | dbx_id1             | Custom      | String         |
| clientModifiedDate | dbx_client_modified | Custom      | Date           |
| serverModifiedDate | dbx_server_modified | Custom      | Date           |
| fileSize           | dbx_file_size       | Custom      | Long (numeric) |
| pathDisplay        | dbx_path_display    | Custom      | String         |
| tags               | dbx_tags            | Custom      | String         | ## Shortcuts               |
| Dropbox field name | Index field name    | Description | Data type      |
| ---                | ---                 | ---         | ---            |
| sourceUrl          | \_source_uri        | Default     | String         |
| category           | \_category          | Default     | String         |
| fileName           | dbx_file_name       | Custom      | String         |
| fileId             | dbx_id1             | Custom      | String         |
| clientModifiedDate | dbx_client_modified | Custom      | Date           |
| serverModifiedDate | dbx_server_modified | Custom      | Date           |
| fileSize           | dbx_file_size       | Custom      | Long (numeric) |
| pathDisplay        | dbx_path_display    | Custom      | String         |
| tags               | dbx_tags            | Custom      | String         |
