# Asana integration

Connect Amazon Quick to your Asana workspace to manage projects, tasks, and team collaboration. You can create, update, and manage Asana content without leaving your Amazon Quick environment. For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## What you can do

With Asana integration, you can perform actions within your Asana workspaces through the Asana API.

**Connector**

Create, update, and manage projects, tasks, and team assignments through the Asana API.

## Set up Asana integration

Follow these steps to connect Amazon Quick to your Asana workspace.

1. In the Amazon Quick console, choose **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Asana**.
4. Fill in the following details:

   - **Name** - Enter a descriptive name for your Asana integration.
   - **Description** - Describe the purpose of this integration.

5. Choose the connection type and configure the network type settings.
6. Configure the authentication settings based on your chosen authentication method.
7. Select **Create and continue**.
8. Add users to share the integration with.
9. Click **Next**.

## Configure authentication

Asana integration uses custom user-based OAuth authentication. Configure the following authentication fields:

- **Base URL** - Asana API base URL.
- **Client ID** - Your Asana OAuth app client ID.
- **Client Secret** - Your Asana OAuth app client secret.
- **Authorization URL** - Asana OAuth authorization endpoint.
- **Redirect URL** - OAuth redirect URI for your application.

### Required OAuth scopes

When you create your Asana OAuth application, configure these scopes:

- `tasks:write` - Create and modify tasks.
- `tasks:read` - Read task information.
- `workspaces:read` - Access workspace information.
- `workspaces.typeahead:read` - Search within workspaces.
- `stories:read` - Read task stories and comments.
- `users:read` - Access user information.
- `projects:read` - Read project information.
- `project_templates:read` - Access project templates.

## Manage Asana integrations

You can perform these management tasks for your Asana integrations:

- **Edit integration settings** - Update authentication settings or Asana configuration.
- **Share integration access** - Make the integration available to other users.
- **Delete integration** - Remove the integration and revoke authentication.
