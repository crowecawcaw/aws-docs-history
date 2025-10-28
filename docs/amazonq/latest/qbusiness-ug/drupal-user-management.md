# How Amazon Q Business connector

crawls Drupal ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Drupal data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Drupal instance. If you choose to activate ACL crawling,
the information can be used to filter chat responses to your end user's document access
level.

Amazon Q gets the user and group information from the Drupal instance.The group
and user IDs are mapped as follows:

- `_group_ids` – Group IDs exist in Drupal on files where there are
  set access permissions. They are mapped from the names of the groups in
  Drupal.
- `_user_id` – User IDs exist in Drupal on files where there are
  set access permissions. They are mapped from the user emails as the IDs in
  Drupal.
  For more
  information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
