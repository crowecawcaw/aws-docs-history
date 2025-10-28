# Grant Users Permissions to Use Amazon Bedrock

and Generative AI Features in Canvas

Generative AI features in Amazon SageMaker Canvas are powered by Amazon Bedrock foundation models, which are large
language models (LLMs) that have the capability to understand and generate human-like text.
This page describes how to grant the permissions necessary for the following features
in SageMaker Canvas:

- [Chat with and compare Amazon Bedrock models](canvas-fm-chat.md "canvas-fm-chat.md"):
  Access and start conversational chats with Amazon Bedrock models through SageMaker Canvas.
- [Use the Chat for data prep feature in Data Wrangler](canvas-chat-for-data-prep.md "canvas-chat-for-data-prep.md") : Use natural language to explore, visualize, and transform your data. This feature is
  powered by Anthropic Claude 2.
- [Fine-tune Amazon Bedrock foundation models](canvas-fm-chat-fine-tune.md "canvas-fm-chat-fine-tune.md"):
  Fine-tune an Amazon Bedrock foundation model on your own data to receive customized responses.
  In order to use these features, you must first request access to the specific Amazon Bedrock model
  that you want to use. Then, add the necessary AWS IAM permissions and a trust relationship with
  Amazon Bedrock to the user's execution role. To grant the permissions to the role, you can choose one of the
  following methods:

- Create a new Amazon SageMaker AI domain or user profile and turn on Amazon Bedrock permissions. For more information, see
  [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md").
- Edit the settings for an existing Amazon SageMaker AI domain or user profile.
- Manually add permissions and a trust relationship to a domain's or user's IAM
  role.

## Step 1: Add Amazon Bedrock model access

Access to Amazon Bedrock models isn't granted by default, so you must go to the Amazon Bedrock console to
request access to models for your AWS account.

To learn how to request access to a specific Amazon Bedrock model, following the procedure to
**Add model access** on the page
[Manage access to Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md") in the _Amazon Bedrock User Guide_.

## Step 2: Grant permissions to the user's IAM role

When setting up your Amazon SageMaker AI domain or user profile, the user's IAM execution role
must have the [AmazonSageMakerCanvasBedrockAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md") policy attached, as well as a trust relationship with Amazon Bedrock,
so that your user can access Amazon Bedrock models from SageMaker Canvas.

You can modify the domain settings and either create a new execution role (to which SageMaker AI
attaches the required permissions for you) or specify an existing role.

Alternatively, you can manually modify the permissions for an existing IAM role through the IAM console.

Both methods are described in the following sections.

You can edit your domain or user profile settings to turn on the
**Canvas Ready-to-use models configuration** setting and specify an
Amazon Bedrock role.

To edit your domain settings and grant access to Amazon Bedrock models for Canvas users
in the domain, do the following:

1. Go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose **Domains**.
3. From the list of domains, choose your domain.
4. Choose the **App Configurations** tab.
5. In the **Canvas** section, choose **Edit**.
6. The **Edit Canvas settings** page opens. For the
   **Canvas Ready-to-use models configuration** section, do
   the following:
   1. Turn on the **Enable Canvas Ready-to-use models option**.
   2. For **Amazon Bedrock role**, select **Create and use a new
      execution role** to create a new IAM execution role that has the
      [AmazonSageMakerCanvasBedrockAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md") policy attached and a trust
      relationship with Amazon Bedrock. This IAM role is assumed by Amazon Bedrock when you access Amazon Bedrock models,
      use the chat for data prep feature, or fine-tune Amazon Bedrock models in Canvas. If you already have an execution role with a
      trust relationship, then select **Use an existing execution role**
      and choose your role from the dropdown.

7. Choose **Submit** to save your changes.
   Your users should now have the necessary permissions to access Amazon Bedrock models,
   use the chat for data prep feature, and fine-tune Amazon Bedrock models in Canvas.

You can use the same procedure above for editing an individual user’s settings, except
go into the individual user’s profile from the domain page and edit the user settings
instead. Permissions granted to an individual user don’t apply to other users in
the domain, while permissions granted through the domain settings apply to all user
profiles in the domain.

For more information on editing your domain settings, see [View and Edit domains](domain-view-edit.md "domain-view-edit.md").

You can manually grant users permissions to access and fine-tune Amazon Bedrock models in Canvas by
adding permissions to the IAM role specified for the domain or user’s profile. The
IAM role must have the [AmazonSageMakerCanvasBedrockAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md") policy attached and a trust relationship
with Amazon Bedrock.

The following section shows you how to attach the policy to your IAM role and create
the trust relationship with Amazon Bedrock.

First, take note of your domain or user profile’s IAM role. Note that permissions
granted to an individual user don’t apply to other users in the domain, while
permissions granted through the domain apply to all user profiles in the
domain.

To configure the IAM role and grant permissions to fine-tune foundation models in
Canvas, do the following:

1. Go to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**.
3. Search for the user's IAM role by name from the list of roles and select
   it.
4. On the **Permissions** tab, choose **Add
   permissions**. From the dropdown menu, choose **Attach
   policies**.
5. Search for the `AmazonSageMakerCanvasBedrockAccess` policy and select
   it.
6. Choose**Add permissions**.
7. Back on the IAM role’s page, choose the **Trust relationships**
   tab.
8. Choose **Edit trust policy**.
9. In the policy editor, find the **Add a principal option** in the
   right panel and choose **Add**.
10. In the dialog box, for **Principal type**, select **AWS
    services**.
11. For **ARN**, enter
    `bedrock.amazonaws.com`.
12. Choose **Add principal**.
13. Choose **Update policy**.
    You should now have an IAM role that has the
    [AmazonSageMakerCanvasBedrockAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasBedrockAccess.md") policy attached and a trust relationship
    with Amazon Bedrock. For information about AWS managed policies, see [Managed policies and
    inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _IAM User Guide_.
