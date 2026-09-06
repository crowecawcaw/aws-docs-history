

# Configure Zoom for AppFabric
<a name="zoom"></a>

Zoom is an all-in-one intelligent collaboration platform that makes connecting easier, more immersive, and more dynamic for businesses and individuals. Zoom technology puts people at the center, enabling meaningful connections, facilitating modern collaboration, and driving human innovation through solutions like team chat, phone, meetings, omnichannel cloud contact center, smart recordings, whiteboard, and more, in one offering.

You can use AWS AppFabric for security to audit logs and user data from Zoom, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for Zoom](#zoom-appfabric-support)
+ [Connecting AppFabric to your Zoom account](#zoom-appfabric-connecting)

## AppFabric support for Zoom
<a name="zoom-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from Zoom.

### Prerequisites
<a name="zoom-prerequisites"></a>

To use AppFabric to transfer audit logs from Zoom to supported destinations, you must meet the following requirements:
+ You must have a Zoom Pro, Business, Education, or Enterprise plan.
+ Your Zoom **Admin** role must have permission to create server-to-server OAuth applications. For information about enabling server-to-server OAuth applications, see the [Enable permissions](https://developers.zoom.us/docs/internal-apps/s2s-oauth/#enable-permissions) section of the *Server-to-Server OAuth* page in the *Zoom Developers Guide* on the Zoom website.
+ Your Zoom **Admin** role must have permission to view admin activity logs and sign in/sign out audit activity. For more information about enabling permission to view audit activity, see [Using role management](https://support.zoom.us/hc/en-us/articles/115001078646) and [Using Admin Activity Logs](https://support.zoom.us/hc/en-us/articles/360032748331-Using-Admin-Activity-Logs) on the Zoom Support website.

### Rate limit considerations
<a name="zoom-rate-limits"></a>

Zoom imposes rate limits on the Zoom API. For more information about Zoom API rate limits, see [Rate limits](https://developers.zoom.us/docs/api/rest/rate-limits/) in the *Zoom Developers Guide*. If the combination of AppFabric and your existing Zoom applications exceed the limit, audit logs appearing in AppFabric might be delayed.

### Data delay considerations
<a name="zoom-data-delay"></a>

You might see an approximately 24-hour delay for an audit event to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss.

## Connecting AppFabric to your Zoom account
<a name="zoom-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, then you must authorize AppFabric with Zoom. To find the information required to authorize Zoom with AppFabric, use the following steps.

### Create a server-to-server OAuth application
<a name="zoom-create-oauth-application"></a>

AppFabric uses server-to-server OAuth with app credentials to integrate with Zoom. To create a server-to-server OAuth application in Zoom, follow the instructions in [Create a Server-to-Server OAuth app](https://developers.zoom.us/docs/internal-apps/create/) in the *Zoom Developers Guide*. AppFabric does not support Zoom webhooks, and you can skip the section for adding webhook subscriptions.

### Required scopes
<a name="zoom-required-scopes"></a>

 Zoom offers two types of scopes: granular scopes (for newly created applications) and classic scopes (for previously-created applications). 

You must add the following granular scopes to your Zoom server-to-server OAuth application:
+ `report:read:user_activities:admin`
+ `report:read:operation_logs:admin`
+ `user:read:email:admin`
+ `user:read:user:admin`

If you are using a previously-created application, you need to add the following classic scopes:
+ `report:read:admin`
+ `user:read:admin`

### App authorizations
<a name="zoom-app-authorizations"></a>

#### Tenant ID
<a name="zoom-tenant-id"></a>

AppFabric will request your tenant ID. The tenant ID in AppFabric is the Zoom account ID. To find your Zoom account ID, use the following steps:

1. Navigate to the Zoom marketplace.

1. Choose **Manage**.

1. Choose the server-to-server OAuth application that you use for AppFabric.

1. Enter the account ID from the **App Credentials** page into the **Tenant ID** field in AppFabric.

#### Tenant name
<a name="zoom-tenant-name"></a>

Enter a name that identifies this unique Zoom organization. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Client ID
<a name="zoom-client-id"></a>

AppFabric will request your client ID. To find your Zoom client ID, use the following steps:

1. Navigate to the Zoom marketplace.

1. Choose **Manage**.

1. Choose the server-to-server OAuth application that you use for AppFabric.

1. Enter the client ID from the **App Credentials** page into the **Client ID** field in AppFabric.

#### Client secret
<a name="zoom-client-secret"></a>

AppFabric will request your client secret. To find your Zoom client secret, use the following steps:

1. Navigate to the Zoom marketplace.

1. Choose **Manage**.

1. Choose the server-to-server OAuth application that you use for AppFabric.

1. Enter the client secret from the **App Credentials** page into the **Client secret** field in AppFabric.

#### Audit log delivery
<a name="zoom-audit-log-delivery"></a>

Zoom makes audit logs available by accessing the API every 24 hours. When viewing audit logs with AppFabric, the data that you see for Zoom is for the previous day’s activities.