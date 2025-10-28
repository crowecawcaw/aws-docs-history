# Configure Webex by Cisco for AppFabric

Cisco is a worldwide leader in technology that powers the Internet.
Cisco inspires new possibilities by reimagining your applications,
securing your data, transforming your infrastructure, and empowering your teams for a global
and inclusive future.

**About Webex by Cisco**

Webex is a leading provider of cloud-based collaboration solutions which
includes video meetings, calling, messaging, events, customer experience solutions like
contact center and purpose-built collaboration devices. Webex’s focus on
delivering inclusive collaboration experiences fuels innovation, which leverages AI and
Machine Learning, to remove the barriers of geography, language, personality, and
familiarity with technology. Its solutions are underpinned with security and privacy by
design. Webex works with the world’s leading business and productivity apps –
delivered through a single application and interface. Learn more at [webex.com](https://webex.com "https://webex.com").

You can use AWS AppFabric for security to audit logs and user data from Webex,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Webex](#webex-appfabric-support "#webex-appfabric-support")
- [Connecting AppFabric to your
  Webex account](#webex-appfabric-connecting "#webex-appfabric-connecting")

## AppFabric support for Webex

AppFabric supports receiving user information and audit logs from
Webex.

### Prerequisites

To use AppFabric to transfer audit logs from Webex to supported
destinations, you must meet the following requirements:

- You must have a Collaboration Flex plan, Meet Plan, Call Plan, or higher.
  For more information about creating or upgrading to the applicable
  Webex plan type, see [Webex pricing for all features](https://pricing.webex.com/us/en/hybrid-work/meetings/all-features/ "https://pricing.webex.com/us/en/hybrid-work/meetings/all-features/") on the
  Webex website.
- Your account must have the [Pro Pack](https://help.webex.com/en-us/article/np3c1rm/Pro-Pack-For-Control-Hub "https://help.webex.com/en-us/article/np3c1rm/Pro-Pack-For-Control-Hub") license to access Security Audit Events provided by
  one of the Cisco AuditLog APIs.
- You must have a user with the **Organizational
  Administrator** > **Full
  Administrator** role.
- The **Administrator Roles** configuration for
  your **Full Administrator** must have the
  **Compliance Officer** option
  enabled.

### Rate limit considerations

Webex imposes rate limits on the Webex API. For more
information about the Webex API rate limits, see [Rate
limits](https://developer.webex.com/docs/basics#upper-limits-for-api-requests "https://developer.webex.com/docs/basics#upper-limits-for-api-requests") in the _Webex Developers
Guide_ on the Webex website. If the combination
of AppFabric and your existing Webex API applications exceed the limit,
audit logs appearing in AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

Webex account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Webex. To find the information required to authorize
Webex with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Webex using OAuth. To create an OAuth
application in Webex, use the following steps:

1. Follow the instructions in the [Registering your Integration](https://developer.webex.com/docs/integrations#registering-your-integration "https://developer.webex.com/docs/integrations#registering-your-integration") section in the
   **Integrations & Authorization** page of the
   _Webex Developers Guide_.
2. Use a redirect URL with the following format.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the
code for the AWS Region in which you’ve configured your AppFabric app bundle.
For example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

### Required scopes

You must add the following scopes to your Webex OAuth
application:

- `spark-compliance:events_read`
- `audit:events_read`
- `spark-admin:people_read`

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
Webex organization ID. For information about how to find your
Webex organization ID, see [Look Up Your Organization ID in CiscoWebex Control Hub](https://help.webex.com/en-us/article/k5pal8/Look-Up-Your-Organization-ID-in-Cisco-Webex-Control-Hub "https://help.webex.com/en-us/article/k5pal8/Look-Up-Your-Organization-ID-in-Cisco-Webex-Control-Hub") on the Webex Help
Center website.

#### Tenant name

Enter a name that identifies this unique Webex instance. AppFabric
uses the tenant name to label the app authorizations and any ingestions created
from the app authorization.

#### Client ID

AppFabric will request your Webex client ID. To find your
Webex client ID, use the following steps:

1. Sign into your Webex account at [https://developer.webex.com](https://developer.webex.com "https://developer.webex.com").
2. Choose your avatar at the top right.
3. Choose **My Webex Apps**.
4. Choose the OAuth2 application that you use for AppFabric.
5. Enter the client ID on this page into the **Client
   ID** field in AppFabric.

#### Client secret

AppFabric will request your Webex client secret.
Webex only presents your client secret once when you
initially create your OAuth application. To generate a new client secret if you
didn't save the initial client secret, use the following steps:

1. Sign into your Webex account at [https://developer.webex.com](https://developer.webex.com "https://developer.webex.com").
2. Choose your avatar at the top right.
3. Choose **My Webex Apps**.
4. Choose the OAuth2 application that you use for AppFabric.
5. On this page, generate a new client secret.
6. Enter the new client secret into the **Client
   secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric you will receive a pop-up window
from Webex to approve the authorization. To approve the AppFabric
authorization, choose **accept**.
