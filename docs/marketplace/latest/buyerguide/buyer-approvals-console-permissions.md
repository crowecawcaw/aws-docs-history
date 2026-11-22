

# Permissions for approval requests in the AWS Marketplace console

To view, approve, or decline purchase approval requests in the AWS Marketplace console, IAM users and roles need the permissions in this topic. Who can do what depends on the account:
+ **View approval requests** – With the view permissions, IAM users and roles in a member account can view the approval requests from that account. IAM users and roles in your AWS management account or a delegated administrator account can view approval requests from every account in your organization.
+ **Approve, decline, or override approval requests** – Only IAM users and roles in your AWS management account or a delegated administrator account, with the approve and decline permissions.

Overriding a request uses the same permissions as approving or declining it. For more information, see [Overriding an approval request](buyer-approvals-requests-page.md#buyer-approvals-override).

**Note**  
Email approvers don't need an AWS account or IAM permissions. Requests routed to an external system are approved in that system, according to its own permissions. To configure approval rules, approval chains, and email approvers, use the `AWSPrivateMarketplaceAdminFullAccess` AWS managed policy. For more information, see [AWS managed policy: AWSPrivateMarketplaceAdminFullAccess](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess).

**Example: View approval requests**  
The `AWSMarketplaceManageSubscriptions` AWS managed policy includes the permissions to view approval requests. For more information, see [AWS managed policy: AWSMarketplaceManageSubscriptions](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsmarketplacemanagesubscriptions). To grant only view access, use a customer managed policy like the following one. It allows an IAM user or role to view purchase approval requests and the related agreement details. In a member account, the user or role can view only the requests from that account.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ViewMarketplaceApprovalRequests",
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:DescribeAgreement",
        "aws-marketplace:GetAgreementApproval",
        "aws-marketplace:GetAgreementRequest",
        "aws-marketplace:GetAgreementRequestTerms",
        "aws-marketplace:GetAgreementTerms",
        "aws-marketplace:ListAgreementApprovals",
        "aws-marketplace:ListAgreementRequests",
        "aws-marketplace:SearchAgreements"
      ],
      "Resource": "*"
    }
  ]
}
```

**Example: Approve, decline, or override approval requests**  
No AWS managed policy includes the permissions to approve or decline approval requests. To grant them, create a customer managed policy like the following one. It allows an IAM user or role in your management account or a delegated administrator account to view, approve, decline, and override purchase approval requests.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageMarketplaceApprovalRequests",
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:AcceptAgreementApproval",
        "aws-marketplace:DescribeAgreement",
        "aws-marketplace:GetAgreementApproval",
        "aws-marketplace:GetAgreementRequest",
        "aws-marketplace:GetAgreementRequestTerms",
        "aws-marketplace:GetAgreementTerms",
        "aws-marketplace:ListAgreementApprovals",
        "aws-marketplace:ListAgreementRequests",
        "aws-marketplace:RejectAgreementApproval",
        "aws-marketplace:SearchAgreements"
      ],
      "Resource": "*"
    }
  ]
}
```