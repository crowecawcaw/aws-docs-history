# How Amazon Q Business connector

crawls Slack ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

Slack organizes content into documents, which include messages, attachments,
posts, snippets, thread replies, and emojis. Messages and attachments can belong to
different conversation types such as direct messages (DMs), public channels, or private
channels.

When you connect a Slack data source to Amazon Q Business, Amazon Q Business crawls ACL information (channel IDs) attached to a document from your
Slack instance. If you choose to activate ACL crawling, this information can be
used to filter chat responses to your end user's document access level. Access Control
(ACLs) in Slack is managed through users and groups.

**Identity Crawling**: Slack allows link sharing
at the document level. If a document link is shared across different channels (DMs, groups,
or private channels), the new channel ID is included during crawling, effectively expanding
ACLs to include members of those channels. Slack does not enforce explicit deny
rules: public channels allow user removal but do not prevent them from rejoining, whereas
private channels restrict reentry without an invitation. The minimum permission to query
channel data varies: for public channels, workspace membership is sufficient, while private
channels require direct membership for access. Slack enforces username
restrictions, supporting only lowercase letters, numbers, periods, hyphens, and underscores.
This lowercase format is maintained when crawling identities. ACL mismatches can occur if
case differences exist between Slack usernames and identity data stored in the
connector, potentially preventing access to crawled information. When a user is deactivated
or deleted, they lose access to crawled data, and subsequent syncs reflect this by removing
the user from ACLs.

**Permission Inheritance**: The Slack Workspace is
the top-most entity controlling access. All workspace members can access public channels by
default. Public channels have no ACLs; they are accessible to all workspace members. If ACLs
are disabled, all public channel content is open to everyone on Amazon Q. DMs,
groups, and private channels have independent ACLs, which completely replace any parent
ACLs. Private channels restrict access to invited members, including external collaborators
via Slack Connect. All entities inherit permissions from the parent.

**Mapping Rules**: Slack's inheritance mapping
follows its native structure without custom logic. Federated groups are treated as local
upon syncing, with all members stored regardless of status. Emails, links, and other text
within messages are crawled as regular strings without specific parsing. Link-sharing does
not modify document ACLs: a shared link in a message is crawled as plain text rather than as
an access control change. Public channels are accessible to all Amazon Q users if
no ACL is applied.

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
