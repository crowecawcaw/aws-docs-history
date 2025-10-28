**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using rule statements in AWS WAF

This section explains how rule statements work.

Rule statements are the part of a rule that tells AWS WAF how to inspect a web request.
When AWS WAF finds the inspection criteria in a web request, we say that the web request
matches the statement. Every rule statement specifies what to look for and how,
according to the statement type.

Every rule in AWS WAF has a single top-level rule statement, which can contain other
statements. Rule statements can be very simple. For example, you could have a statement
that provides a set of originating countries to inspect your web requests for or you
could have a rule statement in a protection pack (web ACL) that just references a rule group. Rule
statements can also be very complex. For example, you could have a statement that
combines many other statements with logical AND, OR, and
NOT statements.

For most rules, you can add custom AWS WAF labeling to matching requests. The rules in the AWS Managed Rules rule groups
add labels to matching requests. The labels that a rule adds provide
information about the request to rules that are evaluated later in the protection pack (web ACL) and also in AWS WAF logs and metrics.
For information about labeling, see
[Web request labeling in AWS WAF](waf-labels.md "waf-labels.md")
and
[Label match rule
statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md").

###### Nesting rule statements

AWS WAF supports nesting for many rule statements, but not for all. For example, you
can't nest a rule group statement inside of another statement. You need to use
nesting for some scenarios, such as scope-down statements and logical statements.
The rule statement lists and rule details that follow describe the nesting
capabilities and requirements for each category and rule.

The visual editor for rules in the console supports only one level of nesting for rule
statements. For example, you can nest many types of statements inside a logical
AND or OR rule, but you can't nest another
AND or OR rule, because that requires a second level of
nesting. To implement multiple levels of nesting, provide the rule
definition in JSON, either through the JSON rule editor in the console or through the
APIs.

###### Topics

- [Adjusting rule statement settings in AWS WAF](waf-rule-statement-fields.md "waf-rule-statement-fields.md")
- [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md")
- [Referencing reusable entities in AWS WAF](waf-rule-statement-reusable-entities.md "waf-rule-statement-reusable-entities.md")
