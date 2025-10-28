# Using tags in IAM policies

After you start tagging resources, you can define tag-based, resource-level permissions in
AWS Identity and Access Management (IAM) policies. By using tags in this way, you can implement granular
control of which users and roles in your AWS account have permission to create and tag
resources, and which users and roles have permission to add, edit, and remove tags more
generally. To control access based on tags, you can use [tag-related condition keys](../../../service-authorization/latest/reference/list_amazonsecuritylake.md#amazonsecuritylake-policy-keys "../../../service-authorization/latest/reference/list_amazonsecuritylake.md#amazonsecuritylake-policy-keys") in the [Condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of IAM policies.

For example, you can create a policy that allows a user to have full access to all
Amazon Security Lake resources, if the `Owner` tag for the resource specifies their
username:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ModifyResourceIfOwner",
 "Effect": "Allow",
 "Action": "securitylake:*",
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

If you define tag-based, resource-level permissions, the permissions take effect
immediately. This means that your resources are more secure as soon as they're created,
and you can quickly start enforcing the use of tags for new resources. You can also use
resource-level permissions to control which tag keys and values can be associated with
new and existing resources. For more information, see [Controlling access to AWS resources
using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.
