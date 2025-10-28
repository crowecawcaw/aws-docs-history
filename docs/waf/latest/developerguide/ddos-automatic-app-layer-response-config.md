**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Enabling automatic application layer DDoS mitigation

This page explains how to configure Shield Advanced to automatically respond to
application layer attacks.

You enable Shield Advanced automatic mitigation as part of the application layer
DDoS protections for your resource. For information about doing this through the
console, see [Configure application layer DDoS protections](manage-protection.md#configure-app-layer-protection "manage-protection.md#configure-app-layer-protection").

The automatic mitigation functionality requires you to do the
following:

- **Associate a web ACL with the resource**
  – This is required for any Shield Advanced application layer protection. You
  can use the same web ACL for multiple resources. We recommend doing this
  only for resources that have similar traffic. For information about web
  ACLs, including the requirements for using them with multiple resources, see
  [How AWS WAF works](how-aws-waf-works.md "how-aws-waf-works.md").
- **Enable and configure Shield Advanced
  automatic application layer DDoS mitigation** – When you enable this,
  you specify whether you want Shield Advanced to automatically block or count web
  requests that it determines to be part of a DDoS attack. Shield Advanced adds a
  rule group to the associated web ACL and uses it to dynamically manage its
  response to DDoS attacks on the resource. For information about the rule
  action options, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").
- **(Optional, but recommended) Add a rate-based rule to
  the web ACL** – By default, the rate-based rule provides your
  resource with basic protection against DDoS attacks by preventing any
  individual IP address from sending too many requests in a short time. For
  information about rate-based rules, including custom request aggregation options and
  examples, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").

## What happens

when you enable automatic mitigation

Shield Advanced does the following when you enable automatic mitigation:

- **As needed, adds a rule group for Shield Advanced use** –
  If the AWS WAF web ACL that you have associated with the resource doesn't
  already have an AWS WAF rule group rule that's dedicated to
  automatic application layer DDoS mitigation, Shield Advanced adds one.

The name of the rule group rule starts with `ShieldMitigationRuleGroup`. The
rule group always contains a rate-based rule named
`ShieldKnownOffenderIPRateBasedRule`, which limits the
volume of requests from IP addresses that are known to be sources of
DDoS attacks. For additional details about the Shield Advanced rule group and
the web ACL rule that references it, see [Protecting the application layer with the Shield Advanced
rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md").

- **Starts responding to DDoS attacks against the resource**
  – Shield Advanced automatically responds to DDoS attacks for the
  protected resource. In addition to the rate-based rule, which is always
  present, Shield Advanced uses its rule group to deploy custom AWS WAF rules for
  DDoS attack mitigation. Shield Advanced tailors these rules to your application
  and to the attacks that your application experiences, and tests them
  against the resource's historical traffic before deploying them.

Shield Advanced uses a single rule group rule in any web ACL that you use for
automatic mitigation. If Shield Advanced has already added the rule group for
another protected resource, it doesn't add another rule group to the web ACL.

Automatic application layer DDoS mitigation depends on the presence of the rule group to
mitigate attacks. If the rule group is removed from the AWS WAF web ACL for any
reason, the removal disables automatic mitigation for all resources
that are associated with the web ACL.
