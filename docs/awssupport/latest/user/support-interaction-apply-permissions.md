# Applying required permissions for support interactions

To apply permissions to your IAM users, complete the following steps:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, then choose **Create policy**.
3. Choose the **JSON** tab and paste one of the policy documents mentioned in the previous sections.
4. Choose **Next: Tags**, then **Next: Review**.
5. Enter a policy name such as `SupportConsoleInteractionsAccess` and provide a description that explains the policy's purpose.
6. Choose **Create policy**.
7. Attach the policy to your IAM users, groups, or roles that need access to the Support Center.
   If you have existing AWSSupportAccess managed policy attachments, then attach the supplementary custom policy alongside the managed policy.
