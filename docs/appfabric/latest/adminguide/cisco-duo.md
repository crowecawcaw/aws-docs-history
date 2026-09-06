

# Configure Cisco Duo for AppFabric
<a name="cisco-duo"></a>

Cisco Duo protects against breaches with a leading access management suite that provides strong multi-layered defenses and innovative capabilities that allow legitimate users in and keep bad actors out. For any organization concerned about being breached and needs a solution fast, Cisco Duo quickly enables strong security while also improving user productivity.

You can use AWS AppFabric for security to receive audit logs and user data from Cisco Duo, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for Cisco Duo](#cisco-duo-appfabric-support)
+ [Connect AppFabric to your Cisco Duo account](#cisco-duo-appfabric-connecting)

## AppFabric support for Cisco Duo
<a name="cisco-duo-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from Cisco Duo.

### Prerequisites
<a name="cisco-duo-prerequisites"></a>

To use AppFabric to transfer audit logs from Cisco Duo to supported destinations, you must meet the following requirements:
+ To access the audit logs, you need to have an active subscription to a Duo Essentials, Duo Advantage, or Duo Premier edition. Alternatively, new customers with an Advantage or Premier trial can also access. For more information about Cisco Duo editions, see [Editions & Pricing](https://duo.com/editions-and-pricing).
+ You need to be an Administrator with Owner role to create or modify Admin API.
+ You need to add Grant read log resource” permissions to access audit logs in the admin API.

### Rate limit considerations
<a name="cisco-duo-rate-limit"></a>

Cisco Duo imposes rate limits on the Cisco Duo API. For more information about the Cisco Duo API rate limits, see the rate limits under [Authentication Logs](https://duo.com/docs/adminapi#authentication-logs). If the combination of AppFabric and your existing Cisco Duo API applications exceed Cisco Duo's limits, audit logs appearing in AppFabric might be delayed. Contact Cisco Duo if you need a rate limit increase.

### Data delay considerations
<a name="cisco-duo-data-delay"></a>

You might see up to a 30-minute delay for an audit event to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. However, this might be customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/).

## Connect AppFabric to your Cisco Duo account
<a name="cisco-duo-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, you must authorize AppFabric with Cisco Duo. To find the information required to authorize Cisco Duo with AppFabric, use the following steps.

### Create a Cisco Duo Admin API application
<a name="cisco-duo-create-application"></a>

AppFabric integrates with Cisco Duo using an API service token. To create an application in Cisco Duo, use the following steps.
+ To create a Cisco Duo Admin API application, follow the instructions in [First steps](https://duo.com/docs/adminapi#first-steps) in the *Cisco Duo Admin API*.

### Required permissions
<a name="cisco-duo-required-scopes"></a>

You must add the following scopes to your Cisco Duo application:
+ Grant read log
+ Grant read resource

### App authorizations
<a name="cisco-duo-app-authorizations"></a>

#### Tenant ID
<a name="cisco-duo-tenant-id"></a>

AppFabric will request a tenant ID. You can find the tenant ID in the Cisco Duo hostname. To find the hostname in Cisco Duo, follow these steps.

1. Navigate to the [Cisco Duo Admin Login](https://admin.duosecurity.com/login?next=%2F) page and sign in.

1. Navigate to **Applications** and then choose **Protect an Application**.

1. Locate the entry for **Admin API** in the applications list, and then choose **Protect** to the far-right to configure your application and get your API hostname.

1. The API hostname is formatted as `api-{{<tenant-id>}}.duosecurity.com`, in which `{{<tenant-id>}}` is the Tenant ID.

#### Tenant name
<a name="cisco-duo-tenant-name"></a>

Enter a name that identifies this unique Cisco Duo organization. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Service token
<a name="cisco-duo-service-token"></a>

AppFabric will request a service token. The service token is a colon-separated integration key and secret key with the following format.

```
{{integrationkey}}:{{secretkey}}
```

To find your integration key and secret key in Cisco Duo, use the following steps.

1. Navigate to the [Cisco Duo Admin Login](https://admin.duosecurity.com/login?next=%2F) page and sign in.

1. Navigate to **Applications** and then choose **Protect an Application**.

1. "Click **Protect an Application** and locate the entry for **Admin API** in the applications list. Click **Protect** at the far-right to configure the application. Scroll down to the scopes section and add **Grant read log** and **Grant read resource**.