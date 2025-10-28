**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS Firewall Manager

AWS Firewall Manager simplifies your administration and maintenance tasks across multiple accounts
and resources for a variety of protections, including AWS WAF, AWS Shield Advanced, Amazon VPC security groups and network ACLs,
AWS Network Firewall, and Amazon Route 53 Resolver DNS Firewall. With Firewall Manager, you set up your protections just once
and the service automatically applies them across your accounts and resources, even as you add new accounts and resources.

Firewall Manager provides these benefits:

- Helps to protect resources across accounts
- Helps to protect all resources of a particular type, such as all Amazon CloudFront
  distributions
- Helps to protect all resources with specific tags
- Automatically adds protection to resources that are added to your account
- Allows you to subscribe all member accounts in an AWS Organizations organization to
  AWS Shield Advanced, and automatically subscribes new in-scope accounts that join the
  organization
- Allows you to apply security group rules to all member accounts or specific subsets of accounts in an AWS Organizations
  organization, and automatically applies the
  rules to new in-scope accounts that join the organization
- Lets you use your own rules, or purchase managed rules from AWS Marketplace
  Firewall Manager is particularly useful when you want to protect your entire organization rather than a
  small number of specific accounts and resources, or if you frequently add new resources
  that you want to protect. Firewall Manager also provides centralized monitoring of DDoS attacks across
  your organization.

###### Note

Charges incurred by AWS Firewall Manager are for the underlying services, such as AWS WAF and AWS Config. For
more information, see [AWS Firewall Manager Pricing](https://aws.amazon.com/firewall-manager/pricing/ "https://aws.amazon.com/firewall-manager/pricing/").

###### Topics

- [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md")
- [Using AWS Firewall Manager administrators](fms-administrators.md "fms-administrators.md")
- [Setting up AWS Firewall Manager policies](getting-started-fms-intro.md "getting-started-fms-intro.md")
- [Using AWS Firewall Manager policies](working-with-policies.md "working-with-policies.md")
- [Using Firewall Manager managed lists](working-with-managed-lists.md "working-with-managed-lists.md")
- [Grouping your resources in Firewall Manager](fms-resource-sets.md "fms-resource-sets.md")
- [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md")
- [AWS Firewall Manager integration with AWS Security Hub](fms-findings.md "fms-findings.md")
- [Security in your use of the AWS Firewall Manager service](fms-security.md "fms-security.md")
- [AWS Firewall Manager quotas](fms-limits.md "fms-limits.md")
- [Migrating AWS WAF Classic Web ACLs in Firewall Manager](migrate-waf-classic-fms.md "migrate-waf-classic-fms.md")
