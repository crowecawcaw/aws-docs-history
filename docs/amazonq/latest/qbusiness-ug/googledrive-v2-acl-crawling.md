# How Amazon Q Business connector crawls Google Drive ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

The Google Drive connector for Amazon Q Business crawls files
with enhanced performance. It supports various file formats, including spreadsheets,
presentations, images, audio/video files, and Google Docs™.

**Roles/permissions**: The Google
Drive connector translates Google Drive permissions into
ACLs that are compatible with Amazon Q Business. There are four primary roles
with permissions:

- Owner - Has full control.
- Editor - Can modify content, update metadata, and add or remove comments.
- Commenter - Can view content and add comments.
- Viewer - Has read-only access.
  **Permission Inheritance**: The Google
  Drive connector is designed to detect and handle hierarchical content
  organization across My Drive and Shared Drives with improved efficiency. By default,
  files and subfolders inherit permissions from parent folders. Permissions can be
  explicitly modified at either the file or folder level to override inherited
  settings. In this case, the ACLs are a union of the parent ACLs and child ACLs.

**Identity Crawling**: Domain-wide access is
supported using service account authentication. Google Drive supports nested groups,
meaning that one group can be a member of another. The connector handles complex
group structures by flattening group memberships and ensuring that permissions are
applied correctly across all levels.

**Change Management**: ACL changes are automatically
detected and processed during incremental synchronization.

**Failure handling**: The connector implements a
fail-close approach, meaning that if there are permissions-related issues or API
failures, a document is skipped from ingestion rather than being made publicly
accessible.
