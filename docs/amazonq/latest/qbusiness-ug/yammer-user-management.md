# How Amazon Q Business connector

crawls Microsoft Yammer ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Microsoft Yammer data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Microsoft Yammer instance. If you choose to activate ACL crawling,
the information can be used to filter chat responses to your end user's document access
level.

The group and user IDs are mapped as follows:

- `_email_id` – Your Microsoft email ID is an identifier that's
  necessary to configure each connector instance. Your email ID can be found in the
  properties section of your Microsoft account dashboard.
- `_group_id` – Group IDs exist in Microsoft Yammer
  Instances where there are set access permissions. They're mapped from the names of
  the groups in Microsoft Yammer.

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
