

# Synchronize a skill from GitHub

 AWS Agent Registry can read a skill from a folder in a GitHub repository: only the folder’s SKILL.md, or the whole folder as a skill package. The registry reads the folder at a branch or tag when you create the record, when you change its source, and when you call `UpdateRegistryRecord` with `triggerSynchronization` set to `true`.

The registry reads the repository with the access of a GitHub user who authorizes it, through an AgentCore Identity OAuth 2.0 credential provider for your GitHub OAuth App. The first time that you synchronize with a credential provider, a GitHub user approves access in a browser, and the record waits in `CREATE_PENDING_AUTH` or `UPDATE_PENDING_AUTH` status until the approval completes.

## Supported GitHub hosts
<a name="registry-skill-sync-github-hosts"></a>


| Host | Example source URL | 
| --- | --- | 
| GitHub.com, including organizations on GitHub Enterprise Cloud |  `https://github.com/octo-org/skills/tree/main/skills/my-skill`  | 
| GitHub Enterprise Cloud with data residency (GHE.com) |  `https://octocorp.ghe.com/octo-org/skills/tree/main/skills/my-skill`  | 
| GitHub Enterprise Server that is reachable from the internet |  `https://github.example.com/octo-org/skills/tree/main/skills/my-skill`  | 

**Important**  
 AWS Agent Registry supports GitHub Enterprise Server only through a public endpoint: one that is reachable from the internet over HTTPS (port 443), with a publicly trusted certificate. Private connectivity isn’t supported. The registry can’t synchronize from a server that is reachable only from a VPC or an on-premises network, or only through a private DNS name or a private IP address. For the full requirements, see [Make GitHub Enterprise Server reachable](#registry-skill-sync-github-ghes).

The console accepts a folder URL on any of these hosts. For GHE.com and GitHub Enterprise Server, the credential provider must be a custom OAuth 2.0 provider, because only a custom provider can point at that host. For more information, see [Create an OAuth App and a credential provider](#registry-skill-sync-github-provider).

## Source URL and mode
<a name="registry-skill-sync-github-source"></a>

Set the source in `source.fromUrl.url`, and set `repositoryProvider` to `GITHUB` in `descriptors.agentSkillsDefinition.additionalData`. The registry treats an `https://` source as a GitHub source only when `repositoryProvider` is set, regardless of the host.

The URL names the skill’s folder, in the form `https://<host>/<owner>/<repo>/tree/<branch-or-tag>/<path>`:
+ It names a folder in the repository, after the branch or tag. The registry doesn’t accept a repository URL without a folder or a `/blob/` URL for a file.
+ The branch or tag can contain slashes, such as `release/v2`. It can’t be a commit SHA.
+ The branch or tag must match exactly one branch or one tag. If the URL can be read as more than one branch or tag, the synchronization fails. To choose one, start it with `refs/heads/` for a branch or `refs/tags/` for a tag, for example `https://github.com/octo-org/skills/tree/refs/tags/v1.2.0/skills/my-skill`.
+ It has no port other than 443, no user name or password, and no query string or fragment.
+ The host is a DNS name, not an IP address. Hosts such as `api.github.com`, `gist.github.com`, and `raw.githubusercontent.com` don’t serve repositories and aren’t accepted.

The folder path and each part of the branch or tag and path have maximum lengths. For the limits, see [Skill package limits](bedrock-agentcore-limits.md#registry-skill-package-limits).

The member that holds the source determines what the registry reads:


| Member | What the registry reads | 
| --- | --- | 
|  `skillMd.source`  | Only the folder’s `SKILL.md` file. The file name must be exactly `SKILL.md`. Don’t add the file name to the URL. The record gets the text in `skillMd.data`, and no package. | 
|  `skillPackage.source`  | Every file in the folder and its subfolders. The registry builds a skill package from them with SKILL.md at the root of the archive, and validates it as described in [Skill package format and validation](registry-skill-package-format.md). Because SKILL.md is at the root, the folder’s name doesn’t have to match the skill’s `name`. The folder must have a `SKILL.md` or `skill.md` file at its top, and can’t contain symbolic links, Git submodules, or Git Large File Storage (LFS) files. | 

Each synchronization resolves the branch or tag again and reads the commit that it points to at that time. The record shows the commit in `synchronizedSource.gitHub.commitId`.

## Before you begin
<a name="registry-skill-sync-github-prereqs"></a>

### Create an OAuth App and a credential provider
<a name="registry-skill-sync-github-provider"></a>

**Note**  
 AWS Agent Registry reads GitHub through a GitHub OAuth App. GitHub Apps aren’t supported.

1. In GitHub, create a GitHub OAuth App in your account or organization, on the same host as your repositories. For GitHub Enterprise Server, create it on the server.

1. In AgentCore Identity, create an OAuth 2.0 credential provider for the OAuth App, in the same AWS account and Region as the registry. For more information about credential providers, see [Manage credential providers with AgentCore Identity](identity-outbound-credential-provider.md).
   + For `github.com`, create a GitHub credential provider. For more information, see [GitHub](identity-idp-github.md).
   + For GHE.com and GitHub Enterprise Server, create a custom credential provider with your host’s OAuth authorization and token endpoints, for example `https://github.example.com/login/oauth/authorize` and `https://github.example.com/login/oauth/access_token`. For more information, see [Add OAuth client using custom provider](identity-add-oauth-client-custom.md).

1. In the OAuth App settings, set **Authorization callback URL** to the callback URL of the credential provider. The two URLs must match exactly.

**Your responsibility: match the credential provider to the source host**  
 AWS Agent Registry knows the GitHub host from the source URL. It doesn’t know the host of the credential provider’s authorization and token endpoints, so it can’t check that the two hosts match. It sends the access token to the source’s host. If the source names a different host from the provider, a token that one GitHub host issued goes to the other host.  
Use a credential provider for the same GitHub host as the source. Check both before you create or update a GitHub source.
Limit who can create and update records in the registry (`agent-registry:CreateRegistryRecord` and `agent-registry:UpdateRegistryRecord`), and who can use the credential provider, because they choose the source host.
Give an authorization link only to the GitHub user who approves access, and approve only links that you expect, from a person or an application that you trust. Don’t share authorization links, for example in tickets, chats, or logs. The GitHub approval page shows the provider’s host, not the host that receives the token.

### Configure the source’s credentials
<a name="registry-skill-sync-github-credential-config"></a>

A GitHub source takes exactly one entry in `credentialProviderConfigurations`, of type `OAUTH`:
+  `providerArn` — The ARN of the credential provider. It must be in the registry’s account and Region.
+  `grantType` — The OAuth grant type. It must be `AUTHORIZATION_CODE`. A GitHub OAuth App doesn’t support the client credentials grant.
+  `scopes` — The GitHub OAuth scopes to request. To read private repositories, request `repo`. GitHub grants read and write access to your repositories for that scope. To read only public repositories, request no scopes.
+  `customParameters` — (Optional) Additional key-value parameters for the OAuth request.
+  `returnUrl` — (Optional) The URL that the user’s browser goes to after the user approves access. For more information, see [Choose where the user returns](#registry-skill-sync-github-return-url).

### Check your organization’s policies
<a name="registry-skill-sync-github-org"></a>

The authorized GitHub user must be able to read the repository. If the repository’s organization enforces SAML single sign-on, the user must authorize the OAuth App’s access to the organization through single sign-on. If the organization restricts OAuth App access, an organization owner must approve the OAuth App.

### Make GitHub Enterprise Server reachable
<a name="registry-skill-sync-github-ghes"></a>

The registry reaches GitHub Enterprise Server over the internet. The server must meet these requirements:
+ Its host name is a public DNS name that resolves only to public IP addresses. Use the host name that the server is configured with.
+ Its host name is in a domain that you own. It can’t be in a domain that AWS owns, such as `amazonaws.com` or `cloudfront.net`, or be a reserved or internal name, such as one that ends in `.internal` or `.corp`.
+ It accepts HTTPS connections on port 443 from the internet.
+ Its TLS certificate is issued by a public certificate authority for the server’s host name.
+ Its API answers directly, with no proxy or sign-in page in front of it. The registry doesn’t follow redirects.
+ For a full-package source, the server’s archive host also meets these requirements. With subdomain isolation turned on, that host is the `codeload` subdomain of the server’s host name.

### Set up permissions
<a name="registry-skill-sync-github-permissions"></a>

When a request sets or synchronizes a GitHub source, the registry calls AgentCore Identity with the caller’s credentials. The caller must be an IAM role or IAM user in the account that owns the registry. In addition to `agent-registry:CreateRegistryRecord` or `agent-registry:UpdateRegistryRecord`, the caller needs the following permissions. Replace the Region, account ID, and `my-github-provider` with your values. The registry’s workload identity is named `registry-<registryId>`, so its ARN is `arn:aws:bedrock-agentcore:<region>:<account-id>:workload-identity-directory/default/workload-identity/registry-<registryId>`.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "GetWorkloadAccessTokenForRegistry",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetWorkloadAccessTokenForUserId",
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default/workload-identity/registry-*"
      ]
    },
    {
      "Sid": "GetGitHubToken",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceOauth2Token",
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default/workload-identity/registry-*",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default/oauth2credentialprovider/my-github-provider"
      ]
    },
    {
      "Sid": "ReadGitHubProviderClientSecret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:bedrock-agentcore-identity!default/oauth2/my-github-provider-*"
    }
  ]
}
```

AgentCore Identity reads the credential provider’s client secret with the caller’s credentials, so the caller needs `secretsmanager:GetSecretValue` on it.

If the registry is encrypted with a customer managed key, a request that sets or synchronizes a full-package source also needs `kms:GenerateDataKey` on the registry’s key. For more information, see [Set customer managed key policy](registry-kms-key-policy.md). To complete authorizations in the console, the IAM role or user also needs the permissions in [IAM Permissions](registry-iam-permissions.md).

## Authorize GitHub access
<a name="registry-skill-sync-github-authorization"></a>

The registry asks a GitHub user to approve access when no approval exists yet for the following combination:
+ The registry
+ The IAM role or IAM user that makes the request (for a role, the role itself, not the role session)
+ The GitHub host
+ The credential provider
+ The scopes and custom parameters

Your later requests with the same combination reuse the approval, for any record in the registry, and need no browser step. Another IAM role or user in the same account needs its own approval.

**Note**  
GitHub issues at most 10 tokens for each combination of GitHub user, OAuth App, and scopes. Each approval gets its own token, and so does each request with `forceAuthentication`. Other applications that use the same OAuth App count toward the same limit. When the user approves access more than 10 times, GitHub revokes one of the earlier tokens without notice: the oldest token that was never used, or otherwise the least recently used token. Records that use the revoked token fail their next synchronization, and the user must approve access again. For more information, see [Creating multiple tokens for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#creating-multiple-tokens-for-oauth-apps) on the GitHub Docs website.

When an approval is needed, the flow works as follows:

1. You call `CreateRegistryRecord`, or `UpdateRegistryRecord` with a new source or with `triggerSynchronization`. The response has the status `CREATE_PENDING_AUTH` or `UPDATE_PENDING_AUTH` and an `authorizationData.oauth2` member. `authorizationData` is returned only in this response: `GetRegistryRecord` and `ListRegistryRecords` never return it. It has these members:
   +  `authorizationUrl` — The URL that the user opens to approve access. Treat it as sensitive, and give it only to the user who approves access.
   +  `userId` — The AgentCore Identity user ID that the approval is for.
   +  `authorizationAttemptId` — The ID of this authorization attempt.
   +  `expiresAt` — When the link expires. The link can stop working shortly before this time.

1. The user opens `authorizationUrl` and approves access on GitHub.

1. AgentCore Identity sends the user’s browser to the return URL, with a `session_id` query parameter.

1. The AWS Agent Registry console or your application completes the authorization, as described in [Choose where the user returns](#registry-skill-sync-github-return-url).

1. The registry synchronizes every record that waits for this approval. The records move to `CREATING` or `UPDATING`, and then to `DRAFT`, or to `CREATE_FAILED` or `UPDATE_FAILED`.

If an approval for the same combination is already in progress, the response returns the same link and expiry time. That link returns the user wherever the request that started the approval chose: its `returnUrl`, or the console. A changed `returnUrl` applies to the next approval that the record starts.

If a response has a pending status but no `authorizationData`, call `UpdateRegistryRecord` with `triggerSynchronization` to get the link.

### Choose where the user returns
<a name="registry-skill-sync-github-return-url"></a>

 **Without `returnUrl` **, AgentCore Identity returns the user to the registry’s page in the AWS Agent Registry console. Sign in to the console as the same IAM role or IAM user that started the authorization. The console asks **Finish authorizing GitHub access for this registry?** Choose **Complete**, and the console completes the authorization.

 **With `returnUrl` **, AgentCore Identity returns the user to your application. Your application verifies its own signed-in user, and then completes the authorization by calling the AgentCore Identity [CompleteResourceTokenAuth](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CompleteResourceTokenAuth.html) operation with these values:
+  `sessionUri` — The `session_id` query parameter of the request that your application receives.
+  `userIdentifier.userId` — The `userId` from `authorizationData.oauth2`, which your application stored for this user when it started the authorization.

For information about how to build this endpoint securely, see [OAuth 2.0 authorization URL session binding](oauth2-authorization-url-session-binding.md). The IAM principal that your application uses must be in the account that owns the registry. It needs `bedrock-agentcore:CompleteResourceTokenAuth` on the registry’s workload identity and its directory, the token vault, and the credential provider. It also needs `secretsmanager:GetSecretValue` on the credential provider’s client secret, because AgentCore Identity reads the secret with your application’s credentials.

The following example shows the call that a handler makes, with the AWS SDK for Python (Boto3):

```python
import boto3

