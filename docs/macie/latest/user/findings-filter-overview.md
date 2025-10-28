# Filtering Macie findings

To perform targeted analysis and to analyze findings more efficiently, you can filter
Amazon Macie findings. With filters, you build custom views and queries for findings, which can
help you identify and focus on findings that have specific characteristics. Use the Amazon Macie
console to filter findings, or submit queries programmatically using the Amazon Macie API.

When you create a filter, you use specific attributes of findings to define criteria for
including or excluding findings from a view or from query results. A _finding attribute_ is a field that stores specific data for a finding, such as
severity, type, or the name of the S3 bucket that a finding applies to.

In Macie, a filter consists of one or more conditions. Each condition, also referred to as a
_criterion_, consists of three parts:

- An attribute-based field, such as **Severity** or **Finding
  type**.
- An operator, such as _equals_ or _not equals_.
- One or more values. The type and number of values depends on the field and operator that
  you choose.
  If you create a filter that you want to use again, you can save it as a _filter
  rule_. A _filter rule_ is a set of filter criteria that you
  create and save to reapply when you review findings on the Amazon Macie console.

You can also save a filter as a _suppression rule_. A
_suppression rule_ is a set of filter criteria that you create and save to
automatically archive findings that match the criteria of the rule. To learn about suppression
rules, see [Suppressing findings](findings-suppression.md "findings-suppression.md").

###### Topics

- [Filter fundamentals](findings-filter-basics.md "findings-filter-basics.md")
- [Fields for filtering
  findings](findings-filter-fields.md "findings-filter-fields.md")
- [Creating and applying
  filters](findings-filter-procedure.md "findings-filter-procedure.md")
- [Defining filter
  rules](findings-filter-rule-procedures.md "findings-filter-rule-procedures.md")
