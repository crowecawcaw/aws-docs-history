

# Salesforce integration
<a name="salesforce-integration"></a>

With the Salesforce connector in Amazon Quick, you can perform actions within Salesforce organizations, including managing records, querying data, and interacting with Salesforce APIs. For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

Amazon Quick supports two OAuth flows for Salesforce:


**Salesforce authentication flows**  

| Flow | Description | 
| --- | --- | 
| User authentication (three-legged OAuth, 3LO) | Authorization code flow. Each user authenticates through a browser. Best for multi-user environments where actions run on behalf of the signed-in user. | 
| Service authentication (two-legged OAuth, 2LO) | Client credentials flow. Machine-to-machine authentication with no user interaction. All actions run as a designated "Run As" user that you configure in Salesforce. | 

**Note**  
As of the Salesforce Spring '26 release (February 2026), new Connected App creation is disabled by default across all Salesforce organizations. This guide uses Salesforce's External Client Apps (ECAs), which are fully compatible with the Amazon Quick Salesforce connector.

## Prerequisites
<a name="salesforce-integration-prerequisites"></a>

Before you set up the Salesforce integration, make sure you have the following:
+ A Salesforce organization with System Administrator access.
+ Amazon Quick Author role or higher.
+ Your Amazon Quick instance URL (for example, `https://us-east-1.quicksight.aws.amazon.com`).

## Step 1: Create an External Client App in Salesforce
<a name="salesforce-eca-setup"></a>

Create an External Client App (ECA) in Salesforce to enable OAuth authentication with Amazon Quick.

### Navigate to External Client App Manager
<a name="salesforce-eca-navigate"></a>

1. Sign in to your Salesforce organization and choose **Setup** (gear icon in the top right).

1. In the navigation pane, expand **Platform Tools** > **Apps** > **External Client Apps** > **External Client App Manager**.

1. Choose **New External Client App**.

### Fill in basic information
<a name="salesforce-eca-basic-info"></a>

Enter the following basic information for your External Client App:


**External Client App basic information**  

| Field | Value | 
| --- | --- | 
| External Client App Name | A descriptive name (for example, "Amazon Quick Integration") | 
| API Name | Auto-generated from the app name | 
| Contact Email | Your admin email address | 
| Distribution State | Local (default) | 

## Step 2: Configure OAuth settings
<a name="salesforce-oauth-setup"></a>

### Enable OAuth
<a name="salesforce-enable-oauth"></a>

In the **API (Enable OAuth Settings)** section, select **Enable OAuth** to expand the OAuth configuration panel.

### Set callback URL
<a name="salesforce-callback-url"></a>

Enter the Amazon Quick OAuth callback URL in the **Callback URL** field:

`{{<your-quick-instance-url>}}/sn/oauthcallback`

For example: `https://us-east-1.quicksight.aws.amazon.com/sn/oauthcallback`

### Add OAuth scopes
<a name="salesforce-oauth-scopes"></a>

Move the following scopes from **Available OAuth Scopes** to **Selected OAuth Scopes**:
+ Access the identity URL service (id, profile, email, address, phone)
+ Manage user data via APIs (api)
+ Manage user data via Web browsers (web)
+ Full access (full)
+ Access Visualforce applications (visualforce)
+ Perform requests at any time (refresh\_token, offline\_access)
+ Access unique user identifiers (openid)
+ Access custom permissions (custom\_permissions)
+ Access Connect REST API resources (chatter\_api)
+ Access Analytics REST API resources (wave\_api)
+ Access Analytics REST API Charts Geodata resources (eclair\_api)
+ Manage Pardot services (pardot\_api)

### Enable OAuth flows
<a name="salesforce-oauth-flows"></a>

Select the following flow options:

**For both user authentication (3LO) and service authentication (2LO):**
+ **Enable Client Credentials Flow**
+ **Enable Authorization Code and Credentials Flow**
+ **Enable Token Exchange Flow**

**For user authentication (3LO) only:**
+ **Require user credentials in the POST body for Authorization Code and Credentials Flow**. This setting sends user credentials in the POST body during authorization code exchange. It applies only to user authentication and has no effect on service authentication.

**Note**  
If you plan to use only service authentication (2LO), you do not need to select **Require user credentials in the POST body for Authorization Code and Credentials Flow**.

