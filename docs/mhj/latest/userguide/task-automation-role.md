AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# IAM roles for Migration Hub Journeys task

automation

###### Note

The task-automation feature is in preview release. It is available in
US East (N. Virginia).

This is pre-release documentation. Both the task-automation feature and this
documentation are subject to change.

Automated Migration Hub Journeys tasks require an account connection with an associated IAM
role that has the following trust policy and permissions policy.

For information about how to create an IAM role with these two policies, see
[Create a role using
custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md").

For information about how to associate an IAM role with an account connection,
see [Associating IAM roles with an AWS account
connection in AWS Migration Hub Journeys](associate-roles.md "associate-roles.md").

## Trust policy

The following trust policy allows Migration Hub Journeys to assume the role. To use this
trust policy, replace `account-connection-ARN` with the
ARN of a connection whose status is `Connected`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "journeys.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mgh:`us-east-1`:`111122223333`:connection/`connection-id`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "journeys.amazonaws.com"
 },
 "Action": "sts:TagSession"
 }
 ]
}`

```

To set a condition based on an AWS account ID instead of on a connection
ARN, you can use the following trust policy. However, keep in mind that this
policy is more permissive than the policy with a condition based on connection
ARN. The reason this trust policy is more permissive is that members of other
migration journeys that have connections to the same AWS account can use it to
run automation. Therefore, we recommend that you use the previous policy and set
the condition based on a specific connection, instead of on an
AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Principal": {
 "Service": "journeys.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringLike": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "journeys.amazonaws.com"
 },
 "Action": "sts:TagSession"
 }
 ]
 }`

```

###### Warning

Migration Hub Journeys no longer supports associating new IAM roles that have the
following trust policy. If you already have a connection with an associated
role that has the following trust policy, you can continue to use that role
to execute automated tasks until January 31, 2025.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "journeys.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:mgh:`us-east-1`:`111122223333`:connection/`connection-id`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "journeys.amazonaws.com"
 },
 "Action": "sts:TagSession"
 }
 ]
}`

```

## Permissions policy

The following permissions policy grants access to describe and run AWS Migration Hub
automation units.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "mgn:ListApplications",
 "mgn:ListWaves",
 "mgn:ListConnectors",
 "mgh:ListCreatedArtifacts",
 "mgh:ListAutomationUnits",
 "mgh:ListMigrationTaskUpdates",
 "mgh:DescribeAutomationUnit",
 "mgh:CreateAutomationRun",
 "mgh:DescribeAutomationRun",
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 }
 ]
}`

```
