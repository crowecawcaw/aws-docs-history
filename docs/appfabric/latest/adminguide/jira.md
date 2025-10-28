# Configure Atlassian Jira suite for AppFabric

Atlassian unleashes the potential of every team. Their agile and DevOps, IT
service management and work management software helps teams organize, discuss, and complete
shared work. The majority of the Fortune 500 and over 240,000 companies of all sizes
worldwide - including NASA, Kiva, Deutsche Bank, and
Salesforce - rely on Atlassian solutions to help their
teams work better together and deliver quality results on time. Learn more about
Atlassian products, including Jira Software,
Confluence, Jira Service Management,
Trello, Bitbucket, and Jira Align at [Atlassian](https://www.atlassian.com/ "https://www.atlassian.com/").

You can use AWS AppFabric for security to audit logs and user data from the Jira
suite (other than Jira Align), normalize the data into Open
Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3)
bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for the Jira
  suite](#jira-appfabric-support "#jira-appfabric-support")
- [Connecting AppFabric to your Jira
  account](#jira-appfabric-connecting "#jira-appfabric-connecting")

## AppFabric support for the Jira

suite

AppFabric supports receiving user information and audit logs from the Jira
suite, with the exception of Jira Align.

### Prerequisites

To use AppFabric to transfer audit logs from the Jira suite to
supported destinations, you must meet the following requirements:

- You must have a Jira Standard Plan or higher. For more
  information about the capabilities of the Jira plans, see
  [Jira Software](https://www.atlassian.com/software/jira/pricing "https://www.atlassian.com/software/jira/pricing"), [Jira Service Management](https://www.atlassian.com/software/jira/service-management/pricing "https://www.atlassian.com/software/jira/service-management/pricing"), [Jira Work Management](https://www.atlassian.com/software/jira/work-management/pricing "https://www.atlassian.com/software/jira/work-management/pricing"), and [Jira Product Discovery](https://www.atlassian.com/software/jira/product-discovery/pricing "https://www.atlassian.com/software/jira/product-discovery/pricing") pricing pages.
- You must have a user with the **Organization
  admin** role in your Jira account. For more
  information about roles, see [Give users admin permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/ "https://support.atlassian.com/user-management/docs/give-users-admin-permissions/") on the Atlassian
  Support website.

### Rate limit considerations

The Jira suite imposes rate limits on the Jira API.
For more information about the Jira suite API rate limits, see [Rate
limiting](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/ "https://developer.atlassian.com/cloud/jira/platform/rate-limiting/") on the _Atlassian Developers
Guide_ website. If the combination of AppFabric and your existing
Jira API applications exceed the limit, audit logs appearing in
AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Jira

account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Jira. To find the information required to authorize
Jira with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with the Jira suite using OAuth. To create an
OAuth application in Jira, use the following steps:

1. Navigate to the [Atlassian Developer Console](https://developer.atlassian.com/console/ "https://developer.atlassian.com/console/").
2. Next to **My apps**, choose **Create**,
   **OAuth 2.0 integration**.
3. Give your app a name and choose **Create**.
4. Navigate to the **Authorization** section and choose
   **Add** next to OAuth 2.0.
5. Use a URL with the following format in the **Callback
   URL** field and choose **Save**
   changes.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you configured your AppFabric app bundle. For example, the
code for the US East (N. Virginia) Region is `us-east-1`.
For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 6. Navigate to the **Settings** section, copy your client ID
and client secret, and save it to use for the AppFabric app
authorization.

### Required scopes

You must add the following scopes to your Jira OAuth application’s
**Permissions** page:

- Under Classic Scopes:
  - Jira API > `read:jira-user`

- Under Granular Scopes:
  - Jira API > `read:audit-log:jira`
  - Jira API > `read:user:jira`

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
**Jira instance subdomain**. You can
find your **Jira instance subdomain** in your
browser’s address bar between **https://** and
**.atlassian.net**.

#### Tenant name

Enter a name that identifies this unique Jira server. AppFabric
uses the tenant name to label the app authorizations and any ingestions created
from the app authorization.

#### Client ID

AppFabric will request your client ID. To find your client ID in Jira, use the
following steps:

1. Navigate to the [Atlassian Developer Console](https://developer.atlassian.com/console/ "https://developer.atlassian.com/console/").
2. Select the OAuth application that you use to connect AppFabric.
3. Enter the client ID from the **Settings** page into
   the client ID field in AppFabric.

#### Client secret

AppFabric will request your client secret. The **Client secret**
in AppFabric is the **Secret** in Jira. To find your
**Secret** in Jira, use the following
steps:

1. Navigate to the [Atlassian Developer Console](https://developer.atlassian.com/console/ "https://developer.atlassian.com/console/").
2. Select the OAuth application that you use to connect AppFabric.
3. Enter the secret from the **Settings** page into the
   **Client Secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric you will receive a pop-up window
from Jira to approve the authorization. To approve the AppFabric
authorization, choose **Allow**.
