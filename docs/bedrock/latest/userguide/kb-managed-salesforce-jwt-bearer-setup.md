

# Set up OAuth 2.0 JWT Bearer authentication for Salesforce document-level access controls
<a name="kb-managed-salesforce-jwt-bearer-setup"></a>

To filter results by each user's Salesforce permissions, the Salesforce connector checks access as the querying user at query time. It does this with the OAuth 2.0 JWT Bearer Flow: the connector signs a short-lived assertion with a private key that you provide, and Salesforce returns a token for that user. The content crawl continues to use the OAuth 2.0 Client Credentials Flow.

Complete these steps in addition to [Set up OAuth 2.0 Client Credentials authentication for Salesforce](kb-managed-salesforce-oauth2-setup.md). Both flows can use the same External Client App.

## Prerequisites
<a name="kb-managed-salesforce-jwt-bearer-prereqs"></a>

Before you begin, make sure that you have the following:
+ The External Client App, Run-As user, Consumer Key, and Consumer Secret from the Client Credentials setup.
+ Administrator access to the Salesforce org.
+ OpenSSL, or another tool that can generate an RSA key pair and an X.509 certificate.

## Step 1: Generate a signing key and certificate
<a name="kb-managed-salesforce-jwt-bearer-step1"></a>

Generate a 2048-bit RSA key pair, a self-signed certificate, and an unencrypted PKCS\#8 copy of the private key:

```
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout jwt-signing.key -out jwt-signing.crt -days 730 -subj '/CN={{bedrock-kb-salesforce}}'
openssl pkcs8 -topk8 -nocrypt -in jwt-signing.key -out jwt-signing-pkcs8.key
```
+ `jwt-signing.crt` is the certificate. You upload it to Salesforce in step 2.
+ `jwt-signing-pkcs8.key` is the private key. You store it in the secret in step 5. It must be unencrypted PKCS\#8 (`BEGIN PRIVATE KEY`). A PKCS\#1 key (`BEGIN RSA PRIVATE KEY`) or an encrypted key is rejected.

**Important**  
Protect the private key as you would an administrator password. Anyone who holds it can obtain a token for any pre-authorized user of the app. Store it only in AWS Secrets Manager, and delete local copies after you create the secret.

## Step 2: Enable digital signatures and add scopes
<a name="kb-managed-salesforce-jwt-bearer-step2"></a>

1. In **Setup**, open **External Client App Manager** and edit your External Client App.

1. Under **OAuth Settings**, select **Enable JWT Bearer Flow** (labeled **Use digital signatures** on some orgs) and upload `jwt-signing.crt`.

1. Under **OAuth Scopes**, make sure the app has exactly these two scopes:
   + **Manage user data via APIs (api)**
   + **Perform requests at any time (refresh\_token, offline\_access)**

   Both are required, and the token request fails with any other scope added. The connector doesn't use refresh tokens, but Salesforce requires the scope for this flow.

1. Choose **Save**. Allow up to 10 minutes for the change to take effect before you test.

## Step 3: Pre-authorize the users who will query the knowledge base
<a name="kb-managed-salesforce-jwt-bearer-step3"></a>

1. On the app's **Policies** tab, under **OAuth Policies**, set **Permitted Users** to **Admin approved users are pre-authorized**.

1. Add every Profile or Permission Set held by users who query the knowledge base.

1. If the crawl uses the same External Client App, also pre-authorize the Run-As user through a Profile or Permission Set on the app. Otherwise, the crawl fails after you change **Permitted Users**.

Only pre-authorized users can be checked. A user outside the pre-authorized Profiles and Permission Sets gets no results from this data source.

**Note**  
Pre-authorization is ongoing. When a new group of users starts using the knowledge base, add their Profile or Permission Set to the app. A dedicated Permission Set assigned to every such user makes this a single assignment per user.

