# Salesforce integration

With Salesforce action connector in Amazon Quick Suite, you can perform actions within Salesforce organizations, including managing records, querying data, and interacting with Salesforce APIs. This action connector supports task execution only and requires Amazon Quick Suite Pro tier or higher.

## What you can do

With Salesforce integration, you can perform actions within your Salesforce organizations through the action connector.

**Action connector**

Create, update, and query Salesforce objects such as leads, accounts, contacts, and opportunities.

###### Note

Salesforce integration doesn't support data access or knowledge base creation. It's designed specifically for task execution and API interactions with Salesforce objects.

## Before you begin

Before you set up Salesforce integration, make sure you have the following:

- Salesforce organization with appropriate permissions.
- Salesforce connected app or API access credentials.
- Amazon Quick Suite Author or higher.
- Administrative access to configure OAuth applications (if using user authentication).

## Step 1: Set up Salesforce connected app

###### Note

Create a connected app in Salesforce. Do not create an external client app. External client apps are not compatible with this integration.

Create a connected app in Salesforce to enable OAuth authentication with Amazon Quick Suite.

1. Sign in to your Salesforce account and navigate to the Setup page using the Setup icon in the top right.
2. In the Quick Find bar, enter `Apps`, then follow these steps:
   - Select **External Client Apps**
   - Select **Settings**
   - Under Settings, create a new connected app

3. Choose **New Connected App**.
4. Choose **Create a connected app**.
5. In the Basic Information section, enter the following required information:
   - **Connected App Name** - A descriptive name for your connected app.
   - **API Name** - A unique API name for your application.
   - **Contact Email** - Your contact email address.

6. In the OAuth Settings section, select the following checkboxes:
   - **Enable OAuth Settings**
   - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows** _(recommended)_

     Enable this option to add an additional security layer to the Authorization Code flow.

   - **Require Secret for Web Server Flow**
   - **Require Secret for Refresh Token Flow**
   - **Enable Client Credentials Flow**
   - **Enable Authorization Code and Credential Flow**
   - **Enable Token Exchange Flow**
   - **Require Secret for Token Exchange Flow**

7. Add the following required OAuth scopes:
   - `api` - Access Salesforce APIs
   - `refresh_token` - Maintain access when user is offline
   - `offline_access` - Perform requests at any time
   - `full` - Full access to all data
   - `web` - Web-based access
   - `visualforce` - Access Visualforce pages
   - `custom_permissions` - Access custom permissions
   - `chatter_api` - Access Chatter API
   - `wave_api` - Access Analytics API
   - `eclair_api` - Access Einstein Analytics API
   - `pardot_api` - Access Pardot API
   - `id` - Access identity information
   - `email` - Access email address
   - `profile` - Access basic profile information
   - `address` - Access address information
   - `phone` - Access phone number
   - `open_id` - Access OpenID Connect

8. Enter the callback URL in the format: `<quicksuite-url>/sn/oauthcallback`
9. Choose **Save**.

## Step 2: Configure consumer details and execution user

Configure the consumer details and set up an execution user for the client credentials flow.

1. From the Manage Connected Apps page, choose **Manage Consumer Details**. You might need to verify your identity.
2. Copy the **Consumer Key (Client ID)** and **Consumer Secret (Client Secret)**.
3. Choose **Apply**.
4. Choose **Initial Access Token**, then choose **OK**.
5. Configure the execution user:
   1. From the connected app detail page, choose **Edit** under the Action column.
   2. Under OAuth Policies > Refresh Token Policy, select **Immediately expire refresh token**.
   3. Under Client Credentials Flow, for Run As, choose the user to assign the client credentials flow.
   4. Choose **Save**.

## Step 3: Set up Salesforce action connector

After preparing your Salesforce connected app credentials, create the Salesforce action connector in Amazon Quick Suite.

Salesforce integration supports action execution only - data access and knowledge base
creation are not available for Salesforce systems.

1. In the Amazon Quick Suite console, choose **Integrations**.
2. Choose **Salesforce** from the integration options, and click
   the Add (plus "+") button.
3. Fill in the integration details:
   - **Name** - Descriptive name for your Salesforce action connector.
   - **Description** (Optional) - Purpose of the action connector.

4. Choose your connection type:
   - **User authentication** - OAuth-based authentication for individual user access.
   - **Service authentication** - Service-to-service authentication for application access.

5. Fill in the connection settings based on your selected authentication method (either user or service):
   1. For **User authentication (OAuth)**, configure the following fields:
      - **Base URL** - Salesforce instance URL (for example, https://your-domain.salesforce.com).
      - **Client ID** - Salesforce connected app consumer key.
      - **Client Secret** - Salesforce connected app consumer secret.
      - **Token URL** - Salesforce OAuth token endpoint.
      - **Auth URL** - Salesforce OAuth authorization endpoint.
      - **Redirect URL** - OAuth redirect URI configured in your connected app.

6. Select **Create and continue**.
7. Choose users to share the integration with.
8. Click **Next**.

## Step 4: Associate action connector to automation groups

To use Salesforce actions in automations, you must associate the action connector with your automation groups.

1. Navigate to your automation group settings.
2. Associate the Salesforce action connector with the automation group that will use these actions.
3. Create a new automation for the automation group to access Salesforce actions in your workflows.

## Available task actions

After you create your Salesforce integration, you can review the available actions for interacting with Salesforce objects. Common Salesforce actions include:

- Create, read, update, and delete (CRUD) operations on standard and custom objects.
- Query Salesforce data using SOQL (Salesforce Object Query Language).
- Manage leads, accounts, contacts, and opportunities.
- Execute Apex methods and custom logic.
- Manage cases, tasks, and activities.
- Access reports and dashboards.

## Share integrations

You can share Salesforce action connectors with other users in your organization. Follow these steps:

1. After you create the integration, choose **Share integration**.
2. Select users or groups to share the integration with.
3. Set appropriate permissions for shared access.
4. Confirm sharing settings.

Shared users can use the Salesforce integration to perform actions within the connected Salesforce organization, subject to the permissions configured in the original authentication setup.

## Manage Salesforce action connectors

After you create your Salesforce action connector, you can manage it using these options:

- **Edit action connector** - Update authentication settings or Salesforce instance configuration.
- **Share action connector** - Make the action connector available to other users in your organization.
- **Monitor usage** - View action connector activity and API usage metrics.
- **Review actions** - See the complete list of available Salesforce actions.
- **Delete action connector** - Remove the action connector and revoke associated authentication.
