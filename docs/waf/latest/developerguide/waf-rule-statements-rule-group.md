**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using rule group rule statements in AWS WAF

###### Note

Rule group rule statements are not nestable.

This section describes the rule group rule statements that you can use
in your protection pack (web ACL). Rule group protection pack (web ACL) capacity units (WCUs) are set by the
rule group owner at the time of creation. For
information about WCUs, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").

| Rule group statement                                                                                                                 | Description                                                                                                                                                                                                                                              | WCUs                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Using managed rule group statements](waf-rule-statement-type-managed-rule-group.md "waf-rule-statement-type-managed-rule-group.md") | Runs the rules that are defined in the specified managed rule group. You can narrow the scope of requests that the rule group evaluates by adding a scope-down statement. You can't nest a managed rule group statement inside any other statement type. | Defined by the rule group, plus any additional WCUs for a scope-down statement. |
| [Using rule group statements](waf-rule-statement-type-rule-group.md "waf-rule-statement-type-rule-group.md")                         | Runs the rules that are defined in a rule group that you manage. You can't add a scope-down statement to a rule group reference statement for your own rule group. You can't nest a rule group statement inside any other statement type                 | You define the WCU limit for the rule group when you create it.                 |
