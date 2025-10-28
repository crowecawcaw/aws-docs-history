# Considerations for creating an Amazon MSK

Replicator

The following sections give an overview of the prerequisites, supported configurations, and best practices for using the MSK Replicator feature. It covers the necessary permissions, cluster compatibility, and Serverless-specific requirements, as well as guidance on managing the Replicator after creation.

## IAM

permissions required to create an MSK Replicator

Here is an example of the IAM policy required to create an MSK Replicator. The
action `kafka:TagResource` is only needed if tags are provided when
creating the MSK Replicator. Replicator IAM policies should be attached to the IAM
role that corresponds to your client. For information about creating authorization
policies, see [Create authorization policies](iam-access-control.md#create-iam-access-control-policies "iam-access-control.md#create-iam-access-control-policies").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MSKReplicatorIAMPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`123456789012`:role/`MSKReplicationRole`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "kafka.amazonaws.com"
 }
 }
 },
 {
 "Sid": "MSKReplicatorServiceLinkedRole",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::`123456789012`:role/aws-service-role/kafka.amazonaws.com/`AWSServiceRoleForKafka*`"
 },
 {
 "Sid": "MSKReplicatorEC2Actions",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeVpcs",
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1:`123456789012`:subnet/`subnet-0abcd1234ef56789`",
 "arn:aws:ec2:us-east-1:`123456789012`:security-group/`sg-0123abcd4567ef89`",
 "arn:aws:ec2:us-east-1:`123456789012`:network-interface/`eni-0a1b2c3d4e5f67890`",
 "arn:aws:ec2:us-east-1:`123456789012`:vpc/`vpc-0a1b2c3d4e5f67890`"
 ]
 },
 {
 "Sid": "MSKReplicatorActions",
 "Effect": "Allow",
 "Action": [
 "kafka:CreateReplicator",
 "kafka:TagResource"
 ],
 "Resource": [
 "arn:aws:kafka:us-east-1:`123456789012`:cluster/`myCluster`/`abcd1234-56ef-78gh-90ij-klmnopqrstuv`",
 "arn:aws:kafka:us-east-1:`123456789012`:replicator/`myReplicator`/`wxyz9876-54vu-32ts-10rq-ponmlkjihgfe`"
 ]
 }
 ]
}`

```

The following is an example IAM policy to describe replicator. Either the `kafka:DescribeReplicator` action or `kafka:ListTagsForResource` action is needed, not both.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "kafka:DescribeReplicator",
 "kafka:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```
