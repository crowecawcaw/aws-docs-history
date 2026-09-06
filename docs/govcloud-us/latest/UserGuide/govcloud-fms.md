

# AWS Firewall Manager in AWS GovCloud (US)
<a name="govcloud-fms"></a>

AWS Firewall Manager simplifies your administration and maintenance tasks across multiple accounts and resources for AWS WAF, AWS Shield Advanced, Amazon VPC security groups, and AWS Network Firewall. With Firewall Manager, you set up your AWS WAF firewall rules, Shield Advanced protections, Amazon VPC security groups, Network Firewall firewalls, and DNS Firewall rule group associations just once. The service automatically applies the rules and protections across your accounts and resources, even as you add new resources.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Firewall Manager differs
<a name="govcloud-diffs-28"></a>

The following differences apply to AWS Firewall Manager:
+  AWS Marketplace managed rule groups for AWS WAF cannot be used with Firewall Manager security policies in AWS GovCloud (US). Managed rule groups are collections of predefined, ready-to-use rules that AWS and AWS Marketplace sellers write and maintain for you. AWS managed rule groups are provided free of charge with AWS WAF and are available for use in AWS GovCloud (US) with Firewall Manager security policies. AWS Marketplace rule groups are provided for subscription by AWS Marketplace sellers and are not available for use in AWS GovCloud (US) with Firewall Manager.
+  Firewall Manager security policies for AWS WAF cannot be enabled on Amazon CloudFront distributions in AWS GovCloud (US).
+  Firewall Manager does not support AWS Shield Advanced or AWS WAF Classic.

## Documentation
<a name="govcloud-docs-67"></a>

 [AWS Firewall Manager documentation](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html).

## Export-controlled content
<a name="govcloud-itar-content-106"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ AWS Firewall Manager metadata is not permitted to contain export-controlled data. For example, do not enter export-controlled data into user input fields such as the following:
  + Firewall Manager policy name
  + Resource Tag/Key values