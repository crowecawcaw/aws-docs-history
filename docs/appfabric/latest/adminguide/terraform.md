# Configure Terraform Cloud for AppFabric

HashiCorp Terraform Cloud is the world’s most widely used multi-cloud
provisioning product. The Terraform ecosystem has more than 3,000 providers,
14,000 modules, and 250 million downloads. Terraform Cloud is the fastest way
to adopt Terraform, providing everything practitioners, teams, and global
businesses need to create and collaborate on infrastructure and manage risks for security,
compliance, and operational constraints.

You can use AWS AppFabric for security to receive audit logs and user data from Terraform
Cloud, normalize the data into Open Cybersecurity Schema Framework (OCSF)
format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Terraform Cloud](#terraform-appfabric-support "#terraform-appfabric-support")
- [Connecting AppFabric to your Terraform Cloud account](#terraform-appfabric-connecting "#terraform-appfabric-connecting")

## AppFabric support for Terraform Cloud

AppFabric supports receiving user information and audit logs from Terraform
Cloud.

### Prerequisites

To use AppFabric to transfer audit logs from Terraform Cloud to
supported destinations, you must meet the following requirements:

- To access the audit logs, you must have a Terraform Cloud
  Plus Edition plan and be the owner of the organization. For more information
  about Terraform Cloud plans, see [Terraform pricing](https://www.hashicorp.com/products/terraform/pricing?ajs_aid=33c212cb-664b-45d6-aee8-d3791e90a893&product_intent=terraform "https://www.hashicorp.com/products/terraform/pricing?ajs_aid=33c212cb-664b-45d6-aee8-d3791e90a893&product_intent=terraform") on the HashiCorp
  Terraform website.
- TBD Audit logs are available for organizations that can be created from
  the Terraform Cloud account.

### Rate limit considerations

Terraform Cloud imposes rate limits on the Terraform
Cloud API. For more information about the Terraform Cloud
API rate limits, see [API Rate Limiting](https://developer.hashicorp.com/terraform/enterprise/application-administration/general#api-rate-limiting "https://developer.hashicorp.com/terraform/enterprise/application-administration/general#api-rate-limiting") in the Terraform Cloud Developer
administration general setting on the Terraform Cloud website. If the
combination of AppFabric and your existing Terraform Cloud API
applications exceed Terraform Cloud's limits, audit logs appearing in
AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Terraform Cloud account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Terraform Cloud. To find the information required to authorize
Terraform Cloud with AppFabric, use the following steps.

### Create an organization API token

AppFabric integrates with Terraform Cloud using an organization API
token. For more information about the Terraform Cloud organization
API tokens, see [Organization API Tokens](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens "https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens"). To create an organization, follow the
instructions in [Creating Organizations](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/organizations#creating-organizations "https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/organizations#creating-organizations"). To create an organization API token in
Terraform Cloud, use the following steps.

1. Navigate to the [Terraform Cloud sign in](https://app.terraform.io/session "https://app.terraform.io/session") page and sign
   in.
2. Choose **Organization**, **Settings** on
   the left-side panel, and then choose **API tokens**.
3. Under **Organization Tokens**, choose **Create an
   organization token** and then choose **Generate
   token**.
4. (Optional) Enter the token's expiration date or time, or create a token
   that never expires.
5. Copy and save the token. You'll need this later in AppFabric. If you close the
   page before saving the token you must revoke the old token and create a new
   one.

### App authorizations

#### Tenant ID

AppFabric will request a tenant ID. The tenant ID for your Terraform
Cloud account is the current organization URL of your account. You
can find this by logging in to your Terraform Cloud organization
and copying the current organization URL. The tenant ID should follow one of the
following formats:

```
https://app.terraform.io/app/`organization_URL`
```

#### Tenant name

Enter a name that identifies this unique Terraform Cloud
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Service account token

AppFabric will request your service account token. The service account token in
AppFabric is the organization API token you created in [Create an organization API token](#terraform-create-org-token "#terraform-create-org-token").
