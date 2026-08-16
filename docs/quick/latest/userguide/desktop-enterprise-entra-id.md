# Set up enterprise sign-in with Microsoft Entra ID for Amazon Quick on desktop

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

This page walks you through all four steps to set up enterprise sign-in with Microsoft
Entra ID:

1. Create an OIDC application in Microsoft Entra ID and record its values.
2. Add the extension access in the Amazon Quick administration console.
3. Create the extension in the Amazon Quick console.
4. Download, verify, and distribute the desktop application.

###### Note

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md "desktop-enterprise-setup.md").

## Step 1: Create an OIDC application in Microsoft Entra ID

Register a public OIDC client application in Microsoft Entra ID. The Amazon Quick
desktop application uses this client to authenticate users through the authorization
code flow with PKCE. This client requires no client secret. Grant the
`offline_access` scope so that the application can issue refresh tokens.
Without it, users must re-authenticate frequently.

For more information, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app "https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app") in the Microsoft Entra documentation.

###### To create the Entra ID app registration

1. In the Azure portal, navigate to **Microsoft Entra
   ID → App registrations → New registration**.
2. Configure the following settings:

| Setting                 | Value                                                             |
| ----------------------- | ----------------------------------------------------------------- |
| Name                    | `Amazon Quick Desktop`                                            |
| Supported account types | Accounts in this organizational directory only<br>(Single tenant) |
| Redirect URI platform   | Public client/native (mobile & desktop)                           |
| Redirect URI            | `http://localhost:18080`                                          |

3. Choose **Register**.
4. On the **Overview** page, note the
   **Application (client) ID** and
   **Directory (tenant) ID**. You need these
   values in later steps.

This is a public client registration. Entra ID enforces PKCE automatically for
public clients.

###### To configure API permissions

1. In the app registration, navigate to **API
   permissions → Add a permission → Microsoft Graph →
   Delegated permissions**.
2. Add the following permissions: `openid`,
   `email`, `profile`,
   `offline_access`.
3. Choose **Add permissions**.
4. If your organization requires it, choose **Grant
   admin consent for [your organization]**.

###### To configure authentication settings

1. In the app registration, navigate to **Authentication**.
2. Under **Advanced settings**, set
   **Allow public client flows** to
   **Yes**.
3. Verify that `http://localhost:18080` is listed under
   **Mobile and desktop applications**.
4. Choose **Save**.

###### To configure token claims

1. In the app registration, navigate to **Token configuration**.
2. Choose **Add optional claim**.
3. Select token type: **ID**.
4. Select the `email` claim and choose
   **Add**.

###### Important

This step is required. Without the `email` optional claim,
Microsoft Entra ID does not include the user's email address in the ID
token, and Amazon Quick cannot map the token to a user. Additionally,
each user who signs in must have their **Mail** attribute populated in their Entra ID profile (under
**Contact Information**). The User Principal
Name (UPN) alone is not sufficient — the Mail attribute must contain
a value.

Record the following OIDC endpoints. You enter these values, together with the
**Application (client) ID** you noted earlier, in
Step 2. Replace `<TENANT_ID>` with your Directory (tenant) ID.

###### Important

The Issuer URL must include the `/v2.0` path suffix. Do not
use the **Authority URL** shown in the Entra ID Endpoints panel, which omits
this suffix. If the `/v2.0` suffix is missing, token validation
fails with an "Invalid issuer" error at sign-in time.

| Field                  | Value                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------- |
| Client ID              | The *_Application (client) ID_<br>• from the<br>app registration *_Overview_<br>• page |
| Issuer URL             | `https://login.microsoftonline.com/<TENANT_ID>/v2.0`                                   |
| Authorization endpoint | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize`                  |
| Token endpoint         | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token`                      |
| JWKS URI               | `https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys`                    |

###### Tip

The JWKS URI is not displayed in the Microsoft Entra ID
**Endpoints** panel. You can find it by
opening the **OpenID Connect metadata
document** URL from the Endpoints panel and locating the
`jwks_uri` field in the JSON response. Alternatively,
construct it using the format shown in the preceding table.

###### Important

If your application has custom signing keys because of the
claims-mapping feature, you must append an `appid` query
parameter containing the **Application (client)
ID** to the JWKS URI. Otherwise, token validation fails because
the default keys endpoint does not return the application's custom signing
key. For example:

`https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys?appid=<CLIENT_ID>`

