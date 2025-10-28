# Configure OneLogin by One Identity for

AppFabric

OneLogin by One Identity is a modern, cloud-based access management
solution that seamlessly manages all digital identities for your workforce, customers and
partners. OneLogin provides secure single sign-on (SSO), multi-factor
authentication (MFA), adaptive authentication, desktop-level MFA, directory integration with
AD, LDAP, G Suite and other external directories, identity lifecycle management and much
more. With OneLogin, you can protect your organization from the most common
attacks, resulting in increased security, frictionless user experiences, and compliance with
regulatory requirements.

You can use AWS AppFabric for security to receive audit logs and user data from
OneLogin, normalize the data into Open Cybersecurity Schema Framework
(OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose
stream.

###### Topics

- [AppFabric support for OneLogin by One
  Identity](#onelogin-appfabric-support "#onelogin-appfabric-support")
- [Connecting AppFabric to your OneLogin
  by One Identity account](#onelogin-appfabric-connecting "#onelogin-appfabric-connecting")

## AppFabric support for OneLogin by One

Identity

AppFabric supports receiving user information and audit logs from OneLogin by One
Identity.

### Prerequisites

To use AppFabric to transfer audit logs from OneLogin by One Identity
to supported destinations, you must meet the following requirements:

- You must have a OneLogin Advanced or Professional
  account.
- You must have a user with the Admin/Delegated Admin Privileges.

### Rate limit considerations

OneLogin by One Identity imposes rate limits on the
OneLogin API. For more information about the
OneLogin API rate limits, see [Get Rate Limit](https://developers.onelogin.com/api-docs/1/oauth20-tokens/get-rate-limit "https://developers.onelogin.com/api-docs/1/oauth20-tokens/get-rate-limit") in the _OneLogin API
Reference_. If the combination of AppFabric and your existing
OneLogin API applications exceed OneLogin's
limits, audit logs appearing in AppFabric might be delayed. However, the
OneLogin rate limit can be increased. For assistance, contact
your OneLogin by One Identity Account Manager or contact [One Identity](https://partners.amazonaws.com/contactpartner?partnerId=001E000000UfZycIAF&partnerName=One%20Identity "https://partners.amazonaws.com/contactpartner?partnerId=001E000000UfZycIAF&partnerName=One%20Identity").

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your OneLogin

by One Identity account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with OneLogin by One Identity. To find the information required to
authorize OneLogin with AppFabric, use the following steps.

### Create an OAuth

application

AppFabric integrates with OneLogin by One Identity using OAuth. To
create an OAuth application in OneLogin, use the following
steps:

1. Navigate to the [OneLogin log-in page](https://app.onelogin.com/login "https://app.onelogin.com/login") and sign in.
2. From the **Developers** menu, choose **API
   Credentials**.
3. Choose **New Credentials**, enter a name for your new
   credential, and then choose **Read all**.
4. Choose **Save**. OneLogin creates a client
   ID and a client secret.

### Required scopes

You must add the following scopes to your OneLogin by One Identity
OAuth application:

- Read all. For more information about scopes and client credentials, see
  [Working with API Credentials](https://developers.onelogin.com/api-docs/1/getting-started/working-with-api-credentials "https://developers.onelogin.com/api-docs/1/getting-started/working-with-api-credentials") in the
  _OneLogin API Reference_.

### App authorizations

#### Tenant ID

AppFabric will request a tenant ID. The tenant ID in AppFabric is your instance
subdomain. You can find your tenant ID in the address bar of your browser. For
example, `subdomain` is the tenant ID in the following URL
`https://`subdomain`.onelogin.com`.

#### Tenant name

Enter a name that identifies this unique OneLogin by One
Identity organization. AppFabric uses the tenant name to label the app
authorizations and any ingestions created from the app authorization.

#### Client ID

AppFabric will request a client ID. To find your client ID in OneLogin by
One Identity, use the following steps:

1. Navigate to the [OneLogin log-in page](https://app.onelogin.com/login "https://app.onelogin.com/login") and sign in.
2. From the **Developers** menu, choose **API
   Credentials**.
3. Choose the API credential to get the Client ID.

#### Client secret

AppFabric will request a client secret. To find your client secret in
OneLogin by One Identity, use the following steps:

1. Navigate to the [OneLogin log-in page](https://app.onelogin.com/login "https://app.onelogin.com/login") and sign in.
2. From the **Developers** menu, choose **API
   Credentials**.
3. Choose the API credential to get the Client Secret.

#### Client app

authorization

In AppFabric, create an app authorization using your tenant ID and name, and your
client ID and name. Choose connect to activate the authorization.
