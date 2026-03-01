# Slack data source connector field mappings

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

The Amazon Q Slack connector supports the following field
mappings:

| Slack field name | Index field name      | Description | Data type      |
| ---------------- | --------------------- | ----------- | -------------- |
| size             | sl_gen_size           | Custom      | Long (numeric) |
| emojis           | sl_gen_emojis         | Custom      | String list    |
| title            | sl_gen_title          | Custom      | String         |
| authors          | \_authors             | Default     | String list    |
| url              | \_source_uri          | Default     | String         |
| category         | sl_gen_category       | Custom      | String         |
| created_at       | \_created_at          | Default     | Date           |
| last_updated_at  | \_last_updated_at     | Default     | Date           |
| msg_channel_id   | sl_message_channel_id | Custom      | String         |
| msg_channel_name | sl_msg_channel_name   | Custom      | String         |
