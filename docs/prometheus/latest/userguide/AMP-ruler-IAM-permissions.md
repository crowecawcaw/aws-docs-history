# Understanding IAM permissions needed for

using rules

You must give users permissions to use rules in Amazon Managed Service for Prometheus. Create an AWS Identity and Access Management (IAM)
policy with the following permissions, and assign the policy to your users, groups, or
roles.

###### Note

For more information about IAM, see [Identity and Access Management for Amazon Managed Service for Prometheus](security-iam.md "security-iam.md").

**Policy to give access to use rules**

The following policy gives access to use rules for all resources in your
account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aps:CreateRuleGroupsNamespace",
 "aps:ListRuleGroupsNamespaces",
 "aps:DescribeRuleGroupsNamespace",
 "aps:PutRuleGroupsNamespace",
 "aps:DeleteRuleGroupsNamespace"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Policy to give access to only one namespace**

You can also create policy that gives access to only specific policies. The following
sample policy gives access only to the `RuleGroupNamespace` specified. To use
this policy, replace `<account>`,
`<region>`,
`<workspace-id>`, and
`<namespace-name>` with appropriate values for your
account.
