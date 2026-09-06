

# Configure Google Analytics for AppFabric
<a name="google-analytics"></a>

Google Analytics is a web analytics service that provides statistics and basic analytical tools for search engine optimization (SEO) and marketing purposes. Google Analytics is used to track website performance and collect visitor insights. It can help organizations determine top sources of user traffic, gauge the success of their marketing activities and campaigns, track goal completions (such as purchases, adding products to carts), discover patterns and trends in user engagement and obtain other visitor information such as demographics. Small and medium-sized retail websites often use Google Analytics to obtain and analyze various customer behavior analytics, which can be used to improve marketing campaigns, drive website traffic and better retain visitors.

You can use AWS AppFabric for security to audit logs and user data from Azure Monitor, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for Google Analytics](#google-analytics-appfabric-support)
+ [Connecting AppFabric to your Google Analytics account](#google-analytics-appfabric-connecting)

## AppFabric support for Google Analytics
<a name="google-analytics-appfabric-support"></a>

AppFabric supports receiving audit logs from Google Analytics.

### Prerequisites
<a name="google-analytics-prerequisites"></a>

To use AppFabric to transfer audit logs from Google Analytics to supported destinations, you must meet the following requirements:
+ You must be Administrator of the Google Analytics account.
+ For AppFabric to deliver logs, you need to enable the [Google Analytics Admin API](https://console.cloud.google.com/flows/enableapi?apiid=analyticsadmin.googleapis.com) on your Google Cloud project. Be sure to use a new project when setting up the Google Analytics OAuth application.

### Rate limit considerations
<a name="google-analytics-rate-limits"></a>

Google Analytics imposes rate limits on the Google Analytics API. For more information about Google Analytics API rate limits, see [Limits and Quotas](https://developers.google.com/analytics/devguides/config/admin/v1/quotas) on the *Google Analytics website*. If the combination of AppFabric and your existing *Google Analytics* API applications exceed the limit, audit logs appearing in AppFabric might be delayed.

### Data delay considerations
<a name="google-analytics-data-delay"></a>

You might see up to a 30-minute delay for an audit event to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. However, this might be customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/).

## Connecting AppFabric to your Google Analytics account
<a name="google-analytics-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, you must authorize AppFabric with Google Analytics. Use the following steps to find the information required to authorize Google Analytics with AppFabric.

### Create an OAuth application
<a name="google-analytics-create-oauth-application"></a>

AppFabric integrates with the Google Analytics using OAuth. Complete the following steps to create an OAuth application in Google Analytics:

1. To configure your OAuth consent screen, follow the instructions in Configure the OAuth consent screen in the Google Developer Guide on the Google website.

1. Choose External for the User type

1. To configure OAuth credentials for AppFabric, follow the instructions in the OAuth client ID credentials section of the Create access credentials page in the Google Developer Guide.

1. Use a redirect URL with the following format.

   ```
   https://{{<region>}}.console.aws.amazon.com/appfabric/oauth2
   ```

   In that address, `{{<region>}}` is the code for the AWS Region in which you’ve configured your AppFabric app bundle. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the redirect URL is `https://{{us-east-1}}.console.aws.amazon.com/appfabric/oauth2`.

### Required scopes
<a name="google-analytics-required-scopes"></a>

You must add the following scope to your Google Analytics OAuth application:

```
https://www.googleapis.com/auth/analytics.edit
```

### App authorizations
<a name="google-analytics-app-authorizations"></a>

#### Tenant ID
<a name="google-analytics-tenant-id"></a>

AppFabric will request a tenant ID. The tenant ID in AppFabric is your Google Analytics account ID.

1. Go to the [Google Analytics home page](https://analytics.google.com/analytics/web/).

1. Choose **Admin** in the navigation pane.

1. You will find your account ID under **Account** > **Account Settings** > **Account details** > **Account ID**.

#### Tenant name
<a name="google-analytics-tenant-name"></a>

Enter a name that identifies this unique Google Analytics organization. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Client ID
<a name="google-analytics-client-id"></a>

AppFabric will request a client ID. Use the following steps to find your client ID in Google Analytics:

1. Go to the [Credentials page](https://console.developers.google.com/apis/credentials).

1. In the **OAuth 2.0 Client IDs** section, choose the client ID you created.

1. The client ID is listed in the **Additional information** section of the page.

#### Client secret
<a name="google-analytics-client-secret"></a>

AppFabric will request a client secret. Use the following steps to find your client secret in Google Analytics:

1. Go to the [Credentials page](https://console.developers.google.com/apis/credentials).

1. In the **OAuth 2.0 Client IDs** section, choose the client name.

1. The client secret is listed in the **Client secrets** section of the page.

#### App authorization
<a name="google-analytics-app-authorizing"></a>

After creating the app authorization in AppFabric you will receive a pop-up window from Google Analytics to approve the authorization. To approve the AppFabric authorization by choosing **Allow**.