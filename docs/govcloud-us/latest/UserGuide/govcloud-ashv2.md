# AWS Security Hub in AWS GovCloud (US)

AWS Security Hub is a unified cloud security solution that prioritizes your critical security issues and helps you respond at scale. Security Hub detects security issues by automatically correlating and enriching security signals from multiple sources, such as posture management (AWS Security Hub CSPM), vulnerability management (Amazon Inspector), sensitive data (AWS Macie), and threat detection (Amazon GuardDuty). This enables security teams to prioritize active risks in their cloud environments through automated analyses and contextual insights. Through intuitive visualizations, Security Hub transforms complex security signals into actionable insights, which enables you to make informed decisions about your security quickly. Security Hub also includes automated response workflows to help you remediate risks, improve team productivity, and minimize operational disruptions.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Security Hub differs

The following differences apply to Security Hub:

**Integrations**

Integrations with third-party products are not available in the AWS GovCloud (US) Region. For more information about integrations in other AWS Regions, see [Integrations with AWS services and third-party products](../../../securityhub/latest/userguide/securityhub-v2-integrations.md "../../../securityhub/latest/userguide/securityhub-v2-integrations.md") in the _AWS Security Hub User Guide_.

**Automation Rules**

Automation rules for integrations are not available in the AWS GovCloud (US) Region. Automation rules allow you to automatically update finding fields based on specified criteria. For more information about automation rules in other AWS Regions, see [Automating response and remediation](../../../securityhub/latest/userguide/securityhub-v2-automation-rules.md "../../../securityhub/latest/userguide/securityhub-v2-automation-rules.md") in the _Security Hub User Guide_.

**Cost Estimator**

The Security Hub cost estimator is not available in the AWS GovCloud (US) Region. The cost estimator is a console feature that provides cost estimates for security capabilities across your AWS environment, comparing individual service pricing (GuardDuty, Amazon Inspector, Security Hub CSPM) against Security Hub's simplified pricing plans. It uses AWS Cost Explorer data to auto-populate usage information for management, delegated administrator, member, and standalone accounts. For more information about the cost estimator in other AWS Regions, see [AWS Security Hub Cost Estimator](../../../securityhub/latest/userguide/security-hub-cost-estimator.md "../../../securityhub/latest/userguide/security-hub-cost-estimator.md") in the _AWS Security Hub User Guide_.

**Usage**

The Security Hub Usage page is not available in the AWS GovCloud (US) Region. The Usage page is a console feature that helps customers track and manage Security Hub costs by displaying current costs, projected monthly costs, and usage broken down by security capability or individual AWS account. Customers in AWS GovCloud (US) can continue to use AWS Cost Explorer to analyze Security Hub costs. For more information about the Usage page in other AWS Regions, see [Understanding the Security Hub Usage page](../../../securityhub/latest/userguide/security-hub-usage-page.md "../../../securityhub/latest/userguide/security-hub-usage-page.md") in the _AWS Security Hub User Guide_.

**Security Hub Extended Plan**

The Security Hub Extended plan is not available in the AWS GovCloud (US) Region. The Extended plan enables customers to protect their enterprise estate across cloud, endpoint, network, identity, data, email, and browser through an integrated security operations experience centered in Security Hub. With the Extended plan, customers can subscribe to partner solutions with flexible pay-as-you-go pricing through AWS Marketplace, with no upfront investments or long-term commitments required.

**Unused access findings**

In the AWS GovCloud (US) Region the unused access analyzer runs in the us-gov-west-1 region. For more information about unused access findings see: [Understanding unused access findings in Security Hub](../../../securityhub/latest/userguide/unused-access-findings.md "../../../securityhub/latest/userguide/unused-access-findings.md") in the _AWS Security Hub User Guide_.

**Network Scanning**

The Network Scanning feature is not available in the AWS GovCloud (US) Region. For more information about Network Scanning in Security Hub see [Network Scanning in Security Hub](../../../securityhub/latest/userguide/securityhub-v2-network-scanning.md "../../../securityhub/latest/userguide/securityhub-v2-network-scanning.md") in the _AWS Security Hub User Guide_.

**Account Coverage**

The Account coverage page and widget do not include coverage details for how many accounts have Security Hub enabled in the AWS GovCloud (US) Region. For more information about account coverage in Security Hub see [Account coverage in Security Hub](../../../securityhub/latest/userguide/security-hub-account-coverage.md "../../../securityhub/latest/userguide/security-hub-account-coverage.md") in the _AWS Security Hub User Guide_.

**AWS Security Hub CSPM and Amazon Inspector**

Security Hub uses findings from AWS Security Hub CSPM (Cloud Security Posture Management) and Amazon Inspector. For information about the availability of these features in AWS GovCloud (US) Region, see the following:

- **AWS Security Hub CSPM** - For information about AWS Security Hub CSPM feature differences in AWS GovCloud (US) Region, including controls, see [AWS Security Hub CSPM in AWS GovCloud (US)](govcloud-ash.md "govcloud-ash.md") in the _AWS GovCloud (US) User Guide_.
- **Amazon Inspector** - For information about Amazon Inspector feature differences in AWS GovCloud (US) Region, see [Amazon Inspector in AWS GovCloud (US)](govcloud-inspector.md "govcloud-inspector.md") in the _AWS GovCloud (US) User Guide_.

## Documentation

- [AWS Security Hub documentation](../../../securityhub/latest/userguide/what-is-securityhub-v2.md "../../../securityhub/latest/userguide/what-is-securityhub-v2.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No data will leave the AWS GovCloud (US) Regions for this service.
