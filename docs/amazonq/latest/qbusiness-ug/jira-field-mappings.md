Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Jira data source connector field mappings

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
Jira connector supports the following entities and the associated reserved
and custom attributes.

###### Supported entities and field mappings

- [Projects](#jira-field-mappings-projects "#jira-field-mappings-projects")
- [Issues](#jira-field-mappings-ticket-issues "#jira-field-mappings-ticket-issues")
- [Comments](#jira-field-mappings-comments "#jira-field-mappings-comments")
- [Attachments](#jira-field-mappings-attachments "#jira-field-mappings-attachments")
- [Worklogs](#jira-field-mappings-worklogs "#jira-field-mappings-worklogs")

## Projects

| Jira field name | Index field name | Description | Data type   |
| --------------- | ---------------- | ----------- | ----------- |
| title           | j\_title         | Custom      | String      |
| project\_key    | j\_project\_key  | Custom      | String      |
| lead            | j\_lead          | Custom      | String list |
| url             | \_source\_uri    | Default     | String      |

## Issues

| Jira field name  | Index field name    | Description | Data type   |
| ---------------- | ------------------- | ----------- | ----------- |
| title            | j\_title            | Custom      | String      |
| issue\_key       | j\_issue\_key       | Custom      | String      |
| status           | j\_status           | Custom      | String      |
| project\_name    | j\_project\_name    | Custom      | String      |
| projectKey       | j\_project\_key     | Custom      | String      |
| authors          | \_authors           | Default     | String list |
| assignee         | j\_assignee         | Custom      | String      |
| created\_at      | \_created\_at       | Default     | Date        |
| updated\_at      | \_last\_updated\_at | Default     | Date        |
| url              | \_source\_uri       | Default     | String      |
| issue\_type      | j\_issue\_type      | Custom      | String      |
| priority         | j\_priority         | Custom      | String      |
| resolution       | j\_resolution       | Custom      | String      |
| affects\_version | j\_affects\_version | Custom      | String      |
| fix\_version     | j\_fix\_version     | Custom      | String      |
| labels           | j\_labels           | Custom      | String      |
| environment      | j\_environment      | Custom      | String      |
| reporter         | j\_reporter         | Custom      | String      |
| votes            | j\_votes            | Custom      | String      |
| watchers         | j\_watchers         | Custom      | String      |
| due              | j\_due              | Custom      | String      |
| resolved         | j\_resolved         | Custom      | String      |

## Comments

| Jira field name | Index field name    | Description | Data type   |
| --------------- | ------------------- | ----------- | ----------- |
| authors         | \_authors           | Default     | String list |
| title           | j\_title            | Custom      | String      |
| createdAt       | \_created\_at       | Default     | Date        |
| updatedAt       | \_last\_updated\_at | Default     | Date        |
| project\_name   | j\_project\_name    | Custom      | String      |
| project\_key    | j\_project\_key     | Custom      | String      |
| issue\_key      | j\_issue\_key       | Custom      | String      |
| url             | \_source\_uri       | Default     | String      |

## Attachments

| Jira field name | Index field name | Description | Data type   |
| --------------- | ---------------- | ----------- | ----------- |
| title           | j\_title         | Custom      | String      |
| authors         | \_authors        | Default     | String list |
| size            | j\_size          | Custom      | String      |
| createdAt       | \_created\_at    | Default     | Date        |
| url             | \_source\_uri    | Default     | String      |
| project\_name   | j\_project\_name | Custom      | String      |
| project\_key    | j\_project\_key  | Custom      | String      |
| issue\_key      | j\_issue\_key    | Custom      | String      |

## Worklogs

| Jira field name | Index field name    | Description | Data type   |
| --------------- | ------------------- | ----------- | ----------- |
| title           | j\_title            | Custom      | String      |
| authors         | \_authors           | Default     | String list |
| createdAt       | \_created\_at       | Default     | Date        |
| updatedAt       | \_last\_updated\_at | Default     | Date        |
| url             | \_source\_uri       | Default     | String      |
| project\_name   | j\_project\_name    | Custom      | String      |
| project\_key    | j\_project\_key     | Custom      | String      |
| issue\_key      | j\_issue\_key       | Custom      | String      |
