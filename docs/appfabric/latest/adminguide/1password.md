

# Configure 1Password for AppFabric
<a name="1password"></a>

1Password is a password manager that helps you create, store, and use strong passwords for all your online accounts. It also protects your data with encryption, alerts you about breaches, and lets you share passwords.

You can use AWS AppFabric for security to audit logs and user data from 1Password, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for 1Password](#1password-appfabric-support)
+ [Connecting AppFabric to your 1Password account](#1password-appfabric-connecting)

## AppFabric support for 1Password
<a name="1password-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from 1Password.

### Prerequisites
<a name="1password-prerequisites"></a>

To use AppFabric to transfer audit logs from 1Password to supported destinations, you must meet the following requirements:
+ You must have an active paid 1Password Business or Enterprise subscription plan. For more information, see [1Password Enterprise](https://1password.com/business-pricing) on the 1Password website.
+ You must have an administrator role or team owner in the 1Password account. For more information, see [Groups](https://support.1password.com/groups/) in the 1Password support website.

### Rate limit considerations
<a name="1password-rate-limits"></a>

The 1Password AuditLog Events API limits requests to 600 per minute and up to 30,000 per hour. Exceeding these limits returns an error. For more information, see [1Password API Rate limits](https://developer.1password.com/docs/events-api/reference/#rate-limits) in the *1Password Events API reference*.

### Data delay considerations
<a name="1password-data-delay"></a>

You might see up to a 30-minute delay for an audit event to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. However, this might be customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/).

## Connecting AppFabric to your 1Password account
<a name="1password-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, you must authorize AppFabric with 1Password. To find the information required to authorize 1Password with AppFabric, use the following steps.

### Create a personal 1Password access token
<a name="1password-appfabric-access-token"></a>

1Password supports personal access tokens for public clients. Complete the following steps to generate a personal access token.

1. Sign in to your 1Password account.

1. Choose **Integrations** in the navigation pane.

1. If existing integrations are present, choose **Directory**. Otherwise, continue to the next step.

1. Choose **Other** under **Events Reporting Integration**.

1. On the **Add integration** page, enter your security information and event management (SIEM) system name (e.g., AppFabric Secure)

1. Choose **Add Integration**, then complete the following steps in the **Set up token** page.

   1. Provide the token name to be used in the AppFabric secure environment.

   1. We recommend that you choose **Never** in the **Expires After** drop-down list. If any other value is selected then 1Password revokes the token after the expiration time elapses.

   1. In the **Events to Report** section, choose **Sign-in attempts**, **Item usage events**, and **Audit events**.

1. Choose **Issue Token** to create the token.

1. Choose **Save in 1Password** and complete the following steps.

   1. The title will be auto-populated based on your system and token names.

   1. Choose **Private** under **Select A Vault**.

   1. Choose **Save**.

For more information, see [Get started with 1Password Events Reporting](https://support.1password.com/events-reporting/) on the 1Password website.

### App authorizations
<a name="1password-app-authorizations"></a>

#### Tenant ID
<a name="1password-tenant-id"></a>

AppFabric will request your tenant ID. The tenant ID in AppFabric will be your 1Password sign-in address. Complete the following steps to find your tenant ID.

1. Sign in to your 1Password account.

1. Choose **Settings** in the navigation pane.

1. Your 1Password sign-in is listed on the page. For example, **example-account.1password.com**.

#### Tenant name
<a name="1password-tenant-name"></a>

Enter a name that identifies this unique 1Password organization. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Service account token
<a name="1password-service-account-token"></a>

You must have a service account token from an 1Password service account to enter into the AppFabric 1Password app authorization. If you don't have a service account token, use the following instructions:

AppFabric will request a service account token. The service account token in AppFabric is the personal access token you created. Complete the following steps in the **1Password** portal to find the personal access token.

1. Choose **Dashboard**.

1. Choose **People**.

1. Choose **Account Owner Name**.

1. Choose **Private**.

1. Choose **View Vault**.

1. Choose **Token Name**.

#### Client Authorization
<a name="1password-client-authorization"></a>

Create an app authorization in AppFabric using the tenant ID, tenant name and service account token. Then choose **Connect** to activate the authorization.