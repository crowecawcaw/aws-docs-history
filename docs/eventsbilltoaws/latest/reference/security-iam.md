# Identity and Access Management for Bill to AWS

Bill to AWS uses IAM to control access to billing approval actions. You
must attach the IAM policy `ReInventTicketApprovalAccess` to the
approver's identity before they can view or approve charges.

If the approver attempts to review a charge without the policy attached, they
receive an "Authorization failed" error prompting them to contact their AWS
administrator to attach the `ReInventTicketApprovalAccess` policy.

## ReInventTicketApprovalAccess managed policy

AWS provides the `ReInventTicketApprovalAccess` managed policy
that grants permission to view re:Invent pass charge details and approve or
decline billing to AWS accounts. This policy grants the following permissions:

- `eventsbilltoaws:info` – View re:Invent pass charge details
- `eventsbilltoaws:approve` – Approve or decline re:Invent pass charges billed to the AWS account

For the full policy document, see
[ReInventTicketApprovalAccess](../../../aws-managed-policy/latest/reference/ReInventTicketApprovalAccess.md "../../../aws-managed-policy/latest/reference/ReInventTicketApprovalAccess.md").

## To attach the ReInventTicketApprovalAccess policy

### Using IAM (IAM users and roles)

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** or **Roles**.
3. Choose the name of the user or role for the designated approver.
4. Choose the **Permissions** tab, then choose **Add permissions**.
5. Choose **Attach policies directly**.
6. Search for `ReInventTicketApprovalAccess`, select the checkbox next to it, and choose **Next**.
7. Choose **Add permissions**.

### Using IAM Identity Center (recommended for organizations using SSO)

1. Open the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Permission sets**.
3. Select the permission set assigned to the designated approver.
4. Choose **Policies** → **Attach policies**.
5. Under **AWS managed policies**, search for `ReInventTicketApprovalAccess`, select it, and save.

## Policy updates

The following table describes updates to the AWS managed policy for Bill
to AWS.

| Policy updates for Bill to AWS              | Change                                                                                                                                              | Description   | Date |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---- |
| `ReInventTicketApprovalAccess` – New policy | Bill to AWS added a new managed policy that grants permission to view re:Invent pass charge details and approve or decline billing to AWS accounts. | June 10, 2026 |
| Bill to AWS started tracking policy changes | Bill to AWS started tracking changes for its AWS managed policies.                                                                                  | June 10, 2026 |
