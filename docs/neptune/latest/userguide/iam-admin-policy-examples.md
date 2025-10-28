# Creating IAM administrative

policy statements for Amazon Neptune

## General administrative policy examples

The following examples show how to create Neptune administrative policies that
grant permissions to take various management actions on a DB cluster.

### Policy that prevents an IAM user

from deleting a specified DB instance

The following is an example policy that prevents an IAM user from deleting a
specified Neptune DB instance:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyDeleteOneInstance",
 "Effect": "Deny",
 "Action": "rds:DeleteDBInstance",
 "Resource": "arn:aws:rds:`us-west-2`:`123456789012`:db:`my-instance-name`"
 }
 ]
}`

```

### Policy that grants permission to

create new DB instances

The following is an example policy that allows an IAM user to create DB instances
in a specified Neptune DB cluster:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateInstance",
 "Effect": "Allow",
 "Action": "rds:CreateDBInstance",
 "Resource": "arn:aws:rds:`us-west-2`:`123456789012`:cluster:`my-cluster`"
 }
 ]
}`

```

### Policy that grants permission to

create new DB instances that use a specific DB parameter group

The following is an example policy that allows an IAM user to create DB instances
in a specified DB cluster (here `us-west-2`) in a specified Neptune DB cluster
using only a specified DB parameter group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateInstanceWithPG",
 "Effect": "Allow",
 "Action": "rds:CreateDBInstance",
 "Resource": [
 "arn:aws:rds:`us-west-2`:`123456789012`:cluster:`my-cluster`",
 "arn:aws:rds:`us-west-2`:`123456789012`:pg:`my-instance-pg`"
 ]
 }
 ]
}`

```

### Policy that grants permission to

describe any resource

The following is an example policy that allows an IAM user to describe any
Neptune resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDescribe",
 "Effect": "Allow",
 "Action": "rds:Describe*",
 "Resource": "*"
 }
 ]
}`

```

## Tag-based administrative policy examples

The following examples show how to create Neptune administrative policies that
tags to filter permissions for various management actions on a DB cluster.

### Example 1: Grant permission for actions

on a resource using a custom tag that can take multiple values

The policy below allows use of the `ModifyDBInstance`,
`CreateDBInstance` or `DeleteDBInstance` API on any DB
instance that has the `env` tag set to either `dev` or
`test`:

JSON

```
`{ "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDevTestAccess",
 "Effect": "Allow",
 "Action": [
 "rds:ModifyDBInstance",
 "rds:CreateDBInstance",
 "rds:DeleteDBInstance"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "rds:db-tag/env": [
 "dev",
 "test"
 ],
 "rds:DatabaseEngine": "neptune"
 }
 }
 }
 ]
}`

```

### Example 2: Limit the set of tag keys and

values that can be used to tag a resource

This policy uses a `Condition` key to allow a tag that has the key
`env` and a value of `test`, `qa`, or
`dev` to be added to a resource:

JSON

```
`{ "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowTagAccessForDevResources",
 "Effect": "Allow",
 "Action": [
 "rds:AddTagsToResource",
 "rds:RemoveTagsFromResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "rds:req-tag/env": [
 "test",
 "qa",
 "dev"
 ],
 "rds:DatabaseEngine": "neptune"
 }
 }
 }
 ]
}`

```

### Example 3: Allow full access to Neptune resources based on `aws:ResourceTag`

The following policy is similar to the first example above, but uses the
`aws:ResourceTag` instead:

JSON

```
`{ "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowFullAccessToDev",
 "Effect": "Allow",
 "Action": [
 "rds:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/env": "dev",
 "rds:DatabaseEngine": "neptune"
 }
 }
 }
 ]
}`

```
