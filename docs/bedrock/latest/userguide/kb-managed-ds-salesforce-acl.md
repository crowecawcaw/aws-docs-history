

# Document-level access controls
<a name="kb-managed-ds-salesforce-acl"></a>

**ACL awareness is not authorization**  
Bedrock Managed Knowledge Base provides ACL-aware filtering (it filters results by access permissions) but this is not a security boundary. Bedrock Managed Knowledge Base does not authenticate end users. Your application is responsible for authenticating users and passing verified identity context. Bedrock Managed Knowledge Base cannot verify the authenticity of the user context you provide. As a result, this feature filters results based on the identity you supply, but it does not constitute true authorization. You must not rely on this feature as your only access control mechanism — always pair it with upstream authentication.

**Field-level security is not enforced**  
Bedrock Managed Knowledge Base enforces access at the document level. If a user can read a Salesforce record (a Knowledge article or a Document), they receive all of its indexed content, including text from fields that Salesforce field-level security hides from them. Don't rely on field-level security to protect content in crawled records. Keep sensitive text in separate records that are restricted by sharing rules or data categories, or exclude those records from the crawl (for example, with a data category filter).

Salesforce data sources optionally support document-level access control. When enabled, Bedrock Managed Knowledge Base syncs access control lists (ACLs) from Salesforce during each crawl and verifies each user's permissions in Salesforce at query time. Users only see the content they are authorized to access in Salesforce. For the overview of ACL awareness across all connectors, see [Access Control Lists awareness enablement](kb-managed-acl.md).

## How it works
<a name="kb-managed-ds-salesforce-acl-how"></a>

When a user queries a knowledge base that uses an ACL-enabled Salesforce data source, Bedrock Managed Knowledge Base enforces access controls in two stages:
+ **Pre-retrieval filtering**: Bedrock Managed Knowledge Base applies the access control lists that were synced from Salesforce during the last crawl, returning only candidate documents the user is permitted to access.
+ **Real-time verification**: Bedrock Managed Knowledge Base checks each candidate document with Salesforce as the querying user. Salesforce applies all of its own access rules, including sharing rules, role hierarchy, ownership, data category visibility, and folder access. Only documents the user can currently read are included in the response.

Real-time verification keeps results current when Salesforce permissions change between syncs.

## Supported content
<a name="kb-managed-ds-salesforce-acl-content"></a>

The following table shows how access is checked for each type of Salesforce content.


**Salesforce content and access checks**  

| Content | Access is checked against | 
| --- | --- | 
| Published Knowledge articles | The user's access to the article | 
| Archived Knowledge articles | The user's access to the archived article version | 
| Documents (folder-stored files) | The user's access to the Document's folder | 
| Knowledge article attachments | The user's access to the attachment | 

Each attachment is checked on its own, so a user sees an attachment exactly when Salesforce lets them read it, which can differ from their access to its parent article.

To see archived articles, the querying user needs the Salesforce **View Archived Articles** permission.

Document-level access controls apply to internal Salesforce users. Experience Cloud users (customer and partner community users) are not supported, and queries made on their behalf return no results from this data source.

**Note**  
Access is checked per record, not per field. Field-level security doesn't limit which parts of a readable record a user receives.

## Enable ACL awareness
<a name="kb-managed-ds-salesforce-acl-enable"></a>

Complete [Set up OAuth 2.0 JWT Bearer authentication for Salesforce document-level access controls](kb-managed-salesforce-jwt-bearer-setup.md) first. Then set `aclEnabled` to `true` in the `connectorParameters` and set `authType` to `OAUTH2_WITH_JWT_BEARER`. The two settings must be used together: the `OAUTH2_WITH_JWT_BEARER` authentication type is available only with ACL enabled, and an ACL-enabled data source that uses `OAUTH2` is rejected.

**Important**  
ACL configuration is permanent. You cannot enable ACLs on a data source created without ACL support, and you cannot disable ACLs after they are enabled.

```
"connectorParameters": {
    "type": "SALESFORCE",
    "connectorType": "SALESFORCE",
    "version": "1",
    "aclEnabled": true,
    "connectionConfiguration": {
        "secretArn": "{{arn:aws:secretsmanager:region:account-id:secret:secret-name}}",
        "authType": "OAUTH2_WITH_JWT_BEARER",
        "hostUrl": "https://{{your-domain}}.my.salesforce.com"
    },
    "dataEntityConfiguration": {
        "crawlKnowledgeArticles": true,
        "crawlKnowledgeArticleAttachments": true,
        "crawlArchiveKnowledgeArticleItems": true,
        "crawlDocuments": true
    }
}
```

When you update the data source with the [UpdateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateDataSource.html) operation, include `"aclEnabled": true` in every request.

## Query an ACL-enabled Salesforce data source
<a name="kb-managed-ds-salesforce-acl-query"></a>

Pass the user's email address in `userContext.userId` on `Retrieve`, `AgenticRetrieveStream`, and `GetDocumentContent` requests. For the request syntax, see [ACL-aware retrieval on managed knowledge bases](kb-test-retrieve-acl.md).
+ **Email matching**: The email address is matched against the Salesforce user's **Email** field, without regard to case. Email aliases (for example, `jane+support@example.com`) are not normalized.
+ **User context required**: If you omit `userContext`, the Salesforce data source returns no results. Content from data sources without ACLs in the same knowledge base is returned to all users.
+ **Fewer results**: Responses can contain fewer results than you requested, because documents are filtered after ranking.
+ **Checking a user's access**: `CheckIngestedDocumentAcl` and `GetIngestedDocumentAcl` evaluate only the ACL synced at the last crawl and don't run the real-time check. To confirm what a user can get, call `GetDocumentContent` with `userContext`.

## When permission changes take effect
<a name="kb-managed-ds-salesforce-acl-changes"></a>
+ Access removals and record-level changes (sharing rules, group membership, role, folder sharing, and data category visibility) take effect within a few minutes.
+ New object-level read access to Knowledge or Documents, including access for new users, takes effect after the next successful sync.
+ New or edited content appears after the next sync.

Real-time verification can remove access granted at the last sync, but it can't add access.

## API usage
<a name="kb-managed-ds-salesforce-acl-api-usage"></a>

Real-time verification makes Salesforce API calls on behalf of querying users. These calls count toward your org's daily API request limit, together with the crawl and your other integrations. Factor query volume into your org's API capacity planning.

## Troubleshooting
<a name="kb-managed-ds-salesforce-acl-troubleshooting"></a>

**Note**  
ACL misconfigurations do not produce explicit errors during retrieval. Retrieval fails closed: affected documents are omitted, so a query returns fewer or zero results rather than an error.


**ACL-enabled Salesforce symptoms, causes, and fixes**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| No user gets results. | The private key doesn't match a certificate on the app, users aren't pre-authorized, instanceType doesn't match the org type, or session IP locking is on. | Review the steps in [Set up OAuth 2.0 JWT Bearer authentication for Salesforce document-level access controls](kb-managed-salesforce-jwt-bearer-setup.md). | 
| One user gets no results. | The email address doesn't match the user's Salesforce Email field or is shared by more than one active user; the user is inactive or frozen, isn't pre-authorized, lacks the API Enabled permission, or is an Experience Cloud user; or login IP ranges or login hours block the user. | Correct the user's email address, status, pre-authorization, or permissions in Salesforce. | 
| A new user gets no results. | Access was granted after the last sync. | Run a sync. | 