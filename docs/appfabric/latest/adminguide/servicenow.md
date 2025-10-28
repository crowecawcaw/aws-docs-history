# Configure ServiceNow for AppFabric

ServiceNow is a leading provider of cloud-based services that automate
enterprise IT operations. ServiceNow’s ITOM gives enterprises complete visibility and
control of their entire IT environment – including virtualized and cloud infrastructure. It
simplifies service mapping, delivery and assurance, consolidating IT service and
infrastructure data into a single system of record. It also automates and streamlines key
processes — including event, incident, problem, configuration and change
management.

You can use AWS AppFabric for security to receive audit logs and user data from
ServiceNow, normalize the data into Open Cybersecurity Schema Framework
(OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose
stream.

###### Topics

- [AppFabric support for
  ServiceNow](#servicenow-appfabric-support "#servicenow-appfabric-support")
- [Data delay considerations](#servicenow-data-delay "#servicenow-data-delay")
- [Connecting AppFabric to your
  ServiceNow account](#servicenow-appfabric-connecting "#servicenow-appfabric-connecting")

## AppFabric support for

ServiceNow

AppFabric supports receiving user information and audit logs from
ServiceNow.

### Prerequisites

To use AppFabric to transfer audit logs from ServiceNow to supported
destinations, you must meet the following requirements:

- You can use AppFabric with any ServiceNow plan type.
- You must have a user with the Administrator role in your
  ServiceNow account.
- You must have a ServiceNow instance.

### Rate limit considerations

ServiceNow imposes rate limits on the ServiceNow
API. For more information about the ServiceNow API rate limits, see
[Inbound REST API rate limiting](https://docs.servicenow.com/bundle/tokyo-api-reference/page/integrate/inbound-rest/concept/inbound-REST-API-rate-limiting.html "https://docs.servicenow.com/bundle/tokyo-api-reference/page/integrate/inbound-rest/concept/inbound-REST-API-rate-limiting.html") on the ServiceNow
website. If the combination of AppFabric and your existing ServiceNow API
applications exceed the limits, audit logs appearing in AppFabric may be delayed.

## Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application as
well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

ServiceNow account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with ServiceNow. Use the following steps to find the information required
to authorize ServiceNow with AppFabric.

### Create an OAuth application

The Now Platform supports OAuth 2.0 - Authorization Grant type for
public clients to generate an access token.

1. Register your OAuth application. This requires the following three steps.
   For more information on completing these steps, see the [Register your application with ServiceNow](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725643 "https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725643") on the
   _ServiceNow website_.
   1. Register the app and make sure the **Auth Scope**
      has access to the **Table API**, with a
      **REST API PATH** of
      **now/table**, and an **HTTP
      Method** of **GET** as shown in the
      following example.

   ![OAuth app configuration in ServiceNow.](images/servicenow-oauth-config.png) 2. Generate an authorization code. 3. Generate a bearer token using the authorization code.

2. Use a redirect URL with the following format.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you configured your AppFabric app bundle. For example, the
code for the US East (N. Virginia) Region is `us-east-1`.
For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

### App authorizations

#### Tenant ID

AppFabric will request a tenant ID. The tenant ID in AppFabric is your instance name.
You can find your tenant ID in the address bar of your browser. For example,
`example` is the tenant ID in the
following URL
`https://`example`.service-now.com`.

#### Tenant name

Enter a name that identifies this unique ServiceNow
organization. AppFabric uses the tenant’s name to label the app authorizations and
any ingestions created from the app authorization.

#### Client ID

AppFabric will request a client ID. Use the following steps to find your client ID
in ServiceNow.

1. Navigate to the ServiceNow console.
2. Choose **System OAuth**, and then choose the
   **Application Registry** tab.
3. Choose your application.
4. Enter the client ID from your OAuth client into the **Client
   ID** field in AppFabric.

#### Client secret

AppFabric will request a client secret. Use the following steps to find your
client secret in ServiceNow.

1. Navigate to the ServiceNow console.
2. Choose **System OAuth**, and then choose the
   **Application Registry** tab.
3. Choose your application.
4. Enter the client secret from your OAuth application into the
   **Client Secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from ServiceNow to approve the authorization. Choose
**Allow** to approve the AppFabric authorization.
