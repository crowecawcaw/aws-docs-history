# Using Tag-Based Access Control

The Amazon ECR `CreateRepository` API action enables you to specify tags when you create the
repository. For more information, see [Tagging a private repository in Amazon ECR](ecr-using-tags.md "ecr-using-tags.md").

To enable users to tag repositories on creation, they must have permissions to use the
action that creates the resource (for example, `ecr:CreateRepository`). If tags
are specified in the resource-creating action, Amazon performs additional authorization on
the `ecr:CreateRepository` action to verify if users have permissions to create
tags.

You can use tag-based access control through IAM policies. The following are
examples.

The following policy would only allow a user to create or tag a repository as
`key=environment,value=dev`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateTaggedRepository",
 "Effect": "Allow",
 "Action": [
 "ecr:CreateRepository"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "dev"
 }
 }
 },
 {
 "Sid": "AllowTagRepository",
 "Effect": "Allow",
 "Action": [
 "ecr:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/environment": "dev"
 }
 }
 }
 ]
}`

```

The following policy would allow a user to pull images from all repositories unless they
were tagged as `key=environment,value=prod`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
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
