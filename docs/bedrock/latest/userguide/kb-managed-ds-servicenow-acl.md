

# Document-level access controls
<a name="kb-managed-ds-servicenow-acl"></a>

ServiceNow data sources optionally support document-level access control. When enabled, Bedrock Managed Knowledge Base resolves each document's ServiceNow user criteria into concrete users during the crawl. It enforces these criteria at query time, so users only see content they are entitled to in ServiceNow. For the overview of ACL awareness across all connectors, see [Access Control Lists awareness enablement](kb-managed-acl.md).

**ACL awareness is not authorization**  
Bedrock Managed Knowledge Base provides ACL-aware filtering (it filters results by access permissions) but this is not a security boundary. Bedrock Managed Knowledge Base does not authenticate end users. Your application is responsible for authenticating users and passing verified identity context. Bedrock Managed Knowledge Base cannot verify the authenticity of the user context you provide. As a result, this feature filters results based on the identity you supply, but it does not constitute true authorization. You must not rely on this feature as your only access control mechanism — always pair it with upstream authentication.

## How it works
<a name="kb-managed-ds-servicenow-acl-how"></a>

Understanding this flow helps you set correct expectations and diagnose access issues. Access flows through three stages: ServiceNow defines the permissions, the connector resolves them to concrete users during the crawl, and Bedrock Managed Knowledge Base enforces them at query time.
+ **ServiceNow (source)** — User criteria on each knowledge article or knowledge base, plus the four-table service catalog ACL model, define who can read each document.
+ **Crawl-time resolution** — The connector reads each document's user criteria and resolves them to concrete allow and deny user lists. It does this by reading the group, role, and attribute membership tables. It writes synthetic `uc_<criteria_sys_id>` allow and deny groups and stores them per document in the index.
+ **Query-time enforcement** — Your application passes the querying user's verified identity (email). The index returns only the documents that identity is permitted to see. Deny always wins, and unknown users get nothing. This behavior is called *fail-closed*: when the system can't confirm access, it denies access by default rather than granting it.

The principal is the user's email address. Your application must pass the authenticated user's email as the identity on the retrieve call.

## What is crawled
<a name="kb-managed-ds-servicenow-acl-crawl"></a>

When ACLs are enabled, Bedrock Managed Knowledge Base crawls the following permission structures from ServiceNow:
+ Knowledge article and knowledge base user criteria (both `can_read` and `cannot_read`), at the article level and the knowledge-base level.
+ Service catalog item permissions, using the four-table model (direct-user allow and deny, and criteria allow and deny).
+ The group, role, and attribute memberships used to resolve criteria to concrete users, from tables such as `sys_user_grmember`, `sys_user_has_role`, and `sys_security_acl`.

Resolving these structures requires additional read roles on the service account and specific knowledge base configuration in ServiceNow. Complete this setup before you enable ACLs. See [Additional setup for document-level access control (ACLs)](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-acl).

At query time you pass the user's email address. Bedrock Managed Knowledge Base matches it against each document's resolved allow and deny lists. For more information about the identity model, see [Access Control Lists awareness enablement](kb-managed-acl.md).

## Enable ACL awareness
<a name="kb-managed-ds-servicenow-acl-enable"></a>

To enable ACL awareness for a ServiceNow data source, set `aclEnabled` to `true` in the `connectorParameters`. ACLs use the same OAuth 2.0 Client Credentials (2LO, or two-legged OAuth) authentication as a content-only data source — no separate authentication type is required. Before you create the data source, complete the ServiceNow-side setup (the additional service-account read roles and knowledge base configuration) described in [Additional setup for document-level access control (ACLs)](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-acl).

**Important**  
ACL configuration is permanent. You cannot enable ACLs on a data source created without ACL support, and you cannot disable ACLs after they are enabled.

When you create an ACL-enabled data source, use the following settings:
+ Enable **Service Catalogs** if you want catalog ACLs enforced (the four-table model of direct-user and criteria allow and deny lists).
+ Filter to the specific ACL-restricted knowledge bases and catalogs you validated during setup.