### Enable security settings
<a name="salesforce-security-settings"></a>

Select the following security options:

**For user authentication (3LO):**
+ **Require Proof Key for Code Exchange (PKCE)**. Select this option.
+ **Require Secret for Web Server Flow** (selected by default)
+ **Require Secret for Refresh Token Flow** (selected by default)

**For service authentication (2LO):**
+ **Require Proof Key for Code Exchange (PKCE)**. Clear this option. PKCE is designed for browser-based authorization code flows and is incompatible with client credentials.
+ **Require Secret for Web Server Flow** (selected by default)
+ **Require Secret for Refresh Token Flow** (selected by default)

**Important**  
If you need to support both user authentication (3LO) and service authentication (2LO) on the same External Client App, clear the **Require Proof Key for Code Exchange (PKCE)** option. PKCE cannot be enabled alongside client credentials on the same app. Create separate External Client Apps if you require PKCE for user authentication.

Choose **Create** to save the External Client App.

## Step 3: Get consumer credentials
<a name="salesforce-consumer-details"></a>

1. After creation, you are on the ECA detail page.

1. Navigate to the **Settings** tab or choose **Manage Consumer Details**.

1. You might need to verify your identity (email verification code).

1. Copy the **Consumer Key** (Client ID) and **Consumer Secret** (Client Secret).

**Important**  
Save these credentials securely. You need them when you configure the connector in Amazon Quick.

## Step 3b: Configure service authentication (2LO)
<a name="salesforce-2lo-setup"></a>

