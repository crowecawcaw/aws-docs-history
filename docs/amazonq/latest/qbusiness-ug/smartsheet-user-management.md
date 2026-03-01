# How Amazon Q Business connector crawls Smartsheet ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

Smartsheet organizes its data into several entities, including Workspaces, Sheets,
Rows, Columns, Attachments, and Comments. Workspaces serve as hierarchical containers that
hold folders and individual sheets. Connectors support crawling ACL and identity information
where applicable based on the data source. When you connect a Smartsheet data source
to Amazon Q Business, Amazon Q Business crawls ACL information attached to a
document (user and group information) from your Smartsheet instance. The
Smartsheet connector does not allow disabling ACLs, so you must always inforce
permissions. ACL information can be used to filter chat responses based your end users'
document access level.

**Roles/Permissions**: Users and groups can be assigned
various roles including Admin, Editor, and Viewer. Permissions can be managed at different
levels, including Workspaces, Sheets, and individual Rows. Smartsheet enforces an
Allow Mode for ACLs, meaning permissions are granted explicitly without an explicit deny
option. Sheets and Workspaces can be shared via links with different permission levels (View
or Edit), but public link sharing is not supported. In addition, Smartsheet allows
setting sheets as either searchable or non-searchable, and the connector ensures that this
setting is honored when ingesting Smartsheet data. The minimum permission required
to read a sheet or workspace is "Viewer". Proper mapping between Smartsheet ACLs and
Amazon Q ACL definitions is essential to ensure security and permission
consistency.

**Identity Crawling**: Smartsheet supports both local
and federated users/groups, but the connector does not support federated. Usernames in
Smartsheet are case-insensitive and allow special characters. This system ensures
that two users can have the same name but must have unique email addresses. In addition,
group names must be unique, because Smartsheet does not allow duplicate group names
with mixed case. This prevents identity collisions, ensuring that permissions and access
remain properly assigned. If an identity is deleted and later recreated, it does not
automatically inherit previous permissions. Smartsheet does not have a suspended
user concept, if a user is removed from the user library, they still appear in shared lists
for sheets where they previously had access.

**Permission Inheritance**: Permissions in Smartsheet
follow an inheritance model, where Workspaces act as the top-most entity. If no explicit ACL
is set at the sheet or folder level, permissions are inherited from the parent Workspace.
Inherited permissions typically operate as an intersection of parent permissions, unless
explicitly modified. However, sheets can have their own ACLs that override inherited
permissions. Document-level permissions can include options such as "View Sheet" or "Edit
Sheet".

**Change Management**: Change Log Mode in Amazon Q Business enables incremental updates by capturing modifications made to content
in Smartsheet. It indexes only newly added, updated, or deleted items since the last
crawl, onstead of re-indexing all documents. Any changes to user or group access permissions
are also recorded, ensuring accurate and up-to-date indexing.

**Failure handling**: The connector follows a fail-close
approach, meaning if there are permission-related issues or API failures, affected documents
are skipped from ingestion rather than being made publicly accessible. This prevents
unauthorized access while maintaining data integrity.

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
