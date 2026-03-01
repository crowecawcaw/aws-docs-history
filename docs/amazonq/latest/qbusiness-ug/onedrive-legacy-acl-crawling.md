# How Amazon Q Business connector crawls Microsoft OneDrive ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

The Microsoft OneDrive connector for Amazon Q Business crawls files, including
documents, spreadsheets, presentations, and notes, as the primary content type. It supports
various file formats and integrates directly with Microsoft Office apps.

**Roles/permissions**: The Microsoft OneDrive connector
translates Microsoft OneDrive permissions into ACLs that are compatible with Amazon Q Business. The basic permissions include:

- Read-only Access: users can view
- Preview Access: users can view but cannot download
- Edit: users can modify content
  **Permission Inheritance**: The Microsoft OneDrive connector
  is designed to detect and handle hierarchical content organization. In Microsoft OneDrive
  files and subfolders inherit permissions from parent folders by default. Permissions can be
  customized at sub-folder and file levels. In this case, the ACLs are a union of the parent
  ACLs and child ACLs.

**Identity Crawling**: Individual user and group
synchronization is supported, including federated groups. Users and groups are synced using
email IDs (each group in Active Directory will have email assigned to it).

**Change Management**: ACL changes are supported in Change
Log Mode, ensuring that items added, updated, or deleted since the last crawl are indexed.
Any changes to access or permissions of groups or users for any entity will be
captured.

**Failure handling**: The connector implements a fail-close
approach, meaning that if there are permission-related issues or API failures, the document
is skipped from ingestion rather than being made publicly accessible.
