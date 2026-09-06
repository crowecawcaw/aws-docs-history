

# Microsoft OneNote integration
<a name="microsoft-onenote-integration"></a>

With the Microsoft OneNote connector, you can manage notebooks, sections, and pages from your Microsoft 365 account directly in Amazon Quick through natural language. The connector uses Microsoft Graph for OneNote operations.

Amazon Quick supports two authentication methods for Microsoft OneNote. Choose the method that best fits your organization's security requirements.
+ **Default OAuth app** – Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their Microsoft 365 account.
+ **Custom OAuth app** – Uses a customer-managed application registered in Microsoft Entra ID. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md).

## Before you begin
<a name="microsoft-onenote-prerequisites"></a>

Make sure that you have the following before you set up the integration.
+ An active Microsoft 365 account with access to the OneNote notebooks that you want to use.
+ For **Custom OAuth app**: Access to Microsoft Entra ID (formerly Azure Active Directory) to register an application and configure Microsoft Graph permissions for OneNote.
+ For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Microsoft Entra ID
<a name="microsoft-onenote-source-setup"></a>

If you are using **Default OAuth app** authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#microsoft-onenote-quicksuite-setup).

For Custom OAuth app authentication, register an application in the [Microsoft Entra admin center](https://entra.microsoft.com/) and configure Microsoft Graph delegated permissions for OneNote. Add the Amazon Quick callback URL `https://{{{region}}}.quicksight.aws.amazon.com/sn/oauthcallback` as a redirect URI. Replace {{{region}}} with your AWS Region (for example, `us-east-1`). For step-by-step instructions, see [Authentication and authorization basics](https://learn.microsoft.com/en-us/graph/auth/auth-concepts) in the Microsoft Graph documentation. Record the Application (client) ID and a client secret value — you need them when you configure Amazon Quick.

Add the following as Delegated permissions in your Entra app registration. For the full permissions reference, see [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference) in the Microsoft documentation.


**OneNote action integration – delegated permissions**  

| Permission | Description | 
| --- | --- | 
| Notes.Create | Allows the app to create OneNote notebooks on behalf of the signed-in user. | 
| Notes.Read | Allows the app to read OneNote notebooks on behalf of the signed-in user. | 
| Notes.Read.All | Allows the app to read all OneNote notebooks that the signed-in user has access to. | 
| Notes.ReadWrite | Allows the app to read and write OneNote notebooks on behalf of the signed-in user. | 
| Notes.ReadWrite.All | Allows the app to read and write all OneNote notebooks that the signed-in user has access to. | 
| Notes.ReadWrite.CreatedByApp | Allows the app to read and write OneNote notebooks created by the app on behalf of the signed-in user. | 
| offline\_access | Allows the app to refresh access tokens without requiring the user to sign in again. This reduces how often users need to re-authenticate. | 
| Sites.Read.All | Allows the app to read documents and list items in all site collections on behalf of the signed-in user. | 
| Team.ReadBasic.All | Allows the app to read the names and descriptions of teams on behalf of the signed-in user. | 
| User.Read | Allows the app to read the signed-in user's profile. | 
| User.ReadBasic.All | Allows the app to read a basic set of profile properties of all users on behalf of the signed-in user. | 

## Setting up the connector in Amazon Quick
<a name="microsoft-onenote-quicksuite-setup"></a>

### Connect from the Available tab
<a name="microsoft-onenote-quick-connect"></a>

If you want to use Default OAuth app authentication, you can connect directly from the **Available** tab without additional configuration.

1. In the Amazon Quick console, choose **Connectors**.

1. On the **Available** tab, find **OneNote** and choose **Connect**.

1. Complete the Microsoft sign-in flow and grant the requested permissions.

To configure a connector with Custom OAuth app instead, use the **Create for your team** tab as described below.

### Create from the Create for your team tab
<a name="microsoft-onenote-full-setup"></a>

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **OneNote**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. For **Connection type**, choose **Public network**.

1. For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.

   1. For **Default OAuth app**:

      No additional credentials are needed. Choose **Next** to continue.

   1. For **Custom OAuth app**, configure the following fields:
      + **Base URL** (Optional) – The Microsoft Graph base URL. Example: `https://graph.microsoft.com/v1.0`
      + **Client ID** – The Application (client) ID from your Microsoft Entra ID app registration.
      + **Public OAuth client** (Optional) – Select this option if your Microsoft Entra ID app is configured as a public client (no client secret).
      + **Client secret** – The client secret value from your Microsoft Entra ID app registration.
      + **Token URL** – The Microsoft identity platform token endpoint. Example: `https://login.microsoftonline.com/common/oauth2/v2.0/token`
      + **Authorization URL** – The Microsoft identity platform authorization endpoint. Example: `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`
      + **Redirect URL** – Pre-filled with the Amazon Quick callback URL.
**Note**  
For tenant-specific authentication, replace `common` in the Token URL and Authorization URL with your Microsoft Entra ID tenant ID.

1. Choose **Next**.

1. A Microsoft sign-in window opens. Review the requested permissions and choose **Accept**.

1. On the **Review** page, review the available actions for the connector. Choose **Next**.

1. On the **Publish** page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.

1. Choose **Publish**.

## Available actions
<a name="microsoft-onenote-actions"></a>

After you set up the connector, the actions exposed by OneNote are available. To see the current set of actions for your connector, go to the connector's **Available actions** view in the Amazon Quick console.

## Managing and troubleshooting
<a name="microsoft-onenote-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

### Authentication issues
<a name="microsoft-onenote-troubleshooting-auth"></a>
+ **Sign-in fails (Default OAuth app or Custom OAuth app)** – Verify that your Microsoft 365 account is active and that you can sign in to OneNote on the web directly. For Custom OAuth app, confirm that the redirect URI in your Microsoft Entra ID app matches the Amazon Quick callback URL.
+ **Insufficient permissions** – Verify that the Microsoft Graph permissions configured on your Microsoft Entra ID app include the OneNote scopes required for the operations you want to use, and that admin consent has been granted if required.
+ **Invalid client credentials (Custom OAuth app)** – Verify that the Client ID and Client secret match the values in your Microsoft Entra ID app registration. Confirm that the client secret has not expired.