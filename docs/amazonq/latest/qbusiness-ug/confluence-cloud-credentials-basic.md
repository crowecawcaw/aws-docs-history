

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Basic authentication
<a name="confluence-cloud-credentials-basic"></a>

You can connect Amazon Q to Confluence (Cloud) using basic authentication credentials. The following procedure gives you an overview of how to configure Confluence (Cloud) to connect to Amazon Q using basic authentication.

**Configuring Confluence (Cloud) basic authentication for Amazon Q**

1. Log in to your account from the [Confluence (Cloud)](https://confluence.atlassian.com/). Note the username you logged in with. You will need this later to connect to Amazon Q.

1. From your Confluence (Cloud) home page, note your Confluence (Cloud) URL from your Confluence browser URL. For example: {{https://example.atlassian.net}}. You will need this later to connect to Amazon Q.

1. Then, go to [Security]( https://id.atlassian.com/manage-profile/security/api-tokens.) page in Confluence (Cloud).

1. From the **API tokens** page, select **Create API token**.  
![Screenshot of the Atlassian account settings page showing where to access API tokens.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/confluence-1.png)

1. In the **Create an API token** dialog box that opens, for **Label**, add a name for your API token. Then, select **Create**.  
![Screenshot of the "Create an API token" dialog box where users enter a label for their API token.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/confluence-2.png)

1. From the **Your new API token** dialog box, copy the API token and save it in a text editor of your choice. You can't retrieve the API token once you close the dialog box.  
![Screenshot of the "Your new API token" dialog box displaying the generated API token that needs to be copied and saved.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/confluence-3.png)

1. Select **Close**.

You now have the username, Confluence (Cloud) URL, and Confluence (Cloud) API token you need to connect to Amazon Q with basic authentication.

For more information, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) in Atlassian Support.

## Atlassian Admin Authentication
<a name="confluence-cloud-credentials-admin-auth"></a>

To ensure Amazon Q can access all user and group information from your Confluence (Cloud) instance, you must provide Atlassian admin credentials. These credentials allow Amazon Q to sync user information regardless of individual email visibility settings.

### Get your Atlassian admin credentials
<a name="w2aac31c14c23c29c39c23c11c11b5"></a>

1. Sign in to the [Atlassian admin portal](https://admin.atlassian.com/) with administrator permissions.

1.  Open the Administration app for your organization. The URL should look like: `https://admin.atlassian.com/o/{ORGANIZATION-UUID}/overview` 

1. Choose **Settings**, then choose **API Keys**.

1. Choose **Create API key**.

1. Select all available scopes for the API key. 

   Note that the Confluence APIs that fetch user and group information require full scope access.

1.  Copy and save both the **Organization ID** and **API Key**. Note that API keys expire. Monitor the expiration date and update your data source credentials before the key expires. 

### Get your Directory ID
<a name="w2aac31c14c23c29c39c23c11c11b7"></a>

1. Use the Atlassian Admin Workspace API to get your Directory ID. Run the following command:

   ```
   curl --request POST \
   --url 'https://api.atlassian.com/admin/v2/orgs/{ORGANIZATION-ID}/workspaces' \
   --header 'Authorization: Bearer {API-KEY}' \
   --header 'Accept: application/json' \
   --header 'Content-Type: application/json'
   ```

1. In the API response, find the workspace entry that matches your Confluence Cloud instance. Look for `"type": "Confluence"`. Verify the workspace name matches your instance and then copy the directory value from the attributes section. If your instance isn't listed, use the pagination cursor in the `links.next` field to view additional pages.

   ```
   curl --request POST \
   --url 'https://api.atlassian.com/admin/v2/orgs/{ORGANIZATION-ID}/workspaces' \
   --header 'Authorization: Bearer {API-KEY}' \
   --header 'Accept: application/json' \
   --header 'Content-Type: application/json' \
   --data '{"cursor": "{NEXT-PAGE-TOKEN}"}'
   ```

### Update your Confluence data source
<a name="w2aac31c14c23c29c39c23c11c11b9"></a>

When creating or updating your Confluence Cloud data source, provide these three values in your AWS Secrets Manager secret:

1. Admin API Key

1. Organization ID

1. Directory ID

For more information about Atlassian admin API scopes, see [Atlassian API scopes documentation](https://developer.atlassian.com/cloud/admin/scopes/).

For API details, see [Atlassian Admin Workspace API reference](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces).