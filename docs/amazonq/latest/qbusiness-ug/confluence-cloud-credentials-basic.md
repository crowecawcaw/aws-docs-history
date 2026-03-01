# Basic authentication

You can connect Amazon Q to Confluence (Cloud) using basic
authentication credentials. The following procedure gives you an overview of how to
configure Confluence (Cloud) to connect to Amazon Q using basic
authentication.

###### Configuring Confluence (Cloud) basic authentication for Amazon Q

1. Log in to your account from the [Confluence (Cloud)](https://confluence.atlassian.com/ "https://confluence.atlassian.com/"). Note
   the username you logged in with. You will need this later to connect to
   Amazon Q.
2. From your Confluence (Cloud) home page, note your Confluence (Cloud) URL
   from your Confluence browser URL. For example:
   `https://example.atlassian.net`. You will need
   this later to connect to Amazon Q.
3. Then, go to [Security](https://id.atlassian.com/manage-profile/security/api-tokens. " https://id.atlassian.com/manage-profile/security/api-tokens.") page in Confluence (Cloud).
4. From the **API tokens** page, select **Create API
   token**.

![Screenshot of the Atlassian account settings page showing where to access API tokens.](images/confluence-1.png) 5. In the **Create an API token** dialog box that opens, for
**Label**, add a name for your API token. Then, select
**Create**.

![Screenshot of the "Create an API token" dialog box where users enter a label for their API token.](images/confluence-2.png) 6. From the **Your new API token** dialog box, copy the API
token and save it in a text editor of your choice. You can't retrieve the
API token once you close the dialog box.

![Screenshot of the "Your new API token" dialog box displaying the generated API token that needs to be copied and saved.](images/confluence-3.png) 7. Select **Close**.
You now have the username, Confluence (Cloud) URL, and Confluence (Cloud) API
token you need to connect to Amazon Q with basic authentication.

For more information, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/") in
Atlassian Support.

## Atlassian Admin Authentication

To ensure Amazon Q can access all user and group information from your
Confluence (Cloud) instance, you must provide Atlassian admin credentials. These credentials allow
Amazon Q to sync user information regardless of individual email visibility settings.

### Get your Atlassian admin credentials

1. Sign in to the [Atlassian
   admin portal](https://admin.atlassian.com/ "https://admin.atlassian.com/") with administrator permissions.
2. Open the Administration app for your organization. The URL should look like:
   `https://admin.atlassian.com/o/{ORGANIZATION-UUID}/overview`
3. Choose **Settings**, then choose
   **API Keys**.
4. Choose **Create API key**.
5. Select all available scopes for the API key.

Note that the Confluence APIs that fetch user and group
information require full scope access. 6. Copy and save both the **Organization
ID** and **API Key**.
Note that API keys expire. Monitor the expiration date and
update your data source credentials before the key
expires.

### Get your Directory ID

1. Use the Atlassian Admin Workspace API to get your Directory ID. Run the following command:

```

curl --request POST \
--url 'https://api.atlassian.com/admin/v2/orgs/{ORGANIZATION-ID}/workspaces' \
--header 'Authorization: Bearer {API-KEY}' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json'

```

2. In the API response, find the workspace entry that matches your
   Confluence Cloud instance. Look for `"type":
"Confluence"`. Verify the workspace name matches your
   instance and then copy the directory value from the attributes
   section. If your instance isn't listed, use the pagination cursor in
   the `links.next` field to view additional pages.

```
curl --request POST \
--url 'https://api.atlassian.com/admin/v2/orgs/{ORGANIZATION-ID}/workspaces' \
--header 'Authorization: Bearer {API-KEY}' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{"cursor": "{NEXT-PAGE-TOKEN}"}'

```

### Update your Confluence data source

When creating or updating your Confluence Cloud data source, provide these
three values in your AWS Secrets Manager secret:

1. Admin API Key
2. Organization ID
3. Directory ID

For more information about Atlassian admin API scopes, see [Atlassian API
scopes documentation](https://developer.atlassian.com/cloud/admin/scopes/ "https://developer.atlassian.com/cloud/admin/scopes/").

For API details, see [Atlassian Admin Workspace API reference](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces "https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces").
