# Aurora (PostgreSQL) data source

connector field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q enables
you to map document attributes from your data sources to fields in your Amazon Q
index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use reserved
  attributes to map commonly occurring document attributes in your data source to
  Amazon Q index fields.
- **Custom** – You can create custom attributes to map
  document attributes that are unique to your data to Amazon Q index fields.
  When you connect Amazon Q to a data source, Amazon Q automatically maps specific data
  source document attributes to fields within an Amazon Q index. If a document attribute in
  your data source doesn't have a attribute mapping already available, or if you want to
  map additional document attributes to index fields, use the custom field mappings to specify
  how a data source attribute maps to an Amazon Q index field. You create field mappings by
  editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through
the API.

The Amazon Q PostgreSQL connector supports the following field mappings:

###### Supported field mappings

- [Document](#aurora-postgresql-field-mappings-document "#aurora-postgresql-field-mappings-document")

## Document

| JDBC field name   | Index field name  | Description | Data type |
| ----------------- | ----------------- | ----------- | --------- |
| jd_document_id    | jd_document_id    | Custom      | String    |
| jd_document_title | jd_document_title | Custom      | String    |
| jd_source_uri     | \_source_uri      | Default     | String    |
