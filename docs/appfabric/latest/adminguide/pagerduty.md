# Configure PagerDuty for AppFabric

PagerDuty is a Digital Operations Management Platform that helps teams
mitigate customer-impacting issues by turning any signal into action so you can resolve
issues faster and operate more efficiently. Integrates with CloudWatch,
GuardDuty, CloudTrail, and Personal Health
Dashboard.

You can use AWS AppFabric for security to receive audit logs and user data from
PagerDuty, normalize the data into Open Cybersecurity Schema Framework
(OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose
stream.

###### Topics

- [AppFabric support for PagerDuty](#pagerduty-appfabric-support "#pagerduty-appfabric-support")
- [Connecting AppFabric to your PagerDuty account](#pagerduty-appfabric-connecting "#pagerduty-appfabric-connecting")

## AppFabric support for PagerDuty

AppFabric supports receiving user information and audit logs from
PagerDuty.

### Prerequisites

To use AppFabric to transfer audit logs from PagerDuty to supported
destinations, you must meet the following requirements:

- To access the audit logs, you must have a PagerDuty
  **Business** or **Digital
  Operations** plan.
- You should be a Global Admin or account owner of the
  PagerDuty account.

### Rate limit considerations

PagerDuty imposes rate limits on the PagerDuty API.
For more information about the PagerDuty API rate limits, see [REST API Rate Limits](https://developer.pagerduty.com/docs/72d3b724589e3-rest-api-rate-limits "https://developer.pagerduty.com/docs/72d3b724589e3-rest-api-rate-limits") on the PagerDuty Developer
Platform. If the combination of AppFabric and your existing PagerDuty API
applications exceed PagerDuty's limits, audit logs appearing in AppFabric
might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your PagerDuty account

The PagerDuty platform supports API access keys. To generate an API
access key, use the following steps.

### Create an API Access Key

AppFabric integrates with PagerDuty using an API Access key for public
clients. To create an API access key in PagerDuty, use the following
steps:

1. Navigate to the [PagerDuty log-in page](https://identity.pagerduty.com/global/authn/authentication/PagerDutyGlobalLogin/enter_email "https://identity.pagerduty.com/global/authn/authentication/PagerDutyGlobalLogin/enter_email") and sign in.
2. Choose **Integrations**, **API Access
   Keys**.
3. Choose **Create New API Key**.
4. Enter a description and then select **Read-only API
   Key**.
5. Choose **Create Key**.
6. Copy and save the API key. You'll need this later in AppFabric. If you close
   the page before saving the API key you must generate a new API key and save
   it. This key should be dedicated to AppFabric to avoid sharing the
   PagerDuty API rate limit with your other
   integrations.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID for your
PagerDuty account is the base URL of your account. You can
find this by logging in to PagerDuty and copying from the address
bar of your web browser. The tenant ID should follow one of the following
formats:

- For US accounts,
  ``subdomain`.pagerduty.com`
- For EU accounts,
  ``subdomain`.eu.pagerduty.com`

#### Tenant name

Enter a name that identifies this unique PagerDuty
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Service account token

AppFabric will request your service account token. The service account token in
AppFabric is the API access key you created in [Create an API Access Key](#pagerduty-create-api-key "#pagerduty-create-api-key").
