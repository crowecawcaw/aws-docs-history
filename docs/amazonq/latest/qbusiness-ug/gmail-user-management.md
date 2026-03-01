# How Amazon Q Business connector crawls Gmail ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Gmail data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group information) from your Gmail instance. ACL crawling behavior differs between the two Gmail connector versions.

###### Note

**ACL behavior by connector version:**

- **Latest connector:** ACL and identity crawling is automatically enabled and cannot be disabled. Only applies to email messages and draft emails - attachments are not supported.
- **Legacy connector:** ACL and identity crawling can be manually configured during setup. Applies to both messages and attachments when attachment crawling is enabled.
  The legacy Gmail connector for Amazon Q Business crawls 2 primary content types: messages (email along with metadata such as subject, from, or to) and attachments. Each email message (in sent and inbox) and its respective attachments is considered as a separate document with distinct document IDs. Currently, the connector cannot associate an attachment with its parent message, even though attachments inherit permissions from parent messages.

###### Note

**Latest connector limitations:** The latest Gmail
connector does not support attachment crawling. The latest Gmail connector does not
support attachment crawling. If your organization requires attachment indexing, use the
legacy connector instead.

**Permission Inheritance**: ACLs for messages are set based on user email addresses. **Legacy connector only:** Attachments automatically inherit permissions from parent email messages when attachment crawling is enabled.

**ACL indexing**: Individual user synchronization is supported based on email addresses, and domain-wide access is supported using service account authentication.

**Change Management**: ACL changes are supported in both Full Crawl and Incremental or Change Log modes.

**Failure handling** The connector implements a fail-close
approach for API failures, with rate limiting handled through queue-based wait time with
exponential backoff. When permissions issues occur, documents are skipped from ingestion
rather than being made publicly accessible.

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
