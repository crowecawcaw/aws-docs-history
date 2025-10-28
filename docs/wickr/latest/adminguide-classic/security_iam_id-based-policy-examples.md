This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Identity-based policy examples for

AWS Wickr

By default, a brand new IAM user has no permissions to do anything. An IAM
administrator must create and assign IAM policies that give users permission to
administer the AWS Wickr service. The following shows an example of a permissions
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "wickr:CreateAdminSession",
 "wickr:ListNetworks"
 ],
 "Resource": "*"
 }
 ]
}`

```

This sample policy gives users permissions to create, view, and manage Wickr networks
using the AWS Management Console for Wickr. To learn more about the elements within an IAM policy
statement, see [Identity-based
policies for Wickr](security_iam_service-with-iam-id-based-policies.md "security_iam_service-with-iam-id-based-policies.md"). To learn how to
create an IAM policy using these example JSON policy documents, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](security_iam_service-with-iam-policy-best-practices.md "security_iam_service-with-iam-policy-best-practices.md")
- [Using the
  AWS Management Console for Wickr](security_iam_id-based-policy-examples-console.md "security_iam_id-based-policy-examples-console.md")
- [Allow users
  to view their own permissions](security_iam_id-based-policy-examples-view-own-permissions.md "security_iam_id-based-policy-examples-view-own-permissions.md")
