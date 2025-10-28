# Using tags to control access to

AWS CodeConnections resources

Tags can be attached to the resource or passed in the request to services that support
tagging. In AWS CodeConnections, resources can have tags, and some actions can include
tags. When you create an IAM policy, you can use tag condition keys to control the
following:

- Which users can perform actions on a pipeline resource, based on tags that it
  already has.
- Which tags can be passed in an action's request.
- Whether specific tag keys can be used in a request.
  The following examples demonstrate how to specify tag conditions in policies for AWS
  CodeConnections users.

###### Example 1: Allow actions based on tags in the request

The following policy grants users permission to create connections in AWS
CodeConnections.

To do that, it allows the `CreateConnection` and
`TagResource` actions if the request specifies a tag named
`Project` with the value `ProjectA`. (The
`aws:RequestTag` condition key is used to control which tags can be
passed in an IAM request.) The `aws:TagKeys` condition ensures tag key
case sensitivity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateConnection",
 "codeconnections:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Project": "ProjectA"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["Project"]
 }
 }
 }
 ]
}`

```

###### Example 2: Allow actions based on resource tags

The following policy grants users permission to perform actions on, and get
information about, resources in AWS CodeConnections.

To do that, it allows specific actions if the pipeline has a tag named
`Project` with the value `ProjectA`. (The
`aws:RequestTag` condition key is used to control which tags can be
passed in an IAM request.) The `aws:TagKeys` condition ensures tag key
case sensitivity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeconnections:CreateConnection",
 "codeconnections:DeleteConnection",
 "codeconnections:ListConnections"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Project": "ProjectA"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": ["Project"]
 }
 }
 }
 ]
}`

```
