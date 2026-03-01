# Configure Smartsheet for AppFabric

Smartsheet is a work management platform that helps you align work, people,
and technology across your enterprise. Smartsheet offers a robust set of
enterprise-grade capabilities to empower everyone to manage projects, automate workflows,
and rapidly build solutions at scale, creating an environment for innovation while
maintaining security and compliance.

You can use AWS AppFabric for security to audit logs and user data from Smartsheet,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Smartsheet](#smartsheet-appfabric-support "#smartsheet-appfabric-support")
- [Connecting AppFabric to your Smartsheet account](#smartsheet-appfabric-connecting "#smartsheet-appfabric-connecting")

## AppFabric support for Smartsheet

AppFabric supports receiving user information and audit logs from
Smartsheet.

### Prerequisites

To use AppFabric to transfer audit logs from Smartsheet to supported
destinations, you must meet the following requirements:

- You must have a Smartsheet Business, Enterprise, or Advance
  account. For more information about creating or upgrading your
  Smartsheet account, see either [Smartsheet
  pricing](https://www.smartsheet.com/pricing "https://www.smartsheet.com/pricing") or [Smartsheet Advance](https://www.smartsheet.com/pricing/smartsheet-advance "https://www.smartsheet.com/pricing/smartsheet-advance") on the
  Smartsheet website.
- You must complete the [Smartsheet developer registration](https://developers.smartsheet.com/register/ "https://developers.smartsheet.com/register/")
  process.

### Rate limit considerations

Smartsheet imposes rate limits on the Smartsheet
API. For more information about the Smartsheet API rate limits, see
[Rate limiting](https://smartsheet.redoc.ly/#section/Work-at-Scale/Rate-Limiting "https://smartsheet.redoc.ly/#section/Work-at-Scale/Rate-Limiting") in the _Smartsheet API Reference on the
Smartsheet website_.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Smartsheet account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Smartsheet. To find the information required to authorize
Smartsheet with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Smartsheet using OAuth. To create an OAuth
application in Smartsheet, use the following steps:

1. Navigate to the developer tools in your Smartsheet
   account.
2. Choose **Create New App** from the developer tools
   screen.
3. Complete all of the input fields on the **Create New
   App** screen.
4. Use any unique value for **App URL** and **App
   Contact/support**.
5. Use a redirect URL with the following format as the App redirect
   URL.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the
code for the AWS Region in which you’ve configured your AppFabric app bundle.
For example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 6. Choose **Save**. 7. Copy and save the app client ID and app secret.

### Required scopes

Smartsheet does not require you to explicitly add scopes to your
OAuth configuration. AppFabric will request the following scopes in the authorization
request to your Smartsheet account:

- `READ_EVENTS`
- `READ_USERS`

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
Smartsheet account ID.

#### Tenant name

AppFabric will request your tenant ID. Enter any value that uniquely identifies
your Smartsheet account.

#### Client ID

AppFabric will request your client ID. The client ID in AppFabric is your
Smartsheet app client ID. To find your app client ID in
Smartsheet, use the following steps:

1. Navigate to the developer tools in your Smartsheet
   account.
2. Select the OAuth application that you use to connect with
   AppFabric.
3. Enter the app client ID from the **App Profile**
   screen into the **Client ID** field in AppFabric.

#### Client secret

AppFabric will request your client secret. The client secret in AppFabric is your
Smartsheet app secret. To find your app secret in
Smartsheet, use the following steps:

1. Navigate to the developer tools in your Smartsheet
   account.
2. Select the OAuth application that you use to connect with
   AppFabric.
3. Enter the app secret from the **App Profile** screen
   into **Client Secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Smartsheet to approve the authorization. To approve
the AppFabric authorization, choose **Allow**.
