# Configure Microsoft 365 for AppFabric

Microsoft 365 is a product family of productivity software, collaboration,
and cloud-based services owned by Microsoft.

You can use AWS AppFabric for security to audit logs and user data from Microsoft
365, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output
the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for
  Microsoft 365](#microsoft-365-appfabric-support "#microsoft-365-appfabric-support")
- [Connecting AppFabric to your
  Microsoft 365 account](#microsoft-365-appfabric-connecting "#microsoft-365-appfabric-connecting")

## AppFabric support for

Microsoft 365

AppFabric supports receiving user information and audit logs from Microsoft 365.

### Prerequisites

To use AppFabric to transfer audit logs from Microsoft 365 to supported
destinations, you must meet the following requirements:

- You must subscribe to a Microsoft 365 Enterprise plan. For
  more information about creating or upgrading to a Microsoft
  365 Enterprise plan, see [Microsoft 365 Enterprise Plans](https://www.microsoft.com/en-us/microsoft-365/compare-microsoft-365-enterprise-plans "https://www.microsoft.com/en-us/microsoft-365/compare-microsoft-365-enterprise-plans") on the
  Microsoft website.
- You must have a user with **Administrator**
  permissions in your Microsoft 365 account.
- You must turn on audit logging for your organization. For more
  information, see [Turn auditing on or off](https://learn.microsoft.com/en-us/microsoft-365/compliance/audit-log-enable-disable?view=o365-worldwide "https://learn.microsoft.com/en-us/microsoft-365/compliance/audit-log-enable-disable?view=o365-worldwide") on the Microsoft
  website.

### Rate limit considerations

Microsoft 365 imposes rate limits on the Microsoft
365 API. For more information about Microsoft 365 API rate limits,
see [Microsoft Graph service-specific throttling limits](https://learn.microsoft.com/en-us/graph/throttling-limits "https://learn.microsoft.com/en-us/graph/throttling-limits")
in the Microsoft Graph documentation on the Microsoft
website. If the combination of AppFabric and your existing Microsoft 365
API applications exceed the limit, audit logs appearing in AppFabric might be
delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

Microsoft 365 account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Microsoft 365. To find the information required to authorize
Microsoft 365 with AppFabric, use the following steps.

### Create an OAuth

application

AppFabric integrates with Microsoft 365 using OAuth. To create an OAuth
application in Microsoft 365, use the following steps:

1. Follow the instructions in the [Register an application](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application "https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application") section in the _Azure Active Directory Developer Guide_ on the
   Microsoft website.

Choose **Accounts in this organizational directory only**
in the **Supported Account Types** configuration. 2. Follow the instructions in the [Add a redirect URI](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-redirect-uri "https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-redirect-uri") section in the _Azure
Active Directory Developer Guide_.

Choose the **Web platform**.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the
code for the AWS Region in which you’ve configured your AppFabric app bundle.
For example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

You can skip the other input fields for the Web platform. 3. Follow the instructions in the [Add a client secret](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret "https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret") section of the _Azure Active
Directory Developer Guide_.

### Required permissions

You must add the following permissions to your OAuth application. To add
permissions, follow the instructions in the [Add permissions to access your web API](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-permissions-to-access-your-web-api "https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-permissions-to-access-your-web-api") section of the _Azure
Active Directory Developer Guide_.

- `Microsoft Graph API` > `User.Read`
  (automatically added)
- `Office 365 Management APIs` >
  `ActivityFeed.Read` (Select Delegated Type)
- `Office 365 Management APIs` >
  `ActivityFeed.ReadDlp` (Select Delegated Type)
- `Office 365 Management APIs` >
  `ServiceHealth.Read` (Select Delegated Type)

After you’ve added the permissions, to grant admin consent for the permissions,
follow the instructions in the [Admin consent button](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#admin-consent-button "https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#admin-consent-button") section of the _Azure Active Directory
Developer Guide_.

### App authorizations

AppFabric supports receiving user information and audit logs from your
Microsoft 365 account. To receive both audit logs and user data
from Microsoft 365, you must create two app authorizations, one that
is named **Microsoft 365** in the app authorization
drop-down list, and another that is named **Microsoft 365
Audit Log** in the app authorization drop-down list. You can use the
same tenant ID, client ID and client secret for both app authorizations. To receive
audit logs from Microsoft 365, you need both the
**Microsoft 365** and
**Microsoft 365 Audit Log** app
authorizations. To use the user access tool alone, only the
**Microsoft 365** app authorization is
required.

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your Azure Active
Directory tenant ID. To find your Azure Active Directory tenant ID, see [How to find your Azure Active Directory tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/how-to-find-tenant "https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/how-to-find-tenant") in the
_Azure Product Documentation_ on the
Microsoft website.

#### Tenant name

Enter a name that identifies this unique Microsoft 365 account.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Client ID

AppFabric will request your client ID. The client ID in AppFabric is the
Microsoft 365 application (client) ID. To find your
Microsoft 365 application (client) ID, use the following
steps:

1. Open the overview page for the OAuth application that you use with
   AppFabric.
2. The application (client) ID appears under
   **Essentials**.
3. Enter the application (client) ID for your OAuth client into the
   **Client ID** field in AppFabric.

#### Client secret

AppFabric will request your client secret. Microsoft 365 provides
this value only when you initially create the client secret for your OAuth
application. To generate a new client secret if you don't have one, use the
following steps:

1. To create a client secret, follow the instructions in the [Add a client secret](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret "https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret") section of the _Azure Active
   Directory Developer Guide_ .
2. Enter the contents of the **Value** field into the
   **Client secret** field in AppFabric.

#### Approve

authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Microsoft 365 to approve the authorization. To
approve the AppFabric authorization, choose **allow**.
