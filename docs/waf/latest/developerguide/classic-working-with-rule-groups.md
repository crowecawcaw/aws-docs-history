**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Working with AWS WAF Classic rule groups for use with AWS Firewall Manager

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

An AWS WAF Classic _rule group_ is a set of rules that you add to an AWS WAF Classic
AWS Firewall Manager policy. You can create your own rule group, or you can purchase a managed rule
group from AWS Marketplace.

###### Important

If you want to add an AWS Marketplace rule group to your Firewall Manager policy, each account in your
organization must first subscribe to that rule group. After all accounts have
subscribed, you can then add the rule group to a policy. For more information, see [AWS Marketplace rule groups](classic-waf-managed-rule-groups.md "classic-waf-managed-rule-groups.md").

###### Topics

- [Creating an AWS WAF Classic rule group](classic-create-rule-group.md "classic-create-rule-group.md")
- [Adding and deleting rules from an AWS WAF Classic rule group](classic-rule-group-editing.md "classic-rule-group-editing.md")
