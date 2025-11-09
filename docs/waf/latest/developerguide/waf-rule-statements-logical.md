**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using logical rule statements in AWS WAF

This section explains what a logical rule statement is and how it works.

Use logical rules statements to combine other statements or negate their
results. Every logical rule statement takes at least one nested
statement.

To logically combine or negate rule statement results, you nest the statements
under logical rule statements.

Logical rules statements are nestable. You can nest them inside other logical rule
statements and use them in scope-down statements. For information about scope-down
statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md "waf-rule-scope-down-statements.md").

###### Note

The visual editor on the console supports one level of rule statement nesting,
which works for many needs. To nest more levels, edit the JSON representation of
the rule on the console or use the APIs.

This table describes the logical rule statements and provides
guidelines for calculating protection pack (web ACL) capacity units (WCU) usage for each. For
information about WCUs, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").

| Logical Statement                                                               | Description                                   | WCUs                       |
| ------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------- |
| [AND<br>logic](waf-rule-statement-type-and.md "waf-rule-statement-type-and.md") | Combines nested statements with AND<br>logic. | Based on nested statements |
| [NOT<br>logic](waf-rule-statement-type-not.md "waf-rule-statement-type-not.md") | Negates the results of a nested statement.    | Based on nested statement  |
| [OR<br>logic](waf-rule-statement-type-or.md "waf-rule-statement-type-or.md")    | Combines nested statements with OR logic.     | Based on nested statements |
