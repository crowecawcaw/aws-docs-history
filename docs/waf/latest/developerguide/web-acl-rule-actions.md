**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How AWS WAF handles rule and rule group actions

This section explains how AWS WAF uses rules and rule groups to handle actions.

When you configure your rules and rule groups, you choose how you want AWS WAF to handle matching web requests:

- **Allow and Block are terminating actions** – Allow
  and Block actions stop all other processing of the protection pack (web ACL) on the matching
  web request. If a rule in a protection pack (web ACL) finds a match for a request and the rule
  action is Allow or Block, that match determines the final disposition of the
  web request for the protection pack (web ACL). AWS WAF doesn't process any other rules in the
  protection pack (web ACL) that come after the matching one. This is true for rules that you
  add directly to the protection pack (web ACL) and rules that are inside an added rule group.
  With the Block action, the protected resource doesn't receive or process the
  web request.
- **Count is a non-terminating action** – When a rule
  with a Count action matches a request, AWS WAF counts the request, then
  continues processing the rules that follow in the protection pack (web ACL) rule set.
- **CAPTCHA and Challenge can be non-terminating or terminating actions** – When a rule
  with one of these actions matches a request, AWS WAF checks its token status. If the request has a valid
  token, AWS WAF treats the match similar to a Count match, and then
  continues processing the rules that follow in the protection pack (web ACL) rule set. If the
  request doesn't have a valid token, AWS WAF terminates the evaluation and sends the client a CAPTCHA puzzle or silent background client session challenge to solve.
  If the rule evaluation doesn't result in any terminating action, then AWS WAF applies the protection pack (web ACL)
  default action to the request. For information, see [Setting the protection pack (web ACL) default action in AWS WAF](web-acl-default-action.md "web-acl-default-action.md").

In your protection pack (web ACL), you can override the action settings for rules inside a rule group and
you can override the action that's returned by a rule group. For
information, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").

###### Interaction between actions and priority settings

The actions that AWS WAF applies to a web request are affected by the numeric priority settings of the rules in
the protection pack (web ACL). For example, say that your protection pack (web ACL) has a rule with Allow action and a numeric priority of 50 and another
rule with Count action and a numeric priority of 100.
AWS WAF evaluates the rules in a protection pack (web ACL) in the order of their priority, starting from the lowest setting,
so it will evaluate the allow rule before the count rule.
A web request that matches both rules will match the allow rule first. Since
Allow is a terminating action, AWS WAF will stop the evaluation at this match and won't evaluate the request against
the count rule.

- If you only want to include requests that don't match the allow rule in your
  count rule metrics, then the priority settings of the rules would work.
- On the other hand, if you want count metrics from the count rule even for requests that match the allow rule,
  you'd need to give the count rule a lower numeric priority setting than the allow rule, so that it runs first.
  For more information about priority settings,
  see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").
