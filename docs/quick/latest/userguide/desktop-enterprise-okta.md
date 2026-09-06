

# Set up enterprise sign-in with Okta for Amazon Quick on desktop
<a name="desktop-enterprise-okta"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

This page walks you through all four steps to set up enterprise sign-in with Okta:

1. Create an OIDC application in Okta and record its values.

1. Add the extension access in the Amazon Quick administration console.

1. Create the extension in the Amazon Quick console.

1. Download, verify, and distribute the desktop application.

**Note**  
Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md).

## Step 1: Create an OIDC application in Okta
<a name="desktop-enterprise-okta-step1"></a>

Register an OIDC native application in Okta. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE, and requests the `openid`, `profile`, `email`, and `offline_access` scopes at sign-in.

For more information, see [Create OpenID Connect app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm) in the Okta documentation.

**To create the Okta OIDC Native Application**

1. In the Okta Admin Console, navigate to **Applications → Applications → Create App Integration**.

1. Select **OIDC - OpenID Connect** as the sign-in method.

1. Select **Native Application** as the application type, then choose **Next**.

1. Configure the following settings:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-okta.html)

1. Choose **Save**.

1. On the **General** tab, note the **Client ID**.

Okta enforces PKCE (S256) automatically for native applications.

**To verify authentication settings**

1. In the app integration, go to the **General** tab.

1. Under **General Settings**, confirm that the application type is **Native**, client authentication is **None** (public client), and PKCE is **Required**.

1. Under **LOGIN**, confirm that `http://localhost:18080` is listed as a redirect URI.

1. Choose **Save** if you made any changes.

Record the following OIDC endpoints. You enter these values, together with the **Client ID** you noted earlier, in Step 2. Replace `<OKTA_DOMAIN>` with your Okta domain (for example, `your-org.okta.com`). For the endpoint reference, see [Authorization Code with PKCE](https://developer.okta.com/docs/guides/implement-grant-type/authcodepkce/main/) in the Okta documentation.


| Field | Value | 
| --- | --- | 
| Client ID | The Client ID from the General tab | 
| Issuer URL | https://<OKTA\_DOMAIN> | 
| Authorization endpoint | https://<OKTA\_DOMAIN>/oauth2/v1/authorize | 
| Token endpoint | https://<OKTA\_DOMAIN>/oauth2/v1/token | 
| JWKS URI | https://<OKTA\_DOMAIN>/oauth2/v1/keys | 

**Use the standard Okta domain, not the admin subdomain**  
Use your standard Okta domain (for example, `your-org.okta.com`) in these endpoints, not the `-admin` subdomain (`your-org-admin.okta.com`) shown in the address bar of the admin console. The `-admin` subdomain does not host the OAuth endpoints, so using it causes sign-in to fail with an HTTP 404 error.

## Step 2: Add the extension access in the Amazon Quick administration console
<a name="w2aac51c11c27c15"></a>

In the Amazon Quick administration console, add an extension access using the OIDC endpoint values and Client ID that you recorded in Step 1.

**To add the extension access**

1. Sign in to the Amazon Quick administration console and choose **Manage account**.

1. In the left navigation pane, under **Permissions**, choose **Extension access**.

1. Choose **Add extension access**.

1. Under **Select Service**, select **Amazon Quick (Desktop application for Quick)**, and then choose **Next**.

1. Enter the extension details using the values you recorded in Step 1:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-okta.html)

1. Choose **Add**.
**Important**  
Verify that all values are correct before you choose **Add**. The extension access configuration cannot be edited after creation. If any value is incorrect, you must delete the extension access and create a new one.

## Step 3: Create the extension in the Amazon Quick console
<a name="w2aac51c11c27c17"></a>

After you add the extension access in the Amazon Quick administration console, create the extension on the **Extensions** page in the Amazon Quick console.

**To create the extension**

1. In the Amazon Quick console, in the left navigation pane, choose **Extensions**. If you don't see **Extensions**, choose **More** to find it.

1. Choose **Add extension**.

1. Select the **Desktop application for Quick** extension access that you created in Step 2, and then choose **Next**.

1. Choose **Create**.

**Important**  
Both Step 2 and Step 3 are required. If you add the extension access but do not create the extension, enterprise sign-in is not available and users see the error: "Enterprise sign-in for Quick Desktop has not been configured for this account."

**Note**  
Creating the extension is a one-time, account-level action. After an administrator creates the extension, enterprise sign-in is available for all users in the account. Individual users do not need to enable the extension themselves — they only need to download the desktop application and sign in.

## Step 4: Download, verify, and distribute the desktop application
<a name="w2aac51c11c27c19"></a>

In this step, you download and install the desktop application, verify that enterprise sign-in works, and then distribute the application to your users.

First, download the application from the Amazon Quick console.

**To download the desktop application**

1. In the Amazon Quick console, in the left navigation pane, choose **Extensions**. If you don't see **Extensions**, choose **More** to find it.

1. Select the Quick Desktop extension that you created in Step 3.

1. Choose the more options icon (**...**) for the extension.

1. Choose **Download for Windows** or **Download for Mac**, depending on your operating system.

Then, install the application. For installation instructions, see [Getting started](getting-started-desktop.md).

After you install the application, verify that enterprise sign-in works.

**To verify enterprise sign-in**

1. Open the Amazon Quick desktop application.

1. On the sign-in screen, choose **Continue with SSO**.

1. (Optional) Select your AWS Region from the list, or choose **Dynamic** to have the application detect your Region automatically.

1. Authenticate with your corporate credentials. The application redirects to your identity provider, and then returns to the Home screen after authentication succeeds.

**Tip**  
If sign-in fails, verify the values you entered in Step 2 against the OIDC endpoints and Client ID from Step 1. If any value is incorrect, delete the extension access under **Permissions → Extension access** in the Amazon Quick administration console, and repeat Step 2 with the correct values. For more help, see [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md).

Finally, after you verify the setup, distribute the application to your users. Direct them to [Getting started](getting-started-desktop.md) for download, installation, and sign-in instructions. Users choose **Continue with SSO** and sign in with their corporate credentials — no additional per-user configuration is required.