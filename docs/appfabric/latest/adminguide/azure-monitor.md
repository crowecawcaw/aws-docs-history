# Configure Azure Monitor for AppFabric

Azure Monitor is a comprehensive monitoring solution for collecting,
analyzing, and responding to monitoring data from your cloud and on-premises environments.
You can use Azure Monitor to maximize the availability and performance of
your applications and services. It helps you understand how your applications are performing
and allows you to manually and programmatically respond to system events.

Azure Monitor collects and aggregates the data from every layer and
component of your system across multiple Azure and non-Azure subscriptions and tenants. It
stores it in a common data platform for consumption by a common set of tools that can
correlate, analyze, visualize, and/or respond to the data. You can also integrate other
Microsoft and non-Microsoft tools. The Azure Monitor activity log is a
platform log that provides insight into subscription-level events. The activity log includes
information like when a resource is modified or a virtual machine is started.

You can use AWS AppFabric for security to audit logs and user data from Azure
Monitor, normalize the data into Open Cybersecurity Schema Framework (OCSF)
format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Azure
  Monitor](#azure-monitor-appfabric-support "#azure-monitor-appfabric-support")
- [Connecting AppFabric to your
  Azure Monitor account](#azure-monitor-appfabric-connecting "#azure-monitor-appfabric-connecting")

## AppFabric support for Azure

Monitor

AppFabric is capable of receiving user information and audit logs from the following
Azure Monitor services:

- Azure Monitor
- API Management
- Microsoft Sentinel
- Security Center

### Prerequisites

To use AppFabric to transfer audit logs from Azure Monitor to supported
destinations, you must meet the following requirements:

- You need to have a Microsoft Azure account with either a
  free trial or pay-as-you-go subscription.
- At least one subscription is required to fetch the events within that
  subscription.

### Rate limit considerations

Azure Monitor imposes rate limits to the security principal (user
or application) making the requests and the subscription ID or tenant ID. For more
information about the Azure Monitor API rate limits, see [Understand how Azure Resource Manager throttles requests](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling")
on the _Azure Monitor Developer website_.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

Azure Monitor account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Azure Monitor. To find the information required to authorize
Azure Monitor with AppFabric, use the following steps.

### Create an OAuth

application

AppFabric integrates with Azure Monitor using OAuth2. Complete the
following steps to create an OAuth2 application in Azure
Monitor:

1. Navigate to the [Microsoft
   Azure Portal](https://portal.azure.com "https://portal.azure.com") and sign in.
2. Navigate to **Microsoft Entra ID**.
3. Choose **App Registrations**.
4. Choose on **New Registration**.
5. Enter a name for the client such as Azure Monitor OAuth
   Client. This will be the name of the registered application.
6. Verify the **Supported account types** is set to
   **Single Tenant**.
7. For the **Redirect URI**, select **Web**
   as the platform and add a redirect URI. Use the following format for the
   redirect URI:

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In that address, `<region>` is
the code for the AWS Region in which you’ve configured your AppFabric app
bundle. For example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

The authentication response will be sent to the provided URI after
successfully authenticating the user. Providing this now is optional and it
can be changed later, but a value is required for most authentication
scenarios. 8. Choose **Register**. 9. In the registered app, choose on **Certificates &
secrets** and then **New client
secret**. 10. Add a description for the secret. 11. Select the secret expiration duration. You can select any preset duration
from the drop-down or set a custom duration. 12. Choose **Add**. Client secret values can only be viewed
immediately after creation. Be sure to save the secret somewhere safe before
leaving the page.

### Required permissions

You must add the following permissions to your OAuth application. To add
permissions, follow the instructions in the [Add permissions to access your web API](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-your-web-api "https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-your-web-api") section of the
_Microsoft Entra Developer Guide_.

- Microsoft Graph User Access API > User.Read.All (Select
  Delegated Type)
- Microsoft Graph User Access API > offline_access (Select
  Delegated Type)
- Azure Service Management Audit Log API > user_impersonation
  (Select Delegated Type)

After you’ve added the permissions, to grant admin consent for the permissions,
follow the instructions in the [Admin consent button](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#admin-consent-button "https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#admin-consent-button") section of the _Microsoft
Entra Developer Guide_.

### App authorizations

AppFabric supports receiving user information and audit logs from your Azure
Monitor account. To receive both audit logs and user data from
Azure Monitor, you must create two app authorizations, one that
is named **Azure Monitor** in the app authorization
drop-down list, and another that is named **Azure Monitor
Audit Logs** in the app authorization drop-down list. You can use the
same tenant ID, client ID and client secret for both app authorizations. To receive
audit logs from Azure Monitor you need both the
**Azure Monitor** and **Azure
Monitor Audit Logs** app authorizations. To use the user
access tool alone, only the **Azure Monitor** app
authorization is required.

#### Tenant ID

AppFabric will request your tenant ID. Complete the following steps to find your
client ID in **Azure Monitor**:

1. Navigate to the [Microsoft Azure Portal](https://portal.azure.com/ "https://portal.azure.com/").
2. Navigate to **Azure Active Directory**.
3. In the **App Registrations** section, choose the app
   that was previously created.
4. In the **Overview** section, copy the tenant ID from
   the **Directory (tenant) ID** field.

#### Tenant name

Enter a name that identifies this unique Azure Monitor
subscription. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

###### Note

The tenant name should be maximum 2,048 characters consisting of numbers,
lower/upper case letters, and the following special characters: period (.),
underscore (\_), dash (-) and empty space.

#### Client ID

AppFabric will request a client ID. Complete the following procedure to find your
client ID in Azure Monitor:

1. Navigate to the [Microsoft Azure Portal](https://portal.azure.com/ "https://portal.azure.com/").
2. Navigate to **Azure Active Directory**.
3. In the **App Registrations** section, choose the app
   that was previously created.
4. In the **Overview** section, copy the client ID from
   the **Application (client) ID** field.

#### Client secret

AppFabric will request a client secret. Client secret for the registered OAuth app
is what you generated in Step 11 of the OAuth App creation section. If you
misplace the client secret generated during the OAuth app creation, repeat the
steps 8-11 in the OAuth App creation section to regenerate a new one.

#### App authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Microsoft Azure to approve the authorization. Sign in
to your account from the window and approve the AppFabric authorization by choosing
**Allow**.
