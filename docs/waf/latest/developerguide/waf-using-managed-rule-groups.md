**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Working with managed rule

groups

This section provides guidance for accessing and managing your managed rule groups.

When you add a managed rule group to your protection pack (web ACL), you can choose the same
configuration options as you can your own rule groups, plus additional settings.

Through the console, you access managed rule group information during the process
of adding and editing the rules in your protection packs (web ACLs). Through the APIs and the command
line interface (CLI), you can directly request managed rule group
information.

When you use a managed rule group in your protection pack (web ACL), you can edit the following settings:

- **Version** – This is available only if the rule
  group is versioned. For more information, see [Using versioned managed rule groups in AWS WAF](waf-managed-rule-groups-versioning.md "waf-managed-rule-groups-versioning.md").
- **Override rule actions** – You can override the
  actions for rules in the rule group to any action. Setting them to
  Count is useful for testing a rule group before using it
  to manage your web requests. For more information, see [Rule group rule action overrides](web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rules "web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rules").
- **Scope-down statement** – You can add a
  scope-down statement, to filter out web requests that you don't want to
  evaluate with the rule group. For more information, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").
- **Override rule group action** – You can override
  the action that results from the rule group evaluation, and set it to
  Count only. This option isn't commonly used. It
  doesn't alter how AWS WAF evaluates the rules in the rule group. For more
  information, see [Rule group return action override to
  Count](web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rule-group "web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rule-group").

###### To edit the managed rule group settings in your protection pack (web ACL)

- **Console**
  - (Option) When you add the managed rules group to your protection pack (web ACL),
    you can choose **Edit** to view and edit the
    settings.
  - (Option) After you've added the managed rule group into your
    protection pack (web ACL), from the **protection packs (web ACLs)** page, choose the
    protection pack (web ACL) you just created. This takes you to the protection pack (web ACL) edit
    page.
    - Choose **Rules**.
    - Select the rule group, then choose
      **Edit** to view and edit the
      settings.

- **APIs and CLI** – Outside of the
  console, you can manage the managed rule group settings when you create
  and update the protection pack (web ACL).
