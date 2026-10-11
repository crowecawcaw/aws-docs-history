

# Document-level access controls
<a name="kb-managed-ds-zendesk-acl"></a>

**ACL awareness is not authorization**  
Bedrock Managed Knowledge Base provides ACL-aware filtering (it filters results by access permissions) but this is not a security boundary. Bedrock Managed Knowledge Base does not authenticate end users. Your application is responsible for authenticating users and passing verified identity context. Bedrock Managed Knowledge Base cannot verify the authenticity of the user context you provide. As a result, this feature filters results based on the identity you supply, but it does not constitute true authorization. You must not rely on this feature as your only access control mechanism — always pair it with upstream authentication.

Zendesk data sources optionally support document-level access control. When enabled, Bedrock Managed Knowledge Base syncs access control lists (ACLs) from Zendesk during each crawl and verifies each user's permissions at query time. Users only see the articles and community posts they are authorized to access in Zendesk. For the overview of ACL awareness across all connectors, see [Access Control Lists awareness enablement](kb-managed-acl.md).

## How it works
<a name="kb-managed-ds-zendesk-acl-how"></a>

When a user queries a knowledge base that uses an ACL-enabled Zendesk data source, Bedrock Managed Knowledge Base enforces access controls in two stages:
+ **Pre-retrieval filtering** — Bedrock Managed Knowledge Base applies the access control lists that were synced from Zendesk during the last crawl, returning only candidate documents the user (or their groups) is permitted to access.
+ **Real-time verification** — Bedrock Managed Knowledge Base verifies the candidate documents in real time by checking the querying user's current access in Zendesk. Only documents the user is currently authorized to access are included in the response.

This two-stage approach provides document-level access control that stays current even when Zendesk permissions change between syncs.

## Enable ACL awareness
<a name="kb-managed-ds-zendesk-acl-enable"></a>

To enable ACL awareness for a Zendesk data source, set `aclEnabled` to `true` in the `connectorParameters`. ACLs use the same OAuth 2.0 Client Credentials (2LO, or two-legged OAuth) authentication that a content-only Zendesk data source uses. No separate authentication type is required.

**Important**  
ACL configuration is permanent. You cannot enable ACLs on a data source created without ACL support, and you cannot disable ACLs after they are enabled.

```
"connectorParameters": {
    "type": "ZENDESK",
    "connectorType": "ZENDESK",
    "version": "1",
    "aclEnabled": true,
    "connectionConfiguration": {
        "secretArn": "{{arn:aws:secretsmanager:region:account-id:secret:secret-name}}",
        "authType": "OAUTH2",
        "hostUrl": "https://{{yoursubdomain}}.zendesk.com"
    },
    "dataEntityConfiguration": {
        "crawlArticles": true,
        "crawlArticleAttachments": true,
        "crawlCommunityPosts": true
    }
}
```