# Accessing

Amazon MSK clusters based on tags

You can use conditions in your identity-based policy to control access to
Amazon MSK resources based on tags. This example shows how you might create a
policy that allows the user to describe the cluster, get its bootstrap brokers, list
its broker nodes, update it, and delete it. However, permission is granted only if
the cluster tag `Owner` has the value of that user's user name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessClusterIfOwner",
 "Effect": "Allow",
 "Action": [
 "kafka:Describe*",
 "kafka:Get*",
 "kafka:List*",
 "kafka:Update*",
 "kafka:Delete*"
 ],
 "Resource": "arn:aws:kafka:us-east-1:012345678012:cluster/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Owner": "${aws:username}"
 }
 }
 }
 ]
}`

```

You can attach this policy to the IAM users in your account. If a user named
`richard-roe` attempts to update an MSK cluster, the
cluster must be tagged `Owner=richard-roe` or
`owner=richard-roe`. Otherwise, he is denied access. The condition
tag key `Owner` matches both `Owner` and `owner`
because condition key names are not case-sensitive. For more information, see [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