agentcore = boto3.client('bedrock-agentcore', region_name='us-east-1')


def complete_registry_authorization(session_id, signed_in_user):
    # Look up the userId that you stored for this user from authorizationData.oauth2,
    # and refuse the request if this user didn't start an authorization.
    user_id = load_pending_registry_authorization(signed_in_user)
    if user_id is None:
        raise PermissionError('No GitHub authorization in progress for this user')

    agentcore.complete_resource_token_auth(
        sessionUri=session_id,
        userIdentifier={'userId': user_id},
    )
```

 `returnUrl` must meet these rules:
+ It uses the `https` scheme, written in lowercase, with a public domain name, not an IP address. Only `localhost`, `127.0.0.1`, and `[::1]` can also use `http`.
+ It has no user name, password, or fragment. A query string is allowed.
+ It’s no longer than 2,048 characters.

### Timing and pending records
<a name="registry-skill-sync-github-pending"></a>
+ The authorization link expires 10 minutes after the approval starts, at the time in `expiresAt`. A request that joins an approval in progress gets less time.
+ Approve access before the link expires. If the approval isn’t completed by then, the record moves to `CREATE_FAILED` or `UPDATE_FAILED`, and `statusReason` says that the authorization expired.
+ If another of your requests restarts the same approval, waiting records follow the new link, for at most 30 minutes in total. If the approval fails or still isn’t completed, the record moves to `CREATE_FAILED` or `UPDATE_FAILED`, and `statusReason` says why.
+ To get a new link, for example after the link expired or was lost, call `UpdateRegistryRecord` with `triggerSynchronization` set to `true`. The record gets a new link and a new wait.
+ While a record is in `CREATE_PENDING_AUTH` or `UPDATE_PENDING_AUTH` status, you can read, deprecate, and delete it. Other updates fail with a `ConflictException`, except an update that synchronizes a GitHub source: one that sets `triggerSynchronization` (with or without `forceAuthentication`), or sets a new or changed GitHub source.
+ A record in `CREATE_PENDING_AUTH` has no package yet. For a record in `UPDATE_PENDING_AUTH`, `GetRegistryRecord` keeps returning a download URL for its last package, unless the update replaces an uploaded package with a synchronized one.

## Create a record that synchronizes from GitHub
<a name="registry-skill-sync-github-create"></a>

### Console
<a name="registry-skill-sync-github-create-console"></a>

1. Open the registry detail page in the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#).

1. In the **Registry records** section, choose **Create record**.

1. In the **Record source** section, choose **Synchronize from source**.

1. In the **Record details** section, for **Type**, choose **Skills**. The **Descriptor** is set to **Agent skills definition**.

1. For **Source**, choose **GitHub**.

1. For **Content type**, choose **Skill markdown** to read the folder’s SKILL.md, or **Skill package** to read the whole folder as a skill package.

1. For **GitHub folder**, enter the folder URL, in the form `https://<host>/<owner>/<repo>/tree/<branch>/<path>`. Name a branch or a tag after `/tree/`, not a commit SHA. The console accepts a URL on any of the hosts in [Supported GitHub hosts](#registry-skill-sync-github-hosts).

