# Configure Okta for AppFabric

Okta is the World’s Identity Company. As the leading independent Identity
partner, Okta frees everyone to safely use any technology—anywhere, on any
device or app. The most trusted brands trust Okta to enable secure access,
authentication, and automation. With flexibility and neutrality at the core of the
Okta Workforce Identity and Customer Identity Clouds, business leaders
and developers can focus on innovation and accelerate digital transformation, thanks to
customizable solutions and more than 7,000 pre-built integrations. Okta is
building a world where Identity belongs to you. Learn more at
okta.com.

You can use AWS AppFabric for security to audit logs and user data from Okta,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Okta](#okta-appfabric-support "#okta-appfabric-support")
- [Connecting AppFabric to your Okta account](#okta-appfabric-connecting "#okta-appfabric-connecting")

## AppFabric support for Okta

AppFabric supports receiving user information and audit logs from
Okta.

### Prerequisites

To use AppFabric to transfer audit logs from Okta to supported
destinations, you must meet the following requirements:

- You can use AppFabric with any Okta plan type.
- You must have a user with the **Super Admin**
  role in your Okta account.
- The user approving the app authorization in AppFabric must also have the
  **Super Admin** role in your
  Okta account.

### Rate limit considerations

Okta imposes rate limits on the Okta API. For more
information about the Okta API rate limits, see [Rate limits](https://developer.okta.com/docs/reference/rate-limits/ "https://developer.okta.com/docs/reference/rate-limits/")
in the _Okta Developer Guide_ on the
Okta website. If the combination of AppFabric and your existing
Okta API applications exceed Okta's limits, audit
logs appearing in AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Okta account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Okta. To find the information required to authorize
Okta with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with Okta using OAuth. To create an OAuth
application to connect with AppFabric, follow the instructions in [Create OIDC app integrations](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm "https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm") on the _Okta Help
Center_ website. Following are configuration considerations for
AppFabric:

1. For **Application Type**, choose **Web
   application**.
2. For **Grant type**, choose **Authorization
   Code** and **Refresh Token**.
3. Use a redirect URL with the following format as the **Sign-in
   redirect URI** and **Sign-out redirect
   URI**.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you’ve configured your AppFabric app bundle. For example,
the code for the US East (N. Virginia) Region is
`us-east-1`. For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 4. You can skip the **Trusted Origins**
configuration. 5. Grant access to everyone in your Okta organization in the
**Controlled access** configuration.

###### Note

If you skip this step during initial OAuth application creation, you
can assign everyone in your organization as a group using the
**Assignments** tab on the application
configuration page. 6. You can leave all other options with their default values.

### Required scopes

You must add the following scopes to your Okta OAuth
application:

- `okta.logs.read`
- `okta.users.read`

### App authorizations

#### Tenant ID

AppFabric will request a tenant ID. The tenant ID in AppFabric is your
Okta domain. For more information about finding your
Okta domain, see [Find
your Okta domain](https://developer.okta.com/docs/guides/find-your-domain/main/ "https://developer.okta.com/docs/guides/find-your-domain/main/") in the _Okta
Developer Guide_ on the Okta website.

#### Tenant name

Enter a name that identifies this unique Okta organization.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Client ID

AppFabric will request a client ID. To find your client ID in Okta,
use the following steps:

1. Navigate to the Okta developer console.
2. Choose the **Applications** tab.
3. Choose your application and then choose the
   **General** tab.
4. Scroll to the **Client Credentials** section.
5. Enter the client ID from your OAuth client into the **Client
   ID** field in AppFabric.

#### Client secret

AppFabric will request a client secret. To find your client secret in
Okta, use the following steps:

1. Navigate to the Okta developer console.
2. Choose the **Applications** tab.
3. Choose your application and then choose the
   **General** tab.
4. Scroll to the **Client Credentials** section.
5. Enter the client secret from your OAuth application into the
   **Client Secret** field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Okta to approve the authorization. To approve the
AppFabric authorization, choose **allow**. The user approving the
Okta authorization must have **Super
Admin** permission in Okta.
