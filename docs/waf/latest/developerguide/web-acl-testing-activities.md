**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Monitoring and tuning your AWS WAF protections

Monitor and tune your AWS WAF protections.

###### Note

To follow the guidance in this section, you need to understand generally how to create and
manage AWS WAF protections like protection packs (web ACLs), rules, and rule groups. That information is
covered in earlier sections of this guide.

Monitor web traffic and rule matches to verify the behavior of the protection pack (web ACL). If
you find problems, adjust your rules to correct and then monitor to verify the
adjustments.

Repeat the following procedure until the protection pack (web ACL) is managing your web traffic as
you need it to.

###### To monitor and tune

1. ###### Monitor traffic and rule matches

Make sure that traffic is flowing and that your test rules are finding
matching requests.

Look for the following information for the protections that you're
testing:

    * **Logs** – Access information about the rules that
     match a web request:




    	+ **Your rules** - Rules in the protection pack (web ACL) that have
    	 Count action are listed under
    	 `nonTerminatingMatchingRules`. Rules with
    	 Allow or Block are listed as the
    	 `terminatingRule`. Rules with CAPTCHA or
    	 Challenge can be either terminating or non-terminating,
    	 and so are listed under one of the two categories, according to
    	 the result of the rule match.
    	+ **Rule groups** - Rule groups are identified in the
    	 `ruleGroupId` field, with their rule matches
    	 categorized the same as for standalone rules.
    	+ **Labels** - Labels that rules have applied to the
    	 request are listed in the `Labels` field.
    For more information, see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").
    * **Amazon CloudWatch metrics** – You can access the following
     metrics for your protection pack (web ACL) request evaluation.




    	+ **Your rules** – Metrics are grouped by the rule
    	 action. For example, when you test a rule in Count
    	 mode, its matches are listed as `Count` metrics
    	 for the protection pack (web ACL).
    	+ **Your rule groups** – The metrics for your rule
    	 groups are listed under the rule group metrics.
    	+ **Rule groups owned by another account** – Rule group metrics
    	 are generally visible only to the rule group owner. However, if
    	 you override the rule action for a rule, the metrics for that
    	 rule will be listed under your protection pack (web ACL) metrics. Additionally, labels added by any rule
    	 group are listed in your protection pack (web ACL) metrics.


    	Rule groups in this category are [AWS Managed Rules for AWS WAF](aws-managed-rule-groups.md "aws-managed-rule-groups.md"), [AWS Marketplace rule groups](marketplace-rule-groups.md "marketplace-rule-groups.md"), [Recognizing rule groups provided by other services](waf-service-owned-rule-groups.md "waf-service-owned-rule-groups.md"), and rule
    	 groups that are shared with you by another account. When a protection pack (web ACL) is deployed through Firewall Manager, any rules within the WebACL that have a Count action will not display their metrics in the member account.
    	+ **Labels** - Labels that were added to a web request
    	 during evaluation are listed in the protection pack (web ACL) label metrics. You
    	 can access the metrics for all labels, regardless of whether they were added
    	 by your rules and rule groups or by rules in a rule group that another account owns.
    For more information, see [Viewing metrics for your web
     ACL](web-acl-testing-view-metrics.md "web-acl-testing-view-metrics.md").
    * **protection pack (web ACL) traffic overview dashboards** –
     Access summaries of the web traffic that a protection pack (web ACL) has evaluated by
     going to the protection pack (web ACL)'s page in the AWS WAF console and opening the
     **Traffic overview** tab.


    The traffic overview dashboards provide near real-time summaries of the Amazon CloudWatch metrics
     that AWS WAF collects when it evaluates your application web traffic.


    For more information, see [Traffic overview dashboards for protection packs (web ACLs)](web-acl-dashboards.md "web-acl-dashboards.md").
    * **Sampled web requests** – Access information for
     the rules that match a sampling of the web requests. The sample
     information identifies matching rules by the metric name for the rule in
     the protection pack (web ACL). For rule groups, the metric identifies the rule group
     reference statement. For rules inside rule groups, the sample lists the
     matching rule name in `RuleWithinRuleGroup`.


    For more information, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