1. For **Credential provider**, choose the credential provider for your OAuth App.

   The console selects **OAuth client** for **Credential type** and offers no other option, because the registry reads a GitHub folder with a GitHub user’s token. The provider list shows every OAuth 2.0 credential provider in your account, but you can select only a provider of the **GithubOauth2** or **CustomOauth2** vendor. Use a **GithubOauth2** provider for `github.com`, and a **CustomOauth2** provider for GHE.com or GitHub Enterprise Server. You can also enter a provider ARN.

1. For **Repository access**, choose **Private repository** to request the `repo` scope, or **Public repository** to request no scopes.

1. (Optional) For **Return URL**, enter your application’s return URL. Leave it empty to return to this registry’s page in the console.

1. (Optional) In the **Tags** section, add tags to the record.

1. Choose **Create record**.

If a GitHub user must approve access, the console shows **Authorize on GitHub** and the time when the link expires, and the record has the status **Create pending authorization**. Choose **Authorize on GitHub**, and approve access on GitHub. When GitHub returns you to the console, choose **Complete**. If you no longer have the link, choose **Manage**, choose **Synchronization**, and then choose **Authorize on GitHub** in the notification.

The record takes its name and description from the `name` and `description` in SKILL.md, and takes them again on every synchronization.

### AWS CLI
<a name="registry-skill-sync-github-create-cli"></a>

