# Set up enterprise sign-in with Okta for Amazon Quick on desktop

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

This page walks you through all four steps to set up enterprise sign-in with
Okta:

1. Create an OIDC application in Okta and record its values.
2. Add the extension access in the Amazon Quick administration console.
3. Create the extension in the Amazon Quick console.
4. Download, verify, and distribute the desktop application.

###### Note

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md "desktop-enterprise-setup.md").

## Step 1: Create an OIDC application in Okta

Register an OIDC native application in Okta. The Amazon Quick desktop application
uses this client to authenticate users through the authorization code flow with PKCE.
This client requires no client secret. Enable the Refresh Token grant type and grant
the `offline_access` scope so that the application can maintain long-lived
sessions.

For more information, see [Create OpenID Connect app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm "https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm") in the Okta
documentation.

###### To create the Okta OIDC Native Application

1. In the Okta Admin Console, navigate to **Applications → Applications → Create App
   Integration**.
2. Select **OIDC - OpenID Connect** as the
   sign-in method.
3. Select **Native Application** as the
   application type, then choose **Next**.
4. Configure the following settings:

| Setting               | Value                                     |
| --------------------- | ----------------------------------------- |
| App integration name  | `Amazon Quick Desktop`                    |
| Grant type            | Authorization Code and Refresh Token      |
| Sign-in redirect URIs | `http://localhost:18080`                  |
| Assignments           | Assign to the appropriate users or groups |

5. Choose **Save**.
6. On the **General** tab, note the
   **Client ID**.

Okta enforces PKCE (S256) automatically for native applications.

###### To configure scopes

1. In the Okta Admin Console, navigate to **Security → API → Authorization Servers** and
   select your authorization server (for example, **default**).
2. On the **Scopes** tab, verify that
   the following scopes are enabled: `openid`,
   `email`, `profile`,
   `offline_access`.
3. On the **Access Policies** tab,
   verify that the policy assigned to this application allows the
   `Authorization Code` and `Refresh Token`
   grant types.

###### To verify authentication settings

1. In the app integration, go to the **General** tab.
2. Under **General Settings**, confirm that
   the application type is **Native**, client
   authentication is **None** (public client),
   and PKCE is **Required**.
3. Under **LOGIN**, confirm that
   `http://localhost:18080` is listed as a redirect URI.
4. Choose **Save** if you made any
   changes.

Record the following OIDC endpoints. You enter these values, together with the
**Client ID** you noted earlier, in Step 2. Replace
`<OKTA_DOMAIN>` with your Okta domain (for example,
`your-org.okta.com`).

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| Client ID              | The *_Client ID_<br>• from the<br>*_General_<br>• tab |
| Issuer URL             | `https://<OKTA_DOMAIN>/oauth2/default`                |
| Authorization endpoint | `https://<OKTA_DOMAIN>/oauth2/default/v1/authorize`   |
| Token endpoint         | `https://<OKTA_DOMAIN>/oauth2/default/v1/token`       |
| JWKS URI               | `https://<OKTA_DOMAIN>/oauth2/default/v1/keys`        |

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
