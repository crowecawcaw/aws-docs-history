# Service roles for AWS HealthOmics

A service role is an AWS Identity and Access Management (IAM) role that grants permissions for an AWS service to access resources in
your account. You provide a service role to AWS HealthOmics when you start an import job or start a run.

The HealthOmics console can create the required role for you. If you use the HealthOmics API to manage resources, create the
service role using the IAM console. For more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

Service roles must have the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The trust policy allows the HealthOmics service to assume the role.

###### Topics

- [Example IAM service policies](#permissions-service-samplepolicies "#permissions-service-samplepolicies")
- [Example CloudFormation template](#permissions-service-sampletemplates "#permissions-service-sampletemplates")

## Example IAM service policies

In these examples, resource names and account IDs are placeholders for you to replace with actual
values.

The following example shows the policy for a service role that you can use for starting a run. The policy
grants permissions to access the Amazon S3 output location, the workflow log group, and the Amazon ECR container for the
run.

###### Note

If you're using call caching for the run, add the run cache Amazon S3 location as a resource in the s3 permissions.

###### Example Service role policy for starting a run

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket1`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket1`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/omics/WorkflowLog:log-stream:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/omics/WorkflowLog:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchCheckLayerAvailability"
 ],
 "Resource": [
 "arn:aws:ecr:`us-east-1`:`123456789012`:repository/*"
 ]
 }
 ]
}`

```

The following example shows the policy for a service role that you can use for a store import job. The policy
grants permissions to access the Amazon S3 input location .

###### Example Service role for Reference store job

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },

 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 }

 ]
}`

```

## Example CloudFormation template

The following sample CloudFormation template creates a service role that gives HealthOmics permission to access Amazon S3 buckets that
have names prefixed with `omics-`, and to upload workflow logs.

###### Example Reference

store, Amazon S3 and CloudWatch Logs permissions

```
Parameters:
  bucketName:
    Description: Bucket name
    Type: String

Resources:
  serviceRole:
    Type: AWS::IAM::Role
    Properties:
      Policies:
        - PolicyName: read-reference
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action:
                - omics:*
              Resource: !Sub arn:${AWS::Partition}:omics:${AWS::Region}:${AWS::AccountId}:referenceStore/*
        - PolicyName: read-s3
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action:
                - s3:ListBucket
              Resource: !Sub arn:${AWS::Partition}:s3:::${bucketName}
            - Effect: Allow
              Action:
                - s3:GetObject
                - s3:PutObject
              Resource: !Sub arn:${AWS::Partition}:s3:::${bucketName}/*
        - PolicyName: upload-logs
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action:
                - logs:DescribeLogStreams
                - logs:CreateLogStream
                - logs:PutLogEvents
              Resource: !Sub arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:loggroup:/aws/omics/WorkflowLog:log-stream:*
            - Effect: Allow
              Action:
                - logs:CreateLogGroup
              Resource: !Sub arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:loggroup:/aws/omics/WorkflowLog:*
      AssumeRolePolicyDocument: |
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": [
                "sts:AssumeRole"
              ],
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "omics.amazonaws.com"
                ]
              }
            }
          ]
        }

```