Save the descriptors in a file, such as `descriptors.json`. This example synchronizes the folder’s SKILL.md from a private repository on `github.com`:

```json
{
  "agentSkillsDefinition": {
    "additionalData": {
      "repositoryProvider": "GITHUB",
      "skillMd": {
        "source": {
          "fromUrl": {
            "url": "https://github.com/octo-org/skills/tree/main/skills/my-skill",
            "credentialProviderConfigurations": [
              {
                "credentialProviderType": "OAUTH",
                "credentialProvider": {
                  "oauthCredentialProvider": {
                    "providerArn": "arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default/oauth2credentialprovider/my-github-provider",
                    "grantType": "AUTHORIZATION_CODE",
                    "scopes": ["repo"]
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

To synchronize the whole folder as a package, use `skillPackage` in place of `skillMd`. For GHE.com or GitHub Enterprise Server, use your host in the URL and a credential provider for that host. To return the user to your application, add `"returnUrl": "https://app.example.com/registry/oauth/callback"` to `oauthCredentialProvider`.

Create the record:

```bash
aws agent-registry-control create-registry-record \
  --registry-id <registryId> \
  --name "my-skill" \
  --record-type SKILL \
  --record-version "1.0" \
  --descriptors file://descriptors.json \
  --region us-east-1
