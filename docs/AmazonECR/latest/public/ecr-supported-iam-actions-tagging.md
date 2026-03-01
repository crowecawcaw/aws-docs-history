# Using tag-based access control in Amazon ECR public

The Amazon ECR Public `CreateRepository` API action enables you to specify tags
when you create the repository. For more information, see [Tag an Amazon ECR Public repository](ecr-public-using-tags.md "ecr-public-using-tags.md").

To enable users to tag repositories on creation, they must have permissions to use the
action that creates the resource (for example,
`ecr-public:CreateRepository`). If tags are specified in the
resource-creating action, AWS performs additional authorization on the
`ecr-public:CreateRepository` action to verify if users have permissions
to create tags.

You can used tag-based access control through IAM policies. The following are
examples.

The following policy would only allow an IAM user to create or tag a public
repository where the tag key is `environment` and tag value is
`dev`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowOnlyTagWithVals",
 "Effect": "Allow",
 "Action": [
 "ecr-public:CreateRepository",
 "ecr-public:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": [
 "dev"
 ]
 }
 }
 }
 ]
}`

```

The following policy would allow an IAM user access to all public repositories
unless they were tagged as `key=environment,value=prod`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ecr-public:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "ecr-public:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ecr:ResourceTag/environment": "prod"
 }
 }
 }
 ]
}`

```
