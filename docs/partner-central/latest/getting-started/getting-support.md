

# Getting support

The AWS Partner Central and Marketplace Support page in the AWS Partner Central console is where you get help with AWS Partner Network, AWS Partner Central, and AWS Marketplace questions. On the Support page, you start a support chat in the AWS assistant panel. AWS Partner Central Agents answer your questions instantly. The answers draw on your AWS Partner Central account details and on AWS Partner Central and AWS Marketplace guides.

In the support chat, you can do the following:
+ Get answers to AWS Partner Central and AWS Marketplace questions, based on your account details.
+ Create a support case when you need help from the AWS Partner Central or AWS Marketplace support team. The chat fills in the case form, and you review and submit it.
+ Check the status of your cases, summarize case correspondence, reply to cases, and resolve cases.
+ Request an automated billing adjustment. The chat directs you to the **Agreements** page. For more information, see [Refunds and cancellations in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/refunds.html) in the *AWS Marketplace Seller Guide*.

On the Support page, you can also track your cases on the **Active cases** and **Resolved cases** tabs. To use the Support page, your role needs the permissions in [Required permissions](#support-permissions).

## Get answers in the support chat
<a name="get-support-partner-central"></a>

Start with the support chat for any AWS Partner Central or AWS Marketplace question. Most questions get an answer without a support case.

**To get answers in the support chat**

1. Open the Support page in the AWS Partner Central console at [https://us-east-1.console.aws.amazon.com/partnercentral/support](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).

1. Choose **Get support**, or choose one of the suggested questions, such as **How much are listing fees?** To see other suggested questions, choose **Shuffle**.

   The support chat opens in the AWS assistant panel next to the Support page.

1. In the AWS assistant chat, ask your question, and then choose the send icon.

1. Review the answer. To ask a follow-up question, enter it in the AWS assistant chat.

To start a support chat from the case list, choose **Actions** on the **Active cases** tab, and then choose **Get support**.

**Note**  
AWS Partner Central doesn't save support chat conversations. To keep information from a conversation, copy it before you close the chat.

## Create a support case
<a name="how-support-chat-works"></a>

If an answer doesn't resolve your issue, the support chat helps you create a case for the AWS Partner Central or AWS Marketplace support team. The chat asks for the details that the case needs. AWS generative AI then fills in a case form from your conversation, and you review and submit it.

Before you start, open a support chat. For more information, see [Get answers in the support chat](#get-support-partner-central).

**To describe your issue**

1. In the AWS assistant chat, describe your issue. Include what's happening, when it started, and any related identifiers, such as an opportunity, fund request, listing, or invoice.

1. Answer the questions that the chat asks.

   When the chat has the details that it needs, it displays a case form.

**To review and submit the case form**

1. Review the case form, and update any fields that need changes. For a description of each field, see [Support case form fields](#support-case-form-fields).

1. If the chat can't predict the category of your issue, choose a **Category** and a **Sub-category**.

1. (Optional) To add files, choose **Choose files**.

1. (Optional) In **Additional email contacts**, enter up to 10 email addresses, separated by commas. If you aren't signed in as the AWS account root user, add your own email address so that you get case notifications.

1. Choose **Submit**.

   The chat displays **Support case created successfully** and your case ID. The case also appears on the **Active cases** tab of the Support page. To open the case in AWS Support Center, choose **View support case**.

### Support case form fields
<a name="support-case-form-fields"></a>

The following table describes each field on the case form.


| Field | Description | 
| --- | --- | 
| Subject | A short summary of your issue, from 1 to 250 characters. | 
| Description | The details of your issue, from 1 to 8,000 characters. | 
| Attachments | (Optional) Up to 3 files. Images can be up to 3.75 MB, and documents can be up to 4.5 MB. Supported file types are .doc, .docx, .xlsx, .png, .jpeg, .pdf, .csv, .txt, and .md. | 
| Case type | Always Partner Central and Marketplace. You can't change this field. | 
| Service | The area of your issue: APN Funding, AWS Partner Central, Commercial Marketplace, CRM Integration, European Sovereign Cloud Marketplace, or Intelligence Community Marketplace. | 
| Category | The topic within the service, for example ACE Leads and Opportunities. | 
| Sub-category | The specific issue within the category, for example General Opportunity or Lead Inquiries. | 
| Additional email contacts | (Optional) Up to 10 email addresses, separated by commas. These contacts receive AWS Support email notifications for the case. | 

## Track your support cases
<a name="track-support-cases"></a>

The Support page lists your AWS Partner Central and AWS Marketplace support cases. The **Active cases** tab lists open cases. The **Resolved cases** tab lists closed cases.

**To find a support case**

1. In the AWS Partner Central left navigation pane, choose **Support**.

1. Choose the **Active cases** or **Resolved cases** tab.

1. In **Find active cases** or **Find resolved cases**, enter a word from the case subject.

1. (Optional) On the **Active cases** tab, select a status from **Filter status**.

1. (Optional) To sort the list, choose a column heading. To get the latest case information, choose the refresh icon.

Active cases have one of the following statuses:
+ **Unassigned** – The case is waiting for a support engineer.
+ **Work in progress** – A support engineer is working on the case.
+ **Pending Amazon action** – The case is waiting for a response from AWS.
+ **Pending customer action** – The case is waiting for your response.
+ **Customer action completed** – You responded, and the case is waiting for AWS.
+ **Reopened** – The case was resolved and then opened again.

**To change how the case list displays**

1. On the **Active cases** or **Resolved cases** tab, choose the preferences icon.

1. For **Page size**, choose **10 cases**, **20 cases**, or **50 cases**.

1. For **Select visible columns**, select the columns that you want to see: **Status**, **Case ID**, and **Created (UTC)**. The **Subject** column always appears.

1. Choose **Confirm**.

To see all of your cases in AWS Support Center, choose **Actions**, and then choose **View all cases in AWS Support Center**.

## Reply to or resolve a support case
<a name="reply-support-case"></a>

You can reply to or resolve a support case in the support chat or in AWS Support Center. The support chat is the fastest option because you stay in AWS Partner Central. In the support chat, you can also ask for the status of a case or a summary of its correspondence.

**To reply to a support case in the support chat**

1. Start a support chat. For more information, see [Get answers in the support chat](#get-support-partner-central).

1. Enter your case ID, or ask the chat to list your open cases.

1. Ask the chat to submit a follow-up to the case, and enter your message.

1. Review the request, and then choose **Approve**. To cancel the request, choose **Dismiss**.

   The chat adds your reply to the case.

**Important**  
Include only the information that the support team needs to resolve your case. Case correspondence is visible to anyone who can view the case, so leave out credentials, credit card numbers, signed URLs, and personally identifiable information.

**To reply to a support case in AWS Support Center**

1. On the **Active cases** tab of the Support page, choose the case subject. The case opens in AWS Support Center in a new browser tab.

1. Under **Correspondence**, choose **Reply**.

1. In **Reply**, enter your message. You can enter up to 8,000 characters.

1. (Optional) To add files, choose **Choose file**. You can attach up to 10 files, and each file can be up to 150 MB.

1. (Optional) In **Additional contacts**, enter the email addresses of people to copy on case emails. Separate addresses with commas or semicolons. You can enter up to 10 addresses.

1. Choose **Submit**.

To read a response from AWS in another language, choose **Translate** under the response, and then choose a language. To rate a response, select a number of stars next to **Was this response helpful?**

**To resolve a support case in the support chat**

1. Start a support chat.

1. Enter your case ID, or ask the chat to list your open cases.

1. Ask the chat to resolve the case.

1. Review the request, and then choose **Approve**. To cancel the request, choose **Dismiss**.

**To resolve a support case in AWS Support Center**

1. On the **Active cases** tab of the Support page, choose the case subject.

1. In AWS Support Center, choose **Resolve case**.

After you resolve a case, it moves to the **Resolved cases** tab.

## Required permissions
<a name="support-permissions"></a>

To use the Support page, your AWS Identity and Access Management (IAM) role needs permissions to create and manage support cases. The support chat also checks whether your account is an AWS Partner or an AWS Marketplace seller. It uses this check to categorize your case.

If you use an AWS managed policy for AWS Partner Central or AWS Marketplace, you already have the right permissions. The exception is `AWSMarketplaceSellerProductsReadOnly`. With that policy, you can track your cases on the Support page, but you can't open one or reply to it. For more information, see [AWS managed policies for AWS Partner Central users](https://docs.aws.amazon.com/partner-central/latest/getting-started/managed-policies.html) and [AWS managed policies for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html).

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
| partnercentral:ListPartners | Confirm that your account is an AWS Partner. The support chat checks both the AWS and Sandbox catalogs, so the partnercentral:Catalog condition must allow both. Partners need this permission. | 
| aws-marketplace:ListEntities | Confirm that your account is an AWS Marketplace seller. Sellers need this permission. | 

You can't scope these actions to specific resources, so each statement must use `"Resource": "*"`. If your account is both an AWS Partner and an AWS Marketplace seller, include both `partnercentral:ListPartners` and `aws-marketplace:ListEntities`.

The following example IAM policy grants the permissions that a partner needs. You can use it as written.

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
      "Sid": "PartnerCentralAccountCheck",
      "Effect": "Allow",
      "Action": "partnercentral:ListPartners",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "partnercentral:Catalog": [
            "AWS",
            "Sandbox"
          ]
        }
      }
    }
  ]
}
```

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