```

If a GitHub user must approve access, the response looks like the following:

```json
{
    "recordArn": "arn:aws:agent-registry:us-east-1:111122223333:registry/AbCdEfGh1234/record/Rec123456789",
    "status": "CREATE_PENDING_AUTH",
    "authorizationData": {
        "oauth2": {
            "authorizationUrl": "<authorization URL>",
            "userId": "<user ID>",
            "authorizationAttemptId": "a1B2c3D4e5",
            "expiresAt": "2026-11-19T18:10:00Z"
        }
    }
}
```

Open `authorizationUrl` in a browser and approve access on GitHub, and then complete the authorization in the console or in your application. If the approval already exists, the status is `CREATING` and the response has no `authorizationData`.

### AWS SDK
<a name="registry-skill-sync-github-create-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to create a record that synchronizes a full skill package from GitHub Enterprise Server, and prints the authorization link if a GitHub user must approve access:

```python
import boto3

client = boto3.client('agent-registry-control')

response = client.create_registry_record(
    registryId='<registryId>',
    name='my-skill',
    recordType='SKILL',
    recordVersion='1.0',
    descriptors={
        'agentSkillsDefinition': {
            'additionalData': {
                'repositoryProvider': 'GITHUB',
                'skillPackage': {
                    'source': {
                        'fromUrl': {
                            'url': 'https://github.example.com/octo-org/skills/tree/main/skills/my-skill',
                            'credentialProviderConfigurations': [{
                                'credentialProviderType': 'OAUTH',
                                'credentialProvider': {
                                    'oauthCredentialProvider': {
                                        'providerArn': 'arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default/oauth2credentialprovider/my-ghes-provider',
                                        'grantType': 'AUTHORIZATION_CODE',
                                        'scopes': ['repo'],
                                        'returnUrl': 'https://app.example.com/registry/oauth/callback'
                                    }
                                }
                            }]
                        }
                    }
                }
            }
        }
    },
)

