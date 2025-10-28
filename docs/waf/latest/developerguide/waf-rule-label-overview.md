**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How labeling works in AWS WAF

This section explains how AWS WAF labels work.

When a rule matches a web request, if the rule has labels defined, AWS WAF adds the labels to
the request at the end of the rule evaluation. Rules that are evaluated after the
matching rule in the protection pack (web ACL) can match against the labels that the rule has added.

###### Who adds labels to requests

The protection pack (web ACL) components that evaluate requests can add labels to the requests.

- Any rule that isn't a rule group reference statement can add labels to matching web
  requests. The labeling criteria is part of the rule definition, and when a web
  request matches the rule, AWS WAF adds the rule's labels to the request. For
  information, see [AWS WAF rules that add labels](waf-rule-label-add.md "waf-rule-label-add.md").
- The geo match rule statement adds country and region labels to any request that it
  inspects, regardless of whether the statement results in a match. For
  information, see [Geographic match rule
  statement](waf-rule-statement-type-geo-match.md "waf-rule-statement-type-geo-match.md").
- The AWS Managed Rules for AWS WAF all add labels to requests that they inspect. They add some labels
  based on rule matches in the rule group and they add some based on AWS
  processes that the managed rule groups use, such as the token labeling added
  when you use an intelligent threat mitigation rule group. For information about the labels that
  each managed rule group adds, see [AWS Managed Rules rule groups list](aws-managed-rule-groups-list.md "aws-managed-rule-groups-list.md").

###### How AWS WAF manages labels

AWS WAF adds the rule's labels to the request at the end of the rule's inspection of the
request. Labeling is part of a rule's match activities, similar to the action.

Labels don't persist with the web request after the protection pack (web ACL) evaluation ends. In order for
other rules to match against a label that your rule adds, your rule action must not
terminate the evaluation of the web request by the protection pack (web ACL). The rule action must be set
to Count, CAPTCHA, or Challenge. When the protection pack (web ACL) evaluation
doesn't terminate, subsequent rules in the protection pack (web ACL) can run their label matching criteria
against the request. For more information about rule actions, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

###### Access to labels during protection pack (web ACL) evaluation

Once added, labels remain available on the request as long as AWS WAF is evaluating the
request against the protection pack (web ACL). Any rule in a protection pack (web ACL) can access labels that have been
added by the rules that have already run in the same protection pack (web ACL). This includes rules
that are defined directly inside the protection pack (web ACL) and rules defined inside rule groups
that are used in the protection pack (web ACL).

- You can match against a label in your rule's request inspection criteria using
  the label match statement. You can match against any label that's attached to
  the request. For statement details, see [Label match rule
  statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md").
- The geographic match statement adds labels with or without a match, but
  they're only available after the statement's containing protection pack (web ACL) rule has
  completed the request evaluation.
  - You can't use a single rule, for example a logical `AND` statement, to run a
    geo match statement followed by a label match statement against the
    geographic labels. You must put the label match statement in a separate
    rule that runs after the rule that contains the geo match statement.
  - If you use a geo match statement as a scope-down statement inside a rate-based rule
    statement or managed rule group reference statement, the labels that the
    geo match statement adds are not available for inspection by the
    containing rule's statement. If you need to inspect geographic labeling
    in a rate-based rule statement or a rule group, you must run the geo
    match statement in a separate rule that runs beforehand.

###### Access to label information outside of protection pack (web ACL) evaluation

Labels don't persist with the web request after the protection pack (web ACL) evaluation ends, but
AWS WAF records label information in the logs and in metrics.

- AWS WAF stores Amazon CloudWatch metrics for the first 100 labels on any single request.
  For information about accessing label metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") and
  [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").
- AWS WAF summarizes CloudWatch label metrics in the protection pack (web ACL) traffic overview dashboards in the
  AWS WAF console. You can access the dashboards on any protection pack (web ACL) page. For more
  information, see [Traffic overview dashboards for protection packs (web ACLs)](web-acl-dashboards.md "web-acl-dashboards.md").
- AWS WAF records labels in the logs for the first 100 labels on a request. You
  can use labels, along with the rule action, to filter the logs that AWS WAF
  records. For information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
  Your protection pack (web ACL) evaluation can apply more than 100 labels to a web request and match
  against more than 100 labels, but AWS WAF only records the first 100 in the logs and
  metrics.
