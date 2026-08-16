# User-managed setup (3LO)

With user-managed setup, you sign in to OneDrive directly and Amazon Bedrock Managed Knowledge Base handles authentication. Users can complete setup in a few minutes.

###### Important

User-managed setup does not support document-level access control (ACL). All indexed content is accessible to any user who has access to query the knowledge base. Individual permissions in OneDrive are not enforced. Carefully review which content you include when creating a knowledge base. If you require document-level access control, use Microsoft Entra App ID authentication instead. See [Set up Microsoft Entra App ID authentication for OneDrive](kb-managed-onedrive-entra-setup.md "kb-managed-onedrive-entra-setup.md"). For more information about document-level access control, see [Access Control Lists awareness enablement](kb-managed-acl.md "kb-managed-acl.md").

## How your credentials are stored

With user-managed setup, you do not create or provide an AWS Secrets Manager secret yourself, and you do not provide a tenant ID. When you sign in, Amazon Bedrock Managed Knowledge Base creates a secret in your AWS account with a system-generated ARN and stores a 3LO refresh token in it. Amazon Bedrock Managed Knowledge Base uses the refresh token to obtain and refresh access tokens as needed to access the data source.

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

You can create 3LO secrets and complete the user consent flow through the Amazon Bedrock Knowledge Bases console. You can then reference these AWS Secrets Manager entries when creating a third-party data connector (see [Connect a OneDrive data source](kb-managed-ds-onedrive-connect.md "kb-managed-ds-onedrive-connect.md")). These entries are not associated with any knowledge base and can be used across separate knowledge bases as needed.

## Before you begin

Before you begin, make sure you have the following:

- A Microsoft 365 account with access to the OneDrive content you want to index.
- Access to Amazon Bedrock with permissions to create knowledge bases.
- A browser that allows popups from the Amazon Bedrock Knowledge Bases console domain.

Most users complete setup without any extra steps. However, if your Microsoft 365 tenant restricts third-party app access, you might see an error when you sign in. In this case, a Microsoft 365 administrator needs to grant one-time consent for the Amazon Bedrock KB application. After consent is granted, any user in your organization can connect.

If you are not a Microsoft 365 administrator, share the following information with your administrator:

- **What to do:** Grant admin consent for the Amazon Bedrock KB OneDrive application.
- **Why:** Amazon Bedrock KB needs delegated read access to OneDrive files to index content for knowledge bases.

## Grant organization-wide admin consent

Some Amazon Bedrock KB features require delegated permissions from Microsoft Entra. By default, you see a Microsoft consent dialog the first time you use the feature. A Microsoft 365 administrator can pre-consent on behalf of the entire organization. After consent is granted, you are not prompted with the consent dialog. This is a one-time action per application.

###### Note

If your Microsoft 365 tenant is configured to restrict user consent for third-party applications, admin consent is required, not optional. Without it, users see an error when they attempt to use the feature.

The following table describes the user experience with and without admin consent.

Admin consent scenarios| Scenario | User experience |
| --- | --- |
| Admin consent not granted | Each user sees the Microsoft permissions consent dialog on first use. Users might be blocked if your tenant restricts user consent for third-party apps. |
| Admin consent granted | Users aren't prompted for consent. The feature works immediately for all users in the organization. |

### Granting consent through the consent dialog

The simplest way to grant admin consent is through the Microsoft consent dialog that appears during the feature flow.

###### To grant consent through the consent dialog

1. Have a Global Administrator or Privileged Role Administrator initiate the feature flow that triggers the consent dialog.
2. In the Microsoft sign-in dialog, select the **Consent on behalf of your organization** check box.
3. Choose **Accept**.

This grants consent for the requested delegated permissions for all users in your Microsoft 365 tenant.

### Granting consent through the Microsoft Entra admin center

Administrators can also grant consent directly from the Microsoft Entra admin center.

###### To grant consent through the Microsoft Entra admin center

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/ "https://entra.microsoft.com/") on the Microsoft website.
2. In the left navigation pane, expand **Entra ID** and choose **Enterprise applications**.
3. Locate the enterprise application for the Amazon Bedrock KB feature.

###### Note

The application name appears in the consent dialog that users see when they first use the feature. 4. In the left navigation pane, choose **Permissions**. 5. Choose **Grant admin consent for `Your Organization`**. 6. Confirm the consent.

### Verifying consent

After you grant consent, the enterprise application's **Permissions** page shows all delegated permissions with a status indicator under the **Admin consent** column.

###### Note

When an administrator grants organizational consent, Microsoft Entra automatically creates an enterprise application (service principal) in your tenant. To revoke access, disable or delete this service principal from **Enterprise applications** in the Microsoft Entra admin center.

### Checking tenant consent settings

To check whether your tenant restricts user consent, complete the following steps.

###### To check tenant consent settings

1. In the Microsoft Entra admin center, choose **Entra ID**, **Enterprise applications**, **Consent and permissions**, **User consent settings**.
2. If the setting is **Do not allow user consent**, an administrator must grant consent before users can use the feature.

## Permissions requested

The following delegated permissions are requested when a user signs in. Share this list with your administrator if they need to review the permissions before granting consent.

User-managed setup — permissions| Permission | API | Type | Description |
| --- | --- | --- | --- |
| `Files.Read.All` | Microsoft Graph | Delegated | Read all files the signed-in user can access. |
| `User.Read` | Microsoft Graph | Delegated | Sign in and read the user's profile. |
| `offline_access` | Microsoft Graph | Delegated | Maintain access using refresh tokens. |

## Troubleshooting

If you run into problems during user-managed setup, match the symptom against the following.

User-managed setup issues| Issue | Cause and resolution |
| --- | --- |
| App blocked by administrator | Your Microsoft 365 tenant restricts third-party app access. Ask your Microsoft 365 administrator to grant admin consent. For more information, see [Grant organization-wide admin consent](#kb-managed-onedrive-3lo-admin-consent "#kb-managed-onedrive-3lo-admin-consent"). |
| Sign-in window closes without completing | Verify that your browser allows popups from the Amazon Bedrock KB console domain and that third-party cookies are enabled. |
| Missing content | Verify that the account you used for authentication has access to the files and folders you selected. Content shared with you after the initial sync requires a resync to be indexed. |

## Next steps

After you complete user-managed setup, create the data source with `authType` set to `MANAGED_OAUTH2`. See [Connect a OneDrive data source](kb-managed-ds-onedrive-connect.md "kb-managed-ds-onedrive-connect.md").
