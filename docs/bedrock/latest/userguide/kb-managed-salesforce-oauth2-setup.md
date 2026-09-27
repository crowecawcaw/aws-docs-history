

# Set up OAuth 2.0 Client Credentials authentication for Salesforce
<a name="kb-managed-salesforce-oauth2-setup"></a>

The Salesforce connector authenticates with OAuth 2.0 Client Credentials (2LO), which Salesforce calls the Client Credentials Flow. You register an External Client App and assign a dedicated Run-As integration user. The connector authenticates as the app and acts as that user, with no interactive sign-in; no Salesforce username, password, or security token is stored. Complete all the following steps in Salesforce before you configure the data source in Amazon Bedrock.

**Note**  
Newer Salesforce orgs create these credentials under **External Client App Manager**, the successor to the classic Connected App. The steps below use that framework. The OAuth mechanics (the `client_credentials` grant, scopes, Run-As user, and Consumer Key and Secret) are the same either way.

## Prerequisites
<a name="kb-managed-salesforce-oauth2-prereqs"></a>

Before you begin, make sure that you have the following in Salesforce:
+ Administrator access to the Salesforce org, with permission to create and manage External Client Apps.
+ My Domain enabled, which is required for the Client Credentials Flow. Your instance URL looks like `https://{{your-domain}}.my.salesforce.com`.
+ A dedicated integration user to assign as the Run-As user (least-privilege, non-interactive).

## Step 1: Create the External Client App
<a name="kb-managed-salesforce-oauth2-step1"></a>

1. In **Setup**, search for **External Client App Manager** (under **Apps** > **External Client Apps**), and then choose **New External Client App**.

1. Enter an **External Client App Name**, **API Name**, and **Contact Email**. Leave **Distribution State** as `Local`.

## Step 2: Enable OAuth and add scopes
<a name="kb-managed-salesforce-oauth2-step2"></a>

1. Expand **API (Enable OAuth Settings)** and select **Enable OAuth**.

1. Set a **Callback URL**. The Client Credentials Flow doesn't redirect, but the field is required. Enter any HTTPS URL that you control (for example, `https://login.salesforce.com/services/oauth2/callback`).

1. Under **OAuth Scopes**, add **Manage user data via APIs (api)**. This is the scope the Knowledge article crawl uses.

## Step 3: Enable the Client Credentials Flow
<a name="kb-managed-salesforce-oauth2-step3"></a>

1. Under **Flow Enablement**, select **Enable Client Credentials Flow** and accept the confirmation dialog.

1. Choose **Save and Continue**.

## Step 4: Assign the Run-As user
<a name="kb-managed-salesforce-oauth2-step4"></a>

The Client Credentials Flow runs as a specific user, and that user's permissions govern what the connector can read.

1. On the app's **Policies** tab, choose **Edit**.

1. Expand **OAuth Policies** > **OAuth Flows and External Client App Enhancements**, and ensure that **Enable Client Credentials Flow** is selected.

1. Set the **Run As** lookup to your integration user, and then choose **Save**.

**Note**  
Least privilege: The Run-As user needs read access to the Knowledge articles (and their data categories) that you intend to crawl. Use a dedicated integration user for this connector only, never for interactive UI logins.

## Step 5: Retrieve the Consumer Key and Secret
<a name="kb-managed-salesforce-oauth2-step5"></a>

1. On the app's **Settings** tab, expand **OAuth Settings** and open **Consumer Key and Secret** (identity verification may be prompted).

1. These values become the `clientId` (Consumer Key) and `clientSecret` (Consumer Secret) in your secret.

## Step 6: Create the Secrets Manager secret
<a name="kb-managed-salesforce-oauth2-step6"></a>

Store the credentials in an AWS Secrets Manager secret in the same AWS Region as your knowledge base with the following key-value pairs:

```
{
    "clientId": "{{your-consumer-key}}",
    "clientSecret": "{{your-consumer-secret}}",
    "instanceUrl": "https://{{your-domain}}.my.salesforce.com"
}
```


**Secret fields**  

| Field | Description | 
| --- | --- | 
| clientId | The External Client App's Consumer Key, used to request the OAuth token. | 
| clientSecret | The External Client App's Consumer Secret. | 
| instanceUrl | Your org's My Domain base URL (include https://, no trailing slash). The token endpoint is {instanceUrl}/services/oauth2/token, and it is also the API base for the crawl. This value must match the connection hostUrl. | 

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-salesforce-creds}} \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source `secretArn`. The knowledge base execution role must have `secretsmanager:GetSecretValue` permission on the secret.

## Next steps
<a name="kb-managed-salesforce-oauth2-next"></a>

After you store the secret, create the data source. See [Connect a Salesforce data source](kb-managed-ds-salesforce-connect.md).