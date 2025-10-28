# OAuth 2.0

authentication

You can connect Amazon Q to Confluence (Cloud) using OAuth 2.0
authentication credentials. The following procedures give you an overview of how to
configure Confluence (Cloud) to connect to Amazon Q using OAuth 2.0
authentication.

###### Steps to configure Confluence (Cloud) OAuth 2.0

authentication

- [Step 1: Retrieving username
  and Confluence (Cloud) URL](#confluence-cloud-credentials-url "#confluence-cloud-credentials-url")
- [Step 2: Configuring an
  OAuth 2.0 app integration](#confluence-cloud-credentials-oauth-app "#confluence-cloud-credentials-oauth-app")
- [Step 3: Retrieving
  Confluence (Cloud) client ID and client Secret](#confluence-cloud-credentials-id-secret "#confluence-cloud-credentials-id-secret")
- [Step 4: Generating an
  Confluence (Cloud) access token](#confluence-cloud-credentials-access "#confluence-cloud-credentials-access")
- [Step 5: Generating a
  Confluence (Cloud) refresh token](#confluence-cloud-credentials-refresh "#confluence-cloud-credentials-refresh")
- [Step 6: Generating
  a new Confluence (Cloud) access token using a refresh token](#confluence-cloud-credentials-refresh-access "#confluence-cloud-credentials-refresh-access")

## Step 1: Retrieving username

and Confluence (Cloud) URL

To connect Confluence (Cloud) to Amazon Q, you need your
Confluence (Cloud) username and your Confluence (Cloud) URL. The following
procedure shows you how to retrieve these.

###### Retrieving username and Confluence (Cloud) URL

1. Log in to your account from the [Confluence (Cloud)](https://confluence.atlassian.com/ "https://confluence.atlassian.com/").
   Note the username you logged in with. You will need this later to
   connect to Amazon Q.
2. From your Confluence (Cloud) home page, note your Confluence (Cloud)
   URL from your Confluence browser URL. For example:
   `https://example.atlassian.net`. You will
   need this later to both configure your OAuth 2.0 token and connect to
   Amazon Q.

## Step 2: Configuring an

OAuth 2.0 app integration

To connect Confluence (Cloud) to Amazon Q using OAuth 2.0
authentication, you need to create a Confluence (Cloud) OAuth 2.0 app with the
necessary permissions. The following procedure shows you how to create
this.

###### Configuring an OAuth 2.0 app integration

1. Log in to your account from the [Atlassian Developer
   page](https://developer.atlassian.com/ "https://developer.atlassian.com/").
2. Select the profile icon from the top-right corner. Then, from the
   dropdown menu that opens, select **Developer
   Console**.

![Screenshot of the Atlassian Developer Console showing the "Create" button and options for creating a new integration.](images/confluence-4.png) 3. From the **Welcome** page, select
**Create** and then select **OAuth 2.0
integration**.

![Screenshot of the Atlassian Developer Console welcome page showing the "Create" dropdown menu with the "OAuth 2.0 integration" option highlighted.](images/confluence-5.png) 4. On the **Create a new OAuth 2.0 (3LO) integration**
page, for **Name**, enter a name for the OAuth 2.0
application you are creating. Then, select the **I agree to be
bound by Atlassian's developer terms** checkbox, and select
**Create**.

![Screenshot of the "Create a new OAuth 2.0 (3LO) integration" page where users enter a name for the OAuth application and agree to the Atlassian developer terms.](images/confluence-6.png)

The console will display a summary page outlining the details of the
OAuth 2.0 app created.

![Screenshot of the OAuth 2.0 app summary page showing details of the created application including name, ID, and other configuration information.](images/confluence-7.png) 5. From the left navigation menu, choose
**Authorization**. 6. From the **Authorization** page, choose
**Add** to add **OAuth 2.0 (3LO)**
to your app.

![Screenshot of the OAuth 2.0 app's Authorization page showing the "Add callback URL" button that users need to click to configure the callback URL for the OAuth flow.](images/confluence-8.png) 7. On the **OAuth 2.0 authorization code grants (3LO) for
apps**, enter the Confluence (Cloud) URL you copied as the
**Callback URL** and then choose **Save
changes**.

![Screenshot of the "OAuth 2.0 authorization code grants (3LO) for apps" section showing the Callback URL field where users enter the Confluence URL for the OAuth redirect.](images/confluence-9.png) 8. From the **Authorization URL generator** section that
appears, choose **Add APIs** to add APIs to your app.
This will redirect you to the **Permissions**
page. 9. On the **Permissions** page, for
**Scopes**, navigate to **User Identity
API**. Select **Add**, and then select
**Configure**.

![Screenshot of the Permissions page showing the "User Identity API" option that needs to be selected to configure user identity permissions for the OAuth app.](images/confluence-10.png) 10. On the **User Identity API** page, choose
**Edit Scopes**, and the add the following
`read` scopes:

    * **`read:me`** – View active
     user profile
    * **`read:account`** – View
     user profiles

![Screenshot of the User Identity API permissions page showing the available scopes that can be selected for the OAuth application, with read scopes highlighted.](images/confluence-12.png)

Then, select **Save**. 11. Return to the **Permissions** page. From
**Scopes**, navigate to **Confluence
API**. Select **Add**, and the select
**Configure**.

![Screenshot of the Permissions page showing the Confluence API option that needs to be selected to configure API permissions for accessing Confluence content.](images/confluence-11.png) 12. Navigate to the **Granular scopes** page.

![Screenshot of the Confluence API Granular scopes page showing the available API permission scopes that can be configured for the OAuth application.](images/confluence-14.png)

Then, choose **Edit Scopes**, and the add the
following `read` scopes:

    * **`read:content:confluence`**
     – View detailed contents
    * **`read:content-details:confluence`**
     – View content details
    * **`read:space-details:confluence`**
     – View space details
    * **`read:audit-log:confluence`**
     – View audit records
    * **`read:page:confluence`**
     – View pages
    * **`read:attachment:confluence`**
     – View and download content attachments
    * **`read:blogpost:confluence`**
     – View blogposts
    * **`read:custom-content:confluence`**
     – View custom content
    * **`read:comment:confluence`**
     – View comments
    * **`read:template:confluence`**
     – View content templates
    * **`read:label:confluence`**
     – View labels
    * **`read:watcher:confluence`**
     – View content watchers
    * **`read:group:confluence`**
     – View groups
    * **`read:relation:confluence`**
     – View entity relationships
    * **`read:user:confluence`**
     – View user details
    * **`read:configuration:confluence`**
     – View Confluence settings
    * **`read:space:confluence`**
     – View space details
    * **`read:space.permission:confluence`**
     – View space permissions
    * **`read:space.property:confluence`**
     – View space properties
    * **`read:user.property:confluence`**
     – View user properties
    * **`read:space.setting:confluence`**
     – View space settings
    * **`read:analytics.content:confluence`**
     – View analytics for content
    * **`read:content.permission:confluence`**
     – Check content permissions
    * **`read:content.property:confluence`**
     – View content properties
    * **`read:content.restriction:confluence`**
     – View content restrictions
    * **`read:content.metadata:confluence`**
     – View content summaries
    * **`read:inlinetask:confluence`**
     – View tasks
    * **`read:task:confluence`**
     – View tasks
    * **`read:permission:confluence`**
     – View content restrictions and space permissions
    * **`read:whiteboard:confluence`**
     – View whiteboards
    * **`read:app-data:confluence`**
     – Read app data
    * *(Optional)* **`read:database:confluence`**
     – Read database
    * *(Optional)* **`read:embed:confluence`**  – Read embeddings
    * *(Optional)* **`read:folder:confluence`**  – Read folders
    * *(Optional)* **`read:email-address:confluence`**  – Read email addresses

Then, select **Save**.

For more information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/") and [Determining the scopes required for an operation](https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/ "https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/") in
Atlassian Developer.

### Atlassian Admin Authentication

To ensure Amazon Q can access all user and group information from your
Confluence (Cloud) instance, you must provide Atlassian admin credentials. These credentials allow
Amazon Q to sync user information regardless of individual email visibility settings.

####

Get your Atlassian admin credentials

1. Sign in to the [Atlassian admin portal](https://admin.atlassian.com/ "https://admin.atlassian.com/")with administrator permissions.
2. Open the Administration app for your organization. The URL should look like:
   `https://admin.atlassian.com/o/{ORGANIZATION-UUID}/overview`
3. Choose **Settings**, then choose
   **API Keys**.
4. Choose **Create API key**\
5. Select all available scopes for the API key.

Note that the Confluence APIs that fetch user and group
information require full scope access. 6. Copy and save both the **Organization
ID** and **API Key**.
Note that API keys expire. Monitor the expiration date and
update your data source credentials before the key
expires.

####

Get your Directory ID

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

#### Creating your Confluence data source

When creating your Confluence Cloud data source, provide these
three values in your AWS Secrets Manager secret:

1. Admin API Key
2. Organization ID
3. Directory ID

For more information about Atlassian admin API scopes, see [Atlassian API
scopes documentation](https://developer.atlassian.com/cloud/admin/scopes/ "https://developer.atlassian.com/cloud/admin/scopes/").

For API details, see [Atlassian Admin Workspace API reference](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces "https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces").

#### Updating your Confluence data source

To update an existing Confluence Cloud data source with new admin credentials, add the
following key pairs to your AWS Secrets Manager secret:

1. adminApiKey, {Admin API Key}
2. organizationId, {Organization ID}
3. directoryId, {Directory ID}

For more information about Atlassian admin API scopes, see [Atlassian API
scopes documentation](https://developer.atlassian.com/cloud/admin/scopes/ "https://developer.atlassian.com/cloud/admin/scopes/").

For API details, see [Atlassian Admin Workspace API reference](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces "https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces").

## Step 3: Retrieving

Confluence (Cloud) client ID and client Secret

To connect Confluence (Cloud) to Amazon Q using OAuth 2.0
authentication, you need to provide a Confluence (Cloud) client ID and client
secret. The following procedure shows you how to retrieve these.

###### Note

You must create an OAuth 2.0 app before you can retrieve the client ID and
client secret. See [Configuring an OAuth 2.0 app integration](confluence-cloud-credentials.md#confluence-cloud-credentials-oauth-app "confluence-cloud-credentials.md#confluence-cloud-credentials-oauth-app")
for more details.

###### Retrieving Confluence (Cloud) client ID and client secret

- From the left navigation menu, choose **Settings**.
  Then, scroll down to **Authentication details** section
  and copy and save the following in a text editor of your choice:
  - Client ID – You will enter this as **App
    key** in the Amazon Q console.
  - Client Secret – You will enter this as **App
    secret** in the Amazon Q console.

![Screenshot of the OAuth application details page showing the client ID and client secret that need to be copied for API authentication with Confluence.](images/confluence-15.png)

You will need these to generate your Confluence (Cloud) OAuth 2.0
token and also to connect Amazon Q to
Confluence (Cloud).

For more information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/") and [Determining the scopes required for an operation](https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/ "https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/") in
Atlassian Developer.

## Step 4: Generating an

Confluence (Cloud) access token

To connect Confluence (Cloud) to Amazon Q, you need to generate an
access token. The following procedure outlines how to generate an access token
in Confluence (Cloud).

###### Generating your Confluence (Cloud) access token

1. Log in to your account from the [Atlassian Developer
   page](https://developer.atlassian.com/ "https://developer.atlassian.com/").
2. Open the OAuth 2.0 app you want to generate a refresh token
   for.
3. From the left navigation menu, choose
   **Authorization** again. Then, for **OAuth
   2.0 (3LO)**, choose **Configure**.
4. From the **Authorization** page, from
   **Authorization URL generator**, from
   **Granular Confluence API authorization URL**, copy
   the URL and save it in a text editor of your choice.

![Authorization page showing URL generator fields for User identity, Classic, and Granular Confluence API.](images/confluence-16.png)

The URL is of the following format:

```
https://auth.atlassian.com/authorize?
audience=api.atlassian.com
&client_id=`YOUR_CLIENT_ID`
&scope=`REQUESTED_SCOPE%20REQUESTED_SCOPE_TWO`
&redirect_uri=https://`YOUR_APP_CALLBACK_URL`
&state=`YOUR_USER_BOUND_VALUE`
&response_type=code
&prompt=consent
```

5. In the saved authorization URL, update the
   `state=${YOUR_USER_BOUND_VALUE}` parameter value to any
   text of your choice. For example,
   `state=``sample_text`.

For more information, see [What is the state parameter used for?](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#what-is-the-state-parameter-used-for- "https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#what-is-the-state-parameter-used-for-") in
Atlassian Support. 6. Open a web browser of your choice. Then, paste the authorization URL
you copied into the browser URL. On the page that opens up, make sure
everything is correct and then select
**Accept**.

![Atlassian account access request screen showing permissions and a warning about development mode.](images/confluence-17.png)

You will be returned to your Confluence (Cloud) home page. 7. Copy the URL of the Confluence (Cloud) home page and save it in a text
editor of your choice. The URL contains the authorization code for your
application. You will need this code to generate your Confluence (Cloud)
access token. The whole section after `code=` is the
authorization code. 8. Navigate to Postman.

If you don't have Postman, you can also choose to use cURL to generate
a Confluence (Cloud) access token. Use the following cURL command to do
so:

```
curl --location 'https://auth.atlassian.com/oauth/token' \
--header 'Content-Type: application/json' \
--data '{"grant_type": "authorization_code",
"client_id": "`YOUR_CLIENT_ID`",
"client_secret": "`YOUR_CLIENT_SECRET`",
"code": "`AUTHORIZATION_CODE`",
"redirect_uri": "`YOUR_CALLBACK_URL`"}'
```

9. On the Postman home page, select `POST` as the method, and
   then enter the following URL in the **Enter URL or paste
   text** box:
   `https://auth.atlassian.com/oauth/token`.
10. Then, select **Body** from the menu, and select
    **raw**
    **JSON**.

![API request interface showing POST method, URL, and JSON body with OAuth parameters.](images/confluence-18.png) 11. In the text box, enter the following code extract, replacing the
fields with your credential values:

```
{"grant_type": "authorization_code",
"client_id": "`YOUR_CLIENT_ID`",
"client_secret": "`YOUR_CLIENT_SECRET`",
"code": "`YOUR_AUTHORIZATION_CODE`",
"redirect_uri": "`https://YOUR_APP_CALLBACK_URL`"}

```

12. Then, select **Send**. If everything is configured
    correctly, Postman will return an
    `access-token`. Copy the access token and save it using a
    text editor of your choice. You will need it to connect
    Confluence (Cloud) to Amazon Q.

For more information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/") in Atlassian
Developer.

## Step 5: Generating a

Confluence (Cloud) refresh token

The access token you use to connect Confluence (Cloud) to Amazon Q
using OAuth 2.0 authentication expires after 1 hour. When it does, you can
either repeat the whole authorization process and generate a new access token.
Or, you can choose to generate a refresh token. You can use the refresh token to
regenerate a new access token when an existing access token expires.

To do this, you add a `%20offline_access` parameter to the end of
the `scope` value in the authorization URL you used to generate your
access token. The following procedure shows you how to generate a refresh
token.

###### Generating an Confluence (Cloud) refresh token

1. Log in to your account from the [Atlassian Developer
   page](https://developer.atlassian.com/ "https://developer.atlassian.com/").
2. Open the OAuth 2.0 app you want to generate a refresh token
   for.
3. From the left navigation menu, choose
   **Authorization** again. Then, for **OAuth
   2.0 (3LO)**, choose **Configure**.
4. From the **Authorization** page, from
   **Authorization URL generator**, from
   **Granular Confluence API authorization URL**, copy
   the URL and save it in a text editor of your choice.

![Authorization page showing URL generator fields for User identity, Classic, and Granular Confluence API.](images/confluence-16.png) 5. In the saved authorization URL, update the
`state=${YOUR_USER_BOUND_VALUE}` parameter value to any
text of your choice. For example,
`state=``sample_text`.

For more information, see [What is the state parameter used for?](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#what-is-the-state-parameter-used-for- "https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#what-is-the-state-parameter-used-for-") in
Atlassian Support. 6. Then, add the following text at the end of the `scope`
value in your authorization URL: `%20offline_access` and copy
it. For example:

```
https://auth.atlassian.com/authorize?
audience=api.atlassian.com
&client_id=`YOUR_CLIENT_ID`
&scope=`REQUESTED_SCOPE%20REQUESTED_SCOPE_TWO%20offline_access`
&redirect_uri=https://`YOUR_APP_CALLBACK_URL`
&state=`YOUR_USER_BOUND_VALUE`
&response_type=code
&prompt=consent
```

7. Open a web browser of your choice and paste the modified authorization
   URL you copied into the browser URL. On the page that opens up, make
   sure everything is correct and then select
   **Accept**.

![Atlassian account access request screen showing permissions and a warning about development mode.](images/confluence-17.png)

You will be returned to the Confluence (Cloud) console. 8. Copy the URL of the Confluence (Cloud) home page and save it in a text
editor of your choice. The URL contains the authorization code for your
application. You will need this code to generate your Confluence (Cloud)
refresh token. The whole section after `code=` is the
authorization code. 9. Navigate to Postman.

If you don't have Postman, you can also choose to use cURL to generate
a Confluence (Cloud) access token. Use the following cURL command to do
so:

```
curl --location 'https://auth.atlassian.com/oauth/token' \
--header 'Content-Type: application/json' \
--data '{"grant_type": "authorization_code",
"client_id": "`YOUR CLIENT ID`",
"client_secret": "`YOUR CLIENT SECRET`",
"code": "`AUTHORIZATION CODE`",
"redirect_uri": "`YOUR CALLBACK URL`"}'
```

10. On the Postman home page, select `POST` as the method, and
    then enter the following URL in the **Enter URL or paste
    text** box:
    `https://auth.atlassian.com/oauth/token`.
11. Then, select **Body** from the menu, and select
    **raw**
    **JSON**.

![API request interface showing POST method, URL, and JSON body with OAuth parameters.](images/confluence-18.png) 12. In the text box, enter the following code extract, replacing the
fields with your credential values:

```
{"grant_type": "authorization_code",
"client_id": "`YOUR_CLIENT_ID`",
"client_secret": "`YOUR_CLIENT_SECRET`",
"code": "`YOUR_AUTHORIZATION_CODE`",
"redirect_uri": "`https://YOUR_APP_CALLBACK_URL`"}

```

13. Then, select **Send**. If everything is configured
    correctly, Postman will return an
    `refresh-token`.

Copy the refresh token and save it using a text editor of your choice.
You will need it to connect Confluence (Cloud) to Amazon Q.

For more information, see [Implementing a Refresh Token Flow](https://developer.atlassian.com/cloud/oauth/getting-started/refresh-tokens/ "https://developer.atlassian.com/cloud/oauth/getting-started/refresh-tokens/") in Atlassian
Developer.

## Step 6: Generating

a new Confluence (Cloud) access token using a refresh token

You can use the refresh token you generated to create a new access
token-refresh token pair when an existing access token expires. The following
procedure shows you how to generate a refresh token.

###### Generating an Confluence (Cloud) access token-refresh token pair

1. Copy the refresh token you generated following the steps in [Step 5: Generating a Confluence (Cloud) refresh
   token](confluence-cloud-credentials.md#confluence-cloud-credentials-refresh "confluence-cloud-credentials.md#confluence-cloud-credentials-refresh").
2. Navigate to Postman.

If you don't have Postman, you can also choose to use cURL to generate
a new Confluence (Cloud) access token. Use the following cURL command to
do so:

```
curl --location 'https://auth.atlassian.com/oauth/token' \
--header 'Content-Type: application/json' \
--data '{"grant_type": "refresh_token",
"client_id": "`YOUR_CLIENT_ID`",
"client_secret": "`YOUR_CLIENT_SECRET`",
"refresh_token": "`YOUR_REFRESH_TOKEN`"}'
```

3. On the Postman home page, select `POST` as the method, and
   then enter the following URL in the **Enter URL or paste
   text** box:
   `https://auth.atlassian.com/oauth/token`.
4. Then, select **Body** from the menu, and select
   **raw**
   **JSON**.

![Screenshot of the Postman interface showing how to set up a POST request to refresh an access token using the refresh token.](images/confluence-20.png) 5. In the text box, enter the following code extract, replacing the
fields with your credential values:

```
{"grant_type": "refresh_token",
"client_id": "`YOUR_CLIENT_ID`",
"client_secret": "`YOUR_CLIENT_SECRET`",
"refresh_token": "`YOUR REFRESH TOKEN`"}

```

6. Then, select **Send**. If everything is configured
   correctly, Postman will return a new access token-refresh
   token pair in the following format:

```
{
"access_token": "`string`,
"expires_in": "`expiry time of access_token in second`",
"scope": "`string`",
"refresh_token": "`string`"
}
```

For more information, see [Implementing a Refresh Token Flow](https://developer.atlassian.com/cloud/oauth/getting-started/refresh-tokens/ "https://developer.atlassian.com/cloud/oauth/getting-started/refresh-tokens/") and [How do I get a new access token, if my access token expires or is revoked?](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#how-do-i-get-a-new-access-token--if-my-access-token-expires-or-is-revoked- "https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#how-do-i-get-a-new-access-token--if-my-access-token-expires-or-is-revoked-") in Atlassian Developer.
