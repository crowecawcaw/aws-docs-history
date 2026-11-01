

# Identity and Access Management for Bill to AWS
<a name="security-iam"></a>

 Bill to AWS uses AWS Identity and Access Management (IAM) to control access to billing approval actions. You must attach the IAM policy `ReInventTicketApprovalAccess` to the approver's identity before they can view or approve charges. 

 If the approver attempts to review a charge without the policy attached, they receive an "Authorization failed" error prompting them to contact their AWS administrator to attach the `ReInventTicketApprovalAccess` policy. 

## ReInventTicketApprovalAccess managed policy
<a name="managed-policy-reinvent-ticket"></a>

 AWS provides the `ReInventTicketApprovalAccess` managed policy that grants permission to view re:Invent pass charge details and approve or decline billing to AWS accounts. This policy grants the following permissions: 
+ `eventsbilltoaws:info` – View re:Invent pass charge details
+ `eventsbilltoaws:approve` – Approve or decline re:Invent pass charges billed to the AWS account

 For the full policy document, see [ReInventTicketApprovalAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReInventTicketApprovalAccess.html). 

## Attaching the ReInventTicketApprovalAccess policy
<a name="attach-policy"></a>

You can attach the policy using IAM or AWS IAM Identity Center. Use the method that matches how you manage access to your account.<a name="attach-policy-iam"></a>

**To use IAM**

This method applies to IAM users and roles.

1. Open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users** or **Roles**.

1. Choose the name of the user or role for the designated approver.

1. Choose the **Permissions** tab, then choose **Add permissions**.

1. Choose **Attach policies directly**.

1. Search for `ReInventTicketApprovalAccess`, select the checkbox next to it, and choose **Next**.

1. Choose **Add permissions**.<a name="attach-policy-identity-center"></a>

**To use IAM Identity Center**

This method is recommended for organizations that use single sign-on.

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. In the navigation pane, choose **Permission sets**.

1. Select the permission set assigned to the designated approver.

1. Choose **Policies**, and then choose **Attach policies**.

1. Under **AWS managed policies**, search for `ReInventTicketApprovalAccess`, select it, and then choose **Save**.

## Policy updates
<a name="security-iam-awsmanpol-updates"></a>

 The following table describes updates to the AWS managed policy for Bill to AWS. 


| Change | Description | Date | 
| --- | --- | --- | 
| `ReInventTicketApprovalAccess` – New policy | Bill to AWS added a new managed policy that grants permission to view re:Invent pass charge details and approve or decline billing to AWS accounts. | June 10, 2026 | 
| Bill to AWS started tracking policy changes | Bill to AWS started tracking changes for its AWS managed policies. | June 10, 2026 | 