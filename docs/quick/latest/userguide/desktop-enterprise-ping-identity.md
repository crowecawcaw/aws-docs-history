# Set up enterprise sign-in with Ping Identity for Amazon Quick on desktop

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

This page walks you through all four steps to set up enterprise sign-in with Ping
Identity:

1. Create an OIDC application in your Ping Identity product (PingFederate or
   PingOne) and record its values.
2. Add the extension access in the Amazon Quick administration console.
3. Create the extension in the Amazon Quick console.
4. Download, verify, and distribute the desktop application.

###### Note

Before you begin, review the prerequisites in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md "desktop-enterprise-setup.md").

## Step 1: Create an OIDC application in Ping Identity

Register a public OIDC client in your Ping Identity product. The Amazon Quick
desktop application uses this client to authenticate users through the authorization
code flow with PKCE. This client requires no client secret. Enable the Refresh Token
grant type and grant the `offline_access` scope. Choose the
instructions for your Ping Identity product.

### PingFederate

For more information, see [Setting up an OIDC application in PingFederate](https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html "https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html") in the Ping
Identity documentation.

###### To create the PingFederate OIDC client

1. In the PingFederate administrative console, go to
   **Applications → OAuth →
   Clients**, and choose **Add
   Client**.
2. In the **Client ID** field, enter
   a unique identifier for this client.
3. In the **Name** field, enter
   `Amazon Quick Desktop`.
4. For **Client Authentication**,
   select **None**.
5. In the **Redirection URI**
   section, enter `http://localhost:18080` and choose
   **Add**.
6. In the **Allowed Grant Types**
   list, select **Authorization Code**
   and **Refresh Token**.
7. Select the **Require Proof Key for Code
   Exchange (PKCE)** checkbox.
8. Under **Common Scopes**, grant
   the following: `openid`, `email`,
   `profile`, `offline_access`.
9. Choose **Save**.
10. Note the **Client ID**. You need
    this value in later steps.

###### To configure the OIDC policy

1. In the PingFederate administrative console, go to
   **Applications → OAuth → OpenID
   Connect Policy Management**.
2. Select the OIDC policy associated with this client, or choose
   **Add Policy** to create
   one.
3. Select the **Return ID Token On Refresh
   Grant** checkbox. This ensures that the desktop
   application receives a fresh ID token with current claims when
   refreshing the session.
4. Under **Attribute Contract**,
   verify that the `email` claim is included and mapped
   to the corresponding user attribute in your authentication
   source. The `email` claim must be present in tokens
   issued during both initial authentication and refresh token
   grants.
5. Choose **Save**.

Record the following OIDC endpoints. You enter these values, together with the
**Client ID** you noted earlier, in Step 2. Replace
`<PINGFEDERATE_HOST>` with your PingFederate server
hostname.

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| Client ID              | The *_Client ID_<br>• you entered when<br>you created the client |
| Issuer URL             | `https://<PINGFEDERATE_HOST>`                                    |
| Authorization endpoint | `https://<PINGFEDERATE_HOST>/as/authorization.oauth2`            |
| Token endpoint         | `https://<PINGFEDERATE_HOST>/as/token.oauth2`                    |
| JWKS URI               | `https://<PINGFEDERATE_HOST>/pf/JWKS`                            |

### PingOne

For more information, see [Editing an application – Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html "https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html") in the Ping Identity
documentation.

###### To create the PingOne OIDC native application

1. In the PingOne admin console, go to **Applications → Applications** and choose the
   **+** icon.
2. Enter `Amazon Quick Desktop` as the application
   name.
3. In the **Application Type**
   section, select **Native**, then
   choose **Save**.
4. On the **Configuration** tab,
   choose **Edit** and configure the
   following settings:

| Setting                              | Value                                |
| ------------------------------------ | ------------------------------------ |
| Response Type                        | Code                                 |
| Grant Type                           | Authorization Code and Refresh Token |
| PKCE Enforcement                     | S256                                 |
| Redirect URIs                        | `http://localhost:18080`             |
| Token Endpoint Authentication Method | None                                 |

5. Choose **Save**.
6. On the **Resources** tab, add the
   following scopes: `openid`, `email`,
   `profile`, `offline_access`.
7. On the **Attribute Mappings** tab,
   verify that the `email` attribute is mapped to the
   user's email address.
8. Toggle the application to **Enabled**.
9. Note the **Client ID** and
   **Environment ID** from the
   **Configuration** tab.

###### Note

The PingOne domain varies by region. The following examples use
`.com`. Replace the domain with the one for your
environment (for example, `.ca`, `.eu`, or
`.asia`).

Record the following OIDC endpoints. You enter these values, together with the
**Client ID** you noted earlier, in Step 2. Replace
`<ENV_ID>` with your PingOne environment ID.

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| Client ID              | The *_Client ID_<br>• from the<br>*_Configuration_<br>• tab |
| Issuer URL             | `https://auth.pingone.com/<ENV_ID>/as`                      |
| Authorization endpoint | `https://auth.pingone.com/<ENV_ID>/as/authorize`            |
| Token endpoint         | `https://auth.pingone.com/<ENV_ID>/as/token`                |
| JWKS URI               | `https://auth.pingone.com/<ENV_ID>/as/jwks`                 |

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
