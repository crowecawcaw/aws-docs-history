

# AWS Security Hub CSPM in AWS GovCloud (US)
<a name="govcloud-ash"></a>

AWS Security Hub CSPM provides you with a comprehensive view of your security state in AWS and helps you check your environment against security industry standards and best practices. Security Hub collects security data from across AWS accounts, services, and supported third-party partner products and helps you analyze your security trends and identify the highest priority security issues.

## Region availability
<a name="region-availability"></a>

 Security Hub CSPM is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-East) 
+  AWS GovCloud (US-West) 

## How Security Hub CSPM differs
<a name="feature-diffs"></a>

 **Product integrations** 

Not all [integrations with AWS Services and third-party partners](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-providers.html) are available in the AWS GovCloud (US) Region.

For a list of the supported integrations in the AWS GovCloud (US) Region, see [Integrations that are supported in AWS GovCloud (US-East) and AWS GovCloud (US-West)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-regions.html#securityhub-regions-integration-support-govcloud).

 **Controls** 

Not all security controls are supported in the AWS GovCloud (US) Region. For details, see the following lists in the * AWS Security Hub CSPM User Guide*.
+  [Controls that are not available in AWS GovCloud (US-East)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-regions.html#securityhub-control-support-govuseast1) 
+  [Controls that are not available in AWS GovCloud (US-West)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-regions.html#securityhub-control-support-govuswest1) 

 **Cross-Region aggregation** 

 [Cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) is supported with limitations in AWS GovCloud (US). In AWS GovCloud (US), cross-Region aggregation is supported only for findings, finding updates, and insights across AWS GovCloud (US). Specifically, you can only aggregate findings, finding updates, and insights between AWS GovCloud (US-East) and AWS GovCloud (US-West).

## Documentation
<a name="documentation"></a>
+  [AWS Security Hub CSPM documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 

## Export-controlled content
<a name="itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.