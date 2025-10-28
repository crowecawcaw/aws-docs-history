# Passing role permissions

Part of a rule definition is an IAM role that grants permission to access resources
specified in the rule's action. The rules engine assumes that role when the rule's
action is invoked. The role must be defined in the same AWS account as the
rule.

When creating or replacing a rule you are, in effect, passing a role to the rules
engine. The `iam:PassRole` permission is required to perform this operation.
To verify that you have this permission, create a policy that grants the
`iam:PassRole` permission and attach it to your IAM user. The following
policy shows how to allow `iam:PassRole` permission for a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/myRole"
 ]
 }
 ]
}`

```

In this policy example, the `iam:PassRole` permission is granted for the
role `myRole`. The role is specified using the role's ARN. Attach this policy
to your IAM user or role that your user belongs to. For more information, see [Working with Managed
Policies](../../../service-authorization/latest/reference/access_policies_managed-using.md "../../../service-authorization/latest/reference/access_policies_managed-using.md").

###### Note

Lambda functions use resource-based policy, where the policy is attached directly
to the Lambda function itself. When you create a rule that invokes a Lambda function,
you don't pass a role, so the user creating the rule doesn't need the
`iam:PassRole` permission. For more information about Lambda function
authorization, see [Granting Permissions Using a Resource Policy](../../../lambda/latest/dg/intro-permission-model.md#intro-permission-model-access-policy "../../../lambda/latest/dg/intro-permission-model.md#intro-permission-model-access-policy").
