# How Amazon Q Business connector

crawls Box ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

**Roles/permissions**: The Box connector
translates Box permissions into ACLs that are compatible with Amazon Q Business. There are seven primary roles with permissions:

- Co-owner - Has full control, can change advanced folder settings
- Editor - Has read/write access, can view, download, edit, delete, and manage
  sharing.
- Viewer - Has read-only access, can preview and download
- Uploader - Has limited write access, can only upload and see names
- Viewer Uploader - A combination of Viewer and Uploader capabilities
- Previewer - Has limited read access, can only preview items
- Previewer Uploader - A combination of Previewer and Uploader capabilities
  **Permission Inheritance**: Files/subfolders inherit
  permissions from parent folders by default. Permissions follow a "waterfall" design where
  individuals have access to the folder they are invited into and any subfolders beneath it.
  Changing permissions on subfolders will result in an error because collaboration is only
  changeable at the item where it was created.

**Identity Crawling**: Individual user and group
synchronization is supported via email addresses. Each user gets a unique user ID, even if
recreated with the same email address. Permissions are tied to user IDs, not email
addresses.

Change Management: ACL changes are supported in change log mode, including collaboration
invites, accepts, and role changes.

Failure handling: The connector implements a fail-close approach for API failures, with
rate limiting handled through queue-based wait time with exponential backoff. Documents are
skipped from ingestion rather than being made publicly accessible when permission-related
issues occur.

For more information, see [Key data
source connector concepts](-connector-app.md#-connector-key-concepts "-connector-app.md#-connector-key-concepts").
