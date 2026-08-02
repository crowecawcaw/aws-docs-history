Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# GitHub (Server) data source connector field mappings

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
GitHub connector supports the following entities and the associated
reserved and custom attributes.

###### Important

If you map any GitHub (Server) field to Amazon Q document title and document body fields,
Amazon Q will generate responses from data in the document title and body.

###### Note

You can map any GitHub field to the document title or document body
Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Repository](#github-field-mappings-repository "#github-field-mappings-repository")
- [Repository Commit](#github-field-mappings-repository-commit "#github-field-mappings-repository-commit")
- [Issue Document](#github-field-mappings-issue-document "#github-field-mappings-issue-document")
- [Issue Comment](#github-field-mappings-issue-comment "#github-field-mappings-issue-comment")
- [Issue Attachment](#github-field-mappings-issue-attachment "#github-field-mappings-issue-attachment")
- [Pull Request Comment](#github-field-mappings-pull-request-comment "#github-field-mappings-pull-request-comment")
- [Pull Request Document](#github-field-mappings-pull-request-document "#github-field-mappings-pull-request-document")
- [Pull Request Attachment](#github-field-mappings-pull-request-attachment "#github-field-mappings-pull-request-attachment")

## Repository

| GitHub field name    | Index field name           | Description | Data type   |
| -------------------- | -------------------------- | ----------- | ----------- |
| Description          | \_document\_body           | Default     | String      |
| repositoryName       | gh\_repository\_name       | Custom      | String      |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String      |
| category             | \_category                 | Default     | String      |
| owner                | \_authors                  | Default     | String list |
| sourceUrl            | \_source\_uri              | Default     | String      |
| createdAt            | \_created\_at              | Default     | Date        |
| updatedAt            | \_last\_updated\_at        | Default     | Date        |

## Repository Commit

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| Description          | \_document\_body           | Default     | String         |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| fileType             | \_file\_type               | Default     | String         |
| owner                | \_authors                  | Default     | String list    |
| sourceUrl            | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| fileName             | gh\_file\_name             | Default     | String         |
| fileSize             | gh\_size                   | Default     | Long (numeric) |
| branchName           | gh\_branch\_name           | Default     | String         |

## Issue Document

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| issueNumber          | gh\_issue\_number          | Custom      | Long (numeric) |
| issueTitle           | gh\_issue\_title           | Custom      | String         |
| owner                | \_authors                  | Default     | String list    |
| fileType             | \_file\_type               | Default     | String         |
| issueSourceUrl       | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| issueFileName        | gh\_file\_name             | Custom      | String         |
| issueState           | gh\_issue\_state           | Custom      | String         |
| issueLabel           | gh\_issue\_labels          | Default     | String list    |
| issueAssignee        | gh\_issue\_assignee        | Default     | String list    |

## Issue Comment

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| issueNumber          | gh\_issue\_number          | Custom      | Long (numeric) |
| issueTitle           | gh\_issue\_title           | Custom      | String         |
| owner                | \_authors                  | Default     | String list    |
| issueSourceUrl       | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| issueState           | gh\_issue\_state           | Custom      | String         |
| issueLabel           | gh\_issue\_labels          | Default     | String list    |
| issueAssignee        | gh\_issue\_assignee        | Default     | String list    |

## Issue Attachment

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| issueNumber          | gh\_issue\_number          | Custom      | Long (numeric) |
| issueTitle           | gh\_issue\_title           | Custom      | String         |
| owner                | \_authors                  | Default     | String list    |
| issueSourceUrl       | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| issueFileName        | gh\_file\_name             | Custom      | String         |
| issueFileType        | \_file\_type               | Custom      | String         |
| issueState           | gh\_issue\_state           | Custom      | String         |
| issueLabel           | gh\_issue\_labels          | Default     | String list    |
| issueAssignee        | gh\_issue\_assignee        | Default     | String list    |

## Pull Request Comment

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| PRNumber             | gh\_pr\_number             | Custom      | Long (numeric) |
| PRTitle              | gh\_pr\_title              | Custom      | String         |
| owner                | \_authors                  | Default     | String list    |
| PRSourceUrl          | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| PRState              | gh\_pr\_state              | Custom      | String         |
| PRLabel              | gh\_pr\_labels             | Default     | String list    |
| PRAssignee           | gh\_pr\_assignee           | Default     | String list    |

## Pull Request Document

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| PRNumber             | gh\_number                 | Custom      | Long (numeric) |
| PRTitle              | gh\_pr\_title              | Custom      | String         |
| owner                | \_authors                  | Default     | String list    |
| PRSourceUrl          | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| PRFileName           | gh\_file\_name             | Custom      | String         |
| PRFileType           | \_file\_type               | Custom      | String         |
| PRState              | gh\_pr\_state              | Custom      | String         |
| PRLabel              | gh\_pr\_labels             | Default     | String list    |
| PRAssignee           | gh\_pr\_assignee           | Default     | String list    |

## Pull Request Attachment

| GitHub field name    | Index field name           | Description | Data type      |
| -------------------- | -------------------------- | ----------- | -------------- |
| repositoryName       | gh\_repository\_name       | Custom      | String         |
| repositoryVisibility | gh\_repository\_visibility | Custom      | String         |
| category             | \_category                 | Default     | String         |
| PRNumber             | gh\_number                 | Custom      | Long (numeric) |
| PRTitle              | gh\_pr\_title              | Custom      | String         |
| owner                | \_authors                  | Default     | String list    |
| PRSourceUrl          | \_source\_uri              | Default     | String         |
| createdAt            | \_created\_at              | Default     | Date           |
| updatedAt            | \_last\_updated\_at        | Default     | Date           |
| PRFileName           | gh\_file\_name             | Custom      | String         |
| PRFileType           | \_file\_type               | Custom      | String         |
| PRState              | gh\_pr\_state              | Custom      | String         |
| PRLabel              | gh\_pr\_labels             | Default     | String list    |
| PRAssignee           | gh\_pr\_assignee           | Default     | String list    |
