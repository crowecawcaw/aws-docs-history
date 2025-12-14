# AWS Security Hub CSPM in AWS GovCloud (US)

AWS Security Hub provides you with a comprehensive view of your security state in AWS and helps you check your environment against security industry standards and best practices. Security Hub collects security data from across AWS accounts, services, and supported third-party partner products and helps you analyze your security trends and identify the highest priority security issues.

## How Security Hub CSPM differs for AWS GovCloud (US)

**Product integrations**

Not all [integrations with AWS Services and third-party partners](../../../securityhub/latest/userguide/securityhub-findings-providers.md "../../../securityhub/latest/userguide/securityhub-findings-providers.md") are available in the AWS GovCloud (US) Region.

For a list of the supported integrations in the AWS GovCloud (US) Region, see [Integrations that are supported in AWS GovCloud (US-East) and AWS GovCloud (US-West)](../../../securityhub/latest/userguide/securityhub-regions.md#securityhub-regions-integration-support-govcloud "../../../securityhub/latest/userguide/securityhub-regions.md#securityhub-regions-integration-support-govcloud").

**Controls**

Not all security controls are supported in the AWS GovCloud (US) Region. For details, see the following lists in the _AWS Security Hub CSPM User Guide_.

- [Controls that are not supported in AWS GovCloud (US-East)](../../../securityhub/latest/userguide/securityhub-regions.md#securityhub-control-support-govuseast1 "../../../securityhub/latest/userguide/securityhub-regions.md#securityhub-control-support-govuseast1")
- [Controls that are not supported in AWS GovCloud (US-West)](../../../securityhub/latest/userguide/securityhub-regions.md#securityhub-control-support-govuswest1 "../../../securityhub/latest/userguide/securityhub-regions.md#securityhub-control-support-govuswest1")

**Cross-Region aggregation**

[Cross-Region aggregation](../../../securityhub/latest/userguide/finding-aggregation.md "../../../securityhub/latest/userguide/finding-aggregation.md") is supported with limitations in AWS GovCloud (US). In AWS GovCloud (US), cross-Region aggregation is supported only for findings, finding updates, and insights across AWS GovCloud (US). Specifically, you can only aggregate findings, finding updates, and insights between AWS GovCloud (US-East) and AWS GovCloud (US-West).

## Documentation for Security Hub CSPM

[AWS Security Hub CSPM documentation](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
