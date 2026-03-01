# How Amazon Q Business connector crawls Zendesk ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Zendesk data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Zendesk instance. If you choose to activate ACL crawling,
the information can be used to filter chat responses to your end users' document access
level.

The Zendesk connector supports enabling or disabling data ingestion for various
entities including Tickets, Ticket Comments, Ticket Comment Attachments, Articles, Article
Attachments, Article Comments, Community Topics, Community Posts, and Community Post
Comments. For Ticket Comment Attachments and Article Attachments, the Zendesk
connector allows applying include/exclude patterns based on file types, enabling more
granular control over which attachments are ingested into Amazon Q Business.

**Roles/Permissions**: Zendesk roles define user
permissions within the platform, including Admins, Agents, Light Agents, End Users, and
Guide Admins. Admins have full control over settings, user management, and content access.
Agents handle tickets, respond to customer queries, and may have restricted access based on
group assignments. Light Agents can view and comment on tickets internally but cannot
interact with customers. End Users are customers who can submit and track tickets. Guide
Admins manage knowledge base content, including articles and community posts. Access control
is determined by roles, groups, organizations, and user segments, ensuring the right level
of visibility and permissions across the system. The Zendesk connector translates
these roles into Amazon Q Business compatible ACLs, supporting View (Read), Edit, and
Delete permissions.

**Identity Crawling**: The connector ensures accurate
synchronization of user access control by retrieving and updating user identities, groups,
and permissions. During this process, it fetches users from Zendesk
Organizations, Groups, and User Segments, aligning them with the correct Access Control
Lists (ACLs) in Amazon Q Business. This allows for consistent enforcement of
role-based access, ensuring that users can only view content they are permitted to access.
Additionally, identity crawling updates group memberships dynamically, reflecting changes in
user roles, suspended accounts, and newly assigned permissions during scheduled
syncs.

**Permissions Inheritance**: In Zendesk,
permission inheritance varies across data source entities such as tickets, articles, and
community content. For tickets, permissions are inherited based on roles (Requester,
Assignee, Follower) and group or organization membership. Permissions for comments, notes
and attachments of tickets are inherited from parent. Community topics and posts inherit
permissions from assigned user segments, but Admins and Guide Admins have universal
access.

**Change Management**: Change Log Mode in Amazon Q Business enables incremental updates by capturing modifications made to content
in Zendesk. Instead of re-indexing all documents, it indexes only newly added,
updated, or deleted items since the last crawl. Any changes to user or group access
permissions are also recorded, ensuring accurate and up-to-date indexing. However, change
log sync does not update ACLs for suspended or reactivated users.

**Failure Handling**: The connector follows a fail-close
approach, meaning if there are permission-related issues or API failures, affected documents
are skipped from ingestion rather than being made publicly accessible. This prevents
unauthorized access while maintaining data integrity.

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
