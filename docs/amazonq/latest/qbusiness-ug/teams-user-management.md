# How Amazon Q Business connector crawls Microsoft Teams ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

Microsoft Teams content is categorized into Chats, Channels, and Calendar. Chats
support one-on-one and group conversations with attachments, which can be filtered using
email domains or regex rules. Channels are structured within Microsoft Teams and can be
Standard (open to all team members), Shared (accessible to team members and invited external
users), or Private (restricted to specific members). Calendars facilitate meeting scheduling
and management, supporting attachments and OneNote tabs.

When you connect a Microsoft Teams data source to Amazon Q Business, Amazon Q Business makes a copy of these resources and creates an index that can be used to
respond to user prompts and queries. Additionally, the connector crawls ACL information
attached to a document (user and group information) from your Microsoft Teams instance.
If you choose to activate ACL crawling, the information can be used to filter chat responses
to your end user's document access level.

**Identity Crawling**: Amazon Q Business synchronizes
both local and federated users/groups. Federated groups are synced outside Amazon Q, and their memberships are not stored. Identities are canonicalized by converting all
letters to lowercase to prevent duplication issues, meaning "TestUser" and "testuser" are
treated as the same. When a user is deleted, their permissions are not inherited by a newly
created user with the same name, ensuring secure access management. Once a user is marked as
disabled in Microsoft Teams, after the next sync users will no longer have access to
search or retrieve previously crawled data, including calendar meetings.

Users can configure the connector to include filters for channel posts and attachments.
Team and Channel name can be included and excluded. Also, we can add regular expression to
include and exclude filters for attachments. Private channels are restricted to specific
members within a team. Shared and private channels have their own ACLs, enabling more
granular permission management.

**Permission Inheritance**: Chats, Channels and Calendar
inherit permissions from the root or the group while attachments inherit from their parent
entity (chat, channel, or calendar event).

**Change Management**: Change Log Mode in Amazon Q Business enables incremental updates by capturing modifications made to content
in Microsoft Teams. Instead of re-indexing all documents, it indexes only newly added,
updated, or deleted items since the last crawl. Any changes to user or group access
permissions are also recorded, ensuring accurate and up-to-date indexing.

**Failure handling**: The connector follows a fail-close
approach, meaning if there are permission-related issues or API failures, affected documents
are skipped from ingestion rather than being made publicly accessible. This prevents
unauthorized access while maintaining data integrity.

For more information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
