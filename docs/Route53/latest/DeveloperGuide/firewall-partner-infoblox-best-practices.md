

# Best practices for Infoblox partner managed rules

We recommend the following best practices when using Infoblox partner managed DNS threat protection:
+ **Testing before production:** Before deploying to production, use `ALERT` mode to perform a dry run. Review alert logs, then switch to `BLOCK` after it is validated. This matters most for the lower threat levels, which can match more legitimate domains.
+ **Multiple rules per category:** Each security category creates a separate rule. You can assign different actions to different categories, for example `BLOCK` for critical and high risk domains and `ALERT` for the rest.
+ **Amazon VPC association:** After adding rules, make sure the rule group is associated with a Amazon VPC for the rules to take effect.
+ **AWS Firewall Manager integration:** Use the **Associate with an AWS Firewall Manager policy** option to apply rule groups across your organization.