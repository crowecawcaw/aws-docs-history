# How Amazon Q Business connector

crawls IBM DB2 ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect a database data source to Amazon Q, Amazon Q crawls user and group
information from a column in the source table. You specify this column in the console or
using the `configuration` parameter as part of the `CreateDataSource`
operation.

If you choose to activate ACL crawling, the information can be used to filter chat
responses to your end user's document access level.

A database data source has the following limitations:

- You can only specify an allow list for a database data source. You can't specify a
  deny list.
- You can only specify groups. You can't specify individual users for the allow
  list.
- The database column should be a string containing a semicolon delimited list of
  groups.
  For more
  information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding User Store](connector-principal-store.md "connector-principal-store.md")
