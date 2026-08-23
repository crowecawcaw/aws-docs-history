# Set up OAuth 2.0 Client Credentials authentication for ServiceNow

Use the ServiceNow Table API with OAuth 2.0 Client Credentials (2LO) for
authentication. Complete all the following steps in your ServiceNow instance before you
configure the data source in Amazon Bedrock.

## Step 1: Enable client credentials grant type

1. In ServiceNow, navigate to `sys_properties.list` using the
   filter navigator.
2. Create a new system property with the following values:

   - **Name** –
     `glide.oauth.inbound.client.credential.grant_type.enabled`
   - **Type** –
     `true | false`
   - **Value** –
     `true`

## Step 2: Create a dedicated service account

1. Navigate to **User Administration** >
   **Users**.
2. Choose **New** and complete the form:

   - **User ID** – A descriptive name
     (for example, `svc.amazon.quick.kb`).
   - **Web service access only** –
     Checked. This prevents interactive login.
   - **Password** – Set a strong
     password. The connector uses OAuth, but a password is required
     for account creation.

3. Choose **Submit**.

## Step 3: Assign service account roles

1. Open the service account (**User
   Administration** > **Users** >
   your service account).
2. Under the **Roles** tab, choose **Edit** and add the following roles:

   - `knowledge_admin` – Full read access to all
     knowledge base articles. Bypasses per-KB user criteria
     restrictions.
   - `catalog_admin` – Full read access to all
     service catalog items. Bypasses per-catalog restrictions.

3. Choose **Save**.

###### Note

After saving, you see approximately 14 total roles. ServiceNow
auto-inherits contained roles from the `_admin` parent roles. You
only manually assign the two roles listed in step 2 (`knowledge_admin`
and `catalog_admin`). Do not assign the `admin`,
`itil`, or `snc_read_only` roles.

## Step 4: Register the OAuth application

1. Navigate to **System OAuth** > **Application Registry**.
2. Choose **New** > **Create an OAuth API endpoint for external clients**.
3. Complete the form:

   - **Name** – A descriptive name
     (for example, `Amazon-Quick-KB-Client`).
   - **Redirect URL** – Leave
     blank. Not required for client credentials flow.

4. Choose **Submit**.
5. Immediately copy the **Client ID** and
   **Client Secret**. The Client Secret is only
   shown once.

###### Important

You must use the interceptor page to create the application. Do not create the
record by directly inserting into the `oauth_entity` table.

## Step 5: Configure the OAuth application

1. Re-open the application record from the Application Registry list.
2. If the **OAuth Application User** field is
   not visible, add it using **Configure** >
   **Form Builder**.
3. Set the following fields:

   - **OAuth Application User** –
     Your service account (for example,
     `svc.amazon.quick.kb`).
   - **Scope Restriction** –
     `Broadly scoped`.
   - **Client Type** –
     `integration_as_a_service`.

4. Choose **Update**.

## Step 6: Configure API access policies

Without API access policies, tokens authenticate but the Table API returns
HTTP 401. Complete both sub-steps below.

###### Create the Inbound Authentication Profile

1. Navigate to **System Web Services** >
   **API Access Policies** > **Inbound Authentication Profile**.
2. Choose **New** and set:

   - **Name** – For example,
     `Amazon-Quick-KB-Client-Profile`.
   - **Type** –
     `OAuth`.
   - **OAuth Entity** – Select
     your OAuth application.

3. Choose **Submit**.
4. Re-open the profile. In the **Authentication
   Policies** related list, choose **Edit** and add **Allow Access
   Policy**. Choose **Save**.

###### Create the REST API Access Policy

1. Navigate to **System Web Services** >
   **API Access Policies** > **REST API Access Policies**.
2. Choose **New** and set:

   - **Name** – For example,
     `Table API Oauth access policy`.
   - **REST API** –
     `Table API`.
   - **REST API Path** –
     `now/table`.
   - **Apply to all methods** –
     Checked.
   - **Apply to all resources** –
     Checked.
   - **Apply to all tables** –
     Checked.
   - **Apply to all versions** –
     Checked.

3. Choose **Submit**.
4. Re-open the policy. In the **Inbound authentication
   profiles** related list, choose **Edit** and add your Inbound Authentication Profile. Choose
   **Save**.

## Step 7: Verify the OAuth flow

Before you configure the data source, verify that the OAuth flow works
end-to-end.

**Request a token:**

```
curl -s -X POST "https://`INSTANCE`.service-now.com/oauth_token.do" \
  -d "grant_type=client_credentials" \
  -d "client_id=`CLIENT_ID`" \
  -d "client_secret=`CLIENT_SECRET`"
```

**Verify Table API access:**

```
curl -s "https://`INSTANCE`.service-now.com/api/now/table/kb_knowledge?sysparm_limit=1" \
  -H "Authorization: Bearer `ACCESS_TOKEN`"
```

The following table describes each verification result and the action to
take.

Verification results| Result | Meaning | Action |
| --- | --- | --- |
| HTTP 200 with data | Working correctly | Proceed to create the Secrets Manager secret. |
| HTTP 200 with empty array | Missing `knowledge_admin` role | Assign the `knowledge_admin` role to the service<br>account. |
| HTTP 401 | API access policy not configured | Verify both the Inbound Authentication Profile and the REST API<br>Access Policy configuration. |

## Step 8: Create the Secrets Manager secret

Store the credentials in an AWS Secrets Manager secret in the same AWS Region as your
knowledge base with the following key-value pairs:

```
{
    "clientId": "`your-client-id`",
    "clientSecret": "`your-client-secret`",
    "instanceUrl": "https://`YOUR_INSTANCE`.service-now.com"
}
```

Secret fields| Field | Description |
| --- | --- |
| `clientId` | The App Client ID from step 4. |
| `clientSecret` | The App Client Secret revealed at creation time in step 4. |
| `instanceUrl` | Full ServiceNow instance URL (include `https://`,<br>no trailing slash). |

###### Important

The `instanceUrl` must not have a trailing slash.

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name `bedrock-servicenow-creds` \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source
`secretArn`.

## Next steps

After you store the secret, create the data source. See [Connect a ServiceNow data source](kb-managed-ds-servicenow-connect.md "kb-managed-ds-servicenow-connect.md").
