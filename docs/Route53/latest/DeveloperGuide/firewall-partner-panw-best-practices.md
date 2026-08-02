# Best practices for Palo Alto Networks partner managed rules

We recommend the following best practices when using Palo Alto Networks partner
managed DNS threat protection:

- **Testing before production:** Before deploying
  to production, use `ALERT` mode to perform a dry run. Review alert logs, then
  switch to `BLOCK` after it is validated.
- **Multiple rules per category:** Each security
  category creates a separate rule. You can assign different actions to different
  categories.
- **Amazon VPC association:** After adding rules, make sure
  the rule group is associated with a Amazon VPC for the rules to take
  effect.
- **AWS Firewall Manager integration:** Use the
  **Associate with an AWS Firewall Manager policy** option to apply rule
  groups across your organization.
