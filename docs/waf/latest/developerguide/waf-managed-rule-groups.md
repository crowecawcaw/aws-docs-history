**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using managed rule groups in AWS WAF

This section explains what managed rule groups are and how they work.

Managed rule groups are collections of predefined, ready-to-use rules that AWS and AWS Marketplace sellers
write and maintain for you. Basic AWS WAF pricing applies to your use of any managed rule group.
For AWS WAF pricing information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

- _The AWS Managed Rules rule groups for AWS WAF Bot Control, AWS WAF Fraud Control account takeover prevention (ATP), and AWS WAF Fraud Control account creation fraud prevention (ACFP)_ are available
  for additional fees, beyond the basic AWS WAF charges. For pricing details, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").
- _All other AWS Managed Rules rule groups_ are available to AWS WAF customers
  at no additional cost.
- _AWS Marketplace rule groups_ are available by subscription through AWS Marketplace.
  Each of these rule groups is owned and managed by the AWS Marketplace seller. For
  pricing information to use an AWS Marketplace rule group, contact the AWS Marketplace seller.
  Some managed rule groups are designed to help protect specific types of web applications like
  WordPress, Joomla, or PHP. Others offer broad protection against known threats or common web
  application vulnerabilities, including some of the ones listed in the [OWASP Top
  10](https://owasp.org/www-project-top-ten/ "https://owasp.org/www-project-top-ten/"). If you're subject to regulatory
  compliance like PCI or HIPAA, you might be able to use managed rule groups to satisfy web
  application firewall requirements.

###### Automatic updates

Keeping up to date on the constantly changing threat landscape can be time consuming and
expensive. Managed rule groups can save you time when you implement and use AWS WAF.
Many AWS and AWS Marketplace sellers automatically update managed rule groups and provide
new versions of rule groups when new vulnerabilities and threats emerge.

In some cases, AWS is notified of new vulnerabilities before public disclosure, due to its
participation in a number of private disclosure communities. In those cases, AWS can
update the AWS Managed Rules rule groups and deploy them for you even before a new threat is widely known.

###### Restricted access to rules in a managed rule group

Each managed rule group provides a comprehensive description of the types of attacks and
vulnerabilities that it's designed to protect against. To protect the intellectual
property of the rule group providers, you can't view all of the details for the
individual rules within a rule group. This restriction also helps to keep malicious
users from designing threats that specifically circumvent published rules.

###### Topics

- [Using versioned managed rule groups in AWS WAF](waf-managed-rule-groups-versioning.md "waf-managed-rule-groups-versioning.md")
- [Working with managed rule
  groups](waf-using-managed-rule-groups.md "waf-using-managed-rule-groups.md")
- [AWS Managed Rules for AWS WAF](aws-managed-rule-groups.md "aws-managed-rule-groups.md")
