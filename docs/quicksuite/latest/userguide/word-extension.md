# Amazon Quick Suite Microsoft Word

extension

The Quick Suite extension for Microsoft Word integrates
AI-powered assistance directly into your document creation and editing workflows. Users
can access Quick Suite capabilities within Word to enhance their
document productivity and content quality without switching between applications.

The Word extension enables users to:

- Review, draft, and revise documents with AI assistance.
- Summarize documents and get insights.
- Simplify and improve writing quality.
- Use actions from action connectors configured in Amazon Quick Suite.
- Access any company knowledge sources added to your Amazon Quick Suite instance from
  within Microsoft Word.

###### Important

- The Amazon Quick Suite customer integrating Microsoft Word must
  have a paid Word organization with an
  _M365 subscription for their
  organization_.
- Amazon Quick Suite does not use user data for service improvement or for
  training its underlying large language models (LLMs).

###### Topics

- [Prerequisites for Microsoft Word
  extension](#word-prerequisites "#word-prerequisites")
- [Configure Microsoft Word
  extension access](#configure-word-extension "#configure-word-extension")

## Prerequisites for Microsoft Word

extension

Before adding the Amazon Quick Suite extension to Microsoft Word,
administrators must complete the following steps:

1. Have a Microsoft 365 Business subscription and be a Global
   Admin or have administrative permissions (specifically
   `AppCatalog.ReadWrite.All`).
2. Have a Amazon Quick Suite instance.
3. Your Microsoft 365 tenant ID. You can find this by going to
   the Azure portal > **Azure Active
   Directory** > **Properties**, or by using
   PowerShell. For detailed steps, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant "https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant") in
   the Microsoft Learn portal.

If you configured the authentication to connect to Amazon Quick Suite with IAM Identity Center, complete the following additional steps:

1. Ensure you have an IAM Identity Center instance enabled on your AWS account.
2. If you are connecting an external IAM provider to IAM Identity Center, ensure that every user under your IAM provider configuration has an email associated with them.
3. If you are using Entra ID, set up SCIM identity propagation between the Microsoft Entra ID instance and IAM Identity Center. For detailed steps,
   see [Configure SAML and SCIM with Microsoft Entra ID
   and IAM Identity Center](../../../singlesignon/latest/userguide/azure-ad-idp.md "../../../singlesignon/latest/userguide/azure-ad-idp.md").

## Configure Microsoft Word

extension access

As an administrator, you must allow the Amazon Quick Suite Microsoft Word
Extension to connect to your Amazon Quick Suite application environment and web
experience. You can use the Amazon Quick Suite console to manage extension access
configurations.

### User attribute mapping

When you configure a Microsoft Word extension, user identity is
mapped by default using the following attributes:

- **Amazon Quick Suite user attribute** - Email address is
  used to map Amazon Quick Suite users to their corresponding Microsoft
  365 accounts. The system uses the email address to establish
  the connection between user identities.
- **M365 Office add-in user attribute**

* User Principal Name (UPN) is used to match against
  Microsoft 365 user accounts. Users need to use the
  User Principal Name (UPN) to sign in to
  Microsoft 365. Email address that works on both cloud
  and on-premise systems.

These default mappings ensure secure and accurate user identification across
both platforms without requiring additional configuration.

###### Topics

- [Add Microsoft Word extension access for accounts using IAM Identity Center](#add-word-extension-access-idc "#add-word-extension-access-idc")
- [Add Microsoft Word
  extension access for accounts using other authentication methods](#add-word-extension-access "#add-word-extension-access")
- [Edit Microsoft Word
  extension access](#edit-word-extension-access "#edit-word-extension-access")
- [Delete Microsoft
  Word extension access](#delete-word-extension-access "#delete-word-extension-access")

### Add Microsoft Word extension access for accounts using IAM Identity Center

Configuring extension access with IAM Identity Center requires completing steps specific to your identity provider (Entra ID or Okta) followed by common setup steps in AWS.

#### Configure IAM Identity Center with Entra ID

Follow these steps only if you are using IAM Identity Center with Entra ID to set up and configure an Azure tenant on your Microsoft Azure portal:

###### To set up an Azure tenant

1. In the Azure account, create a new app registration.
   1. Go to **App registrations**.
   2. In the **App registrations** screen, choose **New registration**. Under the **Supported account types** option, choose **Accounts in this organizational directory only (Personal use only - Single tenant)**. Once finished, choose **Register**.
   3. Note the client ID. You will need this later.
   4. Create a client secret for the app registration and keep note of it. You will need this later.

2. Add callback URLs for each Region in which your Word extension will be installed.
   1. Navigate to the app registration's **Authentication** tab.
   2. Choose **Platform Configurations**, **Add a platform**.
   3. Choose **Web**.
   4. Compose a callback URL using the following format, replacing `your-region` with your Amazon Quick Suite instance Region. The Word extension supports the following Regions: `ap-southeast-2`, `eu-west-1`, `us-west-2`, and `us-east-1`.

   ```
   qbs-cell001.dp.appintegrations.`your-region`.prod.plato.ai.aws.dev/auth/idc-tti/callback
   ```

   5. Insert the callback URL as the redirect URI and choose **Configure** when done.

Follow these steps to configure a Trusted Token Issuer on your IAM Identity Center instance in your AWS Console:

###### To configure a Trusted Token Issuer

1. Go to your AWS account and navigate to your IAM Identity Center instance.
2. Navigate to **Settings**, **Authentication**.
3. Choose **Create trusted token issuer**.
4. Add the issuer URL, which should follow this template, where `Tenant ID` refers to your Entra tenant ID:

```
login.microsoftonline.com/`Tenant ID`/v2.0
```

###### Note

The issuer URL should be the OIDC discovery endpoint of your identity without the well-known document URI path. If you include the well-known document URI path, this will not work. See Trusted token issuer configuration settings. 5. Choose **Email** as the Identity Provider attribute and IAM Identity Center attribute.

After completing these Entra ID-specific steps, proceed to the [Complete AWS Configuration (all providers)](#complete-aws-config-word "#complete-aws-config-word") section below.

#### Configure IAM Identity Center with Okta

Follow these steps only if you are using IAM Identity Center with Okta to set up and configure your App Integration in the Okta Admin console:

###### To set up an Okta Application

1. In your Okta account, create a new Okta App Integration.
   1. In your Okta Admin console, navigate to **Applications** > **Applications**.
   2. Click on **Create App Integration**.
   3. For the Sign-in method, select **OIDC - OpenID Connect**.
   4. For the Application type, select **Web Application**.
   5. Click on **Next**.
   6. Provide an App integration name.
   7. Under **Grant type** > **Core grants**, ensure **Authorization Code** and **Refresh Token** are selected.
   8. Under **Grant type** > **Advanced** > **Other grants**, ensure **Implicit (hybrid)** is selected.

2. Add callback URIs for each Region in which your Word extension will be installed
   1. Compose a callback URI using the following format, replacing `your-region` with your Amazon Quick Suite instance Region for each region where you wish to configure the extension. The Word extension supports the following Regions: `ap-southeast-2`, `eu-west-1`, `us-west-2`, and `us-east-1`.

   ```
   qbs-cell001.dp.appintegrations.`your-region`.prod.plato.ai.aws.dev/auth/idc-tti/callback
   ```

   2. Under **Sign-in redirect URIs**, click on **Add URI** and paste each of the URIs you generated from the previous step.

3. Provide your organization access to the app:
   1. Under **Assignments** > **Controlled access**, select the groups in your organization that need to have access.
   2. Under **Assignments** > **Enable immediate access**, select **Enable immediate access with Federation Broker Mode**.
   3. Click on **Save**.

4. Note down the **Client ID** and **Client Secret** for the app integration you just created. You will need this in the next steps.

###### To configure a Trusted Token Issuer

1. Go to your AWS account and navigate to your IAM Identity Center instance.
2. Navigate to **Settings** > **Authentication**.
3. Choose **Create trusted token issuer**.
4. Add the issuer URL, which should follow this template, where `yourOktaDomain` refers to the okta URL for your organization, which may look like `your-organization.okta.com`:

```
https://{`yourOktaDomain`}/oauth2/default
```

###### Note

The issuer URL should be the OIDC discovery endpoint of your identity without the well-known document URI path. If you include the well-known document URI path, this will not work. See Trusted token issuer configuration settings. 5. Choose **Email** as the Identity Provider attribute and IAM Identity Center attribute.

After completing these Okta-specific steps, proceed to the [Complete AWS Configuration (all providers)](#complete-aws-config-word "#complete-aws-config-word") section below.

#### Complete AWS Configuration (all providers)

Follow these steps to set up permissions on AWS Console:

###### To set up permissions

1. Navigate to Secrets Manager on AWS console.
2. Choose **Store a new secret**.
3. Choose **Other type of secret** and choose the **Plaintext** tab.
4. Your secret should be in the following format and use the app registration client ID and app registration client secret that you saved from the earlier steps:

```

{
"client_id":"`Your app registration client ID`",
"client_secret":"`Your app registration client secret`"
}
```

5. Navigate to the secret you just created and save the ARN for later.
6. Now navigate to IAM on AWS console.
7. Choose **Access Management**, **Roles** in the left navigation bar.
8. Choose **Create role**.
9. Choose **Custom trust policy**.
10. Configure the role to trust our service principal for the relevant Region that you selected when configuring your identity provider app integration by adding the following statement replacing `your-region` with the Region you chose when creating your identity provider app integration:

```

{
"Version": "2012-10-17",
"Statement": [
{
    "Effect": "Allow",
    "Principal": {
        "Service": "`your-region`.prod.appintegrations.plato.aws.internal"
    },
    "Action": "sts:AssumeRole",
    "Condition": {}
}
]
}
```

11. Choose **Next**.
12. Provide a name and description and choose **Create role**.
13. Navigate to the role you just created and choose it.
14. Choose **Add Permissions**, **Create inline policy**.
15. Choose **JSON**.
16. Configure the role with permissions to read secrets from Secrets Manager and permissions to invoke `sso:DescribeTrustedTokenIssuer` by adding the following statement:

```

{
"Version": "2012-10-17",
"Statement": [
{
    "Sid": "BasePermissions",
    "Effect": "Allow",
    "Action": [
        "secretsmanager:GetSecretValue",
        "sso:DescribeTrustedTokenIssuer"
    ],
    "Resource": "*"
}
]
}
```

17. Provide a policy name and choose **Create policy**.
18. Copy and save the ARN of the IAM role you created for later. You will need it in the next steps.

Now you can follow these steps to create a new extension access configuration that will allow Amazon Quick Suite to integrate with your Microsoft Word environment:

###### To create an extension access configuration

1. Sign in to the Amazon Quick Suite console.
2. In the top right, choose the profile picture icon.
3. From the drop-down menu, choose **Manage account**.
4. Under **Permissions**, choose **Extension access**.
5. In the top right, choose **New extension access**.
6. Select **Microsoft Word**. Then, choose **Next**.
7. Configure the following fields:
   - **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Word extension (maximum 512 alphanumeric characters, hyphens allowed but no spaces).
   - **Description (optional)** - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration (maximum 1000 characters).
   - **M365 tenant ID** - Enter your Microsoft 365 tenant identifier (must be 36 characters).
   - **Secrets Role ARN** - Paste the ARN of the IAM role you created from the previous steps.
   - **Secrets ARN** - Paste the ARN of the Secrets Manager secret you created from the previous steps.

8. Choose **Add** to save the new access configuration.

A success message will open up on the top right of your screen. 9. From the success message, choose **View extensions** to finish installing your extension.

###### Note

You can also navigate to the installation screen from **Connections** > **Extensions** in the Amazon Quick Suite menu.

Once created, this extension access configuration enables authors and other admin in your organization to create and deploy Amazon Quick Suite extensions within your Microsoft Word environment.

###### Note

For your end users to begin using your Microsoft Word extension, an admin or author must finish deploying a extension after you configure extension access. Notify your authors that they can view, edit, and complete installation of this extension under **Extensions** in the left navigation once it has been shared. To learn how to do this see Installing your Microsoft Word extension in the Microsoft Word extension author guide.

### Add Microsoft Word

extension access for accounts using other authentication methods

Follow these steps to create a new extension access configuration that will
allow Amazon Quick Suite to integrate with your Microsoft Word
environment.

1. Sign in to the Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. In the top right, select **New extension
   access**.
6. Select **Microsoft Word**. Then, select
   **Next**.
7. Configure the following fields:
   - **Name** - A name for your extension is
     pre-filled for you. You can edit this and enter a descriptive
     name for the Word extension (maximum 512
     alphanumeric characters, hyphens allowed but no spaces).
   - **Description** (optional) - A description
     for your extension is pre-filled for you. You can edit this and
     enter a new description to provide additional context about this
     extension configuration (maximum 1000 characters).
   - **M365 tenant ID** - Enter your
     Microsoft 365 tenant identifier (must be 36
     characters).

8. Select **Add** to save the new access
   configuration.

A success message will open up on the top right of your screen. 9. From the success message, select **View extensions**
to finish installing your extension.

###### Note

You can also navigate to the installation screen from
**Connections** >
**Extensions** in the Amazon Quick Suite menu.

Once created, this extension access configuration enables authors and other
admin in your organization to create and deploy Amazon Quick Suite extensions within
your Microsoft Word environment.

###### Note

For your end users to begin using your Microsoft Word
extension, an admin or author must finish deploying a extension after you
configure extension access. Notify your authors that they can view, edit,
and complete installation of this extension under
**Extensions** in the left navigation once it has been
shared. To learn how to do this see [Installing your Microsoft Word
extension in the Microsoft Word extension author
guide](word-extension-author-guide.md#add-extensions-word "word-extension-author-guide.md#add-extensions-word").

### Edit Microsoft Word

extension access

Use these steps to modify the configuration settings of an existing
Microsoft Word extension access.

1. Sign in to the Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the **Microsoft
   Word** extension you need to edit.
6. Select **Edit**.
7. Edit the configuration as required and select
   **Save** to confirm the changes.

Your changes to the Microsoft Word extension access
configuration are saved and will take effect immediately.

### Delete Microsoft

Word extension access

Follow these steps to permanently remove a Microsoft Word
extension access configuration. This action cannot be undone.

###### Note

Deleting a extension access removes access for all users in your M365
tenant and deletes all extensions created for Word.

1. Sign in to the Amazon Quick Suite console.
2. In the top right, select the profile picture icon.
3. From the drop-down menu, select **Manage
   account**.
4. Under **Permissions**, select **Extension
   access**.
5. Select the three dot menu icon for the Microsoft Word
   Extension you need to delete.
6. Select **Delete**.
7. Enter the word, "confirm", and select
   **DELETE**.

###### Note

If the process to delete extension access fails, the admin must switch to
the author view and delete the Word extensions that are using
the configured extension access before returning to delete the extension
access.

With Microsoft Word extension access configured, your team can now use
Amazon Quick Suite to enhance their document creation workflows with AI assistance for
reviewing, drafting, revising, and accessing organizational knowledge directly within
Word.
