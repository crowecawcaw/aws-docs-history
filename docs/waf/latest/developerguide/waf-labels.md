**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Web request labeling in AWS WAF

This section explains what AWS WAF labels are.

A label is metadata added to a web request by a rule when the rule matches the request.
Once added, a label remains available on the request until the protection pack (web ACL) evaluation ends. You can access labels in rules
that run later in the protection pack (web ACL) evaluation by using a label match statement. For details, see
[Label match rule
statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md").

Labels on web requests generate Amazon CloudWatch label metrics. For a list of metrics and
dimensions, see [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label"). For
information about accessing metrics and metric summaries through CloudWatch and through the AWS WAF
console, see [Monitoring and tuning your AWS WAF protections](web-acl-testing-activities.md "web-acl-testing-activities.md").

###### Labeling use cases

Common use cases for AWS WAF labels include the following:

- **Evaluating a web request against multiple rule statements before
  taking action on the request** – After a match is found with a
  rule in a protection pack (web ACL), AWS WAF continues evaluating the request against the protection pack (web ACL) if the
  rule action doesn't terminate the protection pack (web ACL) evaluation. You can use labels to evaluate
  and collect information from multiple rules before you decide to allow or block the
  request. To do this, change the actions for your existing rules to Count and
  configure them to add labels to matching requests. Then, add one or more new rules
  to run after your other rules, and configure them to evaluate the labels and manage
  the requests according to the label match combinations.
- **Managing web requests by geographical region** – You
  can use the geographic match rule alone to manage web requests by the country of
  origin. To fine-tune the location down to the region level, you use the geo match
  rule with a Count action followed by a label match rule. For information
  about the geo match rule, see [Geographic match rule
  statement](waf-rule-statement-type-geo-match.md "waf-rule-statement-type-geo-match.md").
- **Reusing logic across multiple rules** –
  If you need to reuse the same logic across multiple rules, you can use labels to
  single-source the logic and just test for the results. When you have multiple
  complex rules that use a common subset of nested rule statements, duplicating
  the common rule set across your complex rules can be time consuming and error
  prone. With labels, you can create a new rule with the common rule subset that
  counts matching requests and adds a label to them. You add the new rule to your
  protection pack (web ACL) so that it runs before your original complex rules. Then, in your
  original rules, you replace the shared rule subset with a single rule that
  checks for the label.

For example, say you have multiple rules that you want to only apply to your
login paths. Rather than have each rule specify the same logic to match
potential login paths, you can implement a single new rule that contains that logic.
Have the new rule add a label to matching requests to indicate that the request is on a login path. In
your protection pack (web ACL), give this new rule a lower numeric priority setting than your
original rules so that it runs first. Then, in your original rules, replace the shared logic with a
check for the presence of the label.
For information about priority settings, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").

- **Creating exceptions to rules in rule groups** – This
  option is particularly useful for managed rule groups, which you can't view or
  alter. Many managed rule group rules add labels to matching web
  requests, to indicate the rules that matched and possibly to provide additional
  information about the match. When you use a rule group that adds labels to
  requests, you can override the rule group rules to count matches, and then run a rule
  after the rule group that handles the web request based on the rule group labels. All
  AWS Managed Rules add labels to matching web requests. For details, see the rule
  descriptions at [AWS Managed Rules rule groups list](aws-managed-rule-groups-list.md "aws-managed-rule-groups-list.md").
- **Using label metrics to monitor traffic patterns**
  – You can access metrics for labels that you add through your rules and for
  metrics added by any managed rule groups that you use in your protection pack (web ACL). All of the
  AWS Managed Rules rule groups add labels to the web requests that they evaluate. For a list of label
  metrics and dimensions, see [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label"). You can access metrics and metric summaries
  through CloudWatch and through the protection pack (web ACL) page in the AWS WAF console. For information, see
  [Monitoring and tuning your AWS WAF protections](web-acl-testing-activities.md "web-acl-testing-activities.md").
