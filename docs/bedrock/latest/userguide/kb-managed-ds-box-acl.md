# Document-level access controls

###### ACL awareness is not authorization

Bedrock Managed Knowledge Base provides ACL-aware filtering, not a security boundary. Bedrock Managed Knowledge Base does not authenticate end users — your application is responsible for authenticating users and passing verified identity context. Because Bedrock Managed Knowledge Base cannot verify the authenticity of the user context you provide, this feature filters results based on the identity you supply but does not constitute true authorization. You must not rely on this feature as a sole access control mechanism without upstream authentication.

Box data sources optionally support document-level access control. When enabled, Bedrock Managed Knowledge Base syncs access control lists (ACLs) from Box during each crawl and verifies each user's permissions at query time, so users only see results from files they are authorized to access in Box. Document-level access control requires Client Credentials Grant authentication. For the overview of ACL awareness across all connectors, see [Access Control Lists awareness enablement](kb-managed-acl.md "kb-managed-acl.md").

## How it works

When a user queries a knowledge base that uses an ACL-enabled Box data source, Bedrock Managed Knowledge Base enforces access controls in two stages:

- **Pre-retrieval filtering** — Bedrock Managed Knowledge Base applies the access control lists that were synced from Box during the last crawl, returning only candidate documents the user (or their groups) is permitted to access.
- **Real-time verification** — Bedrock Managed Knowledge Base verifies the candidate documents in real time by checking the querying user's current access in Box. Only documents the user is currently authorized to access are included in the response.

This two-stage approach provides document-level access control that stays current even when Box permissions change between syncs.
