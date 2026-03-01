# Configure Dropbox for AppFabric

Dropbox helps your organization get better work done faster by bringing
your people together - no matter what they’re working on, where they’re working, or what
kind of tools they happen to be using. It enables users to accelerate innovation and
efficiency by providing a simple, secure way to share content. Dropbox is one
place to keep life organized and keep work moving. With more than 700 million registered
users across 180 countries, Dropbox is on a mission to design a more
enlightened way of working.

You can use AWS AppFabric for security to audit logs and user data from Dropbox,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Dropbox](#dropbox-appfabric-support "#dropbox-appfabric-support")
- [Connecting AppFabric to your Dropbox account](#dropbox-appfabric-connecting "#dropbox-appfabric-connecting")

## AppFabric support for Dropbox

AppFabric supports receiving user information and audit logs from
Dropbox.

### Prerequisites

To use AppFabric to transfer audit logs from Dropbox to supported
destinations, you must meet the following requirements:

- You must have a Dropbox Business account. For more
  information about creating or upgrading to a Dropbox Business
  account, see [Dropbox Business](https://www.dropbox.com/business "https://www.dropbox.com/business") on the
  Dropbox website.
- You must have a user with the Team Admin role in your
  Dropbox account. For more information about roles, see
  [How
  to change admin rights for your Dropbox team](https://help.dropbox.com/security/change-admin-rights "https://help.dropbox.com/security/change-admin-rights") on
  the _Dropbox Help Center_ website.

### Rate limit considerations

Dropbox imposes rate limits on the Dropbox API. For
more information about the Dropbox API rate limits, see [Rate
limits](https://developers.dropbox.com/dbx-performance-guide#api-rate-limits "https://developers.dropbox.com/dbx-performance-guide#api-rate-limits") on the _Dropbox Performance
Guide_ website. If the combination of AppFabric and your existing
Dropbox API applications exceed the limit, audit logs appearing
in AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Dropbox account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Dropbox. To find the information required to authorize
Dropbox with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Dropbox using OAuth. To create an OAuth
application in Dropbox, use the following steps:

1. Choose **Create app** in the Dropbox App
   Console at [https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps "https://www.dropbox.com/developers/apps").
2. On the new application configuration page, choose **Scoped
   access** for the API.
3. Next, select **Full Dropbox** for the type
   of access.
4. Name your OAuth application, and then chose **Create
   app** to complete the initial OAuth application setup.
5. On the application info page, add a redirect URL with the following format
   in the OAuth2 redirect URIs field.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the
code for the AWS Region in which you configured your AppFabric app bundle. For
example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 6. Choose **Add**. 7. Copy and save your app key and app secret for use in the AppFabric app
authorization. 8. You can leave all other fields on the **Settings** tab
with their default values.

### Required scopes

You must add the following scopes to your Dropbox app using the
**Permissions** tab on the app info screen:

- `account_info.read`
- `team_data.member`
- `events.read`
- `members.read`
- `team_info.read`

Choose **Submit** after you are done.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. Enter any value that uniquely identifies
your Dropbox account, such as team name.

#### Tenant name

Enter a name that identifies this unique Dropbox account. AppFabric
uses the tenant name to label the app authorizations and any ingestions created
from the app authorization.

#### Client ID

AppFabric will request a client ID. The client ID in AppFabric is your
Dropbox app key. To find your Dropbox app key, use the
following steps:

1. Navigate to the Dropbox App Console at [https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps "https://www.dropbox.com/developers/apps").
2. Find the app that you use to connect AppFabric.
3. Find the app key in the **Status** section of the
   app’s info page.
4. Enter the app key for your Dropbox app into the
   **Client ID** field in AppFabric.

#### Client secret

AppFabric will request a client secret. The client secret in AppFabric is your
Dropbox app secret. To find your Dropbox app
secret, use the following steps:

1. Navigate to the Dropbox App Console at [https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps "https://www.dropbox.com/developers/apps").
2. Find the app that you use to connect AppFabric.
3. Find the app secret in the **Status** section of the
   app’s info page.
4. Enter the app secret for your Dropbox app into the
   **Client Secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Dropbox to approve the authorization. To approve the
AppFabric authorization, choose **Allow**.
