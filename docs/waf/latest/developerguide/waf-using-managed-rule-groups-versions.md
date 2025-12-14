**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Retrieving the available versions for a managed rule

group

The available versions of a managed rule group are versions that haven't yet
been scheduled to expire. The list indicates which version is the current default version for the rule group.

###### To retrieve a list of the available versions of a managed rule group

- **Console**
  - (Option) When you add the managed rule group to your protection pack (web ACL),
    choose **Edit** to see the rule group's
    information. Expand the **Version** dropdown to
    see the list of available versions.
  - (Option) After you've added the managed rule group into your protection pack (web ACL), choose
    **Edit** on the protection pack (web ACL), and then select
    and edit the rule group rule. Expand the
    **Version** dropdown to see the list of
    available versions.

- **API** –
  - `ListAvailableManagedRuleGroupVersions`

- **CLI** –
  - `aws wafv2 list-available-managed-rule-group-versions
--scope=<CLOUDFRONT|REGIONAL> --vendor-name <vendor> --name
<managedrule_name>`
