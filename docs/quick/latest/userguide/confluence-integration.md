# Atlassian Confluence integration

With Atlassian Confluence integration in Amazon Quick, you can perform actions on
Confluence content and create knowledge bases from Confluence spaces, pages, and
blog posts. This integration supports both action capabilities and data ingestion
capabilities.

## What you can do

Confluence users can ask questions about content stored in their Confluence spaces and
pages. For example, users can inquire about project documentation, team wikis, or
search for specific information across multiple spaces. The integration enables users to
quickly access and understand information from their Confluence content, regardless of
location or type, while providing contextual details such as publication dates,
modification history, and page ownership—all contributing to more efficient information
discovery and better-informed decision making.

With Confluence actions, you can create, update, and manage pages, spaces, and other Confluence objects directly through Amazon Quick. These action capabilities allow you to streamline content management tasks without leaving your Amazon Quick environment.

## Before you begin

Before you set up Confluence integration, make sure you have the following:

- Atlassian Confluence Cloud
- For action connectors: Amazon Quick Enterprise subscription.
- For data access: Amazon Quick Professional subscription or higher.

## Prepare Atlassian app setup and authentication

Before setting up the integration in Amazon Quick, prepare your Atlassian app and authentication credentials. Confluence integration supports different authentication methods depending on your integration type.

### Action connector authentication setup

For action connectors, gather authentication credentials using one of these methods:

**User authentication (3LO)**

Gather the following information from your Atlassian app setup:

- **Base URL** - Your Confluence instance URL. This is the URL used for API
  calls, and not the same URL that users of Confluence log into.
  It will look something like the following example: [https://api.atlassian.com/ex/confluence/`yourInstanceId`](https://api.atlassian.com/ex/confluence/yourInstanceId "https://api.atlassian.com/ex/confluence/yourInstanceId")
- **Client ID** - Atlassian app client ID.
- **Client Secret** - Atlassian app client secret.
- **Token URL** - Atlassian OAuth token endpoint.
- **Auth URL** - Atlassian OAuth authorization endpoint.
- **Redirect URL** - OAuth redirect URI.

**Required OAuth scopes:**

- `search:confluence` - Search Confluence content. This is a classic scope in
  Confluence.
- `read:page:confluence` - Read page content. This is a granular scope in
  Confluence.
- `write:page:confluence` - Create and modify pages. This is a granular scope in
  Confluence.
- `read:space:confluence` - Access space information. This is a granular scope in
  Confluence.

**Service authentication (API Key)**

Gather the following information from your Confluence administrator:

- **API Key** - Confluence API token.
- **Base URL** - Your Confluence instance URL, used for API calls.
- **Email** - Associated user account email.

### Data access authentication setup

For **Bring data from Atlassian Confluence** integrations, prepare for Confluence authentication. During the integration setup, you will need to:

1. Complete the Confluence authentication popup that appears.
2. Grant permissions for Amazon Quick to access your Confluence content.
3. Review and complete the authentication process.

## Set up Confluence integration

After preparing your Atlassian app and authentication credentials, follow these steps to create your Confluence integration:

### Set up knowledge base integration

To create a Confluence integration for knowledge base creation:

1. In the Amazon Quick console, choose **Integrations**.
2. Click **Add** (plus "+" button).
3. Select **Bring data from Atlassian Confluence Cloud**.
4. Select **Next**.
5. Complete the Name and Confluence URL fields:
   - **Name** - Descriptive name for your integration.
   - **Confluence URL** - The URL of your Atlassian site, will resemble the
     following example: ``your-site`.atlassian.net`

6. Select **Next**.
7. Add Integration details and complete authentication.
8. Select **Next**.
9. Complete the Knowledge base details:
   - **Knowledge base name** - Name for your knowledge base.
   - **Description** - Purpose of the knowledge base.
   - **Content selection** - Choose spaces and pages to include.

### Set up action connector integration

To create a Confluence integration for performing actions:

1. In the Amazon Quick console, choose **Integrations**.
2. Click **Add** (plus "+" button).
3. Select **Perform actions**.
4. Select **Next**.
5. Complete the integration details:
   - **Name** - Descriptive name for your integration.
   - **Description** - Purpose of the integration.

6. Choose connection type (user or service authentication).
7. Configure authentication settings based on your chosen method:
   - **For User authentication (3LO):**
     - **Base URL** - Your Confluence instance URL used for API calls.
     - **Client ID** - Atlassian app client ID.
     - **Client Secret** - Atlassian app client secret.
     - **Token URL** - Atlassian OAuth token endpoint.
     - **Auth URL** - Atlassian OAuth authorization endpoint.
     - **Redirect URL** - OAuth redirect URI.

   - **For Service authentication (API Key):**
     - **API Key** - Confluence API token.
     - **Base URL** - Your Confluence instance URL, which is the URL used for API
       calls.
     - **Email** - Associated user account email.

8. Select **Create and continue**.
9. Select users to share the integration with.
10. Select **Next**.

## Manage knowledge bases

After setting up your Confluence integration, you can create and manage knowledge bases from your Confluence content.

### Edit existing knowledge bases

You can modify your existing Confluence knowledge bases:

1. In the Amazon Quick console, choose **Knowledge bases**.
2. Select your Confluence knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same Confluence integration:

1. In the Amazon Quick console, choose **Integrations**, and then select the **Data** tab.
2. Choose your existing Confluence integration from the list.
3. Choose the three-dot icon under **Actions**, then choose **Create knowledge base**.
4. Configure your knowledge base settings and choose "Create".

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

### Supported content types

You can include these content types in your knowledge base:

- Confluence pages and blog posts.
- Spaces content
- Page and blog attachments

###### Note

Amazon Quick doesn't sync ACLs from data sources. When you create a knowledge base in Amazon Quick,
by default only you can get insights from the knowledge base.
For shared content, you can provide access to different users and groups by updating the knowledge base permissions.
