# Configure Miro for AppFabric

Miro is an online workspace for innovation that enables distributed teams
of any size to build the next big thing. The platform’s infinite canvas enables teams to
lead engaging workshops and meetings, design products, brainstorm ideas, and more.
Miro, co-headquartered in San Francisco and Amsterdam, serves more than
50M users worldwide, including 99% of the Fortune 100. Miro was founded in
2011 and currently has more than 1,500 employees in 12 hubs around the world. To learn more,
visit [Miro](https://miro.com "https://miro.com").

Miro includes a full suite of collaborative capabilities designed for
innovation including diagramming, wireframing, real-time data visualization, workshop
facilitation, and built-in support for agile practices, workshops, and interactive
presentations. Miro recently announced Miro AI which extends
Miro’s capabilities, with AI-driven mapping and diagramming, clustering
and summarization, and content generation. Miro enables organizations to
reduce the number of standalone tools, reducing information fragmentation and cost.

You can use AWS AppFabric for security to audit logs and user data from Miro,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Miro](#miro-appfabric-support "#miro-appfabric-support")
- [Connecting AppFabric to your Miro
  account](#miro-appfabric-connecting "#miro-appfabric-connecting")

## AppFabric support for Miro

AppFabric supports receiving user information and audit logs from
Miro.

### Prerequisites

To use AppFabric to transfer audit logs from Miro to supported
destinations, you must meet the following requirements:

- You must have a Miro Enterprise Plan. For more information
  about the Miro plan types, see the [Miro pricing](https://miro.com/pricing/ "https://miro.com/pricing/") page on the Miro
  website.
- You must have a user with the Company Admin role in your
  Miro account. For more information about roles, see the
  _Company level_ section of [Roles in Miro](https://help.miro.com/hc/en-us/articles/360017571194-Roles-in-Miro#Company_level "https://help.miro.com/hc/en-us/articles/360017571194-Roles-in-Miro#Company_level") on the Miro Help Center website.
- You must have an Enterprise Developer team in your Miro
  account. For information about creating developer teams, see [Enterprise
  Developer teams](https://help.miro.com/hc/en-us/articles/4766759572114 "https://help.miro.com/hc/en-us/articles/4766759572114") on the Miro Help Center website.

### Rate limit considerations

Miro imposes rate limits on the Miro API. For more
information about the Miro API rate limits, see [Rate Limiting](https://developers.miro.com/docs/rate-limiting "https://developers.miro.com/docs/rate-limiting") in
the _Miro Developers Guide_ on the
Miro website. If the combination of AppFabric and your existing
Miro API applications exceed the limit, audit logs appearing in
AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Miro

account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Miro. To find the information required to authorize
Miro with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Miro using OAuth. To create an OAuth
application in Miro, use the following steps:

1. To create an OAuth application, follow the instructions in the [Creating and installing apps](https://help.miro.com/hc/en-us/articles/4766759572114#Creating_and_installing_apps "https://help.miro.com/hc/en-us/articles/4766759572114#Creating_and_installing_apps") section of the _Enterprise Developer teams_ article on the Miro
   Help Center website.
2. On the app creation dialog, select the **Expire user authorization
   token** check box after you select a developer team on the
   enterprise organization.

###### Note

You must do this _before_ creating
the app because you can't change this option after you create the
app. 3. On the app page, enter a URL with the following format in the
**Redirect URI for OAuth 2.0 section**.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you’ve configured your AppFabric app bundle. For example,
the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 4. Copy and save your client ID and client secret to use in the AppFabric app
authorization.

### Required scopes

You must add the following scopes on the `Permissions` section of your
Miro OAuth app page:

- `auditlogs:read`
- `organizations:read`

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is your
Miro Team ID. For information about how to find your Miro
Team ID, see the _Frequently Asked Questions_
section of [I am a new Miro Admin. Where to start?](https://help.miro.com/hc/en-us/articles/360021841280-I-am-a-new-Miro-Admin-Where-to-start- "https://help.miro.com/hc/en-us/articles/360021841280-I-am-a-new-Miro-Admin-Where-to-start-") on the
_Miro Help Center_ website.

#### Tenant name

Enter a name that identifies this unique Miro organization.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Client ID

AppFabric will request your client ID. To find your client ID, use the following
steps:

1. Navigate to your Miro profile settings.
2. Select the **Your apps** tab.
3. Select the app that you use to connect with AppFabric.
4. Enter the client ID from the **App Credentials**
   section into the **Client ID** field in AppFabric.

#### Client secret

AppFabric will request your client secret. To find your client secret, use the
following steps:

1. Navigate to your Miro profile settings.
2. Select the **Your apps** tab.
3. Select the app that you use to connect with AppFabric.
4. Enter the client secret from the **App Credentials**
   section into the **Client secret** field in
   AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Miro to approve the authorization. To approve the
AppFabric authorization, choose **Allow**.
