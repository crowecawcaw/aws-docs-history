**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS WAF Fraud Control account takeover prevention (ATP) examples

This section shows example configurations that satisfy common use cases for the
AWS WAF Fraud Control account takeover prevention (ATP) implementations.

Each example provides a description of the use case and then shows the solution in JSON listings for the custom configured rules.

###### Note

You can retrieve JSON listings like the ones shown in these examples through the console
protection pack (web ACL) JSON download or rule JSON editor, or through the `getWebACL`
operation in the APIs and the command line interface.

###### Topics

- [ATP example: Simple
  configuration](waf-atp-control-example-basic.md "waf-atp-control-example-basic.md")
- [ATP example: Custom
  handling for missing and compromised credentials](waf-atp-control-example-user-agent-exception.md "waf-atp-control-example-user-agent-exception.md")
- [ATP example: Response inspection
  configuration](waf-atp-control-example-response-inspection.md "waf-atp-control-example-response-inspection.md")
