**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using scope-down statements in AWS WAF

This section explains what a scope-down statement and how it works.

A scope-down statement is a nestable rule statement that you add inside a managed rule
group statement or a rate-based statement to narrow the set of requests that the
containing rule evaluates. The containing rule only evaluates the requests that
first match the scope-down statement.

- **Managed rule group statement** – If you add a
  scope-down statement to a managed rule group statement, AWS WAF evaluates any
  request that doesn't match the scope-down statement as not matching the rule
  group. Only those requests that match the scope-down statement are evaluated
  against the rule group. For managed rule groups with pricing that's based on
  the number of requests evaluated, scope-down statements can help contain
  costs.

For more information about managed rule group statements, see [Using managed rule group
statements in AWS WAF](waf-rule-statement-type-managed-rule-group.md "waf-rule-statement-type-managed-rule-group.md").

- **Rate-based rule statement** – A rate-based rule
  statement without a scope-down statement rate limits all requests that the
  rule evaluates. If you want to only control the rate for a specific category
  of requests, add a scope-down statement to the rate-based rule. For example,
  to only track and control the rate of requests from a specific geographical
  area, you can specify that geographical area in a geographic match statement and
  add it to your rate-based rule as the scope-down statement.

For more information about rate-based rule statements, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").
You can use any nestable rule in a scope-down statement. For the available
statements, see [Using match rule statements in AWS WAF](waf-rule-statements-match.md "waf-rule-statements-match.md") and [Using logical rule statements in AWS WAF](waf-rule-statements-logical.md "waf-rule-statements-logical.md"). The WCUs for a scope-down
statement are the WCUs required for the rule statement that you define in it.
There's no additional cost for the use of a scope-down statement.

You can configure a scope-down statement in the same way as you do when you use the
statement in a regular rule. For example, you can apply text transformations to a
web request component that you're inspecting and you can specify a forwarded IP
address to use as the IP address. These configurations apply only to the scope-down
statement and are not inherited by the containing managed rule group or rate-based
rule statement.

For example, if you apply text transformations to a query string in your scope-down
statement, the scope-down statement inspects the query string after applying the
transformations. If the request matches the scope-down statement criteria, AWS WAF
then passes the web request to the containing rule in its original state, without
the scope-down statement's transformations. The rule that contains the scope-down
statement might apply text transformations of its own, but it doesn't inherit any
from the scope-down statement.

You can't use a scope-down statement to specify any request inspection
configuration for the containing rule statement. You can't use a scope-down
statement as a web request preprocessor for the containing rule statement. The only
role of a scope-down statement is to determine which requests are passed to the
containing rule statement for inspection.
