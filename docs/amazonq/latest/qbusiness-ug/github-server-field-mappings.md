# GitHub (Server) data source

connector field mappings

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
- [Pull Request
  Comment](#github-field-mappings-pull-request-comment "#github-field-mappings-pull-request-comment")
- [Pull Request
  Document](#github-field-mappings-pull-request-document "#github-field-mappings-pull-request-document")
- [Pull Request
  Attachment](#github-field-mappings-pull-request-attachment "#github-field-mappings-pull-request-attachment")

## Repository

| GitHub field name    | Index field name         | Description | Data type      |
| -------------------- | ------------------------ | ----------- | -------------- | -------------------------- |
| Description          | \_document_body          | Default     | String         |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| owner                | \_authors                | Default     | String list    |
| sourceUrl            | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           | ## Repository Commit       |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| Description          | \_document_body          | Default     | String         |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| fileType             | \_file_type              | Default     | String         |
| owner                | \_authors                | Default     | String list    |
| sourceUrl            | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| fileName             | gh_file_name             | Default     | String         |
| fileSize             | gh_size                  | Default     | Long (numeric) |
| branchName           | gh_branch_name           | Default     | String         | ## Issue Document          |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| issueNumber          | gh_issue_number          | Custom      | Long (numeric) |
| issueTitle           | gh_issue_title           | Custom      | String         |
| owner                | \_authors                | Default     | String list    |
| fileType             | \_file_type              | Default     | String         |
| issueSourceUrl       | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| issueFileName        | gh_file_name             | Custom      | String         |
| issueState           | gh_issue_state           | Custom      | String         |
| issueLabel           | gh_issue_labels          | Default     | String list    |
| issueAssignee        | gh_issue_assignee        | Default     | String list    | ## Issue Comment           |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| issueNumber          | gh_issue_number          | Custom      | Long (numeric) |
| issueTitle           | gh_issue_title           | Custom      | String         |
| owner                | \_authors                | Default     | String list    |
| issueSourceUrl       | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| issueState           | gh_issue_state           | Custom      | String         |
| issueLabel           | gh_issue_labels          | Default     | String list    |
| issueAssignee        | gh_issue_assignee        | Default     | String list    | ## Issue Attachment        |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| issueNumber          | gh_issue_number          | Custom      | Long (numeric) |
| issueTitle           | gh_issue_title           | Custom      | String         |
| owner                | \_authors                | Default     | String list    |
| issueSourceUrl       | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| issueFileName        | gh_file_name             | Custom      | String         |
| issueFileType        | \_file_type              | Custom      | String         |
| issueState           | gh_issue_state           | Custom      | String         |
| issueLabel           | gh_issue_labels          | Default     | String list    |
| issueAssignee        | gh_issue_assignee        | Default     | String list    | ## Pull Request Comment    |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| PRNumber             | gh_pr_number             | Custom      | Long (numeric) |
| PRTitle              | gh_pr_title              | Custom      | String         |
| owner                | \_authors                | Default     | String list    |
| PRSourceUrl          | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| PRState              | gh_pr_state              | Custom      | String         |
| PRLabel              | gh_pr_labels             | Default     | String list    |
| PRAssignee           | gh_pr_assignee           | Default     | String list    | ## Pull Request Document   |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| PRNumber             | gh_number                | Custom      | Long (numeric) |
| PRTitle              | gh_pr_title              | Custom      | String         |
| owner                | \_authors                | Default     | String list    |
| PRSourceUrl          | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| PRFileName           | gh_file_name             | Custom      | String         |
| PRFileType           | \_file_type              | Custom      | String         |
| PRState              | gh_pr_state              | Custom      | String         |
| PRLabel              | gh_pr_labels             | Default     | String list    |
| PRAssignee           | gh_pr_assignee           | Default     | String list    | ## Pull Request Attachment |
| GitHub field name    | Index field name         | Description | Data type      |
| ---                  | ---                      | ---         | ---            |
| repositoryName       | gh_repository_name       | Custom      | String         |
| repositoryVisibility | gh_repository_visibility | Custom      | String         |
| category             | \_category               | Default     | String         |
| PRNumber             | gh_number                | Custom      | Long (numeric) |
| PRTitle              | gh_pr_title              | Custom      | String         |
| owner                | \_authors                | Default     | String list    |
| PRSourceUrl          | \_source_uri             | Default     | String         |
| createdAt            | \_created_at             | Default     | Date           |
| updatedAt            | \_last_updated_at        | Default     | Date           |
| PRFileName           | gh_file_name             | Custom      | String         |
| PRFileType           | \_file_type              | Custom      | String         |
| PRState              | gh_pr_state              | Custom      | String         |
| PRLabel              | gh_pr_labels             | Default     | String list    |
| PRAssignee           | gh_pr_assignee           | Default     | String list    |
