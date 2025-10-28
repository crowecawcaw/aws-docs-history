# IAM policy for CloudWatch Application Insights

To use CloudWatch Application Insights, you must create an [AWS Identity and Access Management (IAM) policy](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") and attach it to your user, group, or
role. For more information about users, groups, and roles, see [IAM Identities (users, user groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md"). The IAM policy
defines the user permissions.

###### To create an IAM policy using the console

To create an IAM policy using the IAM console, perform the following
steps.

1. Go to the [IAM
   console](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home"). In the left navigation pane, select
   **Policies**.
2. At the top of the page, select **Create policy**.
3. Select the **JSON** tab.
4. Copy and paste the following JSON document under the
   **JSON** tab.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "applicationinsights:*",
 "iam:CreateServiceLinkedRole",
 "iam:ListRoles",
 "resource-groups:ListGroups"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

5. Select **Review Policy**.
6. Enter a **Name** for the policy, for example,
   “AppInsightsPolicy.” Optionally, enter a
   **Description**.
7. Select **Create Policy**.
8. In the left navigation pane, select **User groups**, **Users**, or **Roles**.
9. Select the name of the user group, user, or role to which you would
   like to attach the policy.
10. Select **Add permissions**.
11. Select **Attach existing policies directly**.
12. Search for the policy that you just created, and select the check box to
    the left of the policy name.
13. Select **Next: Review**.
14. Make sure that the correct policy is listed, and select **Add
    permissions**.
15. Make sure that you log in with the user associated with the policy that
    you just created when you use CloudWatch Application Insights.

###### To create an IAM policy using the AWS CLI

To create an IAM policy using the AWS CLI, run the [create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md") operation from the command line using the JSON
document above as a file in your current folder.

###### To create an IAM policy using AWS Tools for Windows PowerShell

To create an IAM policy using the AWS Tools for Windows PowerShell, run the [New-IAMPolicy](../../../powershell/latest/reference/items/New-IAMPolicy.md "../../../powershell/latest/reference/items/New-IAMPolicy.md") cmdlt using the JSON document above as a file in your
current folder.
