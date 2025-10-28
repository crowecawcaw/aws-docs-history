# Configure Google Workspace for

AppFabric

Google Workspace is a collection of cloud computing, productivity and
collaboration tools, software and products developed and marketed by Google.

You can use AWS AppFabric for security to audit logs and user data from Google
Workspace, normalize the data into Open Cybersecurity Schema Framework (OCSF)
format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Google
  Workspace](#google-workspace-appfabric-support "#google-workspace-appfabric-support")
- [Connecting AppFabric to your
  Google Workspace account](#google-workspace-appfabric-connecting "#google-workspace-appfabric-connecting")

## AppFabric support for Google

Workspace

AppFabric supports receiving user information and audit logs from Google
Workspace.

### Prerequisites

To use AppFabric to transfer audit logs from Google Workspace to
supported destinations, you must meet the following requirements:

- You must subscribe to the Google Workspace Enterprise
  Standard plan. For more information about creating or upgrading to the
  Google Workspace Enterprise Standard plan, see the [Google
  Workspace Plans](https://workspace.google.com/pricing.html "https://workspace.google.com/pricing.html") website.
- You must have a user with the **Administrator** role in your Google
  Workspace.
- For AppFabric to deliver logs, you need to enable [Google Admin SDK API](https://console.cloud.google.com/flows/enableapi?apiid=admin.googleapis.com "https://console.cloud.google.com/flows/enableapi?apiid=admin.googleapis.com") on your Google Cloud project. For more
  information, see [Enable
  Google Workspace APIs](https://developers.google.com/workspace/guides/enable-apis "https://developers.google.com/workspace/guides/enable-apis") in the _Google
  Workspace Developer Guide_.

### Rate limit considerations

Google Workspace imposes rate limits on the Google
Workspace API. For more information about Google
Workspace API rate limits, see [Limits and
Quotas](https://developers.google.com/admin-sdk/reports/v1/limits "https://developers.google.com/admin-sdk/reports/v1/limits") on the _Google Workspace Admin
Guide_ on the Google Workspace website. If the
combination of AppFabric and your existing Google Workspace API
applications exceed the limit, audit logs appearing in AppFabric might be
delayed.

### Data delay considerations

You might see up to 30-minute delay for most of audit events and up to 4-hours
delay for certain audit events to be delivered to your destination. This is due to
delay in audit events made available by the application as well as due to
precautions taken to reduce data loss. For more information, see [Data retention and lag
times](https://support.google.com/a/answer/7061566?hl=en "https://support.google.com/a/answer/7061566?hl=en") in the _Google WorkSpace Admin Help website_.
However, this might be customizable at an account-level. For assistance contact
[Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

Google Workspace account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Google Workspace. To find the information required to authorize
Google Workspace with AppFabric, use the following steps.

### Create an OAuth

application

AppFabric integrates with Google Workspace using OAuth. To create an
OAuth application in Google Workspace, use the following
steps:

1. To configure your OAuth consent screen, follow the instructions in [Configure the OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent "https://developers.google.com/workspace/guides/configure-oauth-consent") in the
   _Google Workspace Developer Guide_
   on the Google Workspace website.

Choose **Internal** for the **User
type**. 2. To configure OAuth credentials for AppFabric, follow the instructions in the
[OAuth client ID credentials](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id "https://developers.google.com/workspace/guides/create-credentials#oauth-client-id") section of the _Create access credentials_ page in the
_Google Workspace Developer
Guide_. 3. Use a redirect URL with the following format.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the
code for the AWS Region in which you’ve configured your AppFabric app bundle.
For example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

### Required scopes

You must add the following scopes to your Google Workspace OAuth
application:

- `https://www.googleapis.com/auth/admin.reports.audit.readonly`
- `https://www.googleapis.com/auth/admin.directory.user`

If you don't see these scopes, add the **Admin SDK
API** to your Google Cloud API library.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
Google Workspace project ID. To find your project ID, see
[Locate the project ID](https://support.google.com/googleapi/answer/7014113?hl=en "https://support.google.com/googleapi/answer/7014113?hl=en") on the Google API Console Help
website.

#### Tenant name

Enter a name that identifies this unique Google Workspace.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Client ID

AppFabric will request your client ID. To find your client ID, use the following
steps:

1. Find your client ID using the information in the [View Credentials](https://developers.google.com/workspace/guides/manage-credentials#view_credentials "https://developers.google.com/workspace/guides/manage-credentials#view_credentials") section of the _Manage Credentials_ page in the _Google
   Workspace Developer Guide_.
2. Enter the client ID for your OAuth client into the **Client
   ID** field in AppFabric.

#### Client secret

AppFabric will request your client secret. To find your client secret, use the
following steps:

1. Find your client secret using the information in the [View Credentials](https://developers.google.com/workspace/guides/manage-credentials#view_credentials "https://developers.google.com/workspace/guides/manage-credentials#view_credentials") section of the _Manage Credentials_ page on the _Google
   Workspace Developer Guide_.
2. If you need to reset your client secret, use the instructions in the
   [Reset Client Secret](https://developers.google.com/workspace/guides/manage-credentials#reset_client_secret "https://developers.google.com/workspace/guides/manage-credentials#reset_client_secret") section of the _Manage Credentials_ page on the _Google
   Workspace Developer Guide_.
3. Enter the your client secret into the **Client
   secret** field in AppFabric.

#### Approve

authorization

After creating the app authorization in AppFabric you will receive a pop-up window
from Google Workspace to approve the authorization. To approve
the AppFabric authorization, choose **allow**.