To confirm the correct value, open the OpenID Connect metadata document
with the same `appid` parameter appended
(`https://login.microsoftonline.com/<TENANT_ID>/.well-known/openid-configuration?appid=<CLIENT_ID>`)
and use the `jwks_uri` it returns. For more information, see
[Validate the signature](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens#validate-the-signature "https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens#validate-the-signature") in the Microsoft Entra documentation.

## Step 2: Add the extension access in the Amazon Quick administration console

In the Amazon Quick administration console, add an extension access using the OIDC
endpoint values and Client ID that you recorded in Step 1.

###### To add the extension access

1. Sign in to the Amazon Quick administration console and choose
   **Manage account**.
2. In the left navigation pane, under **Permissions**,
   choose **Extension access**.
3. Choose **Add extension access**.
4. Under **Select Service**, select
   **Amazon Quick (Desktop application for
   Quick)**, and then choose **Next**.
5. Enter the extension details using the values you recorded in Step 1:

| Field                  | Value                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                   | A name for this extension access (for example,<br>`QuickDesktop-access`). This is an internal reference<br>only and is not configured in your IdP. Use alphanumeric<br>characters and hyphens only, with no spaces. |
| Description            | (Optional) A description of this extension access, for your<br>reference only.                                                                                                                                      |
| Issuer URL             | The exact OIDC issuer URL from Step 1, including any required<br>path suffix.                                                                                                                                       |
| Authorization Endpoint | The OIDC authorization endpoint URL from Step 1                                                                                                                                                                     |
| Token Endpoint         | The OIDC token endpoint URL from Step 1                                                                                                                                                                             |
| JWKS URI               | The JSON Web Key Set URI from Step 1                                                                                                                                                                                |
| Client ID              | The OIDC client identifier (Client ID or Application (client)<br>ID) that you recorded in Step 1. Required.                                                                                                         |

6. Choose **Add**.

###### Important

Verify that all values are correct before you choose
**Add**. The extension access
configuration cannot be edited after creation. If any value is
incorrect, you must delete the extension access and create a new
one.

## Step 3: Create the extension in the Amazon Quick console

After you add the extension access in the Amazon Quick administration console, create
the extension on the **Extensions** page in the Amazon Quick console.

###### To create the extension

1. In the Amazon Quick console, in the left navigation pane, choose
   **Extensions**. If you don't see
   **Extensions**, choose
   **More** to find it.
2. Choose **Add extension**.
3. Select the **Desktop application for
   Quick** extension access that you created in Step 2, and then
   choose **Next**.
4. Choose **Create**.

###### Important

Both Step 2 and Step 3 are required. If you add the extension access but do not
create the extension, enterprise sign-in is not available and users see the error:
"Enterprise sign-in for Quick Desktop has not been configured for this
account."

###### Note

Creating the extension is a one-time, account-level action. After an
administrator creates the extension, enterprise sign-in is available
for all users in the account. Individual users do not need to enable
the extension themselves — they only need to download the desktop
application and sign in.

## Step 4: Download, verify, and distribute the desktop application

In this step, you download and install the desktop application, verify that enterprise
sign-in works, and then distribute the application to your users.

First, download the application from the Amazon Quick console.

###### To download the desktop application

1. In the Amazon Quick console, in the left navigation pane, choose
   **Extensions**. If you don't see
   **Extensions**, choose
   **More** to find it.
2. Select the Quick Desktop extension that you created in Step 3.
3. Choose the more options icon (**...**) for the
   extension.
4. Choose **Download for Windows** or
   **Download for Mac**, depending on your operating
   system.

Then, install the application. For installation instructions, see [Getting started](getting-started-desktop.md "getting-started-desktop.md").

After you install the application, verify that enterprise sign-in works.

###### To verify enterprise sign-in

1. Open the Amazon Quick desktop application.
2. On the sign-in screen, choose **Continue with
   SSO**.
3. (Optional) Select your AWS Region from the list, or choose
   **Dynamic** to have the application detect
   your Region automatically.
4. Authenticate with your corporate credentials. The application redirects
   to your identity provider, and then returns to the Home screen after
   authentication succeeds.

###### Tip

If sign-in fails, verify the values you entered in Step 2 against the OIDC
endpoints and Client ID from Step 1. If any value is incorrect, delete the
extension access under **Permissions → Extension
access** in the Amazon Quick administration console, and repeat Step 2 with the
correct values. For more help, see [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md "desktop-enterprise-setup-troubleshooting.md").

Finally, after you verify the setup, distribute the application to your users. Direct
them to [Getting started](getting-started-desktop.md "getting-started-desktop.md") for download, installation, and sign-in
instructions. Users choose **Continue with SSO** and sign in
with their corporate credentials — no additional per-user configuration is
required.
