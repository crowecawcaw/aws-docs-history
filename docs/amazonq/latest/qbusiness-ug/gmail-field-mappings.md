# Gmail data source connector

field mappings

You can improve search results and customize your users' chat experience by mapping document attributes from your Gmail data to fields in your Amazon Q index.

With Amazon Q, you can map two types of attributes to index fields:

- **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
- **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.
  When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have an attribute mapping already available, or if you want to map additional document attributes to index fields, you can use custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after you create your application and retriever.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through the API.

The Amazon Q
Gmail connector supports the following entities and the associated reserved
and custom attributes.

###### Supported entities and field mappings

- [Messages](#gmail-field-mappings-messages "#gmail-field-mappings-messages")

## Messages

| Gmail field name | Index field name         | Description | Data type   |
| ---------------- | ------------------------ | ----------- | ----------- |
| category         | \_category               | Default     | String      |
| internalDate     | \_created_at             | Default     | Date        |
| id               | gmail_message_is         | Custom      | String      |
| labelIds         | gmail_message_label_ids  | Custom      | String list |
| historyId        | gmail_message_history_id | Custom      | String      |
| subject          | gmail_subject            | Custom      | String      |
| from             | gmail_from               | Custom      | String      |
| to               | gmail_to                 | Custom      | String list |
| cc               | gmail_cc                 | Custom      | String list |
| bcc              | gmail_bcc                | Custom      | String list |
