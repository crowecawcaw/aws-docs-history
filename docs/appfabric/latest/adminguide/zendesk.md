# Configure Zendesk for AppFabric

Zendesk started the customer experience revolution in 2007 by enabling any
business around the world to take their customer service online. Today,
Zendesk is the champion of great service everywhere for everyone, and
powers billions of conversations, connecting more than 100,000 brands with hundreds of
millions of customers over telephony, chat, email, messaging, social channels, communities,
review sites, and help centers. Zendesk products are built with love to be
loved. The company was conceived in Copenhagen, Denmark, built and grown in California, and
today employs more than 6,000 people across the world.

You can use AWS AppFabric for security to audit logs and user data from Zendesk,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Zendesk](#zendesk-appfabric-support "#zendesk-appfabric-support")
- [Connecting AppFabric to your Zendesk account](#zendesk-appfabric-connecting "#zendesk-appfabric-connecting")

## AppFabric support for Zendesk

AppFabric supports receiving user information and audit logs from
Zendesk.

### Prerequisites

To use AppFabric to transfer audit logs from Zendesk to supported
destinations, you must meet these requirements:

- You must have a Zendesk Suite Enterprise or Enterprise Plus
  account or a Zendesk Support Enterprise account. For more
  information about creating or upgrading to a Zendesk
  Enterprise account, see [Checking your plan type Zendesk](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan "https://support.zendesk.com/hc/en-us/articles/5411234991258-plan") on the
  Zendesk website.
- You must have a user with the **Administrator** role in your Zendesk account.
  For more information about roles, see [Understanding Zendesk Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles "https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles") on the
  Zendesk website.

### Rate limit considerations

Zendesk imposes rate limits on the Zendesk API. For
more information about the Zendesk API rate limits, see [Rate
limits](https://developer.zendesk.com/api-reference/introduction/rate-limits/ "https://developer.zendesk.com/api-reference/introduction/rate-limits/") in the _Zendesk Developers
Guide_ on the Zendesk website. If the combination of
AppFabric and your existing Zendesk API applications exceed the limit,
audit logs appearing in AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Zendesk account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Zendesk. To find the information required to authorize
Zendesk with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Zendesk using OAuth. In
Zendesk, you must create an OAuth application with the following
settings:

1. Follow the instructions in the [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845965210#topic_s21_lfs_qk "https://support.zendesk.com/hc/en-us/articles/4408845965210#topic_s21_lfs_qk") section of the
   _Using OAuth authentication with your
   application_ article on the Zendesk Support
   website.
2. Use a redirect URL with the following format.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the
code for the AWS Region in which you’ve configured your AppFabric app bundle.
For example, the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`.

### App authorizations

#### Tenant ID

AppFabric will request your Tenant ID. The Tenant ID in AppFabric is your
Zendesk subdomain. For more information about finding your
Zendesk subdomain, see [Where can I find my Zendesk subdomain](https://support.zendesk.com/hc/en-us/articles/4409381383578-Where-can-I-find-my-Zendesk-subdomain- "https://support.zendesk.com/hc/en-us/articles/4409381383578-Where-can-I-find-my-Zendesk-subdomain-") on the
Zendesk Support website.

#### Tenant name

Enter a name that identifies this unique Zendesk organization.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Client ID

AppFabric will request a client ID. The client ID in AppFabric is your
Zendesk API unique identifier. To find your Zendesk unique
identifier, use the following steps:

1. Navigate to the [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410 "https://support.zendesk.com/hc/en-us/articles/4408838272410") in your Zendesk account.
2. Choose **Apps and integrations**.
3. Choose **APIs**, **Zendesk
   APIs**.
4. Choose the **OAuth Clients** tab.
5. Choose the OAuth application that you created for AppFabric.
6. Enter the unique identifier for your OAuth client into the
   **Client ID** field in AppFabric.

#### Client secret

AppFabric will request a client secret. The client secret in AppFabric is your
Zendesk secret token. Zendesk presents your
secret token only once when you first create your Zendesk OAuth
application. To generate a new secret token if you didn't save the initial
secret token, use the following steps:

1. Navigate to the [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410 "https://support.zendesk.com/hc/en-us/articles/4408838272410") in your Zendesk account.
2. Choose **Apps and integrations**.
3. Choose **APIs**, **Zendesk
   APIs**.
4. Choose the **OAuth Clients** tab.
5. Choose the OAuth application that you created for AppFabric.
6. Choose the **Regenerate** button next to the
   **Secret token** field.
7. Enter the new secret token into the **Client secret**
   field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Zendesk to approve the authorization. To approve the
AppFabric authorization, choose **Allow**.
