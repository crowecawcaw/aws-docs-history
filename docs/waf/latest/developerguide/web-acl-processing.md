**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using protection packs (web ACLs) with rules and rule groups in AWS WAF

This section introduces how protection packs (web ACLs) and web ACLs work with rules and rule groups.

The way a protection pack (web ACL) handles a web request depends on the following:

- The numeric priority settings of the rules in the protection pack (web ACL) and inside rule groups
- The action settings on the rules and protection pack (web ACL)
- Any overrides that you place on the rules in the rule groups that you add
  For a list of the rule action settings, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

You can customize request and response handling in your rule action settings and
default protection pack (web ACL) action settings. For information, see [Customized web requests and responses in
AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").

###### Topics

- [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md")
- [How AWS WAF handles rule and rule group actions](web-acl-rule-actions.md "web-acl-rule-actions.md")
- [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md")