print(f"Status: {response['status']}")
oauth2 = response.get('authorizationData', {}).get('oauth2')
if oauth2:
    # Store oauth2['userId'] with your signed-in user, then send the user to the link.
    print(f"Approve access before {oauth2['expiresAt']}: {oauth2['authorizationUrl']}")
```

## Synchronize again or authorize again
<a name="registry-skill-sync-github-resync"></a>

The registry doesn’t watch the repository for changes. To read the folder again, request a synchronization. An update that sets a different source URL or credential configuration also starts one on its own. An update that sends the stored source back unchanged, or changes only the return URL, doesn’t start one.

A synchronization that changes an `APPROVED` record’s content creates a new `DRAFT` revision, and discovery keeps returning the approved revision until the new one is approved. A synchronization that reads the same SKILL.md and package returns the record to its previous status. A failed synchronization keeps the record’s previous content and package. If the synchronization was to replace an uploaded package, `GetRegistryRecord` returns no download URL until a synchronization succeeds.

You can also ask the user to approve access again even though the current approval still works, for example to use a different GitHub account. The new approval replaces the approval that your other records in the registry use for the same host, credential provider, scopes, and custom parameters. Each forced approval gets a new GitHub token, which counts toward GitHub’s token limit. For more information, see [Authorize GitHub access](#registry-skill-sync-github-authorization).

GitHub can reject the token, for example after the GitHub account owner revokes the OAuth App’s access. The synchronization then fails. Synchronize again to authorize again. If you get the same error, also ask the GitHub account owner to approve access again.

### Console
<a name="registry-skill-sync-github-resync-console"></a>

To synchronize an unchanged source again, choose **Manage**, choose **Synchronization**, and then choose **Sync** to confirm.

To point the record at another folder, to authorize GitHub access again, or to give an existing record a GitHub source for the first time, use the edit form. It holds a skill record’s source in the **Skill content** section, along with the record’s other content sources.

1. On the record detail page, choose **Manage**, and then choose **Edit**.

1. In the **Skill content** section, for **Skill content source**, choose **Synchronize from source**. The console warns you that saving with a different source replaces the record’s content and removes the previous source, including an uploaded package.

1. For **Additional content**, choose **Skill definition** to keep or add a structured skill definition in JSON, or **None**. SKILL.md always comes from the source, so the editor for it isn’t offered here. If the record has a definition and you choose **None**, saving removes it.

1. For **Source**, choose **GitHub**.

1. Set **Content type**, **GitHub folder**, **Credential provider**, **Repository access**, and **Return URL**, as described in [Create a record that synchronizes from GitHub](#registry-skill-sync-github-create-console).

   The form opens on the record’s stored source, and keeps each source’s location separately, so you can switch between **GitHub** and **Amazon S3** without losing either one.

1. (Optional) Select **Trigger synchronization** to read the folder on save. A new or changed source synchronizes on its own, so you need this only to read an unchanged source again.

1. (Optional) Select **Re-authorize GitHub access** to ask a GitHub user to approve access again, even though the current approval still works.

   The console selects **Trigger synchronization** and you can’t clear it, because a forced approval requires a synchronization. The new approval also replaces the one that your other records in this registry use for the same credential provider and repository access.

1. Choose **Save changes**.

Because the save starts a synchronization, **Save and submit for approval** isn’t available, and the console explains why. Save your changes, wait for the synchronization to finish, and then submit the record for approval.

While the record waits for a GitHub user to approve access, you can’t save changes to it. The record’s **Edit** action isn’t available in `CREATE_PENDING_AUTH` and `UPDATE_PENDING_AUTH` status, and the form’s fields and **Save** buttons aren’t available either. The console tells you to authorize access or to wait for the authorization to expire. For more information, see [Timing and pending records](#registry-skill-sync-github-pending).

### AWS CLI
<a name="registry-skill-sync-github-resync-cli"></a>

To read the folder again, update the record with `triggerSynchronization`:

```bash
aws agent-registry-control update-registry-record \
  --registry-id <registryId> \
  --record-id <recordId> \
  --trigger-synchronization \
  --region us-east-1
