# Configure Ping Identity for AppFabric

At Ping Identity, we believe in making digital experiences both secure and
seamless for all users, without compromise. That's why more than half of the Fortune 100
choose Ping Identity to protect digital interactions for their users while
making experiences frictionless. On August 23, 2023, Ping Identity and
ForgeRock joined together to deliver more choice, deeper expertise, and a
more complete identity solution for customers and partners.

You can use AWS AppFabric for security to receive audit logs and user data from Ping
Identity, normalize the data into Open Cybersecurity Schema Framework (OCSF)
format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Ping Identity](#pingidentity-appfabric-support "#pingidentity-appfabric-support")
- [Connecting AppFabric to your Ping Identity account](#pingidentity-appfabric-connecting "#pingidentity-appfabric-connecting")

## AppFabric support for Ping Identity

AppFabric supports receiving user information and audit logs from Ping
Identity.

### Prerequisites

To use AppFabric to transfer audit logs from Ping Identity to supported
destinations, you must meet the following requirements:

- You must have an Essential, Plus, or Premium Ping Identity
  account. For more information about creating or upgrading to the applicable
  Ping Identity plan type, see [Ping
  Identity pricing for all features](https://www.pingidentity.com/en/platform/pricing.html "https://www.pingidentity.com/en/platform/pricing.html") on the Ping
  Identity website.
- You must have **Identity Data Read Only**
  role in your Ping Identity account. You can add roles to your
  account by granting roles for your application. For more information about
  roles, see [Roles](https://docs.pingidentity.com/r/en-us/pingone/p1_c_roles "https://docs.pingidentity.com/r/en-us/pingone/p1_c_roles") on the Ping Identity Support
  website.

### Rate limit considerations

Ping Identity doesn't publish rate limits. You must create a
support case or reach out to your Ping Identity Customer Success
team. If the combination of AppFabric and your existing Ping Identity API
applications exceed Ping Identity's limits, audit logs appearing in
AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Ping Identity account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Ping Identity. To find the information required to authorize
Ping Identity with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Ping Identity using OAuth. To create an OAuth
application in Ping Identity, use the following steps:

1. Follow the instructions in the [Create an application connection](https://apidocs.pingidentity.com/pingone/main/v1/api/#create-an-application-connection "https://apidocs.pingidentity.com/pingone/main/v1/api/#create-an-application-connection") section in the
   _PingOne for Developers_ guide on
   the Ping Identity website.
2. After you create the application, customize the grant types.
   1. When signed in to the application, choose the
      **Configuration** tab and click the pencil icon
      to make changes in the existing configuration.
   2. Under **Grant Type**, select
      **Authorization Code**. Keep **PKCE
      Enforcement** as **OPTIONAL**.
   3. Select **Refresh Token** and choose your refresh
      durations.

3. Use a redirect URL with the following format in **Redirect
   URL/callback URL**.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you’ve configured your AppFabric app bundle. For example,
the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your Ping
Identity instance name. You can find your tenant ID in the address
bar of your browser. For example,
``API_PATH`/v1/environments/`environmentID``.
Where `API_PATH` represents the regional
domain for the PingOne server, such as
`api.pingone.com`, and
`environmentID` represents your
environment ID indicated in your application environment properties. For more
information about environment properties, see [Environment Properties](https://docs.pingidentity.com/r/en-us/pingone/p1_c_environments "https://docs.pingidentity.com/r/en-us/pingone/p1_c_environments") on the Ping Identity
website.

#### Tenant name

Enter a name that identifies this unique Ping Identity
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Client ID

AppFabric will request a client ID. To find your client ID in Ping
Identity, use the following steps:

1. Sign in to PingOne admin console and choose
   **Applications**.
2. Choose the application from the list.
3. Choose the **Overview** tab, and then look for the
   **Client ID** value.

#### Client secret

AppFabric will request a client secret. To find your client secret in Ping
Identity, use the following steps:

1. Sign in to PingOne admin console and choose
   **Applications**.
2. Choose the application from the list.
3. Choose the **Overview** tab, and then look for the
   **Client Secret** value.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Ping Identity to approve the authorization. To
approve the AppFabric authorization, choose **allow**.
