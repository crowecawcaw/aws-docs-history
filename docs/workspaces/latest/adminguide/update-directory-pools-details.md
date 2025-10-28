# Update directory details for your

WorkSpaces Pools

You can complete the following directory management tasks using the WorkSpaces Pools
console.

## Authentication

You can configure additional authentication options for your WorkSpaces Pools. Pools
requires SAML 2.0 authentication.

###### To enable and configure SAML 2.0 Identity Provider authentiation

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to authentication and choose **Edit**.
5. Choose **Edit SAML 2.0 Identity Provider**.
6. Check the **Enable SAML 2.0 authentication** checkbox.
7. Enter the **User Access URL** to direct the WorkSpaces Pools client
   during federated sign-in.
8. Enter the **IdP deep link parameter name** (optional).
9. Choose **Save**.

###### To enable and configure Certificate-Based Authentication

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to Authentication and choose **Edit**.
5. Choose **Edit Certificate-Based Authentication**.
6. Check the **Enable Certificate-Based Authentication**
   checkbox.
7. Choose from the dropdown the **AWS Certificate Manager (ACM) Private Certificate
   Authority (CA)**.
8. Choose **Save**.

## Security group

Apply a security group to your WorkSpaces Pools in your directory.

###### To configure security group for your WorkSpaces Pools

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to Security group and choose **Edit**.
5. From the dropdown, choose a security group.

## Active Directory Config

Configure your directory Active Directory Config with an Organization Unit (OU),
directory domain name, and AWS Secrets Manager secret.

###### To configure your Active Directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to Active Directory Config and choose **Edit**.
5. To find an Organizational Unit (OU), you can start typing all or part of the OU
   name and choose the OU you want to use.

###### Note

(Optional) After choosing the OU, rebuild the existing WorkSpaces to update the
OU. For more information, see [Rebuild a WorkSpace in WorkSpaces Personal](rebuild-workspace.md "rebuild-workspace.md") 6. Choose **Save**.

###### Note

The directory domain name and AWS Secrets Manager secret can't be edited after
you've created your pool.

## Streaming properties

Configure how your users can transfer data between their pooled WorkSpace and their
local device.

###### To configure streaming properties

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to Streaming properties and choose **Edit**.
5. Configure the following streaming properties:
   - Clipboard permissions
     - From the drop down list, choose one of the following:
       - **Allow copy and paste** - Allows copying to
         local device and pasting to remote session.
       - **Allow paste to remote session** - Allows
         pasting to remote session.
       - **Allow copy to local device** - Allows
         copying to a local device.
       - Disabled

     - Choose to allow or not allow print to local device.
     - Choose to allow or not allow diagnostic logging.
     - Choose to allow or not allow smart card sign in.
     - To enable Home Folders storage, choose **Enable Home
       Folders**.

6. Choose **Save**.

## IAM role

Select an IAM role for you WorkSpaces Pools.

###### To select an IAM role

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to IAM role and choose **Edit**.
5. Choose an IAM role from the drop down. To create a new IAM role, choose
   **Create new IAM role**.
6. Choose **Save**.

## Tags

Add new tags to your WorkSpaces Pools

###### To add a new tag

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the directory you want to configure.
4. Go to Tags and choose **Manage tags**.
5. Choose **Add new tags** and enter the key pair value that you
   want to use. A key can be a general category, such as "project," "owner," or
   "environment," with specific associated values.
6. Choose **Save changes**.
