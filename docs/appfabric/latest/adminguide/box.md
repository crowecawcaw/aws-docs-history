# Configure Box for AppFabric

Box is the leading Content Cloud, a single platform that empowers
organizations to manage the entire content lifecycle, work securely from anywhere, and
integrate across best-of-breed apps.

You can use AWS AppFabric to receive audit logs and user data from Box,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for the Box](#box-appfabric-support "#box-appfabric-support")
- [Connecting AppFabric to your Box
  account](#box-appfabric-connecting "#box-appfabric-connecting")

## AppFabric support for the Box

AppFabric supports receiving user information and audit logs from
Box.

### Prerequisites

To use AppFabric to transfer audit logs from Box to supported
destinations, you must meet the following requirements:

- To access the audit logs, you need to have an active paid subscription to
  [Business, Business Plus,
  Enterprise, or Enterprise Plus](https://www.box.com/pricing "https://www.box.com/pricing") plans.
- You must have a user with the [Admin Privileges](https://developer.box.com/guides/events/enterprise-events/for-enterprise/ "https://developer.box.com/guides/events/enterprise-events/for-enterprise/").
- You must have [2-factor authentication](https://support.box.com/hc/en-us/articles/360043697154-Two-Factor-Authentication-Set-Up-for-Your-Account "https://support.box.com/hc/en-us/articles/360043697154-Two-Factor-Authentication-Set-Up-for-Your-Account") enabled on your Box
  account for viewing and copying the application's client secret from the
  configuration tab.

### Rate limit considerations

Box imposes rate limits on the Box API. For more
information about the Box API [rate limits](https://developer.box.com/guides/api-calls/permissions-and-errors/rate-limits/#per-api-rate-limits "https://developer.box.com/guides/api-calls/permissions-and-errors/rate-limits/#per-api-rate-limits"), see Rate limits on the Box Developers Guide
website. If the combination of AppFabric and your existing Box
applications exceed the limit, audit logs appearing in AppFabric might be
delayed.

### Data delay considerations

You may see up to 30-minute delay in an audit event to get delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this may be
customizable on an account level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Box

account

After you create your app bundle within the AppFabric service, you need to authorize AppFabric
with Box. To find the information required to authorize
Box with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with the Box using OAuth. Use the following steps
to create an OAuth application in Box, For more information, see
[Creating an OAuth App](https://developer.box.com/guides/authentication/client-credentials/client-credentials-setup/ "https://developer.box.com/guides/authentication/client-credentials/client-credentials-setup/") on the Box website.

1. Log in to Box and go to the the [Developer
   Console](https://app.box.com/developers/console "https://app.box.com/developers/console").
2. Choose **Create New App**.
3. Choose **Custom App** from the list of application types.
   A modal will appear to prompt a selection for the next step.
4. Enter an app name and description.
5. Choose **Integration** from the
   **Purpose** dropdown list.
   1. Choose **Security & Compliance** from the
      **Categories** dropdown list.
   2. Enter **AWS AppFabric Secure** in the
      **Which external system are you integrating
      with?** text box.

6. Choose **Server Authentication (Client Credentials
   Grant)** if you would like to verify application identity with
   a client ID and client secret.
7. Choose **Create App**.
8. Choose the **Configuration** tab.
9. In the **App Access Level** section of the page, choose
   **App + Enterprise Access**.
10. In the **Application Scopes** section of the page, Choose
    the **Manage users** and **Manage enterprise
    properties**.
11. Choose **Save Changes**.

A Box Admin needs to authorize the application within the
Box Admin Console before the application can be used.
Complete the following steps to request an authorization.

    1. Choose the **Authorization** tab for your
     application within the [Developer
     Console](https://app.box.com/developers/console "https://app.box.com/developers/console").
    2. Choose **Review and Submit** to send an email to
     your Box enterprise Admin for approval. For more
     information, see [Authorization](https://developer.box.com/guides/authorization/ "https://developer.box.com/guides/authorization/") in the *Box
     guide*.


    ###### Note

    You must re-submit your app if any changes are made after
     submission.

### Required scopes

The following application scopes are required. For more information about scopes,
see [Scopes](https://developer.box.com/guides/api-calls/permissions-and-errors/scopes/ "https://developer.box.com/guides/api-calls/permissions-and-errors/scopes/") on the _Box documentation website_.

- Manage enterprise properties
  (`manage_enterprise_properties`)
- Manage users (`manage_managed_users`)

### App authorizations

#### Tenant ID

AppFabric will request a tenant ID. The tenant ID in AppFabric is the
Box Enterprise ID. The Box Enterprise ID can
be found in the admin console under **Account & Billing**

> **Account Information** > **Enterprise
> ID**. For more information, see [Enterprise ID](https://developer.box.com/platform/appendix/locating-values/#as-an-admin "https://developer.box.com/platform/appendix/locating-values/#as-an-admin") on the _Box documentation
> website_.

#### Tenant name

Enter a name that identifies this unique Box organization.
AppFabric uses the tenant name to label the app authorizations and any ingestion
created from the app authorization.

#### Client ID and client

secret

1. Log in to Box and go to the [Developer
   Console](https://app.box.com/developers/console "https://app.box.com/developers/console").
2. Choose **My Apps** in the navigation menu.
3. Choose the OAuth application that you use to connect AppFabric.
4. Choose the **Configuration** tab.
5. Scroll to the **Oauth 2.0 Credentials** section of
   the page.
6. Enter the client ID from your OAuth **Client Id**
   into the **Client ID** field in AppFabric.
7. Choose **Fetch Client Secret**.
8. Enter the client secret from your OAuth Client Secret into the
   **Client Secret** field in AppFabric.
