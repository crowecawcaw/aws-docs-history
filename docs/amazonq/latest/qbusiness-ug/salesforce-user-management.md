# How Amazon Q Business connector

crawls Salesforce ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an Salesforce data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Salesforce instance. If you choose to activate ACL crawling,
the information can be used to filter chat responses to your end user's document access
level.

You can apply ACL based chat filtering using Salesforce standard objects
and chatter feeds. ACL based chat filtering isn't available for Salesforce
knowledge articles.

**For standard objects, the `_user_id` and
`_group_ids` are used as follows:**

- `_user_id` – The username of the Salesforce
  user.
- `_group_ids` – The group names in
  Salesforce.

      + Name of the Salesforce
       `Profile`
      + Name of the Salesforce
       `Group`
      + Name of the Salesforce
       `UserRole`
      + Name of the Salesforce
       `PermissionSet`

  **For chatter feeds, the `_user_id` and
  `_group_ids` are used as follows:**

- `_user_id` – The username of the Salesforce user.
  Only available if the item is posted in the user's feed.
- `_group_ids` – Group IDs are used as follows. Only available if
  the feed item is posted in a chatter or collaboration group.
  - The name of the chatter or collaboration group.
  - If the group is public, `PUBLIC:ALL`.

###### Important

To maintain secure access control for Amazon Q Business, each user must have a
unique email address across all connected data sources.

In Salesforce users can share an email address while having a different
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
