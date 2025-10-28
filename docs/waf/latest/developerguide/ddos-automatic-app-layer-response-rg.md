**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Protecting the application layer with the Shield Advanced

rule group

This page explains how the Shield Advanced rule group works in your web ACL.

Shield Advanced manages automatic mitigation activities using rules in a rule group that
it owns and manages for you. Shield Advanced references the rule group with a rule in the
web ACL that you have associated with your protected resource.

###### The rule group rule in your web ACL

The Shield Advanced rule group rule in your web ACL has the following properties:

- **Name** –
  `ShieldMitigationRuleGroup``_`account-id`_`web-acl-id`_`unique-identifier``
- **Web ACL capacity units (WCU)** –

150.  These WCUs count against the WCU
      usage in your web ACL.
      Shield Advanced creates this rule in your web ACL with a priority setting of
      10,000,000, so that it runs after your other rules
      and rule groups in the web ACL. AWS WAF runs the rules in a web ACL from the lowest
      numeric priority setting on up. During your management of the web ACL, this priority
      setting might change.

The automatic mitigation functionality doesn't consume any additional
AWS WAF resources in your account, other than the WCUs used by the rule group in your web ACL. For
example, the Shield Advanced rule group isn't counted as one of your account's rule groups.
For information about account limits in AWS WAF, see [AWS WAF quotas](limits.md "limits.md").

###### Rules in the rule group

Within the referenced Shield Advanced rule group, Shield Advanced maintains a rate-based
rule `ShieldKnownOffenderIPRateBasedRule`, which limits the volume of
requests from IP addresses that are known to be sources of DDoS attacks. This
rule serves as the first line of defense against any attack, because it's always
present in the rule group and it doesn't rely on the analysis of traffic
patterns to contain attacks. This rule's action is set to the action that you
choose for your automatic mitigations, just like the other rules in
the rule group. For information about rate-based rules, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").

###### Note

The rate-based rule `ShieldKnownOffenderIPRateBasedRule` operates independent of
Shield Advanced event detection. While automatic mitigation is enabled, this rule rate limits IP addresses that
are known to be sources of DDoS attacks. For these IP addresses, the rule's rate limiting can prevent attacks
and also keep attacks from appearing in the Shield Advanced detection information. This trade off favors prevention
over complete visibility into attack patterns.

In addition to the permanent rate-based rule described above, the rule group contains any rules that Shield Advanced is
currently using to mitigate DDoS attacks. Shield Advanced adds, modifies, and removes these
rules as needed. For information, see [How Shield Advanced manages automatic mitigation](ddos-automatic-app-layer-response-behavior.md "ddos-automatic-app-layer-response-behavior.md").

###### Metrics

The rule group generates AWS WAF metrics, but because this rule group is owned by
Shield Advanced, these metrics aren't available to view. For more information, see [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md").