2. ###### Configure mitigations to address false positives

If you determine that a rule is generating false positives, by matching web requests when
it shouldn't, the following options can help you tune your protection pack (web ACL) protections
to mitigate.

###### Correcting rule inspection criteria

For your own rules, you often just need to adjust the settings that you're using to
inspect web requests. Examples include changing the specifications in a
regex pattern set, adjusting the text transformations that you apply to a
request component before inspection, or switching to using a forwarded IP
address. See the guidance for the rule type that's causing problems, under
[Using rule statements in AWS WAF](waf-rule-statements.md "waf-rule-statements.md").

###### Correcting more complex problems

For inspection criteria that you don't control and for some complex rules, you might
need to make other changes, like adding rules that explicitly allow
or block requests or that eliminate requests from evaluation by the
problematic rule. Managed rule groups most commonly need this type
of mitigation, but other rules can too. Examples include the
rate-based rule statement and the SQL injection attack rule
statement.

What you do to mitigate false positives depends on your use case. The following are common
approaches:

    * **Add a mitigating rule** – Add a rule that runs
     before the new rule and that explicitly allows requests that are causing
     false positives. For information about rule evaluation order in a web
     ACL, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").


    With this approach, the allowed requests are sent to the protected resource, so they
     never reach the new rule for evaluation. If the new rule is a paid
     managed rule group, this approach can also help contain the cost of
     using the rule group.
    * **Add a logical rule with a mitigating rule** – Use
     logical rule statements to combine the new rule with a rule that
     excludes the false positives. For information, see [Using logical rule statements in AWS WAF](waf-rule-statements-logical.md "waf-rule-statements-logical.md").


    For example, say you're adding an SQL injection attack match statement that's generating
     false positives for a category of requests. Create a rule that matches
     those requests, and then combine the rules using logical rule statements
     so that you match only on requests that both don't match the false
     positives criteria and do match the SQL injection attack criteria.
    * **Add a scope-down statement** – For rate-based
     statements and managed rule group reference statements, exclude requests
     that result in false positives from evaluation by adding a scope-down
     statement inside the main statement.


    A request that doesn't match the scope-down statement never reaches the rule group or
     rate-based evaluation. For information about scope-down statements, see
     [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md"). For an example,
     see [Excluding IP range from bot management](waf-bot-control-example-scope-down-ip.md "waf-bot-control-example-scope-down-ip.md").
    * **Add a label match rule** – For rule groups that
     use labeling, identify the label that the problematic rule is applying
     to requests. You might need to set the rule group rules in count mode
     first, if you haven't already done that. Add a label match rule,
     positioned to run after the rule group, that matches against the label
     that's being added by the problematic rule. In the label match rule, you
     can filter the requests that you want to allow from those that you want
     to block.


    If you use this approach, when you're finished testing, keep the problematic rule in
     count mode in the rule group, and keep your custom label match rule in
     place. For information about label match statements, see [Label match rule
     statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md"). For examples,
     see [Allowing a specific blocked bot](waf-bot-control-example-allow-blocked-bot.md "waf-bot-control-example-allow-blocked-bot.md")
     and [ATP example: Custom
     handling for missing and compromised credentials](waf-atp-control-example-user-agent-exception.md "waf-atp-control-example-user-agent-exception.md").
    * **Change the version of a managed rule group** – For
     versioned managed rule groups, change the version that you're using. For
     example, you could switch back to the last static version that you were
     using successfully.


    This is usually a temporary fix. You might change the version for
     your production traffic while you continue testing the latest version in
     your test or staging environment, or while you wait for a more
     compatible version from the provider. For information about managed rule
     group versions, see [Using managed rule groups in AWS WAF](waf-managed-rule-groups.md "waf-managed-rule-groups.md").

When you're satisfied that the new rules are matching requests as you need them to, move to
the next stage of your testing and repeat this procedure. Perform the final stage of
testing and tuning in your production environment.
