# How Amazon Q Business connector crawls Google Calendar ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Google Calendar data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Google Calendar instance. If you choose to activate ACL crawling,
the information can be used to filter chat responses to your end user's document access
level.

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
