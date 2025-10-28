# Execution IAM policy

You can specify an Execution IAM Policy, in addition to an Execution Role, when submitting job runs on EMR Serverless. The resulting permissions assumed by the job run is the intersection of
the permissions in the Execution Role and the specified Execution IAM Policy.

## Getting Started

Steps to use Execution IAM policy::

Create an `emr-serverless` application or use an existing one and then run the following aws cli to start a job run
with an inline IAM policy:

```
aws emr-serverless start-job-run --region us-west-2 \
      --application-id `application-id` \
      --execution-role-arn `execution-role-arn` \
      --job-driver `job-driver-options` \
      --execution-iam-policy '{"policy": "`inline-policy`"}'
```

## CLI command examples

If we have the following policy stored in the `policy.json` file on the machine:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::my-test-bucket",
 "arn:aws:s3:::my-test-bucket/*"
 ],
 "Sid": "AllowS3Getobject"
 }
 ]
}`

```

Then we can start a job with this policy using the following AWS CLI command:

```
aws emr-serverless start-job-run --region us-west-2 \
      --application-id `application-id` \
      --execution-role-arn `execution-role-arn` \
      --job-driver `job-driver-options`
      --execution-iam-policy '{
          "policy": '$(jq -c '. | @json' policy.json)'
      }'
```

You can also use both AWS and Customer managed policies, specifying them through their ARNs:

```
aws emr-serverless start-job-run --region us-west-2 \
      --application-id `application-id` \
      --execution-role-arn `execution-role-arn` \
      --job-driver `job-driver-options`
      --execution-iam-policy '{
          "policyArns": [
          "arn:aws:iam::aws:policy/AmazonS3FullAccess",
          "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
          ]
    }'
```

It's possible to specify both an inline IAM policy and managed policy ARNs in the same request as well:

```
aws emr-serverless start-job-run --region us-west-2 \
      --application-id `application-id` \
      --execution-role-arn `execution-role-arn` \
      --job-driver `job-driver-options`
      --execution-iam-policy '{
          "policy": '$(jq -c '. | @json' policy.json)',
          "policyArns": [
          "arn:aws:iam::aws:policy/AmazonS3FullAccess",
          "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
          ]
      }'
```

## Important Notes

- The `execution-role-policy`'s `policy` field can have a maximum
  length of 2048 chars.
- The inline IAM policy string specified in the `execution-iam-policy`'s `policy` field has to conform to the json string
  standard, with no newlines and quotes escaped as in the preceding example.
- A list of up to 10 managed policy ARNs can be specified as a value to the `execution-iam-policy`'s `policyArns` field.
- Managed policy ARNs must be a list of valid AWS or Customer managed policy ARN, when a Customer managed policy ARN is specified, the policy must belong to the
  same AWS account of the EMR-S JobRun.
- When both inline IAM policy and managed policies are used, the plaintext that you use for the inline and managed policies combined
  can't exceed 2,048 characters.
- The resulting permissions assumed by the JobRun is the intersection of the permissions in the Execution Role and the
  specified Execution IAM Policy.

## Policy Intersection

The resulting permissions assumed by the job run is the intersection of the permissions in the Execution Role and the specified Execution IAM Policy. Which means any required permission will have to be specified in both places in order for JobRun to
work. However, it's possible to specify an additional blanket allow statement in the inline policy for any permissions that you don't intend to update or overwrite.

Example

Given the following execution IAM role policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:*"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowS3"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:123456789012:log-group::log-stream"
 ],
 "Sid": "AllowLOGSDescribeloggroups"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeTable"
 ],
 "Resource": [
 "arn:aws:dynamodb:*:*:table/MyCompany1table"
 ],
 "Sid": "AllowDYNAMODBDescribetable"
 }
 ]
}`

```

And the following inline IAM policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::my-test-bucket/tenant1",
 "arn:aws:s3:::my-test-bucket/tenant1/*"
 ],
 "Sid": "AllowS3Getobject"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:*",
 "dynamodb:*"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowLOGS"
 }
 ]
}`

```

The resulting permissions assumed by the JobRun is::

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::my-test-bucket/tenant1",
 "arn:aws:s3:::my-test-bucket/tenant1/*"
 ],
 "Sid": "AllowS3Getobject"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:123456789012:log-group::log-stream"
 ],
 "Sid": "AllowLOGSDescribeloggroups"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeTable"
 ],
 "Resource": [
 "arn:aws:dynamodb:*:*:table/MyCompany1table"
 ],
 "Sid": "AllowDYNAMODBDescribetable"
 }
 ]
}`

```
