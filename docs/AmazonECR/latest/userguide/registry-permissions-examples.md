# Private registry policy examples for

Amazon ECR

The following examples show registry permissions policy statements that you could
use to control the permissions that users have to your Amazon ECR registry.

###### Note

In each example, if the `ecr:CreateRepository` action is removed
from your registry policy, replication can still occur. However, for successful
replication, you need to create repositories with the same name within your
account.

## Example: Allow all IAM

principals in a source account to replicate all repositories

The following registry permissions policy allows all IAM principals (users and
roles) in a source account to replicate all repositories.

Note the following:

- **Important:** When you specify an
  AWS account ID as a principal in a policy, you grant access to all IAM
  users and roles within that account, not just the root user. This
  provides broad access across the entire account.
- **Security Consideration:** Account-level
  permissions grant access to all IAM entities in the specified account.
  For more restrictive access, specify individual IAM users, roles, or use
  condition statements to limit access further.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ReplicationAccessCrossAccount",
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`111122223333`:`root`"
 },
 "Action":[
 "ecr:CreateRepository",
 "ecr:ReplicateImage"
 ],
 "Resource": [
 "arn:aws:ecr:us-west-2:`444455556666`:repository/`*`"
 ]
 }
 ]
}`

```

## Example: Allow IAM

principals from multiple accounts

The following registry permissions policy has two statements. Each statement
allows all IAM principals (users and roles) in a source account to replicate all
repositories.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ReplicationAccessCrossAccount1",
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`111122223333`:root"
 },
 "Action":[
 "ecr:CreateRepository",
 "ecr:ReplicateImage"
 ],
 "Resource": [
 "arn:aws:ecr:us-west-2:`123456789012`:repository/*"
 ]
 },
 {
 "Sid":"ReplicationAccessCrossAccount2",
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`444455556666`:root"
 },
 "Action":[
 "ecr:CreateRepository",
 "ecr:ReplicateImage"
 ],
 "Resource": [
 "arn:aws:ecr:us-west-2:`123456789012`:repository/*"
 ]
 }
 ]
}`

```

## Example: Allow all IAM

principals in a source account to replicate all repositories with prefix
`prod-`.

The following registry permissions policy allows all IAM principals (users and
roles) in a source account to replicate all repositories that start with
`prod-`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ReplicationAccessCrossAccount",
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`111122223333`:`root`"
 },
 "Action":[
 "ecr:CreateRepository",
 "ecr:ReplicateImage"
 ],
 "Resource": [
 "arn:aws:ecr:us-west-2:`444455556666`:repository/`prod-*`"
 ]
 }
 ]
}`

```
