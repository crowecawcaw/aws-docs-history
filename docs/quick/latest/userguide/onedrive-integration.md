# Microsoft OneDrive integration

With Microsoft OneDrive integration, you can perform actions on OneDrive files and folders. You can also create knowledge bases from OneDrive content including documents, spreadsheets, and presentations.

## What you can do

OneDrive integration provides two types of capabilities to help you work with your OneDrive content.

**Action connector**

Create, update, delete, and manage OneDrive content through API calls.

**Knowledge base**

Connect to OneDrive to ask questions and get insights from your documents,
spreadsheets, presentations, and other file types.

## Before you begin

Make sure you have the following before you set up OneDrive integration.

- Microsoft OneDrive account.
- Appropriate OneDrive permissions for the content you want to access.
- For action connectors: Amazon Quick Enterprise subscription
- For data access: Amazon Quick Professional subscription –

As a one-time step from the admin, your Microsoft admin may need to grant
organizational consent first before users can create a OneDrive integration to
bring data. This is because Microsoft requires admin approval when using new
applications (in our case the managed OAuth application), unless your user
consent setting allows bypassing the admin approval. Admins can grant
organization-wide consent by signing in and checking "Consent on behalf of your
organization" during an integration creation for OneDrive.

## Prepare Microsoft App Registration and authentication

Before setting up the integration in Amazon Quick, prepare your Microsoft App Registration and authentication credentials. OneDrive integration supports different authentication methods depending on your integration type.

### Action connector authentication setup

For action connectors, gather authentication credentials using one of these methods:

**User authentication (OAuth)**

Gather the following information from your Microsoft App Registration:

- **Base URL** - Microsoft Graph API base URL.
- **Client ID** - Microsoft 365 application client ID.
- **Client Secret** - Microsoft 365 application client secret.
- **Token URL** - Microsoft OAuth token endpoint.
- **Auth URL** - Microsoft OAuth authorization endpoint.
- **Redirect URL** - OAuth redirect URI, this is the Amazon Quick URL.

**Required OAuth scopes
(Delegated):**

- Files.Read.All
- Notes.Read.All
- User.Read
- Sites.Read.All
- offline_access
- AllSites.Read (sharepoint)

**Service authentication (OAuth)**

Gather the following information from your Microsoft App Registration:

- **Base URL** - Microsoft Graph API base URL.
- **Client ID** - Service application client ID.
- **Client Secret** - Service application client secret.
- **Token URL** - Microsoft OAuth token endpoint.

**Required scope for token generation:**

- `.default` - Default application permissions scope.

### Data access authentication setup

Amazon Quick supports creating OneDrive knowledge base integrations using
three-legged OAuth (3LO). For this approach, Amazon Quick registers a multi-tenant
app with delegated permissions _(Sites.Read.All)_
in their Microsoft Entra account. The delegated permissions model keeps risk low,
despite being a multi-tenant application. Amazon Quick can only access data through
authenticated users' permissions. The security model ensures Quick is limited to
what your users can access.

When an admin grants the organizational consent to allow users to bring data to
Amazon Quick, Azure automatically creates a Service Principal (Enterprise
Application) in the customer tenant. You can disable or delete this Service
Principal anytime from their Enterprise Applications, immediately revoking all
access.

For data access integrations, prepare for Microsoft sign-in authentication. During the integration setup, you will need to:

1. Sign in with your Microsoft account that has access to the OneDrive content.
2. Grant the requested permissions to allow Amazon Quick to access your OneDrive data.
3. Complete the authentication process.

## Set up OneDrive integration

After preparing your Microsoft App Registration and authentication credentials, use the Integrations tab in the Amazon Quick console to set up OneDrive integration.
The setup process varies based on whether you want to perform actions, create knowledge bases, or both.

1. In the Amazon Quick console, choose **Integrations**.
2. Click the Add (plus "+") button.
3. Choose **Microsoft OneDrive** from the integration options.
4. Select your integration type:
   - **Bring data from Microsoft OneDrive** - Sets up data connections for knowledge base creation.
   - **Perform actions in Microsoft OneDrive** - Enables actions like creating, updating, or managing OneDrive files.

5. For knowledge base creation (Bring data from Microsoft OneDrive):
   1. Select **Next**.
   2. Complete authentication.
   3. Select which files from your drive you want to add.
   4. Add Name and Description.
   5. Select **Create**.

6. For actions (Perform actions in Microsoft OneDrive):
   1. Select **Next**.
   2. Add Name and description.
   3. Choose connection type:
      - **User authentication** - OAuth-based authentication for individual user access.
      - **Service authentication** - Service-to-service authentication for application access.

   4. Fill in connection settings based on your selected authentication method (either user or service) using the credentials you prepared earlier.
   5. Select **Create and continue**.
   6. Choose users to share the integration with.
   7. Click **Next**.

## Manage knowledge bases

After setting up your OneDrive integration, you can create and manage knowledge bases from your OneDrive content.

### Edit existing knowledge bases

You can modify your existing OneDrive knowledge bases:

1. In the Amazon Quick console, choose **Knowledge bases**.
2. Select your OneDrive knowledge base from the list.
3. Choose **Actions**, then choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same OneDrive integration:

1. In the Amazon Quick console, choose **Integrations**, and
   then select the **Data** tab.
2. Choose your existing OneDrive integration from the list.
3. Choose the three-dot icon under **Actions**,
   then choose **Create knowledge base**.
4. Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

You can create knowledge bases from these OneDrive content types.

- Microsoft Office documents (Word, Excel, PowerPoint).
- PDF files.
- Text files and rich text documents.
- Text documents with embedded images
- Audio, video, and other common document formats.

###### Note

Amazon Quick doesn’t sync ACLs from data sources. When you create a knowledge base in Amazon Quick,
by default only you can get insights from the knowledge base.
For shared content, you can provide access to different users and groups by updating the knowledge base permissions.

## Limitations

When using One Drive integrations in Amazon Quick, be aware of the following
limitations:

- File comments synchronization is not supported.
