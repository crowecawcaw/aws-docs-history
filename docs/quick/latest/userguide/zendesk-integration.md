# Zendesk Suite integration

Manage your Zendesk support tickets directly from Amazon Quick using natural
language. With the Zendesk Suite connector, you can create, update, search,
and list support tickets without leaving Amazon Quick.

Zendesk Suite is available as a built-in connector in Amazon Quick. To set up
this integration, complete the following two steps. First, prepare your Zendesk
account with the required access. Then, create the connector in Amazon Quick
and authenticate with your Zendesk credentials.

This connector supports OAuth user authentication and API key service
authentication. For information about the authentication methods that
Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Prerequisites

Before you set up the integration, verify that you have the following
resources and access.

- An active Zendesk account with an admin role.
- Permissions to access tickets and support data in your Zendesk
  instance.
- A subscription that meets the requirements described in [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Verify your Zendesk account

Before you configure Amazon Quick, verify that your Zendesk account meets
the following requirements.

- Your Zendesk account is active and you can sign in to the
  [Zendesk sign-in page](https://www.zendesk.com/login/ "https://www.zendesk.com/login/") on the Zendesk website.
- The tickets and support data that you want to access are accessible
  to your account.

## Configure Zendesk account

The Custom OAuth app authentication method in Amazon Quick requires an
OAuth client configured in Zendesk. The API key authentication method
requires an API token.

### To configure an OAuth client

1. In your Zendesk instance, navigate to **Admin
   Center**, then **Apps and
   integrations**, and then **OAuth
   clients** under
   **API**.
2. Choose **Add OAuth Client**.
3. Complete the form with the following fields:

   - **Name** – Enter a name for your
     app.
   - **Description** – Enter a short
     description.
   - **Identifier** – Enter a unique
     identifier for the OAuth client.
   - **Redirect URLs** – Enter
     `https://`region`.quicksight.aws.amazon.com/sn/oauthcallback`.
     Replace `region` with your
     AWS Region, for example,
     `us-east-1`.

4. Choose **Save**. Zendesk generates a client
   secret.

###### Important

Record the client secret now. You cannot retrieve it after
you leave this page. 5. After you capture the secret, choose **Save**
again to create the OAuth client.

The Identifier and the secret serve as the Client ID and Client Secret
when you configure the connector in Amazon Quick with the Custom
OAuth app authentication method.

For more information, see [Using OAuth authentication with your application](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application "https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application") on the
Zendesk website.

### To configure an API token

1. Navigate to **Admin Center**, then
   **Apps and integrations**, and then
   **API tokens**.
2. Choose **Add API token**.
3. For **Description**, enter a short description
   for the API token.
4. Choose **Save**. Zendesk generates an API
   token.

###### Important

Record the API token now. You cannot retrieve it after
you leave this page.

If you choose the API key authentication method in Amazon Quick, use
this API token as the API key value.

For more information, see [Managing API token access to the Zendesk API](https://support.zendesk.com/hc/en-us/articles/4408889192858-Managing-API-token-access-to-the-Zendesk-API "https://support.zendesk.com/hc/en-us/articles/4408889192858-Managing-API-token-access-to-the-Zendesk-API") on the
Zendesk website.

## Set up the integration in Amazon Quick

After you verify your Zendesk account access, create the connector in
Amazon Quick.

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Choose **Zendesk Suite** from the options available.
4. In the **Zendesk Suite** dialog, enter the
   following fields:

   - **Name** – A descriptive name for your
     Zendesk connector.
   - **Description (Optional)** – Choose **+ Add Description** to add notes about how this connector will be used.
   - **Connection type** – Choose
     **Public network**.

5. Choose your authentication method and configure the connector
   settings:

   - **Custom OAuth app** –
     Enter the following fields for your Zendesk instance:

     - **Base URL**
     - **Client ID**
     - **Client Secret**
     - **Token URL**
     - **Authorization URL**
     - **Redirect URL**

   - **API Key** –
     Enter the following fields:

     - **Base URL**
     - **API Key** (Zendesk API token)
     - **Email** associated with your Zendesk account

6. Choose **Next**.
7. Review the actions for Zendesk Suite and choose **Next**.
8. Specify who can access the connector:

   - To share with a team, enter a team name or group email.
   - To keep it private, leave the field blank.
   - To share with all users, toggle **Everyone in your
     organization**.

9. Choose **Publish**.

The connector appears in the **Available** panel
with a status of **Connected**.

## Available actions

After you set up the connector, you can use the following ticket management
actions.

Zendesk Suite available actions| Action | Description |
| --- | --- |
| Create Ticket | Create new ticket |
| List Search Results | Search tickets |
| List Tickets | View all tickets |
| Show Ticket | View ticket details |
| Update Ticket | Edit ticket details |

###### Note

The actions that you can use depend on the permissions that are
configured in your Zendesk account.

## Troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails** – Verify that your
  Zendesk account is active and that you can sign in to the
  [Zendesk sign-in page](https://www.zendesk.com/login/ "https://www.zendesk.com/login/") on the Zendesk website. If your organization uses single sign-on (SSO), confirm
  that your identity provider is configured correctly.
- **Access denied** – Confirm that your
  Zendesk user has an admin role with permissions to access tickets and
  support data. For API key connections, verify that the API token is valid and the associated
  email address is correct.
