# Delegations in AWS Audit Manager

As you navigate through the assessment process in AWS Audit Manager, you might encounter situations
where you need help from subject matter experts to review and validate the collected evidence.
This is where the concept of delegations comes into play.

## Key points

Delegations enable [audit owners](concepts.md#audit-owner "concepts.md#audit-owner") to
assign specific control sets to [delegates](concepts.md#delegate-persona "concepts.md#delegate-persona") –
individuals with specialized expertise in relevant areas. By using the delegation feature, you
can ensure that the evidence for each control is thoroughly evaluated by the appropriate
personnel. This helps you to streamline the review process and enhance the overall accuracy
and reliability of your assessments. Whether you need guidance on interpreting technical
evidence, clarifying compliance requirements, or gaining deeper insights into specific
domains, delegations enable you to collaborate effectively with subject matter experts.

At a high level, the delegation process is as follows:

1. The audit owner chooses a control set in their assessment and delegates it for
   review.
2. The delegate reviews those controls and their evidence, and submits the control set
   back to the audit owner when finished.
3. The audit owner is notified that the review is complete, and checks the reviewed
   controls for any remarks from the delegate.

###### Note

An AWS account can be an audit owner or a delegate in different AWS Regions.

## Additional resources

Use the following sections of this chapter to learn more about how to manage delegation
tasks in AWS Audit Manager.

- [Understanding the different delegation tasks for audit owners](delegate-for-audit-owners.md "delegate-for-audit-owners.md")
  - [Delegating a control set for review in AWS Audit Manager](delegation-for-audit-owners-delegating-a-control-set.md "delegation-for-audit-owners-delegating-a-control-set.md")
  - [Finding and reviewing the delegations that you've sent in AWS Audit Manager](delegation-for-audit-owners-reviewing-delegations.md "delegation-for-audit-owners-reviewing-delegations.md")
  - [Deleting your completed delegations in AWS Audit Manager](delegation-for-audit-owners-cancel-delegations.md "delegation-for-audit-owners-cancel-delegations.md")

- [Understanding the different delegation tasks for delegates](delegation-for-delegates.md "delegation-for-delegates.md")
  - [Viewing your notifications for incoming delegation requests](delegation-for-delegates-viewing-notifications.md "delegation-for-delegates-viewing-notifications.md")
  - [Reviewing the delegated control set and its related evidence](delegation-for-delegates-reviewing-control-set-and-evidence.md "delegation-for-delegates-reviewing-control-set-and-evidence.md")
  - [Adding comments about a control during a control set review](delegation-for-delegates-add-comment.md "delegation-for-delegates-add-comment.md")
  - [Marking a control as reviewed in AWS Audit Manager](delegation-for-delegates-changing-control-status.md "delegation-for-delegates-changing-control-status.md")
  - [Submitting a reviewed control set back to the audit owner](delegation-for-delegates-submitting-back-to-audit-owner.md "delegation-for-delegates-submitting-back-to-audit-owner.md")
