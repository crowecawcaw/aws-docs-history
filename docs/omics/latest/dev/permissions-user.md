# Identity-based IAM policies for HealthOmics

To grant users in your account access to HealthOmics, you use identity-based policies in AWS Identity and Access Management (IAM).
Identity-based policies can apply directly to IAM users, or to IAM groups and roles that are associated with a
user. You can also grant users in another account permission to assume a role in your account and access your HealthOmics
resources.

To grant permission for users to perform actions on a workflow version, you must add the workflow and the
specific workflow version to the resource list.

The following IAM policy allows a user to access all HealthOmics API actions, and to pass [service roles](permissions-service.md "permissions-service.md") to HealthOmics.

###### Example User policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "omics.amazonaws.com"
 }
 }
 }
 ]
}`

```

When you use HealthOmics, you also interact with other AWS services. To access these services, use the managed
policies provided by each service. To restrict access to a subset of resources, you can use the managed policies as
a starting point to create your own more restrictive policies.

######

- [AmazonS3FullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess") – Access to Amazon S3 buckets and objects used by
  jobs.
- [AmazonEC2ContainerRegistryFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess") – Access to Amazon ECR registries and repositories for
  workflow container images.
- [AWSLakeFormationDataAdmin](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin") – Access to Lake Formation databases and tables created by analytics
  stores.
- [ResourceGroupsandTagEditorFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess") – Tag HealthOmics resources with HealthOmics tagging API
  operations.
  The preceding policies don't allow a user to create IAM roles. For a user with these permissions to run a job,
  an administrator must create the service role that grants HealthOmics permission to access data sources. For more
  information, see [Service roles for AWS HealthOmics](permissions-service.md "permissions-service.md").

## Define custom IAM permissions for runs

You can include any workflow, run, or run group referenced by the
`StartRun` request in an authorization request. To do so, list the
desired combination of workflows, runs, or run groups in the IAM policy. For example,
you can limit the use of a workflow to a specific run or run group. You can also specify
that a workflow only be used with a run group.

The following is an example IAM policy that allows a single workflow with a single
run group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:StartRun"
 ],
 "Resource": [
 "arn:aws:omics:us-west-2:123456789012:workflow/1234567",
 "arn:aws:omics:us-west-2:123456789012:runGroup/2345678"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "omics:StartRun"
 ],
 "Resource": [
 "arn:aws:omics:us-west-2:123456789012:run/*",
 "arn:aws:omics:us-west-2:123456789012:runGroup/2345678"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "omics:GetRun",
 "omics:ListRunTasks",
 "omics:GetRunTask",
 "omics:CancelRun",
 "omics:DeleteRun"
 ],
 "Resource": [
 "arn:aws:omics:us-west-2:123456789012:run/*"
 ]
 }
 ]
}`

```
