# AWS Private CA Connector for Active Directory

AWS Private CA can issue and manage certificates required by AWS Managed Microsoft AD. Using the AWS Private CA
Connector for Active Directory (Connector for AD), you can replace
on-premises enterprise or other third-party CAs with a managed private CA that you own,
providing certificate enrollment to users, groups, and machines that are managed by your
AD.

You can use the Connector for AD with AWS Managed Microsoft AD to eliminate on-premises
infrastructure by migrating your AD and public key infrastructure to the cloud. For
customers looking to use AWS Private CA with their on-premises AD, this feature also integrates
with AWS Managed Microsoft AD Connector.

###### Topics

- [Are You a First-Time Connector for AD
  User?](#first-time-user "#first-time-user")
- [Set up Connector for AD](connector-for-ad-getting-started-prerequisites.md "connector-for-ad-getting-started-prerequisites.md")
- [Get started with
  AWS Private CA Connector for Active Directory](connector-for-ad-getting-started.md "connector-for-ad-getting-started.md")
- [AWS Private CA connectors for Active Directory](connector-for-ad-procedures.md "connector-for-ad-procedures.md")
- [Integrating Connector for AD into
  event-driven applications using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md")
- [Troubleshoot issues with AWS Private CA Connector for Active Directory](troubleshoot-connector-ad.md "troubleshoot-connector-ad.md")

## Are You a First-Time Connector for AD

User?

If you are a first-time user of Connector for AD, we recommend that you
begin by reading the following sections:

- [What is AWS Private CA?](PcaWelcome.md "PcaWelcome.md")
- [What is
  AWS Directory Service?](../../../directoryservice/latest/admin-guide/what_is.md "../../../directoryservice/latest/admin-guide/what_is.md")

### Access

Connector for AD

You can access Connector for AD through the console, AWS CLI, and APIs. You can get access to the connector in the
console from the AWS Private CA console, from your AWS Directory Service console, or by searching for
Connector for AD in the AWS Management Console search bar.

### Pricing

Connector for AD is offered as a feature of AWS Private CA at no additional
cost. You only pay for the private certificate authorities and the certificates you
issue through them.

For the latest AWS Private CA pricing information, see [AWS Private Certificate Authority Pricing](https://aws.amazon.com/private-ca/pricing/ "https://aws.amazon.com/private-ca/pricing/"). You can also use the [AWS pricing
calculator](https://calculator.aws/#/createCalculator/certificateManager "https://calculator.aws/#/createCalculator/certificateManager") to estimate costs.
