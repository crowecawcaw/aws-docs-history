**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Referencing reusable entities in AWS WAF

This section explains how reusable entities work in AWS WAF.

Some rules use entities that are reusable and that are managed outside of your web
ACLs, either by you, AWS, or an AWS Marketplace seller. When the reusable entity is updated,
AWS WAF propagates the update to your rule. For example, if you use an AWS Managed Rules rule group in a
protection pack (web ACL), when AWS updates the rule group, AWS propagates the change to your web
ACL, to update its behavior. If you use an IP set statement in a rule, when you
update the set, AWS WAF propagates the change to all rules that reference it, so any
protection packs (web ACLs) that use those rules are kept up-to-date with your changes.

The following are the reusable entities that you can use in a rule statement.

- **IP sets** – You create and manage
  your own IP sets. On the console, you can access these from the navigation
  pane. For information about managing IP sets, see [IP sets and regex pattern sets in AWS WAF](waf-referenced-set-managing.md "waf-referenced-set-managing.md").
- **Regex match sets** – You create and
  manage your own regex match sets. On the console, you can access these from
  the navigation pane. For information about managing regex pattern sets, see
  [IP sets and regex pattern sets in AWS WAF](waf-referenced-set-managing.md "waf-referenced-set-managing.md").
- **AWS Managed Rules rule groups** – AWS manages these
  rule groups. On the console, these are available for your use when you add a
  managed rule group to your protection pack (web ACL). For more information about these, see
  [AWS Managed Rules rule groups list](aws-managed-rule-groups-list.md "aws-managed-rule-groups-list.md").
- **AWS Marketplace managed rule groups** – AWS Marketplace
  sellers manage these rule groups and you can subscribe to them to use them.
  To manage your subscriptions, on the navigation pane of the console, choose
  **AWS Marketplace**. The AWS Marketplace managed rule groups are listed
  when you add a managed rule group to your protection pack (web ACL). For rule groups that you
  haven't yet subscribed to, you can find a link to AWS Marketplace on that page as
  well. For more information about AWS Marketplace seller managed rule groups, see [AWS Marketplace rule groups](marketplace-rule-groups.md "marketplace-rule-groups.md").
- **Your own rule groups** – You manage
  your own rule groups, usually when you need some behavior that isn't
  available through the managed rule groups. On the console, you can access
  these from the navigation pane. For more information, see [Managing your own rule groups](waf-user-created-rule-groups.md "waf-user-created-rule-groups.md").

###### Deleting a referenced set or rule group

When you delete a referenced entity, AWS WAF checks to see if it's currently
being used in a protection pack (web ACL). If AWS WAF finds that it's in use, it warns you. AWS WAF is
almost always able to determine if an entity is being referenced by a protection pack (web ACL).
However, in rare cases, it might not be able to do so. If you need to be sure
that the entity that you want to delete isn't in use, check for it in your web
ACLs before deleting it.
