# How Amazon Q Business connector

crawls ServiceNow ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an ServiceNow data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your ServiceNow instance. If you choose to activate ACL crawling,
the information can be used to filter chat responses to your end user's document access
level.

###### Note

Amazon Q Business supports:

- Role-based, static ACLs for Service Catalogs
- Role-based, static ACLs for Knowledge Bases
- Role-based, static ACLs for Incidents
  Amazon Q Business does not honor limitations set by ServiceNow's advanced ACLs on
  documents.

The group and user IDs are mapped as follows:

- `_group_ids` – Group IDs exist in ServiceNow on
  files where there are set access permissions. They're mapped from the role names of
  `sys_ids` in ServiceNow.
- `_user_id` – User IDs exist in ServiceNow on
  files where there are set access permissions. They're mapped from the user emails as
  the IDs in ServiceNow.

###### Important

To maintain secure access control for Amazon Q Business, each user must have a
unique email address across all connected data sources.

In ServiceNow users can share an email address while having a different
application-specific unique identifier. However, in Amazon Q Business email
addresses act as unique identifiers.

This means that if a document is shared with a particular user (for example,
arnav\_desai@example.com who is part of pentesters@example.com) on the basis of an
application-specific unique ID, every other user who shares pentesters@example.com (for
example, xiulan\_wang@example.com and efua\_owusu@example.com, both of whom are part of
pentesters@example.com) can receive Amazon Q Business responses with content from
a document that was shared only with Arnav. Similarly, content created by Arnav that
only he should be able to access via Amazon Q Business chat responses, could also
be part of Amazon Q Business chat responses for Xiulan and Efua, because they
share the same email address.

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
