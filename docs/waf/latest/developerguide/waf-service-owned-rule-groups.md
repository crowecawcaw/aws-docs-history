**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Recognizing rule groups provided by other services

If you or an administrator in your organization uses AWS Firewall Manager or AWS Shield Advanced to manage resource protections using AWS WAF, you might see rule group reference statements added to protection packs (web ACLs) in your account.

The names of these rule groups begin with the following strings:

- **`ShieldMitigationRuleGroup`**
  – These rule groups are managed by AWS Shield Advanced and used to provide
  automatic application layer DDoS mitigation to protected application layer (layer 7)
  resources.

When you enable automatic application layer DDoS mitigation for a protected resource,
Shield Advanced adds one of these rule groups to the protection pack (web ACL) that you have associated
with the resource. Shield Advanced assigns the rule group reference statement a
priority setting of 10,000,000, so that it runs
after the rules that you have configured in the protection pack (web ACL). For more information
about these rule groups, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

###### Warning

Don't try to manually manage this rule group in your protection pack (web ACL). In particular, don't manually
delete the `ShieldMitigationRuleGroup` rule group reference
statement from your protection pack (web ACL). Doing this could have unintended consequences
for all resources that are associated with the protection pack (web ACL). Instead, use
Shield Advanced to disable automatic mitigation for the resources that are
associated with the protection pack (web ACL). Shield Advanced will remove the rule group for you
when it's not needed for automatic mitigation.

- **`PREFMManaged` and `POSTFMManaged`**
  – These rule groups are managed by AWS Firewall Manager based on Firewall Manager AWS WAF policy configurations.
  Firewall Manager provides these rule groups inside protection packs (web ACLs) that Firewall Manager manages.

Firewall Manager creates protection packs (web ACLs) for you with names that begin with `FMManagedWebACLV2`.
You can configure Firewall Manager to retrofit your existing protection packs (web ACLs) as well. For these,
the protection pack (web ACL) name is the one that you specified when you created it. In either case, Firewall Manager will add these rule groups
to the protection pack (web ACL). For more information, see [Using AWS WAF policies with Firewall Manager](waf-policies.md "waf-policies.md").