If you are using user authentication (3LO) only, skip this section and proceed to [Step 4: Configure Salesforce connector in Amazon Quick](#salesforce-integration-setup).

Service authentication requires additional configuration in the External Client App's Policies tab. These steps enable the client credentials flow operationally and designate the user identity under which all actions run.

### Enable client credentials and set the Run As user
<a name="salesforce-2lo-policies"></a>

1. In Salesforce Setup, navigate to your External Client App and choose the **Policies** tab.

1. Choose **Edit**.

1. Under **OAuth Policies**, select **Enable Client Credentials Flow**.

1. In the **Run As** field that appears, choose the user account under which all service authentication actions run. This is typically an administrator or dedicated service account.

1. Choose **Save**.

**Important**  
The **Enable Client Credentials Flow** option exists in two places: the **Settings** tab (enables the capability) and the **Policies** tab (enables it operationally and sets the Run As user). You must enable it in both places. Salesforce tokens are always user-scoped. The Run As user determines the identity and permissions for all actions that run through service authentication.

### Verify the token endpoint
<a name="salesforce-2lo-verify-token"></a>

Before you configure Amazon Quick, verify that the client credentials flow works by requesting a token from the Salesforce token endpoint. Run the following command from a terminal:

```
curl -X POST https://{{your-domain}}.my.salesforce.com/services/oauth2/token \
  -d "grant_type=client_credentials" \
  -d "client_id={{CONSUMER_KEY}}" \
  -d "client_secret={{CONSUMER_SECRET}}"
```

A successful response returns a JSON object that contains `access_token`, `instance_url`, and `token_type` fields.

If the response contains the error `no client credentials user enabled`, the Run As user is not configured. Return to [Enable client credentials and set the Run As user](#salesforce-2lo-policies) and verify that you enabled client credentials and assigned a Run As user on the **Policies** tab.

## Step 4: Configure Salesforce connector in Amazon Quick
<a name="salesforce-integration-setup"></a>

### Navigate to Connectors
<a name="salesforce-navigate-connectors"></a>

1. Open Amazon Quick and choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Salesforce**.

1. If prompted that a connector already exists, choose **No, create new**.

### User authentication (3LO) connection details
<a name="salesforce-connection-details"></a>

If you are using user authentication, enter the following connection details:


**Salesforce connector: user authentication (3LO)**  

| Field | Value | 
| --- | --- | 
| Name | A descriptive name (for example, "Salesforce ECA") | 
| Network | Public network | 
| Auth Type | Custom OAuth app | 
| Base URL | https://{{<your-domain>}}.my.salesforce.com/services/data/v60.0 | 
| Client ID | Consumer Key from Step 3 | 
| Client Secret | Consumer Secret from Step 3 | 
| Token URL | https://{{<your-domain>}}.my.salesforce.com/services/oauth2/token | 
| Authorization URL | https://{{<your-domain>}}.my.salesforce.com/services/oauth2/authorize | 
| Redirect URL | Pre-filled (do not change) | 

Choose **Next** to proceed.

### Service authentication (2LO) connection details
<a name="salesforce-connection-details-2lo"></a>

If you are using service authentication, enter the following connection details:


**Salesforce connector: service authentication (2LO)**  

| Field | Value | 
| --- | --- | 
| Name | A descriptive name (for example, "Salesforce Service Auth") | 
| Network | Public network | 
| Auth Type | Custom OAuth (Service Auth) | 
| Base URL | https://{{<your-domain>}}.my.salesforce.com/services/data/v60.0 | 
| Client ID | Consumer Key from Step 3 | 
| Client Secret | Consumer Secret from Step 3 | 
| Token URL | https://{{<your-domain>}}.my.salesforce.com/services/oauth2/token | 
| Authorization URL | Leave blank. Do not enter a value for service authentication. | 
| Scopes | api (use space-separated short-form scope names only) | 

**Important**  
Do not populate **Authorization URL** for service authentication. Amazon Quick rejects the form if an authorization URL is entered for a client credentials flow.

Choose **Next** to proceed.

## Step 5: Verify and publish
<a name="salesforce-verify-publish"></a>

1. On the **Review** page, verify the available Salesforce actions (up to 42 actions).

1. Choose **Next** to proceed to user sharing.

1. Select users or groups who should have access to this connector.

1. Choose **Publish** to publish the connector.

After you publish the connector, you can use Salesforce actions in Amazon Quick chat, flows, and automations.

## Available actions
<a name="salesforce-integration-actions"></a>

After you set up the connector, the following Salesforce actions are available:
+ Create, read, update, and delete (CRUD) operations on standard and custom objects.
+ Query Salesforce data using SOQL (Salesforce Object Query Language).
+ Manage leads, accounts, contacts, and opportunities.
+ Execute Apex methods and custom logic.
+ Manage cases, tasks, and activities.
+ Access reports and dashboards.

**Note**  
Salesforce integration supports action execution only. Data access and knowledge base creation are not available for Salesforce systems.

## Troubleshooting
<a name="salesforce-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).
+ **`URL no longer exists` error**. Verify that you are using the correct Salesforce domain in the Token URL and Authorization URL. Do not use legacy endpoints.
+ **OAuth validation fails (user authentication)**. Verify that PKCE is enabled on the ECA and that the Callback URL exactly matches your Amazon Quick instance URL with `/sn/oauthcallback` appended.
+ **Missing scopes error**. Go back to the ECA configuration in Salesforce and ensure all required OAuth scopes are in the **Selected** list, not still in **Available**.
+ ****Connected App** option is unavailable**. This is expected after Salesforce Spring '26. Use an External Client App instead. ECAs are the supported replacement.

**Service authentication (2LO) issues**
+ **`no client credentials user enabled` error**. The client credentials flow is not enabled on the **Policies** tab, or no Run As user is assigned. Navigate to the External Client App, choose the **Policies** tab, choose **Edit**, select **Enable Client Credentials Flow**, assign a Run As user, and save. For more information, see [Enable client credentials and set the Run As user](#salesforce-2lo-policies).
+ **`One or more parameters are invalid` error in Amazon Quick**. This error typically indicates one of the following issues:
  + The **Authorization URL** field contains a value. Leave this field blank for service authentication.
  + The **Scopes** field uses commas instead of spaces. Use space-separated short-form scope names only.
  + The **Client ID** or **Client Secret** contains leading or trailing whitespace.
  + The **Token URL** contains a trailing slash.
+ **`request not supported on this domain` error**. Use your Salesforce runtime domain (`{{your-domain}}.my.salesforce.com`), not the setup domain (`*.salesforce-setup.com`).
+ **PKCE errors with service authentication**. PKCE is incompatible with the client credentials flow. Clear the **Require Proof Key for Code Exchange (PKCE)** option in the External Client App's security settings. For more information, see [Enable security settings](#salesforce-security-settings).