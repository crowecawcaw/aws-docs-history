

# Getting started with the AWS assistant
<a name="getting-started"></a>

Use the AWS assistant for general questions in the AWS Management Console and AWS Console Mobile Application. Available capabilities vary between the AWS Management Console and the AWS Console Mobile Application.

## Step 1: Access the AWS assistant
<a name="access-assistant"></a>

Choose where you want to use the AWS assistant.

------
#### [ AWS Management Console ]

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/).

1. Choose the AWS assistant icon in the unified navigation bar. The AWS assistant chat panel opens as a side panel.

1. Enter a question in the text field, and review the response and its source links.

------
#### [ AWS Console Mobile Application ]

1. Open the AWS Console Mobile Application.

1. Choose the AWS assistant icon.

1. Enter a question, and review the response and its source links.

------

## Step 2: Verify required permissions
<a name="permissions-overview"></a>

Your IAM identity needs permission to use the AWS assistant. The existing `AmazonQDeveloperAccess` AWS managed policy provides quick access to the base conversational features.

To chat, your IAM identity needs permission for `q:StartConversation`, `q:SendMessage`, `q:GetConversation`, and `q:ListConversations`. If one of these actions isn't allowed, you get a permissions error. For all AWS assistant permissions, see [Permissions reference for the AWS assistant](permissions-reference.md).

You need additional permissions when the AWS assistant accesses service APIs or resources on your behalf. These permissions can cover cost data, support cases, or customer managed AWS Key Management Service (AWS KMS) keys.

The AWS assistant does not give you access to resources or actions that your IAM identity cannot access. For example, to list Amazon Simple Storage Service (Amazon S3) buckets, your identity must have `s3:ListAllMyBuckets`.

For example policies, see [Identity-based policy examples for the AWS assistant](security-iam-examples.md).

## [Optional] Step 3: Review Pro tier access
<a name="subscription-access"></a>

If you already have an Amazon Q Developer Pro subscription and want to use Pro tier benefits in the AWS Management Console, use AWS IAM Identity Center. If your AWS IAM Identity Center identity has an active Amazon Q Developer Pro subscription, the subscription is available automatically.

Customer managed AWS KMS keys are available only with a Pro subscription. For more information, see [Key management](data-protection.md#key-management).

If you access the AWS Management Console with IAM or IAM federation, you might be prompted to authenticate with AWS IAM Identity Center. This prompt can appear after you reach a Free tier quota or use a Pro-only capability. For tier quotas, see [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/).

Note the following identity requirements:
+ The AWS assistant doesn't support AWS Builder ID.
+ Pro tier access in the AWS Management Console requires an organization instance of IAM Identity Center with identity-enhanced console sessions enabled. If your identity is in an account instance, you can use the Free tier only.
+ If you're subscribed to Amazon Q Developer Pro in the management account of an organization in AWS Organizations, you can use your subscription while signed in to a member account only if an administrator enables profile sharing. Otherwise, you use the Free tier in member accounts. For more information, see [Enabling profile sharing in Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-profile-sharing.html) in the *Amazon Q Developer User Guide*.

Normal AWS service charges can apply when the AWS assistant calls other services on your behalf.