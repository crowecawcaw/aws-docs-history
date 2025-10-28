# Configure GitHub for AppFabric

GitHub is a platform and cloud-based service for software development and
version control using Git, allowing developers to store and manage their code. It provides
the distributed version control of Git plus access control, bug tracking, software feature
requests, task management, continuous integration, and wikis for every project.

You can use AWS AppFabric for security to receive audit logs and user data from
GitHub, normalize the data into Open Cybersecurity Schema Framework
(OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose
stream.

###### Topics

- [AppFabric support for
  GitHub](#github-appfabric-support "#github-appfabric-support")
- [Connecting AppFabric to your
  GitHub account](#github-appfabric-connecting "#github-appfabric-connecting")

## AppFabric support for

GitHub

AppFabric supports receiving user information and audit logs from
GitHub.

### Prerequisites

To use AppFabric to transfer audit logs from GitHub to supported
destinations, you must meet the following requirements:

- To access the Audit logs you need to have an enterprise account.
- To access the Enterprise audit logs you need to have Administrator role
  for your enterprise account.
- To get audit logs from organization, you need to be Organization
  owner.

### Rate limit considerations

GitHub imposes rate limits on the GitHub API. For
more information about the GitHub API rate limits, see [API Request Limits and Allocations](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/rate-limits-for-github-apps "https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/rate-limits-for-github-apps") on the
_GitHub website_. If the combination of
AppFabric and your existing GitHub API applications exceed
GitHub’s limits, audit logs appearing in AppFabric may be
delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

GitHub account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with GitHub. To find the information required to authorize
GitHub with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with the GitHub using OAuth. Use the following
steps to create an OAuth application in GitHub. For more information,
see [Creating
GitHubs Apps](https://docs.github.com/en/apps/creating-github-apps "https://docs.github.com/en/apps/creating-github-apps") on the _GitHub
website_.

1. Choose your profile photo located in the top-right corner of the page, and
   then choose **Settings**.
2. Choose **Developer settings** in the left navigation
   pane.
3. Choose **OAuth apps** in the left navigation pane.
4. Choose **New OAuth App**.

###### Note

This button will be labeled **Register a new
application** if you haven't previously created an OAuth
app. 5. Enter the name of your app in the **Application name**
text box. 6. Enter the full application instance URL in the **Homepage
URL** text box. 7. (Optional) Enter a description for your app in the **Application
description** text box. Users will see this description. 8. Enter a URL with the following format in the **Authorization
callback URL** text box.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you configured your AppFabric app bundle. For example, the
code for the US East (N. Virginia) Region is `us-east-1`.
For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 9. Choose **Enable Device Flow** if your OAuth app will use
device flow to identify and authorize users. For more information about
device flow, see [Authorizing OAuth apps](https://docs.github.com/en/enterprise-cloud@latest/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow "https://docs.github.com/en/enterprise-cloud@latest/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#device-flow") on the _GitHub
website_. 10. Choose **Register application**.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID should be provided in either
of the following formats:

**Enterprise audit log:**

Use the enterprise's audit log if you want to know aggregated actions from all
of the organizations owned by your enterprise account.

To use the enterprise audit log, the tenant ID is your account's enterprise
ID. You can find your enterprise ID in the address bar of your browser. For
example, `exampleenterprise` is the
enterprise ID in the following URL
`https://github.com/settings/enterprises/`examplenterprise``.

When you specify the tenant ID for enterprise audit log, you must prefix it
with `enterprise:`. Therefore, specify the previous example as
`enterprise:examplenterprise`.

**Organization audit log:**

Use the organization’s audit log as an organization admin if you want to know
the actions performed by members of your organization. It includes details such
as who performed the action, what the action was, and when it was
performed.

To use organization audit log, the tenant ID is your organization ID. You can
find your organization ID in the address bar of your browser. For example,
`exampleorganization` is the
organization ID in the following URL
`https://github.com/settings/organizations/`exampleorganization``.

When you specify the tenant ID for organization audit log, you must prefix it
with `organization:`. Therefore, specify the previous example as
`organization:exampleorganization`.

#### Tenant name

Enter a name that identifies this unique GitHub enterprise or
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Client ID

AppFabric will request a client ID. Use the following steps to find your client ID
in GitHub,

1. Choose your profile photo located in the top-right corner of the page,
   and then choose **Settings**.
2. Choose **Developer settings** in the left navigation
   pane.
3. Choose **OAuth apps** in the left navigation
   pane.
4. Choose the specific OAuth app, and then look for the **Client
   ID** value.

#### Client secret

AppFabric will request a client secret. Use the following steps to find your
client secret in GitHub.

1. Choose your profile photo located in the top-right corner of the page,
   and then choose **Settings**.
2. Choose **Developer settings** in the left navigation
   pane.
3. Choose **OAuth apps** in the left navigation
   pane.
4. Choose the specific OAuth app, and then look for the **Client
   Secret** value. If you are unable to find an existing
   client secret, then you might need to generate a new one.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from GitHub to approve the authorization. To approve the
AppFabric authorization, choose **Allow**.

Make sure that your organizations have [granted access](https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/approving-oauth-apps-for-your-organization "https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/approving-oauth-apps-for-your-organization") to the OAuth app, if [OAuth App access restrictions](https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions "https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions") are enabled.
