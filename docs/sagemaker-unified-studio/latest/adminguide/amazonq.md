# Amazon Q in Amazon SageMaker Unified Studio

In the current release of Amazon SageMaker Unified Studio, by default, all users of an Amazon SageMaker unified
domain have access to the Free Tier release of Amazon Q.

Amazon Q Developer is an AI coding assistant that can chat about code, provide inline code
completions, and generate net new code. For more information, see [What is Amazon Q
Developer?](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md") in the Amazon Q Developer User Guide.

###### Topics

- [Enable Amazon Q Developer Pro](#amazonq-enable "#amazonq-enable")
- [Disable Amazon Q Developer Pro](#amazonq-disable "#amazonq-disable")
- [Troubleshooting Amazon Q in Amazon SageMaker Unified Studio](#amazonq-troubleshoot "#amazonq-troubleshoot")

## Enable Amazon Q Developer Pro

To enable Amazon Q Developer Pro in Amazon SageMaker Unified Studio, you must do the following:

- [Configure SSO user access to Amazon SageMaker Unified Studio for the users of
  your Amazon SageMaker unified domain](user-management.md "user-management.md").
- Subscribe to Amazon Q Developer Pro in the Amazon Q console in the same AWS Region and
  the same AWS account that you use for Amazon SageMaker Unified Studio. To do this, complete the following
  procedure:
  1.  Navigate to the [Amazon Q
      console](https://console.aws.amazon.com/amazonq "https://console.aws.amazon.com/amazonq").
  2.  Confirm that Amazon Q is connected to an instance of IAM Identity Center. This should be
      displayed on the Getting started page in the Connect to Identity Center section. If it is not
      connected, follow the steps in the Set up IAM Identity Center section in this guide.
  3.  On the **Subscriptions** page, choose
      **Subscribe**.
  4.  If you have not yet subscribed a user to Q, a popup window appears informing you that
      Amazon Q will create a managed application instance on your behalf. Choose **Create
      and subscribe to Q Developer Pro**.
  5.  A popup window appears inviting you to assign users and groups to Q for developer.
      Choose **Get started**.
  6.  In the search bar, type the first name of a user or the group name of a group you want
      to add to Q for developer. Then select the name of that user or group when it appears on the
      screen.
  7.  Repeat step 6 for all the users and groups that you want to have access to Q in
      Amazon SageMaker Unified Studio.
  8.  Choose **Assign**.

- Enable Amazon Q Developer Pro in the Amazon SageMaker management console. To do this,
  complete the following procedure.
  1.  Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
      navigation bar to choose the appropriate AWS Region.
  2.  Choose a domain where you want to enable Amazon Q Developer Pro and then on the domain's
      details page, choose the **Amazon Q** tab.
  3.  In the **Amazon Q** tab, expand the **Actions**
      drop-down and choose **Edit**.
  4.  On the **Edit Amazon Q subscription** page, choose **Q
      Developer Pro** and then choose **Update**.

## Disable Amazon Q Developer Pro

In order to disable Amazon Q in your domain, you must update your permissions to use deny
statements and update your domain level configuration. Do this by completing the following
steps:

- Update your permissions in the [AWS
  policy: SageMakerStudioDomainExecutionRolePolicy](security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md "security-iam-awsmanpol-SageMakerStudioDomainExecutionRolePolicy.md") to Deny
  “q:\*”.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "q:*",
 "glue:StartCompletion",
 "glue:GetCompletion"
 ],
 "Resource": "*"
 }
 ]
}`

```

- Update your permissions in the [AWS
  policy: SageMakerStudioProjectUserRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md "security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md") to Deny
  “q:\*”.

```

{
        "Sid": "AmazonQChatPermissions",
        "Effect": "Deny",
        "Action": [
            "q:*",
            "glue:StartCompletion",
           "glue:GetCompletion",
           "codewhisperer:GenerateRecommendations",
           "sqlworkbench:PutQCustomContext",
           "sqlworkbench:GetQCustomContext",
           "sqlworkbench:DeleteQCustomContext",
           "sqlworkbench:GetQSqlRecommendations",
           "sqlworkbench:GetQSqlPromptQuotas"
        ],
        "Resource": "*"
    },

```

- Update the Q setting in the domain level configuration.

```

arn:aws:ssm:<region>:<account-id>:parameter/amazon/datazone/q/<domain-id> to empty
arn:aws:ssm:<region>:<account-id>:parameter/amazon/datazone/q/<domain-id>/q-enabled to false

```

## Troubleshooting Amazon Q in Amazon SageMaker Unified Studio

This section lists potential issues you may encounter when configuring Amazon Q for use.
Follow the suggested steps to resolve the issues.

- **Amazon Q Q&A chat failing**

The Q&A chat may fail if you log-in using IAM Identity Center with an Amazon Q
subscription in a standalone account. This is because Q&A chat only supports subscriptions in
Organization accounts (management or member accounts). Only the free tier for Q&A is offered in
standalone accounts. In cases where the Amazon Q profile is in a different account than the
domain (e.g., Q in management, domain in member), you may need to provide the Q profile ARN
explicitly. We recommend the following actions:

    + It is recommended to keep the Q profile in the same account as the domain.
    + If using a management account for the Q profile in an organizational setup, be prepared
     to provide the Q profile ARN.
    + Allow up to 10 minutes for Q services to fully initialize after creating a Q
     profile.
