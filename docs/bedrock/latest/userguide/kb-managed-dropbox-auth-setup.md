

# Set up authentication for Dropbox

The Dropbox connector authenticates with a refresh token issued to your own Dropbox app. You create a scoped-access app in the Dropbox App Console, grant it read scopes, authorize it once with offline access, and store the app key, app secret, and refresh token in an AWS Secrets Manager secret. On every sync, the connector exchanges the refresh token for a short-lived access token. There is no AWS-hosted consent page or redirect step.

Complete all the following steps before you configure the data source in Amazon Bedrock.

## Choose an authentication type
<a name="kb-managed-dropbox-auth-choose"></a>

Decide which authentication type you need before you create the app, because it determines the scopes you grant and who authorizes the app.
+ `OAUTH2` – The connector acts as the one user who authorizes the app and crawls only that user's Dropbox. Any Dropbox user can authorize the app. Document-level access control is not available.
+ `TEAM_ADMIN` – A team admin authorizes the app with team scopes, which issues a team-linked refresh token. The connector crawls content across the team. Document-level access control is available.

Use a separate Dropbox app for each authentication type. An `OAUTH2` app that has no team scopes can only ever issue user-linked tokens.

## Step 1: Create the Dropbox app
<a name="kb-managed-dropbox-auth-step1"></a>

