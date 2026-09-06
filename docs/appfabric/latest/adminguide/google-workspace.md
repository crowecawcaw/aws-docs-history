

# Configure Google Workspace for AppFabric
<a name="google-workspace"></a>

Google Workspace is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google.

You can use AWS AppFabric for security to audit logs and user data from Google Workspace, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support forGoogle Workspace](#google-workspace-appfabric-support)
+ [Connecting AppFabric to your Google Workspace account](#google-workspace-appfabric-connecting)

## AppFabric support forGoogle Workspace
<a name="google-workspace-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from Google Workspace.

### Prerequisites
<a name="google-workspace-prerequisites"></a>

To use AppFabric to transfer audit logs from Google Workspace to supported destinations, you must meet the following requirements:
+ You must subscribe to the Google Workspace Enterprise Standard plan. For more information about creating or upgrading to the Google Workspace Enterprise Standard plan, see the [Google Workspace Plans](https://workspace.google.com/pricing.html) website.
+ You must have a user with the **Administrator** role in your Google Workspace.
+ For AppFabric to deliver logs, you need to enable [Google Admin SDK API](https://console.cloud.google.com/flows/enableapi?apiid=admin.googleapis.com) on your Google Cloud project. For more information, see [Enable Google Workspace APIs](https://developers.google.com/workspace/guides/enable-apis) in the *Google Workspace Developer Guide*.

### Rate limit considerations
<a name="google-workspace-rate-limits"></a>

Google Workspace imposes rate limits on the Google Workspace API. For more information about Google Workspace API rate limits, see [Limits and Quotas](https://developers.google.com/admin-sdk/reports/v1/limits) on the *Google Workspace Admin Guide* on the Google Workspace website. If the combination of AppFabric and your existing Google Workspace API applications exceed the limit, audit logs appearing in AppFabric might be delayed.

### Data delay considerations
<a name="google-workspace-data-delay"></a>

You might see up to 30-minute delay for most of audit events and up to 4-hours delay for certain audit events to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. For more information, see [ Data retention and lag times](https://support.google.com/a/answer/7061566?hl=en) in the *Google WorkSpace Admin Help website*. However, this might be customizable at an account-level. For assistance contact [Support](https://aws.amazon.com/contact-us/).

## Connecting AppFabric to your Google Workspace account
<a name="google-workspace-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, you must authorize AppFabric with Google Workspace. To find the information required to authorize Google Workspace with AppFabric, use the following steps.

### Create an OAuth application
<a name="google-workspace-create-oauth-application"></a>

AppFabric integrates with Google Workspace using OAuth. To create an OAuth application in Google Workspace, use the following steps:

1. To configure your OAuth consent screen, follow the instructions in [Configure the OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent) in the *Google Workspace Developer Guide* on the Google Workspace website.

   Choose **Internal** for the **User type**.

1. To configure OAuth credentials for AppFabric, follow the instructions in the [OAuth client ID credentials](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) section of the *Create access credentials* page in the *Google Workspace Developer Guide*.

1. Use a redirect URL with the following format.

   ```
   https://{{<region>}}.console.aws.amazon.com/appfabric/oauth2
   ```

   In this URL, `{{<region>}}` is the code for the AWS Region in which you’ve configured your AppFabric app bundle. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the redirect URL is `https://{{us-east-1}}.console.aws.amazon.com/appfabric/oauth2`.

### Required scopes
<a name="google-workspace-required-scopes"></a>

You must add the following scopes to your Google Workspace OAuth application:
+ `https://www.googleapis.com/auth/admin.reports.audit.readonly`
+ `https://www.googleapis.com/auth/admin.directory.user`

If you don't see these scopes, add the **Admin SDK API** to your Google Cloud API library.

### App authorizations
<a name="google-workspace-app-authorizations"></a>

#### Tenant ID
<a name="google-workspace-tenant-id"></a>

AppFabric will request your tenant ID. The tenant ID in AppFabric is your Google Workspace project ID. To find your project ID, see [Locate the project ID](https://support.google.com/googleapi/answer/7014113?hl=en) on the Google API Console Help website.

#### Tenant name
<a name="google-workspace-tenant-name"></a>

Enter a name that identifies this unique Google Workspace. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Client ID
<a name="google-workspace-client-id"></a>

AppFabric will request your client ID. To find your client ID, use the following steps:

1. Find your client ID using the information in the [View Credentials](https://developers.google.com/workspace/guides/manage-credentials#view_credentials) section of the *Manage Credentials* page in the *Google Workspace Developer Guide*.

1. Enter the client ID for your OAuth client into the **Client ID** field in AppFabric.

#### Client secret
<a name="google-workspace-client-secret"></a>

AppFabric will request your client secret. To find your client secret, use the following steps:

1. Find your client secret using the information in the [View Credentials](https://developers.google.com/workspace/guides/manage-credentials#view_credentials) section of the *Manage Credentials* page on the *Google Workspace Developer Guide*.

1. If you need to reset your client secret, use the instructions in the [Reset Client Secret](https://developers.google.com/workspace/guides/manage-credentials#reset_client_secret) section of the *Manage Credentials* page on the *Google Workspace Developer Guide*.

1. Enter the your client secret into the **Client secret** field in AppFabric.

#### Approve authorization
<a name="google-workspace-approve-authorization"></a>

After creating the app authorization in AppFabric you will receive a pop-up window from Google Workspace to approve the authorization. To approve the AppFabric authorization, choose **allow**.