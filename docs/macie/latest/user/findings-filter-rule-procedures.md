# Defining filter rules for Macie

findings

To perform consistent analysis of findings, you can create and apply filter rules. A
_filter rule_ is a set of filter criteria that you create and
save to use again when you review findings on the Amazon Macie console. Filter rules can help you
perform repeated, consistent analysis of findings that have specific characteristics. For
example, you might create one filter rule for analyzing all high-severity sensitive data
findings that report specific types of sensitive data. You might create another filter rule for
analyzing all high-severity policy findings for Amazon Simple Storage Service (Amazon S3) buckets that store unencrypted
objects.

When you create a filter rule, you use specific attributes of findings to define criteria
for including or excluding findings from a view. A _finding
attribute_ is a field that stores specific data for a finding, such as severity,
type, or the name of the S3 bucket that a finding applies to. You also specify a name, and,
optionally, a description of the rule. To then analyze findings that match the criteria of the
rule, choose the rule. Macie applies the rule's criteria and displays only those findings that
match the criteria. Macie also displays the criteria to help you determine which criteria it
applied.

Note that filter rules are different from suppression rules. A _suppression
rule_ is a set of filter criteria that you create and save to automatically archive
findings that match the criteria of the rule. Although both types of rules store and apply
filter criteria, a filter rule doesn't perform any action on findings that match the rule's
criteria. Instead, a filter rule only determines which findings appear on the console after you
apply the rule. For information about suppression rules, see [Suppressing findings](findings-suppression.md "findings-suppression.md").

###### Topics

- [Creating a filter rule](findings-filter-rule-create.md "findings-filter-rule-create.md")
- [Applying a filter rule](findings-filter-rule-apply.md "findings-filter-rule-apply.md")
- [Changing a filter rule](findings-filter-rule-change.md "findings-filter-rule-change.md")
- [Deleting a filter rule](findings-filter-rule-delete.md "findings-filter-rule-delete.md")
