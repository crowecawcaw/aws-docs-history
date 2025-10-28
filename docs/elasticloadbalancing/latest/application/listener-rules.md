# Listener rules for your Application Load Balancer

The listener rules for your Application Load Balancer determine how it routes requests to targets. When a
listener receives a request, it evaluates the request against each rule in priority order,
starting with the lowest numbered rule. Each rule includes conditions to be met and the
actions to perform when the conditions for the rule are met. This flexible routing mechanism
allows you to implement sophisticated traffic distribution patterns, support multiple
applications or microservices behind a single load balancer, and customize request handling
based on your application's specific requirements.

###### Rule basics

- Each rule consists of the following components: priority, actions, conditions, and
  optional transforms.
- Each rule action has a type and the information required to perform the
  action.
- Each rule condition has a type and the information required to evaluate the
  condition.
- Each rule transform has a regular expression to match and a replacement string.
- When you create a listener, you define actions for the default rule. The default
  rule can't have conditions or transforms. If none of the conditions for any other
  rules are met, then the action for the default rule is performed.
- Rules are evaluated in priority order, from the lowest value to the highest value.
  The default rule is evaluated last. You can't change the priority of the default
  rule.
- Each rule must include exactly one of the following actions: `forward`,
  `redirect`, or `fixed-response`, and it must be the last
  action to be performed.
- Each rule other than the default rule can optionally include one of the following
  conditions: `host-header`, `http-request-method`,
  `path-pattern`, and `source-ip`. It can also optionally
  include one or both of the following conditions: `http-header` and
  `query-string`.
- Each rule other than the default rule can optionally include one host header
  rewrite transform and one URL rewrite transform.
- You can specify up to three comparison strings per condition and up to five per
  rule.

###### Contents

- [Action types](rule-action-types.md "rule-action-types.md")
- [Condition types](rule-condition-types.md "rule-condition-types.md")
- [Transforms](rule-transforms.md "rule-transforms.md")
- [Add a rule](add-rule.md "add-rule.md")
- [Edit a rule](edit-rule.md "edit-rule.md")
- [Delete a rule](delete-rule.md "delete-rule.md")
