

# Set up Client Credentials Grant authentication for Box
<a name="kb-managed-box-ccg-setup"></a>

Client Credentials Grant (`CCG`) authentication is the recommended authentication method for a Box data source. The connector authenticates as a Box app using the Client Credentials Grant (2LO) flow, with a service account (not a user) that crawls all enterprise content and no interactive sign-in. It is the only authentication method that supports document-level access control (ACLs). Use it for most deployments.

## Step 1: Create the Box app
<a name="kb-managed-box-ccg-step1"></a>

1. Navigate to the [Box Developer Console](https://app.box.com/developers/console).

1. Choose **Create a New App**.

1. Under **Authentication Method**, select **Server Authentication**.

1. Select **Client Credentials Grant** (marked as **Recommended** by Box).

1. Name the app and choose **Create**. You are taken to the configuration page.

## Step 2: Configure app permissions
<a name="kb-managed-box-ccg-step2"></a>

**Access level** — Under **App Access Level**, select **App \+ Enterprise Access**.

**Important**  
Without App \+ Enterprise access, the service account cannot view all enterprise data and the connector fails to crawl.

**Content actions (required)** — Enable both of the following:
+ Read All Files and Folders
+ Write All Files and Folders

**Important**  
Box treats downloads as a write interaction, so **Write** is required even for read-only crawling.

**Administrative actions** — Enable both of the following:
+ Manage Users
+ Manage Groups

**Note**  
Administrative actions are required for document-level access control (ACL) support. If you do not need ACLs, you can omit them. Box offers only the full manage permission set — there is no read-only option.

**Additional configuration** — Enable **Make API calls using the as-user header**. This allows the connector to delegate as individual users and crawl per-user content. Leave **Generate user access tokens** off.

## Step 3: Save and collect credentials
<a name="kb-managed-box-ccg-step3"></a>

1. Choose **Save**. You see an **App settings saved successfully** confirmation.

1. In the right panel (**App Details** > **Access**), copy the **Client ID**.

1. Choose **Fetch Secret** to reveal the **Client Secret**, then copy it.
**Note**  
The client secret is not shown automatically after creation. You must choose **Fetch Secret** to reveal it. Do this immediately after saving, before navigating away.

1. Scroll down to **Properties** in the right panel and collect the **User ID** (`ccgUserId`) and **Enterprise ID** (`enterpriseId`).

## Step 4: Authorize the app
<a name="kb-managed-box-ccg-step4"></a>

After you save, the **Status** panel on the right shows **Authorization: Not Submitted** with an **Authorize** button.

1. Choose **Authorize** to submit for admin review.

1. An enterprise admin must approve the app before it can be used.

**Important**  
The app does not function until admin authorization is granted. **Not Submitted** means the app fails at runtime.

## Step 5: Create the Secrets Manager secret
<a name="kb-managed-box-ccg-step5"></a>

Store the credentials in an AWS Secrets Manager secret with the following key-value pairs:

```
{
    "clientId": "{{your-client-id}}",
    "clientSecret": "{{your-client-secret}}",
    "enterpriseId": "{{your-enterprise-id}}",
    "ccgUserId": "{{your-user-id}}"
}
```


**CCG secret fields**  

| Field | Description | 
| --- | --- | 
| clientId | App client ID from the Access section (right panel). | 
| clientSecret | Revealed by choosing Fetch Secret after saving the app. | 
| enterpriseId | From the Properties panel. Identifies the Box enterprise instance to crawl. | 
| ccgUserId | From the Properties panel. Validates that the credentials can delegate as a user. | 

Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name {{bedrock-box-ccg-creds}} \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source `secretArn`.

## Next steps
<a name="kb-managed-box-ccg-next"></a>

After you store the secret, create the data source with `authType` set to `CCG`. See [Connect a Box data source](kb-managed-ds-box-connect.md). To filter query results by user permissions, see [Document-level access controls](kb-managed-ds-box-acl.md).