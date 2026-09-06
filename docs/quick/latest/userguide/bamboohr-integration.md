

# BambooHR integration
<a name="bamboohr-integration"></a>

Connect Amazon Quick to your BambooHR system to manage employee data, time-off requests, and HR processes. You can create, update, and manage HR content without leaving your Amazon Quick environment. For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## What you can do
<a name="bamboohr-integration-capabilities"></a>

With BambooHR integration, you can perform actions within your BambooHR systems through the BambooHR API.

**Connector**  
Create, update, and manage employee records, time-off requests, and other HR processes through the BambooHR API.

## Set up BambooHR integration
<a name="bamboohr-integration-setup"></a>

Follow these steps to connect Amazon Quick to your BambooHR system.

1. In the Amazon Quick console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **BambooHR**.

1. Complete the integration details:
   + **Name** - Enter a descriptive name for your BambooHR integration.
   + **Description** (Optional) - Describe the purpose of this integration.

1. Choose connection type (user or service authentication).

1. Complete the connection settings based on authentication method:
   + **For User authentication (OAuth):**
     + **Base URL** - Your BambooHR instance URL.
     + **Client ID** - OAuth client identifier.
     + **Client Secret** - OAuth client secret.
     + **Token URL** - OAuth token endpoint.
     + **Auth URL** - OAuth authorization endpoint.
     + **Redirect URL** - OAuth callback URL.

     **Required OAuth scopes**: When you create your BambooHR OAuth application, configure the scopes you need for your use case. Common scopes include:
     + `employee` - Access employee information.
     + `employee.write` - Write employee information.
     + `time_off` - Access time off information.
     + `time_off.write` - Write time off information.
     + `company:info` - Access company information.
     + `payroll` - Access payroll data.
**Note**  
Additional scopes may be required depending on the specific BambooHR actions you plan to use. Consult your BambooHR administrator for the complete list of available scopes.
   + **For Service authentication (API Key):**
     + **Base URL** - Your BambooHR instance URL.
     + **API Key** - Your BambooHR API key.
     + **Email** - Email address associated with the API key.

1. Select **Create and continue**.

1. Select users to share the integration with.

1. Click **Next**.

## Manage BambooHR integration
<a name="bamboohr-integration-management"></a>

You can perform these management tasks for your BambooHR integration:

### Edit integration settings
<a name="bamboohr-integration-editing"></a>

To modify your BambooHR integration settings:

1. In the Amazon Quick console, choose **Connectors**.

1. Choose **BambooHR** from the connector list.

1. Select your integration from the list and choose **Edit**.

1. Modify your integration settings as needed.

1. Choose **Save changes**.

### Share integration
<a name="bamboohr-integration-sharing"></a>

You can share your BambooHR connector with other users in your organization.

1. From the BambooHR integration details page, choose **Share**.

1. Configure your sharing options and permission levels.

1. Choose **Share integration**.

### Delete integration
<a name="bamboohr-integration-deletion"></a>

To permanently remove your BambooHR integration:

1. From the BambooHR integration details page, choose **Delete**.

1. Review the deletion impact, including any workflows or automations using this integration.

1. Type the integration name to confirm deletion.

1. Choose **Delete integration**.

## What happens next
<a name="bamboohr-integration-setup-results"></a>

After you complete the setup, your BambooHR integration appears in the integrations list. You can use it in Amazon Quick workflows, automations, and AI agents to perform HR-related tasks.

## Troubleshoot BambooHR integration
<a name="bamboohr-integration-troubleshooting"></a>

If you encounter issues with your BambooHR integration, try these solutions:

Authentication failures  
Verify that your BambooHR credentials are correct and that the API key or OAuth application has the necessary permissions.

Connection timeouts  
Check that your BambooHR instance URL is correct and accessible from Amazon Quick.

Permission errors  
Ensure that the authenticated user or API key has the required permissions to perform the requested HR operations in BambooHR.

Action execution failures  
Review the action parameters and ensure they match the expected format for BambooHR API calls.