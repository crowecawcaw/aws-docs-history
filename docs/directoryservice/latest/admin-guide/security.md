# Security in AWS Directory Service

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet
the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. Third-party auditors regularly test
  and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To
  learn about the compliance programs that apply to AWS Directory Service, see [AWS Services in Scope by
  Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using Directory Service. The following topics show you how to configure Directory Service to meet your security and
  compliance objectives. You also learn how to use other AWS services that help you to monitor
  and secure your Directory Service resources.

**Security topics**

The following security topics can be found in this section:

- [Identity and access management for Directory Service](iam_auth_access.md "iam_auth_access.md")
- [Logging and monitoring in AWS Directory Service](incident-response.md "incident-response.md")
- [Compliance validation for AWS Directory Service](ds-compliance.md "ds-compliance.md")
- [Resilience in AWS Directory Service](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure security in AWS Directory Service](infrastructure-security.md "infrastructure-security.md")
  **Additional security topics**

The following additional security topics can be found in this guide:

_Accounts, trusts, and AWS resource access_

- [AWS Managed Microsoft AD Administrator account and
  group permissions](ms_ad_getting_started_admin_account.md "ms_ad_getting_started_admin_account.md")
- [Group Managed Service Accounts](ms_ad_key_concepts.md#ms_ad_key_concepts_gmsa "ms_ad_key_concepts.md#ms_ad_key_concepts_gmsa")
- [Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](ms_ad_setup_trust.md "ms_ad_setup_trust.md")
- [Kerberos constrained delegation](ms_ad_key_concepts.md#ms_ad_key_concepts_kerberos "ms_ad_key_concepts.md#ms_ad_key_concepts_kerberos")
- [Granting AWS Managed Microsoft AD users and groups access to AWS
  resources with IAM roles](ms_ad_manage_roles.md "ms_ad_manage_roles.md")
- [Authorization for AWS applications and services using Directory Service](ad_manage_apps_services_authorization.md "ad_manage_apps_services_authorization.md")
  _Secure your directory_

- [Secure your AWS Managed Microsoft AD](ms_ad_security.md "ms_ad_security.md")
- [Secure your AD Connector directory](ad_connector_security.md "ad_connector_security.md")
  _Logging and monitoring_

- [Monitor your AWS Managed Microsoft AD](ms_ad_monitor.md "ms_ad_monitor.md")
- [Monitor your AD Connector directory](ad_connector_monitor.md "ad_connector_monitor.md")
  _Resilience_

- [Patching and maintenance for
  AWS Managed Microsoft AD](ms_ad_key_concepts.md#ms_ad_key_concepts_maintenance "ms_ad_key_concepts.md#ms_ad_key_concepts_maintenance")
