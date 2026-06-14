# Bill to AWS for re:Invent

"Bill to AWS" allows attendees to bill re:Invent pass purchases directly to
their AWS account. An AWS account administrator must authorize the billing
by attaching the `ReInventTicketApprovalAccess` managed policy to
the approver's IAM identity.

## How the Bill to AWS payment flow works

1. An attendee registers for re:Invent and selects "Bill to AWS" as payment method.
2. An attendee provides their organization's AWS Account ID and Approver email.
3. The approver receives an email with a link to the AWS Management Console.
4. The approver signs in to the AWS Management Console and reviews the charge details.
5. The approver approves or declines the charge.
6. If approved, the ticket charge appears on the AWS account bill.

###### Note

The approver has 7 days to act on the request. If no action is taken,
the request expires and the attendee must resubmit.

## Prerequisites

Before an approver can review and approve Bill to AWS charges, complete the following:

- An active AWS account
- An IAM user, role, or IAM Identity Center permission set for the designated approver
- The `ReInventTicketApprovalAccess` managed policy attached to the approver's IAM identity

## Setting up authorization

To authorize an approver to review and act on Bill to AWS requests,
attach the `ReInventTicketApprovalAccess` AWS managed policy
to their IAM identity. For detailed instructions, see
[Identity and Access Management for Bill to AWS](security-iam.md "security-iam.md").
