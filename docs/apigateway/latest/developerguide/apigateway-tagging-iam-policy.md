# Using tags to control access to API Gateway REST API resources

Conditions in AWS Identity and Access Management policies are part of the syntax that you use to specify permissions to API Gateway
resources. For details about specifying IAM policies, see [Control access to a REST API with IAM permissions](permissions.md "permissions.md"). In API Gateway, resources can
have tags, and some actions can include tags. When you create an IAM policy, you can use tag condition keys to
control:

- Which users can perform actions on an API Gateway resource, based on tags that the resource already has.
- Which tags can be passed in an action's request.
- Whether specific tag keys can be used in a request.
  Using tags for attribute-based access control can allow for finer control than API-level control, as well as
  more dynamic control than resource-based access control. IAM policies can be created that allow or disallow an
  operation based on tags provided in the request (request tags), or tags on the resource that is being operated on
  (resource tags). In general, resource tags are for resources that already exist. Request tags are for when you're
  creating new resources.

For the complete syntax and semantics of tag condition keys, see [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User
Guide_.

The following examples demonstrate how to specify tag conditions in policies for API Gateway users.

## Limit actions based on resource tags

The following example policy grants users permission to perform all actions on all resources, as long as
those resources don't have the tag `Environment` with a value of `prod`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "apigateway:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "apigateway:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Environment": "prod"
 }
 }
 }
 ]
}`

```

## Allow actions based on resource tags

The following example policy allows users to perform all actions on API Gateway resources, as long as the
resources have the tag `Environment` with a value of `Development`. The `Deny` statement prevents the user from changing
the value of the `Environment` tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConditionallyAllow",
 "Effect": "Allow",
 "Action": [
 "apigateway:*"
 ],
 "Resource": [
 "arn:aws:apigateway:*::*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Environment": "Development"
 }
 }
 },
 {
 "Sid": "AllowTagging",
 "Effect": "Allow",
 "Action": [
 "apigateway:*"
 ],
 "Resource": [
 "arn:aws:apigateway:*::/tags/*"
 ]
 },
 {
 "Sid": "DenyChangingTag",
 "Effect": "Deny",
 "Action": [
 "apigateway:*"
 ],
 "Resource": [
 "arn:aws:apigateway:*::/tags/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "Environment"
 }
 }
 }
 ]
}`

```

## Deny tagging operations

The following example policy allows a user to perform all API Gateway actions, except for changing tags.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "apigateway:*"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "apigateway:*"
 ],
 "Resource": "arn:aws:apigateway:*::/tags*"
 }
 ]
}`

```

## Allow tagging operations

The following example policy allows a user to get all API Gateway resources, and change tags for those resources. To get the tags for a resource, the user must have `GET` permissions for that resource. To update the tags for a resource, the user must have
`PATCH` permissions for that resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "apigateway:GET",
 "apigateway:PUT",
 "apigateway:POST",
 "apigateway:DELETE"
 ],
 "Resource": [
 "arn:aws:apigateway:*::/tags/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "apigateway:GET",
 "apigateway:PATCH"
 ],
 "Resource": [
 "arn:aws:apigateway:*::*"
 ]
 }
 ]
}`

```
