# Third-party data sources integration

Integrating CloudWatch pipelines with your third-party data source let you connect external security
tools, identity providers, and monitoring platforms to CloudWatch pipelines for centralized data
analysis. This integration consolidates security events, audit logs, and telemetry data
from multiple sources.

###### Note

Data collected from third-party sources is mutated to adhere to the required
schema when it is collected by CloudWatch pipelines. The original data source is not retained by
CloudWatch.

Third-party data can be collected using two methods:

1. **Direct API Integration** – Some sources
   offer Event Stream APIs where you only need to provide API credentials to
   configure the connector
2. **S3 Bucket Integration** – Data from
   sources can be ingested into a customer-managed S3 bucket for CloudWatch pipelines to
   collect
   The following table identified the integrations methods used by the supported
   third-party data platforms:

| Source                           | Integration pattern | Requires S3 bucket | Requires SQS queue | Uses Secrets Manager extension | Required IAM policies                                                                                                                              |
| -------------------------------- | ------------------- | ------------------ | ------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Akamai DataStream 2              | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Check Point NGFW                 | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Cisco Duo                        | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Cisco Meraki                     | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Cisco Umbrella                   | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| CrowdStrike Falcon               | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Drupal Core                      | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Entrust IDaaS                    | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| F5 BIG-IP                        | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| GitHub                           | API                 | No                 | No                 | Yes (optional)                 | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| GitLab                           | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| HashiCorp Vault                  | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Jamf Protect                     | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Microsoft Entra ID               | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Microsoft Office 365             | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Microsoft Windows Event Logs     | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Netskope                         | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Okta Auth0                       | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Okta SSO                         | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| OneLogin Identity                | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Palo Alto Networks NGFW          | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Palo Alto Prisma Cloud           | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| PingIdentity PingAccess          | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| PingIdentity PingFederate        | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| PingIdentity PingOne             | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Proofpoint TAP                   | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Slack Audit Log                  | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| SentinelOne                      | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| ServiceNow CMDB                  | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Tanium Endpoint Management       | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Tenable Vulnerability Management | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Wiz CNAPP                        | API                 | No                 | No                 | Yes                            | [API caller<br>permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions")                   |
| Zeek                             | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |
| Zscaler ZIA/ZPA                  | S3 Delivery         | Yes                | Yes                | No                             | [Source-specific IAM<br>policies](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") |

Third-party integration sent through Security Hub CSPM is also supported. For
comprehensive information about Security Hub's third-party integrations, including
supported partners and integration configurations with "Sends findings" direction,
refer to the [Security Hub Third-Party Integration documentation](../../../securityhub/latest/userguide/securityhub-partner-providers.md "../../../securityhub/latest/userguide/securityhub-partner-providers.md").

AWS Security Hub (distinct from Security Hub CSPM) also supports third-party
integrations as data sources. For the full list of supported integrations, refer to the
[Security Hub third-party integrations documentation](../../../securityhub/latest/userguide/securityhub-v2-integrations.md "../../../securityhub/latest/userguide/securityhub-v2-integrations.md").

**Data transformation and standardization**

Third-party integrations support data transformation to standardized formats for
consistent analysis:

- **Open Cybersecurity Schema Framework (OCSF)**
  – Converts security events from different vendors into a common schema
  for unified threat detection and analysis. Because OCSF is only for certain
  event classes, not all raw events are mapped to OCSF.
- **Custom transformations** – Pipeline
  processors that normalize data formats, enrich events with additional context,
  and filter relevant information.
- **Field mapping** – Automatic mapping of
  vendor-specific fields to standardized field names for consistent querying and
  analysis.

###### Note

Storing telemetry data from third-party sources in OCSF is an optional feature
that might not be available for all data sources.

**Log group**

Third-party data is ingested into a CloudWatch log group. If you are using the
AWS Management Console to configure CloudWatch pipelines if the log group does not exist, it is created
automatically through the wizard process.

**Authentication and security**

Third-party integrations use secure authentication methods to protect data in
transit:

- **OAuth 2.0 and application registration**
  – Secure token-based authentication for cloud platforms like Microsoft
  and Okta.
- **API keys and certificates** – Encrypted
  authentication credentials for direct API access.
- **IAM roles and policies** – AWS
  Identity and Access Management integration for secure S3 bucket access and
  cross-account data sharing.

###### Note

Data collected from third-party sources is mutated to adhere to the required
schema when it is collected by CloudWatch pipelines. The original data source is not
retained by CloudWatch.

Each integration requires platform-specific configuration to establish secure data
delivery to your AWS environment.

The following sections provide detailed setup procedures for supported third-party
integrations. Each integration includes prerequisites, configuration steps, and
validation procedures to make sure proper data flow.
