# AWS WAF in AWS GovCloud (US)

AWS WAF is a web application firewall that lets you monitor web requests that are forwarded to resources, such as AWS API Gateway and AWS Application Load Balancers. You can also use AWS WAF to block or allow requests based on conditions that you specify, such as the IP addresses that requests originate from or values in the requests.

For list of services that AWS WAF supports, please visit the [service page](https://aws.amazon.com/waf "https://aws.amazon.com/waf").

## How AWS WAF Differs for AWS GovCloud (US)

AWS WAF for AWS GovCloud (US) doesn't support the following functionality:

- Managed rule groups that are provided for subscription by AWS Marketplace third party sellers are not available for use in AWS GovCloud (US). The only managed rule groups that are available in AWS GovCloud (US) are the AWS managed rule groups that are provided with AWS WAF.
  For more information about managed rule groups in AWS WAF, see [Managed rule groups](../../../waf/latest/developerguide/waf-managed-rule-groups.md "../../../waf/latest/developerguide/waf-managed-rule-groups.md") in the AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide.

## Documentation for AWS WAF

[AWS WAF documentation](https://aws.amazon.com/documentation/waf/ "https://aws.amazon.com/documentation/waf/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No export-controlled data may be entered, stored, or processed by AWS WAF.
  For example, AWS WAF metadata is not permitted to contain export-controlled
  data.

For example, do not enter export-controlled data in the following
fields:

    + Web ACL name
    + CloudWatch metric name
    + Condition
    + Rule name
    + String filters and regex pattern set
