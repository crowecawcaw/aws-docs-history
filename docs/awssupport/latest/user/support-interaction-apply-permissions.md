

# Applying required permissions for support interactions
<a name="support-interaction-apply-permissions"></a>

To apply permissions to your IAM users, complete the following steps:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**, then choose **Create policy**. 

1. Choose the **JSON** tab and paste one of the policy documents mentioned in the previous sections.

1. Choose **Next: Tags**, then **Next: Review**.

1. Enter a policy name such as `SupportConsoleInteractionsAccess` and provide a description that explains the policy's purpose.

1. Choose **Create policy**.

1. Attach the policy to your IAM users, groups, or roles that need access to the Support Center.

If you have existing AWSSupportAccess managed policy attachments, then attach the supplementary custom policy alongside the managed policy.