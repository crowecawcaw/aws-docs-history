# Jira data source connector

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
| title           | j_title          | Custom      | String      |
| project_key     | j_project_key    | Custom      | String      |
| lead            | j_lead           | Custom      | String list |
| url             | \_source_uri     | Default     | String      |

## Issues

| Jira field name | Index field name  | Description | Data type   |
| --------------- | ----------------- | ----------- | ----------- |
| title           | j_title           | Custom      | String      |
| issue_key       | j_issue_key       | Custom      | String      |
| status          | j_status          | Custom      | String      |
| project_name    | j_project_name    | Custom      | String      |
| projectKey      | j_project_key     | Custom      | String      |
| authors         | \_authors         | Default     | String list |
| assignee        | j_assignee        | Custom      | String      |
| created_at      | \_created_at      | Default     | Date        |
| updated_at      | \_last_updated_at | Default     | Date        |
| url             | \_source_uri      | Default     | String      |
| issue_type      | j_issue_type      | Custom      | String      |
| priority        | j_priority        | Custom      | String      |
| resolution      | j_resolution      | Custom      | String      |
| affects_version | j_affects_version | Custom      | String      |
| fix_version     | j_fix_version     | Custom      | String      |
| labels          | j_labels          | Custom      | String      |
| environment     | j_environment     | Custom      | String      |
| reporter        | j_reporter        | Custom      | String      |
| votes           | j_votes           | Custom      | String      |
| watchers        | j_watchers        | Custom      | String      |
| due             | j_due             | Custom      | String      |
| resolved        | j_resolved        | Custom      | String      |

## Comments

| Jira field name | Index field name  | Description | Data type   |
| --------------- | ----------------- | ----------- | ----------- |
| authors         | \_authors         | Default     | String list |
| title           | j_title           | Custom      | String      |
| createdAt       | \_created_at      | Default     | Date        |
| updatedAt       | \_last_updated_at | Default     | Date        |
| project_name    | j_project_name    | Custom      | String      |
| project_key     | j_project_key     | Custom      | String      |
| issue_key       | j_issue_key       | Custom      | String      |
| url             | \_source_uri      | Default     | String      |

## Attachments

| Jira field name | Index field name | Description | Data type   |
| --------------- | ---------------- | ----------- | ----------- |
| title           | j_title          | Custom      | String      |
| authors         | \_authors        | Default     | String list |
| size            | j_size           | Custom      | String      |
| createdAt       | \_created_at     | Default     | Date        |
| url             | \_source_uri     | Default     | String      |
| project_name    | j_project_name   | Custom      | String      |
| project_key     | j_project_key    | Custom      | String      |
| issue_key       | j_issue_key      | Custom      | String      |

## Worklogs

| Jira field name | Index field name  | Description | Data type   |
| --------------- | ----------------- | ----------- | ----------- |
| title           | j_title           | Custom      | String      |
| authors         | \_authors         | Default     | String list |
| createdAt       | \_created_at      | Default     | Date        |
| updatedAt       | \_last_updated_at | Default     | Date        |
| url             | \_source_uri      | Default     | String      |
| project_name    | j_project_name    | Custom      | String      |
| project_key     | j_project_key     | Custom      | String      |
| issue_key       | j_issue_key       | Custom      | String      |
