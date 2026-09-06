

# Set up OAuth 2.0 authentication for Box
<a name="kb-managed-box-oauth2-setup"></a>

OAuth 2.0 authentication (`OAUTH2`) authenticates as a Box app on behalf of a specific user, using the OAuth 2.0 (3LO) flow. The connector crawls the content that user can access. OAuth 2.0 authentication is user-specific and does not support document-level access control (ACLs); use it only when Client Credentials Grant authentication is not viable. The user must sign in manually to generate tokens.

**Important**  
To filter query results by user permissions, use Client Credentials Grant authentication instead. See [Set up Client Credentials Grant authentication for Box](kb-managed-box-ccg-setup.md).

## Step 1: Create the OAuth app
<a name="kb-managed-box-oauth2-step1"></a>

1. Navigate to the [Box Developer Console](https://app.box.com/developers/console).

1. Choose **Create a New App**.

1. Select **User Authentication (OAuth 2.0)** — app type: **User**.

1. Name the app and choose **Create**.

## Step 2: Configure the redirect URI
<a name="kb-managed-box-oauth2-step2"></a>

Under **OAuth 2.0 Redirect URIs**, enter the redirect URL. If you have an existing redirect endpoint, use it. Otherwise, use the following test endpoint:

```
https://httpbin.org/anything
```

**Important**  
`httpbin.org` is a test redirect endpoint, which is fine for credential generation. Do not use it in production.

## Step 3: Configure content actions
<a name="kb-managed-box-oauth2-step3"></a>

Enable both of the following content actions:
+ Read All Files and Folders
+ Write All Files and Folders

Do not enable administrative actions or the as-user header for OAuth 2.0. No other settings are required.

## Step 4: Generate the access token
<a name="kb-managed-box-oauth2-step4"></a>

1. Sign in to the Box account for the user you want to crawl (in your browser).

1. Navigate to the authorization URL, replacing {{your-client-id}} with your app client ID and {{random-string}} with an arbitrary value:

   ```
   https://account.box.com/api/oauth2/authorize?response_type=code&client_id={{your-client-id}}&state={{random-string}}
   ```

1. After you authorize, you are redirected to httpbin. Copy the `code` value from the URL:

   ```
   https://httpbin.org/anything?state={{your-state}}&code={{auth-code}}
   ```

1. Run the following command to exchange the code for tokens:

   ```
   curl -i -X POST "https://api.box.com/oauth2/token" \
     -H "content-type: application/x-www-form-urlencoded" \
     -d "client_id={{your-client-id}}" \
     -d "client_secret={{your-client-secret}}" \
     -d "code={{code-from-above}}" \
     -d "grant_type=authorization_code"
   ```

1. The response contains `access_token` and `refresh_token`. Copy both.

## Step 5: Create the Secrets Manager secret
<a name="kb-managed-box-oauth2-step5"></a>

Store the credentials in an AWS Secrets Manager secret with the following key-value pairs:

```
{
    "clientId": "{{your-client-id}}",
    "clientSecret": "{{your-client-secret}}",
    "accessToken": "{{your-access-token}}",
    "refreshToken": "{{your-refresh-token}}"
}
```

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-box-oauth2-creds}} \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source `secretArn`.

## Next steps
<a name="kb-managed-box-oauth2-next"></a>

After you store the secret, create the data source with `authType` set to `OAUTH2`. See [Connect a Box data source](kb-managed-ds-box-connect.md).