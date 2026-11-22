

# Getting support for AWS Marketplace

## Get answers and support in AWS Partner Central
<a name="get-support-seller"></a>

Sellers get help on the AWS Partner Central and Marketplace Support page in the AWS Partner Central console. On the Support page, you start a support chat in the AWS assistant panel. AWS Partner Central Agents answer your AWS Marketplace questions instantly. The answers draw on your seller account details and on AWS Partner Central and AWS Marketplace guides.

In the support chat, you can do the following:
+ Get answers about listings, offers, agreements, disbursements, and other AWS Marketplace topics, based on your seller account.
+ Create a support case when you need help from the AWS Marketplace support team. The chat fills in the case form, including the category, and you review and submit it.
+ Check the status of your cases, summarize case correspondence, reply to cases, and resolve cases.
+ Request an automated billing adjustment. The chat directs you to the **Agreements** page. For more information, see [Refunds and cancellations in AWS Marketplace](refunds.md).
+ Submit a Product Load Form for Intelligence Community Marketplace (ICMP) products. On the product creation page, choose the banner to open the support chat with your request filled in.

To use the Support page, your role needs the permissions in [Required permissions](#get-support-seller-permissions).

**To get answers in the support chat**

1. Open the Support page in the AWS Partner Central console at [https://us-east-1.console.aws.amazon.com/partnercentral/support](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).

1. Choose **Get support** to open the support chat in the AWS assistant panel.

1. In the AWS assistant chat, ask your question. Include any related identifiers, such as a product ID, offer ID, agreement ID, or invoice number.

1. Review the answer. To ask a follow-up question, enter it in the AWS assistant chat.

If an answer doesn't resolve your issue, the support chat helps you create a case for the AWS Marketplace support team. The chat asks for the details that the case needs and fills in the case form.

**To create a support case for AWS Marketplace**

1. In the support chat, describe your issue, and answer the questions that the chat asks.

   When the chat has the details that it needs, it displays a case form.

1. Review the case form. The chat fills in **Service**, **Category**, and **Sub-category** from your conversation. Update any fields that need changes.

1. Choose **Submit**.

   The chat displays your case ID. The case also appears on the **Active cases** tab of the Support page.

To track a case, reply to a case, or change the case list, see [Getting support](https://docs.aws.amazon.com/partner-central/latest/getting-started/getting-support.html) in the *AWS Partner Central Getting Started Guide*.

## Finding your AWS account number for customer support
<a name="GettingSupport"></a>

If you or your users need to contact Support, you need your AWS account number.

**To find your AWS account number**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/home) with your user name.

1. In the top navigation bar, choose your account name.

1. Copy the **Account ID** from the top of the menu.

Following are the support options available to sellers:


|  **Private Offers Success Team (POST)**  |  **Vendor Finance Success Team (VFS)**  |  **Managed Catalog Operations (MCO)**  |  **AWS Customer Service (AWS CS)**  | 
| --- | --- | --- | --- | 
| The POST team supports sellers, channel partners, and buyers with private offer operational enablement and support. | The VFS team improves processes that impact vendor finance cash application, reconciliation, and related reporting. The team also supports onboarding ISVs/CPs with finance specific questions regarding MPPOs and CPPOs (excluding public offers). | The MCO team is responsible for on-boarding third-party sellers of software onto the AWS Marketplace platform, They also support reviewing and processing software products for policy and compliance. | The AWS CS team is a specialized group of Technical Customer Support Associates and Specialists (TCSA/TCSS) who handle account and billing contacts related to AWS Marketplace services. | 
| **How to contact**<br />Use the Support page in the AWS Partner Central console. | **How to contact**<br />Use the Support page in the AWS Partner Central console. | **How to contact**<br />Use the Support page in the AWS Partner Central console. | **How to contact**<br />Use the [AWS Support Console](https://support.console.aws.amazon.com/support/home?). | 
| **Reasons to contact**+  Private offer creation enablement <br />+  Modifications to MPPOs via Agreement-Based Offers (ABO) <br />+  Private offer ad-hoc requests <br />+  CPPO re-drives  | **Reasons to contact**+  Disbursement questions <br />+  Late payments regarding MPPOs and CPPOs <br />+  Enablement invoice training, disbursements, and reporting  | **Reasons to contact**+  Onboarding support <br />+  Seller support and education <br />+  Seller and catalog quality and security <br />+  AMI permissions <br />+  Setting-up seller account information  | **Reasons to contact**+  Account and billing support <br />+  Switch to invoicing requests  | 

For refund and cancellation requests, choose **Get support** on the Support page.

**Note**  
To create cases in the AWS Support Console, you need AWS Support permissions. For more information, see [AWS Support identity-based policy examples](https://docs.aws.amazon.com/awssupport/latest/user/security_iam_id-based-policy-examples.html) in the *AWS Support User Guide*. For the permissions that the Support page needs, see [Required permissions](#get-support-seller-permissions).

## Required permissions
<a name="get-support-seller-permissions"></a>

To use the Support page, your AWS Identity and Access Management (IAM) role needs permissions to create and manage support cases. The support chat also checks whether your account is an AWS Marketplace seller. It uses this check to categorize your case.

If you use an AWS managed policy for AWS Marketplace or AWS Partner Central, you already have the right permissions. For more information, see [AWS managed policies for AWS Marketplace sellers](security-iam-awsmanpol.md).

If you use a customer managed policy, add the permissions in the following table. Make sure that your users are assigned to a role that has these permissions.

The following table lists each permission and what it allows on the Support page.


| Permission | What it allows | 
| --- | --- | 
| support:SearchForCases | List and search your cases on the Active cases and Resolved cases tabs, and list your cases in the support chat. | 
| support:DescribeCases | View case details and status, and confirm a case after you create it. | 
| support:DescribeCommunications | Read case correspondence and summarize it in the support chat. | 
| support:CreateCase | Create a support case. | 
| support:AddAttachmentsToSet | Attach files to a case. Without this permission, the case is created without attachments. | 
| support:AddCommunicationToCase | Reply to a case or submit a follow-up from the support chat. | 
| support:ResolveCase | Resolve a case. | 
| support-console:\* | View, reply to, and resolve your cases in AWS Support Center. | 
| aws-marketplace:ListEntities | Confirm that your account is an AWS Marketplace seller. | 

You can't scope these actions to specific resources, so each statement must use `"Resource": "*"`. If your account is also an AWS Partner, add `partnercentral:ListPartners`. For more information, see [Required permissions](https://docs.aws.amazon.com/partner-central/latest/getting-started/getting-support.html#support-permissions) in the *AWS Partner Central Getting Started Guide*.

The following example IAM policy grants the permissions that a seller needs. You can use it as written.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PartnerCentralAndMarketplaceSupportCases",
      "Effect": "Allow",
      "Action": [
        "support:SearchForCases",
        "support:DescribeCases",
        "support:DescribeCommunications",
        "support:CreateCase",
        "support:AddAttachmentsToSet",
        "support:AddCommunicationToCase",
        "support:ResolveCase"
      ],
      "Resource": "*"
    },
    {
      "Sid": "SupportCenterConsole",
      "Effect": "Allow",
      "Action": "support-console:*",
      "Resource": "*"
    },
    {
      "Sid": "MarketplaceSellerAccountCheck",
      "Effect": "Allow",
      "Action": "aws-marketplace:ListEntities",
      "Resource": "*"
    }
  ]
}
```