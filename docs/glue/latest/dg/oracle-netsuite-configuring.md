# Configuring Oracle NetSuite

Before you can use AWS Glue to transfer data from Oracle NetSuite, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have a Oracle NetSuite account. For more information, see [Creating a Oracle NetSuite account](#oracle-netsuite-configuring-creating-oracle-netsuite-account "#oracle-netsuite-configuring-creating-oracle-netsuite-account").
- Your Oracle NetSuite account is enabled for API access.
- You have created an OAuth 2.0 API integration in your Oracle NetSuite developer account. This integration provides the client credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [Creating a Oracle NetSuite client app and OAuth 2.0 credentials](#oracle-netsuite-configuring-creating-oracle-netsuite-client-app "#oracle-netsuite-configuring-creating-oracle-netsuite-client-app").

If you meet these requirements, you’re ready to connect AWS Glue to your Oracle NetSuite account.

## Creating a Oracle NetSuite account

Navigate to [Oracle NetSuite](https://www.netsuite.com/portal/home.shtml "https://www.netsuite.com/portal/home.shtml"), and choose **Free Product Tour**. Fill in the required details to get a free product tour, through which you can contact a vendor. The process for procuring an account is as follows:

- The procurement of a NetSuite account is done via a vendor, who provides a form/quote which has to be legally reviewed.
- The account to be procured for Oracle NetSuite connector is of **Standard Cloud Service**.
- This account is created by the vendor and temporary credentials are shared by them. You will receive a welcome mail from NetSuite <billing@notification.netsuite.com> <system@sent-via.netsuite.com> with the details such as your username, and a link to set your password.
- Use the **Set your password** link to set the password for the username provided by the vendor.

## Creating a Oracle NetSuite client app and OAuth 2.0 credentials

To get the Client ID and Client Secret you create a Oracle NetSuite client app:

1. Log into your NetSuite account through the [NetSuite customer login](https://system.netsuite.com/pages/customerlogin.jsp "https://system.netsuite.com/pages/customerlogin.jsp").
2. Choose **Setup** > **Company** > **Enable features**.
3. Navigate to the **SuiteCloud** section and select the **REST WEB SERVICES** checkbox under **SuiteTalk (Web Services)**.
4. Select the **OAUTH 2.0** checkbox under **Manage Authentication**. Click **Save**.
5. Go to **Setup** > **Integration** > **Manage Integrations** and choose **New** to create an OAuth2.0 application.
6. Enter a name of your choice and keep the **STATE** as Enabled.
7. If checked, uncheck the **TBA: AUTHORIZATION FLOW** and **TOKEN-BASED AUTHENTICATION** checkboxes displayed under **Token-based Authentication**.
8. Select the **AUTHORIZATION CODE GRANT** and **PUBLIC CLIENT** checkboxes under **OAuth 2.0**.
9. Under Auth, note the Client ID and Client Secret.
10. Enter a **REDIRECT URI**. For example, https://us-east-1.console.aws.amazon.com/gluestudio/oauth
11. Select the **REST WEB SERVICES** checkbox under **SCOPE**.
12. Select the **USER CREDENTIALS** checkbox under **User Credentials**. Choose **Save**.
13. Note the CONSUMER KEY/CLIENT ID and CONSUMER SECRET/CLIENT SECRET under **Client Credentials**. These values are displayed only once.
14. Create an ADMINISTRATOR role if needed by navigating to **User/Roles** > **Manage Roles** > **New**.
15. While creating a custom role, add full access under the **Permissions** tab for the following entities/functionalities:
    - "Deposit", "Items", "Item Fulfillment", "Make Journal Entry", "Purchase Order", "Subsidiaries", "Vendors", "Bills", "Vendor Return Authorization", "Track Time", "Customer Payment", "Custom Record Entries", "Custom Record Types", "REST Web Services", "OAuth 2.0 Authorized Applications Management", "Custom Entity Fields", "Log in using OAuth 2.0 Access Tokens".

For more information see [OAuth 2.0](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_157769826287.html "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_157769826287.html") in the NetSuite Applications Suite documentation.
