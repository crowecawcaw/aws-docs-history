# Microsoft SharePoint integration

With Microsoft SharePoint integration, you can perform actions on SharePoint lists and
items. You can also create knowledge bases from SharePoint content including document
libraries, sites, and pages.

## What you can do

SharePoint users can ask questions about content stored in their SharePoint sites and
document libraries. For example, users can inquire about project documents, team sites,
or search for specific information across multiple libraries. The integration enables
users to quickly access and understand information from their SharePoint content,
regardless of location or type, while providing contextual details such as publication
dates, modification history, and document ownership—all contributing to more efficient
information discovery and better-informed decision making.

## Before you begin

Make sure you have the following before you set up SharePoint integration.

- Microsoft SharePoint Online
- For action connectors: Amazon Quick Enterprise subscription
- For data access: Amazon Quick Professional subscription or higher – As a one-time step from the admin, your Microsoft admin may
  need to grant organizational consent first before users can create a SharePoint
  integration to bring data. This is because Microsoft requires admin approval
  when using new applications (in our case the managed OAuth application), unless
  your user consent setting allows bypassing the admin approval. Admins can grant
  organization-wide consent by signing in and checking "Consent on behalf of your
  organization" during an integration creation for SharePoint.

## Prepare Microsoft App Registration and authentication

Before setting up the integration in Amazon Quick, prepare your Microsoft App Registration and authentication credentials. SharePoint integration supports different authentication methods depending on your integration type and user tier.

### Action connector authentication setup

For action connectors, prepare authentication credentials using one of these methods:

**User authentication (3LO)**

Gather the following information from your Microsoft Azure AD app registration:

- **Base URL** - Your SharePoint site URL.
- **Client ID** - AWS application client ID.
- **Client Secret** - AWS application client secret.
- **Token URL** - OAuth token endpoint.
- **Auth URL** - OAuth authorization endpoint.
- **Redirect URL** - OAuth redirect URI.

**Required OAuth scopes:**

- offline_access
- Notes.Read.All
- Sites.Read.All
- AllSites.Read (sharepoint)
- User.Read

**Service authentication (API Key)**

Gather the following information from your SharePoint administrator:

- **Base URL** - Your SharePoint site URL.
- **API Key** - SharePoint API access key.
- **Email** - Associated service account email.

**Required scope for token generation:**

- `.default` - Default application permissions scope.

### Data access authentication setup

Amazon Quick supports creating SharePoint knowledge base integrations using
three-legged OAuth (3LO). For this approach, Amazon Quick registers a multi-tenant
app with delegated permissions _(Sites.Read.All)_
in their Microsoft Entra account. The delegated permissions model keeps risk low,
despite being a multi-tenant application. Quick can only access SharePoint through
authenticated users' permissions. The security model ensures Quick is limited to
what your users can access.

When an admin grants the organizational consent to allow users to bring data to
Amazon Quick, Azure automatically creates a Service Principal (Enterprise
Application) in the customer tenant. You can disable or delete this Service
Principal anytime from their Enterprise Applications, immediately revoking all
access.

For data access integrations, prepare for Microsoft 3LO authentication. During the integration setup, you will need to:

1. Sign in with your Microsoft account that has access to the SharePoint content.
2. Grant the requested permissions to allow Amazon Quick to access your SharePoint data.
3. Complete the authentication process.

## Set up SharePoint integration

After preparing your Microsoft App Registration and authentication credentials, use the Integrations tab in the Amazon Quick console to set up SharePoint integration. The setup process varies based on whether you want to perform actions, access data, or both.

1. In the Amazon Quick console, choose **Integrations**.
2. Choose **Microsoft SharePoint** from the integration
   options, and click the Add (plus "+") button.
3. Select your integration type:
   - **Bring data from Microsoft SharePoint** - Sets up data connections for knowledge base creation.
   - **Perform actions in Microsoft SharePoint** - Enables actions on SharePoint lists and items.

4. For knowledge base creation (Bring data from Microsoft SharePoint):
   1. Select **Next**.
   2. Fill in Name and complete authentication.
   3. Select which pages/files/folders you want to add.
   4. Fill in details like Name, Description, and content URLs.
   5. Select **Create and continue**.

5. For actions (Perform actions in Microsoft SharePoint):
   1. Select **Next**.
   2. Add Name and description.
   3. Choose connection type:
      - **User authentication** - 3LO-based authentication for individual user access.
      - **Service authentication** - API key-based authentication for service access.

   4. Fill in connection settings based on your selected authentication method (either user or service) using the credentials you prepared earlier.
   5. Select **Create and continue**.
   6. Choose users to share the integration with.
   7. Click **Next**.

After clicking **Create**, the data sync is started
automatically.

