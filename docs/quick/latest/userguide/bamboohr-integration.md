# BambooHR integration

Connect Amazon Quick to your BambooHR system to manage employee data, time-off requests, and HR processes. You can create, update, and manage HR content without leaving your Amazon Quick environment. This integration requires Amazon Quick Pro tier or higher.

## What you can do

With BambooHR integration, you can perform actions within your BambooHR systems through the BambooHR API.

**Action connector**

Create, update, and manage employee records, time-off requests, and other HR processes through the BambooHR API.

## Set up BambooHR integration

Follow these steps to connect Amazon Quick to your BambooHR system.

1.  In the Amazon Quick console, choose **Integrations**.
2.  Click **Add** (plus "+" button).
3.  Complete the integration details:
    - **Name** - Enter a descriptive name for your BambooHR integration.
    - **Description** (Optional) - Describe the purpose of this integration.

4.  Choose connection type (user or service authentication).
5.  Complete the connection settings based on authentication method:
    - **For User authentication (OAuth):**

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

    ###### Note

    Additional scopes may be required depending on the specific BambooHR actions you plan to use. Consult your BambooHR administrator for the complete list of available scopes.
    - **For Service authentication (API Key):**
      - **Base URL** - Your BambooHR instance URL.
      - **API Key** - Your BambooHR API key.
      - **Email** - Email address associated with the API key.

6.  Select **Create and continue**.
7.  Select users to share the integration with.
8.  Click **Next**.

## Manage BambooHR integration

You can perform these management tasks for your BambooHR integration:

### Edit integration settings

To modify your BambooHR integration settings:

1. In the Amazon Quick console, choose **Integrations**.
2. Choose **BambooHR** from the integration grid.
3. Select your integration from the list and choose **Edit**.
4. Modify your integration settings as needed.
5. Choose **Save changes**.

### Share integration

You can share your BambooHR action connector with other users in your organization.

1. From the BambooHR integration details page, choose **Share**.
2. Configure your sharing options and permission levels.
3. Choose **Share integration**.

### Delete integration

To permanently remove your BambooHR integration:

1. From the BambooHR integration details page, choose **Delete**.
2. Review the deletion impact, including any workflows or automations using this integration.
3. Type the integration name to confirm deletion.
4. Choose **Delete integration**.

## What happens next

After you complete the setup, your BambooHR integration appears in the integrations list. You can use it in Amazon Quick workflows, automations, and AI agents to perform HR-related tasks.

## Troubleshoot BambooHR integration

If you encounter issues with your BambooHR integration, try these solutions:

Authentication failures

Verify that your BambooHR credentials are correct and that the API key or OAuth application has the necessary permissions.

Connection timeouts

Check that your BambooHR instance URL is correct and accessible from Amazon Quick.

Permission errors

Ensure that the authenticated user or API key has the required permissions to perform the requested HR operations in BambooHR.

Action execution failures

Review the action parameters and ensure they match the expected format for BambooHR API calls.
