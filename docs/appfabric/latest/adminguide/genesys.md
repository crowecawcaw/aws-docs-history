

# Configure Genesys Cloud for AppFabric
<a name="genesys"></a>

Genesys Cloud creates fluid conversations across digital and voice channels in an easy, all-in-one interface. This positions companies to provide exceptional experiences for employees and customers and reap the benefits of speedy deployments, reduced complexity and simple administration.

You can use AWS AppFabric for security to receive audit logs and user data from Genesys Cloud, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for Genesys Cloud](#genesys-appfabric-support)
+ [Connecting AppFabric to your Genesys Cloud account](#genesys-appfabric-connecting)

## AppFabric support for Genesys Cloud
<a name="genesys-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from Genesys Cloud.

### Prerequisites
<a name="genesys-prerequisites"></a>

To use AppFabric to transfer audit logs from Genesys Cloud to supported destinations, you must meet the following requirements:
+ You must have a Genesys Cloud account.
+ You must have a user with the Administrator role in your Genesys Cloud account.

### Rate limit considerations
<a name="genesys-rate-limit"></a>

Genesys Cloud imposes rate limits on the Genesys Cloud API. For more information about the Genesys Cloud API rate limits, see [Rate limits](https://developer.genesys.cloud/platform/api/rate-limits) on the Genesys Cloud Developer website.

### Data delay considerations
<a name="genesys-data-delay"></a>

You might see up to a 30-minute delay for an audit event to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. However, this might be customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/).

## Connecting AppFabric to your Genesys Cloud account
<a name="genesys-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, you must authorize AppFabric with Genesys Cloud. To find the information required to authorize Genesys Cloud with AppFabric, use the following steps.

### Create an OAuth application
<a name="genesys-create-oauth-application"></a>

AppFabric integrates with Genesys Cloud using OAuth. To create an OAuth application in Genesys Cloud, use the following steps:

1. Follow the instructions in [Create an OAuth Client](https://help.mypurecloud.com/articles/create-an-oauth-client/) on the *Genesys Cloud Resource Center* website.

   For **Grant types**, choose **Code Authorization**.

1. Use a redirect URL with the following format as the **Authorized redirect URIs**.

   ```
   https://{{<region>}}.console.aws.amazon.com/appfabric/oauth2
   ```

   In this URL, {{<region>}} is the code for the AWS Region in which you’ve configured your AppFabric app bundle. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the redirect URL is `https://{{us-east-1}}.console.aws.amazon.com/appfabric/oauth2`.

1. Select the **Scope** box to display a list of scopes available to your app. Select scope `audits:readonly` and `users:readonly`. For information about scopes, see [OAuth Scopes](https://developer.genesys.cloud/api/rest/authorization/scopes.html) in the Genesys Cloud Developer Center.

1. Choose **Save**. Genesys Cloud creates a Client ID and a Client Secret (token).

### Required scopes
<a name="genesys-required-scopes"></a>

You must add the following scopes to your Genesys Cloud OAuth application:
+ `audits:readonly`
+ `users:readonly`

### App authorizations
<a name="genesys-app-authorizations"></a>

#### Tenant ID
<a name="genesys-tenant-id"></a>

AppFabric will request your tenant ID. The tenant ID in AppFabric is your Genesys Cloud instance name. You can find your tenant ID in the address bar of your browser. For example, `usw2.pure.cloud` is the tenant ID in the following URL `https://login.usw2.pure.cloud`.

#### Tenant name
<a name="genesys-tenant-name"></a>

Enter a name that identifies this unique Genesys Cloud organization. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Client ID
<a name="genesys-client-id"></a>

AppFabric will request a client ID. To find your client ID in Genesys Cloud, use the following steps:

1. Choose **Admin**.

1. Under **Integrations**, choose **OAuth**.

1. Choose the OAuth client to get the Client ID.

#### Client secret
<a name="genesys-client-secret"></a>

AppFabric will request a client secret. To find your client secret in Genesys Cloud, use the following steps:

1. Choose **Admin**.

1. Under **Integrations**, choose **OAuth**.

1. Choose the OAuth client to get the Client Secret.