# Salesforce integration

With the Salesforce action connector in Amazon Quick, you can perform actions
within Salesforce organizations, including managing records, querying data, and
interacting with Salesforce APIs. For Amazon Quick subscription requirements,
see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

###### Note

As of the Salesforce Spring '26 release (February 2026), new Connected
App creation is disabled by default across all Salesforce organizations.
This guide uses Salesforce's External Client Apps (ECAs), which are fully
compatible with the Amazon Quick Salesforce connector.

## Prerequisites

Before you set up the Salesforce integration, make sure you have the
following:

- A Salesforce organization with System Administrator access.
- Amazon Quick Author role or higher.
- Your Amazon Quick instance URL (for example,
  `https://us-east-1.quicksight.aws.amazon.com`).

## Step 1: Create an External Client App in Salesforce

Create an External Client App (ECA) in Salesforce to enable OAuth
authentication with Amazon Quick.

### Navigate to External Client App Manager

1. Sign in to your Salesforce organization and choose
   **Setup** (gear icon in the top
   right).
2. In the navigation pane, expand **Platform
   Tools** > **Apps** >
   **External Client Apps** >
   **External Client App Manager**.
3. Choose **New External Client App**.

### Fill in basic information

Enter the following basic information for your External Client
App:

External Client App basic information| Field | Value |
| --- | --- |
| **External Client App Name** | A descriptive name (for example, "Amazon Quick<br>Integration") |
| **API Name** | Auto-generated from the app name |
| **Contact Email** | Your admin email address |
| **Distribution State** | Local (default) |

## Step 2: Configure OAuth settings

### Enable OAuth

In the **API (Enable OAuth Settings)** section, select
**Enable OAuth** to expand the OAuth configuration
panel.

### Set callback URL

Enter the Amazon Quick OAuth callback URL in the **Callback
URL** field:

``<your-quick-instance-url>`/sn/oauthcallback`

For example:
`https://us-east-1.quicksight.aws.amazon.com/sn/oauthcallback`

### Add OAuth scopes

Move the following scopes from **Available OAuth
Scopes** to **Selected OAuth Scopes**:

- Access the identity URL service (id, profile, email, address,
  phone)
- Manage user data via APIs (api)
- Manage user data via Web browsers (web)
- Full access (full)
- Access Visualforce applications (visualforce)
- Perform requests at any time (refresh\_token,
  offline\_access)
- Access unique user identifiers (openid)
- Access custom permissions (custom\_permissions)
- Access Connect REST API resources (chatter\_api)
- Access Analytics REST API resources (wave\_api)
- Access Analytics REST API Charts Geodata resources
  (eclair\_api)
- Manage Pardot services (pardot\_api)

### Enable OAuth flows

Select the following flow options:

- **Enable Client Credentials Flow**
- **Enable Authorization Code and Credentials
  Flow**
- **Enable Token Exchange Flow**

### Enable security settings

Select the following security options:

- **Require Proof Key for Code Exchange
  (PKCE)**
- **Require Secret for Web Server Flow**
  (selected by default)
- **Require Secret for Refresh Token Flow**
  (selected by default)

Choose **Create** to save the External Client
App.

## Step 3: Get consumer credentials

1. After creation, you are on the ECA detail page.
2. Navigate to the **Settings** tab or choose
   **Manage Consumer Details**.
3. You might need to verify your identity (email verification
   code).
4. Copy the **Consumer Key** (Client ID) and
   **Consumer Secret** (Client Secret).

###### Important

Save these credentials securely. You need them when you configure
the connector in Amazon Quick.

## Step 4: Configure Salesforce connector in Amazon Quick

### Navigate to Connectors

1. Open Amazon Quick and choose
   **Connectors**.
2. Choose the **Create for your team**
   tab.
3. Find and choose **Salesforce**.
4. If prompted that a connector already exists, choose
   **No, create new**.

### Fill in connection details

Enter the following connection details:

Salesforce connector connection details| Field | Value |
| --- | --- |
| **Name** | A descriptive name (for example, "Salesforce<br>ECA") |
| **Network** | Public network |
| **Auth Type** | Custom OAuth app |
| **Base URL** | `https://`<your-domain>`.my.salesforce.com/services/data/v60.0` |
| **Client ID** | Consumer Key from Step 3 |
| **Client Secret** | Consumer Secret from Step 3 |
| **Token URL** | `https://`<your-domain>`.my.salesforce.com/services/oauth2/token` |
| **Authorization URL** | `https://`<your-domain>`.my.salesforce.com/services/oauth2/authorize` |
| **Redirect URL** | Pre-filled (do not change) |

Choose **Next** to proceed.

## Step 5: Verify and publish

1. On the **Review** page, verify the available
   Salesforce actions (up to 42 actions).
2. Choose **Next** to proceed to user
   sharing.
3. Select users or groups who should have access to this
   connector.
4. Choose **Publish** to publish the
   connector.

After you publish the connector, you can use Salesforce actions in
Amazon Quick chat, flows, and automations.

## Available actions

After you set up the connector, the following Salesforce actions are
available:

- Create, read, update, and delete (CRUD) operations on standard
  and custom objects.
- Query Salesforce data using SOQL (Salesforce Object Query
  Language).
- Manage leads, accounts, contacts, and opportunities.
- Execute Apex methods and custom logic.
- Manage cases, tasks, and activities.
- Access reports and dashboards.

###### Note

Salesforce integration supports action execution only. Data access
and knowledge base creation are not available for Salesforce
systems.

## Troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

- **"URL no longer exists" error** –
  Ensure you are using the correct Salesforce domain in the Token URL
  and Authorization URL. Do not use legacy endpoints.
- **OAuth validation fails** – Verify
  that PKCE is enabled on the ECA and that the Callback URL exactly
  matches your Amazon Quick instance URL with
  `/sn/oauthcallback` appended.
- **Missing scopes error** – Go back
  to the ECA configuration in Salesforce and ensure all required OAuth
  scopes are in the **Selected** list, not still in
  **Available**.
- **"Connected App" option greyed
  out** – This is expected after Salesforce Spring '26.
  Use an External Client App instead. ECAs are the supported
  replacement.
