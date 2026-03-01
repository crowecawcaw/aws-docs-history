# Box data source connector field mappings

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

The Amazon Q
Box connector supports the following entities and the associated reserved and
custom attributes.

###### Supported entities and field mappings

- [Files and folders](#box-field-mappings-files-folders "#box-field-mappings-files-folders")
- [Comments](#box-field-mappings-comments "#box-field-mappings-comments")
- [Tasks](#box-field-mappings-tasks "#box-field-mappings-tasks")
- [Web links](#box-field-mappings-web-links "#box-field-mappings-web-links")

## Files and folders

| Box field name | Index field name  | Description | Data type   |
| -------------- | ----------------- | ----------- | ----------- |
| bx_createdAt   | \_created_at      | Default     | Date        |
| bx_modifiedAt  | \_last_updated_at | Default     | Date        |
| bx_authors     | \_authors         | Default     | String list |
| bx_uri         | \_source_uri      | Default     | String      |
| bx_size        | bx_file_size      | Custom      | String      |
| bx_category    | \_category        | Default     | String      |

## Comments

| Box field name | Index field name  | Description | Data type |
| -------------- | ----------------- | ----------- | --------- |
| bx_createdAt   | \_created_at      | Default     | Date      |
| bx_modifiedAt  | \_last_updated_at | Default     | Date      |
| bx_author      | \_authors         | Custom      | String    |
| bx_parentFile  | bx_comment_item   | Custom      | String    |
| bx_category    | \_category        | Default     | String    |

## Tasks

| Box field name  | Index field name    | Description | Data type |
| --------------- | ------------------- | ----------- | --------- |
| bx_createdAt    | \_created_at        | Default     | Date      |
| bx_action       | bx_task_action      | Custom      | String    |
| bx_taskComplete | bx_task_completed   | Custom      | String    |
| bx_taskItem     | bx_task_item        | Custom      | String    |
| bx_taskAssigned | bx_task_assigned_to | Custom      | String    |
| bx_author       | bx_author           | Custom      | String    |
| bx_category     | \_category          | Default     | String    |
| bx_uri          | \_source_uri        | Default     | String    |

## Web links

| Box field name | Index field name | Description | Data type |
| -------------- | ---------------- | ----------- | --------- |
| bx_createdAt   | \_created_at     | Default     | Date      |
| bx_author      | bx_author        | Custom      | String    |
| bx_category    | \_category       | Default     | String    |
| bx_uri         | \_source_uri     | Default     | String    |
