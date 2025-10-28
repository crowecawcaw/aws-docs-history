# Drupal data source connector

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

The Amazon Q Drupal connector supports the following entities and
the associated reserved and custom attributes.

###### Supported entities and field mappings

- [Contents](#drupal-field-mappings-contents "#drupal-field-mappings-contents")
- [Comments](#drupal-field-mappings-comments "#drupal-field-mappings-comments")
- [Attachments](#drupal-field-mappings-attachments "#drupal-field-mappings-attachments")

## Contents

| Drupal field name | Index field name     | Entity       | Category | Field type |
| ----------------- | -------------------- | ------------ | -------- | ---------- | -------------- |
| title             | dpl_title            | All Entities | Default  | String     |
| sourceUrl         | dpl_source_url       | All Entities | Default  | String     |
| createdAt         | dpl_created_date     | All Entities | Default  | Date       |
| updatedAt         | dpl_updated_date     | All Entities | Default  | Date       |
| published         | dpl_published        | All Entities | Default  | String     |
| tag               | dpl_tag              | All Entities | Default  | String     |
| author            | dpl_author           | All Entities | Default  | String     |
| category          | dpl_category         | All Entities | Default  | String     |
| visibility        | dpl_visibility       | All Entities | Default  | String     |
| viewId            | dpl_view_id          | All Entities | Default  | String     | ## Comments    |
| Drupal field name | Index field name     | Entity       | Category | Field type |
| ---               | ---                  | ---          | ---      | ---        |
| title             | dpl_comment_title    | All Entities | Default  | String     |
| sourceUrl         | dpl_source_url       | All Entities | Default  | String     |
| createdAt         | dpl_created_date     | All Entities | Default  | Date       |
| updatedAt         | dpl_updated_date     | All Entities | Default  | Date       |
| approvedStatus    | dpl_status           | All Entities | Default  | String     |
| author            | dpl_author           | All Entities | Default  | String     |
| category          | dpl_category         | All Entities | Default  | String     |
| parentEntityId    | dpl_parent_entity_id | All Entities | Default  | String     |
| visibility        | dpl_visibility       | All Entities | Default  | String     |
| viewId            | dpl_view_id          | All Entities | Default  | String     | ## Attachments |
| Drupal field name | Index field name     | Entity       | Category | Field type |
| ---               | ---                  | ---          | ---      | ---        |
| fileName          | dpl_file_name        | All Entities | Default  | String     |
| sourceUrl         | dpl_source_url       | All Entities | Default  | String     |
| createdAt         | dpl_created_date     | All Entities | Default  | Date       |
| updatedAt         | dpl_updated_date     | All Entities | Default  | Date       |
| status            | dpl_status           | All Entities | Default  | String     |
| fileType          | dpl_file_type        | All Entities | Default  | String     |
| fileSize          | dpl_file_size        | All Entities | Default  | String     |
| fileUploadedBy    | dpl_file_uploaded_by | All Entities | Default  | String     |
| category          | dpl_category         | All Entities | Default  | String     |
| parentEntityId    | dpl_parent_entity_id | All Entities | Default  | String     |
| visibility        | dpl_visibility       | All Entities | Default  | String     |
| viewId            | dpl_view_id          | All Entities | Default  | String     |
