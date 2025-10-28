**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF rule groups

This section explains what a rule group is and how it works.

A rule group is a reusable set of rules that you can add to a protection pack (web ACL). For more information
about protection packs (web ACLs), see [Configuring protection in AWS WAF](web-acl.md "web-acl.md").

Rule groups fall into the following main categories:

- Your own rule groups, which you create and maintain.
- Managed rule groups that AWS Managed Rules teams create and maintain for you.
- Managed rule groups that AWS Marketplace sellers create and maintain for you.
- Rule groups that are owned and managed by other services like AWS Firewall Manager and Shield Advanced.

###### Differences between rule groups and protection packs (web ACLs)

Rule groups and protection packs (web ACLs) both contain rules, which are defined in the same manner in both
places. Rule groups differ from protection packs (web ACLs) in the following ways:

- Rule groups can't contain rule group reference statements.
- You can reuse a single rule group in multiple protection packs (web ACLs) by adding a rule group reference
  statement to each protection pack (web ACL). You can't reuse a protection pack (web ACL).
- Rule groups don't have default actions. In a protection pack (web ACL), you set a default action for
  each rule or rule group that you include. Each individual rule inside a rule group
  or protection pack (web ACL) has an action defined.
- You don't directly associate a rule group with an AWS resource. To protect
  resources using a rule group, you use the rule group in a protection pack (web ACL).
- The system defines a maximum capacity of 5,000 protection pack (web ACL) capacity units (WCUs) for each protection pack (web ACL). Each rule group has a WCU setting that must be set at creation. You can use
  this setting to calculate the additional capacity requirements that using a rule
  group would add to your protection pack (web ACL). For more information about WCUs, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").
  For information about rules, see [AWS WAF rules](waf-rules.md "waf-rules.md").

This section provides guidance for creating and managing your own rule groups,
describes the managed rule groups that are available to you, and provides guidance for
using managed rule groups.

###### Topics

- [Using managed rule groups in AWS WAF](waf-managed-rule-groups.md "waf-managed-rule-groups.md")
- [Managing your own rule groups](waf-user-created-rule-groups.md "waf-user-created-rule-groups.md")
- [AWS Marketplace rule groups](marketplace-rule-groups.md "marketplace-rule-groups.md")
- [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md")
