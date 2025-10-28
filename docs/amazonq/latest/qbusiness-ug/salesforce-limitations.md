# Known limitations for the Salesforce Online

connector

The Salesforce Online connector has the following known limitations:

- The Salesforce Online connector doesn't currently (as of 2/14/25) support explicit
  deny permission specifications for Contract, Task, and Custom objects and their respective
  attachments, although it respects base access controls for Salesforce Online entities.
  Users who have access to an entity through base access controls would still have access to
  those entities in Amazon Q Business - even if they have been added to the explicit deny list
  in Salesforce.
- The Salesforce Online connector doesn't support field-level access control,
  respecting only the parent-level access control. If a field-level access control
  configuration is detected within an entity, Amazon Q Business will utilize the parent level
  security setting. This means that if a user has access to the parent entity/document in
  Salesforce, they will be able to see all fields of that document in Amazon Q Business,
  regardless of any field-level security restrictions that exist in Salesforce.
- The Salesforce Online connector does not offer the ability to perform incremental
  syncs based on new, modified, or deleted files. At this time, it can perform only full
  syncs.
- The Salesforce Online API doesn't provide the status of deleted
  **Group**, **Partner**, **Profile**,
  and **User** entities. So, the Salesforce Online connector can't
  retrieve this information.
- The Salesforce Online API doesn't provide the status of modified **Attachment
  titles** (Lightning Version). So, the Salesforce Online connector can't
  retrieve this information.
- The Salesforce Online connector supports custom field mappings only for the following
  entities: **Account**, **Campaign**,
  **Contact**, **Contract**, **Case**,
  **Product**
  **Lead**, **Pricebook**, and
  **CustomEntity**.
- The Salesforce Online API does not provide ACL information for documents with shared
  access types.
- By default, Salesforce Online Developer has a maximum limit of 15000 total calls per
  24 hour period. If a request exceeds this limit, the API returns a
  `REQUEST_LIMIT_EXCEEDED` error.
- Because Amazon Q Business uses email address as unique identifiers, each user
  must have a unique email address.
- The Salesforce Online connector only updates user status during connector syncs,
  meaning that any deactivated users are only deactivated in Amazon Q Business during the next
  connector sync. If a user is deactivated in Salesforce they may retain access through
  Amazon Q Business until the next sync.
- The Salesforce Online connector respects hierarchies for custom object record access
  regardless of Salesforce settings, due to Salesforce API limitations. In other words,
  while Salesforce Online lets users disable Grant Access Using Hierarchies for custom
  objects, the role hierarchy will still apply for Amazon Q Business.
- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content"
  option is not available due to Salesforce Online API limitations. We recommend using
  "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if
  you need to use this sync mode.