```

To ask a GitHub user to approve access again, set `forceAuthentication` together with `triggerSynchronization`:

```bash
aws agent-registry-control update-registry-record \
  --registry-id <registryId> \
  --record-id <recordId> \
  --trigger-synchronization \
  --force-authentication \
  --region us-east-1
```

## Check what the registry read
<a name="registry-skill-sync-github-result"></a>

After a successful synchronization, `GetRegistryRecord` returns `synchronizedSource.gitHub` with the following members:
+  `url` — The source URL that the registry read.
+  `synchronizedAt` — When the registry read it.
+  `commitId` — The commit that the branch or tag pointed to.

```json
"synchronizedSource": {
    "gitHub": {
        "url": "https://github.com/octo-org/skills/tree/main/skills/my-skill",
        "synchronizedAt": "2026-11-19T17:00:18Z",
        "commitId": "<commit-sha>"
    }
}
```

A failed synchronization leaves `synchronizedSource` as it was. After you change the source, it shows the previous source until a synchronization of the new one succeeds.

## Troubleshoot a GitHub source
<a name="registry-skill-sync-github-errors"></a>

When a synchronization fails, the record moves to `CREATE_FAILED` or `UPDATE_FAILED`, and `statusReason` describes the problem. The following table lists common causes.


| Status reason mentions | What to check | 
| --- | --- | 
| The repository, branch or tag, or path was not found, or the GitHub credentials can’t read it | The URL’s owner, repository, branch or tag, and folder exist, and the authorized GitHub user can read the repository. For a private repository, request the `repo` scope. | 
| The source URL matches more than one branch or tag | Start the branch or tag in the URL with `refs/heads/` or `refs/tags/`. | 
| No SKILL.md was found in the skill folder | The folder has a file named exactly `SKILL.md` at the branch or tag. | 
| GitHub rejected the OAuth access token | Update the record with `triggerSynchronization` to authorize again, and also set `forceAuthentication` if the error repeats. | 
| The repository’s organization enforces SAML single sign-on, or restricts OAuth App access | The user authorized the OAuth App for single sign-on, or an organization owner approved the OAuth App. | 
| GitHub is rate limiting requests for the authorized GitHub user | Synchronize again after the time in the message. | 
| The GitHub Enterprise Server’s TLS certificate isn’t trusted, or its host name resolves to an address that isn’t public | The server meets the requirements in [Make GitHub Enterprise Server reachable](#registry-skill-sync-github-ghes). | 

For package and SKILL.md problems, see [How validation failures appear](registry-skill-package-format.md#registry-skill-package-format-failures).