## Step 4: Review org settings and user data
<a name="kb-managed-salesforce-jwt-bearer-step4"></a>
+ **Turn off session IP locking.** In **Setup** > **Session Settings**, clear **Lock sessions to the IP address from which they originated**. With it selected, access checks can't complete and the data source returns no results for any user.
+ **Review login IP ranges and login hours.** Profile login IP ranges and login hours also apply to the access check. A user blocked by them gets no results.
+ **Give querying users the API Enabled permission.** A user without the **API Enabled** permission gets no results.
+ **Give each user a unique email address.** The connector identifies the querying user by email address. Salesforce requires unique usernames but allows shared email addresses, so a user whose email address belongs to more than one active Salesforce user gets no results. To find shared addresses, run this query in the Developer Console:

  ```
  SELECT Email, COUNT(Id) FROM User WHERE IsActive = true GROUP BY Email HAVING COUNT(Id) > 1
  ```
+ **Give the Run-As user Read access to Users.** The connector uses the Run-As user to look up the querying user's Salesforce username from their email address.

## Step 5: Create the Secrets Manager secret
<a name="kb-managed-salesforce-jwt-bearer-step5"></a>

Document-level access controls use the authentication type `OAUTH2_WITH_JWT_BEARER`. Its secret contains the three Client Credentials fields plus three more. Store it in an AWS Secrets Manager secret in the same AWS Region as your knowledge base:

```
{
    "clientId": "{{your-consumer-key}}",
    "clientSecret": "{{your-consumer-secret}}",
    "instanceUrl": "https://{{your-domain}}.my.salesforce.com",
    "consumerKey": "{{your-consumer-key}}",
    "privateKey": "{{contents-of-jwt-signing-pkcs8.key}}",
    "instanceType": "PROD"
}
```


**Secret fields**  

| Field | Description | 
| --- | --- | 
| clientId | The External Client App's Consumer Key. Used by the Client Credentials Flow for the crawl and the user lookup. | 
| clientSecret | The External Client App's Consumer Secret. | 
| instanceUrl | Your org's My Domain base URL (include https://, no trailing slash). This value must match the connection hostUrl. | 
| consumerKey | The Consumer Key of the app that holds the certificate from step 2. When one app serves both flows, this is the same value as clientId. | 
| privateKey | The contents of jwt-signing-pkcs8.key, unencrypted PKCS\#8. The stored value must contain real line breaks. In the JSON secret, encode them as \\n escapes. A value that still contains literal backslash-n characters after decoding isn't valid. | 
| instanceType | PROD for a production or Developer Edition org, or SANDBOX for a sandbox. A value that doesn't match the org type denies access to every user. | 

**Tip**  
To avoid editing line breaks by hand, build `secret.json` with `jq`, which reads the key file and encodes its line breaks for you:  

```
jq -n \
  --arg clientId "{{your-consumer-key}}" \
  --arg clientSecret "{{your-consumer-secret}}" \
  --arg instanceUrl "https://{{your-domain}}.my.salesforce.com" \
  --arg consumerKey "{{your-consumer-key}}" \
  --rawfile privateKey jwt-signing-pkcs8.key \
  --arg instanceType "PROD" \
  '{clientId: $clientId, clientSecret: $clientSecret, instanceUrl: $instanceUrl, consumerKey: $consumerKey, privateKey: $privateKey, instanceType: $instanceType}' \
  > secret.json
```

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-salesforce-acl-creds}} \
  --secret-string file://secret.json
```

Delete `secret.json` after you create the secret.

Record the secret ARN from the response. You use it as the data source `secretArn`. The knowledge base execution role must have `secretsmanager:GetSecretValue` permission on the secret.

## Rotate the signing key
<a name="kb-managed-salesforce-jwt-bearer-rotate"></a>

To replace the key, generate a new key pair (step 1), upload the new certificate to the app, update `privateKey` in the secret, and then remove the old certificate. Until the secret holds a key that matches a certificate on the app, access checks fail and the data source returns no results.

## Next steps
<a name="kb-managed-salesforce-jwt-bearer-next"></a>

After you store the secret, create the data source with document-level access controls enabled. See [Document-level access controls](kb-managed-ds-salesforce-acl.md).