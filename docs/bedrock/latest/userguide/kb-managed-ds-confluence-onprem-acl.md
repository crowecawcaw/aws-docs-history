

# Document-level access controls
<a name="kb-managed-ds-confluence-onprem-acl"></a>

**ACL awareness is not authorization**  
Bedrock Managed Knowledge Base provides ACL-aware filtering, not a security boundary. Bedrock Managed Knowledge Base does not authenticate end users — your application is responsible for authenticating users and passing verified identity context. Because Bedrock Managed Knowledge Base cannot verify the authenticity of the user context you provide, this feature filters results based on the identity you supply but does not constitute true authorization. You must not rely on this feature as a sole access control mechanism without upstream authentication.

Confluence Data Center data sources optionally support document-level access control. When enabled, Bedrock Managed Knowledge Base syncs access control lists (ACLs) from your Confluence Data Center instance during each crawl and verifies each user's permissions at query time, so users only see results from documents they are authorized to access in Confluence. For the overview of ACL awareness across all connectors, see [Access Control Lists awareness enablement](kb-managed-acl.md).

## How it works
<a name="kb-managed-ds-confluence-onprem-acl-how"></a>

When a user queries a knowledge base that uses an ACL-enabled Confluence Data Center data source, Bedrock Managed Knowledge Base enforces access controls in two stages:
+ **Pre-retrieval filtering** — Bedrock Managed Knowledge Base applies the access control lists that were synced from Confluence during the last crawl, returning only candidate documents the user (or their groups) is permitted to access.
+ **Real-time verification** — Bedrock Managed Knowledge Base verifies the candidate documents in real time by checking the querying user's current access in Confluence. Only documents the user is currently authorized to access are included in the response.

This two-stage approach provides document-level access control that stays current even when Confluence permissions change between syncs.

## What is crawled
<a name="kb-managed-ds-confluence-onprem-acl-crawl"></a>

When ACLs are enabled, Bedrock Managed Knowledge Base crawls the following permission structures from Confluence:
+ **Spaces** — Space permissions apply to all documents in the space by default.
+ **Pages** — Pages can be restricted to specific users and groups. Nested pages inherit restrictions from the parent page.
+ **Blogs** — Blog posts can be restricted to specific users and groups.
+ **Attachments** — Files attached to pages or blog posts inherit the access controls of their parent document.

**Note**  
Access control is resolved by user email. During a crawl, if a user in a document's restriction has no email that can be resolved from your Confluence instance, that user is omitted from the document's synced ACL and the document is still indexed, provided the restriction retains at least one resolvable user or group. If every principal on a restriction is unresolvable, the document fails closed and is not indexed, so that it is never returned to an unauthorized user.

**Note**  
Confluence Data Center returns at most 200 entries per restriction list. If a page, an inherited ancestor page, or a space restricts access to more than 200 users, or to more than 200 groups, Bedrock Managed Knowledge Base syncs only the first 200 entries of that list. This does not cause over-sharing, but a legitimately authorized user whose entry falls beyond the first 200 might be excluded from the synced ACL and can be wrongly denied results for that document. To avoid this, keep individual restriction lists at or below 200 entries; grant access with groups rather than enumerating many individual users, so that a single group entry represents many people.

## Enable ACL awareness
<a name="kb-managed-ds-confluence-onprem-acl-enable"></a>

To enable ACL awareness for a Confluence Data Center data source, set `aclEnabled` to `true` in the `connectorParameters`. Use the `BASIC` or `PERSONAL_TOKEN` auth type with a secret that holds credentials for a Confluence account that has administrator permissions. These administrator permissions are required for identity crawling and real-time verification.

**Important**  
ACL configuration is permanent. If you omit `aclEnabled`, it defaults to `false`. You cannot enable ACLs on a data source created without ACL support, and you cannot disable ACLs after they are enabled.

## Real-time access verification
<a name="kb-managed-ds-confluence-onprem-acl-realtime"></a>

Bedrock Managed Knowledge Base verifies each candidate document against your Confluence Data Center instance at query time entirely server-side, using the credentials configured in the secret over your VPC configuration — there is no end-user sign-in. The connector checks the querying user's current space, page, and blog restrictions, so access changes made since the last crawl are honored.

## Verify your configuration
<a name="kb-managed-ds-confluence-onprem-acl-verify"></a>

You can validate your credentials independently of a retrieve request. Perform each of the following checks:

1. **Confluence content access (crawl)**:
   + Using the credentials from the secret (`BASIC` username and password, or a personal access token), call the Confluence REST API on your instance (for example, list spaces) and confirm it returns HTTP 200.

1. **Identity resolution (identity crawling and real-time verification)**:
   + Confirm the configured account has administrator permissions on the Confluence Data Center instance.
   + Using those credentials, call the Confluence user and group REST APIs on your instance and confirm they return your users and groups.

## Troubleshooting
<a name="kb-managed-ds-confluence-onprem-acl-troubleshooting"></a>

**Note**  
ACL misconfigurations do not produce explicit errors during retrieval. Retrieval fails closed: affected documents are silently omitted, so a query returns fewer or zero results rather than an error. Use the verification checks above to diagnose these issues.


**ACL-enabled Confluence Data Center symptoms, causes, and fixes**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| Retrieve returns 0 results, but the user has access in Confluence. | The configured account lacks administrator permissions, so user and group restrictions cannot be resolved, or the user's email cannot be resolved from the instance. | Confirm the account has administrator permissions and that users have a resolvable email in Confluence. | 
| Crawl or sync fails. | The username or password (or personal access token) is invalid, or the Confluence host is unreachable from the VPC configuration. | Verify the credentials in the secret and confirm the VPC configuration can reach the Confluence host. | 
| One specific user is denied results for a document that restricts access to a very large number of users or groups, while other users on the same document have access. | The document (or an inherited ancestor or space) restricts access to more than 200 users, or more than 200 groups, and the user's entry falls beyond the first 200 that Confluence returns per restriction list. | Keep each restriction list at or below 200 entries. Grant access with groups instead of enumerating many individual users, so a single group entry covers many people. | 
| All users are denied after previously working. | The password or personal access token expired or was revoked. | Rotate the affected credentials in the secret. | 