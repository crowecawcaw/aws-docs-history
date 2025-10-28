# Prerequisites for connecting Amazon Q Business to Dropbox

Before you begin, make sure that you have completed the following
prerequisites.

**In Dropbox, make sure you have:**

- Created a Dropbox Advanced account and set up an admin
  user.
- Created a Dropbox app with a unique **App
  name**, activated **Scoped Access**. For more
  information, see [Dropbox documentation on creating an app](https://www.dropbox.com/developers/reference/getting-started#app%20console "https://www.dropbox.com/developers/reference/getting-started#app%20console") on the
  Dropbox website.
- Activated **Full Dropbox** permissions on the
  Dropbox console and added the following permissions:
  - `files.content.read`
  - `files.metadata.read`
  - `sharing.read`
  - `file_requests.read`
  - `groups.read`
  - `team_info.read`
  - `team_data.content.read`
  - `account_info.read`
  - `members.read`
  - `team_data.member`

- Create an authorization URL containing client ID (app-key), redirect_uri, response type, access type and scopes. Obtain User Authorization by signing in to Dropbox and grant your application the requested permissions.

`Sample Authorization URL:`

`https://www.dropbox.com/oauth2/authorize`

`?client_id=abcd1234example`

`&redirect_uri=https%3A%2F%2Fyourapp.com%2Fcallback`

`&response_type=code`

`&token_access_type=offline`

`&scope=files.metadata.read%20files.content.read`

- Exchange authorization code for tokens by requesting tokens from the Dropbox token endpoint.
  - curl https://api.dropboxapi.com/oauth2/token -d code=AUTH_CODE -d grant_type=authorization_code -d client_id=APP_KEY -d client_secret=APP_SECRET
  - Replace AUTH_CODE with the obtained authorization code, APP_KEY and APP_SECRET with your application client ID (App key) and secret key.

- Noted your Dropbox app key, Dropbox app secret,
  and Dropbox access token and refresh token for OAuth 2.0 authentication
  credentials.
- Generate an OAuth 2.0 access token with token_access_type=offline to obtain a short‑lived access token and a long‑lived refresh token. For more information, see [Dropbox
  documentation on OAuth authentication](https://developers.dropbox.com/oauth-guide "https://developers.dropbox.com/oauth-guide") on the
  Dropbox website.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Dropbox authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
