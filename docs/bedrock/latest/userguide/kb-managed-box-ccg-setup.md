# Set up Client Credentials Grant authentication for Box

Client Credentials Grant (`CCG`) authentication is the recommended
authentication method for a Box data source. The connector authenticates as a Box app
using the Client Credentials Grant (2LO) flow, with a service account (not a user) that
crawls all enterprise content and no interactive sign-in. It is the only authentication
method that supports document-level access control (ACLs). Use it for most
deployments.

## Step 1: Create the Box app

1. Navigate to the [Box
   Developer Console](https://app.box.com/developers/console "https://app.box.com/developers/console").
2. Choose **Create a New App**.
3. Under **Authentication Method**, select
   **Server Authentication**.
4. Select **Client Credentials Grant** (marked as
   **Recommended** by Box).
5. Name the app and choose **Create**. You are
   taken to the configuration page.

## Step 2: Configure app permissions

**Access level** — Under **App Access Level**, select **App + Enterprise
Access**.

###### Important

Without App + Enterprise access, the service account cannot view all enterprise
data and the connector fails to crawl.

**Content actions (required)** — Enable both of
the following:

- Read All Files and Folders
- Write All Files and Folders

###### Important

Box treats downloads as a write interaction, so **Write** is required even for read-only crawling.

**Administrative actions** — Enable both of the
following:

- Manage Users
- Manage Groups

###### Note

Administrative actions are required for document-level access control (ACL)
support. If you do not need ACLs, you can omit them. Box offers only the full
manage permission set — there is no read-only option.

**Additional configuration** — Enable
**Make API calls using the as-user header**. This allows
the connector to delegate as individual users and crawl per-user content. Leave
**Generate user access tokens** off.

## Step 3: Save and collect credentials

1. Choose **Save**. You see an **App settings saved successfully**
   confirmation.
2. In the right panel (**App Details** >
   **Access**), copy the **Client ID**.
3. Choose **Fetch Secret** to reveal the **Client Secret**, then copy it.

###### Note

The client secret is not shown automatically after creation. You must
choose **Fetch Secret** to reveal it. Do this
immediately after saving, before navigating away. 4. Scroll down to **Properties** in the right
panel and collect the **User ID**
(`ccgUserId`) and **Enterprise ID**
(`enterpriseId`).

## Step 4: Authorize the app

After you save, the **Status** panel on the right
shows **Authorization: Not Submitted** with an **Authorize** button.

1. Choose **Authorize** to submit for admin
   review.
2. An enterprise admin must approve the app before it can be used.

###### Important

The app does not function until admin authorization is granted. **Not Submitted** means the app fails at runtime.

## Step 5: Create the Secrets Manager secret

Store the credentials in an AWS Secrets Manager secret with the following key-value
pairs:

```
{
    "clientId": "`your-client-id`",
    "clientSecret": "`your-client-secret`",
    "enterpriseId": "`your-enterprise-id`",
    "ccgUserId": "`your-user-id`"
}
```

CCG secret fields| Field | Description |
| --- | --- |
| `clientId` | App client ID from the **Access**<br>section (right panel). |
| `clientSecret` | Revealed by choosing **Fetch Secret**<br>after saving the app. |
| `enterpriseId` | From the *_Properties_<br>• panel.<br>Identifies the Box enterprise instance to crawl. |
| `ccgUserId` | From the *_Properties_<br>• panel.<br>Validates that the credentials can delegate as a user. |

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name `bedrock-box-ccg-creds` \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source
`secretArn`.

## Next steps

After you store the secret, create the data source with `authType` set
to `CCG`. See [Connect a Box data source](kb-managed-ds-box-connect.md "kb-managed-ds-box-connect.md"). To filter query results by user
permissions, see [Document-level access controls](kb-managed-ds-box-acl.md "kb-managed-ds-box-acl.md").
