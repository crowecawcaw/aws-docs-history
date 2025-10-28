# Configure HubSpot for AppFabric

HubSpot is a customer platform with all the software, integrations, and
resources you need to connect your marketing, sales, content management, and customer
service. HubSpot's connected platform enables you to grow your business
faster by focusing on what matters most: your customers.

You can use AWS AppFabric for security to receive audit logs and user data from
HubSpot, normalize the data into Open Cybersecurity Schema Framework
(OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose
stream.

###### Topics

- [AppFabric support for
  HubSpot](#hubspot-appfabric-support "#hubspot-appfabric-support")
- [Connecting AppFabric to your
  HubSpot account](#hubspot-appfabric-connecting "#hubspot-appfabric-connecting")

## AppFabric support for

HubSpot

AppFabric supports receiving user information and audit logs from
HubSpot.

### Prerequisites

To use AppFabric to transfer audit logs from HubSpot to supported
destinations, you must meet the following requirements:

- You must have an account with the Enterprise subscription in
  HubSpot to access access audit logs. For more information
  about HubSpot subscriptions, see [Manage your HubSpot subscription](https://knowledge.hubspot.com/account/manage-your-hubspot-subscription "https://knowledge.hubspot.com/account/manage-your-hubspot-subscription") on the
  HubSpot Knowledge Base.
- You must have a developer account and an app associated with the
  account.
- You should be a **super admin** to install
  apps in your HubSpot account or have App Marketplace Access
  permission plus the user permissions to accepts the scopes the app is
  requesting.

### Rate limit considerations

HubSpot imposes rate limits on the HubSpot API. For
more information about the HubSpot API rate limits, including limits
for apps using OAuth, see
[Rate
Limits](https://developers.hubspot.com/docs/api/usage-details#rate-limits "https://developers.hubspot.com/docs/api/usage-details#rate-limits") on the HubSpot website. If the combination of
AppFabric and your existing HubSpot API applications exceed
HubSpot's limits, audit logs appearing in AppFabric might be
delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

HubSpot account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with HubSpot. To find the information required to authorize
HubSpot with AppFabric, use the following steps.

### Create an OAuth

application

AppFabric integrates with HubSpot using OAuth. To create an OAuth
application in HubSpot, use the following steps:

1. Follow the instructions in the [Create a
   public app](https://developers.hubspot.com/docs/api/creating-an-app "https://developers.hubspot.com/docs/api/creating-an-app") section in the HubSpot guide on the
   HubSpot website.
2. From the **Auth** tab, add the three scopes listed in
   [Required scopes](#hubspot-required-scopes "#hubspot-required-scopes").
3. Use a redirect URL with the following format in **Redirect
   URL**.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you’ve configured your AppFabric app bundle. For example,
the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 4. Choose **Create app**.

### Required scopes

You must add the following scopes to your HubSpot OAuth
application:

- `settings.users.read`
- `crm.objects.owners.read`
- `account-info.security.read`

### App authorizations

#### Tenant ID

Enter an ID that identifies this unique HubSpot organization.
For example, enter your HubSpot account ID.

#### Tenant name

Enter a name that identifies this unique HubSpot organization.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Client ID

AppFabric will request a client ID. To find your client ID in
HubSpot, use the following steps:

1. Navigate to the [HubSpot log-in page](https://app.hubspot.com/login "https://app.hubspot.com/login") and sign in using
   your developer account credentials.
2. From the **Apps** menu, choose your app.
3. From the **Auth** tab, look for the **Client
   ID** value.

#### Client secret

AppFabric will request a client secret. To find your client secret in
HubSpot, use the following steps:

1. Navigate to the [HubSpot log-in page](https://app.hubspot.com/login "https://app.hubspot.com/login") and sign in using
   your developer account credentials.
2. From the **Apps** menu, choose your app.
3. From the **Auth** tab, look for the **Client
   secret** value.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from HubSpot to approve the authorization. Sign in to your
account using your enterprise account credentials (not your developer account)
to approve the AppFabric authorization. Choose **allow**.
