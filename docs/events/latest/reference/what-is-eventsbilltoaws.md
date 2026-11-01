

# Bill to AWS for re:Invent
<a name="what-is-eventsbilltoaws"></a>

 Bill to AWS allows attendees to bill re:Invent pass purchases directly to their AWS account. An AWS account administrator must authorize the billing by attaching the `ReInventTicketApprovalAccess` managed policy to the approver's AWS Identity and Access Management (IAM) identity. 

## How the Bill to AWS payment flow works
<a name="how-bill-to-aws-works"></a>

1. An attendee registers for re:Invent and selects **Bill to AWS** as the payment method.

1. The attendee provides their organization's AWS account ID and the approver's email address.

1. The approver receives an email with a link to the AWS Management Console.

1. The approver signs in to the AWS Management Console and reviews the charge details.

1. The approver approves or declines the charge.

1. If the charge is approved, it appears on the AWS account bill.

**Note**  
 The approver has 5 days to act on the request. If no action is taken, the request expires and the attendee must resubmit. 

## Prerequisites
<a name="prerequisites"></a>

 Before an approver can review and approve Bill to AWS charges, complete the following: 
+ An active AWS account
+ An IAM user, role, or AWS IAM Identity Center permission set for the designated approver
+ The `ReInventTicketApprovalAccess` managed policy attached to the approver's IAM identity

## Setting up authorization
<a name="setting-up-authorization"></a>

 To authorize an approver to review and act on Bill to AWS requests, attach the `ReInventTicketApprovalAccess` AWS managed policy to their IAM identity. For detailed instructions, see [Identity and Access Management for Bill to AWS](security-iam.md). 