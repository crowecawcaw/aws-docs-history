# Configure Atlassian Confluence for AppFabric

Create, collaborate, and organize all your work in one place. Confluence is
a team workspace where knowledge and collaboration meet. Dynamic pages give your team a
place to create, capture, and collaborate on any project or idea. Spaces help your team
structure, organize, and share work, so every team member has visibility into institutional
knowledge and access to the information they need to do their best work.

You can use AWS AppFabric for security to receive audit logs and user data from
Confluence, normalize the data into Open Cybersecurity Schema Framework
(OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose
stream.

###### Topics

- [AppFabric support for Atlassian
  Confluence](#confluence-appfabric-support "#confluence-appfabric-support")
- [Connecting AppFabric to your
  Atlassian Confluence account](#confluence-appfabric-connecting "#confluence-appfabric-connecting")

## AppFabric support for Atlassian

Confluence

AppFabric supports receiving audit logs from Atlassian Confluence.

### Prerequisites

To use AppFabric to transfer audit logs from Atlassian Confluence to
supported destinations, you must meet the following requirements:

- To access the Audit logs, you need to have an standard, premium, or
  enterprise account. For more information about creating or upgrading to the
  applicable Confluence plan type, see [Confluence Pricing](https://www.atlassian.com/software/confluence/pricing.html "https://www.atlassian.com/software/confluence/pricing.html") on the
  Atlassian website.
- To access the Audit logs, you need to have Administrator permissions for
  your account. For more information about roles, see [Give users admin permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/ "https://support.atlassian.com/user-management/docs/give-users-admin-permissions/") on the Atlassian
  Support website.

### Rate limit considerations

Confluence imposes rate limits on the Atlassian
Confluence API. If the combination of AppFabric and your existing
Atlassian Confluence API applications exceed Atlassian
Confluence's limits, audit logs appearing in AppFabric might be
delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

Atlassian Confluence account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Atlassian Confluence. To find the information required to authorize
Atlassian Confluence with AppFabric, use the following steps.

### Create an OAuth

application

AppFabric integrates with Atlassian Confluence using OAuth. To create
an OAuth application in Atlassian Confluence, use the following
steps.

1. Navigate to the [Atlassian Developer Console](https://developer.atlassian.com/console/ "https://developer.atlassian.com/console/").
2. Choose your profile icon in the top-right and choose **Developer
   console**.
3. Next to **My apps**, choose **Create**,
   **OAuth 2.0 integration**.
4. Choose **Permissions** in the left navigation pane and
   choose **Add** next to Confluence
   API.
5. Under **Classic scopes**, select **Read
   user** (`read:confluence-user`).
6. Under **Granular scopes**, select **View audit
   records** (`read:audit-log:confluence`).
7. Choose **Authorization** in the left navigation pane and
   choose **Add** next to **OAuth 2.0
   (3LO)**.
8. Use a redirect URL with the following format in the **Callback
   URL** text box and choose **Save
   changes**.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you’ve configured your AppFabric app bundle. For example,
the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

### Required scopes

You must add one of the following scopes to your Atlassian
Confluence OAuth application. For more information about scopes, see
[Scopes for OAuth 2.0 (3LO) and Forge apps](https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/ "https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/") on the
Atlassian Developer website. Use the classic scope where
available.

- Classic Scopes:
  - `read:confluence-user`

- Granular Scopes:
  - `read:audit-log:confluence`

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
**Atlassian Confluence instance
subdomain**. You can find your **Atlassian
Confluence instance subdomain** in your browser’s
address bar between **https://** and
**.atlassian.net**.

#### Tenant name

Enter a name that identifies this unique Atlassian Confluence
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Client ID

AppFabric will request a client ID. To find your client ID in Atlassian
Confluence, use the following steps:

1. Navigate to the [Atlassian Developer Console](https://developer.atlassian.com/console/ "https://developer.atlassian.com/console/").
2. Choose your profile icon in the top-right and choose
   **Developer console**, **My
   Apps**.
3. Select the OAuth application that you use to connect AppFabric.
4. Enter the client ID from the **Settings** page into
   the client ID field in AppFabric.

#### Client secret

AppFabric will request a client secret. To find your client secret in
Atlassian Confluence, use the following steps:

1. Navigate to the [Atlassian Developer Console](https://developer.atlassian.com/console/ "https://developer.atlassian.com/console/").
2. Choose your profile icon in the top-right and choose
   **Developer console**, **My
   Apps**.
3. Select the OAuth application that you use to connect AppFabric.
4. Enter the secret from the **Settings** page into the
   **Client Secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Atlassian Confluence to approve the authorization. To
approve the AppFabric authorization, choose **allow**.
