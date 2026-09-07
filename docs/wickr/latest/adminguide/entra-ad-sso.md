

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Configure AWS Wickr with Microsoft Entra (Azure AD) single sign-on
<a name="entra-ad-sso"></a>

AWS Wickr can be configured to use Microsoft Entra (Azure AD) as an identity provider. To do so, complete the following procedures in both Microsoft Entra and the AWS Wickr admin console.

**Warning**  
After SSO is enabled on a network it will sign active users out of Wickr and force them to re-authenticate using the SSO provider.

## Step 1: Register AWS Wickr as an application in Microsoft Entra
<a name="step-1-entra-wickr-application"></a>

Complete the following procedure to register AWS Wickr as an application in Microsoft Entra.

**Note**  
Refer to the Microsoft Entra documentation for detailed screenshots and troubleshooting. For more information, see [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

1. In the navigation pane, choose **Applications** and then choose **App Registrations**.

1. On the **App Registrations** page, choose **Register an application**, and then enter an application name.

1. Select **Accounts in this organizational directory only (Default Directory only - Single tenant)**.

1. Under **Redirect URI**, select **Web**, and then enter the redirect URI available in SSO configuration settings in the AWS Wickr Admin console

1. Choose **Register**.

1. After registration, copy/save the Application (Client) ID generated.  
![Client application ID image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/application-client-id.png)

1. Select the **Endpoints** tab to make a note of the following:

   1. Oauth 2.0 authorization endpoint (v2): E.g.: `https://login.microsoftonline.com/1ce43025-e4b1-462d-a39f-337f20f1f4e1/oauth2/v2.0/authorize` 

   1. Edit this value to remove the 'oauth2/" and "authorize". E.g. fixed URL will look like this: `https://login.microsoftonline.com/1ce43025-e4b1-462d-a39f-337f20f1f4e1/v2.0/`

   1. This will be referenced as the **SSO Issuer**.

## Step 2: Setup authentication
<a name="step-2-entra-setup-authentication"></a>

Complete the following procedure to setup authentication in Microsoft Entra.

1. In the navigation pane, choose **Authentication**.

1. On the **Authentication** page, make sure that the **Web Redirect URI** is the same as entered previously (in *Register AWS Wickr as an Application*).  
![Client authentication image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/authentication.png)

1. Select **Access tokens used for implicit flows** and **ID tokens used for implicit and hybrid flows**.

1. Choose **Save**.  
![Request an access token image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/access-tokens.png)

## Step 3: Setup certificates and secrets
<a name="step-3-entra-setup-certificates"></a>

Complete the following procedure to setup certificates and secrets in Microsoft Entra.

1. In the navigation pane, choose **Certificates & secrets**.

1. On the **Certificates & secrets** page, select the **Client secrets** tab.

1. Under the **Client secrets** tab, select **New client secret**.

1. Enter a description and select an expiration period for the secret.

1. Choose **Add**.  
![Add client secret image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-create-client-secret.png)

1. After the certificate is created, copy the **Client secret value**.  
![An example of a client secret value.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-client-secret-value.png)
**Note**  
The client secret value (not Secret ID) will be required for your client application code. You may not be able to view or copy the secret value after leaving this page. If you do not copy it now, you will have to go back to create a new client secret.

## Step 4: Setup token configuration
<a name="step-4-entra-setup-token"></a>

Complete the following procedure to setup token configuration in Microsoft Entra.

1. In the navigation pane, choose **Token configuration**.

1. On the **Token configuration** page, choose **Add optional claim**.

1. Under **Optional claims**, select the **Token type** as **ID**.

1. After selecting **ID**, under **Claim**, select **email** and **upn**.

1. Choose **Add**.  
![Token type image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-token-type.png)

## Step 5: Setup API permissions
<a name="step-5-entra-setup-api-permissions"></a>

Complete the following procedure to setup API permissions in Microsoft Entra.

1. In the navigation pane, choose **API permissions**.

1. On the **API permissions** page, choose **Add a permission**.  
![Add an permission image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-api-permissions.png)

1. Select **Microsoft Graph ** and then select **Delegated Permissions **.

1. Select the checkbox for **email **, **offline\_access**, **openid**, **profile**.

1. Choose **Add permissions**.

## Step 6: Expose an API
<a name="step-6-entra-expose-api"></a>

Complete the following procedure to expose an API for each of the 4 scopes in Microsoft Entra.

1. In the navigation pane, choose **Expose an API**.

1. On the **Expose an API** page, choose **Add a scope**.  
![Expose an API image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-expose-an-api.png)

   **Application ID URI** should auto populate, and the ID that follows the URI should match the **Application ID** (created in *Register AWS Wickr as an application*).  
![Add a scope image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-add-scope.png)

1. Choose **Save and continue**.

1. Select the **Admins and users** tag, and then enter the scope name as **offline\_access**.

1. Select **State**, and then select **Enable**.

1. Choose **Add scope**.

1. Repeat steps 1—6 of this section to add the following scopes: **email**, **openid**, and **profile**.  
![Add scopes image.](http://docs.aws.amazon.com/wickr/latest/adminguide/images/entra-scopes-api.png)

1. Under **Authorized client applications**, choose **Add a client application**.

1. Select all four scopes created in the previous step.

1. Enter or verify the **Application (client) ID**.

1. Choose **Add application**.

## Step 7: AWS Wickr SSO configuration
<a name="step-7-wickr-sso-configuration"></a>

Complete the following configuration procedure in the AWS Wickr console.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks page**, select the network name to navigate to that network. 

1. In the navigation pane, choose **User management**, and then choose **Configure SSO**.

1. Enter the following details:
   + **Issuer** — This is the endpoint that was modified previously (E.g. `https://login.microsoftonline.com/1ce43025-e4b1-462d-a39f-337f20f1f4e1/v2.0/`).
   + ** Client ID** — This is the **Application (client) ID** from the **Overview** pane.
   + **Client secret (optional)** — This is the **Client secret** from the **Certificates & secrets** pane.
   + **Scopes** — These are the scope names exposed on the **Expose an API** pane. Enter **email**, **profile**, **offline\_access**, and **openid**.
   + **Custom username scope (optional)** — Enter **upn**.
   + **Company ID ** — This can be a unique text value including alphanumeric and underscore characters. This phrase is what your users will enter when registering on new devices.

   *Other fields are optional.*

1. Choose **Next**.

1. Verify the details in the **Review and save** page, and then choose **Save changes**.

SSO configuration is complete. To verify, you can now add a user to the application in Microsoft Entra, and login with the user using SSO and Company ID.

For more information on how to invite and onboard users, see [Create and invite users](https://docs.aws.amazon.com/wickr/latest/adminguide/getting-started.html#getting-started-step3).

## Troubleshooting
<a name="troubleshooting"></a>

Following are common issues you might encounter and suggestions for resolving them.
+ SSO Connection test fails or is unresponsive: 
  + Make sure the **SSO Issuer** is configured as expected.
  + Make sure the required fields in the **SSO Configured** are set as expected.
+ Connection test is successful, but the user is unable to login: 
  + Make sure the user is added to the Wickr application you registered in Microsoft Entra.
  + Make sure the user is using the correct company ID, including the prefix. *E.g. UE1-DemoNetworkW\_drqtva*.
  + The **Client Secret** may not be set correctly in the **AWS Wickr SSO Configuration**. Re-set it by creating another **Client secret** in Microsoft Entra and set the new **Client secret** in the **Wickr SSO Configuration**.