Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Quip data source connector field mappings

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
Quip connector supports the following entities and the associated reserved
and custom attributes.

###### Note

You can map any Quip field to the document title or document body
Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Thread](#quip-field-mappings-thread "#quip-field-mappings-thread")
- [Message](#quip-field-mappings-message "#quip-field-mappings-message")
- [Attachment](#quip-field-mappings-attachment "#quip-field-mappings-attachment")

## Thread

Amazon Q supports crawling [Quip Threads](https://quip.com/dev/automation/documentation/current#tag/Threads "https://quip.com/dev/automation/documentation/current#tag/Threads") and offers the following thread field
mappings.

| Quip field name     | Index field name    | Description | Data type   |
| ------------------- | ------------------- | ----------- | ----------- |
| qp\_authors         | \_authors           | Default     | String list |
| qp\_category        | \_category          | Default     | String      |
| qp\_file\_type      | qp\_file\_type      | Custom      | String      |
| qp\_document\_title | qp\_document\_title | Custom      | String      |
| qp\_source\_uri     | \_source\_uri       | Default     | String      |
| qp\_created\_at     | \_created\_at       | Default     | Date        |
| qp\_updated\_at     | \_last\_updated\_at | Default     | Date        |

## Message

Amazon Q supports crawling [Quip Messages](https://quip.com/dev/automation/documentation/current#tag/Messages "https://quip.com/dev/automation/documentation/current#tag/Messages") and offers the following message field
mappings.

| Quip field name  | Index field name    | Description | Data type   |
| ---------------- | ------------------- | ----------- | ----------- |
| qp\_authors      | \_authors           | Default     | String list |
| qp\_category     | \_category          | Default     | String      |
| qp\_source\_uri  | \_source\_uri       | Default     | String      |
| qp\_parent\_file | qp\_parent\_file    | Custom      | String      |
| qp\_created\_at  | \_created\_at       | Default     | Date        |
| qp\_updated\_at  | \_last\_updated\_at | Default     | Date        |

## Attachment

Amazon Q supports crawling Quip attachments and offers the
following attachment field mappings.

| Quip field name  | Index field name    | Description | Data type   |
| ---------------- | ------------------- | ----------- | ----------- |
| qp\_authors      | \_authors           | Default     | String list |
| qp\_category     | \_category          | Default     | String      |
| qp\_source\_uri  | \_source\_uri       | Default     | String      |
| qp\_file\_type   | qp\_file\_type      | Custom      | String      |
| qp\_parent\_file | qp\_parent\_file    | Custom      | String      |
| qp\_blob\_id     | qp\_blob\_id        | Custom      | String      |
| qp\_created\_at  | \_created\_at       | Default     | Date        |
| qp\_updated\_at  | \_last\_updated\_at | Default     | Date        |
