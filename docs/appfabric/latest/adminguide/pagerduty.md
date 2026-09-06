

# Configure PagerDuty for AppFabric
<a name="pagerduty"></a>

PagerDuty is a Digital Operations Management Platform that helps teams mitigate customer-impacting issues by turning any signal into action so you can resolve issues faster and operate more efficiently. Integrates with CloudWatch, GuardDuty, CloudTrail, and Personal Health Dashboard.

You can use AWS AppFabric for security to receive audit logs and user data from PagerDuty, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for PagerDuty](#pagerduty-appfabric-support)
+ [Connecting AppFabric to your PagerDuty account](#pagerduty-appfabric-connecting)

## AppFabric support for PagerDuty
<a name="pagerduty-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from PagerDuty.

### Prerequisites
<a name="pagerduty-prerequisites"></a>

To use AppFabric to transfer audit logs from PagerDuty to supported destinations, you must meet the following requirements:
+ To access the audit logs, you must have a PagerDuty **Business** or **Digital Operations** plan.
+ You should be a Global Admin or account owner of the PagerDuty account.

### Rate limit considerations
<a name="pagerduty-rate-limit"></a>

PagerDuty imposes rate limits on the PagerDuty API. For more information about the PagerDuty API rate limits, see [REST API Rate Limits](https://developer.pagerduty.com/docs/72d3b724589e3-rest-api-rate-limits) on the PagerDuty Developer Platform. If the combination of AppFabric and your existing PagerDuty API applications exceed PagerDuty's limits, audit logs appearing in AppFabric might be delayed.

### Data delay considerations
<a name="pagerduty-data-delay"></a>

You might see up to a 30-minute delay for an audit event to be delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. However, this might be customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/).

## Connecting AppFabric to your PagerDuty account
<a name="pagerduty-appfabric-connecting"></a>

The PagerDuty platform supports API access keys. To generate an API access key, use the following steps.

### Create an API Access Key
<a name="pagerduty-create-api-key"></a>

AppFabric integrates with PagerDuty using an API Access key for public clients. To create an API access key in PagerDuty, use the following steps:

1. Navigate to the [PagerDuty log-in page](https://identity.pagerduty.com/global/authn/authentication/PagerDutyGlobalLogin/enter_email) and sign in.

1. Choose **Integrations**, **API Access Keys**.

1. Choose **Create New API Key**.

1. Enter a description and then select **Read-only API Key**.

1. Choose **Create Key**.

1. Copy and save the API key. You'll need this later in AppFabric. If you close the page before saving the API key you must generate a new API key and save it. This key should be dedicated to AppFabric to avoid sharing the PagerDuty API rate limit with your other integrations.

### App authorizations
<a name="pagerduty-app-authorizations"></a>

#### Tenant ID
<a name="pagerduty-tenant-id"></a>

AppFabric will request your tenant ID. The tenant ID for your PagerDuty account is the base URL of your account. You can find this by logging in to PagerDuty and copying from the address bar of your web browser. The tenant ID should follow one of the following formats:
+ For US accounts, `{{subdomain}}.pagerduty.com`
+ For EU accounts, `{{subdomain}}.eu.pagerduty.com`

#### Tenant name
<a name="pagerduty-tenant-name"></a>

Enter a name that identifies this unique PagerDuty organization. AppFabric uses the tenant name to label the app authorizations and any ingestions created from the app authorization.

#### Service account token
<a name="pagerduty-service-token"></a>

AppFabric will request your service account token. The service account token in AppFabric is the API access key you created in [Create an API Access Key](#pagerduty-create-api-key).