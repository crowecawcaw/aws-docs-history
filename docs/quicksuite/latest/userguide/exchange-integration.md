# Microsoft Outlook action connector

With Microsoft Outlook action connector in Amazon Quick Suite, you can perform actions within Outlook systems, including managing emails, calendar events, contacts, and interacting with Microsoft Graph APIs. This action connector supports task execution only and requires Amazon Quick Suite Pro tier or higher.

## What you can do

With Microsoft Outlook integration, you can perform actions within your Outlook systems through the Outlook API.

**Action connector**

Create, update, and manage emails, calendar events, contacts, and other messaging operations through the Outlook API.

## Before you begin

Before you set up Microsoft Outlook action connector integration, make sure you have the following:

- Administrative access to Microsoft Azure Active Directory.
- Microsoft Outlook or Exchange Online account with appropriate permissions.
- Amazon Quick Suite Author or higher.

## Step 1: Register an application in Azure

As an administrator, create a new OAuth 2.0 Microsoft Exchange application in the Microsoft Azure developer console with scoped permissions for performing actions in Amazon Quick Suite.

1. Sign in to the Azure portal and navigate to Azure Active Directory.
2. Choose **App registrations**, then choose **New registration**.
3. Enter a name for your application and configure the registration settings.
4. After registration, copy the **Application (client) ID** and **Directory (tenant) ID** from the application overview page.

## Step 2: Configure API permissions

Add the required Microsoft Graph API permissions to your registered application.

1. In your Azure application, choose **API permissions**.
2. Choose **Add a permission** and select **Microsoft Graph**.
3. Add the following required permissions:
   - `Mail.ReadWrite` - Read and write access to user mail.
   - `Mail.Send` - Send mail as a user.
   - `Calendars.ReadWrite` - Read and write access to user calendars.
   - `User.Read.All` - Read all users' basic profiles.
   - `Contacts.Read` - Read user contacts.
   - `Place.Read.All` - Read all place information.
   - `MailboxSettings.Read` - Read user mailbox settings.

4. Choose **Grant admin consent** to approve the permissions.

## Step 3: Generate a client secret

Create a client secret for your Azure application to authenticate with Amazon Quick Suite.

1. In your Azure application, navigate to **Manage** > **Certificates & secrets**.
2. Choose **New client secret**.
3. Enter a description and choose an expiration period.
4. Choose **Add**.
5. Copy the **Value** immediately. This value is only displayed once.

## Step 4: Set up Microsoft Outlook action connector

After preparing your Azure application credentials, create the Microsoft Outlook action connector in Amazon Quick Suite.

1. In the Amazon Quick Suite console, choose **Integrations**.
2. Click the Add (plus "+") button.
3. Choose **Microsoft Outlook** from the integration options.

###### Note

Microsoft Outlook integration supports action execution only. Data access and knowledge base creation are not available for Outlook systems. 4. Fill in the integration details:

    * **Name** - Enter a descriptive name for your Outlook action connector.
    * **Description** (Optional) - Describe the purpose of this action connector.

5. Choose your connection type:
   - **User authentication** - OAuth for individual user access to Outlook.
   - **Service authentication** - Service-to-service authentication for application access.

6. Fill in the connection settings based on your selected authentication method (either user or service) using the Azure application details you prepared earlier.
7. Select **Create and continue**.
8. Choose users to share the integration with.
9. Click **Next**.

## Step 5: Associate action connector to automation groups

To use Microsoft Outlook actions in automations, you must associate the action connector with your automation groups.

1. Navigate to your automation group settings.
2. Associate the Microsoft Outlook action connector with the automation group that will use these actions.
3. Create a new automation for the automation group to access Microsoft Outlook actions in your workflows.

## Manage Microsoft Outlook action connectors

You can perform these management tasks for your Microsoft Outlook action connectors once they have been created. Select them in the list of "Actions":

- **Edit action connector** - Update authentication settings or Outlook configuration.
- **Share action connector** - Make the action connector available to other users in your organization.
- **Delete action connector** - Remove the action connector and revoke authentication.

### What happens next

After you complete the setup, your Microsoft Outlook action connector appears in the actions list. You can use it in Amazon Quick Suite automations and workflows to manage emails, calendar events, and contacts.
