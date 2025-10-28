# OAuth 2.0

authentication

You can connect Amazon Q to Jira using OAuth 2.0
authentication credentials. The following procedures give you an overview of how to
configure Jira to connect to Amazon Q using OAuth 2.0
authentication.

###### Steps to configure Jira OAuth 2.0

authentication

- [Step 1: Retrieving username
  and Jira URL](#jira-credentials-url "#jira-credentials-url")
- [Step 2: Configuring an
  OAuth 2.0 app integration](#jira-credentials-oauth-app "#jira-credentials-oauth-app")
- [Step 3: Retrieving
  Jira client ID and client Secret](#jira-credentials-id-secret "#jira-credentials-id-secret")
- [Step 4: Generating a
  Jira access token](#jira-credentials-access "#jira-credentials-access")
- [Step 5: Generating a
  Jira refresh token](#jira-credentials-refresh "#jira-credentials-refresh")
- [Step 6: Generating
  a new Jira access token using a refresh token](#jira-credentials-refresh-access "#jira-credentials-refresh-access")

## Step 1: Retrieving username

and Jira URL

To connect Jira to Amazon Q, you need your
Jira username and your Jira URL. The following
procedure shows you how to retrieve these.

###### Retrieving username and Jira URL

1. Log in to your account from the [Jira](https://jira.atlassian.com/ "https://jira.atlassian.com/"). Note
   the username you logged in with. You will need this later to connect to
   Amazon Q.
2. From your Jira home page, note your Jira
   URL from your Jira browser URL. For example:
   `https://example.atlassian.net`. You will
   need this later to both configure your OAuth 2.0 token and connect to
   Amazon Q.

## Step 2: Configuring an

OAuth 2.0 app integration

To connect Jira to Amazon Q using OAuth 2.0
authentication, you need to create a Jira OAuth 2.0 app with the
necessary permissions. The following procedure shows you how to create
this.

###### Configuring an OAuth 2.0 app integration

1. Log in to your account from the [Atlassian Developer
   page](https://developer.atlassian.com/ "https://developer.atlassian.com/").
2. Select the profile icon from the top-right corner. Then, from the
   dropdown menu that opens, select **Developer
   Console**.
3. From the **Welcome** page, select
   **Create** and then select **OAuth 2.0
   integration**.
4. On the **Create a new OAuth 2.0 (3LO) integration**
   page, for **Name**, enter a name for the OAuth 2.0
   application you are creating. Then, select the **I agree to be
   bound by Atlassian's developer terms** checkbox, and select
   **Create**.

The console will display a summary page outlining the details of the
OAuth 2.0 app created. 5. From the left navigation menu, choose
**Authorization**. 6. From the **Authorization** page, choose
**Add** to add **OAuth 2.0 (3LO)**
to your app. 7. On the **OAuth 2.0 authorization code grants (3LO) for
apps**, enter the Jira URL you copied as the
**Callback URL** and then choose **Save
changes**. 8. From the **Authorization URL generator** section that
appears, choose **Add APIs** to add APIs to your app.
This will redirect you to the **Permissions**
page. 9. On the **Permissions** page, for
**Scopes**, navigate to **User Identity
API**. Select **Add**, and then select
**Configure**. 10. On the **User Identity API** page, choose
**Edit Scopes**, and the add the following
`read` scopes:

    * **`read:me`** – View active
     user profile
    * **`read:account`** – View
     user profiles

Then, select **Save**. 11. Return to the **Permissions** page. From
**Scopes**, navigate to **Jira
API**. Select **Add**, and then
select **Configure**. 12. On the **Jira API** page, you need to add scopes from both the Classic scopes and Granular scopes sections.

Choose **Edit Scopes**, and add the following scopes:

**In the Classic scopes section, add:**

    * **`read:jira-user`** – View
     active user profiles
    * **`read:jira-work`** – View
     Jira issue data
    * **`manage:jira-configuration`**
     – Manage Jira global settings

**In the Granular scopes section, add:**

    * **`read:application-role:jira`**
     – View application roles

Select **Save**.

For more information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/") and [Determining the scopes required for an operation](https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/ "https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/") in
Atlassian Developer.

## Step 3: Retrieving

Jira client ID and client Secret

To connect Jira to Amazon Q using OAuth 2.0
authentication, you need to provide a Jira client ID and client
secret. The following procedure shows you how to retrieve these.

###### Note

You must create an OAuth 2.0 app before you can retrieve the client ID and
client secret. See [Configuring an OAuth 2.0 app integration](jira-credentials.md#jira-credentials-oauth-app "jira-credentials.md#jira-credentials-oauth-app")
for more details.

###### Retrieving Jira client ID and client secret

- From the left navigation menu, choose **Settings**.
  Then, scroll down to **Authentication details** section
  and copy and save the following in a text editor of your choice:

      + Client ID – You will enter this as **App
       key** in the Amazon Q console.
      + Client Secret – You will enter this as **App
       secret** in the Amazon Q console.

  You will need these to generate your Jira OAuth 2.0
  token and also to connect Amazon Q to
  Jira.

For more information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/") and [Determining the scopes required for an operation](https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/ "https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/") in
Atlassian Developer.

## Step 4: Generating a

Jira access token

To connect Jira to Amazon Q, you need to generate an
access token. The following procedure outlines how to generate an access token
in Jira.

###### Generating your Jira access token

1. Log in to your account from the [Atlassian Developer
   page](https://developer.atlassian.com/ "https://developer.atlassian.com/").
2. Open the OAuth 2.0 app you want to generate a refresh token
   for.
3. From the left navigation menu, choose
   **Authorization** again. Then, for **OAuth
   2.0 (3LO)**, choose **Configure**.
4. From the **Authorization** page, from
   **Authorization URL generator**, from
   **Granular Jira API authorization URL**, copy the
   URL and save it in a text editor of your choice.

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

You will be returned to your Jira home page. 7. Copy the URL of the Jira home page and save it in a text
editor of your choice. The URL contains the authorization code for your
application. You will need this code to generate your Jira
access token. The whole section after `code=` is the
authorization code. 8. Navigate to Postman.

If you don't have Postman, you can also choose to use cURL to generate
a Jira access token. Use the following cURL command to do
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
11. In the text box, enter the following code extract, replacing the
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
    Jira to Amazon Q.

For more information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/") in Atlassian
Developer.

## Step 5: Generating a

Jira refresh token

The access token you use to connect Jira to Amazon Q
using OAuth 2.0 authentication expires after 1 hour. When it does, you can
either repeat the whole authorization process and generate a new access token.
Or, you can choose to generate a refresh token. You can use the refresh token to
regenerate a new access token when an existing access token expires.

To do this, you add a `%20offline_access` parameter to the end of
the `scope` value in the authorization URL you used to generate your
access token. The following procedure shows you how to generate a refresh
token.

###### Generating an Jira refresh token

1. Log in to your account from the [Atlassian Developer
   page](https://developer.atlassian.com/ "https://developer.atlassian.com/").
2. Open the OAuth 2.0 app you want to generate a refresh token
   for.
3. From the left navigation menu, choose
   **Authorization** again. Then, for **OAuth
   2.0 (3LO)**, choose **Configure**.
4. From the **Authorization** page, from
   **Authorization URL generator**, from
   **Granular Jira API authorization URL**, copy the
   URL and save it in a text editor of your choice.
5. In the saved authorization URL, update the
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

You will be returned to the Jira console. 8. Copy the URL of the Jira home page and save it in a text
editor of your choice. The URL contains the authorization code for your
application. You will need this code to generate your Jira
refresh token. The whole section after `code=` is the
authorization code. 9. Navigate to Postman.

If you don't have Postman, you can also choose to use cURL to generate
a Jira access token. Use the following cURL command to do
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
12. In the text box, enter the following code extract, replacing the
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
You will need it to connect Jira to Amazon Q.

For more information, see [Implementing a Refresh Token Flow](https://developer.atlassian.com/cloud/oauth/getting-started/refresh-tokens/ "https://developer.atlassian.com/cloud/oauth/getting-started/refresh-tokens/") in Atlassian
Developer.

## Step 6: Generating

a new Jira access token using a refresh token

You can use the refresh token you generated to create a new access
token-refresh token pair when an existing access token expires. The following
procedure shows you how to generate a refresh token.

###### Generating an Jira access token-refresh token pair

1. Copy the refresh token you generated following the steps in [Step 5: Generating a Jira refresh
   token](jira-credentials.md#jira-credentials-refresh "jira-credentials.md#jira-credentials-refresh").
2. Navigate to Postman.

If you don't have Postman, you can also choose to use cURL to generate
a new Jira access token. Use the following cURL command to
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
5. In the text box, enter the following code extract, replacing the
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
