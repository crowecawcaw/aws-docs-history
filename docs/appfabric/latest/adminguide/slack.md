# Configure Slack for AppFabric

Slack is on a mission to make people’s working lives simpler, more
pleasant, and more productive. It is the productivity platform for customer companies that
improves performance by empowering everyone with no-code automation, making search and
knowledge sharing seamless, and keeping teams connected and engaged as they move work
forward together. As part of Salesforce, Slack is deeply
integrated into the Salesforce Customer 360, supercharging productivity
across sales, service and marketing teams. To learn more and get started with
Slack for free, visit [slack.com](https://www.slack.com "https://www.slack.com").

You can use AWS AppFabric for security to audit logs and user data from Slack,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Slack](#slack-appfabric-support "#slack-appfabric-support")
- [Connecting AppFabric to your Slack account](#slack-appfabric-connecting "#slack-appfabric-connecting")

## AppFabric support for Slack

AppFabric supports receiving user information and audit logs from
Slack.

### Prerequisites

To use AppFabric to transfer audit logs from Slack to supported
destinations, you must meet the following requirements:

- You must have an Enterprise Grid plan with Slack. For more
  information, see [An
  introduction to Slack Enterprise Grid](https://slack.com/resources/why-use-slack/slack-enterprise-grid "https://slack.com/resources/why-use-slack/slack-enterprise-grid") on the
  Slack website.
- You must have a user with the **Org Owner**
  role in your Slack account. For more information about roles,
  see [Types of roles in Slack](https://slack.com/help/articles/360018112273-Types-of-roles-in-Slack "https://slack.com/help/articles/360018112273-Types-of-roles-in-Slack") in the
  _Slack Help Center_ on the
  Slack website.

### Rate limit considerations

Slack imposes rate limits on the Slack API. For more
information about Slack API rate limits, see [Rate limits](https://api.slack.com/docs/rate-limits "https://api.slack.com/docs/rate-limits") in the
_Slack API Usage Guide_ on the
Slack website. If the combination of AppFabric and your existing
Slack API applications exceed the limit, audit logs appearing in
AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Slack account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Slack. To find the information required to authorize
Slack with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Slack using OAuth. There are two ways to
create an OAuth app: **Using an app manifest** or
**From scratch**. To create an OAuth application in
Slack, use the following steps.

Using an app manifest

1. Navigate to the [Slack App Management UI](https://api.slack.com/apps "https://api.slack.com/apps") in your
   browser.
2. Choose **Create New App**.
3. Choose **From an app manifest**.
4. Choose the workspace for which you want to authorize
   AppFabric.
5. In the **Enter app manifest below** box,
   choose **JSON** and replace the existing JSON
   with the following. Replace
   `<region>` with the
   appropriate AWS Region (for example,
   `us-east-1`).

```
{
    "display_information": {
        "name": "AppFabric"
    },
    "oauth_config": {
        "redirect_urls": [
            "https://`<region>`.console.aws.amazon.com/appfabric/oauth2"
        ],
        "scopes": {
            "user": [
                "auditlogs:read",
                "users:read.email",
                "users:read"
            ]
        }
    },
    "settings": {
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "token_rotation_enabled": true
    }
}
```

6. Copy and save the client ID and client secret from the
   **Basic Information** page.
7. For the `auditLogs:read` scope, you must enable
   public distribution of your app. For more information, see
   [Enabling public distribution](https://api.slack.com/start/distributing/public#enabling "https://api.slack.com/start/distributing/public#enabling") on the Slack
   website.

From scratch

1. Choose **From scratch** on the
   **Create an app** screen.
2. Name your app and choose a workspace.
3. Copy and save the client ID and client secret from the
   **Basic Information** page.
4. On the **OAuth & Permissions** page, opt
   in to the **Advanced token security via token
   rotation** option.
5. Add a URL with the following format in the **Redirect
   URLs** section of the **OAuth &
   Permissions** page.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL,
`<region>` is
the code for the AWS Region in which you’ve configured your
AppFabric app bundle. For example, the code for the
US East (N. Virginia) Region is `us-east-1`.
For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 6. For the `auditLogs:read` scope, you must enable
public distribution of your app. For more information, see
[Enabling public distribution](https://api.slack.com/start/distributing/public#enabling "https://api.slack.com/start/distributing/public#enabling") on the Slack
website.

### Required scopes

###### Note

This section is only applicable if you chose to create the OAuth app from
scratch. Skip this section if you chose to use app manifest to create an
application authorization.

You must add the following user token scopes on the **OAuth &
Permissions** page of your Slack OAuth
application:

- `auditlogs:read`
- `users:read.email`
- `users:read`

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
Slack workspace ID. To get your tenant ID, following the
instructions in [Locate
your Slack URL](https://slack.com/help/articles/221769328-Locate-your-Slack-URL "https://slack.com/help/articles/221769328-Locate-your-Slack-URL") in the _Slack
Help Center_ on the Slack website. Your
Slack workspace URL has a format similar to
`examplecorp.slack.com` or
`examplecorp.enterprise.slack.com`. The tenant ID you need is
`examplecorp` without `.slack.com` or
`.enterprise.slack.com`.

#### Tenant name

Enter a name that identifies your Slack workspace ID. AppFabric
uses the tenant name to label the app authorizations and any ingestions created
from the app authorization

#### Client ID

AppFabric will request the client ID from your Slack OAuth
application. To find the client ID, use the following steps:

1. Navigate to the [Slack App Management UI](https://api.slack.com/apps "https://api.slack.com/apps") in your
   browser.
2. Choose the OAuth application that you use with AppFabric.
3. Enter the client ID from the **Basic Information**
   page into the **Client ID** field in AppFabric.

#### Client secret

AppFabric will request the client secret from your Slack OAuth
application. To find the client secret, use the following steps:

1. Navigate to the [Slack App Management UI](https://api.slack.com/apps "https://api.slack.com/apps") in your
   browser.
2. Choose your the OAuth application that you use with AppFabric.
3. Enter the client secret from the **Basic
   Information** page into the **Client
   secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Slack to approve the authorization. To approve the
AppFabric authorization, choose **allow**.
