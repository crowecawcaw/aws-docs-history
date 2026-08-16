# User-managed setup (3LO)

With user-managed setup, you sign in to Confluence Cloud directly to authorize the connection, and Amazon Bedrock Managed Knowledge Base handles authentication. Users can complete setup in a few minutes. After you authorize the connection, create the data source with `authType` set to `MANAGED_OAUTH2`. See [Connect a Confluence data source](kb-managed-ds-confluence-connect.md "kb-managed-ds-confluence-connect.md").

###### Important

User-managed setup does not support document-level access control (ACL). All indexed content is accessible to any user who has access to query the knowledge base. Individual permissions in Confluence are not enforced. Carefully review which content you include when creating a knowledge base. If you require document-level access control, use Basic authentication instead. See [Set up Basic authentication for Confluence](kb-managed-confluence-basic-setup.md "kb-managed-confluence-basic-setup.md"). For more information about document-level access control, see [Access Control Lists awareness enablement](kb-managed-acl.md "kb-managed-acl.md").

## How your credentials are stored

With user-managed setup, you do not create or provide an AWS Secrets Manager secret yourself. When you sign in, Amazon Bedrock Managed Knowledge Base creates a secret in your AWS account with a system-generated ARN and stores a 3LO refresh token in it. Amazon Bedrock Managed Knowledge Base uses the refresh token to obtain and refresh access tokens as needed to access the data source.

When you choose **Sign in**, you can optionally provide a **secret name prefix**. Amazon Bedrock Managed Knowledge Base includes this prefix in the generated secret ARN. Providing a prefix lets you create a scoped-down IAM policy that grants access only to secrets with that prefix. You can put this policy in place before the 3LO token is created. If you do not provide a prefix, the created secret uses the `bedrock-managedkb-oauth` prefix.

The generated secret ARN follows this pattern:

```
arn:aws:secretsmanager:`region`:`account-id`:secret:bedrock-managedkb-oauth/`your-prefix`/`connector-type`/`uuid`
```

**Permissions for the caller (CreateDataSource):** The IAM principal that calls `CreateDataSource` needs the following permissions on the secret:

```
{
    "Effect": "Allow",
    "Action": [
        "secretsmanager:CreateSecret",
        "secretsmanager:GetSecretValue"
    ],
    "Resource": [
        "arn:aws:secretsmanager:`region`:`account-id`:secret:bedrock-managedkb-oauth/`your-prefix`/*"
    ]
}
```

**Permissions for the execution role:** The knowledge base execution role needs read and write access to the secret for token refresh:

```
{
    "Effect": "Allow",
    "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:PutSecretValue"
    ],
    "Resource": [
        "arn:aws:secretsmanager:`region`:`account-id`:secret:bedrock-managedkb-oauth/`your-prefix`/*"
    ]
}
```

You can create 3LO secrets and complete the user consent flow through the Amazon Bedrock Knowledge Bases console. You can then reference these AWS Secrets Manager entries when creating a third-party data connector (see [Connect a Confluence data source](kb-managed-ds-confluence-connect.md "kb-managed-ds-confluence-connect.md")). These entries are not associated with any knowledge base and can be used across separate knowledge bases as needed.

If you run into problems during user-managed setup, use the following guidance.

## Blocked OAuth app authorization

**Symptoms:**

- Error message: "Your site admin must authorize this app for the site `instance-name`.atlassian.net before the app can access your account."
- Choosing **Accept** in the consent dialog has no effect.

**Cause:**

Your Atlassian site administrator has blocked user-installed OAuth apps. When this setting is enabled, only a site or organization administrator can authorize new third-party apps.

**Resolution steps:**

Use one of the following options to resolve this issue.

**Recommended solution: Admin authorizes the app directly**

1. An Atlassian site administrator navigates to Amazon Bedrock KB and starts a new knowledge base setup with Confluence Cloud.
2. Because the administrator has site-level permissions, a clean consent screen appears without the error.
3. The administrator chooses **Accept** to install the app.
4. After the administrator authorizes the app, all other users on the site can connect without issues.

**Alternative (Not recommended): Temporarily allow user-installed apps** — An administrator goes to `admin.atlassian.com`, navigates to **Apps**, **Atlassian Apps**, then chooses the link for third-party and Marketplace apps. Under **Settings**, find **User Installed Apps** and toggle to allow user apps. After the user authorizes Amazon Bedrock KB, toggle the setting back to block user apps.

###### Warning

This approach temporarily disables app authorization controls for your entire site. While unblocked, any user can authorize any third-party OAuth app. Use the recommended solution (admin authorizes directly) whenever possible.

###### Important

Admin authorization applies per Atlassian site, not per organization. If your company has multiple sites (for example, `team-a.atlassian.net` and `team-b.atlassian.net`), each site requires separate authorization.

## Authentication popup fails

**Symptoms:**

- Authentication popup does not appear or closes immediately.
- Popup appears but fails to complete the OAuth flow.

**Resolution steps:**

1. Verify that your browser allows popups from the Amazon Bedrock KB console domain.
2. Verify that your Confluence Cloud instance is accessible from your network.
3. Try using a different browser or clearing your browser cache.
