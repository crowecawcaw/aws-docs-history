

# Document-level access controls

**ACL awareness is not authorization**  
Bedrock Managed Knowledge Base provides ACL-aware filtering (it filters results by access permissions) but this is not a security boundary. Bedrock Managed Knowledge Base does not authenticate end users. Your application is responsible for authenticating users and passing verified identity context. Bedrock Managed Knowledge Base cannot verify the authenticity of the user context you provide. As a result, this feature filters results based on the identity you supply, but it does not constitute true authorization. You must not rely on this feature as your only access control mechanism — always pair it with upstream authentication.

Dropbox data sources that use the `TEAM_ADMIN` authentication type optionally support document-level access control. When enabled, Bedrock Managed Knowledge Base syncs each file's permissions and the team's group memberships from Dropbox during each crawl, and verifies each user's access at query time. Users only see the files and Paper documents they can open in Dropbox. For the overview of ACL awareness across all connectors, see [Access Control Lists awareness enablement](kb-managed-acl.md).

Document-level access control is not available with `OAUTH2`. A single user's token cannot read who else has access to a file across the team.

## How it works
<a name="kb-managed-ds-dropbox-acl-how"></a>

When a user queries a knowledge base that uses an ACL-enabled Dropbox data source, Bedrock Managed Knowledge Base enforces access controls in two stages:
+ **Pre-retrieval filtering** — Bedrock Managed Knowledge Base applies the access control lists that were synced from Dropbox during the last crawl, returning only candidate documents the user (or their groups) is permitted to access.
+ **Real-time verification** — Bedrock Managed Knowledge Base verifies the candidate documents in real time by checking the querying user's current access in Dropbox, using the data source's team credentials to act as that user. Only documents the user is currently authorized to access are included in the response.

This two-stage approach provides document-level access control that stays current when access is removed in Dropbox between syncs.

The principal is the user's email address. Your application must pass the authenticated user's email as the identity on the retrieve call. The email must match the user's Dropbox team member email. Unknown users get nothing. This behavior is called *fail-closed*: when the system cannot confirm access, it denies access by default rather than granting it.

## What is crawled
<a name="kb-managed-ds-dropbox-acl-crawl"></a>

When ACLs are enabled, Bedrock Managed Knowledge Base crawls the following permission structures from Dropbox:
+ The members of each file: users and groups the file is shared with directly.
+ The members of each shared folder and team folder, which apply to every file inside them. Inheritance stops at a folder whose access is set so that it does not inherit members from its parent folder.
+ The owner of each file in a member's own folder.
+ Team groups and their members.

The following do not grant access in the knowledge base:
+ Suspended and removed team members, and users who have been invited to the team but have not joined.
+ Shared links, including "anyone with the link" access. A link is not a member grant, so it is not reflected.

A file that no active user or group can read is skipped and is not indexed.

## Enable ACL awareness
<a name="kb-managed-ds-dropbox-acl-enable"></a>

To enable ACL awareness for a Dropbox data source, set `authType` to `TEAM_ADMIN` and `aclEnabled` to `true` in the `connectorParameters`. If you omit `aclEnabled` on a `TEAM_ADMIN` data source, it defaults to `true`.

Before you create the data source, grant the `groups.read` scope on your Dropbox app, in addition to the scopes that every `TEAM_ADMIN` data source needs, and issue the refresh token after granting it. See [Step 2: Grant scopes](kb-managed-dropbox-auth-setup.md#kb-managed-dropbox-auth-step2). The real-time check uses the same secret, so no additional credentials are required.

**Important**  
ACL configuration is permanent. You cannot enable ACLs on a data source created without ACL support, and you cannot disable ACLs after they are enabled. Because the default for `TEAM_ADMIN` is `true`, a `TEAM_ADMIN` data source created without an explicit `aclEnabled` value is permanently ACL-enabled.

```json
"connectorParameters": {
    "type": "DROPBOX",
    "connectorType": "DROPBOX",
    "version": "1",
    "aclEnabled": true,
    "connectionConfiguration": {
        "secretArn": "{{arn:aws:secretsmanager:region:account-id:secret:secret-name}}",
        "authType": "TEAM_ADMIN"
    },
    "dataEntityConfiguration": {}
}
```

## When permission changes take effect
<a name="kb-managed-ds-dropbox-acl-timing"></a>

The following table describes when a permission change in Dropbox takes effect in the knowledge base.


**When Dropbox permission changes take effect**  

| Change in Dropbox | When the knowledge base reflects it | 
| --- | --- | 
| A user loses access to a file (unshared, removed from a folder or group, suspended, or removed from the team) | At query time, through real-time verification | 
| A user gains access to a file (newly shared, added to a folder or group) | After the next sync | 
| A user gains access to a file through a group membership change | After the next sync | 

## Verify ACL enforcement at query time
<a name="kb-managed-ds-dropbox-acl-verify"></a>

Enforcement applies when your application passes a verified user identity (the user's email) on the retrieve call. Validate each restricted document with contrasting identities:
+ A user who can open the file in Dropbox — the document is returned.
+ A team member who cannot open the file — the document is not returned.
+ An unknown user, or an email that is not an active member of the team — nothing is returned (fail-closed).

Confirm both the allow and the deny direction for each restricted document. A denied user who can retrieve a document is a data leak. An authorized user who gets nothing is over-restriction. Both matter.

## Troubleshooting Dropbox ACL awareness
<a name="kb-managed-ds-dropbox-acl-troubleshooting"></a>

**Note**  
ACL misconfigurations do not produce explicit errors during retrieval. Retrieval fails closed: affected documents are silently omitted, so a query returns fewer or zero results rather than an error.


**ACL-enabled Dropbox symptoms, causes, and fixes**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| CreateDataSource rejects aclEnabled. | The data source uses OAUTH2. | Use TEAM\_ADMIN with a team-linked refresh token. See [Set up authentication for Dropbox](kb-managed-dropbox-auth-setup.md). | 
| The sync fails with a permissions error when ACLs are enabled. | The app is missing groups.read, or the refresh token was issued before it was granted. | Grant the scope, then authorize the app again and update refreshToken in the secret. | 
| A user gets no results for files they can open in Dropbox. | The email your application passes does not match the user's Dropbox team member email, or the user can open the file only through a shared link. | Pass the user's Dropbox team email. Share the file or its folder with the user or a group they belong to. | 
| A user gets no results at all, even though their email matches their Dropbox team member email. | The user has not verified their email address with Dropbox. Dropbox refuses access checks for a member with an unverified email. | Ask the user to verify their email address in Dropbox, then retry. | 
| A user cannot find a file that was shared with them recently. | New access is synced at crawl time. | Trigger a sync (or wait for the next scheduled sync), then retry. | 