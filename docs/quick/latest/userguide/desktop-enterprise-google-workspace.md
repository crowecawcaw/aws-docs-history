

# Set up enterprise sign-in with Google Workspace for Amazon Quick on desktop
<a name="desktop-enterprise-google-workspace"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

This page walks you through all four steps to set up enterprise sign-in with Google Workspace:

1. Create an OIDC application in Google Workspace and record its values.

1. Add the extension access in the Amazon Quick administration console.

1. Create the extension in the Amazon Quick console.

1. Download, verify, and distribute the desktop application.

**Note**  
Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md).

## Step 1: Create an OIDC application in Google Workspace
<a name="desktop-enterprise-google-workspace-step1"></a>

Register an OAuth client in the Google Cloud Console. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE. Google issues a refresh token automatically when the authorization request includes the `access_type=offline` parameter. Quick includes this parameter automatically. No additional scope or grant type configuration is required.

For more information, see [OAuth 2.0 for Mobile & Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app) in the Google for Developers documentation.

**To create the Google OAuth client**

1. In the Google Cloud Console, navigate to **APIs & Services → Credentials → Create Credentials → OAuth client ID**.

1. Configure the following settings:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-google-workspace.html)

1. Choose **Create**.

1. Note the **Client ID** and **Client secret**. You need these values in later steps.

**To configure the OAuth consent screen**

1. In the Google Cloud Console, navigate to **Google Auth Platform → Branding**.

1. Set the **User type** to **Internal**. This restricts sign-in to users in your Google Workspace organization.

1. Fill in the required app information and choose **Save**.

**To configure scopes**

1. In the Google Cloud Console, navigate to **Google Auth Platform → Data Access**.

1. Add the following scopes: `openid`, `email`, `profile`.

1. Choose **Save**.

Record the following OIDC endpoints. You enter these values, together with the **Client ID** you noted earlier, in Step 2.


| Field | Value | 
| --- | --- | 
| Client ID | The Client ID from your OAuth client | 
| Issuer URL | https://accounts.google.com | 
| Authorization endpoint | https://accounts.google.com/o/oauth2/v2/auth | 
| Token endpoint | https://oauth2.googleapis.com/token?client\_secret=<CLIENT\_SECRET> | 
| JWKS URI | https://www.googleapis.com/oauth2/v3/certs | 

**Note**  
Append your client secret to the token endpoint as a `client_secret` query parameter so that token exchange succeeds—for example, `https://oauth2.googleapis.com/token?client_secret=<CLIENT_SECRET>`. Replace `<CLIENT_SECRET>` with the client secret generated for your OAuth client.

## Step 2: Add the extension access in the Amazon Quick administration console
<a name="w2aac51c11c25c15"></a>

In the Amazon Quick administration console, add an extension access using the OIDC endpoint values and Client ID that you recorded in Step 1.

**To add the extension access**

1. Sign in to the Amazon Quick administration console and choose **Manage account**.

1. In the left navigation pane, under **Permissions**, choose **Extension access**.

1. Choose **Add extension access**.

1. Under **Select Service**, select **Amazon Quick (Desktop application for Quick)**, and then choose **Next**.

1. Enter the extension details using the values you recorded in Step 1:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-google-workspace.html)

1. Choose **Add**.
**Important**  
Verify that all values are correct before you choose **Add**. The extension access configuration cannot be edited after creation. If any value is incorrect, you must delete the extension access and create a new one.

## Step 3: Create the extension in the Amazon Quick console
<a name="w2aac51c11c25c17"></a>

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
<a name="w2aac51c11c25c19"></a>

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