### Review available task actions

After setting up your SharePoint integration with action capabilities, review the available task actions to understand what operations you can perform. See [Available task actions](#sharepoint-integration-task-actions "#sharepoint-integration-task-actions") for the complete list of available actions.

### Configure knowledge bases

After setting up your SharePoint integration with data access capabilities, you can create additional knowledge bases. See [Manage knowledge bases](#sharepoint-integration-knowledge-base "#sharepoint-integration-knowledge-base") for detailed configuration options.

## Available task actions

SharePoint action connector provides 19 actions for managing SharePoint content.

| SharePoint Actions | Action Name                           | Description | Type |
| ------------------ | ------------------------------------- | ----------- | ---- |
| Create Item        | Create a new list item                | Write       |
| Update Item        | Update an existing list item          | Write       |
| Delete Item        | Delete a list item                    | Write       |
| Get Item           | Retrieve a specific list item         | Read        |
| List Items         | List items in a SharePoint list       | Read        |
| Get List           | Retrieve details of a SharePoint list | Read        |

###### Note

Additional actions are available for Excel file management, site operations, and advanced list management. Review the complete action list after you create your integration.

## Manage knowledge bases

After setting up your SharePoint integration, you can create and manage knowledge bases from your SharePoint content.

### Edit existing knowledge bases

You can modify your existing SharePoint knowledge bases:

1. In the Amazon Quick console, choose **Knowledge bases**.
2. Select your SharePoint knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same SharePoint integration:

1. In the Amazon Quick console, choose **Integrations**, and then select the **Data** tab.
2. Choose your existing SharePoint integration from the list.
3. Choose the three-dot icon under **Actions**, then choose **Create knowledge base**.
4. Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

### Supported content types

You can create knowledge bases from these SharePoint content types.

- **Document libraries:** Word, Excel, PowerPoint, PDF, OneNote (.one)
- **Media files:** MP3, MP4, MOV, WMV
- **Site pages and wiki pages**

## Manage SharePoint integrations

###### Note

Amazon Quick doesn't sync ACLs from data sources. When you create a knowledge base in Amazon Quick,
by default only you can get insights from the knowledge base.
For shared content, you can provide access to different users and groups by updating the knowledge base permissions.

## Troubleshooting

Use this section to resolve common issues with SharePoint integration.

### Authentication issues

#### Azure AD problems

**Symptoms:** Authentication fails with Azure AD errors, token refresh failures, or permission denied messages.

**Causes and resolutions:**

- **Incorrect app registration:** Verify the Azure AD app registration includes the required API permissions and OAuth scopes.
- **Expired client secret:** Check if the client secret has expired and generate a new one if needed.
- **Insufficient permissions:** Ensure the app registration has been granted admin consent for the required permissions.
- **Incorrect redirect URI:** Verify the redirect URI in Azure AD matches the one configured in Amazon Quick.

#### Permission sync failures

**Symptoms:** Users cannot access content they should have permissions for, or see content they shouldn't access.

**Causes and resolutions:**

- **Permission propagation delay:** SharePoint permissions may take time to propagate. Wait 15-30 minutes and retry.
- **Nested group permissions:** Check if the user is part of nested security groups that may affect permissions.
- **Broken permission inheritance:** Verify that SharePoint items haven't broken permission inheritance unexpectedly.

### Sync performance issues

#### Slow sync

**Symptoms:** Knowledge base sync takes longer than expected or appears to hang.

**Causes and resolutions:**

- **Large content volume:** Reduce the scope of content being synced by applying more restrictive filters.
- **Network connectivity:** Check network connection stability and bandwidth availability.
- **SharePoint throttling:** SharePoint may be throttling requests. Retry the sync during off-peak hours.

#### Content discovery problems

**Symptoms:** Expected SharePoint content is not appearing in the knowledge base.

**Causes and resolutions:**

- **Content filters too restrictive:** Review and adjust content filtering settings to include the missing content.
- **Unsupported content types:** Verify that the content type is supported by SharePoint integration.
- **Permission restrictions:** Ensure the integration has appropriate permissions to access the content.

### Common error messages

`AADSTS50020: User account from identity provider does not exist in tenant`

**Cause:** The user account is not properly configured in Azure AD.

**Resolution:** Verify the user account exists in the correct Azure AD tenant and has appropriate licenses.

`Access denied. You do not have permission to perform this action`

**Cause:** Insufficient SharePoint permissions for the requested operation.

**Resolution:** Contact your SharePoint administrator to verify and grant appropriate permissions.

`The request is throttled`

**Cause:** SharePoint is limiting the number of requests due to high usage.

**Resolution:** Wait and retry the operation. Consider reducing the frequency of requests or syncing during off-peak hours.
