# Customer managed policies

As a best practice, don't use your AWS account root user to interact with AWS, including
AWS Private CA. Instead use AWS Identity and Access Management (IAM) to create an IAM user, IAM role, or
federated user. Create an administrator group and add yourself to it. Then log in as
an administrator. Add additional users to the group as needed.

Another best practice is to create a customer managed IAM policy that you can
assign to users. Customer managed policies are standalone identity-based policies
that you create and which you can attach to multiple users, groups, or roles in your
AWS account. Such a policy restricts users to performing only the AWS Private CA
actions that you specify.

The following example [customer-managed policy](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") allows a user to create a CA audit report. This
is an example only. You can choose any AWS Private CA operations that you want. For more
examples, see [Inline policies](auth-InlinePolicies.md "auth-InlinePolicies.md").

###### To create a customer managed policy

1. Sign in to the IAM console using the credentials of an AWS
   administrator.
2. In the navigation pane of the console, choose
   **Policies**.
3. Choose **Create policy**.
4. Choose the **JSON** tab.
5. Copy the following policy and paste it into the editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"acm-pca:CreateCertificateAuthorityAuditReport",
 "Resource":"*"
 }
 ]
}`

```

6. Choose **Review policy**.
7. For **Name**, type `PcaListPolicy`.
8. (Optional) Type a description.
9. Choose **Create policy**.
   An administrator can attach the policy to any IAM user to limit what AWS Private CA
   actions the user can perform. For ways to apply a permissions policy, see [Changing Permissions for an
   IAM User](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the _IAM User Guide_.
