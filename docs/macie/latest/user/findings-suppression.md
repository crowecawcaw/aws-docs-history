# Suppressing Macie findings

To streamline your analysis of findings, you can create and use suppression rules. A
_suppression rule_ is a set of attribute-based filter
criteria that defines cases where you want Amazon Macie to archive findings automatically.
Suppression rules are helpful in situations where you've reviewed a class of findings and
don't want to be notified of them again.

For example, you might decide to allow S3 buckets to contain mailing addresses, if the
buckets don't allow public access and they encrypt new objects automatically with a
particular AWS KMS key. In this case, you can create a suppression rule that specifies
filter criteria for the following fields: **Sensitive data detection
type**, **S3 bucket public access permission**, and **S3
bucket encryption KMS key id**. The rule suppresses future findings that match
the filter criteria.

If you suppress findings with a suppression rule, Macie continues to generate findings for
subsequent occurrences of sensitive data and potential policy violations that match the
rule's criteria. However, Macie automatically changes the status of the findings to
_archived_. This means that the findings don't appear
by default on the Amazon Macie console, but they persist in Macie until they expire. Macie
stores findings for 90 days.

In addition, Macie doesn't publish suppressed findings to Amazon EventBridge as events or to AWS Security Hub CSPM.
Macie does, however, continue to create and store [sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md") that
correlate to sensitive data findings that you suppress. This helps ensure that you have an immutable history of sensitive data findings for data privacy and protection audits or investigations that you perform.

###### Note

If your account is part of an organization that centrally manages multiple Macie accounts,
suppression rules might work differently for your account. This depends on the category
of findings that you want to suppress, and whether you have a Macie administrator or member
account:

- **Policy findings** – Only a Macie administrator can suppress
  policy findings for the organization's accounts.

If you have a Macie administrator account and you create a suppression rule, Macie applies the rule
to policy findings for all the accounts in your organization unless you
configure the rule to exclude specific accounts. If you have a member account
and you want to suppress policy findings for your account, contact your
Macie administrator.

- **Sensitive data findings** – A Macie administrator and
  individual members can suppress sensitive data findings that their sensitive
  data discovery jobs produce. A Macie administrator can also suppress findings that Macie
  generates while performing automated sensitive data discovery for the organization.

Only the account that creates a sensitive data discovery job can suppress or otherwise
access sensitive data findings that the job produces. Only the Macie administrator
account for an organization can suppress or otherwise access findings that
automated sensitive data discovery produces for accounts in the organization.
For more information about the tasks that administrators and members can perform, see [Macie administrator and member account
relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

###### Topics

- [Creating a suppression
  rule](findings-suppression-rule-create.md "findings-suppression-rule-create.md")
- [Reviewing suppressed
  findings](findings-suppression-view-findings.md "findings-suppression-view-findings.md")
- [Changing a suppression
  rule](findings-suppression-rule-change.md "findings-suppression-rule-change.md")
- [Deleting a suppression
  rule](findings-suppression-rule-delete.md "findings-suppression-rule-delete.md")
