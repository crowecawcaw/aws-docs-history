# Required permissions

You need the following permissions to deploy a cluster with Terraform:

- assume the ParallelCluster API role, which is in charge of interacting with the
  ParallelCluster API
- describe the AWS CloudFormation stack of the ParallelCluster API to verify it exists and retrieve
  its parameters and outputs

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:sts::`111122223333`:role/PCAPIUserRole-*",
 "Effect": "Allow",
 "Sid": "AssumePCAPIUserRole"
 },
 {
 "Action": [
 "cloudformation:DescribeStacks"
 ],
 "Resource": "arn:aws:cloudformation:`us-east-1`:`111122223333`:stack/*",
 "Effect": "Allow",
 "Sid": "CloudFormation"
 }
 ]
}`

```