The following example shows the `connectorParameters` configuration for an ACL-enabled ServiceNow data source:

```
"connectorParameters": {
    "type": "SERVICENOW",
    "connectorType": "SERVICENOW",
    "version": "1",
    "aclEnabled": true,
    "connectionConfiguration": {
        "secretArn": "{{arn:aws:secretsmanager:region:account-id:secret:secret-name}}",
        "authType": "OAUTH2",
        "hostUrl": "https://{{INSTANCE}}.service-now.com"
    },
    "dataEntityConfiguration": {
        "crawlKnowledgeArticles": true,
        "crawlServiceCatalogs": true
    }
}
```

## ACL resolution rules
<a name="kb-managed-ds-servicenow-acl-rules"></a>

The connector resolves ServiceNow user criteria with the following semantics. Use them to set correct expectations when you validate enforcement.


**ACL resolution rules**  

| Rule | Behavior | 
| --- | --- | 
| Article-level can\_read | Overrides the knowledge-base-level can\_read for that article. | 
| No article criteria | Falls back to the knowledge-base-level can\_read. | 
| cannot\_read (deny) | Always wins over can\_read, at both the knowledge-base level and the article level. | 
| match\_all = true | Intersection — the user must satisfy every clause (AND). | 
| match\_all = false | Union — any one clause is sufficient (OR). | 
| All-empty criterion | Public (ANY\_USER) — readable by everyone. | 
| Advanced or scripted criterion | Resolved by a real-time ACL check at query time, which requires the real-time ACL verifier endpoint. See [Set up the real-time ACL verifier endpoint for advanced criteria](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-acl-verifier). | 
| Role inheritance (sys\_user\_role\_contains) | Resolved — holding a parent role that contains the granted role grants access. | 
| Nested groups (group.parent) | Not resolved — a child-group member is not granted a parent-group criterion. This matches ServiceNow's own behavior and is not a connector limitation. | 
| Catalog items | Four-table model: direct-user allow and deny, and criteria allow and deny, resolved at the item level (no knowledge-base-style fallback). Deny wins. | 

## Verify ACL enforcement at query time
<a name="kb-managed-ds-servicenow-acl-verify"></a>

Enforcement applies when your application passes a verified user identity (the user's email) on the retrieve call. Validate each restricted document with contrasting identities:
+ A user who should have access — the document is returned.
+ A user who should not have access (denied, or not in the criteria) — the document is not returned.
+ An unknown or unauthorized user — nothing is returned (fail-closed).

Confirm both the allow and the deny direction for each restricted document. A denied user who can retrieve a document is a data leak. An authorized user who gets nothing is over-restriction. Both matter.

## Troubleshooting
<a name="kb-managed-ds-servicenow-acl-troubleshooting"></a>

**Note**  
ACL misconfigurations do not produce explicit errors during retrieval. Retrieval fails closed: affected documents are silently omitted, so a query returns fewer or zero results rather than an error.


**ACL-enabled ServiceNow symptoms, causes, and fixes**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| Sync fails with a generic internal error, or a restricted knowledge base crawls zero documents. | The service account isn't granted read access on the restricted knowledge base. As a result, glide.knowman.block\_access\_with\_no\_user\_criteria blocks it. | Add a dedicated can\_read user criterion containing only the service account to each restricted knowledge base. See [Configure restricted knowledge bases](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-acl-kb-config). | 
| The crawl fails with HTTP 403, or criteria resolve to zero members and documents are hidden from everyone. | The service account is missing an ACL-read role. | Grant the ACL-read roles to the service account. See [Add ACL-read roles to the service account](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-acl-roles). | 
| Every article in an access-controlled knowledge base is visible to all users. | The out-of-box "Any User" can\_read criterion is still present, which makes the knowledge base public. | Remove the "Any User" entry from Can Read on each access-controlled knowledge base. See [Configure restricted knowledge bases](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-acl-kb-config). | 
| A user's access changed in ServiceNow, but the new result is not reflected. | User criteria are resolved at crawl time, so a change takes effect only after the content is crawled again. | Trigger a sync (or wait for the next scheduled sync), then retry. | 