1. Sign in to the [Dropbox App Console on the Dropbox website](https://www.dropbox.com/developers/apps). For `TEAM_ADMIN`, sign in as a member of the team whose content you want to crawl.

1. Choose **Create app**.

1. Complete the form:
   + **Choose an API** – **Scoped access**.
   + **Choose the type of access you need** – **Full Dropbox**. An app limited to an app folder cannot read the rest of the user's or team's Dropbox.
   + **Name your app** – A descriptive name (for example, `Amazon-Bedrock-KB-Connector`).

1. Choose **Create app**.

1. On the **Settings** tab, copy the **App key** and **App secret**. These become `clientId` and `clientSecret` in the secret.

## Step 2: Grant scopes
<a name="kb-managed-dropbox-auth-step2"></a>

On the app's **Permissions** tab, select the scopes for your authentication type, and then choose **Submit**. Grant scopes before you authorize the app in step 3. A refresh token carries only the scopes that were granted when it was issued, so if you add a scope later, repeat step 3.

The following tables list the scopes to grant for each authentication type.


**Scopes for both authentication types**  

| Scope | Used for | 
| --- | --- | 
| account\_info.read | Reading the account of the user who authorized the app | 
| files.metadata.read | Listing files and folders, and reading file metadata and tags | 
| files.content.read | Downloading files and exporting Paper documents | 
| sharing.read | Listing the shared folders each crawled user has access to, and reading the members of shared files and folders | 


**Additional scopes for TEAM\_ADMIN**  

| Scope | Used for | 
| --- | --- | 
| team\_info.read | Identifying the team admin who authorized the app | 
| members.read | Listing team members and their status | 
| team\_data.member | Reading content as each team member, or as the team admin | 
| team\_data.content.read | Listing team folders | 


**Additional scope for TEAM\_ADMIN with document-level access control**  

| Scope | Used for | 
| --- | --- | 
| groups.read | Reading team groups and their members | 

**Note**  
When you select `team_data.member`, the Dropbox App Console also selects `team_data.governance.write`, which it requires alongside `team_data.member`. The connector only calls read routes and never writes to Dropbox. Do not grant other write scopes, because the access token carries every scope granted to the app.

## Step 3: Authorize the app and get a refresh token
<a name="kb-managed-dropbox-auth-step3"></a>

1. In a browser, open the following URL, replacing {{APP\_KEY}} with your app key. `token_access_type=offline` is what makes Dropbox issue a refresh token.

   ```
   https://www.dropbox.com/oauth2/authorize?client_id={{APP_KEY}}&response_type=code&token_access_type=offline
   ```

1. Sign in and approve the app:
   + For `OAUTH2`, sign in as the user whose Dropbox you want to crawl.
   + For `TEAM_ADMIN`, sign in as a team admin. The consent screen lists the team scopes, and approving it links the app to the whole team.

1. Copy the access code that Dropbox displays. The code is valid for a short time and can be used only once.

1. Exchange the code for a refresh token:

   ```
   curl -s https://api.dropboxapi.com/oauth2/token \
     -d code={{ACCESS_CODE}} \
     -d grant_type=authorization_code \
     -u {{APP_KEY}}:{{APP_SECRET}}
   ```

1. From the response, copy `refresh_token`. This is the `refreshToken` value for the secret. Dropbox refresh tokens do not expire. They stay valid until you or a team admin revoke the app.

**Important**  
Treat the refresh token like a password. A `TEAM_ADMIN` refresh token grants read access to content across your whole Dropbox team.

## Step 4: Verify the token
<a name="kb-managed-dropbox-auth-step4"></a>

Before you store the credentials, check that the refresh token works and carries the scopes you granted.

**Request an access token:**

```
curl -s https://api.dropboxapi.com/oauth2/token \
  -d grant_type=refresh_token \
  -d refresh_token={{REFRESH_TOKEN}} \
  -u {{APP_KEY}}:{{APP_SECRET}}
```

The response contains `access_token` and a `scope` field that lists the scopes on the token. Confirm that every scope from step 2 is listed.

**Call Dropbox with the access token:**
+ For `OAUTH2`:

  ```
  curl -s -X POST https://api.dropboxapi.com/2/users/get_current_account \
    -H "Authorization: Bearer {{ACCESS_TOKEN}}"
  ```
+ For `TEAM_ADMIN`:

  ```
  curl -s -X POST https://api.dropboxapi.com/2/team/get_info \
    -H "Authorization: Bearer {{ACCESS_TOKEN}}"
  ```

The following table describes each verification result and the action to take.


**Verification results**  

| Result | Meaning | Action | 
| --- | --- | --- | 
| HTTP 200 with account or team details | Working correctly | Proceed to create the AWS Secrets Manager secret. | 
| HTTP 400 invalid\_grant on the token request | The refresh token is wrong, or the app was revoked | Repeat step 3. | 
| HTTP 400 or 401 on team/get\_info | The token is user-linked, not team-linked | Grant the team scopes from step 2, and repeat step 3 as a team admin. | 
| A scope from step 2 is missing from scope | The scope was granted after the token was issued | Repeat step 3. | 

## Step 5: Create the AWS Secrets Manager secret
<a name="kb-managed-dropbox-auth-step5"></a>

Store the credentials in an AWS Secrets Manager secret in the same AWS Region as your knowledge base with the following key-value pairs:

```json
{
    "clientId": "{{your-app-key}}",
    "clientSecret": "{{your-app-secret}}",
    "refreshToken": "{{your-refresh-token}}"
}
```


**Secret fields**  

| Field | Description | 
| --- | --- | 
| clientId | The app key from step 1. | 
| clientSecret | The app secret from step 1. | 
| refreshToken | The refresh token from step 3. | 

Both authentication types use the same three fields. The secret does not need an access token, because the connector mints a new access token on every sync. It also does not need a host URL, because every Dropbox account uses the same API host. When you create the data source, Amazon Bedrock checks that all three fields are present.

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-dropbox-creds}} \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source `secretArn`. The knowledge base execution role must have `secretsmanager:GetSecretValue` permission on the secret, and `kms:Decrypt` on the AWS KMS key if the secret is encrypted with a customer managed key.

## Rotate the credentials
<a name="kb-managed-dropbox-auth-rotate"></a>

To rotate the refresh token, repeat step 3 and update `refreshToken` in the secret. The next sync uses the new value. You do not need to update the data source.

## Next steps
<a name="kb-managed-dropbox-auth-next"></a>

After you store the secret, create the data source. See [Connect a Dropbox data source](kb-managed-ds-dropbox-connect.md).