

# Set up OAuth 2.0 Client Credentials authentication for Zendesk
<a name="kb-managed-zendesk-oauth2-setup"></a>

The Zendesk connector authenticates with OAuth 2.0 Client Credentials (2LO). You register an OAuth client in Zendesk, store the client ID and client secret in an AWS Secrets Manager secret, and the connector exchanges them for an access token. There is no per-user consent or redirect step. Complete all the following steps before you configure the data source in Amazon Bedrock.

## Prerequisites
<a name="kb-managed-zendesk-oauth2-prereqs"></a>

Before you begin, make sure that you have the following in Zendesk:
+ A Zendesk Suite (Professional or Enterprise) account with admin access.
+ Your Zendesk host URL (for example, `https://{{yoursubdomain}}.zendesk.com`). You provide this value as the connection `hostUrl`, and it must match the `instanceUrl` that you store in the secret.

## Step 1: Create the OAuth client
<a name="kb-managed-zendesk-oauth2-step1"></a>

1. Log in to your Zendesk account as an admin.

1. From the left navigation, go to **Admin Center**.

1. In **Admin Center**, choose **Apps and integrations**.

1. On the **Apps and integrations** page, choose **OAuth Clients**, and then choose **Add OAuth client**.

1. Complete the form:
   + **Client name** – A human-readable name that is visible to users.
   + **Unique identifier** – This value becomes the Client ID (`clientId`) that you store in the secret.
   + **Client kind** – `Confidential`. The connector authenticates with a client secret, and only a confidential client is issued one. A public client doesn't receive a secret.
   + **Scopes** – Grant `read`. The connector only reads content to crawl, and the token exchange requests `scope=read`.
   + **Redirect URL** – Not used by this connector, because the client credentials (2LO) flow performs no redirect. If the form requires a value, enter a placeholder such as `http://localhost`.

1. Choose **Save**.

1. When the secret dialog appears, copy the generated secret and store it securely. This is the Client Secret (`clientSecret`).

**Important**  
The client secret is shown only once at creation and can't be regenerated or viewed again. If you lose it, recreate or rotate the OAuth client and update the AWS Secrets Manager secret.

You now have the three values that the connector needs: your host URL, the Client ID, and the Client Secret.

## Step 2: Create the Secrets Manager secret
<a name="kb-managed-zendesk-oauth2-step2"></a>

Store the credentials in an AWS Secrets Manager secret in the same AWS Region as your knowledge base with the following key-value pairs:

```
{
    "clientId": "{{your-client-id}}",
    "clientSecret": "{{your-client-secret}}",
    "instanceUrl": "https://{{yoursubdomain}}.zendesk.com"
}
```


**Secret fields**  

| Field | Description | 
| --- | --- | 
| clientId | The OAuth client's Unique identifier from Zendesk (step 1). | 
| clientSecret | The OAuth client's generated secret, copied at creation time in step 1. | 
| instanceUrl | Your Zendesk host URL (include https://, no trailing slash). This value must match the connection hostUrl. The connector validates that the two are equal and builds the token endpoint from hostUrl. | 

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-zendesk-creds}} \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source `secretArn`. The knowledge base execution role must have `secretsmanager:GetSecretValue` permission on the secret.

## Next steps
<a name="kb-managed-zendesk-oauth2-next"></a>

After you store the secret, create the data source. See [Connect a Zendesk data source](kb-managed-ds-zendesk-connect.md).