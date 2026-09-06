

# Amazon Quick Microsoft Teams extension
<a name="teams-extension"></a>

The Quick extension for Microsoft Teams integrates AI-powered assistance directly into your team communication workflows. Users can mention @Amazon Quick in conversations to access company knowledge, use configured action connectors, and get contextual assistance without leaving their Teams environment.

The Teams extension enables users to:
+ Mention **@Amazon Quick** in conversations in Teams channels to add it as a collaborator.
+ Use actions from connectors configured in Amazon Quick.
+ Access any company knowledge sources added to your Amazon Quick instance from within Microsoft Teams.

**Important**  
The Amazon Quick customer integrating Microsoft Teams must have a paid Microsoft Teams organization with an *M365 subscription for their organization*.
Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs).

**Topics**
+ [Prerequisites for Microsoft Teams extension](#teams-prerequisites)
+ [Microsoft Teams extension permissions](teams-extension-permissions.md)
+ [Configure Microsoft Teams extension access](#configure-teams-extension)

## Prerequisites for Microsoft Teams extension
<a name="teams-prerequisites"></a>

Before configuring access for the Amazon Quick extension to Microsoft Teams, administrators must complete the following steps:

1. Have a Microsoft 365 Business subscription and be a Global Admin or have administrative permissions (specifically `AppCatalog.ReadWrite.All`).

1. Have a Amazon Quick instance.

1. Your Microsoft 365 tenant ID. You can find this by going to the Azure portal > **Azure Active Directory** > **Properties**, or by using PowerShell. For detailed steps, see [How to find your tenant ID - Microsoft Entra](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) in the Microsoft Learn portal.

If you configured the authentication to connect to Amazon Quick with IAM Identity Center, complete the following additional steps:

1. Ensure you have an IAM Identity Center instance enabled on your AWS account.

1. If you are connecting an external IAM provider to IAM Identity Center, ensure that every user under your IAM provider configuration has an email associated with them.

1. If you are using Entra ID, set up SCIM identity propagation between the Microsoft Entra ID instance and IAM Identity Center. For detailed steps, see [Configure SAML and SCIM with Microsoft Entra ID and IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/azure-ad-idp.html).

## Configure Microsoft Teams extension access
<a name="configure-teams-extension"></a>

As an administrator, you must allow the Amazon Quick Microsoft Teams to connect to your Amazon Quick application environment. You can use the Amazon Quick console to manage extension access configurations.

### User attribute mapping
<a name="teams-user-attributes"></a>

When you configure a Microsoft Teams extension, user identity is mapped by default using the following attributes:
+ **Amazon Quick user attribute** - Email address is used to map Amazon Quick users to their corresponding Microsoft 365 accounts. The system uses the email address to establish the connection between user identities.
+ **M365 Office add-in user attribute** - User Principal Name (UPN) is used to match against Microsoft 365 user accounts. Users need to use the User Principal Name (UPN) to sign in to Microsoft 365. Email address that works on both cloud and on-premise systems.

These default mappings ensure secure and accurate user identification across both platforms without requiring additional configuration.

**Topics**
+ [User attribute mapping](#teams-user-attributes)
+ [Add Microsoft Teams extension access for accounts using IAM Identity Center](#add-teams-extension-access-idc)
+ [Add Microsoft Teams extension access for accounts using other authentication methods](#add-teams-extension-access)
+ [Edit Microsoft Teams extension access](#edit-teams-extension-access)
+ [Delete Microsoft Teams extension access](#delete-teams-extension-access)

### Add Microsoft Teams extension access for accounts using IAM Identity Center
<a name="add-teams-extension-access-idc"></a>

Configuring extension access with IAM Identity Center requires completing steps specific to your identity provider (for example, Entra ID or Okta) followed by common setup steps in AWS.

#### Configure IAM Identity Center with Entra ID
<a name="configure-idc-entra-id"></a>

Follow these steps only if you are using IAM Identity Center with Entra ID to set up and configure an Azure tenant on your Microsoft Azure portal:

**To set up an Azure tenant**

1. In the Azure account, create a new app registration.

   1. Go to **App registrations**.

   1. In the **App registrations** screen, choose **New registration**. Under the **Supported account types** option, choose **Accounts in this organizational directory only (Personal use only - Single tenant)**. Once finished, choose **Register**.

   1. Note the client ID. You will need this later.

   1. Create a client secret for the app registration. Copy and save the secret's **Value** attribute. You need it later. This value is only shown once and cannot be retrieved after you leave the page.

1. Add callback URLs for each Region in which your Teams extension will be installed.

   1. Navigate to the app registration's **Authentication** tab.

   1. Choose **Platform Configurations**, **Add a platform**.

   1. Choose **Web**.

   1. Compose a callback URL using the following format, replacing {{your-region}} with your Amazon Quick instance Region. The Teams extension supports the following Regions: `ap-southeast-2`, `eu-west-1`, `us-west-2`, and `us-east-1`.

      ```
      qbs-cell001.dp.appintegrations.{{your-region}}.prod.plato.ai.aws.dev/auth/idc-tti/callback
      ```

   1. Insert the callback URL as the redirect URI and choose **Configure** when done.

Follow these steps to configure a Trusted Token Issuer on your IAM Identity Center instance in your AWS Console:

**To configure a Trusted Token Issuer**

1. Go to your AWS account and navigate to your IAM Identity Center instance.

1. Navigate to **Settings**, **Authentication**.

1. Choose **Create trusted token issuer**.

1. Add the issuer URL, which should follow this template, where {{Tenant ID}} refers to your Entra tenant ID:

   ```
   login.microsoftonline.com/{{Tenant ID}}/v2.0
   ```
**Note**  
The issuer URL should be the OIDC discovery endpoint of your identity without the well-known document URI path. If you include the well-known document URI path, this will not work. See Trusted token issuer configuration settings.

1. Choose **Email** as the Identity Provider attribute and IAM Identity Center attribute.

1. Note the trusted token issuer ARN. You will need this in a later step.

After completing these Entra ID-specific steps, proceed to the [Complete AWS Configuration (all providers)](#complete-aws-config-teams) section below.

#### Configure IAM Identity Center with Okta
<a name="configure-idc-okta"></a>

Follow these steps only if you are using IAM Identity Center with Okta to set up and configure your App Integration in the Okta Admin console:

**To set up an Okta Application**

1. In your Okta account, create a new Okta App Integration.

   1. In your Okta Admin console, navigate to **Applications** > **Applications**.

   1. Click on **Create App Integration**.

   1. For the Sign-in method, select **OIDC - OpenID Connect**.

   1. For the Application type, select **Web Application**.

   1. Click on **Next**.

   1. Provide an App integration name.

   1. Under **Grant type** > **Core grants**, ensure **Authorization Code** and **Refresh Token** are selected.

   1. Under **Grant type** > **Advanced** > **Other grants**, ensure **Implicit (hybrid)** is selected.

1. Add callback URIs for each Region in which your Teams extension will be installed

   1. Compose a callback URI using the following format, replacing {{your-region}} with your Amazon Quick instance Region for each region where you wish to configure the extension. The Teams extension supports the following Regions: `ap-southeast-2`, `eu-west-1`, `us-west-2`, and `us-east-1`.

      ```
      qbs-cell001.dp.appintegrations.{{your-region}}.prod.plato.ai.aws.dev/auth/idc-tti/callback
      ```

   1. Under **Sign-in redirect URIs**, click on **Add URI** and paste each of the URIs you generated from the previous step.

1. Provide your organization access to the app:

   1. Under **Assignments** > **Controlled access**, select the groups in your organization that need to have access.

   1. Under **Assignments** > **Enable immediate access**, select **Enable immediate access with Federation Broker Mode**.

   1. Click on **Save**.

1. Note down the **Client ID** and **Client Secret** for the app integration you just created. You will need this in the next steps.

**To configure a Trusted Token Issuer**

1. Go to your AWS account and navigate to your IAM Identity Center instance.

1. Navigate to **Settings** > **Authentication**.

1. Choose **Create trusted token issuer**.

1. Add the issuer URL, which should follow this template, where {{yourOktaDomain}} refers to the okta URL for your organization, which may look like `your-organization.okta.com`:

   ```
   https://{{{yourOktaDomain}}}/oauth2/default
   ```
**Note**  
The issuer URL should be the OIDC discovery endpoint of your identity without the well-known document URI path. If you include the well-known document URI path, this will not work. See Trusted token issuer configuration settings.

1. Choose **Email** as the Identity Provider attribute and IAM Identity Center attribute.

1. Note the trusted token issuer ARN. You will need this in a later step.

After completing these Okta-specific steps, proceed to the [Complete AWS Configuration (all providers)](#complete-aws-config-teams) section below.

#### Complete AWS Configuration (all providers)
<a name="complete-aws-config-teams"></a>

Follow these steps to set up permissions on AWS Console:

**To set up permissions**

1. Navigate to Secrets Manager on AWS console.

1. Choose **Store a new secret**.

1. Choose **Other type of secret** and choose the **Plaintext** tab.

1. Your secret should be in the following format and use the app registration client ID and app registration client secret that you saved from the earlier steps:

   ```
   {
   "client_id":"{{Your app registration client ID}}",
   "client_secret":"{{Your app registration client secret value}}"
   }
   ```

1. Navigate to the secret you just created and save the ARN for later.

1. Now navigate to IAM on AWS console.

1. Choose **Access Management**, **Roles** in the left navigation bar.

1. Choose **Create role**.

1. Choose **Custom trust policy**.

1. Configure the role to trust our service principal for the relevant Region that you selected when configuring your identity provider app integration by adding the following statement replacing {{your-region}} with the Region you chose when creating your identity provider app integration:

   ```
   {
   "Version": "2012-10-17", 		 	 	 
   "Statement": [
   {
       "Effect": "Allow",
       "Principal": {
           "Service": "{{your-region}}.prod.appintegrations.plato.aws.internal"
       },
       "Action": "sts:AssumeRole",
       "Condition": {}
   }
   ]
   }
   ```

1. Choose **Next**.

1. Provide a name and description and choose **Create role**.

1. Navigate to the role you just created and choose it.

1. Choose **Add Permissions**, **Create inline policy**.

1. Choose **JSON**.

1. Configure the role with permissions to read secrets from Secrets Manager and permissions to invoke `sso:DescribeTrustedTokenIssuer` by adding the following statement:

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

1. Provide a policy name and choose **Create policy**.

1. Copy and save the ARN of the IAM role you created for later. You will need it in the next steps.

Now you can follow these steps to create a new extension access configuration that will allow Amazon Quick to integrate with your Microsoft Teams environment:

**To create an extension access configuration**

1. Sign in to the Amazon Quick console.

1. Choose the profile picture icon.

1. From the drop-down menu, choose **Manage account**.

1. Under **Permissions**, choose **Extension access**.

1. Choose **New extension access**.

1. If this is your first time setting up extension access, you are prompted to complete the **Trusted Token Issuer Setup**. Configure the following fields and then choose **Next**:
   + **Trusted Token Issuer ARN** – Enter the trusted token issuer ARN that you noted from the earlier steps.
   + **Aud claim** – Enter the client ID from your app registration (Entra ID) or app integration (Okta) that you saved from the earlier steps.
**Note**  
This is a one-time setup that establishes a trusted identity source for all extensions. Once completed, you won't need to do this again for other extension accesses.

1. Select **Microsoft Teams**. Then, choose **Next**.

1. Configure the following fields:
   + **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Teams extension (maximum 512 alphanumeric characters, hyphens allowed but no spaces).
   + **Description (optional)** - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration (maximum 1000 characters).
   + **M365 tenant ID** - Enter your Microsoft 365 tenant identifier (must be 36 characters).
   + **Secrets Role ARN** - Paste the ARN of the IAM role you created from the previous steps.
   + **Secrets ARN** - Paste the ARN of the Secrets Manager secret you created from the previous steps.

1. Choose **Add** to save the new access configuration.

   A success message will open up on the top right of your screen.

1. From the success message, choose **View extensions** to finish installing your extension.
**Note**  
You can also navigate to the installation screen from **Connections** > **Extensions** in the Amazon Quick menu.

Once created, this extension access configuration enables authors and other admin in your organization to create and deploy Amazon Quick extensions within your Microsoft Teams environment.

**Note**  
For your end users to begin using your Microsoft Teams extension, an admin or author must finish deploying a extension after you configure extension access. Notify your authors that they can view, edit, and complete installation of this extension under **Extensions** in the left navigation once it has been shared. To learn how to do this see Installing your Microsoft Teams extension in the Microsoft Teams extension author guide.

### Add Microsoft Teams extension access for accounts using other authentication methods
<a name="add-teams-extension-access"></a>

Follow these steps to create a new extension access configuration that will allow Amazon Quick to integrate with your Microsoft Teams environment.

1. Sign in to the Amazon Quick console.

1. Choose the profile picture icon.

1. From the drop-down menu, select **Manage account**.

1. Under **Permissions**, select **Extension access**.

1. Choose **New extension access**.

1. Select **Microsoft Teams**, then, **Next**.

1. Configure the following fields:
   + **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Teams extension (maximum 512 alphanumeric characters, hyphens allowed but no spaces).
   + **Description** (optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration (maximum 1000 characters).
   + **M365 tenant ID** - Enter your Microsoft 365 tenant identifier (must be 36 characters).

1. Select **Add** to save the new access configuration.

   A success message will open up on the top right of your screen.

1. From the success message, select **View extensions** to finish installing your extension.
**Note**  
You can also navigate to the installation screen from **Connections** > **Extensions** in the Amazon Quick menu.

Once created, this extension access configuration enables authors and other admins in your organization to deploy your Microsoft Teams Amazon Quick extension within your Microsoft Teams environment.

**Note**  
For your end users to begin using your Microsoft Teams extension, an admin or author must finish deploying a extension after you configure extension access. Notify your authors that they can view, edit, and complete installation of this extension under **Extensions** in the left navigation once it has been shared. To learn how to do this see [Installing your Microsoft Teams extension in the Microsoft Teams extension author guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/teams-extension-author-guide.html#add-extensions-teams).

### Edit Microsoft Teams extension access
<a name="edit-teams-extension-access"></a>

Use these steps to modify the configuration settings of an existing Microsoft Teams extension access.

1. Sign in to the Amazon Quick console.

1. Choose the profile picture icon.

1. From the drop-down menu, select **Manage account**.

1. Under **Permissions**, select **Extension access**.

1. Select the three dot menu icon for the Microsoft Teams extension you need to edit.

1. Select **Edit**.

1. Edit the configuration as required and select **Save** to confirm the changes.

Your changes to the Microsoft Teams extension access configuration are saved and will take effect immediately.

### Delete Microsoft Teams extension access
<a name="delete-teams-extension-access"></a>

Follow these steps to permanently remove a Microsoft Teams extension access configuration. This action cannot be undone.

1. Sign in to the Amazon Quick console.

1. Choose the profile picture icon.

1. From the drop-down menu, select **Manage account**.

1. Under **Permissions**, select **Extension access**.

1. Select the three dot menu icon for the Microsoft Teams Extension you need to delete.

1. Select **Delete**.

1. Enter the word, "confirm", and select **DELETE**.

**Note**  
Deleting a extension access removes access for all users in your M365 tenant and deletes all extensions created for Teams. If delete extension access fails, the admin must switch to the author view and delete the Teams extensions that are using the configured extension access before returning to delete the extension access. 

With Microsoft Teams extension access configured, your team can now use **@Quick** mentions in conversations to access AI assistance, company knowledge, and connectors directly within their Teams environment.